#!/usr/bin/env python3
"""前缀洞全合数的筛概率模型（独立版）。"""
import argparse, math, sys
from collections import Counter
sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status

def factor(n):
    out=[]; x=n
    for p in primes_upto(math.isqrt(n)+1):
        if p*p>x: break
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            out.append((p,e))
    if x>1: out.append((x,1))
    return out

def isprimefac(f,n): return len(f)==1 and f[0][0]==n and f[0][1]==1

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=997); ap.add_argument('--y',type=int,default=7); ap.add_argument('--A',type=int,default=83); ap.add_argument('--Kmax',type=int,default=40)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.P) if args.A<x['a']<args.P]
lengths=[]
for x in rows:
    idx=0; first_prime_idx=None; r=1
    while idx<args.Kmax and r<=args.P:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked':
            idx+=1; n=x['a']+r*args.P
            prime=isprimefac(factor(n),n)
            if prime and first_prime_idx is None: first_prime_idx=idx
        r+=1
    if first_prime_idx is None: first_prime_idx=args.Kmax+1
    lengths.append(first_prime_idx)
print(f"P={args.P},rows={len(rows)},Kmax={args.Kmax}")
print('first_prime_idx_counter=',Counter(lengths))
print('max_first_idx=',max(lengths) if lengths else None,'avg_first_idx=',sum(lengths)/len(lengths) if lengths else None)
for T in [5,8,10,12,16,20,30,40]:
    actual=sum(1 for x in lengths if x>T)/max(1,len(lengths))
    model=math.exp(-T/max(2.0,math.log(args.P*max(2,T))))
    print(f"T={T},actual_survive>{T}={actual:.4f},model≈{model:.4f}")
print('worst rows:')
maxlen=max(lengths) if lengths else None
for x in rows:
    idx=0; first=None; detail=[]; r=1
    while idx<args.Kmax and r<=args.P:
        st,qs=status(args.P,args.y and x['a'],args.y,r)
        if st!='blocked':
            idx+=1; n=x['a']+r*args.P; prime=isprimefac(factor(n),n); detail.append((idx,r,prime,n))
            if prime and first is None: first=idx
        r+=1
    if first==maxlen: print('a',x['a'],'R',x['R'],'first',first,'detail',detail[:max(20,first or 0)])
