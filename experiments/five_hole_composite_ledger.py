#!/usr/bin/env python3
"""前 5 洞全合数账本。

对边界素数 a 的前 K 个非零小骨架洞，检查对应 n_i=a+r_iP：
- 是否素数/合数；
- 最小素因子；
- 两两 gcd 是否只来自洞距；
- 若全合数，所需不同素因子数量与乘积规模。

用法示例：
    python3 experiments/five_hole_composite_ledger.py --P 461 --y 7 --Rmax 150 --K 5
"""
import argparse, math
from collections import Counter
from fixed_anchor_sieve_remainder import sieve, primes_upto
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

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--Rmax',type=int,default=150); ap.add_argument('--K',type=int,default=5); ap.add_argument('--A',type=int,default=83)
args=ap.parse_args(); rows=[x for x in boundary_events(args.P,args.y,args.Rmax) if x['a']>args.A]
full_composite=[]; prime_count_counter=Counter(); min_factor_counter=Counter()
for x in rows:
    front=[]; r=1
    while len(front)<args.K and r<=300:
        st,qs=status(args.P,x['a'],args.y,r)
        if st!='blocked': front.append(r)
        r+=1
    nums=[]; primes=[]; comp=[]; minf=[]
    for r in front:
        n=x['a']+r*args.P; fac=factor(n); nums.append((r,n,fac))
        if len(fac)==1 and fac[0][1]==1 and fac[0][0]==n: primes.append(r)
        else: comp.append(r); minf.append(fac[0][0])
    prime_count_counter[len(primes)]+=1
    for m in minf: min_factor_counter[m]+=1
    # gcd edges
    gcd_edges=[]
    for i,(r1,n1,_) in enumerate(nums):
        for r2,n2,_ in nums[i+1:]:
            g=math.gcd(n1,n2)
            if g>1: gcd_edges.append((r1,r2,g,abs(r2-r1)))
    if not primes: full_composite.append((x,nums,gcd_edges))
    print(f"a={x['a']},R={x['R']},front={front},prime_r={primes},comp_r={comp},minf={minf},gcd_edges={gcd_edges}")
print('prime_count_counter=',prime_count_counter)
print('min_factor_counter_top=',min_factor_counter.most_common(20))
print('full_composite_count=',len(full_composite))
for x,nums,gcd_edges in full_composite[:20]: print('FULL',x['a'],x['R'],nums,gcd_edges)
