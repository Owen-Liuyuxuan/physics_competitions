#!/usr/bin/env python3
"""Check complete translation coverage and PLANCKS split/link invariants.

This validates data integrity, not linguistic accuracy or physics correctness.
"""
import hashlib
import json
import re
from pathlib import Path

from check_sites import dataset
from plancks_boundaries import PAPERS
from translations import load_translations, source_fingerprint

ROOT = Path(__file__).resolve().parents[1]


def main():
    authored = load_translations()
    source = json.loads((ROOT / 'catalog/questions.json').read_text())
    targets = {q['id']: q for q in source if q['role'] == 'problem'
               and q['contest'] in ('Physics Cup', 'PLANCKS')}
    assert set(authored) == set(targets), ('Translation coverage mismatch',
        sorted(set(targets) - set(authored)), sorted(set(authored) - set(targets)))
    assert len(targets) == 130
    assert 'Four points' in targets['physicscup-2022-q4-reader']['reader_html']
    assert sum(q['contest'] == 'Physics Cup' for q in targets.values()) == 41
    assert sum(q['contest'] == 'PLANCKS' for q in targets.values()) == 89
    for ident, t in authored.items():
        body = t['body']
        assert re.search(r'[\u4e00-\u9fff]', body), ident
        assert not re.search(r'TODO|待翻译|稍后补充', body), ident
        # Every dollar delimiter has a matching delimiter of the same kind.
        display = re.findall(r'(?<!\\)\$\$', body)
        assert len(display) % 2 == 0, ('Unpaired display math', ident)
        inline = re.sub(r'(?<!\\)\$\$', '', body)
        assert len(re.findall(r'(?<!\\)\$', inline)) % 2 == 0, ('Unpaired inline math', ident)
        for math in re.findall(r'\$\$(.*?)\$\$|(?<!\$)\$([^$]+)\$(?!\$)', body, re.S):
            depth = 0
            for char in re.sub(r'\\[{}]', '', ''.join(math)):
                if char == '{': depth += 1
                elif char == '}': depth -= 1
                assert depth >= 0, ('Unbalanced math braces', ident)
            assert depth == 0, ('Unbalanced math braces', ident)
        assert t['translation_sha256'] == hashlib.sha256(body.encode()).hexdigest()

    by_id = {q['id']: q for q in source}
    for parent, entries in PAPERS.items():
        split = [q for q in source if q['parent_id'] == parent]
        assert sorted(q['question'] for q in split) == sorted(e[0] for e in entries), parent
        for entry in entries:
            number, _, _, first, last, *_ = entry
            row = by_id[f'{parent}-slice-q{number}']
            pages = [im['page'] for im in row['images']]
            assert pages == list(range(first, last + 1)), (row['id'], pages)
            assert row['boundary_status'] == 'page_ranges_checked'
            if row['role'] == 'problem':
                for sid in row.get('solution_ids', []):
                    sol = by_id[sid]
                    assert sol['question'] == number and sol['role'] == 'solution'
                    assert (sol['contest'], sol['year'], sol['stage']) == (row['contest'], row['year'], row['stage'])
    assert len([q for q in source if q['contest']=='PLANCKS' and q['role']=='solution']) == 59
    pending = json.loads((ROOT / 'catalog/crop-review-queue.json').read_text())
    assert not any(x.get('resource_id', '').startswith('plancks-') for x in pending)
    q7 = by_id['plancks-2025-final-combined-slice-q7']
    a7 = by_id['plancks-2025-final-combined-answer-slice-q7']
    assert q7['images'][-1]['page'] == a7['images'][0]['page'] == 25
    assert q7['images'][-1]['rect'][3] <= a7['images'][0]['rect'][1]
    for n, page in {4:16, 5:9, 6:11, 7:22, 8:13, 9:12}.items():
        p = by_id[f'plancks-2026-final-problem-slice-q{n}']
        assert by_id[p['solution_ids'][0]]['images'][0]['page'] == page

    internal = dataset('internal')
    private = {q['id']:q for q in internal['problems']}
    for ident, t in authored.items():
        attached = private[ident]['translation_zh']
        assert attached['body'] == t['body']
        assert attached['source_sha256'] == source_fingerprint(targets[ident])
        assert private[ident]['title_zh'] == t['title']
    public = dataset('public')
    for row in public['resources'] + public['problems']:
        assert 'translation_zh' not in row
    payload = (ROOT / 'sites/public/dist/data.js').read_text()
    assert all(t['body'] not in payload for t in authored.values())
    print('PASS: 130 Chinese translations (41 Physics Cup + 89 PLANCKS); '
          '11 PLANCKS papers split; 59 solution records; source bindings and public isolation.')
    print('Boundary checks cover page ranges and special mappings, not every crop visually; '
          'translation checks do not imply human verification.')
    from clean_physicscup_solutions import clean
    probe = clean({'contest':'Physics Cup', 'role':'problem',
        'reader_html':'<p>Find the image. With your solution, please submit a drawing.</p>'
                      '<p>Please submit via email.</p>'})
    assert 'Find the image' in probe['reader_html']
    assert 'via email' not in probe['reader_html']


if __name__ == '__main__':
    main()
