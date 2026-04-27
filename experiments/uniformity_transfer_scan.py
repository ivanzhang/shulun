#!/usr/bin/env python3
"""幸存集加性均匀传递扫描。

对模板覆盖筛每一步 S_i，统计在 q<=qmax 上的最大加性桶偏差：
max_b count(S_i mod q=b)-|S_i|/q。

用法示例：
  python3 experiments/uniformity_transfer_scan.py --Ps 997,1999,4001 --K 12 --qmax 120
"""
import argparse
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def step_survivor_sets(P, A, y, K):
    """返回聚合后的每步幸存集。"""
    groups = template_groups(P, A, y, K)
    step_sets = defaultdict(list)
    for group in groups:
        survivors = set(group['anchors'])
        step_sets[0].extend(survivors)
        for idx, r in enumerate(group['holes'], start=1):
            survivors = {a for a in survivors if covered_by_patch(P, a, r, y)}
            step_sets[idx].extend(survivors)
    return step_sets


def max_additive_deviation(values, y, qmax, P):
    """计算给定集合在 q<=qmax 的最大加性偏差。"""
    size = len(values)
    best = (0.0, None, 0, 0.0)
    for q in primes_upto(qmax):
        if q <= y or q == P:
            continue
        counts = Counter(a % q for a in values)
        max_bucket = max(counts.values(), default=0)
        expected = size / q if q else 0
        add = max_bucket - expected
        if add > best[0]:
            best = (add, q, max_bucket, expected)
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='997,1999,4001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--qmax', type=int, default=120)
    args = parser.parse_args()

    print('P step size max_add q max_bucket expected add_over_sqrt')
    for P in parse_ps(args.Ps):
        step_sets = step_survivor_sets(P, args.A, args.y, args.K)
        for step in range(0, args.K + 1):
            vals = step_sets[step]
            if not vals:
                print(P, step, 0, 0, None, 0, 0, 0)
                continue
            add, q, max_bucket, expected = max_additive_deviation(vals, args.y, args.qmax, P)
            add_over_sqrt = add / (len(vals) ** 0.5)
            print(P, step, len(vals), f'{add:.3f}', q, max_bucket, f'{expected:.3f}', f'{add_over_sqrt:.3f}')


if __name__ == '__main__':
    main()
