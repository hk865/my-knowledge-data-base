"""Check that relative links in the repository's Markdown files point to existing files.

Usage: python tools/check_links.py [file.md ...]
Without arguments every tracked and untracked (not ignored) .md file is checked.
Exits with status 1 when a broken link is found.
"""
import os
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'(?:\]\(|src=")([^)"\s]+)')
# Placeholders used inside STYLE.md templates.
PLACEHOLDERS = {'<官方链接>'}


def markdown_files():
    def git(*args):
        out = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout
        return [f for f in out.split('\n') if f.endswith('.md')]
    return sorted(set(git('ls-files') + git('ls-files', '--others', '--exclude-standard')))


def broken_links(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        text = f.read()
    base = os.path.dirname(os.path.join(ROOT, path))
    for target in LINK.findall(text):
        if target in PLACEHOLDERS or re.match(r'^(https?:|mailto:|#|data:)', target):
            continue
        rel = unquote(target.split('#', 1)[0])
        if rel and not os.path.exists(os.path.join(base, rel)):
            yield target


def main():
    files = sys.argv[1:] or markdown_files()
    bad = [(f, t) for f in files for t in broken_links(f)]
    for f, t in bad:
        print(f'{f} -> {t}')
    print(f'checked {len(files)} files; broken links: {len(bad)}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
