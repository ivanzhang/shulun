#!/usr/bin/env python3
"""锚因子二阶复用能量扫描。"""
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
    out=[]; x=n
    for p in primes:
        if p*p>x: break
        while x%p==0:
            out.append(p); x//=p
    if x>1: out.append(x)
    return out

def col_profile(P,c,pt,small,facp):
    D=isqrt(P)
    rough=[]; anchors=defaultdict(list); list_sizes=[]
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%q for q in small):
            rough.append(k)
            if not pt[n]:
                fs=set(factor(n,facp))
                L=sorted(q for q in fs if D<q<P)
            else:
                L=[]
            list_sizes.append(len(L))
            for q in L: anchors[q].append(k)
    reuse_counts=[len(v) for v in anchors.values()]
    reuse_energy=sum(r*(r-1)//2 for r in reuse_counts)
    gap_ratios=[]
    for q,ks in anchors.items():
        for a,b in zip(ks,ks[1:]):
            gap_ratios.append((b-a)/q)
    return {"c":c,"rough":len(rough),"empty":sum(1 for s in list_sizes if s==0),
            "anchor_occ":sum(list_sizes),"distinct_anchor":len(anchors),
            "reuse_energy":reuse_energy,"reuse_hist":Counter(reuse_counts).most_common(8),
            "max_reuse":max(reuse_counts, default=0),
            "gap_ratio_min":min(gap_ratios) if gap_ratios else None,
            "gap_ratio_top":Counter(round(x,2) for x in gap_ratios).most_common(8)}

def choose(P,pt,small,facp,limit=5):
    rows=[col_profile(P,c,pt,small,facp) for c in range(1,P)]
    # hardest hypothetical: few empty and high rough
    rows.sort(key=lambda r:(r['empty'],-r['rough'], -r['reuse_energy']))
    return rows[:limit]

def scan(P):
    pt=sieve(P*P); small=primes_upto(isqrt(P)); facp=primes_upto(P*P)
    return {"P":P,"D":isqrt(P),"top":choose(P,pt,small,facp)}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
