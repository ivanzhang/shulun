#!/usr/bin/env python3
"""用素因子筛快速估计前洞数中 >=4 补丁因子的比例。

用法示例：
  python3 experiments/four_patch_rate_by_sieve.py --P 32003 --K 12
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from demand_side_bad_prefix import prime_anchors
from fixed_anchor_sieve_remainder import primes_upto
from shared_patch_energy import front_holes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=32003)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    args = parser.parse_args()

    anchors = prime_anchors(args.P, args.A)
    triples = []
    nmax = 0
    for a in anchors:
        holes = front_holes(args.P, a, args.y, args.K)
        for idx, r in enumerate(holes, start=1):
            n = a + r * args.P
            triples.append((idx, n))
            nmax = max(nmax, n)
    counts = [0] * (nmax + 1)
    for q in primes_upto(math.isqrt(nmax)):
        if q <= args.y or q == args.P:
            continue
        for m in range(q, nmax + 1, q):
            counts[m] += 1
    before = Counter()
    ge4 = Counter()
    for idx, n in triples:
        before[idx] += 1
        if counts[n] >= 4:
            ge4[idx] += 1
    print('P', args.P, 'N', len(anchors), 'K', args.K, 'nmax', nmax)
    print('idx before ge4 rate')
    for idx in range(1, args.K + 1):
        print(idx, before[idx], ge4[idx], f'{ge4[idx]/before[idx] if before[idx] else 0:.5f}')


if __name__ == '__main__':
    main()
