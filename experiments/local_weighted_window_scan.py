#!/usr/bin/env python3
"""局部密集窗口的带权指标扫描。

枚举连续 W 个前洞窗口，统计：
- N>=2, N>=3, N>=4；
- 补丁集合覆盖数 cover；
- distinct patches 与共享量；
- forced unique count；
用于检验“局部高密度二补丁洞并不便宜，反而强迫大量新补丁”。

用法示例：
  python3 experiments/local_weighted_window_scan.py --Ps 32003,64007,128021,256019 --K 35 --y 11 --W 15 --top-records 10 --top-windows 15
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def collect_records(P, A, y, K):
    """收集死亡最晚记录。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, 0) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, length in states:
                qs = patch_set(a + r * P, y, P)
                if qs:
                    nxt.append((a, length + 1))
                elif length:
                    records.append((idx, a, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, length in states:
            if length:
                records.append((K + 1, a, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def greedy_cover_size(sets):
    """窗口内求集合覆盖数；W=15 时精确回溯也很快。"""
    sets = [tuple(sorted(s)) for s in sets]
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)
    uncovered = set(range(len(sets)))
    chosen = []
    while uncovered:
        q, hits = max(q_to_idx.items(), key=lambda item: len(item[1] & uncovered))
        gain = hits & uncovered
        chosen.append(q)
        uncovered -= gain
    best = {'size': len(chosen)}

    def lower_bound(uncovered_set):
        max_gain = max((len(v & uncovered_set) for v in q_to_idx.values()), default=1)
        return math.ceil(len(uncovered_set) / max(1, max_gain))

    def search(uncovered_set, size):
        if not uncovered_set:
            best['size'] = min(best['size'], size)
            return
        if size + lower_bound(uncovered_set) >= best['size']:
            return
        idx = min(uncovered_set, key=lambda i: len(sets[i]))
        for q in sorted(sets[idx], key=lambda x: -len(q_to_idx[x] & uncovered_set)):
            search(uncovered_set - q_to_idx[q], size + 1)

    search(set(range(len(sets))), 0)
    return best['size']


def window_metrics(P, y, a, window_rows):
    """计算一个窗口的带权指标。"""
    sets = [patch_set(a + r * P, y, P) for _, r in window_rows]
    sizes = [len(s) for s in sets]
    ge2 = sum(1 for x in sizes if x >= 2)
    ge3 = sum(1 for x in sizes if x >= 3)
    ge4 = sum(1 for x in sizes if x >= 4)
    unique = sum(1 for x in sizes if x == 1)
    forced_unique_distinct = len({s[0] for s in sets if len(s) == 1})
    all_patches = [q for s in sets for q in s]
    distinct = len(set(all_patches))
    incidence = len(all_patches)
    repeats = incidence - distinct
    cover = greedy_cover_size(sets)
    q_hist = Counter(all_patches)
    shared = {q: c for q, c in q_hist.items() if c >= 2}
    E2 = sum(x * (x - 1) // 2 for x in sizes)
    return {
        'sizes': sizes,
        'ge2': ge2,
        'ge3': ge3,
        'ge4': ge4,
        'unique': unique,
        'forced_unique_distinct': forced_unique_distinct,
        'distinct': distinct,
        'incidence': incidence,
        'repeats': repeats,
        'cover': cover,
        'shared': shared,
        'E2': E2,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=10)
    parser.add_argument('--top-windows', type=int, default=15)
    args = parser.parse_args()

    windows = []
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            rows = list(enumerate(prefix, start=1))
            for start in range(0, max(0, len(rows) - args.W + 1)):
                window_rows = rows[start:start + args.W]
                metrics = window_metrics(P, args.y, a, window_rows)
                windows.append({
                    'P': P, 'a': a, 'death': death, 'T': len(prefix), 'pattern': pattern,
                    'idx_range': (window_rows[0][0], window_rows[-1][0]),
                    'r_range': (window_rows[0][1], window_rows[-1][1]),
                    **metrics,
                })
    windows.sort(key=lambda x: (x['ge2'], x['ge3'], x['ge4'], x['cover'], x['distinct']), reverse=True)
    print('W', args.W, 'windows', len(windows))
    print('rank P a idx_range r_range ge2 ge3 ge4 unique forced_unique cover distinct incidence repeats E2 sizes shared pattern')
    for rank, win in enumerate(windows[:args.top_windows], start=1):
        print(rank, win['P'], win['a'], win['idx_range'], win['r_range'], win['ge2'], win['ge3'], win['ge4'], win['unique'], win['forced_unique_distinct'], win['cover'], win['distinct'], win['incidence'], win['repeats'], win['E2'], win['sizes'], sorted(win['shared'].items()), win['pattern'])

    dense = [w for w in windows if w['ge2'] >= 7]
    print('dense_ge2>=7 count', len(dense))
    if dense:
        print('dense minima ge3 ge4 cover distinct forced_unique')
        print(min(w['ge3'] for w in dense), min(w['ge4'] for w in dense), min(w['cover'] for w in dense), min(w['distinct'] for w in dense), min(w['forced_unique_distinct'] for w in dense))


if __name__ == '__main__':
    main()
