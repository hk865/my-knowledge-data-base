"""Bring papers.json in line with each paper folder's source.json.

Usage:
    python tools/sync_registry.py [--dry]

source.json is the source of truth for a paper's identity. For every entry in papers.json whose
folder has a source.json, this copies over: title, previous_titles, year, authors, topic_paths,
modality_tags, task_tags, resource_kind and content_kind (only fields present in source.json).
It then rewrites papers.csv, updates the title and topic lines in docs/paper-catalog.md, and
regenerates docs/topics.md. Run it after editing cards; new folders are added with
tools/register_paper.py instead.
"""
import csv
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = ['title', 'previous_titles', 'year', 'authors', 'topic_paths', 'modality_tags', 'task_tags',
          'resource_kind', 'content_kind']


def path(*p):
    return os.path.join(ROOT, *p)


def rd(f):
    return io.open(path(f), encoding='utf-8', newline='').read()


def wr(f, t):
    io.open(path(f), 'w', encoding='utf-8', newline='').write(t)


def main():
    dry = '--dry' in sys.argv
    raw = rd('papers.json')
    papers = json.loads(raw)
    changes = []
    for p in papers:
        folder = p.get('canonical_folder')
        if not folder or not os.path.exists(path(folder, 'source.json')):
            continue
        src = json.loads(rd(folder + '/source.json'))
        for k in FIELDS:
            if k not in src or src[k] in (None, '', []):
                continue
            v = str(src[k]) if k == 'year' else src[k]
            if p.get(k) != v:
                changes.append((p['catalog_anchor'], k, p.get(k), v))
                p[k] = v
    for anchor, k, old, new in changes:
        print(f'{anchor} {k}: {str(old)[:50]} -> {str(new)[:50]}')
    print(f'{len(changes)} field changes')
    if dry or not changes:
        return

    eol = '\r\n' if '\r\n' in raw else '\n'
    wr('papers.json', json.dumps(papers, ensure_ascii=False, indent=2).replace('\n', eol) + eol)

    craw = rd('papers.csv')
    header = next(csv.reader(io.StringIO(craw)))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\r\n')
    w.writerow(header)
    for p in papers:
        w.writerow(['' if p.get(c) is None else json.dumps(p[c], ensure_ascii=False)
                    if isinstance(p.get(c), (list, dict)) else str(p[c]) for c in header])
    wr('papers.csv', buf.getvalue())

    cat = rd('docs/paper-catalog.md')
    for p in papers:
        a = p['catalog_anchor']
        cat = re.sub(rf'(## {a} · )[^\r\n]*', lambda m: m.group(1) + p['title'], cat, count=1)
        cat = re.sub(rf'(<a id="{a}"></a>(?:(?!<a id=).)*?- 主题：)[^\r\n]*',
                     lambda m: m.group(1) + ', '.join(p['topic_paths']), cat, count=1, flags=re.S)
    wr('docs/paper-catalog.md', cat)

    subprocess.run([sys.executable, path('tools', 'gen_topics.py')], check=True, stdout=subprocess.DEVNULL)
    print('papers.json, papers.csv, paper-catalog.md and topics.md updated')


if __name__ == '__main__':
    main()
