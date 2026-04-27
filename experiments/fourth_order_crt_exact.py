#!/usr/bin/env python3
"""四阶重叠的精确 CRT 命中计数。

对每个模板/步/四元组 q，解出 a mod m，并数短区间锚点中实际落入该类者。

用法示例：
  python3 experiments/fourth_order_crt_exact.py --P 8009 --step 1
"""
import argparse
import bisect
import itertools
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def crt_pair(a1, m1, a2, m2):
    """合并互素模的两个同余。"""
    inv = pow(m1, -1, m2)
    t = ((a2 - a1) * inv) % m2
    return (a1 + m1 * t) % (m1 * m2), m1 * m2


def crt_residue(P, r, qs):
    """求 a ≡ -rP mod q for q in qs 的 CRT 剩余。"""
    residue, mod = 0, 1
    for q in qs:
        target = (-r * P) % q
        residue, mod = crt_pair(residue, mod, target, q)
    return residue, mod


def count_interval_residue(sorted_vals, residue, mod):
    """统计 sorted_vals 中等于 residue mod mod 的数。"""
    if not sorted_vals:
        return 0
    lo, hi = sorted_vals[0], sorted_vals[-1]
    first = residue if residue >= lo else residue + ((lo - residue + mod - 1) // mod) * mod
    count = 0
    x = first
    while x <= hi:
        idx = bisect.bisect_left(sorted_vals, x)
        if idx < len(sorted_vals) and sorted_vals[idx] == x:
            count += 1
        x += mod
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=8009)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--step', type=int, default=1)
    args = parser.parse_args()

    crt_exact = 0
    checked_quads = 0
    nonzero_quads = 0
    total_before = 0
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
        vals = sorted(survivors)
        total_before += len(vals)
        max_Q = max(math.isqrt(a + target_r * args.P) for a in vals)
        qs = [q for q in primes_upto(max_Q) if q > args.y and q != args.P]
        for quad in itertools.combinations(qs, 4):
            residue, mod = crt_residue(args.P, target_r, quad)
            cnt = count_interval_residue(vals, residue, mod)
            checked_quads += 1
            if cnt:
                nonzero_quads += 1
                crt_exact += cnt
    print('P', args.P, 'step', args.step, 'before', total_before, 'checked_quads', checked_quads)
    print('crt_exact_H4', crt_exact, 'nonzero_quads', nonzero_quads, 'per_before', f'{crt_exact/total_before if total_before else 0:.6f}')


if __name__ == '__main__':
    main()
