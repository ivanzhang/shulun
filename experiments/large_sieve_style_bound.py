#!/usr/bin/env python3
"""测试大筛型桶偏差界是否足够推出模板筛收缩。

用法示例：
  python3 experiments/large_sieve_style_bound.py --P 8009 --K 10
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=8009)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=10)
    parser.add_argument('--Cdev', type=float, default=1.2)
    args = parser.parse_args()

    groups = template_groups(args.P, args.A, args.y, args.K)
    by_step = defaultdict(lambda: [0, 0, 0.0, 0.0])
    for group in groups:
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            before = len(survivors)
            if before == 0:
                continue
            after_set = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}
            after = len(after_set)
            avg_sum = 0.0
            qcount = 0.0
            for a in survivors:
                Q = math.isqrt(a + r * args.P)
                qs = [q for q in primes_upto(Q) if q > args.y and q != args.P]
                avg_sum += sum(1 / q for q in qs)
                qcount += len(qs)
            avg_sum /= before
            qcount /= before
            # 用并集上界：命中数 <= |S| sum1q + C sqrt(|S|) * pi(Q)
            upper = before * avg_sum + args.Cdev * math.sqrt(before) * qcount
            by_step[idx][0] += before
            by_step[idx][1] += after
            by_step[idx][2] += upper
            by_step[idx][3] += before * avg_sum
            survivors = after_set
    print('P', args.P, 'Cdev', args.Cdev)
    print('idx before after actual_keep density_part upper_bound upper_keep')
    for idx in range(1, args.K + 1):
        before, after, upper, density = by_step[idx]
        if before == 0:
            continue
        print(idx, before, after, f'{after/before:.4f}', f'{density/before:.4f}', f'{upper:.1f}', f'{upper/before:.4f}')


if __name__ == '__main__':
    main()
