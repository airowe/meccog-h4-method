import json,sys,urllib.request,urllib.parse,time
UA={'User-Agent':'Mozilla/5.0 (research script)'}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60))
def search(q,n=200):
    u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=%s'%(n,urllib.parse.quote(q))
    return get(u)['esearchresult']['idlist']
def summ(ids):
    out={}
    for i in range(0,len(ids),150):
        u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id='+','.join(ids[i:i+150])
        r=get(u)['result']
        for k in ids[i:i+150]:
            if k in r: out[k]=r[k]
        time.sleep(0.4)
    return out
if __name__=='__main__':
    seen=set(); allids=[]
    for q in sys.argv[1:]:
        ids=search(q); time.sleep(0.4)
        print('## %s -> %d'%(q,len(ids)))
        new=[i for i in ids if i not in seen]; seen.update(new); allids+=new
    s=summ(allids)
    for k in allids:
        d=s.get(k,{}); doi=next((a['value'] for a in d.get('articleids',[]) if a['idtype']=='doi'),'')
        pmc=next((a['value'] for a in d.get('articleids',[]) if a['idtype']=='pmc'),'')
        print(k,d.get('pubdate','')[:4],pmc,doi,'|',d.get('title','')[:150])
