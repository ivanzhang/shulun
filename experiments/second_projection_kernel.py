#!/usr/bin/env python3
"""检验四点中心化核二阶投影与二点相关核的关系。

K2(a,b) ≈ E_{c,d} K(a,b,c,d)。比较 K2/p^4 与 rho2(a-b)-1。
"""
import argparse
import random
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from fourth_kernel_projection import prob_subset, kernel
from pair_corr_singular_model import model_ratio


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--P',type=int,default=1009)
    ap.add_argument('--c',type=float,default=0.8)
    ap.add_argument('--pairs',type=int,default=120)
    ap.add_argument('--inner',type=int,default=800)
    ap.add_argument('--seed',type=int,default=1)
    args=ap.parse_args()
    random.seed(args.seed)
    flags=sieve(args.P); root=primes(flags,args.P); small=[q for q in root if q<=int(args.c*args.P)]
    p=prob_subset([0],small); p4=p**4
    rec=[]
    for _ in range(args.pairs):
        a,b=random.sample(range(args.P),2)
        vals=[]
        for _ in range(args.inner):
            c=random.randrange(args.P); d=random.randrange(args.P)
            vals.append(kernel([a,b,c,d],small,p))
        k2=mean(vals)/p4
        rho=model_ratio(abs(a-b),small)
        rec.append((k2,rho-1,abs(a-b)))
    mk=mean(x[0] for x in rec); mr=mean(x[1] for x in rec)
    cov=mean((x[0]-mk)*(x[1]-mr) for x in rec)
    vk=mean((x[0]-mk)**2 for x in rec); vr=mean((x[1]-mr)**2 for x in rec)
    corr=cov/(vk*vr)**0.5 if vk and vr else 0
    # 最小二乘 k2 ≈ alpha*(rho-1)+beta
    alpha=cov/vr if vr else 0; beta=mk-alpha*mr
    err=mean(abs(x[0]-(alpha*x[1]+beta)) for x in rec)
    print(f'P={args.P} p={p:.8g} pairs={args.pairs} inner={args.inner}')
    print(f'meanK2={mk:.6g} meanRhoMinus1={mr:.6g} corr={corr:.4f} alpha={alpha:.4f} beta={beta:.4g} meanAbsErr={err:.4g}')
    print('sample k2 rhoMinus1 d')
    for row in rec[:15]: print(f'{row[0]:.5g} {row[1]:.5g} {row[2]}')

if __name__=='__main__': main()
