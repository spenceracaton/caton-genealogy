#!/usr/bin/env python3
"""Sanity checks on claims.jsonl before a commit: duplicate ids, missing grade,
evidence paths that do not exist. Exit 1 on any failure. Run from the repo root."""
import json, sys, pathlib, collections
root = pathlib.Path(__file__).resolve().parent.parent
rows = []
for n, line in enumerate(open(root / 'claims.jsonl', encoding='utf8'), 1):
    if not line.strip():
        continue
    try:
        rows.append(json.loads(line))
    except json.JSONDecodeError as e:
        print(f'line {n}: bad JSON: {e}'); sys.exit(1)
fail = False
ids = collections.Counter(r.get('id') for r in rows)
for i, c in ids.items():
    if c > 1:
        print(f'DUPLICATE id {i} x{c}'); fail = True
KINDS = ('fact', 'hypothesis', 'negative', 'do-not-merge', 'method', 'moot', 'void')
for r in rows:
    if r.get('grade') not in ('A', 'B', 'C'):
        print(f"{r.get('id')}: grade {r.get('grade')!r}"); fail = True
    if 'kind' not in r:
        print(f"{r.get('id')}: no 'kind' field - set one of {KINDS} (see METHOD.md s.4)"); fail = True
    elif r['kind'] not in KINDS:
        print(f"{r.get('id')}: kind {r['kind']!r} not in {KINDS}"); fail = True
    for p in [p.strip() for p in (r.get('evidence') or '').split(';') if p.strip()]:
        if not (root / p).exists():
            print(f"{r.get('id')}: missing evidence file {p}"); fail = True
print(f'{len(rows)} claims checked; ' + ('FAIL' if fail else 'ok'))
sys.exit(1 if fail else 0)
