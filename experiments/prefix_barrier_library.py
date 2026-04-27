#!/usr/bin/env python3
"""高容量前缀屏障库扫描。

枚举真实骨架样本，抽取按容量排序的前 k 个 (q,residue,cap) 前缀，
去重后统计每个前缀对 P<=X 的幸存素数数量：
    survivor_count = #{prime P<=X : A_R(P)<=P}。

用法示例：
    python3 experiments/prefix_barrier_library.py --c 1213 --W 100 --S 55 --X 1000000 --limit 200 --beam 8 --ks 6,7,8,9
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prime_weighted_block_sample import enumerate_weighted_skeletons
from skeleton_union_bound import q_residue_options
from prime_weighted_block_sample import crt_pair


def prefix_key(skeleton, k):
    """生成容量优先前缀类型键。"""
    ordered = sorted(skeleton, key=lambda row: (-row[2], row[0], row[1]))
    prefix = ordered[:k]
    key = tuple((row[0], row[1], row[2]) for row in prefix)
    return key, prefix



def prefix_phase(prefix):
    """把 a ≡ -r_q P mod q 的 r_q 部分先 CRT 合并。"""
    residue = 0
    modulus = 1
    for q, r, *_ in prefix:
        residue, modulus = crt_pair(residue, modulus, r % q, q)
    return residue, modulus


def prefix_anchor_from_phase(residue, modulus, P):
    """由合并相位快速计算 A_R(P)。"""
    anchor = (-residue * (P % modulus)) % modulus
    if anchor == 0:
        anchor = modulus
    return anchor

def survivor_count(prefix, primes, stop_after=None):
    """统计 A_R(P)<=P 的素数数量。"""
    count = 0
    first = []
    min_ratio = None
    residue, modulus = prefix_phase(prefix)
    for P in primes:
        a = prefix_anchor_from_phase(residue, modulus, P)
        ratio = a / P
        if min_ratio is None or ratio < min_ratio:
            min_ratio = ratio
        if a <= P:
            count += 1
            if len(first) < 3:
                first.append((P, a, ratio))
            if stop_after is not None and count > stop_after:
                break
    return count, min_ratio, first


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--limit', type=int, default=200)
    parser.add_argument('--beam', type=int, default=8)
    parser.add_argument('--ks', default='6,7,8,9')
    parser.add_argument('--show', type=int, default=12)
    args = parser.parse_args()

    ks = [int(x) for x in args.ks.split(',') if x]
    holes = holes_for_c(args.c, args.W)
    opts = q_residue_options(holes)
    skeletons = enumerate_weighted_skeletons(opts, args.S, args.limit, args.beam)
    primes = primes_upto(args.X)

    libraries = {k: {} for k in ks}
    occurrences = {k: defaultdict(int) for k in ks}
    for skeleton in skeletons:
        for k in ks:
            if len(skeleton) < k:
                continue
            key, prefix = prefix_key(skeleton, k)
            occurrences[k][key] += 1
            libraries[k].setdefault(key, prefix)

    print('c W S X skeleton_samples piX', args.c, args.W, args.S, args.X, len(skeletons), len(primes))
    for k in ks:
        rows = []
        for key, prefix in libraries[k].items():
            count, min_ratio, first = survivor_count(prefix, primes)
            modulus = math.prod(row[0] for row in prefix)
            rows.append((count, min_ratio, occurrences[k][key], modulus, key, first))
        rows.sort(key=lambda row: (row[0], row[1] if row[1] is not None else math.inf))
        zero = sum(1 for row in rows if row[0] == 0)
        print('k', k, 'unique_prefixes', len(rows), 'zero_prefixes', zero, 'zero_rate', zero / len(rows) if rows else None)
        for count, min_ratio, occ, modulus, key, first in rows[:args.show]:
            print(
                '  prefix',
                'survivors', count,
                'minA/P', f'{min_ratio:.6g}' if min_ratio is not None else None,
                'occ', occ,
                'log10M', f'{math.log10(modulus):.3f}',
                'key', key,
                'first', first,
            )


if __name__ == '__main__':
    main()
