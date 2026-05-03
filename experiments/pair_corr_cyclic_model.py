#!/usr/bin/env python3
"""环形差分二点相关，消除边界效应。"""
import argparse, math
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix
from high_threshold_margin_fast import sieve, primes
from pair_corr_singular_model import model_ratio


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--show',type=int,default=15); args=ap.parse_args()
    P=args.P; flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
    A=alive_matrix(P,args.c); H=[sum(row) for row in A]; p=mean(H)/P
    rows=[]
    for d in range(1,P):
        total=sum((row[r]&row[(r+d)%P]) for row in A for r in range(P))
        e=total/((P-1)*P); real=e/(p*p) if p else 0; mod=model_ratio(d,small)
        rows.append((abs(real-mod),real,mod,d))
    rows.sort(reverse=True)
    print(f'P={P} c={args.c} p={p:.6f} MAE={mean([r[0] for r in rows]):.4f}')
    for err,real,mod,d in rows[:args.show]: print(round(err,3), round(real,3), round(mod,3), d)
if __name__=='__main__': main()
