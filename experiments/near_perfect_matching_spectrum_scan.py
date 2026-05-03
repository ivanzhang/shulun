#!/usr/bin/env python3
"""近乎完美匹配不可能：比较粗候选 gap 谱与锚命中图像谱。"""
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

def gaps(xs): return [b-a for a,b in zip(xs,xs[1:])]

def profile(P,c,pt,small,facp):
    D=isqrt(P)
    rough=[]; anchor_hit=[]; prime=[]; comp=[]; unique_anchor=[]
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%p for p in small):
            rough.append(k)
            if pt[n]:
                prime.append(k)
            else:
                fs=set(factor(n,facp))
                L=sorted(q for q in fs if D<q<P)
                if L:
                    anchor_hit.append(k); comp.append(k)
                    if len(L)==1: unique_anchor.append(k)
    return {"c":c,"N":len(rough),"prime":len(prime),"anchored":len(anchor_hit),"unique":len(unique_anchor),
            "rough_gap":Counter(gaps(rough)).most_common(10),
            "anchored_gap":Counter(gaps(anchor_hit)).most_common(10),
            "unique_gap":Counter(gaps(unique_anchor)).most_common(10),
            "prime_gap":Counter(gaps(prime)).most_common(10),
            "rough_short_gap_ratio":sum(1 for g in gaps(rough) if g<D)/max(1,len(rough)-1),
            "anchored_short_gap_ratio":sum(1 for g in gaps(anchor_hit) if g<D)/max(1,len(anchor_hit)-1),
            "missing_positions_sample":prime[:20]}

def scan(P):
    pt=sieve(P*P); small=primes_upto(isqrt(P)); facp=primes_upto(P*P)
    rows=[profile(P,c,pt,small,facp) for c in range(1,P)]
    # hardest: anchored count high relative N
    rows.sort(key=lambda r:(-(r['anchored']/r['N'] if r['N'] else 0), -r['N']))
    return {"P":P,"D":isqrt(P),"top":rows[:8]}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
