"""Convert JATS XML or PMC HTML into plain text, one paragraph per line."""
import re,sys,html
def conv(path):
    t=open(path,encoding='utf-8',errors='replace').read()
    if path.endswith('.html'):
        m=re.search(r'(?s)<section[^>]*class="body main-article-body".*',t) or re.search(r'(?s)<main.*?</main>',t)
        t=m.group(0) if m else t
    t=re.sub(r'(?s)<(script|style|ref-list|back)\b.*?</\1>','',t) if not path.endswith('.html') else re.sub(r'(?s)<(script|style)\b.*?</\1>','',t)
    t=re.sub(r'(?s)<(caption|fig)\b[^>]*>',r'\n[FIG] ',t)
    t=re.sub(r'(?i)</(p|title|h\d|li|caption|figcaption|td|tr|div|section|sec|label)>','\n',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t).replace('\xa0',' ')
    t=re.sub(r'[ \t]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    return t
for p in sys.argv[1:]:
    out=re.sub(r'\.(pmc\.)?(xml|html)$','.txt',p)
    s=conv(p); open(out,'w').write(s); print(out,len(s))
