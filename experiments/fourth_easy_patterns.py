#!/usr/bin/env python3
"""精确计算四阶展开中 (4),(3,1),(2,2) 模式贡献。"""
import argparse
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=503); ap.add_argument('--c',type=float,default=0.8); args=ap.parse_args()
    P=args.P; A=alive_matrix(P,args.c); n=len(A); H=[sum(row) for row in A]; mu=mean(H); var=mean((h-mu)**2 for h in H); fourth=mean((h-mu)**4 for h in H)
    pr=[mean(row[r] for row in A) for r in range(P)]
    # 预计算 Y 矩阵为 float，P 中等即可
    Y=[[row[r]-pr[r] for r in range(P)] for row in A]
    c4=0.0
    for r in range(P):
        c4 += mean(y[r]**4 for y in Y)
    c31=0.0
    for r in range(P):
        vals_r3=[y[r]**3 for y in Y]
        for s in range(P):
            if s==r: continue
            c31 += 4*mean(vals_r3[i]*Y[i][s] for i in range(n))
    c22=0.0
    for r in range(P):
        vals_r2=[y[r]**2 for y in Y]
        for s in range(r+1,P):
            c22 += 6*mean(vals_r2[i]*(Y[i][s]**2) for i in range(n))
    print(f'P={P} mu={mu:.6f} var={var:.6f} fourth={fourth:.6f}')
    print(f'pattern4={c4:.6f} ratioMu={c4/mu:.4f} ratioFourth={c4/fourth:.4f}')
    print(f'pattern31={c31:.6f} ratioMu={c31/mu:.4f} ratioFourth={c31/fourth:.4f}')
    print(f'pattern22={c22:.6f} ratioMu2={c22/(mu*mu):.4f} ratioFourth={c22/fourth:.4f}')
    print(f'easySum={c4+c31+c22:.6f} residual={fourth-c4-c31-c22:.6f}')

if __name__=='__main__': main()
