"""Formatting shared by registry maintenance scripts.

Only generated identity/status fragments are replaced. Curated labels, notes,
section order and newline styles remain the responsibility of page authors.
"""
import posixpath
import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote


LITERATURE_KINDS = {'paper', 'official_technical_report'}
KIND_WORDS = [('paper', '篇论文'), ('official_technical_report', '篇官方技术报告'),
              ('repository', '个代码仓库'), ('official_blog', '篇官方博客'),
              ('official_documentation', '份官方技术文档'), ('author_article', '篇作者文章')]
CARD_STATUS = re.compile(r'^(?:文献卡|资料卡)(?:，(?:暂无独立精读|非独立全文精读)|（尚无独立精读）)?(?=$| · )')
LIST_ITEM = re.compile(r'^(?P<link>- \[[^\r\n]*?\]\((?P<target>[^\r\n)]+)\))(?P<tail>[^\r\n]*)', re.M)


def eol(text):
    return '\r\n' if '\r\n' in text else '\n'


def card_label(paper):
    return '文献卡' if paper.get('resource_kind', 'paper') in LITERATURE_KINDS else '资料卡'


def list_status(paper):
    if paper.get('content_kind') == 'reading':
        return '技术精读'
    return card_label(paper) + '，暂无独立精读'


def catalog_label(paper):
    return '独立讲解' if paper.get('content_kind') == 'reading' else card_label(paper)


def insert_dated_item(text, line, added_on=None):
    """Append to today's increment section, never to the last historical list.

    An explicit date is useful when registering a batch collected on another day.
    Existing sections and manually authored text are left in place.
    """
    added_on = added_on or date.today()
    date_prefix = f'## {added_on.year}年{added_on.month}月{added_on.day}日'
    heading = re.search(r'^' + re.escape(date_prefix) + r'(?:文献|资源|文献与资料)增量[^\r\n]*', text, re.M)
    newline = eol(text)
    if not heading:
        return text.rstrip('\r\n') + newline * 2 + date_prefix + '文献与资料增量' + newline * 2 + line + newline
    following = re.search(r'^## ', text[heading.end():], re.M)
    end = heading.end() + following.start() if following else len(text)
    items = list(re.finditer(r'^- \[[^\r\n]*', text[heading.end():end], re.M))
    if items:
        at = heading.end() + items[-1].end()
        return text[:at] + newline + line + text[at:]
    at = heading.end()
    return text[:at] + newline * 2 + line + (text[at:] or newline)


def listing_paths(root, domains):
    """Domain-wide inventories only; field-level selections are hand maintained."""
    for domain in sorted(domains):
        for suffix in ('PAPERS.md', 'papers/README.md', 'resources/README.md'):
            name = f'{domain}/{suffix}'
            if (Path(root) / name).is_file():
                yield name


def update_listing(text, listing, papers):
    """Match by resolved local link, so placeholder years and cross-references work."""
    by_target = {}
    for paper in papers:
        folder = paper.get('canonical_folder')
        if folder:
            for target in (folder + '/README.md', paper.get('canonical_readme'), paper.get('canonical_path')):
                if target:
                    by_target[posixpath.normpath(target)] = paper

    def replace(match):
        target = unquote(match['target'].split('#', 1)[0])
        if re.match(r'^[a-zA-Z][\w+.-]*:', target):
            return match[0]
        paper = by_target.get(posixpath.normpath(posixpath.join(posixpath.dirname(listing), target)))
        if paper is None:
            return match[0]
        # Rows without a year slot are curated (e.g. "· 官方技术文档").
        parts = re.match(r'^( · )(年份见原文|\d{4})( · )(.*)$', match['tail'])
        if not parts:
            return match[0]
        status = parts[4]
        known_status = CARD_STATUS.match(status)
        if known_status:
            old = known_status[0]
            if paper.get('content_kind') == 'reading':
                replacement = '技术精读'
            else:
                replacement = re.sub(r'^(文献卡|资料卡)', card_label(paper), old)
            status = replacement + status[len(old):]
        elif paper.get('content_kind') == 'bibliographic_card':
            # "技术精读" is generated, unlike curated labels such as "逐步教学版".
            status = re.sub(r'^技术精读(?=$| · )', list_status(paper), status)
        year = str(paper.get('year') or parts[2])
        return match['link'] + parts[1] + year + parts[3] + status

    return LIST_ITEM.sub(replace, text)


def update_catalog(text, papers):
    """Update anchored entries without rewriting their provenance or footnotes."""
    by_anchor = {p['catalog_anchor']: p for p in papers}

    def replace(match):
        paper = by_anchor.get(match['anchor'])
        if paper is None:
            return match[0]
        block = match[0]
        block = re.sub(r'(^## ' + re.escape(paper['catalog_anchor']) + r' · )[^\r\n]*',
                       lambda m: m[1] + paper['title'], block, count=1, flags=re.M)
        block = re.sub(r'(^- 主题：)[^\r\n]*', lambda m: m[1] + ', '.join(paper['topic_paths']),
                       block, count=1, flags=re.M)

        def link(m):
            old = m['label']
            if old != '独立讲解' and not CARD_STATUS.fullmatch(old):
                return m[0]
            if paper.get('content_kind') == 'reading':
                label = '独立讲解'
            elif old == '独立讲解':
                label = card_label(paper)
            else:
                label = re.sub(r'^(文献卡|资料卡)', card_label(paper), old)
            return f'- [{label}](../{paper["canonical_path"]})'

        return re.sub(r'^- \[(?P<label>[^\r\n\]]+)\]\(\.\./[^\r\n)]+\)', link, block, flags=re.M)

    text = re.sub(r'^<a id="(?P<anchor>p\d+)"></a>.*?(?=^<a id="|^## \d{4}年|\Z)',
                  replace, text, flags=re.M | re.S)
    counts = {kind: sum(p.get('resource_kind', 'paper') == kind for p in papers) for kind, _ in KIND_WORDS}
    parts = '、'.join(f'{counts[kind]} {word}' for kind, word in KIND_WORDS if counts[kind])
    return re.sub(r'共 \d+ 个去重资源（[^）]*）', f'共 {len(papers)} 个去重资源（{parts}）', text, count=1)
