#!/usr/bin/env python3
"""扫描局部窗口 S/H 安全间隙。

H: sqrt(P)-小筛候选数；S=R+U+T: 小筛候选中的粗合数数；D=H-S: 素数数。
输出窗口级 S/H 的均值、极值和分位数，检验是否存在统一 alpha<1。

用法示例：
  python3 experiments/safety_gap_ratio_scan.py --Ps 503,1009,2003,4001 --C 4
"""
import argparse
import math
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def quantile(vals, q):
    if not vals:
        return 0.0
    vals = sorted(vals)
    idx = min(len(vals) - 1, max(0, int(q * (len(vals) - 1))))
    return vals[idx]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003,4001')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L n meanH meanS meanD meanS/H maxS/H q90 q95 q99 minD zeroD maxS_minus_H')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small = primes(sieve(B), B)
        step = max(1, L // 8)
        Hs, Ss, Ds, ratios = [], [], [], []
        for row in range(1, P + 1):
            prefH = [0] * (P + 1)
            prefS = [0] * (P + 1)
            for c in range(1, P + 1):
                n = (row - 1) * P + c
                H = S = 0
                if all(n % q for q in small):
                    H = 1
                    if not flags[n]:
                        fac = factor_distinct(n, plist)
                        if all(q > B for q in fac) and len(fac) in (2, 3):
                            S = 1
                prefH[c] = prefH[c - 1] + H
                prefS[c] = prefS[c - 1] + S
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                H = prefH[end] - prefH[start - 1]
                S = prefS[end] - prefS[start - 1]
                D = H - S
                Hs.append(H); Ss.append(S); Ds.append(D)
                if H:
                    ratios.append(S / H)
        print(
            P, args.C, L, len(ratios),
            f'{mean(Hs):.3f}', f'{mean(Ss):.3f}', f'{mean(Ds):.3f}',
            f'{mean(ratios):.3f}', f'{max(ratios):.3f}',
            f'{quantile(ratios,0.90):.3f}', f'{quantile(ratios,0.95):.3f}', f'{quantile(ratios,0.99):.3f}',
            min(Ds), sum(1 for d in Ds if d == 0), max(s - h for s, h in zip(Ss, Hs)),
        )


if __name__ == '__main__':
    main()
