#!/usr/bin/env python3
"""分解 S 条件方差的 pair 来源：对角、共享粗因子 pair、非共享 pair。

按窗口统计 S、pair 数和共享粗因子 pair 数，估计共享 pair 对 Var(S) 的贡献规模。
"""
import argparse, math
from collections import Counter
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def cov(xs, ys):
    mx=mean(xs); my=mean(ys)
    return mean((x-mx)*(y-my) for x,y in zip(xs,ys))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003'); ap.add_argument('--C',type=float,default=4.0); args=ap.parse_args()
    print('P C L n meanS varS meanPairs meanSharedPairs sharedFrac covS_shared corrS_shared')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); L=max(1,int(args.C*math.sqrt(P)))
        flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B); step=max(1,L//8)
        Ss=[]; pairCounts=[]; sharedCounts=[]
        for row in range(1,P+1):
            certs=[]
            for c in range(1,P+1):
                n=(row-1)*P+c
                if all(n%q for q in small) and not flags[n]:
                    fac=tuple(q for q in factor_distinct(n,plist) if q>B)
                    if len(fac) in (2,3): certs.append((c,fac))
            for start in range(1,P-L+2,step):
                end=start+L-1; items=[x for x in certs if start<=x[0]<=end]
                S=len(items); shared=0
                for i in range(S):
                    seti=set(items[i][1])
                    for j in range(i+1,S):
                        if seti & set(items[j][1]): shared+=1
                Ss.append(S); pairCounts.append(S*(S-1)//2); sharedCounts.append(shared)
        varS=cov(Ss,Ss); varShared=cov(sharedCounts,sharedCounts)
        corr=cov(Ss,sharedCounts)/math.sqrt(varS*varShared) if varS and varShared else 0
        print(P,args.C,L,len(Ss),f'{mean(Ss):.3f}',f'{varS:.3f}',f'{mean(pairCounts):.3f}',f'{mean(sharedCounts):.5f}',f'{mean(sharedCounts)/mean(pairCounts):.5f}',f'{cov(Ss,sharedCounts):.4f}',f'{corr:.3f}')
if __name__=='__main__': main()
