"""Check extracted H4 finding rows before they go into the spreadsheet.

Checks: quote is a verbatim substring of the paper's full text (after whitespace /
quote-character normalisation only), statistic shapes match the official format,
value/provenance pairing, '~' only with estimated_from_figure, no estimated P,
panel-level location, class/strength ranges.

usage: check_rows.py rows/<PMID>.json [...]      exit 1 on any error
       check_rows.py --selftest                   positive + negative controls
"""
import json, os, re, sys, unicodedata

FT = os.path.expanduser('~/Documents/Alzheimers/H4_work/ft')
PROV = {'printed_in_text', 'visual_only', 'estimated_from_figure', 'supplement_only',
        'not_found_in_source', 'full_text_unavailable', 'ambiguous_panel'}
ABSENT = {'not_found_in_source', 'full_text_unavailable', 'ambiguous_panel'}
EST = r'~?\s*'
EFF = [EST + r'\d+(\.\d+)?%$', EST + r'\d+(\.\d+)?x$', EST + r'[a-zA-Z]+\s*=\s*-?\d+(\.\d+)?$', r'qualitative$']
PV = [EST + r'\d+(\.\d+)?([eE][-+]?\d+)?$', EST + r'[<>]=?\s*\d+(\.\d+)?([eE][-+]?\d+)?$']
NN = [EST + r'\d+$', EST + r'\d+\s*-\s*\d+$']


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"',
                                   '–': '-', '—': '-', '−': '-', ' ': ' '}))
    return re.sub(r'\s+', ' ', s).strip().lower()


def check_stat(f, key, shapes, errs, tag):
    v, p = str(f.get(key, '')).strip(), str(f.get(key + '_prov', '')).strip()
    if not v:
        errs.append(f'{tag}: {key} empty')
        return
    if v != 'N/A' and not any(re.match(s, v, re.I) for s in shapes):
        errs.append(f'{tag}: {key} {v!r} has the wrong shape')
    if p not in PROV:
        errs.append(f'{tag}: {key}_prov {p!r} not an allowed code')
        return
    if p in ABSENT and v != 'N/A':
        errs.append(f'{tag}: {key} {v!r} but provenance {p} means no value')
    if p not in ABSENT and v == 'N/A':
        errs.append(f'{tag}: {key} N/A but provenance {p} says a value exists')
    if p == 'estimated_from_figure':
        if key == 'p':
            errs.append(f'{tag}: P value cannot be estimated_from_figure')
        elif not v.startswith('~'):
            errs.append(f'{tag}: estimate {v!r} needs a leading ~')
    elif v.startswith('~'):
        errs.append(f'{tag}: {v!r} has ~ but provenance is {p}')


def check(rows, fulltext):
    errs = []
    ft = norm(fulltext) if fulltext else None
    for i, f in enumerate(rows):
        if f.get('paper'):
            continue
        tag = f'finding {i}'
        q = f.get('quote', '')
        if q != 'N/A':
            if ft is None:
                errs.append(f'{tag}: no full text to check quote against')
            elif norm(q) not in ft:
                errs.append(f'{tag}: quote NOT found verbatim in full text: {q[:70]!r}')
        for k in ('description', 'summary', 'system', 'location'):
            if not str(f.get(k, '')).strip():
                errs.append(f'{tag}: {k} empty')
        loc = str(f.get('location', ''))
        if re.fullmatch(r'(fig(ure)?\.?\s*\d+)', loc.strip(), re.I):
            errs.append(f'{tag}: location {loc!r} is not panel-level')
        try:
            r = float(f.get('relevance'))
            assert 0 <= r <= 1
        except Exception:
            errs.append(f'{tag}: relevance must be 0-1')
        check_stat(f, 'eff', EFF, errs, tag)
        check_stat(f, 'p', PV, errs, tag)
        check_stat(f, 'n', NN, errs, tag)
        c, s = f.get('class'), f.get('strength')
        if c not in (1, 2, 3, 4, 5) or s not in (1, 2, 3, 4, 5):
            errs.append(f'{tag}: class/strength must be ints 1-5')
        elif c == 1 and s >= 4:
            errs.append(f'{tag}: class 1 with strength {s} (scale upside down?)')
        elif c == 4 and s < 3:
            errs.append(f'{tag}: class 4 with strength {s} (<3 is unlikely)')
    return errs


def selftest():
    text = 'ApoE4 reduced surface Apoer2 by 40% (P < 0.01, n = 4).'
    good = [{'paper': True}, {'description': 'd', 'quote': 'reduced surface  Apoer2 by 40%', 'summary': 's',
             'system': 'x', 'location': 'Fig 2C', 'relevance': 0.8, 'eff': '40%', 'eff_prov': 'printed_in_text',
             'p': '<0.01', 'p_prov': 'printed_in_text', 'n': '4', 'n_prov': 'printed_in_text', 'class': 1, 'strength': 1}]
    assert check(good, text) == [], check(good, text)
    bad = dict(good[1], quote='reduced surface Apoer2 by 46%', location='Fig 2', eff='~40%', p='~0.01',
               p_prov='estimated_from_figure', n='N/A', n_prov='printed_in_text', strength=5)
    e = check([bad], text)
    for needle in ('NOT found', 'panel-level', 'has ~ but', 'cannot be estimated', 'N/A but', 'class 1 with'):
        assert any(needle in x for x in e), (needle, e)
    print('selftest ok: clean row passes, 6/6 seeded defects caught')


if __name__ == '__main__':
    if sys.argv[1:] == ['--selftest']:
        selftest(); sys.exit(0)
    bad = 0
    for path in sys.argv[1:]:
        rows = json.load(open(path))
        key = os.path.basename(path).rsplit('.', 1)[0]  # rows/<key>.json -> ft/<key>.txt
        txt = os.path.join(FT, key + '.txt')
        ft = open(txt).read() if os.path.exists(txt) else None
        errs = check(rows, ft)
        n = sum(1 for r in rows if not r.get('paper'))
        print(f'{path}: {n} findings, {len(errs)} errors')
        for e in errs:
            print('  ' + e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)
