#!/usr/bin/env python3
"""需求侧：前 K 洞全合数/首素数洞分布与证书需求。

用法示例：
  python3 experiments/demand_side_bad_prefix.py --P 1999 --Kmax 40
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import sieve
from hole_index_prime_rate import factor, isprimefac
from shared_patch_energy import front_holes


def prime_anchors(P, A):
    """边界锚点短区间。"""
    flags = sieve(P)
    return [a for a in range(A + 1, P) if flags[a]]


def prefix_profile(P, a, y, Kmax):
    """返回前 Kmax 洞的素/合数与补丁证书信息。"""
    holes = front_holes(P, a, y, Kmax)
    rows = []
    first_prime_idx = None
    for idx, r in enumerate(holes, start=1):
        n = a + r * P
        fac = factor(n)
        prime = isprimefac(fac, n)
        if prime and first_prime_idx is None:
            first_prime_idx = idx
        patches = [] if prime else [q for q, _ in fac if y < q <= math.isqrt(n) and q != P]
        rows.append({'idx': idx, 'r': r, 'n': n, 'prime': prime, 'patches': patches})
    return first_prime_idx, rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=1999)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--Kmax', type=int, default=40)
    parser.add_argument('--show-worst', type=int, default=8)
    args = parser.parse_args()

    anchors = prime_anchors(args.P, args.A)
    first_counter = Counter()
    survive = Counter()
    demand_by_T = defaultdict(int)
    patch_inc_by_T = defaultdict(int)
    distinct_patch_by_T = defaultdict(int)
    worst = []

    for a in anchors:
        first, rows = prefix_profile(args.P, a, args.y, args.Kmax)
        first_key = first if first is not None else args.Kmax + 1
        first_counter[first_key] += 1
        for T in range(1, args.Kmax + 1):
            prefix = rows[:T]
            all_composite = all(not x['prime'] for x in prefix)
            if all_composite:
                survive[T] += 1
                demand_by_T[T] += T
                patch_inc_by_T[T] += sum(len(x['patches']) for x in prefix)
                distinct = {q for x in prefix for q in x['patches']}
                distinct_patch_by_T[T] += len(distinct)
        worst.append((first_key, a, rows[:min(args.Kmax, 20)]))

    print('P', args.P, 'N', len(anchors), 'Kmax', args.Kmax)
    print('first_prime_idx_counter', sorted(first_counter.items()))
    print('T survivors rate demand avg_patch_inc avg_distinct_patch')
    for T in [1,2,3,4,5,6,8,10,12,16,20,30,40]:
        if T > args.Kmax:
            continue
        s = survive[T]
        rate = s / len(anchors) if anchors else 0
        avg_inc = patch_inc_by_T[T] / s if s else 0
        avg_dist = distinct_patch_by_T[T] / s if s else 0
        print(T, s, f'{rate:.4f}', demand_by_T[T], f'{avg_inc:.2f}', f'{avg_dist:.2f}')
    print('worst_rows')
    for first_key, a, rows in sorted(worst, reverse=True)[:args.show_worst]:
        detail = [(x['idx'], x['r'], x['prime'], x['patches'][:3]) for x in rows]
        print('a', a, 'first', first_key, 'detail', detail)


if __name__ == '__main__':
    main()
