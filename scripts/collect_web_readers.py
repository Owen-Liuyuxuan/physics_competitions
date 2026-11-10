#!/usr/bin/env python3
"""Preserve safe original webpage structure and TeX for private reading."""
import concurrent.futures
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'p','div','span','strong','em','b','i','u','sub','sup','br','hr','ul','ol','li','h1','h2','h3','h4','blockquote','table','thead','tbody','tr','th','td','a','img','figure','figcaption','pre','code'}

def collect(row):
    if row['contest'] != 'Physics Cup' or row.get('format') != 'webpage':
        return row
    if row.get('solution_cleaning_version'):return row
    if row.get('reader_html'):
        return row
    response=requests.get(row['url'], timeout=35)
    response.raise_for_status()
    soup=BeautifulSoup(response.content,'html.parser')
    content=soup.select_one('.entry-content')
    if content is None:
        raise ValueError('Missing content: '+row['id'])
    image_map={f['url']:f['path'] for f in row['files'] if f['path'].lower().endswith(('.jpg','.png','.gif'))}
    for span in content.select('.wp-katex-eq'):
        display=span.get('data-display')=='true'
        span.replace_with(NavigableString(('\\[' if display else '\\(')+span.get_text()+('\\]' if display else '\\)')))
    for script in content.find_all('script'):
        if script.get('type','').startswith('math/tex'):
            display='mode=display' in script.get('type','')
            script.replace_with(NavigableString(('\\[' if display else '\\(')+script.get_text()+('\\]' if display else '\\)')))
        else:script.decompose()
    for tag in list(content.find_all(True)):
        if tag.name in {'style','iframe','object','embed','form','button','input','svg','noscript'}:
            tag.decompose();continue
        if tag.name not in ALLOWED:
            tag.unwrap();continue
        attrs={}
        if tag.name=='a':
            href=urljoin(row['url'],tag.get('href',''))
            if urlparse(href).scheme=='https':attrs={'href':href,'target':'_blank','rel':'noopener noreferrer'}
        elif tag.name=='img':
            src=urljoin(row['url'],tag.get('src',''))
            if src not in image_map:
                tag.decompose();continue
            attrs={'src':image_map[src],'alt':tag.get('alt','原题附图'),'loading':'lazy'}
        elif tag.name in {'th','td'}:
            attrs={k:str(tag[k]) for k in ('colspan','rowspan') if tag.get(k) and str(tag[k]).isdigit()}
        tag.attrs=attrs
    row=dict(row,reader_html=content.decode_contents(),source_page=row['url'])
    return row

def main():
    path=ROOT/'catalog/extended-resources.json'
    rows=json.loads(path.read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(collect,rows))
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print('Structured webpage readers:',sum(bool(r.get('reader_html')) for r in rows))
    vendor=ROOT/'web/vendor';vendor.mkdir(exist_ok=True)
    target=vendor/'tex-svg-full.js'
    if not target.exists():
        r=requests.get('https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg-full.js',timeout=60);r.raise_for_status();target.write_bytes(r.content)
    print('Local MathJax bundle:',target.stat().st_size)

if __name__=='__main__':main()
