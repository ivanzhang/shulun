#!/usr/bin/env python3
"""真实骨架相位到短带的最近距离实验。

对骨架相位 alpha=lambda/L，短带可达要求存在素数 P<=X 和整数 k：
    |alpha - k/P| < 1/L。
等价于：
    |lambda*P - k*L| < P。

脚本统计枚举骨架的最小归一化距离：
    gap_ratio = min_P dist(lambda*P,LZ) / P。
可达当且仅当 gap_ratio < 1。

用法示例：
    python3 experiments/phase_gap_to_short_band.py --c 1213 --W 100 --S 55 --X 10000000 --limit 20 --beam 6
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prime_weighted_block_sample import crt_pair, enumerate_weighted_skeletons
from skeleton_union_bound import M, q_residue_options


def phase_for_skeleton(skeleton, c):
    """计算骨架 CRT 相位。"""
    lam = c % M
    mod = M
    for q, residue, *_ in skeleton:
        lam, mod = crt_pair(lam, mod, residue % q, q)
    return lam, mod


def min_gap_ratio(lam, mod, primes):
    """返回 min dist(lam*P, mod Z)/P。"""
    best = None
    best_p = None
    best_dist = None
    for P in primes:
        rem = (lam * (P % mod)) % mod
        dist = min(rem, mod - rem)
        ratio = dist / P
        if best is None or ratio < best:
            best = ratio
            best_p = P
            best_dist = dist
    return best, best_p, best_dist


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--beam', type=int, default=6)
    parser.add_argument('--show', type=int, default=10)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.W)
    opts = q_residue_options(holes)
    skeletons = enumerate_weighted_skeletons(opts, args.S, args.limit, args.beam)
    primes = primes_upto(args.X)
    rows = []
    for skeleton in skeletons:
        lam, mod = phase_for_skeleton(skeleton, args.c)
        gap_ratio, best_p, best_dist = min_gap_ratio(lam, mod, primes)
        rows.append((gap_ratio, best_p, best_dist, mod, lam, len(skeleton)))

    rows.sort()
    reachable = sum(1 for row in rows if row[0] < 1)
    print('c W S X skeletons reachable_by_gap', args.c, args.W, args.S, args.X, len(rows), reachable)
    for gap_ratio, best_p, best_dist, mod, lam, qcount in rows[:args.show]:
        print('row', 'gap_ratio', f'{gap_ratio:.6g}', 'bestP', best_p, 'dist', best_dist, 'log10L', f'{math.log10(mod):.6f}', 'qcount', qcount)


if __name__ == '__main__':
    main()
