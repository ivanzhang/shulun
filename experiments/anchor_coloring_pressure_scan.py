#!/usr/bin/env python3
"""锚因子受限列表着色压力扫描（轻量代表列）。"""
from __future__ import annotations
from collections import Counter
from math import isqrt


def sieve(n:int)->list[bool]:
    a=[True]*(n+1)
    if n>=0:a[0]=False
    if n>=1:a[1]=False
    for p in range(2,isqrt(n)+1):
        if a[p]:
            for j in range(p*p,n+1,p): a[j]=False
    return a

def primes_upto(n:int)->list[int]:
    s=sieve(n); return [i for i,v in enumerate(s) if v]

def factor(n:int, primes:list[int])->list[int]:
    out=[]; x=n
    for p in primes:
        if p*p>x: break
        while x%p==0:
            out.append(p); x//=p
    if x>1: out.append(x)
    return out

def column_data(P:int,c:int,pt,small,fac_primes):
    D=isqrt(P); rough=[]; rows=[]
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%q for q in small):
            fs=[] if pt[n] else factor(n, fac_primes)
            anchors=sorted({f for f in fs if D < f < P})
            rough.append(k)
            rows.append({"k":k,"n":n,"prime":pt[n],"anchors":anchors})
    return rough, rows

def pressure_windows(P:int,c:int,pt,small,fac_primes):
    D=isqrt(P); rough, rows=column_data(P,c,pt,small,fac_primes)
    byk={r['k']:r for r in rows}
    wins=[]
    for a in range(0,P-D+1):
        block=[byk[k] for k in rough if a<=k<a+D]
        if not block: continue
        demand=len(block)
        empty=sum(1 for r in block if not r['anchors'])
        comp=[r for r in block if r['anchors']]
        colors=set(x for r in comp for x in r['anchors'])
        # clique demand = all rough in window pairwise within D, so need distinct selected colors for composite points; prime points are empty lists.
        supply=len(colors)
        if empty or demand>=5:
            wins.append({"start":a,"rough":demand,"empty":empty,"with_anchor":len(comp),"distinct_colors":supply,
                         "list_hist":Counter(len(r['anchors']) for r in block).most_common(),
                         "ks":[r['k'] for r in block],"sample_lists":[r['anchors'][:4] for r in block[:8]]})
    wins.sort(key=lambda w:(-w['empty'], -(w['rough']-w['distinct_colors']), -w['rough'], w['start']))
    return wins[:10]

def choose_columns(P:int,pt,small,fac_primes,limit=5):
    vals=[]
    for c in range(1,P):
        rough,rows=column_data(P,c,pt,small,fac_primes)
        empty=sum(1 for r in rows if not r['anchors'])
        vals.append((empty,len(rough),c))
    vals.sort(key=lambda x:(x[0],-x[1],x[2])) # hardest: fewest empty lists, many rough
    return [c for _,_,c in vals[:limit]]

def scan(P:int):
    pt=sieve(P*P); D=isqrt(P); small=primes_upto(D); fac_primes=primes_upto(P*P)
    cols=choose_columns(P,pt,small,fac_primes,5)
    out=[]
    for c in cols:
        rough,rows=column_data(P,c,pt,small,fac_primes)
        out.append({"c":c,"rough":len(rough),"empty_total":sum(1 for r in rows if not r['anchors']),
                    "anchor_total":sum(len(r['anchors']) for r in rows),
                    "distinct_anchor_total":len({a for r in rows for a in r['anchors']}),
                    "windows":pressure_windows(P,c,pt,small,fac_primes)[:3]})
    return {"P":P,"D":D,"columns":out}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
