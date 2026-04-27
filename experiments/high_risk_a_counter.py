#!/usr/bin/env python3
"""固定 P 下高危边界 a 计数（独立版）。"""
import argparse, math, sys
from collections import Counter
sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status
from front_hole_shapes_mod210 import prime_factors


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

def is_prime_fac(f,n): return len(f)==1 and f[0][0]==n and f[0][1]==1

def share_set(shape):
    s=set()
    for i,a in enumerate(shape):
        for b in shape[i+1:]:
            for p in prime_factors(b-a):
                if p>7: s.add(p)
    return tuple(sorted(s))

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=500); ap.add_argument('--A',type=int,default=83); ap.add_argument('--K',type=int,default=6); ap.add_argument('--prime_threshold',type=int,default=1)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if args.A<x['a']<args.P]
summary=[]
for x in rows:
    front=[]; r=1
    while len(front)<args.K and r<=600:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked': front.append(r)
        r+=1
    prime_rs=[]
    for r in front:
        n=x['a']+r*args.P; f=factor(n)
        if is_prime_fac(f,n): prime_rs.append(r)
    sh=share_set(tuple(front))
    summary.append({'a':x['a'],'R':x['R'],'front':front,'prime_count':len(prime_rs),'prime_rs':prime_rs,'share':sh})
print(f"P={args.P},rows={len(summary)},K={args.K}")
print('prime_count_counter=',Counter(s['prime_count'] for s in summary))
print('share_counter=',Counter(s['share'] for s in summary))
high=[s for s in summary if s['prime_count']<=args.prime_threshold]
print(f"high_risk<= {args.prime_threshold}: count={len(high)}")
for s in high: print(s)
