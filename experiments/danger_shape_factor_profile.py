#!/usr/bin/env python3
"""高危前洞形状的失败因子剖面。

针对边界素数 a 的前 K 洞，列出失败洞 n=a+rP 的完整因子，检查失败原因是否为所有素因子 > a。
"""
import argparse, math
from fixed_anchor_sieve_remainder import sieve, primes_upto
from zero_repair_boundary_scan import boundary_events
from small_height_failure_rule import status


def factor(n):
    ps=primes_upto(math.isqrt(n)+1); out=[]; x=n
    for p in ps:
        if p*p>x: break
        if x%p==0:
            e=0
            while x%p==0: x//=p; e+=1
            out.append((p,e))
    if x>1: out.append((x,1))
    return out

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=150); ap.add_argument('--K',type=int,default=5); ap.add_argument('--min-patched',type=int,default=4)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if x['a']>83]
for x in rows:
    front=[]; patched=[]; failed=[]; r=1
    while len(front)<args.K and r<=300:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked':
            front.append(r)
            if st=='patched': patched.append((r,qs))
            else: failed.append(r)
        r+=1
    if len(patched)>=args.min_patched:
        print(f"a={x['a']},R={x['R']},front={front},patched={patched},failed={failed}")
        for r in failed:
            n=x['a']+r*args.P; fac=factor(n)
            print(' fail r',r,'n',n,'fac',fac,'min_factor',fac[0][0],'all_gt_a',all(p> x['a'] for p,e in fac))
