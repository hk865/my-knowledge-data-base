"""Bring papers.json in line with each paper folder's source.json.

Usage:
    python tools/sync_registry.py [--dry]

source.json is the source of truth for a paper's identity. For every entry in papers.json whose
folder has a source.json, this copies over: title, previous_titles, year, authors, topic_paths,
modality_tags, task_tags, resource_kind and content_kind (only fields present in source.json).
It then rewrites papers.csv, updates anchored entries in docs/paper-catalog.md, and regenerates
docs/topics.md. Domain inventories have their year and generated card labels refreshed by link,
including cross-references and resources; curated descriptions and section order are preserved.
Reading links and resource counts are reconciled even when source fields have not changed.
--dry reports pending registry/list/catalog changes without writing or running generators.
Run it after editing cards; new folders are added with tools/register_paper.py instead.
"""
import csv
import io
import json
import os
import re
import subprocess
import sys

from registry_common import eol, listing_paths, update_catalog, update_listing

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = ['title', 'previous_titles', 'year', 'authors', 'topic_paths', 'modality_tags', 'task_tags',
          'resource_kind', 'content_kind']


def path(*p):
    return os.path.join(ROOT, *p)


def rd(f):
    with io.open(path(f), encoding='utf-8', newline='') as stream:
        return stream.read()


def wr(f, t):
    with io.open(path(f), 'w', encoding='utf-8', newline='') as stream:
        stream.write(t)


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        return
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
        # Reconcile every reading, including entries whose kind was already updated.
        if p.get('content_kind') == 'reading' and os.path.isfile(path(folder, 'reading.md')):
            target = folder + '/reading.md'
        elif p.get('content_kind') == 'bibliographic_card':
            target = folder + '/README.md'
        else:
            continue
        if p.get('canonical_path') != target:
            changes.append((p['catalog_anchor'], 'canonical_path', p.get('canonical_path'), target))
            p['canonical_path'] = target
    for anchor, k, old, new in changes:
        print(f'{anchor} {k}: {str(old)[:50]} -> {str(new)[:50]}')
    print(f'{len(changes)} field changes')
    updates = {}

    def stage(filename, text):
        if rd(filename) != text:
            updates[filename] = text

    newline = eol(raw)
    stage('papers.json', json.dumps(papers, ensure_ascii=False, indent=2).replace('\n', newline) + newline)

    craw = rd('papers.csv')
    header = next(csv.reader(io.StringIO(craw)))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\r\n' if '\r\n' in craw else '\n')
    w.writerow(header)
    for p in papers:
        w.writerow(['' if p.get(c) is None else json.dumps(p[c], ensure_ascii=False)
                    if isinstance(p.get(c), (list, dict)) else str(p[c]) for c in header])
    stage('papers.csv', buf.getvalue())

    stage('docs/paper-catalog.md', update_catalog(rd('docs/paper-catalog.md'), papers))

    domains = {(p.get('canonical_folder') or '').split('/')[0] for p in papers} - {''}
    for listing in listing_paths(ROOT, domains):
        stage(listing, update_listing(rd(listing), listing, papers))

    # Resource and reading counts in the root and domain READMEs.
    reads_all = sum(1 for p in papers if p.get('content_kind') == 'reading')
    t = rd('README.md')
    t = re.sub(r'收录 \d+ 项资源，其中 \d+ 篇有讲解', f'收录 {len(papers)} 项资源，其中 {reads_all} 篇有讲解', t, count=1)
    stage('README.md', t)
    for domain in sorted(domains):
        f = f'{domain}/README.md'
        if not os.path.exists(path(f)):
            continue
        own = [p for p in papers if (p.get('canonical_folder') or '').startswith(domain + '/')]
        reads = sum(1 for p in own if p.get('content_kind') == 'reading')
        stage(f, re.sub(r'本领域收录 \d+ 项资源，其中 \d+ 篇有讲解', f'本领域收录 {len(own)} 项资源，其中 {reads} 篇有讲解', rd(f), count=1))

    for filename in updates:
        print(('would update ' if dry else 'updating ') + filename)
    print(f'{len(updates)} registry/catalog/list/count files need update')
    if dry:
        print('nothing written; docs/topics.md regeneration is not run in dry mode')
        return
    for filename, text in updates.items():
        wr(filename, text)

    subprocess.run([sys.executable, path('tools', 'gen_topics.py')], check=True, stdout=subprocess.DEVNULL)
    print('papers.json, papers.csv, paper-catalog.md and topics.md updated')


if __name__ == '__main__':
    main()
