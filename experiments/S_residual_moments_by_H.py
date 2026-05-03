#!/usr/bin/env python3
"""按 H 分桶估计 S 的条件残差矩，检验 Bernstein/Poisson 型高矩。

残差使用每个 H 桶内的 mean(S|H) 中心化。
"""
import argparse, math
from collections import defaultdict
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P C L H count meanS varS varOverH m4OverVar2 m6OverVar3 maxAbsOverSqrtH')
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
            if len(vals)<50: continue
            mu=mean(vals); cen=[v-mu for v in vals]; var=mean(x*x for x in cen)
            m4=mean(x**4 for x in cen); m6=mean(x**6 for x in cen)
            print(P,args.C,L,H,len(vals),f'{mu:.3f}',f'{var:.3f}',f'{var/H if H else 0:.3f}',f'{m4/(var*var) if var else 0:.3f}',f'{m6/(var**3) if var else 0:.3f}',f'{max(abs(x) for x in cen)/math.sqrt(H) if H else 0:.3f}')
if __name__=='__main__': main()
