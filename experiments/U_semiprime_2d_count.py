#!/usr/bin/env python3
"""U 的二维 (u,v) 半素数点计数验证。

U 总点：n=uv<=P^2，L<u<=v，u,v prime，并且 n 不被小素数<=B整除自动成立。
比较：全方阵 U 点数、窗口平均 U、以及二维积分代理。

用法示例：
  python3 experiments/U_semiprime_2d_count.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P B L totalH totalU2d totalUscan densityU/H winMeanH winMeanU alphaU piLayerPairs')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P); L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P); plist = primes(flags, P * P + P); small = primes(sieve(B), B)
        # 二维 U 计数。
        ps = primes(flags, P * P + P)
        usable_u = [u for u in ps if L < u <= P]
        total_u2d = 0
        for u in usable_u:
            hi = (P * P) // u
            if hi < u:
                continue
            # v prime in [u, hi]
            total_u2d += sum(1 for v in ps if u <= v <= hi)
        # 直接扫描全方阵 H/U。
        totalH = totalUscan = 0
        for n in range(1, P * P + 1):
            if all(n % q for q in small):
                totalH += 1
                if not flags[n]:
                    fac = factor_distinct(n, plist)
                    if len(fac) == 2 and all(q > B for q in fac) and min(fac) > L:
                        totalUscan += 1
        # 窗口平均。
        step = max(1, L // 8)
        Hs=[]; Us=[]
        for row in range(1, P + 1):
            prefH=[0]*(P+1); prefU=[0]*(P+1)
            for c in range(1, P + 1):
                n=(row-1)*P+c; H=U=0
                if all(n%q for q in small):
                    H=1
                    if not flags[n]:
                        fac=factor_distinct(n, plist)
                        if len(fac)==2 and all(q>B for q in fac) and min(fac)>L:
                            U=1
                prefH[c]=prefH[c-1]+H; prefU[c]=prefU[c-1]+U
            for start in range(1, P-L+2, step):
                end=start+L-1
                Hs.append(prefH[end]-prefH[start-1]); Us.append(prefU[end]-prefU[start-1])
        print(P,B,L,totalH,total_u2d,totalUscan,f'{totalUscan/totalH:.4f}',f'{mean(Hs):.3f}',f'{mean(Us):.3f}',f'{mean(Us)/mean(Hs):.4f}',len(usable_u))


if __name__ == '__main__':
    main()
