#!/usr/bin/env python3
"""高效扫描：模 P 各剩余类在前 P 项内的首个素数高度。"""
import argparse
import math


def sieve(n):
    arr=bytearray(b"\x01")*(n+1)
    if n>=0: arr[0]=0
    if n>=1: arr[1]=0
    for p in range(2, math.isqrt(n)+1):
        if arr[p]:
            arr[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return arr


def primes_from_flags(flags):
    return [i for i in range(2,len(flags)) if flags[i]]


def record_for(P, flags):
    first=[None]*(P+1)
    for r in range(P):
        base=r*P
        for a in range(1,P+1):
            if first[a] is None and flags[base+a]:
                first[a]=r
    worst_r=max(x for x in first[1:] if x is not None)
    worst_a=max(range(1,P+1), key=lambda a:first[a] if first[a] is not None else P+1)
    missing=[a for a in range(1,P+1) if first[a] is None]
    return {'P':P,'worst_r':worst_r,'worst_a':worst_a,'worst_prime':worst_a+worst_r*P,'missing':missing,'ratio':worst_r/P}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--maxP',type=int,default=5000)
    ap.add_argument('--top',type=int,default=30)
    args=ap.parse_args()
    flags=sieve(args.maxP*args.maxP)
    primes=[p for p in primes_from_flags(flags) if p<=args.maxP]
    rows=[record_for(P,flags) for P in primes]
    rows.sort(key=lambda x:(-x['ratio'],-x['worst_r']))
    for row in rows[:args.top]:
        print(f"P={row['P']},worst_r={row['worst_r']},ratio={row['ratio']:.4f},a={row['worst_a']},prime={row['worst_prime']},missing={len(row['missing'])}")
    print('checked',len(rows),'missing_total',sum(len(r['missing']) for r in rows),'max_worst_r',max(r['worst_r'] for r in rows),'max_ratio',max(r['ratio'] for r in rows))
    for bound in [0.1,0.15,0.2,0.25,0.3]:
        print(f"ratio_gt_{bound}=",sum(r['ratio']>bound for r in rows))

if __name__=='__main__': main()
