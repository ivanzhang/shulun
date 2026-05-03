#!/usr/bin/env python3
"""扫描 S 相对 alpha*H 的残差尺度。

目标验证：S <= alpha H + O_prob(sqrt(H))，并估计 alpha=0.6,0.7,0.8 的安全余量。
"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--C',type=float,default=4.0); ap.add_argument('--alphas',default='0.6,0.7,0.8'); args=ap.parse_args()
    alphas=[float(x) for x in args.alphas.split(',')]
    print('P C L n meanH meanS minD alpha maxResidual maxResidualOverSqrtH violationRate')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P)))
        flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B); step=max(1,L//8)
        pairs=[]
        for row in range(1,P+1):
            prefH=[0]*(P+1); prefS=[0]*(P+1)
            for c in range(1,P+1):
                n=(row-1)*P+c; H=S=0
                if all(n%q for q in small):
                    H=1
                    if not flags[n]:
                        fac=factor_distinct(n,plist)
                        if all(q>B for q in fac) and len(fac) in (2,3): S=1
                prefH[c]=prefH[c-1]+H; prefS[c]=prefS[c-1]+S
            for start in range(1,P-L+2,step):
                end=start+L-1; H=prefH[end]-prefH[start-1]; S=prefS[end]-prefS[start-1]
                pairs.append((H,S))
        meanH=mean(h for h,s in pairs); meanS=mean(s for h,s in pairs); minD=min(h-s for h,s in pairs)
        for alpha in alphas:
            residuals=[s-alpha*h for h,s in pairs]
            scaled=[(s-alpha*h)/math.sqrt(max(h,1)) for h,s in pairs]
            print(P,args.C,L,len(pairs),f'{meanH:.3f}',f'{meanS:.3f}',minD,alpha,f'{max(residuals):.3f}',f'{max(scaled):.3f}',f'{sum(1 for r in residuals if r>0)/len(residuals):.5f}')
if __name__=='__main__': main()
