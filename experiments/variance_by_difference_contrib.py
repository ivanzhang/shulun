#!/usr/bin/env python3
"""方差按差分 d 的贡献分解。"""
import argparse, math
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix


def factor(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0: n//=d; e+=1
            out.append((d,e))
        d+=1 if d==2 else 2
    if n>1: out.append((n,1))
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--top',type=int,default=25); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); H=[sum(row) for row in A]; mu=mean(H); base=(mu/P)**2
    contrib=[]
    total=0.0
    for d in range(1,P):
        pairs=P-d
        e=sum((row[r] & row[r+d]) for row in A for r in range(pairs))/((P-1)*pairs)
        # 对 H^2 方差贡献：2*(P-d)*(E_pair - roughly p_r p_s)。这里用全局 base 近似看差分贡献。
        cval=2*pairs*(e-base)
        total+=cval
        contrib.append((cval,d,e,e/base if base else 0,factor(d)))
    contrib.sort(reverse=True)
    print(f'P={P} mu={mu:.3f} base={base:.6f} totalApproxOff={total:.3f}')
    print('top positive cval d ratio factors')
    for cval,d,e,ratio,fac in contrib[:args.top]: print(round(cval,3), d, round(ratio,3), fac)
    print('top negative')
    for cval,d,e,ratio,fac in sorted(contrib)[:args.top]: print(round(cval,3), d, round(ratio,3), fac)
if __name__=='__main__': main()
