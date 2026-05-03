#!/usr/bin/env python3
"""二点相关异常差分的因子剖析。"""
import argparse, math
from sieve_remainder_pair_correlation import alive_matrix
from high_threshold_margin_fast import sieve, primes
from statistics import mean


def factor(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0: n//=d; e+=1
            out.append((d,e))
        d+=1 if d==2 else 2
    if n>1: out.append((n,1))
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=20); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); H=[sum(row) for row in A]; p=mean(H)/P
    recs=[]
    for d in range(1,P):
        total=0; count=0
        for row in A:
            for r in range(P-d): total += row[r] & row[r+d]
            count += P-d
        e=total/count if count else 0; ratio=e/(p*p) if p else 0
        recs.append((ratio,d,e,total,count,factor(d)))
    recs.sort(reverse=True)
    print('top ratio d e factors')
    for ratio,d,e,total,count,fac in recs[:args.top]: print(round(ratio,3), d, round(e,5), fac)
    print('selected small d')
    for d in range(1,41):
        ratio=[x[0] for x in recs if x[1]==d][0]
        print(d, round(ratio,3), factor(d))
if __name__=='__main__': main()
