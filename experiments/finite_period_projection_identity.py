#!/usr/bin/env python3
"""有限周期投影恒等验证。

对有限素数集 P0，Q=prod P0。定义 A mod Q 为避开所有 p 的小筛集合，Y_h=1_{x+h in A}/pA - 1, x uniform mod Q。
计算 K_r cumulant，并验证 sum_{h mod Q} K_r(h,fixed...)=0。
"""
import argparse, math, itertools


def primes_first(k):
    ps=[]; n=2
    while len(ps)<k:
        if all(n%p for p in ps if p*p<=n): ps.append(n)
        n+=1
    return ps

def partitions(seq):
    if not seq:
        yield []; return
    first=seq[0]
    for rest in partitions(seq[1:]):
        yield [[first]]+[b[:] for b in rest]
        for i in range(len(rest)):
            new=[b[:] for b in rest]; new[i]=[first]+new[i]; yield new

def coeff(k): return (-1)**(k-1)*math.factorial(k-1)

def expectation_Y(offsets,Q,allowed,pA):
    total=0.0
    for x in range(Q):
        prod=1.0
        for h in offsets:
            prod *= (1 if ((x+h)%Q) in allowed else 0)/pA - 1
        total += prod/Q
    return total

def cumulant(offsets,Q,allowed,pA):
    idx=list(range(len(offsets))); total=0.0
    for part in partitions(idx):
        prod=1.0
        for block in part:
            prod*=expectation_Y([offsets[i] for i in block],Q,allowed,pA)
        total+=coeff(len(part))*prod
    return total

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--k',type=int,default=3); ap.add_argument('--r',type=int,default=3); ap.add_argument('--fixed',default='1,5'); args=ap.parse_args()
    ps=primes_first(args.k); Q=1
    for p in ps: Q*=p
    allowed=[x for x in range(Q) if all(x%p for p in ps)]
    allowed=set(allowed); pA=len(allowed)/Q
    fixed=[int(x)%Q for x in args.fixed.split(',') if x.strip()]
    fixed=fixed[:args.r-1]
    while len(fixed)<args.r-1: fixed.append(len(fixed)+1)
    vals=[cumulant([h]+fixed,Q,allowed,pA) for h in range(Q)]
    print('primes Q r fixed pA sum mean maxAbs absSum')
    print(ps,Q,args.r,fixed,pA,f'{sum(vals):.12g}',f'{sum(vals)/Q:.12g}',f'{max(abs(x) for x in vals):.6g}',f'{sum(abs(x) for x in vals):.6g}')
if __name__=='__main__': main()
