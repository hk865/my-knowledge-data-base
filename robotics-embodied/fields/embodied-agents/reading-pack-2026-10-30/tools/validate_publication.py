#!/usr/bin/env python3
"""Validate this public reading package without network, downloads, or GPU use."""
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parents[3]
manifest = json.loads((PACK / 'manifest.json').read_text())
errors = []
assert len(manifest) == 21
assert len({m['id'] for m in manifest}) == 21
files = list(PACK.rglob('*.md'))
for m in manifest:
    for key in ('canonical_folder', 'reading_path'):
        if not (ROOT / m[key]).exists():
            errors.append(f'Missing {key}: {m["id"]}')
    files.extend([ROOT / m['reading_path'], ROOT / m['canonical_folder'] / 'README.md'])
    json.loads((ROOT / m['canonical_folder'] / 'source.json').read_text())
    assert m['pdf_published'] is False
for f in set(files):
    text = f.read_text()
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        parsed = urlsplit(link)
        if parsed.scheme or not parsed.path:
            continue
        if not (f.parent / unquote(parsed.path)).exists():
            errors.append(f'Broken link in {f.relative_to(ROOT)}: {link}')
for f in PACK.rglob('*.json'):
    json.loads(f.read_text())
assert not list(PACK.rglob('*.pdf'))
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: 21 unique papers, {len(set(files))} Markdown files, JSON and relative links valid; no PDF mirrors.')
