#!/usr/bin/env python3
"""按 H 分桶统计 R,U,T 条件均值斜率。"""
import argparse
import math
from collections import defaultdict
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L H count R/H U/H T/H S/H meanR meanU meanT')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P); L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P); plist = primes(flags, P * P + P); small = primes(sieve(B), B)
        step = max(1, L // 8)
        buckets = defaultdict(lambda: {'R': [], 'U': [], 'T': []})
        for row in range(1, P + 1):
            pref = {k: [0] * (P + 1) for k in ('H', 'R', 'U', 'T')}
            for c in range(1, P + 1):
                n = (row - 1) * P + c
                vals = {k: 0 for k in pref}
                if all(n % q for q in small):
                    vals['H'] = 1
                    if not flags[n]:
                        fac = factor_distinct(n, plist)
                        if all(q > B for q in fac):
                            if len(fac) == 2:
                                vals['R' if min(fac) <= L else 'U'] = 1
                            elif len(fac) == 3:
                                vals['T'] = 1
                for k in pref:
                    pref[k][c] = pref[k][c - 1] + vals[k]
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                H = pref['H'][end] - pref['H'][start - 1]
                if H == 0:
                    continue
                for k in ('R', 'U', 'T'):
                    buckets[H][k].append(pref[k][end] - pref[k][start - 1])
        for H in sorted(buckets):
            count = len(buckets[H]['R'])
            if count < 20:
                continue
            means = {k: mean(buckets[H][k]) for k in ('R', 'U', 'T')}
            print(P, args.C, L, H, count, *(f'{means[k]/H:.3f}' for k in ('R','U','T')), f'{sum(means.values())/H:.3f}', *(f'{means[k]:.3f}' for k in ('R','U','T')))


if __name__ == '__main__':
    main()
