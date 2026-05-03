#!/usr/bin/env python3
"""扫描 C=4 纯 S2 折返链候选 q,r。

理论模型：中心 n=qr，左右端点 q(r-a)、r(q-b)，其中有效差分 a*q,b*r，a,b∈{2,4}。
要求端点也是 sqrt(P)-粗半素数，因此 r-a、q-b 需为 >sqrt(P) 的素数。

用法示例：
  python3 experiments/pure_s2_fold_chain_scan.py --Ps 503,1009,2003,4001 --C 4
"""
import argparse
import math
from collections import Counter

from high_threshold_margin_fast import sieve, primes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003,4001')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P B L qCount pairCount chainCount byShift sample')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P)
        qs = [q for q in primes(sieve(2 * B + 10), 2 * B + 10) if B < q <= 2 * B]
        qset = set(qs)
        by_shift = Counter()
        samples = []
        chain_count = 0
        pair_count = 0
        for q in qs:
            for r in qs:
                if q == r:
                    continue
                # 中心 qr 必须在 P^2 范围内，且窗口折返跨度 <= L。
                if q * r >= P * P:
                    continue
                pair_count += 1
                for a in (2, 4):
                    for b in (2, 4):
                        if max(a * q, b * r) > L:
                            continue
                        if q - b <= B or r - a <= B:
                            continue
                        if flags[q - b] and flags[r - a]:
                            chain_count += 1
                            by_shift[(a, b)] += 1
                            if len(samples) < 8:
                                samples.append((q, r, a, b, q - b, r - a))
        print(P, B, L, len(qs), pair_count, chain_count, dict(by_shift), samples)


if __name__ == '__main__':
    main()
