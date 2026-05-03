#!/usr/bin/env python3
"""短除数特征回归：用小素数筛余 H_y0 与若干截断特征预测 H_z。"""
import argparse, math
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes, H_count
from truncated_mobius_predictor import squarefree_divisors, H_trunc, corr


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--P',type=int,default=1009); ap.add_argument('--c',type=float,default=0.8); ap.add_argument('--thetas',default='0.4,0.5,0.6,0.7'); args=ap.parse_args()
    P=args.P; flags=sieve(P); root=primes(flags,P); y=int(args.c*P); small=[q for q in root if q<=y]
    real=[H_count(P,a,y,small) for a in range(1,P)]
    print(f'P={P} real mean={mean(real):.3f} std={pstdev(real):.3f} min={min(real)}')
    for th in [float(x) for x in args.thetas.split(',') if x.strip()]:
        y0=int(P**th); small0=[q for q in root if q<=y0]
        feat=[H_count(P,a,y0,small0) for a in range(1,P)]
        # best linear fit real ≈ alpha feat + beta
        mf=mean(feat); mr=mean(real); var=sum((x-mf)**2 for x in feat); cov=sum((x-mf)*(y-mr) for x,y in zip(feat,real))
        alpha=cov/var if var else 0; beta=mr-alpha*mf
        pred=[alpha*x+beta for x in feat]; err=[p-r for p,r in zip(pred,real)]
        print(f'theta={th:.2f} y0={y0} featMean={mf:.2f} featStd={pstdev(feat):.2f} corr={corr(feat,real):.3f} alpha={alpha:.3f} errStd={pstdev(err):.3f} predMin={min(pred):.2f}')
if __name__=='__main__': main()
