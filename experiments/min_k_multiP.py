#!/usr/bin/env python3
"""多 P 搜索保证边界前 K 洞有素数所需的最小 K。"""
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

def first_prime_hole_index(P,a,y,H):
    idx=0
    for r in range(1,H+1):
        st,qs=status(P,a,y,r)
        if st=='blocked': continue
        idx+=1
        n=a+r*P
        if isprimefac(factor(n),n): return idx,r,n
    return None,None,None

ap=argparse.ArgumentParser(); ap.add_argument('--maxP',type=int,default=700); ap.add_argument('--step',type=int,default=8); ap.add_argument('--y',type=int,default=7); ap.add_argument('--A',type=int,default=83); ap.add_argument('--H',type=int,default=300)
args=ap.parse_args();
for P in [p for p in primes_upto(args.maxP) if p>args.A][::args.step]:
    rows=[x for x in boundary_events(P,args.y,P) if args.A<x['a']<P]
    maxidx=0; worst=[]; none=[]
    for x in rows:
        idx,r,n=first_prime_hole_index(P,x['a'],args.y,args.H)
        if idx is None: none.append(x); continue
        if idx>maxidx: maxidx=idx; worst=[(x,idx,r,n)]
        elif idx==maxidx: worst.append((x,idx,r,n))
    print(f"P={P},rows={len(rows)},K_needed={maxidx},none={len(none)}")
    for x,idx,r,n in worst[:3]: print('  worst',x['a'],x['R'],'idx',idx,'r',r,'n',n)
