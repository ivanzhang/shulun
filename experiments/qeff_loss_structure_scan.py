#!/usr/bin/env python3
"""Q_eff 有效锚颜色损耗结构扫描。"""
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

def profile(P:int,c:int,pt,small,facp):
    D=isqrt(P)
    rough=[]; comp=[]; empty=0; anchors=defaultdict(list); coanchors=Counter(); size_hist=Counter()
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%p for p in small):
            rough.append(k)
            if pt[n]:
                empty+=1; size_hist[0]+=1
            else:
                fs=set(factor(n,facp))
                L=sorted(q for q in fs if D<q<P)
                size_hist[len(L)]+=1
                if L: comp.append(k)
                for q in L: anchors[q].append(k)
                if len(L)>=2:
                    for q in L: coanchors[q]+=len(L)-1
    qeff=len(anchors); N=len(rough); A=sum(len(v) for v in anchors.values())
    # anchor q available positions count in whole column = floor((P-1-r)/q)+1 if r<P
    unused_possible=0; possible=0
    for q in facp:
        if D<q<P:
            r=(-c*pow(P%q,-1,q))%q
            cnt=0 if r>=P else 1+(P-1-r)//q
            possible += 1 if cnt>0 else 0
            if cnt>0 and q not in anchors: unused_possible+=1
    return {"c":c,"N":N,"empty":empty,"comp_with_anchor":len(comp),"Qeff":qeff,"A":A,
            "N_minus_Qeff":N-qeff,"Qeff_over_N":round(qeff/N,3) if N else None,
            "size_hist":size_hist.most_common(),"reuse_hist":Counter(len(v) for v in anchors.values()).most_common(8),
            "possible_colors":possible,"unused_possible":unused_possible,
            "top_reuse":sorted([(len(v),q,v[:5]) for q,v in anchors.items()], reverse=True)[:6]}

def scan(P:int):
    pt=sieve(P*P); D=isqrt(P); small=primes_upto(D); facp=primes_upto(P*P)
    rows=[profile(P,c,pt,small,facp) for c in range(1,P)]
    rows.sort(key=lambda r:(-r['Qeff_over_N'], r['empty'], -r['N'])) # hardest for Qeff不足: ratio high
    return {"P":P,"D":D,"hardest_high_Qeff":rows[:5],"lowest_empty":sorted(rows,key=lambda r:(r['empty'],-r['N']))[:5]}

def main():
    for P in [251,503,1009,2003]: print(scan(P))
if __name__=='__main__': main()
