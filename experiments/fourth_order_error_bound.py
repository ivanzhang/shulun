#!/usr/bin/env python3
"""四阶补丁重叠误差 H4 的实际量与 CRT 上界。

用法示例：
  python3 experiments/fourth_order_error_bound.py --P 8009 --step 1
"""
import argparse
import itertools
import math
import sys
from collections import Counter

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def survivor_before_step(P, A, y, K, target_step):
    """返回 target_step 前各模板幸存者。"""
    rows = []
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if idx == target_step:
                rows.append((group['pattern'], r, survivors, group['holes']))
                break
            survivors = {a for a in survivors if covered_by_patch(P, a, r, y)}
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=8009)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--step', type=int, default=1)
    parser.add_argument('--top', type=int, default=8)
    args = parser.parse_args()

    total_before = 0
    actual_h4 = 0
    actual_deg_ge4 = 0
    crt_sum_floor = 0
    crt_sum_plus1 = 0
    examples = []
    quad_counter = Counter()
    for pat, r, survivors, holes in survivor_before_step(args.P, args.A, args.y, args.K, args.step):
        if not survivors:
            continue
        total_before += len(survivors)
        max_Q = max(math.isqrt(a + r * args.P) for a in survivors)
        qs = [q for q in primes_upto(max_Q) if q > args.y and q != args.P]
        # 实际四重组合数。
        for a in survivors:
            hit_qs = [q for q in qs if (a + r * args.P) % q == 0]
            if len(hit_qs) >= 4:
                actual_deg_ge4 += 1
                actual_h4 += math.comb(len(hit_qs), 4)
                if len(examples) < args.top:
                    examples.append((pat, r, a, a + r * args.P, hit_qs))
        # CRT 界：对每个四元组，a 落在唯一模 m 类，短区间长度 < P。
        for quad in itertools.combinations(qs, 4):
            m = math.prod(quad)
            crt_sum_floor += args.P // m
            crt_sum_plus1 += args.P // m + 1
            quad_counter[quad[0]] += 1
    print('P', args.P, 'step', args.step, 'before', total_before)
    print('actual_deg_ge4', actual_deg_ge4, 'actual_H4_comb', actual_h4)
    print('crt_sum_floor', crt_sum_floor, 'crt_sum_plus1', crt_sum_plus1)
    print('actual_H4_per_before', f'{actual_h4/total_before if total_before else 0:.6f}')
    print('examples', examples)


if __name__ == '__main__':
    main()
