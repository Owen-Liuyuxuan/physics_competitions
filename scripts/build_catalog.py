#!/usr/bin/env python3
"""Build a provenance-first physics contest link catalogue (no PanPhO mirroring).

Requires requests and beautifulsoup4. Run from any directory. Generated files
live in this script's parent directory; existing teaching pages are untouched.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urljoin
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
PAN = "https://panpearl-phys.hkust.edu.hk/info-album.html"
CPHO = {2019: "1264", 2020: "1308", 2021: "1309"}


def soup(url: str) -> BeautifulSoup:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def pan_rows() -> list[dict]:
    page = soup(PAN)
    tables = [t for t in page.select("table.album-a, table.album-b")
              if "年份" in t.find("tr").get_text()]
    rows = []
    for table in tables:
        # The comprehensive and mechanics tables have distinct headers.
        header = table.find("tr").get_text(" ", strip=True)
        mechanics = "相片集" not in header
        for tr in table.find_all("tr", recursive=False) or table.select("tbody > tr"):
            cells = tr.find_all("td", recursive=False)
            if len(cells) < 3:
                continue
            match = re.search(r"20\d{2}", cells[0].get_text())
            if not match or not 2019 <= int(match[0]) <= 2026:
                continue
            year = int(match[0])
            for col, role in ((1, "problem"), (2, "solution")):
                for i, a in enumerate(cells[col].select("a[href]"), 1):
                    href = a["href"]
                    if not href.lower().endswith(".pdf"):
                        continue
                    stage = "mechanics" if mechanics else f"paper-{i}"
                    rows.append(dict(id=f"panpho-{year}-{stage}-{role}",
                                     contest="PanPhO", year=year, edition=year-2004,
                                     stage=stage, role=role, source_tier="official",
                                     title=f"{year} 泛珠 {stage} {role}",
                                     url=urljoin(PAN, href), source_page=PAN,
                                     rights="官方注明未经许可不要转载；仅索引直链",
                                     analysis_status="not_independently_reviewed"))
    assert len(rows) == 48, f"Expected 48 PanPhO PDFs, got {len(rows)}; inspect changed HTML"
    return rows


def cpho_rows() -> list[dict]:
    rows = []
    for year, page_id in CPHO.items():
        url = f"https://cpho.pku.edu.cn/info/1053/{page_id}.htm"
        page = soup(url)
        for a in page.select("a[href]"):
            title = a.get_text(" ", strip=True)
            href = a["href"]
            # Official HTML contains misleading generic 下载 links to an old DOC.
            # Select descriptive anchors, never an adjacent generic 下载 anchor.
            if "第" not in title or not any(t in title for t in ("复赛", "决赛")):
                continue
            if not re.search(r"\.(pdf|docx?)$", href, re.I):
                continue
            stage = "semifinal-theory" if "复赛" in title else "final-theory"
            if "实验" in title:
                stage = "final-experiment-" + ("1" if "一" in title else "2")
            role = "combined" if "及解答" in title else "solution" if "解答" in title else "problem"
            rows.append(dict(id=f"cpho-{year}-{stage}-{role}", contest="CPhO",
                             year=year, edition=year-1983, stage=stage, role=role,
                             title=title, source_tier="official", source_page=url,
                             url=urljoin(url, href), rights="官方公开下载；不推定再分发许可",
                             analysis_status="not_independently_reviewed"))
    return rows


def check(row: dict, download: bool) -> dict:
    row = dict(row)
    row["checked_at"] = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat(timespec="seconds")
    try:
        with requests.get(row["url"], timeout=35, stream=True) as response:
            row["http_status"] = response.status_code
            row["resolved_url"] = response.url
            row["content_type"] = response.headers.get("Content-Type", "")
            response.raise_for_status()
            iterator = response.iter_content(65536)
            prefix = next(iterator, b"")
            row["file_signature"] = "pdf" if prefix.startswith(b"%PDF-") else "ole-doc" if prefix.startswith(bytes.fromhex("d0cf11e0a1b11ae1")) else "unknown"
            row["link_status"] = "file_signature_verified" if row["file_signature"] != "unknown" else "unexpected_content"
            # PanPhO: only check file signature, don't persist or redistribute PDFs.
            if download and row["contest"] == "CPhO" and row["file_signature"] != "unknown":
                content = prefix + b"".join(iterator)
                suffix = ".pdf" if row["file_signature"] == "pdf" else ".doc"
                target = ROOT / "originals" / "cpho" / str(row["year"]) / (row["id"] + suffix)
                target.parent.mkdir(parents=True, exist_ok=True)
                digest = hashlib.sha256(content).hexdigest()
                if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                    target = target.with_name(target.stem + "-" + digest[:12] + suffix)
                target.write_bytes(content)
                row.update(local_path=str(target.relative_to(ROOT)), sha256=digest, bytes=len(content))
    except requests.RequestException as exc:
        row["link_status"] = "request_failed"
        row["error"] = str(exc)
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download-cpho", action="store_true", help="Save official CPhO files for private study")
    args = parser.parse_args()
    rows = pan_rows() + cpho_rows()
    assert len({r["id"] for r in rows}) == len(rows), "Duplicate identifiers"
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(lambda row: check(row, args.download_cpho), rows))
    out = ROOT / "catalog"
    out.mkdir(parents=True, exist_ok=True)
    (out / "official-resources.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    lines = ["# 官方题目与参考解答直链索引", "", "生成日期：" + datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d"), "", 
             "本表是文件级链接核验，不代表逐页校勘或独立解答验证。`file_signature_verified` 表示 HTTP 成功且文件头符合 PDF/DOC。",
             "泛珠官方要求未经许可不要转载；本库仅保存链接，不镜像其试卷。全国赛原件如已下载，仅供个人学习，不代表允许公开再分发。", "",
             "| 竞赛 | 年份 | 卷别 | 类型 | 官方链接 | 核验 | 本地副本 |", "|---|---|---|---|---|---|---|"]
    for row in sorted(rows, key=lambda r: (r["contest"], r["year"], r["stage"], r["role"])):
        local = f"[原件](../{row['local_path']})" if "local_path" in row else "未保存"
        lines.append(f"| {row['contest']} | {row['year']} | {row['stage']} | {row['role']} | [下载]({row['url']}) | {row['link_status']} | {local} |")
    (out / "official-resources.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(dict(total=len(rows), verified=sum(r["link_status"] == "file_signature_verified" for r in rows),
                          local_cpho=sum("local_path" in r for r in rows)), ensure_ascii=False))


if __name__ == "__main__":
    main()
