#!/usr/bin/env python3
"""采样/枚举三点中心化核，按是否有小差分碰撞分类。"""
import argparse, random, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from fourth_kernel_projection import prob_subset


def k3(R, small, p):
    a,b,c=R
    p1=p
    p2ab=prob_subset([a,b],small); p2ac=prob_subset([a,c],small); p2bc=prob_subset([b,c],small)
    p3=prob_subset([a,b,c],small)
    return p3 - p*(p2ab+p2ac+p2bc) + 2*p**3


def factor_score(ds):
    # 简单碰撞强度：gcd 差分的倒数素因子权重近似，用 gcd of product not needed
    return min(ds), math.gcd(ds[0], math.gcd(ds[1], ds[2]))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--samples',type=int,default=30000); ap.add_argument('--seed',type=int,default=1); args=ap.parse_args()
    random.seed(args.seed); flags=sieve(args.P); root=primes(flags,args.P); small=[q for q in root if q<=int(args.c*args.P)]; p=prob_subset([0],small)
    vals=[]; buckets={}
    for _ in range(args.samples):
        R=random.sample(range(args.P),3)
        val=k3(R,small,p)/(p**3)
        ds=[abs(R[0]-R[1]),abs(R[0]-R[2]),abs(R[1]-R[2])]
        mind,g=factor_score(ds)
        key='g>1' if g>1 else ('near' if mind<=10 else 'generic')
        buckets.setdefault(key,[]).append(val); vals.append(val)
    print(f'P={args.P} p={p:.8g} samples={args.samples} meanK3/p3={mean(vals):.6g} absMean={mean(abs(x) for x in vals):.6g}')
    for k,a in sorted(buckets.items()): print(k, len(a), f'mean={mean(a):.6g}', f'abs={mean(abs(x) for x in a):.6g}', f'max={max(abs(x) for x in a):.3g}')

if __name__=='__main__': main()
