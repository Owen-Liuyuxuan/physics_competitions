#!/usr/bin/env python3
"""Collect official Physics Cup / PLANCKS resources for private study.

HTML originals are archived as inert text plus original diagrams, never served
as executable same-origin HTML. PDF originals remain byte-for-byte unchanged.
"""
from __future__ import annotations
import concurrent.futures as futures
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-11-10"
PLAN = "https://plancks.uk/about/past-papers/"

def fetch(url):
    r = requests.get(url, timeout=35)
    r.raise_for_status()
    return r

def page(url):
    s = BeautifulSoup(fetch(url).content, "html.parser")
    return s.select_one(".entry-content") or s.select_one("main") or s

def write_file(data, folder, name, url, kind):
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / name
    digest = hashlib.sha256(data).hexdigest()
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != digest:
        target = target.with_name(target.stem + "-" + digest[:10] + target.suffix)
    target.write_bytes(data)
    return dict(path=str(target.relative_to(ROOT)), name=target.name, url=url, kind=kind,
                bytes=len(data), sha256=digest)

def file_from_url(url, folder, label):
    r = fetch(url)
    content = r.content
    if content.startswith(b"%PDF-"):
        ext = ".pdf"
    elif content.startswith(b"\x89PNG"):
        ext = ".png"
    elif content[:3] == b"\xff\xd8\xff":
        ext = ".jpg"
    elif content[:6] in (b"GIF87a", b"GIF89a"):
        ext = ".gif"
    else:
        raise ValueError("Unexpected file signature: " + url)
    return write_file(content, folder, label+ext, url, "original")

def snapshot(row):
    row = dict(row, files=[], collected_at=DATE)
    folder = ROOT / "originals" / row["contest"].lower().replace(" ", "-") / str(row["year"]) / row["id"]
    try:
        if row.get("format") == "pdf":
            row["files"] = [file_from_url(row["url"], folder, row["id"])]
        else:
            content = page(row["url"])
            text = "Source: " + row["url"] + "\nCollected: " + DATE + "\nFormat: extracted webpage text; not a PDF original.\n\n" + content.get_text("\n", strip=True)
            row["files"].append(write_file(text.encode(), folder, "source-text.txt", row["url"], "webpage-text"))
            # Capture diagrams without third-party trackers or executable formats.
            images = list(dict.fromkeys(urljoin(row["url"], i["src"]) for i in content.select("img[src]") if "physicscup.ee/wp-content/uploads/" in i["src"]))
            attachments = list(dict.fromkeys(urljoin(row["url"], a["href"]) for a in content.select("a[href]") if urlparse(a["href"]).path.lower().endswith(".pdf")))
            for i, u in enumerate(images[:8]):
                try: row["files"].append(file_from_url(u, folder, f"diagram-{i+1}"))
                except (requests.RequestException, ValueError) as e: row.setdefault("warnings", []).append(str(e))
            for i, u in enumerate(attachments[:3]):
                try: row["files"].append(file_from_url(u, folder, f"attachment-{i+1}"))
                except (requests.RequestException, ValueError) as e: row.setdefault("warnings", []).append(str(e))
            if len(attachments) > 3:
                row["additional_pdf_urls"] = attachments[3:]
            row["archive_note"] = "网页文字与原图快照；每页最多归档3个PDF附件，其余保留来源链接。公式以原网页/原PDF为准。"
        row["collection_status"] = "downloaded" if row["files"] else "missing"
    except (requests.RequestException, ValueError) as e:
        row["collection_status"] = "failed"
        row["error"] = str(e)
    return row

def physics_cup():
    archive = "https://physicscup.ee/archive/"
    seasons = {}
    for a in page(archive).select("a[href]"):
        m = re.search(r"20\d{2}", a.get_text())
        if m and 2019 <= int(m[0]) <= 2025:
            seasons[int(m[0])] = urljoin(archive, a["href"])
    seasons[2026] = "https://physicscup.ee/"
    rows = []
    for year, url in sorted(seasons.items()):
        content = page(url)
        current = None
        for a in content.select("a[href]"):
            title = a.get_text(" ", strip=True)
            target = urljoin(url, a["href"]).replace("http://physicscup.ee", "https://physicscup.ee")
            match = re.match(r"Problem\s*(\d+)(?:\s*[-–—:]\s*(.+))?$", title, re.I)
            if match:
                q = int(match[1])
                current = f"physicscup-{year}-q{q}"
                rows.append(dict(id=current, contest="Physics Cup", year=year, stage="单题挑战",
                                 role="problem", granularity="problem", question=q,
                                 title=match[2] or {1:"Added mass",2:"Heat engines",3:"Bouncing ball",4:"Grid of resistors",5:"Diffraction pattern"}.get(q,f"Problem {q}"), url=target, source_page=url, format="pdf" if target.lower().endswith(".pdf") else "webpage",
                                 source_tier="official"))
            elif current and re.search(r"best solution", title, re.I):
                rows.append(dict(id=current+"-solutions", parent_id=current, contest="Physics Cup",
                                 year=year, stage="单题挑战", role="solution", granularity="resource",
                                 title=f"Q{current.split('q')[-1]} · 优秀解法与结果", url=target,
                                 source_page=url, format="webpage", source_tier="official"))
        print("Physics Cup", year, sum(r["year"]==year and r["role"]=="problem" for r in rows), flush=True)
    return list({r["id"]:r for r in rows}.values())

