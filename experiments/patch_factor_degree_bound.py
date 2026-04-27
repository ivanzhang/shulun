#!/usr/bin/env python3
"""统计 B_y 洞合数的补丁素因子个数上界。

用法示例：
  python3 experiments/patch_factor_degree_bound.py --P 8009 --K 20
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from demand_side_bad_prefix import prime_anchors
from hole_index_prime_rate import factor, isprimefac
from shared_patch_energy import front_holes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=8009)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=20)
    args = parser.parse_args()

    degree = Counter()
    examples = []
    for a in prime_anchors(args.P, args.A):
        for r in front_holes(args.P, a, args.y, args.K):
            n = a + r * args.P
            fac = factor(n)
            if isprimefac(fac, n):
                continue
            patches = [q for q, _ in fac if q > args.y and q <= math.isqrt(n) and q != args.P]
            degree[len(patches)] += 1
            if len(patches) >= 4 and len(examples) < 10:
                examples.append((a, r, n, fac, patches))
    print('P', args.P, 'degree', sorted(degree.items()))
    print('examples_ge4', examples)


if __name__ == '__main__':
    main()
