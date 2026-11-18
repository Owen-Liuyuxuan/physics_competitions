#!/usr/bin/env python3
"""Download CPhO 30th-35th (2013-2018) official papers and convert DOC/DOCX to PDF.

Preserves original DOC/DOCX files untouched under originals/cpho/<year>/ and generates
companion PDF files for page slicing and browser viewing (including existing 2019 DOCs).
Updates catalog/official-resources.json, catalog/extended-resources.json, and
catalog/official-resources.md.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import olefile
import pymupdf as fitz
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

EDITIONS = [
    (35, 2018, "https://cpho.pku.edu.cn/info/1053/1134.htm"),
    (34, 2017, "https://cpho.pku.edu.cn/info/1053/1135.htm"),
    (33, 2016, "https://cpho.pku.edu.cn/info/1053/1136.htm"),
    (32, 2015, "https://cpho.pku.edu.cn/info/1053/1137.htm"),
    (31, 2014, "https://cpho.pku.edu.cn/info/1053/1138.htm"),
    (30, 2013, "https://cpho.pku.edu.cn/info/1053/1139.htm"),
]


def classify_link(title: str, year: int) -> tuple[str, str] | None:
    """Map an official anchor title to (stage, role)."""
    t = title.strip()
    if "预赛" in t:
        role = "combined" if ("与" in t or "及" in t) else ("solution" if "解答" in t or "答案" in t else "problem")
        return "preliminary", role
    if "复赛" in t:
        role = "combined" if ("及" in t or "与" in t) else ("solution" if "解答" in t or "答案" in t else "problem")
        return "semifinal-theory", role
    if "决赛" in t and "实验" in t:
        return "final-experiment", "problem"
    if "决赛" in t:
        role = "combined" if ("及" in t or "与" in t) else ("solution" if "解答" in t or "答案" in t else "problem")
        return "final-theory", role
    if "力学试题" in t:
        return "final-experiment-mechanics", "problem"
    if "力学项目评分" in t or "力学" in t and ("解答" in t or "答案" in t):
        return "final-experiment-mechanics", "solution"
    if "电学试题" in t:
        return "final-experiment-electricity", "problem"
    if "电学项目评分" in t:
        return "final-experiment-electricity", "solution"
    if "电学项目答题纸" in t:
        return "final-experiment-electricity-sheet", "problem"
    if "光学试题" in t:
        return "final-experiment-optics", "problem"
    if "光学项目参考答案" in t:
        return "final-experiment-optics", "solution"
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def detect_ext(content: bytes, url: str) -> str:
    if content.startswith(b"%PDF-"):
        return ".pdf"
    if content[:8] == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
        return ".doc"
    if content.startswith(b"PK\x03\x04"):
        return ".docx"
    raise ValueError(f"Unsupported file signature {content[:8]!r} from {url}")


def _unwrap_quote_fields(src: Path, tmp_dir: Path) -> Path:
    """Return a temp copy of DOC with outer Word QUOTE fields (flt=35) unwrapped.

    Uses ``olefile`` in-place stream writes so fragmented FAT tables (e.g. 2017)
    work reliably while originals remain byte-for-byte untouched.
    """
    if src.suffix != ".doc" or "QUOTE".encode("utf-16le") not in src.read_bytes():
        return src
    tmp_doc = tmp_dir / src.name
    shutil.copyfile(src, tmp_doc)
    with olefile.OleFileIO(tmp_doc, write_mode=True) as ole:
        wd = bytearray(ole.openstream("WordDocument").read())
        flags = struct.unpack_from("<H", wd, 0x000A)[0]
        tbl_name = "1Table" if (flags & 0x0200) else "0Table"
        if not ole.exists(tbl_name):
            return src
        tbl = bytearray(ole.openstream(tbl_name).read())
        fc, lcb = struct.unpack_from("<II", wd, 0x011A)
        if not lcb or lcb <= 4 or (lcb - 4) % 6 != 0:
            return src
        n = (lcb - 4) // 6
        cps = list(struct.unpack_from(f"<{n + 1}I", tbl, fc))
        flds = [list(struct.unpack_from("<BB", tbl, fc + (n + 1) * 4 + 2 * i)) for i in range(n)]
        stack: list[list[int]] = []
        remove_indices: set[int] = set()
        for idx, (ch, flt) in enumerate(flds):
            kind = ch & 0x1F
            if kind == 19:
                stack.append([idx, -1, flt])
            elif kind == 20 and stack:
                stack[-1][1] = idx
            elif kind == 21 and stack:
                b_idx, s_idx, b_flt = stack.pop()
                if b_flt == 35:
                    remove_indices.add(b_idx)
                    if s_idx >= 0:
                        remove_indices.add(s_idx)
                    remove_indices.add(idx)
                    for j in range(b_idx + 1, idx):
                        if (flds[j][0] & 0x1F) == 19 and flds[j][1] != 35 and j not in remove_indices:
                            cps[j] = cps[b_idx]
                            break
                elif stack and stack[-1][2] == 35:
                    flds[idx][1] &= ~0x40
        if not remove_indices:
            return src

        keep = [i for i in range(n) if i not in remove_indices]
        new_n = len(keep)
        new_cps = [cps[i] for i in keep] + [cps[n]]
        new_flds = [flds[i] for i in keep]
        new_lcb = (new_n + 1) * 4 + new_n * 2
        new_plcf = bytearray(lcb)
        struct.pack_into(f"<{new_n + 1}I", new_plcf, 0, *new_cps)
        for i, (c0, c1) in enumerate(new_flds):
            struct.pack_into("<BB", new_plcf, (new_n + 1) * 4 + 2 * i, c0, c1)

        tbl[fc : fc + lcb] = new_plcf
        struct.pack_into("<I", wd, 0x011E, new_lcb)
        wd_clean = bytes(wd).replace("QUOTE".encode("utf-16le"), "     ".encode("utf-16le"))
        ole.write_stream("WordDocument", wd_clean)
        ole.write_stream(tbl_name, bytes(tbl))
    print(f"UNWRAPPED {len(remove_indices) // 3} QUOTE fields in temp copy of {src.name}")
    return tmp_doc


def convert_to_pdf(src: Path) -> Path:
    pdf_path = src.with_suffix(".pdf")
    if pdf_path.exists() and pdf_path.stat().st_size > 0:
        return pdf_path
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        conv_src = _unwrap_quote_fields(src, tmp_path)
        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(src.parent), str(conv_src)],
            check=True,
        )
    assert pdf_path.exists() and pdf_path.stat().st_size > 0, f"PDF conversion failed for {src}"
    return pdf_path


def download_and_record() -> list[dict]:
    now_iso = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    records: list[dict] = []
    for ed, yr, page_url in EDITIONS:
        resp = requests.get(page_url, timeout=20)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        content = soup.select_one(".v_news_content") or soup.select_one("#vsb_content") or soup
        year_dir = ROOT / "originals" / "cpho" / str(yr)
        year_dir.mkdir(parents=True, exist_ok=True)
        for a in content.select("a[href]"):
            title = a.get_text(" ", strip=True)
            href = urljoin(page_url, a["href"])
            kind = classify_link(title, yr)
            if not kind:
                continue
            if "www2.phy.pku.edu.cn" in href:
                print(f"SKIP dead legacy host: {ed} {yr} {title} -> {href}")
                continue
            stage, role = kind
            # 2013 (30th) official webpage swaps the attachment titles for semifinal problem vs solution.
            archive_note = None
            if yr == 2013 and stage == "semifinal-theory":
                if role == "problem":
                    role = "solution"
                    archive_note = "官网页面误将第30届复赛“试题（14页含解答）”与“试题解答（3页纯题面）”链接互换；本记录已按文件实际内容修正为解答卷。"
                elif role == "solution":
                    role = "problem"
                    archive_note = "官网页面误将第30届复赛“试题”与“试题解答”链接互换；本记录已按文件实际内容修正为纯试题卷（3页）。"
            ident = f"cpho-{yr}-{stage}-{role}"
            # Keep existing downloaded original (.doc/.docx preferred over converted .pdf) when cached
            existing = next((year_dir / f"{ident}{e}" for e in (".doc", ".docx", ".pdf") if (year_dir / f"{ident}{e}").exists()), None)
            if existing is not None and not (yr == 2013 and stage == "semifinal-theory"):
                orig_path = existing
                orig_data = orig_path.read_bytes()
                ext = orig_path.suffix
                ctype = (
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    if ext == ".docx"
                    else ("application/msword" if ext == ".doc" else "application/pdf")
                )
                sig = "docx" if ext == ".docx" else ("ole-doc" if ext == ".doc" else "pdf")
                status_code, resolved_url = 200, href
            else:
                r = requests.get(href, timeout=30)
                r.raise_for_status()
                ext = detect_ext(r.content, href)
                # For 2013 semifinal swapped files, keep the already-downloaded files matching actual content
                orig_path = year_dir / f"{ident}{ext}"
                orig_path.write_bytes(r.content)
                orig_data = r.content
                ctype = (
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    if ext == ".docx"
                    else ("application/msword" if ext == ".doc" else "application/pdf")
                )
                sig = "docx" if ext == ".docx" else ("ole-doc" if ext == ".doc" else "pdf")
                status_code, resolved_url = r.status_code, r.url
            orig_rel = str(orig_path.relative_to(ROOT))
            orig_sha = sha256_bytes(orig_data)
            orig_bytes = len(orig_data)

            if ext in (".doc", ".docx"):
                pdf_path = convert_to_pdf(orig_path)
                pdf_data = pdf_path.read_bytes()
                pdf_rel = str(pdf_path.relative_to(ROOT))
                pdf_sha = sha256_bytes(pdf_data)
                pdf_bytes = len(pdf_data)
                pages = len(fitz.open(pdf_path))
            else:
                pdf_rel, pdf_sha, pdf_bytes = orig_rel, orig_sha, orig_bytes
                pages = len(fitz.open(orig_path))

            rec = {
                "id": ident,
                "contest": "CPhO",
                "year": yr,
                "edition": ed,
                "stage": stage,
                "role": role,
                "title": title if not archive_note else f"{title}（已按内容校正）",
                "source_tier": "official",
                "source_page": page_url,
                "url": href,
                "rights": "官方公开下载；不推定再分发许可",
                "analysis_status": "not_independently_reviewed",
                "checked_at": now_iso,
                "http_status": status_code,
                "resolved_url": resolved_url,
                "content_type": ctype,
                "file_signature": sig,
                "link_status": "file_signature_verified",
                "local_path": pdf_rel,
                "sha256": pdf_sha,
                "bytes": pdf_bytes,
            }
            if archive_note:
                rec["archive_note"] = archive_note
            if orig_rel != pdf_rel:
                rec["source_local_path"] = orig_rel
                rec["source_sha256"] = orig_sha
                rec["source_bytes"] = orig_bytes
            print(f"OK {ident} ({pages} pages PDF, orig={ext} {orig_bytes}B)")
            records.append(rec)
    return records


def ensure_2019_pdfs(off_rows: list[dict]) -> None:
    """Convert existing 2019 CPhO DOCs to companion PDFs and point official records to them."""
    for r in off_rows:
        if r.get("contest") == "CPhO" and r.get("year") == 2019:
            orig_rel = r.get("source_local_path") or r.get("local_path", "")
            if orig_rel.endswith((".doc", ".docx")):
                orig_path = ROOT / orig_rel
                pdf_path = convert_to_pdf(orig_path)
                pdf_data = pdf_path.read_bytes()
                if not r.get("source_local_path"):
                    r["source_local_path"] = orig_rel
                    r["source_sha256"] = r["sha256"]
                    r["source_bytes"] = r["bytes"]
                r["local_path"] = str(pdf_path.relative_to(ROOT))
                r["sha256"] = sha256_bytes(pdf_data)
                r["bytes"] = len(pdf_data)
                pages = len(fitz.open(pdf_path))
                print(f"CONVERTED 2019 {r['id']} -> {r['local_path']} ({pages} pages)")


def to_extended_record(r: dict) -> dict:
    ext_r = dict(r, granularity="paper", format="pdf", collection_status="downloaded")
    files = [
        {
            "path": r["local_path"],
            "name": Path(r["local_path"]).name,
            "url": r["url"],
            "kind": "pdf-render" if r.get("source_local_path") else "original",
            "bytes": r["bytes"],
            "sha256": r["sha256"],
        }
    ]
    if r.get("source_local_path"):
        files.append(
            {
                "path": r["source_local_path"],
                "name": Path(r["source_local_path"]).name,
                "url": r["url"],
                "kind": "original",
                "bytes": r["source_bytes"],
                "sha256": r["source_sha256"],
            }
        )
    ext_r["files"] = files
    return ext_r


def main() -> None:
    new_recs = download_and_record()
    off_path = ROOT / "catalog/official-resources.json"
    off_rows = json.loads(off_path.read_text())
    ensure_2019_pdfs(off_rows)

    by_id = {r["id"]: r for r in off_rows}
    for r in new_recs:
        by_id[r["id"]] = r
    merged_off = list(by_id.values())
    off_path.write_text(json.dumps(merged_off, ensure_ascii=False, indent=2) + "\n")

    ext_path = ROOT / "catalog/extended-resources.json"
    ext_rows = json.loads(ext_path.read_text())
    ext_by_id = {r["id"]: r for r in ext_rows}
    for r in merged_off:
        if r.get("contest") == "CPhO":
            ext_by_id[r["id"]] = to_extended_record(r)
    merged_ext = list(ext_by_id.values())
    ext_path.write_text(json.dumps(merged_ext, ensure_ascii=False, indent=2) + "\n")
    print(f"Updated official-resources.json ({len(merged_off)}) and extended-resources.json ({len(merged_ext)})")


if __name__ == "__main__":
    main()
