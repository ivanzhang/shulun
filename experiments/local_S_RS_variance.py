#!/usr/bin/env python3
"""S2=R(可复用u<=L)+U(单命中u>L) 的均值方差协方差分解。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def cov(xs,ys):
    mx=mean(xs); my=mean(ys)
    return mean((x-mx)*(y-my) for x,y in zip(xs,ys))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P L meanR meanU meanS varR varU covRU varS rec corrRU')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P))); step=max(1,L//4)
        flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        Rs=[]; Us=[]; Ss=[]
        for row in range(1,P+1):
            prefR=[0]*(P+1); prefU=[0]*(P+1)
            for c in range(1,P+1):
                n=(row-1)*P+c; R=U=0
                if all(n%q for q in small) and not flags[n]:
                    fac=factor_distinct(n,plist)
                    if all(q>B for q in fac) and len(fac)==2:
                        u=min(fac)
                        if u<=L: R=1
                        else: U=1
                prefR[c]=prefR[c-1]+R; prefU[c]=prefU[c-1]+U
            for start in range(1,P-L+2,step):
                end=start+L-1; R=prefR[end]-prefR[start-1]; U=prefU[end]-prefU[start-1]
                Rs.append(R); Us.append(U); Ss.append(R+U)
        varR=cov(Rs,Rs); varU=cov(Us,Us); covRU=cov(Rs,Us); varS=cov(Ss,Ss); rec=varR+varU+2*covRU
        corr=covRU/(varR*varU)**0.5 if varR and varU else 0
        print(P,L,f'{mean(Rs):.3f}',f'{mean(Us):.3f}',f'{mean(Ss):.3f}',f'{varR:.3f}',f'{varU:.3f}',f'{covRU:.3f}',f'{varS:.3f}',f'{rec:.3f}',f'{corr:.3f}')

if __name__=='__main__': main()