def plancks():
    content = page(PLAN)
    # Read actual document URLs from organiser's archive, keeping preliminaries distinct.
    wanted = {
      "plancks_dublin_2024_exam_solutions.pdf": (2024,"国际决赛","combined"),
      "solutions.pdf": (2023,"国际决赛","combined"),
      "plancks_2022_exam.pdf": (2022,"英爱预赛","problem"),
      "plancks2021_problems_solutions.pdf": (2021,"国际决赛","combined"),
      "plancks_kent_2021_exam.pdf": (2021,"英爱预赛","problem"),
      "plancks2020_questions.pdf": (2020,"国际决赛","problem"),
      "plancks2020_answerbooklet.pdf": (2020,"国际决赛","solution"),
      "plancks-2019-problem-set.pdf": (2019,"国际决赛","problem"),
    }
    rows=[]
    for a in content.select("a[href]"):
        u=urljoin(PLAN,a["href"])
        name=unquote(urlparse(u).path).split("/")[-1]
        if name in wanted:
            year,stage,role=wanted[name]
            ident=f"plancks-{year}-{'preliminary' if stage=='英爱预赛' else 'final'}-{role}"
            rows.append(dict(id=ident,contest="PLANCKS",year=year,stage=stage,role=role,
                             granularity="paper",title=f"PLANCKS {year} · {stage}",url=u,
                             source_page=PLAN,format="pdf",source_tier="organiser"))
    newer="https://estudiantes.rsef.es/PLANCKS25/"
    for a in page(newer).select("a[href]"):
        if "PLANCKS25_Soluciones.pdf" in a["href"]:
            rows.append(dict(id="plancks-2025-final-combined",contest="PLANCKS",year=2025,
                             stage="国际决赛",role="combined",granularity="paper",title="PLANCKS 2025 · 国际决赛",
                             url=urljoin(newer,a["href"]),source_page=newer,format="pdf",source_tier="official"))
    exams="https://plancks2026.verenigingspin.nl/"
    links=[urljoin(exams,a["href"]) for a in page(exams).select("a[href]") if a.get_text(strip=True).lower()=="exams"]
    for exam in links[:1]:
        for a in page(exam).select("a[href]"):
            u=urljoin(exam,a["href"])
            if urlparse(u).path.lower().endswith(".pdf"):
                label=a.get_text(" ",strip=True)
                if "PLANCKS-2026-Eindhoven-" in u:
                    role="solution" if "answer" in u.lower() else "problem"
                    rows.append(dict(id=f"plancks-2026-final-{role}",contest="PLANCKS",year=2026,
                                     stage="国际决赛",role=role,
                                     granularity="paper",title="PLANCKS 2026 · "+label,url=u,
                                     source_page=exam,format="pdf",source_tier="official"))
    for role,name in [("problem","Questions"),("solution","Answers")]:
        ident=f"plancks-2026-final-{role}"
        if not any(r["id"]==ident for r in rows):
            rows.append(dict(id=ident,contest="PLANCKS",year=2026,stage="国际决赛",role=role,
                             granularity="paper",title=f"PLANCKS 2026 · 国际决赛 · {role}",
                             url=f"https://plancks2026.verenigingspin.nl/wp-content/uploads/2026/10/PLANCKS-2026-Eindhoven-{name}.pdf",
                             source_page="https://plancks2026.verenigingspin.nl/exams/",format="pdf",source_tier="official"))
    return list({r["id"]:r for r in rows}.values())

def main():
    rows=physics_cup()+plancks()
    # Extend the pre-existing official catalogue with private copies, including PanPhO.
    for row in json.loads((ROOT/"catalog/official-resources.json").read_text()):
        r=dict(row,granularity="paper",format="pdf")
        if r.get("local_path"):
            r["files"]=[dict(path=r["local_path"],name=Path(r["local_path"]).name,
                             url=r["url"],kind="original",bytes=r["bytes"],sha256=r["sha256"])]
            r["collection_status"]="downloaded"
        rows.append(r)
    target=ROOT/"catalog/extended-resources.json"
    cached={r["id"]:r for r in json.loads(target.read_text())} if target.exists() else {}
    rows=[cached[r["id"]] if r["id"] in cached and cached[r["id"]].get("url")==r["url"] and cached[r["id"]].get("collection_status")=="downloaded" else r for r in rows]
    to_fetch=[r for r in rows if "files" not in r]
    with futures.ThreadPoolExecutor(max_workers=4) as pool:
        downloaded=list(pool.map(snapshot,to_fetch))
    updates={r["id"]:r for r in downloaded}
    rows=[updates.get(r["id"],r) for r in rows]
    target=ROOT/"catalog/extended-resources.json"
    target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(records=len(rows),files=sum(len(r.get("files",[])) for r in rows),
                         failed=[r["id"] for r in rows if r.get("collection_status")=="failed"])),flush=True)

if __name__=="__main__": main()
