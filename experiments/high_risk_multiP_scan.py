#!/usr/bin/env python3
"""多 P 高危计数扫描。"""
import argparse, subprocess, sys, re
from fixed_anchor_sieve_remainder import primes_upto

# 为避免导入副作用，直接复用 high_risk_a_counter 的逻辑内嵌简化
import math
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status
from front_hole_shapes_mod210 import prime_factors
from fixed_anchor_sieve_remainder import sieve

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

def stats(P,y,K,A):
    rows=[x for x in boundary_events(P,y,P) if A<x['a']<P]
    counts=[]
    for x in rows:
        front=[]; r=1
        while len(front)<K and r<=P:
            st,qs=status(P,x['a'],y,r)
            if st!='blocked': front.append(r)
            r+=1
        pc=0
        for r in front:
            n=x['a']+r*P
            if isprimefac(factor(n),n): pc+=1
        counts.append(pc)
    high=sum(1 for c in counts if c<=1)
    minpc=min(counts) if counts else None
    return len(rows), high, minpc, counts

ap=argparse.ArgumentParser(); ap.add_argument('--maxP',type=int,default=1000); ap.add_argument('--step',type=int,default=10); ap.add_argument('--y',type=int,default=7); ap.add_argument('--K',type=int,default=6); ap.add_argument('--A',type=int,default=83)
args=ap.parse_args(); ps=[p for p in primes_upto(args.maxP) if p>args.A][::args.step]
for P in ps:
    rows,high,minpc,counts=stats(P,args.y,args.K,args.A)
    print(f"P={P},rows={rows},high<=1={high},min_prime_count={minpc},dist={ {i:counts.count(i) for i in sorted(set(counts))} }")
