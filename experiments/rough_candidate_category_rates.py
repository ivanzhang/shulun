#!/usr/bin/env python3
"""统计整行 sqrt(P)-小筛候选中的 prime/semiprime/triple 比例，与坏段对比。"""
import argparse, math
from statistics import mean
from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def row_rates(P,row,flags,plist,small,B):
    cand=prime=semi=triple=other=0
    for c in range(1,P+1):
        n=(row-1)*P+c
        if all(n%q for q in small):
            cand+=1
            if flags[n]: prime+=1
            else:
                fac=factor_distinct(n,plist)
                if all(q>B for q in fac):
                    if len(fac)==2: semi+=1
                    elif len(fac)==3: triple+=1
                    else: other+=1
                else: other+=1
    return cand,prime,semi,triple,other


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--Ps',default='503,1009,2003,4001,8009'); ap.add_argument('--top',type=int,default=4); args=ap.parse_args()
    print('P B avgCand avgPrimeRate avgSemiRate avgTripleRate lowRows')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B=math.isqrt(P); flags=sieve(P*P+P); plist=primes(flags,P*P+P); small=primes(sieve(B),B)
        rates=[]; low=[]
        for row in range(1,P+1):
            cand,prime,semi,triple,other=row_rates(P,row,flags,plist,small,B)
            if cand:
                rates.append((cand,prime/cand,semi/cand,triple/cand,other/cand))
            pc=sum(1 for c in range(1,P+1) if flags[(row-1)*P+c])
            low.append((pc,row,cand,prime,semi,triple))
        print(P,B,round(mean(x[0] for x in rates),2),round(mean(x[1] for x in rates),3),round(mean(x[2] for x in rates),3),round(mean(x[3] for x in rates),3),sorted(low)[:args.top])

if __name__=='__main__': main()
