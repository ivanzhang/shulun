#!/usr/bin/env python3
"""诊断 M1/M2/M3 的 q 或乘积贡献来源。

用法示例：
  python3 experiments/moment_component_diagnostics.py --P 16001 --step 4 --j 1 --top 20
  python3 experiments/moment_component_diagnostics.py --P 16001 --step 4 --j 2 --top 20
"""
import argparse
import itertools
import math
import sys
from collections import Counter

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def survivors_at_step(P, A, y, K, step):
    """聚合所有模板在 step 前的幸存者，并带上该模板该步 r。"""
    rows = []
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if idx == step:
                rows.append((r, survivors))
                break
            survivors = {a for a in survivors if covered_by_patch(P, a, r, y)}
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=16001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=8)
    parser.add_argument('--step', type=int, default=4)
    parser.add_argument('--j', type=int, default=1)
    parser.add_argument('--top', type=int, default=20)
    args = parser.parse_args()

    contrib = Counter()
    expected = Counter()
    total_N = 0
    for r, survivors in survivors_at_step(args.P, args.A, args.y, args.K, args.step):
        if not survivors:
            continue
        total_N += len(survivors)
        max_Q = max(math.isqrt(a + r * args.P) for a in survivors)
        qs = [q for q in primes_upto(max_Q) if q > args.y and q != args.P]
        for combo in itertools.combinations(qs, args.j):
            m = math.prod(combo)
            cnt = sum(1 for a in survivors if (a + r * args.P) % m == 0)
            if cnt:
                contrib[combo] += cnt
            expected[combo] += len(survivors) / m
    total_actual = sum(contrib.values())
    total_expected = sum(expected.values())
    print('P', args.P, 'step', args.step, 'j', args.j, 'N', total_N, 'actual', total_actual, 'expected', f'{total_expected:.3f}', 'ratio', f'{total_actual/total_expected if total_expected else 0:.3f}')
    print('top_positive combo actual expected ratio excess')
    rows = []
    for combo, actual in contrib.items():
        exp = expected[combo]
        rows.append((actual - exp, actual, exp, combo))
    for excess, actual, exp, combo in sorted(rows, reverse=True)[:args.top]:
        print(combo, actual, f'{exp:.3f}', f'{actual/exp if exp else 0:.2f}', f'{excess:.3f}')
    print('top_negative combo actual expected ratio deficit')
    all_rows = []
    for combo, exp in expected.items():
        actual = contrib[combo]
        all_rows.append((actual - exp, actual, exp, combo))
    for diff, actual, exp, combo in sorted(all_rows)[:args.top]:
        print(combo, actual, f'{exp:.3f}', f'{actual/exp if exp else 0:.2f}', f'{diff:.3f}')


if __name__ == '__main__':
    main()
