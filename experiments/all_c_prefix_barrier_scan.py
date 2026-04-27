#!/usr/bin/env python3
"""遍历 c mod 2310 的高容量前缀屏障扫描。

对每个 c，取 holes_for_c(c,W)，枚举一个/多个高贡献骨架，抽取 k 前缀，
统计 Surv(R_k,X)。默认只检查与 2310 互素的 c。

用法示例：
    python3 experiments/all_c_prefix_barrier_scan.py --W 100 --S 55 --X 1000000 --k 9 --limit 30 --beam 8
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_key, survivor_count
from prime_weighted_block_sample import enumerate_weighted_skeletons
from skeleton_union_bound import M, q_residue_options


def compatible_cs(only_units=True):
    """生成 c mod 2310；默认只取与 2310 互素相位。"""
    for c in range(M):
        if only_units and math.gcd(c, M) != 1:
            continue
        yield c


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--k', type=int, default=9)
    parser.add_argument('--limit', type=int, default=30)
    parser.add_argument('--beam', type=int, default=8)
    parser.add_argument('--allC', action='store_true')
    parser.add_argument('--maxC', type=int, default=None)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    primes = primes_upto(args.X)
    rows = []
    prefix_counter = Counter()
    survivor_cache = {}
    checked = 0
    for c in compatible_cs(only_units=not args.allC):
        if args.maxC is not None and checked >= args.maxC:
            break
        checked += 1
        holes = holes_for_c(c, args.W)
        opts = q_residue_options(holes)
        skeletons = enumerate_weighted_skeletons(opts, args.S, args.limit, args.beam)
        if not skeletons:
            rows.append((math.inf, c, None, None, None, 'no_skeleton'))
            continue
        best_count = math.inf
        best_key = None
        best_min_ratio = None
        best_first = None
        for skeleton in skeletons:
            if len(skeleton) < args.k:
                continue
            key, prefix = prefix_key(skeleton, args.k)
            prefix_counter[key] += 1
            if key in survivor_cache:
                count, min_ratio, first = survivor_cache[key]
            else:
                count, min_ratio, first = survivor_count(prefix, primes)
                survivor_cache[key] = (count, min_ratio, first)
            if count < best_count:
                best_count = count
                best_key = key
                best_min_ratio = min_ratio
                best_first = first
                if count == 0:
                    break
        rows.append((best_count, c, best_min_ratio, best_key, best_first, 'ok'))

    finite = [row for row in rows if row[0] != math.inf]
    zero = sum(1 for row in finite if row[0] == 0)
    nonzero = [row for row in finite if row[0] != 0]
    print('W S X k checked finite zero nonzero unique_prefixes', args.W, args.S, args.X, args.k, checked, len(finite), zero, len(nonzero), len(prefix_counter), 'cache', len(survivor_cache))
    if finite:
        print('max_survivors', max(row[0] for row in finite), 'zero_rate', zero / len(finite))
    print('worst_nonzero')
    for count, c, min_ratio, key, first, status in sorted(nonzero, reverse=True)[:args.show]:
        print('c', c, 'survivors', count, 'minA/P', f'{min_ratio:.6g}' if min_ratio else None, 'key', key, 'first', first)
    print('top_prefix_occurrences')
    for key, occ in prefix_counter.most_common(args.show):
        print('occ', occ, 'key', key)


if __name__ == '__main__':
    main()
