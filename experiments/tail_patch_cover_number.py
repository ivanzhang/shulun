#!/usr/bin/env python3
"""单点尾部的补丁集合覆盖数。

对给定 P,a,y,K，取 B_y 前 K 个洞高度；若这些 n=a+rP 为合数，记录每个洞的所有
可用补丁素数 q>y, q<=sqrt(n)。然后用精确回溯求覆盖这些合数洞所需的最少不同 q 数。
这比“选择最小补丁”的路径统计更强，因为它允许每个合数洞自由改选任一补丁。

用法示例：
  python3 experiments/tail_patch_cover_number.py --P 256019 --a 107827 --K 35 --y 11
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor, isprimefac
from shared_patch_energy import front_holes


def patch_set(n, y, P):
    """列出 n 的所有可用补丁素数。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def greedy_upper(sets):
    """贪心给出覆盖数上界。"""
    uncovered = set(range(len(sets)))
    chosen = []
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)
    while uncovered:
        q, hits = max(q_to_idx.items(), key=lambda item: len(item[1] & uncovered))
        gain = hits & uncovered
        if not gain:
            break
        chosen.append(q)
        uncovered -= gain
    return chosen


def exact_cover_number(sets):
    """精确求最小素数集合覆盖数；尾部样本规模较小，适合回溯。"""
    sets = [tuple(sorted(s)) for s in sets]
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)

    upper_choice = greedy_upper(sets)
    best = {'size': len(upper_choice), 'choice': tuple(upper_choice)}

    def lower_bound(uncovered):
        if not uncovered:
            return 0
        max_gain = max((len(idxs & uncovered) for idxs in q_to_idx.values()), default=1)
        return math.ceil(len(uncovered) / max(1, max_gain))

    def search(uncovered, chosen):
        if not uncovered:
            if len(chosen) < best['size']:
                best['size'] = len(chosen)
                best['choice'] = tuple(chosen)
            return
        if len(chosen) + lower_bound(uncovered) >= best['size']:
            return
        # 选可选补丁最少的未覆盖洞，强化分支剪枝。
        idx = min(uncovered, key=lambda i: len(sets[i]))
        candidates = sorted(sets[idx], key=lambda q: -len(q_to_idx[q] & uncovered))
        for q in candidates:
            new_uncovered = uncovered - q_to_idx[q]
            search(new_uncovered, chosen + [q])

    search(set(range(len(sets))), [])
    return best['size'], best['choice']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, required=True)
    parser.add_argument('--a', type=int, required=True)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--prefix', type=int, default=0, help='只分析前 prefix 个洞；0 表示 K')
    args = parser.parse_args()

    holes = front_holes(args.P, args.a, args.y, args.K)
    if args.prefix:
        holes = holes[:args.prefix]

    rows = []
    composite_sets = []
    for idx, r in enumerate(holes, start=1):
        n = args.a + r * args.P
        fac = factor(n)
        prime = isprimefac(fac, n)
        patches = () if prime else patch_set(n, args.y, args.P)
        rows.append((idx, r, n, prime, patches))
        if not prime:
            composite_sets.append(patches)

    cover_number, choice = exact_cover_number(composite_sets) if composite_sets else (0, ())
    incidence = sum(len(s) for s in composite_sets)
    repeated_capacity = len(composite_sets) - cover_number

    print('P', args.P, 'a', args.a, 'y', args.y, 'holes', len(holes), 'composite', len(composite_sets), 'cover_number', cover_number, 'repeated_capacity', repeated_capacity, 'incidence', incidence)
    print('cover_choice', choice)
    print('idx r prime patch_count patches')
    for idx, r, n, prime, patches in rows:
        print(idx, r, int(prime), len(patches), patches)


if __name__ == '__main__':
    main()
