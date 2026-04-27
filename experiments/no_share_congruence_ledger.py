#!/usr/bin/env python3
"""无共享 A 类同余兼容账本（无副作用版）。"""
import argparse, math, sys
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

def share_primes(shape):
    s=set()
    for i,a in enumerate(shape):
        for b in shape[i+1:]:
            for p in prime_factors(b-a):
                if p>7: s.add(p)
    return s

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=500); ap.add_argument('--A',type=int,default=83); ap.add_argument('--K',type=int,default=6); ap.add_argument('--top',type=int,default=12)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if args.A<x['a']<args.P]
records=[]
for x in rows:
    front=[]; r=1
    while len(front)<args.K and r<=600:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked': front.append(r)
        r+=1
    if share_primes(tuple(front)): continue
    entries=[]; prime_rs=[]; L=1
    for r in front:
        n=x['a']+r*args.P; f=factor(n)
        if is_prime_fac(f,n): prime_rs.append(r); continue
        l=f[0][0]
        residue=(-x['a']*pow(r,-1,l))%l if math.gcd(r,l)==1 else None
        if residue is not None: L*=l
        entries.append((r,l,residue,args.P%l,residue==args.P%l if residue is not None else None))
    records.append({'a':x['a'],'R':x['R'],'front':front,'prime_rs':prime_rs,'entries':entries,'L':L})
records.sort(key=lambda z:(len(z['prime_rs']),-z['L'],z['a']))
print(f"P={args.P},Aclass={len(records)}")
for rec in records[:args.top]:
    print(f"a={rec['a']},R={rec['R']},prime_count={len(rec['prime_rs'])},front={rec['front']},prime_rs={rec['prime_rs']},L={rec['L']},L/P={rec['L']/args.P:.2f}")
    print(' entries=',rec['entries'])
