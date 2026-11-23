"""Print live H4 state: counts from rows/, the paper cap, drift between ORDER,
rows/, reviews/ and the ledger, and the weakest link from state/claims.md.

Runs as the SessionStart hook, so every session starts from measured numbers
rather than counts copied into prose.

usage: state.py              print the summary (exit 0 even when drift is found)
       state.py --selftest   positive and negative controls
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER_CAP = 50


def read_order(assemble_src):
    m = re.search(r'ORDER\s*=\s*\[(.*?)\]', assemble_src, re.S)
    return re.findall(r"'([^']+)'", m.group(1)) if m else None


def findings(rows):
    return [r for r in rows if not r.get('paper')]


def summarize(rows_by_key, order, ledger, review_keys):
    used = {k: rows_by_key[k] for k in order if k in rows_by_key}
    fs = [f for rows in used.values() for f in findings(rows)]
    est = sum(any(f.get(k + '_prov') == 'estimated_from_figure' for k in ('eff', 'p', 'n')) for f in fs)
    kept = set()
    for e in ledger:
        if e.get('decision') == 'kept':
            kept.add(e['key'])
        elif e.get('decision') == 'rekeyed':
            kept.discard(e['key'])
    return {
        'papers': len(used),
        'cap_left': PAPER_CAP - len(used),
        'findings': len(fs),
        'against': sum(bool(f.get('against')) for f in fs),
        'class1': sum(f.get('class') == 1 for f in fs),
        'estimated': est,
        'order_missing_rows': sorted(set(order) - set(rows_by_key)),
        'rows_not_in_order': sorted(set(rows_by_key) - set(order)),
        'kept_not_in_order': sorted(kept - set(order)),
        'order_not_in_ledger': sorted(set(order) - kept),
        'reviewed': len(set(order) & set(review_keys)),
        'ledger_records': len(ledger),
    }


def weakest(claims_md):
    m = re.search(r'^## Weakest link.*?\n(.*?)(?=^## |\Z)', claims_md, re.S | re.M)
    items = re.findall(r'^\d+\.\s+(.+(?:\n[ \t]+\S.*)*)', m.group(1), re.M) if m else []
    items = [' '.join(i.split()) for i in items]
    return items or ['MISSING: state/claims.md has no numbered "## Weakest link" items']


def render(s, weak):
    out = [f"H4 state: {s['papers']} papers ({s['cap_left']} left under the {PAPER_CAP} cap), "
           f"{s['findings']} findings, {s['against']} against, {s['class1']} class 1, "
           f"{s['estimated']} with a figure estimate.",
           f"Ledger: {s['ledger_records']} screened records. Referee reviews on file: "
           f"{s['reviewed']}/{s['papers']} papers in ORDER."]
    for label, key in [('In ORDER but no rows file', 'order_missing_rows'),
                       ('Rows file not in ORDER (pending review?)', 'rows_not_in_order'),
                       ('Ledger says kept but not in ORDER', 'kept_not_in_order'),
                       ('In ORDER but not kept in ledger', 'order_not_in_ledger')]:
        if s[key]:
            out.append(f'DRIFT {label}: {", ".join(s[key])}')
    out.append('Weakest link (search here next):')
    out += [f'  - {w}' for w in weak]
    return '\n'.join(out)


def load():
    rows = {os.path.basename(p).rsplit('.', 1)[0]: json.load(open(p))
            for p in glob.glob(os.path.join(ROOT, 'rows', '*.json'))}
    order = read_order(open(os.path.join(ROOT, 'scripts', 'assemble.py')).read())
    if order is None:
        sys.exit('state.py: could not find ORDER in scripts/assemble.py')
    lp = os.path.join(ROOT, 'state', 'ledger.jsonl')
    ledger = [json.loads(l) for l in open(lp) if l.strip()] if os.path.exists(lp) else []
    reviews = [os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT, 'reviews', '*.md'))]
    cp = os.path.join(ROOT, 'state', 'claims.md')
    claims = open(cp).read() if os.path.exists(cp) else ''
    return rows, order, ledger, reviews, claims


def selftest():
    paper = {'paper': True}
    row = lambda **k: {'class': 3, 'against': False, 'eff_prov': 'printed_in_text', **k}
    rows = {'a': [paper, row(**{'class': 1}), row(against=True, eff_prov='estimated_from_figure')],
            'b': [paper, row()],
            'stray': [paper, row(**{'class': 1})]}
    ledger = [{'key': 'a', 'decision': 'kept'}, {'key': 'b', 'decision': 'excluded'},
              {'key': 'c', 'decision': 'kept'}]
    s = summarize(rows, ['a', 'b', 'ghost'], ledger, ['a'])
    expect = {'papers': 2, 'cap_left': 48, 'findings': 3, 'against': 1, 'class1': 1, 'estimated': 1,
              'order_missing_rows': ['ghost'], 'rows_not_in_order': ['stray'],
              'kept_not_in_order': ['c'], 'order_not_in_ledger': ['b', 'ghost'], 'reviewed': 1}
    bad = {k: (s[k], v) for k, v in expect.items() if s[k] != v}
    assert not bad, f'summarize mismatch: {bad}'
    assert 'stray' not in str(s['class1']) and s['class1'] == 1, 'rows outside ORDER must not count'
    clean = summarize({'a': rows['a']}, ['a'], [{'key': 'a', 'decision': 'kept'}], [])
    assert not any(clean[k] for k in ('order_missing_rows', 'rows_not_in_order',
                                      'kept_not_in_order', 'order_not_in_ledger')), 'false drift on clean input'
    assert weakest('## Weakest link\n\n1. **ARF6** x\n   wrapped\n2. y\n\n## Link 1\n3. not me\n') == ['**ARF6** x wrapped', 'y']
    assert weakest('# nothing here')[0].startswith('MISSING'), 'missing section must be loud'
    assert read_order("ORDER = ['1', 'k2']\n") == ['1', 'k2'] and read_order('x = 1') is None
    rk = summarize({'n': rows['b']}, ['n'], [{'key': 'w', 'decision': 'kept'}, {'key': 'n', 'decision': 'kept'},
                                             {'key': 'w', 'decision': 'rekeyed'}], [])
    assert rk['kept_not_in_order'] == [] and rk['order_not_in_ledger'] == [], f'rekeyed must retire old key: {rk}'
    relog = summarize({'a': rows['a']}, ['a'], [{'key': 'a', 'decision': 'kept'}, {'key': 'a', 'decision': 'excluded'}], [])
    assert relog['order_not_in_ledger'] == [], 'a later re-screen must not un-keep a paper'
    print('selftest ok: counts, drift (4 kinds, plus a clean negative), rekey, weakest-link parse and miss')


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']:
        selftest()
        sys.exit(0)
    rows, order, ledger, reviews, claims = load()
    print(render(summarize(rows, order, ledger, reviews), weakest(claims)))
