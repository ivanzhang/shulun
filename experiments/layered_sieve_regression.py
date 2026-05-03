#!/usr/bin/env python3
"""多层筛余特征线性回归预测 H_0.8，探索 martingale/层结构。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count
from truncated_mobius_predictor import corr


def solve_linear(X, y):
    # small normal equation with Gaussian elimination
    n=len(X); m=len(X[0])
    A=[[sum(X[i][j]*X[i][k] for i in range(n)) for k in range(m)] for j in range(m)]
    b=[sum(X[i][j]*y[i] for i in range(n)) for j in range(m)]
    for i in range(m):
        piv=max(range(i,m), key=lambda r: abs(A[r][i]))
        A[i],A[piv]=A[piv],A[i]; b[i],b[piv]=b[piv],b[i]
        div=A[i][i] or 1e-12
        for j in range(i,m): A[i][j]/=div
        b[i]/=div
        for r in range(m):
            if r==i: continue
            fac=A[r][i]
            for j in range(i,m): A[r][j]-=fac*A[i][j]
            b[r]-=fac*b[i]
    return b

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--thetas',default='0.3,0.4,0.5,0.6,0.7'); args=ap.parse_args()
    P=args.P; flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
    real=[H_count(P,a,y,small) for a in range(1,P)]
    feats=[]
    for th in [float(x) for x in args.thetas.split(',') if x.strip()]:
        y0=int(P**th); small0=[q for q in root if q<=y0]
        feats.append([H_count(P,a,y0,small0) for a in range(1,P)])
    X=[[1]+[f[i] for f in feats] for i in range(P-1)]
    beta=solve_linear(X,real)
    pred=[sum(beta[j]*X[i][j] for j in range(len(beta))) for i in range(P-1)]
    err=[p-r for p,r in zip(pred,real)]
    print(f'P={P} realMean={mean(real):.3f} realStd={pstdev(real):.3f} realMin={min(real)}')
    print('beta', [round(b,4) for b in beta])
    print(f'predStd={pstdev(pred):.3f} predMin={min(pred):.2f} corr={corr(pred,real):.3f} errStd={pstdev(err):.3f} maxAbsErr={max(abs(e) for e in err):.2f}')
if __name__=='__main__': main()
