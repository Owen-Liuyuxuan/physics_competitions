"""Load authored Chinese translations; never synthesize placeholder translations."""
from pathlib import Path
import hashlib
import re

ROOT=Path(__file__).resolve().parents[1]

def load_translations():
    result={}
    for path in sorted((ROOT/'catalog/translations').glob('*.zh.md')):
        sections=re.split(r'^## ([\w-]+) \| (.+)\s*$',path.read_text(),flags=re.M)
        for i in range(1,len(sections),3):
            ident,title,body=sections[i:i+3]
            assert ident not in result, ('Duplicate translation',ident)
            body=body.strip()
            assert len(body)>30, ('Empty translation',ident)
            result[ident]={'language':'zh-CN','title':title.strip(),'body':body,
                'kind':'question_translation','status':'ai_translated',
                'notice':'AI 中文辅助译文，非官方译本，未经人工逐题校订；用于理解题面，不代替原题或参考解答。公式、附图及歧义请对照原卷。',
                'translation_sha256':hashlib.sha256(body.encode()).hexdigest()}
    return result

def source_fingerprint(row):
    """Bind to the actual source PDF or native HTML (not extracted PDF text)."""
    pdf=next((f for f in row.get('files',[]) if f['path'].endswith('.pdf')),None)
    if pdf:return pdf['sha256']
    return hashlib.sha256(row.get('reader_html','').encode()).hexdigest()
