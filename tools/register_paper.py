"""Register paper folders in every index of the repository.

Usage:
    python tools/register_paper.py [--dry] [folder ...]

Without folders, every `<domain>/papers/<name>/source.json` whose folder is not yet in
papers.json is registered. For each new paper this script:

1. appends an entry to papers.json (fields taken from source.json) and rewrites papers.csv;
2. adds a numbered entry to docs/paper-catalog.md and updates its total;
3. lists the paper in `<domain>/papers/README.md` and `<domain>/PAPERS.md`;
4. updates the resource counts in README.md and `<domain>/README.md`;
5. regenerates docs/topics.md with tools/gen_topics.py.

Tags: `modality_tags` and `task_tags` are read from source.json when present; otherwise they
are guessed from topic_paths and printed so they can be corrected (edit source.json and
papers.json, then rerun tools/gen_topics.py). Direction pages (`fields/<x>/PAPERS.md`) are
not touched: the page author decides where a paper belongs.
"""
import csv
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS = ['foundations', 'llm', 'multimodal', 'robotics-embodied', 'cross-domain']
KIND_WORDS = [('paper', '篇论文'), ('official_technical_report', '篇官方技术报告'), ('repository', '个代码仓库'), ('official_blog', '篇官方博客')]

# Fallback tags by topic path prefix (first match wins for each prefix that applies).
GUESS = [
    ('multimodal/generation', ['image'], ['generation']),
    ('multimodal/video-temporal', ['video'], ['generation']),
    ('multimodal/world-models', ['video', 'action'], ['generation']),
    ('multimodal/visual-representation', ['image'], ['understanding']),
    ('multimodal', ['multimodal'], ['understanding']),
    ('robotics/control', ['action', 'state'], ['decision']),
    ('robotics/embodied-policies', ['multimodal', 'action'], ['decision']),
    ('robotics', ['action'], ['decision']),
    ('cross-domain/training-science', ['text'], ['analysis']),
    ('cross-domain/model-science', ['text'], ['analysis']),
    ('cross-domain/evaluation', ['text'], ['evaluation']),
    ('llm', ['text'], ['generation']),
]


def path(*p):
    return os.path.join(ROOT, *p)


def rd(f):
    return io.open(path(f), encoding='utf-8', newline='').read()


def wr(f, t):
    io.open(path(f), 'w', encoding='utf-8', newline='').write(t)


def eol(t):
    return '\r\n' if '\r\n' in t else '\n'


def dump_json(obj, like):
    n = eol(like)
    return json.dumps(obj, ensure_ascii=False, indent=2).replace('\n', n) + n


def guess_tags(topics):
    mod, task = [], []
    for tp in topics:
        for prefix, m, t in GUESS:
            if tp.startswith(prefix):
                mod += [x for x in m if x not in mod]
                task += [x for x in t if x not in task]
                break
    return mod or ['text'], task or ['understanding']


def year_of(src, folder):
    if src.get('year'):
        return str(src['year'])
    readme = path(folder, 'README.md')
    if os.path.exists(readme):
        m = re.search(r'状态：[^\n]*?(\d{4})', rd(folder + '/README.md'))
        if m:
            return m.group(1)
    return ''


def entry_from(folder, src, anchor):
    rid = src['resource_id']
    topics = src.get('topic_paths') or []
    mod = src.get('modality_tags') or None
    task = src.get('task_tags') or None
    guessed = not (mod and task)
    if guessed:
        gm, gt = guess_tags(topics)
        mod, task = mod or gm, task or gt
    reading = src.get('content_kind') == 'reading'
    e = {
        'id': rid, 'title': src['title'], 'url': src.get('official_url'),
        'arxiv_id': rid.split(':', 1)[1] if rid.startswith('arxiv:') else None,
        'doi': rid.split(':', 1)[1] if rid.startswith('doi:') else None,
        'year': year_of(src, folder), 'topic_paths': topics, 'detail_topics': [],
        'architecture_tags': [], 'supervision_tags': [], 'provenance': [src.get('source_origin', 'repository-maintenance')],
        'chat_evidence': [], 'verification_sources': [src.get('official_url')],
        'verification_status': src.get('reading_depth', ''), 'caveats': [],
        'reading_status': src.get('teaching_status', ''), 'resource_kind': src.get('resource_kind', 'paper'),
        'method_tags': [], 'evaluation_tags': [], 'catalog_anchor': anchor, 'user_reading_status': 'unknown',
        'modality_tags': mod, 'task_tags': task,
        'canonical_folder': folder,
        'canonical_path': folder + ('/reading.md' if reading else '/README.md'),
        'canonical_readme': folder + '/README.md', 'source_path': folder + '/source.json',
        'legacy_paths': [], 'content_kind': src.get('content_kind', 'bibliographic_card'),
    }
    if src.get('authors'):
        e['authors'] = src['authors']
    if src.get('previous_titles'):
        e['previous_titles'] = src['previous_titles']
    return e, guessed


