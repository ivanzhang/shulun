#!/usr/bin/env python3
"""Qeff 分桶损耗扫描：按锚 q 尺度统计有效颜色。"""
from __future__ import annotations
from collections import defaultdict, Counter
from math import isqrt, log2


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
        while x%p==0: fs.append(p); x//=p
    if x>1: fs.append(x)
    return fs

def bucket(q,D):
    # dyadic in multiples of D: [D*2^j, D*2^(j+1))
    j=0; x=D
    while q>=2*x:
        x*=2; j+=1
    return j

def profile(P,c,pt,small,facp):
    D=isqrt(P); rough=[]; H=defaultdict(list); possible=Counter(); effective=Counter(); occ=Counter()
    for q in facp:
        if D<q<P:
            r=(-c*pow(P%q,-1,q))%q
            if r<P:
                possible[bucket(q,D)] += 1
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%p for p in small):
            rough.append(k)
            if not pt[n]:
                for q in set(factor(n,facp)):
                    if D<q<P:
                        H[q].append(k)
    for q,ks in H.items():
        b=bucket(q,D); effective[b]+=1; occ[b]+=len(ks)
    return {"c":c,"N":len(rough),"Qeff":len(H),"ratio":round(len(H)/len(rough),3) if rough else 0,
            "possible":dict(possible),"effective":dict(effective),"occ":dict(occ),
            "bucket_eff_ratio":{b: round(effective[b]/possible[b],3) for b in possible if possible[b]},
            "bucket_occ_per_eff":{b: round(occ[b]/effective[b],3) for b in effective if effective[b]}}

def scan(P):
    pt=sieve(P*P); D=isqrt(P); small=primes_upto(D); facp=primes_upto(P*P)
    rows=[profile(P,c,pt,small,facp) for c in range(1,P)]
    rows.sort(key=lambda r:(-r['ratio'],-r['N']))
    return {"P":P,"D":D,"top":rows[:6]}

def main():
    for P in [503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
