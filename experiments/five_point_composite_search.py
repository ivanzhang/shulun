#!/usr/bin/env python3
"""搜索前 K 洞全合数实例。

不只看边界素数，而是在给定 P 下枚举素数 a，取 B_7(a,R_boundary) 的前 K 个非零洞，检查是否全合数。
若存在全合数实例，说明短 5 点素数引理需额外边界/候选条件；若不存在，增强证据。

用法示例：
    python3 experiments/five_point_composite_search.py --P 461 --K 5 --A 83
"""
import argparse, math
from fixed_anchor_sieve_remainder import sieve, primes_upto
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

def is_prime_fac(fac,n): return len(fac)==1 and fac[0][0]==n and fac[0][1]==1

def boundary_R(P,a):
    # 最小 R 使 floor(sqrt(a+(R-1)P))>=a
    return max(1, math.ceil((a*a-a+1)/P))

ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=461); ap.add_argument('--y',type=int,default=7); ap.add_argument('--K',type=int,default=5); ap.add_argument('--A',type=int,default=83)
args=ap.parse_args(); flags=sieve(args.P); full=[]; min_prime_count=999; worst=[]
for a in primes_upto(args.P):
    if a<=args.A: continue
    R=boundary_R(args.P,a)
    front=[]; r=1
    while len(front)<args.K and r<300:
        st,qs=status(args.P,a,args.y,r)
        if st!='blocked': front.append(r)
        r+=1
    nums=[]; prime_rs=[]; minfs=[]
    for r in front:
        n=a+r*args.P; fac=factor(n); nums.append((r,n,fac))
        if is_prime_fac(fac,n): prime_rs.append(r)
        else: minfs.append(fac[0][0])
    if len(prime_rs)<min_prime_count:
        min_prime_count=len(prime_rs); worst=[(a,R,front,prime_rs,minfs,nums)]
    elif len(prime_rs)==min_prime_count:
        worst.append((a,R,front,prime_rs,minfs,nums))
    if not prime_rs: full.append((a,R,front,nums))
print(f"P={args.P},A={args.A},K={args.K},full_composite={len(full)},min_prime_count={min_prime_count},worst_count={len(worst)}")
for row in worst[:30]: print('worst',row[:5])
for row in full[:10]: print('FULL',row)