def insert_after_last_item(text, line):
    n = eol(text)
    lines = text.split(n)
    last = max((i for i, l in enumerate(lines) if l.startswith('- [')), default=len(lines) - 1)
    lines.insert(last + 1, line)
    return n.join(lines)


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        return
    dry = '--dry' in sys.argv
    args = [a.replace('\\', '/').rstrip('/') for a in sys.argv[1:] if a != '--dry']
    raw = rd('papers.json')
    papers = json.loads(raw)
    known = {p.get('canonical_folder') for p in papers} | {p['id'] for p in papers}
    if args:
        folders = args
    else:
        folders = sorted(
            f'{d}/papers/{name}' for d in DOMAINS if os.path.isdir(path(d, 'papers'))
            for name in os.listdir(path(d, 'papers')) if os.path.exists(path(d, 'papers', name, 'source.json')))
    nxt = max(int(p['catalog_anchor'][1:]) for p in papers if re.match(r'p\d+$', p.get('catalog_anchor', ''))) + 1
    added = []
    for folder in folders:
        src = json.loads(rd(folder + '/source.json'))
        if folder in known or src['resource_id'] in known:
            continue
        e, guessed = entry_from(folder, src, 'p%03d' % nxt)
        nxt += 1
        added.append(e)
        print(f"{e['catalog_anchor']} {folder} | {e['title'][:60]} | {e['year']} | "
              f"modality={e['modality_tags']} task={e['task_tags']}{' (guessed)' if guessed else ''}")
    if dry or not added:
        print(f'{len(added)} new; nothing written' if dry else 'nothing to register')
        return

    papers += added
    wr('papers.json', dump_json(papers, raw))

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
    n = eol(cat)
    block = ''
    for p in added:
        block += n.join([f'<a id="{p["catalog_anchor"]}"></a>', f'## {p["catalog_anchor"]} · {p["title"]}', '',
                         f'- 标识：{p["id"]}', f'- 原文 / 官方入口：{p["url"]}', f'- 主题：{", ".join(p["topic_paths"])}',
                         f'- 身份核验：{p["verification_status"]}', '- 用户阅读状态：unknown',
                         f'- [{"独立讲解" if p["content_kind"] == "reading" else "文献卡"}](../{p["canonical_path"]})', '', ''])
    marker = '## 2026年10月3日既有条目更新'
    cat = cat.replace(marker, block + marker, 1) if marker in cat else cat.rstrip() + n + n + block
    counts = {k: sum(1 for p in papers if p.get('resource_kind', 'paper') == k) for k, _ in KIND_WORDS}
    parts = '、'.join(f'{counts[k]} {w}' for k, w in KIND_WORDS if counts[k])
    cat = re.sub(r'共 \d+ 个去重资源（[^）]*）', f'共 {len(papers)} 个去重资源（{parts}）', cat, count=1)
    wr('docs/paper-catalog.md', cat)

    for p in added:
        domain, _, name = p['canonical_folder'].split('/', 2)
        item = f'- [{p["title"]}]({{}}{name}/README.md) · {p["year"] or "年份见原文"} · 文献卡，暂无独立精读'
        for listing, prefix in [(f'{domain}/papers/README.md', ''), (f'{domain}/PAPERS.md', 'papers/')]:
            if os.path.exists(path(listing)) and f'{prefix}{name}/README.md' not in rd(listing):
                wr(listing, insert_after_last_item(rd(listing), item.format(prefix)))

    t = rd('README.md')
    wr('README.md', re.sub(r'收录 \d+ 项资源', f'收录 {len(papers)} 项资源', t, count=1))
    for domain in DOMAINS:
        f = f'{domain}/README.md'
        if not os.path.exists(path(f)):
            continue
        own = [p for p in papers if (p.get('canonical_folder') or '').startswith(domain + '/')]
        reads = sum(1 for p in own if p.get('content_kind') == 'reading')
        t = rd(f)
        wr(f, re.sub(r'本领域收录 \d+ 项资源，其中 \d+ 篇有讲解', f'本领域收录 {len(own)} 项资源，其中 {reads} 篇有讲解', t, count=1))

    subprocess.run([sys.executable, path('tools', 'gen_topics.py')], check=True, stdout=subprocess.DEVNULL)
    print(f'registered {len(added)}; total {len(papers)}')


if __name__ == '__main__':
    main()
