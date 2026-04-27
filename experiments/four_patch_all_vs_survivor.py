#!/usr/bin/env python3
"""比较全锚点四补丁点与模板幸存集中的四补丁点。

用法示例：
  python3 experiments/four_patch_all_vs_survivor.py --P 16001 --K 15
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from demand_side_bad_prefix import prime_anchors
from hole_index_prime_rate import factor
from shared_patch_energy import front_holes
from template_cover_sieve import template_groups, covered_by_patch


def patch_degree(P, a, r, y):
    """补丁因子个数。"""
    n = a + r * P
    return len([q for q, _ in factor(n) if q > y and q <= math.isqrt(n) and q != P])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=16001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=15)
    args = parser.parse_args()

    anchors = prime_anchors(args.P, args.A)
    all_by_step = Counter()
    all_before = Counter()
    for a in anchors:
        for idx, r in enumerate(front_holes(args.P, a, args.y, args.K), start=1):
            all_before[idx] += 1
            if patch_degree(args.P, a, r, args.y) >= 4:
                all_by_step[idx] += 1

    surv_by_step = Counter()
    surv_before = Counter()
    for group in template_groups(args.P, args.A, args.y, args.K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if not survivors:
                break
            surv_before[idx] += len(survivors)
            for a in survivors:
                if patch_degree(args.P, a, r, args.y) >= 4:
                    surv_by_step[idx] += 1
            survivors = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}

    print('P', args.P, 'N', len(anchors), 'K', args.K)
    print('idx all_before all_ge4 all_rate surv_before surv_ge4 surv_rate reduction')
    for idx in range(1, args.K + 1):
        ab = all_before[idx]
        sb = surv_before[idx]
        print(idx, ab, all_by_step[idx], f'{all_by_step[idx]/ab if ab else 0:.5f}', sb, surv_by_step[idx], f'{surv_by_step[idx]/sb if sb else 0:.5f}', f'{(surv_by_step[idx]/max(1,all_by_step[idx])):.3f}')


if __name__ == '__main__':
    main()
