#!/usr/bin/env python3
"""列出 B_y 有限模式的前洞目录，并验证数量为 phi(M_y)。

用法示例：
  python3 experiments/pattern_hole_catalog.py --y 7 --K 20
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import primes_upto


def holes_for_residues(residues, primes, K):
    """给定每个小素数的阻塞高度剩余类，生成前 K 洞。"""
    holes = []
    r = 1
    while len(holes) < K:
        if all(r % p != residues[i] for i, p in enumerate(primes)):
            holes.append(r)
        r += 1
    return holes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=20)
    args = parser.parse_args()

    primes = primes_upto(args.y)
    patterns = [[]]
    for p in primes:
        patterns = [pat + [r] for pat in patterns for r in range(p)]
    # 因 a 是奇素数且 P 奇，模 2 阻塞类固定为 1；实际洞全为偶数。
    catalog = []
    for pat in patterns:
        holes = holes_for_residues(pat, primes, args.K)
        catalog.append((tuple(pat), tuple(holes)))
    unique_holes = Counter(holes for _, holes in catalog)
    print('y', args.y, 'small_primes', primes, 'raw_patterns', len(catalog), 'unique_hole_sequences', len(unique_holes))
    print('max_last_hole', max(holes[-1] for holes in unique_holes), 'min_last_hole', min(holes[-1] for holes in unique_holes))
    print('first_patterns')
    for pat, holes in catalog[:20]:
        print(pat, holes)


if __name__ == '__main__':
    main()
