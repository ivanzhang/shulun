#!/usr/bin/env python3
"""Anchor-neighborhood sparsity 扫描：每个锚的 sqrt(P) 邻域吸引其它锚的次数。"""
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

def hits(P,c,pt,small,facp):
    D=isqrt(P); H=defaultdict(list); point_anchors=defaultdict(list)
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%p for p in small) and not pt[n]:
            for q in set(factor(n,facp)):
                if D<q<P:
                    H[q].append(k); point_anchors[k].append(q)
    return H,point_anchors

def scan_col(P,c,pt,small,facp):
    D=isqrt(P); H,pa=hits(P,c,pt,small,facp)
    degrees=[]; event_sum=0
    for q,ks in H.items():
        neigh_events=0; neigh_colors=set()
        for k in ks:
            for x,qs in pa.items():
                if x!=k and abs(x-k)<D:
                    for q2 in qs:
                        if q2!=q:
                            neigh_events+=1; neigh_colors.add(q2)
        degrees.append((neigh_events,len(neigh_colors),q,len(ks)))
        event_sum+=neigh_events
    degrees.sort(reverse=True)
    return {"c":c,"Qeff":len(H),"event_sum_directed":event_sum,"cross_est":event_sum//2,
            "avg_directed_degree":round(event_sum/len(H),3) if H else 0,
            "max_directed_degree":degrees[0][0] if degrees else 0,
            "degree_hist":Counter(d[0] for d in degrees).most_common(10),
            "top_degrees":degrees[:8]}

def scan(P):
    pt=sieve(P*P); small=primes_upto(isqrt(P)); facp=primes_upto(P*P)
    rows=[scan_col(P,c,pt,small,facp) for c in range(1,P)]
    rows.sort(key=lambda r:(-r['avg_directed_degree'],-r['event_sum_directed']))
    return {"P":P,"D":isqrt(P),"top":rows[:8]}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
