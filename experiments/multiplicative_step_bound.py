#!/usr/bin/env python3
"""检查乘法筛单步保留率 1-prod(1-1/q) 的统一性。

用法示例：
  python3 experiments/multiplicative_step_bound.py --P 8009 --K 12
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def mult_cover_prob(y, Q, P):
    """乘法筛预测：被至少一个补丁素数命中的概率。"""
    prod = 1.0
    for q in primes_upto(Q):
        if q > y and q != P:
            prod *= (1 - 1 / q)
    return 1 - prod


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=8009)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    args = parser.parse_args()

    groups = template_groups(args.P, args.A, args.y, args.K)
    by_step = defaultdict(lambda: [0, 0, 0.0])
    for group in groups:
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            before = len(survivors)
            if before == 0:
                continue
            pred = sum(mult_cover_prob(args.y, math.isqrt(a + r * args.P), args.P) for a in survivors) / before
            after_set = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}
            after = len(after_set)
            by_step[idx][0] += before
            by_step[idx][1] += after
            by_step[idx][2] += pred * before
            survivors = after_set
    print('P', args.P)
    print('idx before after keep_rate mult_pred ratio')
    for idx in range(1, args.K + 1):
        before, after, pred_sum = by_step[idx]
        if before:
            pred = pred_sum / before
            print(idx, before, after, f'{after/before:.4f}', f'{pred:.4f}', f'{(after/before)/pred if pred else 0:.3f}')


if __name__ == '__main__':
    main()
