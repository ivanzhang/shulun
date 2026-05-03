#!/usr/bin/env python3
"""联合能量 Φ 扫描：Qeff 损耗 + 复用 E + Cross。"""
from __future__ import annotations
from collections import defaultdict
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

def metrics(P,c,pt,small,facp):
    D=isqrt(P); rough=[]; H=defaultdict(list); pa=defaultdict(list)
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%p for p in small):
            rough.append(k)
            if not pt[n]:
                for q in set(factor(n,facp)):
                    if D<q<P:
                        H[q].append(k); pa[k].append(q)
    N=len(rough); Q=len(H); A=sum(len(v) for v in H.values())
    E=sum(len(v)*(len(v)-1)//2 for v in H.values())
    # cross adjacent anchored small gaps with multiplicity of anchor-pairs
    anchored=sorted(pa)
    Cross=0
    for a,b in zip(anchored,anchored[1:]):
        if b-a<D:
            Cross += sum(1 for x in pa[a] for y in pa[b] if x!=y)
    return {"c":c,"N":N,"Q":Q,"A":A,"E":E,"Cross":Cross,
            "empty":N-len(pa),"anchored":len(pa),
            "q_ratio":Q/N if N else 0,"A_ratio":A/N if N else 0,"E_ratio":E/N if N else 0,"Cross_ratio":Cross/N if N else 0}

def scan(P):
    pt=sieve(P*P); small=primes_upto(isqrt(P)); facp=primes_upto(P*P)
    rows=[metrics(P,c,pt,small,facp) for c in range(1,P)]
    rows.sort(key=lambda r:(-r['A_ratio'], -r['q_ratio'])) # hardest closest to all-covered
    summary=[]
    for r in rows[:10]:
        N,Q,A,E,C=r['N'],r['Q'],r['A'],r['E'],r['Cross']
        # hypothetical lower E if A forced to N with same Q
        lowerE=(N*N/Q - N)/2 if Q else float('inf')
        summary.append({**r,"forced_E_lower_same_Q":round(lowerE,3),"E_gap":round(lowerE-E,3)})
    return {"P":P,"D":isqrt(P),"top":summary}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
