#!/usr/bin/env python3
"""二点相关与局部奇异级数模型对比。"""
import argparse, math
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix
from high_threshold_margin_fast import sieve, primes


def model_ratio(d, small):
    # 相对 p^2 的模型：prod local pair / prod single^2
    ratio=1.0
    for q in small:
        single=1-1/q
        if d%q==0:
            pair=1-1/q
        else:
            pair=1-2/q
            if pair<=0: return 0.0
        ratio *= pair/(single*single)
    return ratio

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--show',type=int,default=20); args=ap.parse_args()
    P=args.P; flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
    A=alive_matrix(P,args.c); H=[sum(row) for row in A]; p=mean(H)/P
    rows=[]
    for d in range(1,P):
        pairs=P-d
        e=sum((row[r]&row[r+d]) for row in A for r in range(pairs))/((P-1)*pairs)
        real=e/(p*p) if p else 0
        mod=model_ratio(d,small)
        rows.append((abs(real-mod), real, mod, d))
    rows.sort(reverse=True)
    print(f'P={P} c={args.c} p={p:.6f}')
    print('largest abs error real model d')
    for err,real,mod,d in rows[:args.show]: print(round(err,3), round(real,3), round(mod,3), d)
    mae=mean([r[0] for r in rows]); print('MAE',mae)
if __name__=='__main__': main()
