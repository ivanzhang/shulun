#!/usr/bin/env python3
"""验证 connected cumulant 核的低阶投影消失。

对 K3(a,b)，固定 a 求 sum_b K3(a,b)。
对 K4(a,b,c)，固定 a,b 求 sum_c K4，或固定 a 求 sum_{b,c} K4（采样）。
"""
import argparse, math, random
from high_threshold_margin_fast import sieve, primes
from four_point_connected_cumulant_grid import EY
from three_point_singular_cumulant import weight


def K3(a,b,small,pB):
    w01=weight([0,a],small)/(pB*pB)
    w02=weight([0,b],small)/(pB*pB)
    w12=weight([a,b],small)/(pB*pB)
    w3=weight([0,a,b],small)/(pB**3)
    return w3-w01-w02-w12+2

def K4(a,b,c,small,pB):
    e4=EY([0,a,b,c],small,pB)
    return e4 - EY([0,a],small,pB)*EY([b,c],small,pB) - EY([0,b],small,pB)*EY([a,c],small,pB) - EY([0,c],small,pB)*EY([a,b],small,pB)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--sample-a',type=int,default=12); ap.add_argument('--seed',type=int,default=1); args=ap.parse_args()
    random.seed(args.seed); P=args.P; B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); small=primes(sieve(B),B)
    pB=1.0
    for p in small: pB*=1-1/p
    avals=sorted(random.sample(range(1,L+1), min(args.sample_a,L)))
    print('P B L type fixed sum count mean absMean')
    for a in avals:
        vals=[K3(a,b,small,pB) for b in range(1,L+1) if b!=a]
        print(P,B,L,'K3_sum_b',a,f'{sum(vals):.4f}',len(vals),f'{sum(vals)/len(vals):.6f}',f'{sum(abs(x) for x in vals)/len(vals):.6f}')
    # K4 固定 a,b 投影 sum_c，抽少量 pairs。
    pairs=[]
    while len(pairs)<min(args.sample_a, L*(L-1)//2):
        a,b=sorted(random.sample(range(1,L+1),2))
        if (a,b) not in pairs: pairs.append((a,b))
    for a,b in pairs:
        vals=[K4(a,b,c,small,pB) for c in range(1,L+1) if c not in (a,b)]
        print(P,B,L,'K4_sum_c',f'{a},{b}',f'{sum(vals):.4f}',len(vals),f'{sum(vals)/len(vals):.6f}',f'{sum(abs(x) for x in vals)/len(vals):.6f}')
if __name__=='__main__': main()
