#!/usr/bin/env python3
"""筛余分布尾部与高斯/亚高斯尺度比较。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='1009,2003,4001,8009'); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--zs',default='1,2,3,4'); args=ap.parse_args()
    print('P z leftProb rightProb gaussianTwoSidedBound minZ maxZ')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
        vals=[H_count(P,a,y,small) for a in range(1,P)]
        mu=mean(vals); sd=pstdev(vals); zs=[(v-mu)/sd for v in vals]
        for z in [float(x) for x in args.zs.split(',') if x.strip()]:
            lp=sum(1 for x in zs if x<=-z)/len(zs); rp=sum(1 for x in zs if x>=z)/len(zs); gb=2*math.exp(-z*z/2)
            print(f'{P} {z:.1f} {lp:.4f} {rp:.4f} {gb:.4f} {min(zs):.3f} {max(zs):.3f}')
if __name__=='__main__': main()
