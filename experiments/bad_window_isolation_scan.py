#!/usr/bin/env python3
"""坏窗口隔离扫描：粗候选非空且全粗合数的 sqrt(P) 窗口族。"""
from __future__ import annotations

from collections import Counter
from math import gcd, isqrt


def sieve(n: int) -> list[bool]:
    is_prime = [True] * (n + 1)
    if n >= 0: is_prime[0] = False
    if n >= 1: is_prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            for j in range(p*p, n+1, p):
                is_prime[j] = False
    return is_prime


def primes_upto(n: int) -> list[int]:
    s = sieve(n)
    return [i for i,v in enumerate(s) if v]


def factor(n: int, primes: list[int]) -> list[int]:
    fs=[]; x=n
    for p in primes:
        if p*p>x: break
        while x%p==0:
            fs.append(p); x//=p
    if x>1: fs.append(x)
    return fs


def intervals(starts: list[int], D: int) -> list[tuple[int,int]]:
    if not starts: return []
    starts=sorted(starts)
    out=[]; a=starts[0]; b=starts[0]+D
    prev=starts[0]
    for s in starts[1:]:
        if s <= prev+1:
            b=s+D
        else:
            out.append((a,b)); a=s; b=s+D
        prev=s
    out.append((a,b))
    return out


def scan_column(P:int,c:int, prime_table, allp, small) -> dict:
    D=isqrt(P)
    rough=[]; rough_prime=set(); rough_comp={}
    for k in range(P):
        n=k*P+c
        if n>=2 and all(n%q for q in small):
            rough.append(k)
            if prime_table[n]:
                rough_prime.add(k)
            else:
                fs=factor(n, allp)
                if all(f>D for f in fs):
                    rough_comp[k]=sorted(set(fs))
    rough_set=set(rough)
    bad_starts=[]; densities=[]
    for a in range(0,P-D+1):
        ks=[k for k in range(a,a+D) if k in rough_set]
        if ks and all(k in rough_comp for k in ks):
            bad_starts.append(a)
            fac=[]
            for k in ks: fac.extend(rough_comp[k])
            densities.append((len(ks), len(fac), len(set(fac))))
    runs=intervals(bad_starts,D)
    max_run=max((b-a for a,b in runs), default=0)
    covered=sum(b-a for a,b in runs)
    # rough positions covered by bad runs
    covered_rough=set()
    for a,b in runs:
        covered_rough.update(k for k in rough if a<=k<b)
    return {
        "c":c,"bad_windows":len(bad_starts),"bad_runs":len(runs),"max_run_len":max_run,
        "bad_run_cover_len":covered,"rough":len(rough),"rough_prime":len(rough_prime),"rough_comp":len(rough_comp),
        "rough_in_bad_runs":len(covered_rough),"max_bad_rough":max((x[0] for x in densities), default=0),
        "max_factor_occ":max((x[1] for x in densities), default=0),"max_distinct_factor":max((x[2] for x in densities), default=0),
        "sample_runs":runs[:5]
    }


def scan(P:int) -> dict:
    prime_table=sieve(P*P)
    allp=primes_upto(P*P)
    small=primes_upto(isqrt(P))
    rows=[]
    for c in range(1,P):
        item=scan_column(P,c,prime_table,allp,small)
        if item["bad_windows"]:
            rows.append(item)
    rows.sort(key=lambda x:(-x["bad_run_cover_len"],-x["bad_windows"],x["c"]))
    return {"P":P,"D":isqrt(P),"columns_with_bad":len(rows),"top":rows[:8]}


def main():
    for P in [251,503,1009,2003]:
        print(scan(P))

if __name__=='__main__': main()
