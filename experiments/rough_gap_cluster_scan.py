#!/usr/bin/env python3
"""粗筛候选间隔簇扫描。"""
from __future__ import annotations
from math import isqrt
from collections import Counter


def sieve(n:int)->list[bool]:
    a=[True]*(n+1)
    if n>=0:a[0]=False
    if n>=1:a[1]=False
    for p in range(2,isqrt(n)+1):
        if a[p]:
            for j in range(p*p,n+1,p):a[j]=False
    return a

def primes_upto(n:int)->list[int]:
    s=sieve(n); return [i for i,v in enumerate(s) if v]

def col(P,c,prime_table,small):
    rough=[]; rprime=[]; rcomp=[]
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%q for q in small):
            rough.append(k)
            (rprime if prime_table[n] else rcomp).append(k)
    D=isqrt(P)
    gaps=[rough[i+1]-rough[i] for i in range(len(rough)-1)]
    short=sum(1 for g in gaps if g<D)
    clusters=[]
    if rough:
        cur=[rough[0]]
        for a,b in zip(rough,rough[1:]):
            if b-a<D: cur.append(b)
            else:
                clusters.append(cur); cur=[b]
        clusters.append(cur)
    return {"c":c,"rough":len(rough),"prime":len(rprime),"comp":len(rcomp),"short_gaps":short,
            "clusters":len(clusters),"max_cluster":max((len(x) for x in clusters),default=0),
            "gap_top":Counter(gaps).most_common(8)}

def scan(P):
    pt=sieve(P*P); small=primes_upto(isqrt(P))
    rows=[col(P,c,pt,small) for c in range(1,P)]
    rows.sort(key=lambda x:(-x['max_cluster'],-x['short_gaps'],x['c']))
    return {"P":P,"D":isqrt(P),"top":rows[:8],"min_prime":min(r['prime'] for r in rows),"max_cluster":max(r['max_cluster'] for r in rows)}

def main():
    for P in [251,503,1009,2003,5003]: print(scan(P))
if __name__=='__main__': main()
