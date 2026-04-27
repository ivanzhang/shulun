#!/usr/bin/env python3
"""固定模板每一步覆盖率与筛密度模型对比。

用法示例：
  python3 experiments/template_step_density_model.py --P 4001 --K 15
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def prime_sum(y, Q):
    """sum_{y<q<=Q} 1/q。"""
    return sum(1 / q for q in primes_upto(Q) if q > y)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=4001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=15)
    args = parser.parse_args()

    groups = template_groups(args.P, args.A, args.y, args.K)
    by_step = defaultdict(lambda: [0, 0, 0.0, 0.0])
    for group in groups:
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            before = len(survivors)
            if before == 0:
                continue
            # 用当前幸存者的平均 Q 预测该步合数覆盖率。
            avg_Q = sum(math.isqrt(a + r * args.P) for a in survivors) / before
            avg_sum = sum(prime_sum(args.y, math.isqrt(a + r * args.P)) for a in survivors) / before
            after_set = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}
            after = len(after_set)
            by_step[idx][0] += before
            by_step[idx][1] += after
            by_step[idx][2] += avg_Q * before
            by_step[idx][3] += avg_sum * before
            survivors = after_set

    print('P', args.P, 'K', args.K)
    print('idx before after keep_rate avg_Q avg_sum1q poisson_keep')
    for idx in range(1, args.K + 1):
        before, after, qsum, ssum = by_step[idx]
        if before == 0:
            continue
        avg_Q = qsum / before
        avg_sum = ssum / before
        # 若小补丁命中近似 Poisson，合数覆盖概率约 1-exp(-sum1q)。
        poisson_keep = 1 - math.exp(-avg_sum)
        print(idx, before, after, f'{after/before:.4f}', f'{avg_Q:.1f}', f'{avg_sum:.4f}', f'{poisson_keep:.4f}')


if __name__ == '__main__':
    main()
