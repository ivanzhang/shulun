#!/usr/bin/env python3
"""扫描 H_c(P,a) 在 a 上的分布、均值、方差、极值偏差。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def quantile(xs, q):
    xs=sorted(xs); idx=int(q*(len(xs)-1)); return xs[idx]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001,8009'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P c y mean std min q05 med q95 max meanConst minConst std/sqrtMean minDev/std')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_count(P,a,y,small) for a in range(1,P)]
        mu=mean(vals); sd=pstdev(vals); mn=min(vals); mx=max(vals); scale=P/math.log(P)
        print(f'{P} {args.c:.2f} {y} {mu:.3f} {sd:.3f} {mn} {quantile(vals,0.05)} {quantile(vals,0.5)} {quantile(vals,0.95)} {mx} {mu/scale:.4f} {mn/scale:.4f} {sd/math.sqrt(mu):.3f} {(mu-mn)/sd if sd else 0:.3f}')
if __name__=='__main__': main()
