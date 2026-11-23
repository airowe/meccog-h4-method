"""Shortlist rows whose cited figure number does not appear within 600 chars of the quote."""
import json,glob,re,sys
sys.path.insert(0,'scripts'); from check_rows import norm
def nums(loc): return set(re.findall(r'(?:fig(?:ure)?\.?\s*s?|\bs)(\d+)',loc.lower()))
def near(ctx,ns): return any(re.search(r'(?:fig(?:ure)?s?\.?\s*s?|\bs)'+n+r'(?![0-9])',ctx) for n in ns)
def run(paths):
    out=[];tot=0
    for f in paths:
        rows=json.load(open(f)); pmid=f.split('/')[-1].rsplit('.',1)[0]; ft=norm(open(f'ft/{pmid}.txt').read())
        for r in rows[1:]:
            if r['quote']=='N/A' or 'Abstract' in r['location']: continue
            tot+=1; q=norm(r['quote']); i=ft.find(q); ctx=ft[max(0,i-600):i+len(q)+600]
            if not near(ctx,nums(r['location'])): out.append((pmid,r['location'],r['quote'][:90]))
    return out,tot
if __name__=='__main__':
    ctx='we saw less tf uptake (figure 1g,h).'
    assert near(ctx,nums('Fig 1G (left)')) and not near(ctx,nums('Fig 4C')), 'control failed'
    print('controls ok: Fig 1G found, Fig 4C not found')
    out,tot=run(sorted(glob.glob('rows/*.json')))
    for o in out: print('CHECK:',*o)
    print(f'{len(out)}/{tot} shortlisted')
