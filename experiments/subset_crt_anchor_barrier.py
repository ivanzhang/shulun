#!/usr/bin/env python3
"""小子集 CRT 锚点超界判据实验。

对真实骨架的子集 R，固定素数 P 后锚点必须满足：
    a ≡ -r_q P (mod q), q in R。
CRT 合成得到最小正代表 A_R(P) mod L_R。
若 A_R(P)>P，则该子集已排除这个 P；若对所有 P<=X 均 A_R(P)>P，
则该小子集已证明整个骨架不可达。

用法示例：
    python3 experiments/subset_crt_anchor_barrier.py --c 1213 --W 100 --S 55 --X 1000000 --limit 10 --beam 6 --maxK 8
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prime_weighted_block_sample import crt_pair, enumerate_weighted_skeletons
from skeleton_union_bound import q_residue_options


def subset_anchor_modulus(subset, P):
    """返回 a 对子集同余的最小正代表和模数。"""
    residue = 0
    modulus = 1
    for q, r, *_ in subset:
        target = (-r * (P % q)) % q
        residue, modulus = crt_pair(residue, modulus, target, q)
    if residue == 0:
        residue = modulus
    return residue, modulus


def prefix_subsets(skeleton, max_k):
    """按容量优先构造前缀子集。"""
    ordered = sorted(skeleton, key=lambda row: (-row[2], row[0], row[1]))
    return [(k, ordered[:k]) for k in range(1, min(max_k, len(ordered)) + 1)]


def test_subset(subset, primes):
    """统计子集无法排除的 P：A_R(P)<=P。"""
    survivors = []
    max_ratio = 0.0
    min_ratio = None
    for P in primes:
        a, modulus = subset_anchor_modulus(subset, P)
        ratio = a / P
        if min_ratio is None or ratio < min_ratio:
            min_ratio = ratio
        if ratio > max_ratio:
            max_ratio = ratio
        if a <= P:
            survivors.append((P, a, modulus, ratio))
    return survivors, min_ratio, max_ratio


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--beam', type=int, default=6)
    parser.add_argument('--maxK', type=int, default=10)
    parser.add_argument('--show', type=int, default=5)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.W)
    opts = q_residue_options(holes)
    skeletons = enumerate_weighted_skeletons(opts, args.S, args.limit, args.beam)
    primes = primes_upto(args.X)

    print('c W S X skeletons piX', args.c, args.W, args.S, args.X, len(skeletons), len(primes))
    for skel_idx, skeleton in enumerate(skeletons[:args.show]):
        print('skeleton', skel_idx, 'qcount', len(skeleton), 'saving', sum(row[2] for row in skeleton))
        for k, subset in prefix_subsets(skeleton, args.maxK):
            survivors, min_ratio, max_ratio = test_subset(subset, primes)
            modulus = math.prod(row[0] for row in subset)
            compact = [(row[0], row[1], row[2]) for row in subset]
            first = survivors[:3]
            print(
                '  k', k,
                'log10M', f'{math.log10(modulus):.3f}',
                'survivors', len(survivors),
                'minA/P', f'{min_ratio:.6g}',
                'maxA/P', f'{max_ratio:.6g}',
                'subset', compact,
                'first', first,
            )
            if not survivors:
                break


if __name__ == '__main__':
    main()
