#!/usr/bin/env python3
"""Check release isolation, original hashes and all reader references."""
import hashlib
import json
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[1]

def dataset(mode):
    source = (ROOT / 'sites' / mode / 'dist' / 'data.js').read_text()
    return json.loads(source.removeprefix('window.ATLAS = ').rstrip(';\n'))

def main():
    for mode in ('public', 'internal'):
        base = ROOT / 'sites' / mode / 'dist'
        data = dataset(mode)
        rows = data['resources'] + data['problems']
        ids = {r['id'] for r in rows}
        assert len(ids) == len(rows), 'Duplicate record IDs'
        verified = set()
        crops = 0
        for r in rows:
            assert 'math' not in r
            assert 'text' not in r
            assert r.get('collection_status') not in ('pending', 'missing', 'failed')
            for ident in r.get('solution_ids', []):
                assert ident in ids, (r['id'], ident)
            if mode == 'public':
                assert not ({'text', 'reader_html', 'files', 'images', 'local_path', 'translation_zh'} & r.keys())
                continue
            assert r.get('reader_html') or any(f['path'].endswith('.pdf') for f in r.get('files', []))
            if r['contest']=='Physics Cup' and r['role']=='solution':
                assert not r.get('reader_html'),r['id']
                assert r.get('solution_attachments'),r['id']
                for a in r['solution_attachments']:
                    assert (base/a['path']).is_file(),a
                    assert a.get('pages'),a
                    for im in a['pages']:assert (base/im['path']).is_file(),im
            if r.get('reader_html'):
                from bs4 import BeautifulSoup
                html=BeautifulSoup(r['reader_html'], 'html.parser')
                assert not html.select('script, iframe, form, style')
                for img in html.select('img'):
                    assert (base / img['src']).is_file(), (r['id'],img['src'])
            for f in r.get('files', []):
                file = base / f['path']
                assert file.resolve().is_relative_to(base.resolve())
                assert file.exists(), file
                if file in verified:
                    continue
                assert hashlib.sha256(file.read_bytes()).hexdigest() == f['sha256'], file
                if file.suffix == '.pdf':
                    with pymupdf.open(file) as pdf:
                        assert len(pdf) > 0
                verified.add(file)
            for im in r.get('images', []):
                assert (base / im['path']).is_file(), im
                assert im['rect'][3] > im['rect'][1]
                assert (base / im['original']).is_file(), im
                crops += 1
        if mode == 'public':
            assert {p.name for p in base.iterdir()} == {'index.html', 'app.js', 'app.css', 'reader.css', 'data.js'}
            payload = (base / 'data.js').read_text()
            for forbidden in ('/home/', 'files/', 'crops/', 'originals/', 'owen-physics-library.'):
                assert forbidden not in payload, forbidden
        app=(base/'app.js').read_text()
        for removed in ('localStorage', 'analysis-form', 'export-notes', 'import-notes', "tab==='text'"):
            assert removed not in app
        assert '数学工具' not in (base/'index.html').read_text()
        assert 'r.math' not in app
        print(f'{mode}: {len(rows)} unique records; {len(verified)} originals; {crops} valid crop references; PASS')

if __name__ == '__main__':
    main()
