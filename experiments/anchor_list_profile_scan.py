#!/usr/bin/env python3
"""扫描粗候选的锚因子列表大小与覆盖结构。"""
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

def divisors_anchor(n:int,D:int,P:int,primes:list[int])->list[int]:
    out=[]
    for q in primes:
        if q<=D: continue
        if q>=P: break
        if n%q==0: out.append(q)
    return out

def scan(P:int,c:int,pt,small,ap):
    D=isqrt(P)
    sizes=[]; rough=prime=comp=0; anchors=[]
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%q for q in small):
            rough+=1
            L=divisors_anchor(n,D,P,ap)
            if pt[n]: prime+=1
            else: comp+=1
            sizes.append(len(L)); anchors.extend(L)
    return {"c":c,"rough":rough,"prime":prime,"comp":comp,"empty":sum(1 for s in sizes if s==0),
            "size_hist":Counter(sizes).most_common(),"anchor_reuse_top":Counter(anchors).most_common(8),
            "distinct_anchors":len(set(anchors)),"anchor_occ":len(anchors)}

def main():
    for P in [503,1009,2003,5003]:
        pt=sieve(P*P); D=isqrt(P); small=primes_upto(D); ap=primes_upto(P-1)
        rows=[scan(P,c,pt,small,ap) for c in range(1,P)]
        rows.sort(key=lambda x:(x['empty'],-x['rough']))
        print({'P':P,'D':D,'top':rows[:5]})
if __name__=='__main__': main()
