#!/usr/bin/env python3
"""局部窗口 H,S2,T3,Z 的协方差矩阵，分解 Var(D)。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def cov(xs,ys):
    mx=mean(xs); my=mean(ys)
    return mean((x-mx)*(y-my) for x,y in zip(xs,ys))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--Cs',default='4,5,6'); args=ap.parse_args()
    print('P C L meanH meanS meanT meanD varH varS varT covHS covHT covST varD reconstructed')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        for C in [float(x) for x in args.Cs.split(',') if x.strip()]:
            L=max(1,int(C*math.sqrt(P))); step=max(1,L//8)
            Hs=[]; Ss=[]; Ts=[]; Ds=[]
            for row in range(1,P+1):
                prefH=[0]*(P+1); prefS=[0]*(P+1); prefT=[0]*(P+1)
                for c in range(1,P+1):
                    n=(row-1)*P+c; H=S=T=0
                    if all(n%q for q in small):
                        H=1
                        if not flags[n]:
                            fac=factor_distinct(n,plist)
                            if all(q>B for q in fac):
                                if len(fac)==2: S=1
                                elif len(fac)==3: T=1
                    prefH[c]=prefH[c-1]+H; prefS[c]=prefS[c-1]+S; prefT[c]=prefT[c-1]+T
                for start in range(1,P-L+2,step):
                    end=start+L-1
                    H=prefH[end]-prefH[start-1]; S=prefS[end]-prefS[start-1]; T=prefT[end]-prefT[start-1]; D=H-S-T
                    Hs.append(H); Ss.append(S); Ts.append(T); Ds.append(D)
            varH=cov(Hs,Hs); varS=cov(Ss,Ss); varT=cov(Ts,Ts); covHS=cov(Hs,Ss); covHT=cov(Hs,Ts); covST=cov(Ss,Ts); varD=cov(Ds,Ds)
            rec=varH+varS+varT-2*covHS-2*covHT+2*covST
            print(P,C,L,f'{mean(Hs):.3f}',f'{mean(Ss):.3f}',f'{mean(Ts):.3f}',f'{mean(Ds):.3f}',f'{varH:.3f}',f'{varS:.3f}',f'{varT:.3f}',f'{covHS:.3f}',f'{covHT:.3f}',f'{covST:.3f}',f'{varD:.3f}',f'{rec:.3f}')

if __name__=='__main__': main()
