#!/usr/bin/env python3
"""边界锚点集合在模 q 上的分布均匀性。

用法示例：
  python3 experiments/boundary_residue_uniformity.py --P 997 --qmax 100
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from zero_repair_boundary_scan import boundary_events


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=997)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--qmax', type=int, default=150)
    args = parser.parse_args()

    anchors = [x['a'] for x in boundary_events(args.P, args.y, args.P) if args.A < x['a'] < args.P]
    N = len(anchors)
    print(f'P={args.P}, anchors={N}, qmax={args.qmax}')
    print('q max_count avg N/q ratio occupied l2_excess')
    for q in primes_upto(args.qmax):
        if q <= args.y or q == args.P:
            continue
        counter = Counter(a % q for a in anchors)
        max_count = max(counter.values(), default=0)
        avg = N / q
        l2 = sum((counter.get(r, 0) - avg) ** 2 for r in range(q))
        print(q, max_count, f'{avg:.3f}', f'{max_count / max(1, avg):.2f}', len(counter), f'{l2:.2f}')


if __name__ == '__main__':
    main()
