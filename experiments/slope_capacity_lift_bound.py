#!/usr/bin/env python3
"""实际洞集斜率供给容量 + lift 模数阈值计算。

对固定 B11 洞集，计算每个 q>11 在该洞集中的最大节省：
    cap(q)=max_b #{r in H: r=b mod q} - 1。
给定目标 saving=T-cover，求至少需要多少个不同 q 才能供应该 saving。
再给出 L>=2310*prod(最小 m 个可用素数) 的 CRT 模数下界。

用法示例：
    python3 experiments/slope_capacity_lift_bound.py --c 1213 --T 30 --cover 15 --X 10000000
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto

M = 2310
Y = 11


def q_capacity(holes, q):
    """q 在实际洞集中的最大节省。"""
    by = defaultdict(int)
    for r in holes:
        by[r % q] += 1
    return max(by.values(), default=0) - 1


def capacity_profile(holes):
    """实际洞集所有可能共享 q 的容量。"""
    D = max(holes) - min(holes)
    out = []
    for q in [p for p in primes_upto(D) if p > Y]:
        cap = q_capacity(holes, q)
        if cap > 0:
            out.append((q, cap))
    return out


def min_m_by_actual_capacity(profile, S):
    """按实际容量从大到小供应 saving，求必要 m 下界。"""
    ordered = sorted(profile, key=lambda x: (-x[1], x[0]))
    total = 0
    used = []
    for q, cap in ordered:
        total += cap
        used.append((q, cap))
        if total >= S:
            return len(used), total, used
    return None, total, used


def first_available_product(m):
    """最小 m 个可用素数的乘积给出 L 下界。"""
    qs = []
    limit = 100
    while len(qs) < m:
        qs = [p for p in primes_upto(limit) if p > Y]
        limit *= 2
    L = M
    for q in qs[:m]:
        L *= q
    return L, qs[:m]


def anchor_expectation_bound(X, L):
    """sum_{p<=X} p/L 的解析尺度。"""
    if X < 3:
        return 0.0
    return (X * X) / (2.0 * math.log(X) * L)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--cover', type=int, default=15)
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.T)
    D = max(holes) - min(holes)
    S = args.T - args.cover
    profile = capacity_profile(holes)
    m, cap, used_by_capacity = min_m_by_actual_capacity(profile, S)
    if m is None:
        print('impossible', 'c', args.c, 'T', args.T, 'cover', args.cover, 'D', D, 'S', S, 'capacity', cap)
        return
    Lmin, min_qs = first_available_product(m)
    expect = anchor_expectation_bound(args.X, Lmin)
    print('c', args.c, 'T', args.T, 'cover', args.cover, 'saving', S, 'D', D)
    print('holes_first_last', holes[0], holes[-1])
    print('actual_capacity_top', sorted(profile, key=lambda x: (-x[1], x[0]))[:args.show])
    print('necessary_m_lower_bound', m, 'capacity_by_top_m', cap, 'capacity_witness', used_by_capacity)
    print('Lmin_from_first_m_q', Lmin, 'min_qs', min_qs)
    print('log10Lmin', f'{math.log10(Lmin):.3f}', 'sqrtLmin', math.isqrt(Lmin))
    print('X', args.X, 'anchor_expect_bound', f'{expect:.6g}')


if __name__ == '__main__':
    main()
