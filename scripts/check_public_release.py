#!/usr/bin/env python3
"""Dependency-free fail-closed check for GitHub Pages' public-only artifact."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'docs'
ALLOWED={'index.html','app.js','app.css','reader.css','data.js'}
PUBLIC_KEYS={'id','contest','contest_label','year','stage','role','question','title','granularity','parent_id','source_page','source_tier','topics','tag_status','difficulty','model'}

def main():
    assert {p.name for p in BASE.iterdir()}==ALLOWED
    assert all(p.is_file() and not p.is_symlink() for p in BASE.iterdir())
    payload=(BASE/'data.js').read_text()
    data=json.loads(payload.removeprefix('window.ATLAS = ').rstrip(';\n'))
    assert data['mode']=='public' and data['fileCount']==0
    for r in data['resources']+data['problems']:
        assert set(r)<=PUBLIC_KEYS,(r['id'],set(r)-PUBLIC_KEYS)
        assert r['contest_label']=={'CPhO':'全国中学生物理竞赛','PanPhO':'泛珠三角物理奥林匹克'}.get(r['contest'],r['contest'])
    for p in BASE.iterdir():
        text=p.read_text()
        for forbidden in ('originals/','crops/','/home/','owen-physics-library.','Authorization: Bearer','ghp_','github_pat_','source_repository_credential'):
            assert forbidden not in text,(p.name,forbidden)
        assert not re.search(r'files/[0-9a-f]{20}',text),(p.name,'private download path')
    print(f'Public-only Pages artifact PASS: {len(ALLOWED)} files; no originals, cuts, text, credentials or internal addresses.')

if __name__=='__main__':main()
