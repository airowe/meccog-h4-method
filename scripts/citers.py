import json,sys,urllib.request,re
UA={'User-Agent':'Mozilla/5.0 (research script)'}
seen=set()
for pmid in sys.argv[1:]:
    page=1
    while True:
        u=f'https://www.ebi.ac.uk/europepmc/webservices/rest/MED/{pmid}/citations?format=json&pageSize=1000&page={page}'
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60))
        L=d.get('citationList',{}).get('citation',[])
        for c in L:
            k=c.get('id')
            if k in seen: continue
            seen.add(k)
            t=c.get('title','')
            if re.search(r'apoe|apolipoprotein e|e4\b',t,re.I) and re.search(r'recycl|endosom|traffick|surface|endocyt|internaliz|receptor|ARF6|NHE6|ABCA1|sorting|retromer|Rab',t,re.I):
                print(c.get('source'),k,c.get('pubYear'),'|',t[:160])
        if len(L)<1000: break
        page+=1
