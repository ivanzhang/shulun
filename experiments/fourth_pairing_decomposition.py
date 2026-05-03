#!/usr/bin/env python3
"""把真实 H 的四阶中心矩与二点协方差配对项比较。

理论：E(sum Y)^4 = 3-ish pairing sum + cumulant4 sum。
这里计算 Cov矩阵并求 3*sum Cov^2（对称完整索引）。
"""
import argparse
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); n=len(A)
    H=[sum(row) for row in A]; mu=mean(H)
    fourth=mean((h-mu)**4 for h in H); var=mean((h-mu)**2 for h in H)
    pr=[mean(row[r] for row in A) for r in range(P)]
    cov2sum=0.0
    # Cov(r,s)=E(Yr Ys)
    for r in range(P):
        for s in range(P):
            c=sum((row[r]-pr[r])*(row[s]-pr[s]) for row in A)/n
            cov2sum += c*c
    pairing=3*cov2sum
    print(f'P={P} mean={mu:.6f} var={var:.6f} fourth={fourth:.6f} cov2sum={cov2sum:.6f} pairing3={pairing:.6f} residual={fourth-pairing:.6f} residual/fourth={(fourth-pairing)/fourth:.4f}')

if __name__=='__main__': main()
