#!/usr/bin/env python3
"""局部窗口最小覆盖数扫描。

枚举长尾样本中的连续 W 个前洞窗口，精确计算补丁集合覆盖数 cover，寻找最小值。
用于验证“15洞局部覆盖引理 cover>=c”。

用法示例：
  python3 experiments/local_cover_min_scan.py --Ps 8009,16001,32003,64007,128021,256019 --K 35 --y 11 --W 15 --top-records 20 --show 20
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

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


def exact_cover_size(sets):
    """精确集合覆盖数。"""
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='8009,16001,32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=20)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    windows = []
    hist = Counter()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            if len(prefix) < args.W:
                continue
            rows = list(enumerate(prefix, start=1))
            for start in range(len(rows) - args.W + 1):
                window = rows[start:start + args.W]
                sets = [patch_set(a + r * P, args.y, P) for _, r in window]
                cover = exact_cover_size(sets)
                sizes = [len(s) for s in sets]
                all_patches = [q for s in sets for q in s]
                distinct = len(set(all_patches))
                repeats = len(all_patches) - distinct
                ge2 = sum(1 for x in sizes if x >= 2)
                ge3 = sum(1 for x in sizes if x >= 3)
                ge4 = sum(1 for x in sizes if x >= 4)
                forced_unique = len({s[0] for s in sets if len(s) == 1})
                rec = {
                    'P': P, 'a': a, 'death': death, 'pattern': pattern,
                    'idx_range': (window[0][0], window[-1][0]),
                    'r_range': (window[0][1], window[-1][1]),
                    'cover': cover,
                    'sizes': sizes,
                    'ge2': ge2,
                    'ge3': ge3,
                    'ge4': ge4,
                    'forced_unique': forced_unique,
                    'distinct': distinct,
                    'repeats': repeats,
                }
                hist[cover] += 1
                windows.append(rec)
    windows.sort(key=lambda x: (x['cover'], -x['ge2'], x['P']))
    print('W', args.W, 'windows', len(windows), 'cover_hist', sorted(hist.items()))
    print('rank cover P a idx_range r_range ge2 ge3 ge4 forced_unique distinct repeats sizes pattern')
    for rank, win in enumerate(windows[:args.show], start=1):
        print(rank, win['cover'], win['P'], win['a'], win['idx_range'], win['r_range'], win['ge2'], win['ge3'], win['ge4'], win['forced_unique'], win['distinct'], win['repeats'], win['sizes'], win['pattern'])


if __name__ == '__main__':
    main()
