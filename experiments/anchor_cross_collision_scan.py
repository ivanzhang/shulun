#!/usr/bin/env python3
"""锚图像近碰撞 Cross-linear 扫描。"""
from __future__ import annotations
from collections import Counter, defaultdict
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
    fs=[]; x=n
    for p in primes:
        if p*p>x: break
        while x%p==0:
            fs.append(p); x//=p
    if x>1: fs.append(x)
    return fs

def anchor_hits(P,c,pt,small,facp):
    D=isqrt(P); hits=defaultdict(list); rough=[]; anchored=set()
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%p for p in small):
            rough.append(k)
            if not pt[n]:
                for q in set(factor(n,facp)):
                    if D<q<P:
                        hits[q].append(k); anchored.add(k)
    return rough, hits, anchored

def scan_col(P,c,pt,small,facp):
    D=isqrt(P); rough,hits,anchored=anchor_hits(P,c,pt,small,facp)
    qs=list(hits)
    pair_counts=Counter(); total_cross=0; gap_count=Counter()
    # count adjacent anchored small gaps and which anchor pairs can explain them
    anchored_sorted=sorted(anchored)
    for a,b in zip(anchored_sorted, anchored_sorted[1:]):
        h=b-a
        if h<D:
            # all anchors at a and b
            qa=[q for q,ks in hits.items() if a in ks]
            qb=[q for q,ks in hits.items() if b in ks]
            for x in qa:
                for y in qb:
                    if x!=y:
                        pair=tuple(sorted((x,y)))
                        pair_counts[pair]+=1; total_cross+=1; gap_count[h]+=1
    return {"c":c,"rough":len(rough),"anchored":len(anchored),"Qeff":len(qs),
            "adj_small_gaps":sum(1 for a,b in zip(anchored_sorted,anchored_sorted[1:]) if b-a<D),
            "cross_events":total_cross,"distinct_pairs":len(pair_counts),
            "max_pair_reuse":max(pair_counts.values(), default=0),
            "pair_reuse_hist":Counter(pair_counts.values()).most_common(8),
            "gap_top":gap_count.most_common(8),
            "top_pairs":[(v,p) for p,v in pair_counts.most_common(8)]}

def choose_cols(P,pt,small,facp,limit=5):
    rows=[scan_col(P,c,pt,small,facp) for c in range(1,P)]
    rows.sort(key=lambda r:(-r['max_pair_reuse'],-r['cross_events'],r['c']))
    return rows[:limit]

def scan(P):
    pt=sieve(P*P); small=primes_upto(isqrt(P)); facp=primes_upto(P*P)
    return {"P":P,"D":isqrt(P),"top":choose_cols(P,pt,small,facp)}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
