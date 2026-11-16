#!/usr/bin/env python3
"""Replace result pages with verified, actual solution PDFs (never standings)."""
import concurrent.futures
import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from collect_extended import file_from_url
import pymupdf

ROOT=Path(__file__).resolve().parents[1]
VERSION=1

def clean(row):
    row=dict(row)
    if row['contest']!='Physics Cup':return row
    if row['role']=='problem':
        soup=BeautifulSoup(row.get('reader_html',''),'html.parser')
        for p in soup.select('p'):
            # A problem paragraph can end with submission instructions. Never
            # discard the entire statement because these words occur later.
            if re.match(r'\s*(?:please submit|for full regulations)\b',p.get_text(' ',strip=True),re.I):p.decompose()
        if row.get('reader_html'):row['reader_html']=str(soup)
        return row
    if row.get('solution_cleaning_version')==VERSION:return row
    soup=BeautifulSoup(row.get('reader_html',''),'html.parser')
    links=[];seen=set()
    for a in soup.select('a[href]'):
        u=a['href'];author=a.get_text(' ',strip=True)
        if not urlparse(u).path.lower().endswith('.pdf'):continue
        # 2019 places the problem/hint PDFs before the real submitted solutions.
        if re.match(r'^Problem\s*\d',author,re.I) or re.search(r'\bhint\b|intermediate results',author,re.I):continue
        if u not in seen:links.append((author,u));seen.add(u)
    cached={f['url']:f for f in row.get('files',[]) if f['path'].endswith('.pdf')}
    files=[];solutions=[];failures=[]
    for author,u in links[:3]:
        try:
            if u in cached:
                f=dict(cached[u])
            else:
                folder=ROOT/'originals/physics-cup'/str(row['year'])/row['id']
                f=file_from_url(u,folder,f'solution-{len(solutions)+1}')
            with pymupdf.open(ROOT/f['path']) as pdf:
                if not len(pdf):raise ValueError('Empty PDF')
            files.append(f)
            solutions.append(dict(author=author,path=f['path'],url=u))
        except Exception as exc:
            failures.append(dict(url=u,error=type(exc).__name__))
    row.pop('reader_html',None)
    row['files']=files;row['solution_attachments']=solutions
    row['solution_cleaning_version']=VERSION
    row['title']=re.sub(r'优秀解法与结果','参考解答',row['title'])
    row['collection_status']='downloaded' if files else 'unavailable'
    row['archive_note']='仅展示原来源页链接的实际解答PDF，保留作者署名；不展示成绩表、奖金、获奖公告及投稿说明。参赛者解答并非唯一标准答案。'
    row['solution_download_failures']=failures
    row['additional_solution_sources']=[dict(author=a,url=u) for a,u in links[3:]]
    return row

def main():
    path=ROOT/'catalog/extended-resources.json'
    rows=json.loads(path.read_text())
    backup=ROOT/'catalog/physicscup-result-page-archive.json'
    if not backup.exists():backup.write_text(json.dumps([r for r in rows if r['contest']=='Physics Cup' and r['role']=='solution'],ensure_ascii=False,indent=2)+'\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(clean,rows))
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    answers=[r for r in rows if r['contest']=='Physics Cup' and r['role']=='solution']
    print(json.dumps(dict(answer_records=len(answers),usable=sum(bool(r['files']) for r in answers),pdfs=sum(len(r['files']) for r in answers),unavailable=[r['id'] for r in answers if not r['files']]),ensure_ascii=False))

if __name__=='__main__':main()
