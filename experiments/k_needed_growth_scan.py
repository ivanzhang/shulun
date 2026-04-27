#!/usr/bin/env python3
"""K_needed(P) 增长率扫描。"""
import argparse, math, sys
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

def first_prime_hole(P,a,y,H):
    idx=0
    for r in range(1,H+1):
        st,qs=status(P,a,y,r)
        if st=='blocked': continue
        idx+=1
        n=a+r*P
        if isprimefac(factor(n),n): return idx,r,n
    return None,None,None

ap=argparse.ArgumentParser(); ap.add_argument('--maxP',type=int,default=2000); ap.add_argument('--step',type=int,default=10); ap.add_argument('--y',type=int,default=7); ap.add_argument('--A',type=int,default=83); ap.add_argument('--Hfactor',type=float,default=0.5)
args=ap.parse_args(); ps=[p for p in primes_upto(args.maxP) if p>args.A][::args.step]
summary=[]
for P in ps:
    H=max(100,int(args.Hfactor*P))
    rows=[x for x in boundary_events(P,args.y,P) if args.A<x['a']<P]
    maxidx=0; maxr=0; worsta=None; none=0
    for x in rows:
        idx,r,n=first_prime_hole(P,x['a'],args.y,H)
        if idx is None:
            none+=1; continue
        if idx>maxidx:
            maxidx=idx; maxr=r; worsta=x['a']
    lp=math.log(P)
    summary.append((P,len(rows),maxidx,maxr,worsta,none,maxidx/lp if lp else 0,maxr/P if P else 0))
print('P rows K_needed r_needed worst_a none K/logP r/P')
for row in summary:
    print(row[0],row[1],row[2],row[3],row[4],row[5],f"{row[6]:.3f}",f"{row[7]:.4f}")
print('max_K',max(summary,key=lambda x:x[2]))
print('max_Klog',max(summary,key=lambda x:x[6]))
print('max_r_ratio',max(summary,key=lambda x:x[7]))
