#!/usr/bin/env python3
"""Render actual Physics Cup solution PDFs as readable original-page images."""
import json
from pathlib import Path
import pymupdf

ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'catalog/extended-resources.json'
    rows=json.loads(path.read_text());count=0
    for r in rows:
        for i,a in enumerate(r.get('solution_attachments',[]),1):
            folder=ROOT/'derived/physicscup-solutions'/r['id']/str(i)
            folder.mkdir(parents=True,exist_ok=True)
            a['pages']=[]
            with pymupdf.open(ROOT/a['path']) as pdf:
                for j,page in enumerate(pdf):
                    target=folder/f'page-{j+1}.jpg'
                    if not target.exists():page.get_pixmap(matrix=pymupdf.Matrix(1.3,1.3)).save(target,jpg_quality=85)
                    a['pages'].append(dict(path=str(target.relative_to(ROOT)),page=j+1))
                    count+=1
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print('Original solution page images:',count)

if __name__=='__main__':main()
