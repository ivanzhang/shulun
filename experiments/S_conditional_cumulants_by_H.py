#!/usr/bin/env python3
"""按 H 分桶统计 S 的条件 cumulant 量级。"""
import argparse, math
from collections import defaultdict
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P C L H count k2/H k3/H k4/H k4/k2^2 absK3OverH')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P)))
        flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B); step=max(1,L//8)
        buckets=defaultdict(list)
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
                buckets[H].append(S)
        for H in sorted(buckets):
            vals=buckets[H]
            if len(vals)<100: continue
            mu=mean(vals); cen=[v-mu for v in vals]
            m2=mean(x*x for x in cen); m3=mean(x**3 for x in cen); m4=mean(x**4 for x in cen)
            k2=m2; k3=m3; k4=m4-3*m2*m2
            print(P,args.C,L,H,len(vals),f'{k2/H:.4f}',f'{k3/H:.4f}',f'{k4/H:.4f}',f'{k4/(k2*k2) if k2 else 0:.4f}',f'{abs(k3)/H:.4f}')
if __name__=='__main__': main()
