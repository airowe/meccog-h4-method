"""Compare blind referee JSON against our recorded rows.

Reports per item: AGREE / DIFFERS, naming the fields that differ. Self-test plants
two errors and requires both to be caught, so a clean run is a real negative result
and not an all-pass gate.

usage: compare_referee.py state/blind_review/referee_*.json
       compare_referee.py --selftest
"""
import json, glob, os, re, sys

FIELDS = ('eff', 'p', 'n', 'class', 'against')


def load_rows(root='rows'):
    out = {}
    for p in glob.glob(os.path.join(root, '*.json')):
        k = os.path.basename(p)[:-5]
        rows = json.load(open(p))
        for i, f in enumerate(rows[1:], 1):
            out[f'{k}#{i}'] = f
            out.setdefault(f"{k}#{f['location']}", f)
    return out


def norm(v, field=None):
    """Normalise a value for comparison.

    Referees write prose ("~2x (apoE3 157 vs apoE4 84 ng/mg)") where our rows hold a
    bare value ("2x"). Compare the LEADING quantity only, so wording does not count as
    disagreement; a genuinely different number still does.
    """
    s = str(v).strip().lower()
    s = s.replace('not shown', 'n/a').replace('not found', 'n/a').replace('none', 'n/a')
    s = s.replace('not reported', 'n/a').replace('not stated', 'n/a')
    if field in ('eff', 'p', 'n'):
        m = re.search(r'[~<>=]*\s*\d+(?:\.\d+)?\s*(?:%|x|-\s*\d+)?', s)
        if m:
            s = m.group(0)
        elif 'qualitative' in s:
            s = 'qualitative'
        elif 'n/a' in s:
            s = 'n/a'
    s = s.replace(' ', '')
    s = re.sub(r'^[~<>=]+', '', s)
    return s.rstrip('%x')


def compare(ref_items, rows):
    out = []
    for it in ref_items:
        rid = it.get('id', '')
        row = rows.get(rid)
        if row is None:
            key = rid.split('#')[0]
            cands = [v for k, v in rows.items() if k.startswith(key + '#')
                     and rid.split('#', 1)[-1].lower()[:10] in v['location'].lower()]
            row = cands[0] if len(cands) == 1 else None
        if row is None:
            out.append((rid, 'NO_MATCH', []))
            continue
        diff = [f for f in FIELDS if norm(it.get(f, ''), f) != norm(row.get(f, ''), f)]
        out.append((rid, 'DIFFERS' if diff else 'AGREE', diff))
    return out


def selftest():
    rows = {'x#1': {'eff': '50%', 'p': '<0.05', 'n': '3', 'class': 1, 'against': False,
                    'location': 'Fig 1A'}}
    clean = [{'id': 'x#1', 'eff': '50%', 'p': '<0.05', 'n': '3', 'class': 1, 'against': False}]
    assert compare(clean, rows)[0][1] == 'AGREE', 'clean item must agree'
    for field, bad in (('eff', '90%'), ('against', True)):
        planted = [dict(clean[0], **{field: bad})]
        r = compare(planted, rows)[0]
        assert r[1] == 'DIFFERS' and field in r[2], f'planted {field} error not caught'
    assert compare([{'id': 'zz#9'}], rows)[0][1] == 'NO_MATCH', 'missing row must report NO_MATCH'
    prose = [dict(clean[0], eff='~50% (apoE3 100 vs apoE4 50 ng/mg at 30 min)',
                  n='three independent experiments (n = 3)')]
    assert compare(prose, rows)[0][1] == 'AGREE', 'prose wording must not count as disagreement'
    num = [dict(clean[0], eff='~90% (apoE3 100 vs apoE4 10)')]
    assert compare(num, rows)[0][1] == 'DIFFERS', 'a genuinely different number must still differ'
    print('selftest ok: clean agrees, 2/2 planted errors caught, missing row flagged')


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        selftest(); sys.exit()
    rows = load_rows()
    items = [it for p in sys.argv[1:] for it in json.load(open(p))]
    res = compare(items, rows)
    for rid, verdict, diff in res:
        if verdict != 'AGREE':
            print(f'{verdict:9} {rid:46} {",".join(diff)}')
    n = len(res)
    agree = sum(1 for _, v, _ in res if v == 'AGREE')
    print(f'\n{agree}/{n} agree on every field; {sum(1 for _,v,_ in res if v=="DIFFERS")} differ; '
          f'{sum(1 for _,v,_ in res if v=="NO_MATCH")} unmatched')
