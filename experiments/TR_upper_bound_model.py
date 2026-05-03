#!/usr/bin/env python3
"""T/R 安全间隙的保守上界模型扫描。

输出实际 alpha_R, alpha_T，并给出两个粗略理论代理：
  R_proxy = sum_{B<u<=4B, prime u} 1/u / log(P^2/u) 的归一化趋势；
  T_proxy = 三粗因子数量 / 小筛候选数量。

用法示例：
  python3 experiments/TR_upper_bound_model.py --Ps 503,1009,2003,4001 --C 4
"""
import argparse
import math
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003,4001')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P B L meanH meanR meanT alphaR alphaT R_sum1u R_proxy T_crude')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P); L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P); plist = primes(flags, P * P + P); small = primes(sieve(B), B)
        step = max(1, L // 8)
        Hs=[]; Rs=[]; Ts=[]
        for row in range(1, P + 1):
            prefH=[0]*(P+1); prefR=[0]*(P+1); prefT=[0]*(P+1)
            for c in range(1, P + 1):
                n=(row-1)*P+c; H=R=T=0
                if all(n%q for q in small):
                    H=1
                    if not flags[n]:
                        fac=factor_distinct(n, plist)
                        if all(q>B for q in fac):
                            if len(fac)==2 and min(fac)<=L:
                                R=1
                            elif len(fac)==3:
                                T=1
                prefH[c]=prefH[c-1]+H; prefR[c]=prefR[c-1]+R; prefT[c]=prefT[c-1]+T
            for start in range(1, P-L+2, step):
                end=start+L-1
                Hs.append(prefH[end]-prefH[start-1]); Rs.append(prefR[end]-prefR[start-1]); Ts.append(prefT[end]-prefT[start-1])
        large_primes=[q for q in primes(sieve(L), L) if q>B]
        sum1u=sum(1/q for q in large_primes)
        # 代理项只看量纲，不作为严格常数。
        r_proxy=sum(1/(q*max(1, math.log((P*P)/q))) for q in large_primes)
        # 粗 T 代理：Landau 型 loglog^2/log^3 的量纲。
        logP=math.log(P); t_crude=(math.log(logP)**2)/(logP**2) if logP>1 else 0
        print(P,B,L,f'{mean(Hs):.3f}',f'{mean(Rs):.3f}',f'{mean(Ts):.3f}',f'{mean(Rs)/mean(Hs):.3f}',f'{mean(Ts)/mean(Hs):.3f}',f'{sum1u:.3f}',f'{r_proxy:.4f}',f'{t_crude:.4f}')


if __name__=='__main__': main()
