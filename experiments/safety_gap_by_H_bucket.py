#!/usr/bin/env python3
"""按 H 候选数分桶统计 S/H，用于建立条件期望 alpha(H)。

用法示例：
  python3 experiments/safety_gap_by_H_bucket.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from collections import defaultdict
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L H count meanS meanD meanS/H maxS/H')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P); L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P); plist = primes(flags, P * P + P); small = primes(sieve(B), B)
        step = max(1, L // 8)
        buckets = defaultdict(list)
        for row in range(1, P + 1):
            prefH = [0] * (P + 1); prefS = [0] * (P + 1)
            for c in range(1, P + 1):
                n = (row - 1) * P + c; H = S = 0
                if all(n % q for q in small):
                    H = 1
                    if not flags[n]:
                        fac = factor_distinct(n, plist)
                        if all(q > B for q in fac) and len(fac) in (2, 3):
                            S = 1
                prefH[c] = prefH[c - 1] + H; prefS[c] = prefS[c - 1] + S
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                H = prefH[end] - prefH[start - 1]
                S = prefS[end] - prefS[start - 1]
                buckets[H].append(S)
        for H in sorted(buckets):
            vals = buckets[H]
            if len(vals) < 5:
                continue
            print(P, args.C, L, H, len(vals), f'{mean(vals):.3f}', f'{H-mean(vals):.3f}', f'{mean(vals)/H if H else 0:.3f}', f'{max(vals)/H if H else 0:.3f}')


if __name__ == '__main__':
    main()
