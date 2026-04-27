#!/usr/bin/env python3
"""扫描长尾样本的唯一补丁洞密度与集合覆盖数比例。

先复用证书路径搜索找到死亡最晚的若干锚点，再对这些锚点的合数前缀计算：
1. 每个合数洞的全部补丁集合 Q_i；
2. 唯一补丁洞数量 #{i: |Q_i|=1}；
3. 精确集合覆盖数 C_cover。

用法示例：
  python3 experiments/unique_patch_density_scan.py --Ps 32003,64007,128021,256019 --K 35 --y 11 --top 5
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor, isprimefac
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回 n 的全部可用补丁素数。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def greedy_upper(sets):
    """集合覆盖贪心上界。"""
    uncovered = set(range(len(sets)))
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)
    chosen = []
    while uncovered:
        q, hits = max(q_to_idx.items(), key=lambda item: len(item[1] & uncovered))
        gain = hits & uncovered
        if not gain:
            break
        chosen.append(q)
        uncovered -= gain
    return chosen


def exact_cover_number(sets):
    """精确集合覆盖数；长尾规模通常不大。"""
    sets = [tuple(sorted(s)) for s in sets]
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)
    upper = greedy_upper(sets)
    best = {'size': len(upper)}

    def lower_bound(uncovered):
        max_gain = max((len(v & uncovered) for v in q_to_idx.values()), default=1)
        return math.ceil(len(uncovered) / max(1, max_gain))

    def search(uncovered, chosen_size):
        if not uncovered:
            best['size'] = min(best['size'], chosen_size)
            return
        if chosen_size + lower_bound(uncovered) >= best['size']:
            return
        idx = min(uncovered, key=lambda i: len(sets[i]))
        for q in sorted(sets[idx], key=lambda x: -len(q_to_idx[x] & uncovered)):
            search(uncovered - q_to_idx[q], chosen_size + 1)

    search(set(range(len(sets))), 0)
    return best['size']


def collect_records(P, A, y, K):
    """收集死亡最晚的路径记录。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, ()) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            next_states = []
            for a, path in states:
                patches = patch_set(a + r * P, y, P)
                if patches:
                    next_states.append((a, path + (min(patches),)))
                elif path:
                    records.append((idx, a, path, group['holes'][:idx], group['pattern']))
            states = next_states
        for a, path in states:
            if path:
                records.append((K + 1, a, path, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def analyze_record(P, y, death, a, holes):
    """分析一个锚点到死亡前的合数前缀。"""
    composite_holes = holes[:death - 1] if death <= len(holes) else holes
    sets = []
    prime_positions = []
    for idx, r in enumerate(composite_holes, start=1):
        n = a + r * P
        fac = factor(n)
        if isprimefac(fac, n):
            prime_positions.append(idx)
            continue
        sets.append(patch_set(n, y, P))
    unique_count = sum(1 for s in sets if len(s) == 1)
    forced_unique_distinct = len({s[0] for s in sets if len(s) == 1})
    cover = exact_cover_number(sets) if sets else 0
    incidence = sum(len(s) for s in sets)
    return {
        'T': len(sets),
        'unique': unique_count,
        'forced_unique_distinct': forced_unique_distinct,
        'cover': cover,
        'incidence': incidence,
        'prime_positions': prime_positions,
        'max_patch_options': max((len(s) for s in sets), default=0),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--top', type=int, default=5)
    args = parser.parse_args()

    print('P rank death a T unique unique_ratio forced_unique_distinct forced_ratio cover cover_ratio incidence avg_options max_options distinct_path repeats pattern')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for rank, rec in enumerate(collect_records(P, args.A, args.y, args.K)[:args.top], start=1):
            death, a, path, holes, pattern = rec
            stats = analyze_record(P, args.y, death, a, holes)
            T = stats['T']
            distinct_path = len(set(path))
            repeats = len(path) - distinct_path
            print(
                P, rank, death, a, T,
                stats['unique'], f'{stats["unique"]/T if T else 0:.3f}',
                stats['forced_unique_distinct'], f'{stats["forced_unique_distinct"]/T if T else 0:.3f}',
                stats['cover'], f'{stats["cover"]/T if T else 0:.3f}',
                stats['incidence'], f'{stats["incidence"]/T if T else 0:.3f}',
                stats['max_patch_options'], distinct_path, repeats, pattern,
            )


if __name__ == '__main__':
    main()
