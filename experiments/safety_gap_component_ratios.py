#!/usr/bin/env python3
"""扫描 R/H、U/H、T/H 分量安全间隙。

用法示例：
  python3 experiments/safety_gap_component_ratios.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def quantile(vals, q):
    vals = sorted(vals)
    return vals[min(len(vals) - 1, max(0, int(q * (len(vals) - 1))))] if vals else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L n meanH meanR meanU meanT R/H U/H T/H S/H q95_R q95_U q95_T q95_S')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small = primes(sieve(B), B)
        step = max(1, L // 8)
        sums = {k: [] for k in ('H', 'R', 'U', 'T')}
        ratios = {k: [] for k in ('R', 'U', 'T', 'S')}
        for row in range(1, P + 1):
            pref = {k: [0] * (P + 1) for k in sums}
            for c in range(1, P + 1):
                n = (row - 1) * P + c
                vals = {k: 0 for k in sums}
                if all(n % q for q in small):
                    vals['H'] = 1
                    if not flags[n]:
                        fac = factor_distinct(n, plist)
                        if all(q > B for q in fac):
                            if len(fac) == 2:
                                vals['R' if min(fac) <= L else 'U'] = 1
                            elif len(fac) == 3:
                                vals['T'] = 1
                for k in sums:
                    pref[k][c] = pref[k][c - 1] + vals[k]
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                vals = {k: pref[k][end] - pref[k][start - 1] for k in sums}
                for k in sums:
                    sums[k].append(vals[k])
                H = vals['H']
                if H:
                    ratios['R'].append(vals['R'] / H)
                    ratios['U'].append(vals['U'] / H)
                    ratios['T'].append(vals['T'] / H)
                    ratios['S'].append((vals['R'] + vals['U'] + vals['T']) / H)
        print(
            P, args.C, L, len(ratios['S']),
            *(f'{mean(sums[k]):.3f}' for k in ('H', 'R', 'U', 'T')),
            *(f'{mean(ratios[k]):.3f}' for k in ('R', 'U', 'T', 'S')),
            *(f'{quantile(ratios[k], 0.95):.3f}' for k in ('R', 'U', 'T', 'S')),
        )


if __name__ == '__main__':
    main()
