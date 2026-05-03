#!/usr/bin/env python3
"""分解 H 的三阶中心矩：模式 (3),(2,1),(1,1,1)。"""
import argparse
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); n=len(A); H=[sum(row) for row in A]; mu=mean(H)
    m3=mean((h-mu)**3 for h in H); var=mean((h-mu)**2 for h in H)
    pr=[mean(row[r] for row in A) for r in range(P)]
    Y=[[row[r]-pr[r] for r in range(P)] for row in A]
    c3=0.0
    for r in range(P): c3 += mean(row[r]**3 for row in Y)
    c21=0.0
    for r in range(P):
        yr2=[row[r]**2 for row in Y]
        for s in range(P):
            if s!=r: c21 += 3*mean(yr2[i]*Y[i][s] for i in range(n))
    c111=m3-c3-c21
    print(f'P={P} mu={mu:.6f} var={var:.6f} m3={m3:.6f} m3/var^1.5={m3/(var**1.5):.4f}')
    print(f'pattern3={c3:.6f} ratioMu={c3/mu:.4f}')
    print(f'pattern21={c21:.6f} ratioMu={c21/mu:.4f} ratioMu2={c21/(mu*mu):.4f}')
    print(f'pattern111={c111:.6f} ratioMu={c111/mu:.4f} ratioMu2={c111/(mu*mu):.4f}')

if __name__=='__main__': main()
