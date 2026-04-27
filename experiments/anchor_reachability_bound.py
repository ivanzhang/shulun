#!/usr/bin/env python3
"""真实余数类骨架的锚点可达性严格上界实验。

对骨架 B 的 CRT 模数 L，整数锚点条件为：
    0 < (-lambda P mod L) < P, P <= X。

对每个整数 P，不超过 P 个 residue 可落入短带；若把 P 粗放到所有整数，
则命中数严格不超过：
    sum_{P<=X} (P/L + 1/L) + 1
这里用更保守、易读的界：
    min(pi(X), X(X+1)/(2L) + X/L + 1)。

该脚本枚举高贡献真实骨架，比较实际命中与上述严格骨架级上界。

用法示例：
    python3 experiments/anchor_reachability_bound.py --c 1213 --W 100 --S 55 --X 10000000 --limit 100 --beam 6
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prime_weighted_block_sample import anchor_counts_for_skeleton, enumerate_weighted_skeletons
from skeleton_union_bound import q_residue_options


def integer_reach_upper_bound(X, L, pi_x):
    """骨架级整数锚点数量的保守严格上界。"""
    area = X * (X + 1) / (2 * L) + X / L + 1
    return min(pi_x, area)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--limit', type=int, default=100)
    parser.add_argument('--beam', type=int, default=6)
    parser.add_argument('--show', type=int, default=10)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.W)
    opts = q_residue_options(holes)
    skeletons = enumerate_weighted_skeletons(opts, args.S, args.limit, args.beam)
    primes = primes_upto(args.X)
    prime_set = set(primes)
    pi_x = len(primes)

    total_actual_int = 0
    total_actual_prime = 0
    total_bound = 0.0
    rows = []
    for skeleton in skeletons:
        counted = anchor_counts_for_skeleton(skeleton, args.c, primes, prime_set)
        if counted is None:
            continue
        integer_hits, prime_hits, mod, lam = counted
        bound = integer_reach_upper_bound(args.X, mod, pi_x)
        total_actual_int += integer_hits
        total_actual_prime += prime_hits
        total_bound += bound
        rows.append((bound, integer_hits, prime_hits, mod, lam, skeleton))

    print('c W S X skeletons piX', args.c, args.W, args.S, args.X, len(rows), pi_x)
    print('total_actual_int', total_actual_int, 'total_actual_prime', total_actual_prime, 'total_strict_upper', total_bound)
    for bound, integer_hits, prime_hits, mod, lam, skeleton in sorted(rows)[:args.show]:
        print(
            'row',
            'bound', f'{bound:.6g}',
            'int', integer_hits,
            'prime', prime_hits,
            'log10L', f'{math.log10(mod):.6f}',
            'qcount', len(skeleton),
        )


if __name__ == '__main__':
    main()
