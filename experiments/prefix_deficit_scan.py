#!/usr/bin/env python3
"""首空隙前缀负偏差扫描。

对每个素数 P 的最坏剩余类 a，取首个素数高度 R0。
在 [0,R0) 中真实幸存数 H=0，比较筛模型期望 E=R0*prod(1-1/q)，
并记录覆盖重数、唯一覆盖数、二阶偏差，寻找可证明的结构性障碍。

用法示例：
    python3 experiments/prefix_deficit_scan.py --maxP 2000 --top 30
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r, fixed_cover_stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--maxP', type=int, default=2000)
    ap.add_argument('--top', type=int, default=30)
    args = ap.parse_args()

    prime_flags = sieve(args.maxP * args.maxP)
    rows = []
    for P in primes_upto(args.maxP):
        if P < 3:
            continue
        worst_a, worst_R = 1, -1
        for a in range(1, P + 1):
            r0 = first_prime_r(P, a, prime_flags)
            if r0 is not None and r0 > worst_R:
                worst_a, worst_R = a, r0
        if worst_R <= 0:
            continue
        rec = fixed_cover_stats(P, worst_a, R=worst_R)
        mult = rec['multiplicity']
        unique = mult.get(1, 0)
        rec['first_prime_R'] = worst_R
        rec['unique'] = unique
        rec['unique_ratio'] = unique / worst_R
        rec['mean_mult'] = rec['total_hits'] / worst_R
        rec['pair_per_R'] = rec['pair'] / worst_R
        rows.append(rec)

    rows.sort(key=lambda x: (-x['first_prime_R'], -x['E']))
    print('按首空隙长度排序：')
    for rec in rows[:args.top]:
        print(
            f"P={rec['P']},a={rec['a']},R0={rec['first_prime_R']},Q={rec['Q']},q={rec['q_count']},"
            f"E={rec['E']:.3f},unique={rec['unique']},u/R={rec['unique_ratio']:.3f},"
            f"mean_mult={rec['mean_mult']:.3f},pair/R={rec['pair_per_R']:.3f},"
            f"pair_dev={rec['pair_dev']:.2f},mult={sorted(rec['multiplicity'].items())}"
        )

    rows.sort(key=lambda x: -x['E'])
    print('\n按前缀期望 E 排序：')
    for rec in rows[:args.top]:
        print(
            f"P={rec['P']},a={rec['a']},R0={rec['first_prime_R']},E={rec['E']:.3f},"
            f"unique={rec['unique']},mean_mult={rec['mean_mult']:.3f},pair_dev={rec['pair_dev']:.2f}"
        )


if __name__ == '__main__':
    main()
