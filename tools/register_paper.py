"""Register paper folders in every index of the repository.

Usage:
    python tools/register_paper.py [--dry] [--date YYYY-MM-DD] [folder ...]

Without folders, every `<domain>/papers/<name>/source.json` whose folder is not yet in
papers.json is registered. For each new paper this script:

1. appends an entry to papers.json (fields taken from source.json) and rewrites papers.csv;
2. adds a numbered entry to docs/paper-catalog.md and updates its total;
3. lists the paper in `<domain>/papers/README.md` and `<domain>/PAPERS.md`;
4. updates the resource counts in README.md and `<domain>/README.md`;
5. regenerates docs/topics.md with tools/gen_topics.py.

Tags: `modality_tags` and `task_tags` are read from source.json when present; otherwise they
are guessed from topic_paths and printed so they can be corrected (edit source.json, then
run tools/sync_registry.py). Direction pages (`fields/<x>/PAPERS.md`) are not touched:
the page author decides where a paper belongs. New list entries go into today's dated
section; --date overrides that registration date without changing publication years.
"""
import argparse
import csv
from datetime import date
import io
import json
import os
import re
import subprocess
import sys
from urllib.parse import urlsplit

from registry_common import catalog_label, eol, insert_dated_item, list_status, update_catalog

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS = ['foundations', 'llm', 'multimodal', 'robotics-embodied', 'cross-domain']

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
    with io.open(path(f), encoding='utf-8', newline='') as stream:
        return stream.read()


def wr(f, t):
    with io.open(path(f), 'w', encoding='utf-8', newline='') as stream:
        stream.write(t)


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


def public_source_urls(values):
    """Keep paper/source links, not private conversation permalinks."""
    if not isinstance(values, list):
        return []
    private_hosts = ('chatgpt.com', 'chat.openai.com', 'claude.ai', 'gemini.google.com')
    result = []
    for value in values:
        if not isinstance(value, str):
            continue
        try:
            parsed = urlsplit(value)
            host = parsed.hostname or ''
        except ValueError:
            continue
        if (parsed.scheme in ('http', 'https') and host and not parsed.username and not parsed.password
                and not any(host == domain or host.endswith('.' + domain) for domain in private_hosts)):
            result.append(value)
    return result


def public_chat_evidence(values):
    """Export only academic provenance metadata, never raw chats or private IDs."""
    if not isinstance(values, list):
        return []
    fields = ('role', 'date', 'association', 'message_time_association', 'evidence_type', 'relationship')
    result = []
    for value in values:
        if not isinstance(value, dict):
            continue
        item = {key: value[key] for key in fields if isinstance(value.get(key), str)}
        if isinstance(value.get('messageTimes'), list):
            item['messageTimes'] = [time for time in value['messageTimes'] if isinstance(time, str)]
        if item:
            result.append(item)
    return result


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
        'chat_evidence': public_chat_evidence(src.get('chat_evidence', [])),
        'verification_sources': public_source_urls(src.get('verification_sources', [src.get('official_url')])),
        'verification_status': src.get('verification_status') or 'not_recorded', 'caveats': [],
        'assistant_reading_status': src.get('reading_depth') or 'not_recorded',
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
    if 'original_chat_urls' in src:
        e['original_chat_urls'] = public_source_urls(src['original_chat_urls'])
    for key in ('reading_scope', 'read_version'):
        if key in src:
            e[key] = src[key]
    if 'reading_scope' not in src and 'reading_boundary' in src:
        e['reading_scope'] = src['reading_boundary']
    return e, guessed


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry', action='store_true', help='preview without writing')
    parser.add_argument('--date', type=date.fromisoformat, default=date.today(), help='registration date (YYYY-MM-DD)')
    parser.add_argument('folders', nargs='*')
    options = parser.parse_args()
    dry = options.dry
    args = [a.replace('\\', '/').rstrip('/') for a in options.folders]
    raw = rd('papers.json')
    papers = json.loads(raw)
    known = {p.get('canonical_folder') for p in papers} | {p['id'] for p in papers}
    if args:
        folders = args
    else:
        folders = sorted(
            f'{d}/{kind}/{name}' for d in DOMAINS for kind in ['papers', 'resources']
            if os.path.isdir(path(d, kind))
            for name in os.listdir(path(d, kind)) if os.path.exists(path(d, kind, name, 'source.json')))
    nxt = max((int(p['catalog_anchor'][1:]) for p in papers if re.match(r'p\d+$', p.get('catalog_anchor', ''))), default=0) + 1
    added = []
    for folder in folders:
        src = json.loads(rd(folder + '/source.json'))
        if folder in known or src['resource_id'] in known:
            continue
        e, guessed = entry_from(folder, src, 'p%03d' % nxt)
        nxt += 1
        added.append(e)
        known.update((folder, src['resource_id']))
        print(f"{e['catalog_anchor']} {folder} | {e['title'][:60]} | {e['year']} | "
              f"{list_status(e)} | date={options.date} | "
              f"modality={e['modality_tags']} task={e['task_tags']}{' (guessed)' if guessed else ''}")
    if dry or not added:
        print(f'{len(added)} new; nothing written' if dry else 'nothing to register')
        return

    papers += added
    wr('papers.json', dump_json(papers, raw))

    craw = rd('papers.csv')
    header = next(csv.reader(io.StringIO(craw)))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\r\n' if '\r\n' in craw else '\n')
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
                         f'- [{catalog_label(p)}](../{p["canonical_path"]})', '', ''])
    # Dated maintenance notes follow the anchored catalog; never hardcode a day.
    marker = re.search(r'^## \d{4}年\d{1,2}月\d{1,2}日', cat, re.M)
    cat = cat[:marker.start()] + block + cat[marker.start():] if marker else cat.rstrip() + n + n + block
    cat = update_catalog(cat, papers)
    wr('docs/paper-catalog.md', cat)

    for p in added:
        domain, kind, name = p['canonical_folder'].split('/', 2)
        for listing, prefix in [(f'{domain}/{kind}/README.md', ''), (f'{domain}/PAPERS.md', kind + '/')]:
            if os.path.exists(path(listing)) and f'{prefix}{name}/README.md' not in rd(listing):
                item = f'- [{p["title"]}]({prefix}{name}/README.md) · {p["year"] or "年份见原文"} · {list_status(p)}'
                wr(listing, insert_dated_item(rd(listing), item, options.date))

    t = rd('README.md')
    reads = sum(1 for p in papers if p.get('content_kind') == 'reading')
    t = re.sub(r'收录 \d+ 项资源，其中 \d+ 篇有讲解', f'收录 {len(papers)} 项资源，其中 {reads} 篇有讲解', t, count=1)
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
