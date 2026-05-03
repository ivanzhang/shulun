#!/usr/bin/env python3
"""H_c 分布高阶矩与极值 z-score。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='251,503,1009,2003,4001,8009'); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    print('P n mean sd minZ maxZ m3 m4 m6')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_count(P,a,y,small) for a in range(1,P)]
        mu=mean(vals); sd=pstdev(vals)
        zs=[(v-mu)/sd for v in vals]
        moms=[]
        for k in [3,4,6]: moms.append(mean([z**k for z in zs]))
        print(f'{P} {P-1} {mu:.3f} {sd:.3f} {min(zs):.3f} {max(zs):.3f} {moms[0]:.3f} {moms[1]:.3f} {moms[2]:.3f}')
if __name__=='__main__': main()
