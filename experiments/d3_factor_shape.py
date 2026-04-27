#!/usr/bin/env python3
"""统计 d=3 点的补丁因子形状。

用法示例：
  python3 experiments/d3_factor_shape.py --P 16001 --step 4 --top 20
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups, covered_by_patch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=16001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=8)
    parser.add_argument('--step', type=int, default=4)
    parser.add_argument('--top', type=int, default=20)
    args = parser.parse_args()

    shapes = Counter()
    examples = []
    count = 0
    for group in template_groups(args.P, args.A, args.y, args.K):
        survivors = set(group['anchors'])
        target_r = None
        for idx, r in enumerate(group['holes'], start=1):
            if idx == args.step:
                target_r = r
                break
            survivors = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}
        if not survivors:
            continue
        for a in survivors:
            n = a + target_r * args.P
            patches = [q for q, _ in factor(n) if q > args.y and q <= math.isqrt(n) and q != args.P]
            if len(patches) == 3:
                count += 1
                product = math.prod(patches)
                cofactor = n // product
                shapes[(patches[0], patches[1])] += 1
                if len(examples) < args.top:
                    examples.append((a, target_r, n, patches, cofactor))
    print('P', args.P, 'step', args.step, 'd3_count', count)
    print('top_first_two', shapes.most_common(args.top))
    print('examples', examples)


if __name__ == '__main__':
    main()
