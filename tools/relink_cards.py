"""Point arXiv links at the local paper card when one exists.

Usage:
    python tools/relink_cards.py [--dry] [path-prefix-to-skip ...]

Scans direction pages (<domain>/fields/**/*.md), readings (<domain>/papers/*/reading.md),
perspectives/**/*.md and foundations/relations/*.md. Every Markdown link of the form
](https://arxiv.org/abs/<id>) whose <id> has a card folder <domain>/papers/arxiv-<id>/ is
rewritten to a relative link to that card's README.md. Links with a version suffix or an
anchor are left alone (they usually point at a specific section on purpose), and so are
synthesis.csv source URLs. A card never links to itself. Run it after registering new cards;
pass path prefixes to skip files another maintainer is editing right now.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINS = ['llm', 'multimodal', 'robotics-embodied', 'cross-domain']
LINK = re.compile(r'\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)')


def norm(p):
    return p.replace(os.sep, '/')


def main():
    dry = '--dry' in sys.argv
    skip = [a.replace('\\', '/').rstrip('/') for a in sys.argv[1:] if a != '--dry']
    os.chdir(ROOT)
    cards = {}
    for d in DOMAINS:
        for c in glob.glob(f'{d}/papers/arxiv-*'):
            cards[os.path.basename(c)[len('arxiv-'):]] = norm(c)
    files = []
    for d in DOMAINS:
        files += glob.glob(f'{d}/fields/**/*.md', recursive=True)
        files += glob.glob(f'{d}/papers/*/reading.md')
    files += glob.glob('perspectives/**/*.md', recursive=True)
    files += glob.glob('foundations/relations/*.md')
    total = 0
    for f in sorted(norm(x) for x in files):
        if any(f.startswith(s) for s in skip):
            continue
        text = io.open(f, encoding='utf-8', newline='').read()
        base = os.path.dirname(f)

        def repl(m):
            card = cards.get(m.group(1))
            if not card or os.path.normpath(card) == os.path.normpath(base):
                return m.group(0)
            return '](' + norm(os.path.relpath(card + '/README.md', base)) + ')'

        new = LINK.sub(repl, text)
        if new != text:
            n = len(LINK.findall(text)) - len(LINK.findall(new))
            total += n
            print(f'{f}: {n}')
            if not dry:
                io.open(f, 'w', encoding='utf-8', newline='').write(new)
    print(f'{total} links {"would be " if dry else ""}rewritten')


if __name__ == '__main__':
    main()
