#!/usr/bin/env python3
"""局部 cover 最小窗口的共享结构解析。

寻找连续 W 个前洞中 cover 最小的窗口，输出每个补丁素数覆盖哪些洞、高度差，
并检查共享补丁是否都由 q | r_i-r_j 解释。

用法示例：
  python3 experiments/local_cover_sharing_structure.py --Ps 128021,256019 --K 35 --y 11 --W 15 --top-records 20 --show 8
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


def exact_cover(sets):
    """精确集合覆盖，返回大小和一个覆盖选择。"""
    sets = [tuple(sorted(s)) for s in sets]
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)
    uncovered = set(range(len(sets)))
    greedy = []
    while uncovered:
        q, hits = max(q_to_idx.items(), key=lambda item: len(item[1] & uncovered))
        greedy.append(q)
        uncovered -= hits
    best = {'size': len(greedy), 'choice': tuple(greedy)}

    def lower_bound(uncovered_set):
        max_gain = max((len(v & uncovered_set) for v in q_to_idx.values()), default=1)
        return math.ceil(len(uncovered_set) / max(1, max_gain))

    def search(uncovered_set, chosen):
        if not uncovered_set:
            if len(chosen) < best['size']:
                best['size'] = len(chosen)
                best['choice'] = tuple(chosen)
            return
        if len(chosen) + lower_bound(uncovered_set) >= best['size']:
            return
        idx = min(uncovered_set, key=lambda i: len(sets[i]))
        for q in sorted(sets[idx], key=lambda x: -len(q_to_idx[x] & uncovered_set)):
            search(uncovered_set - q_to_idx[q], chosen + [q])

    search(set(range(len(sets))), [])
    return best['size'], best['choice']


def window_records(P, y, death, a, holes, pattern, W):
    """生成窗口记录。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    if len(prefix) < W:
        return []
    rows = list(enumerate(prefix, start=1))
    out = []
    for start in range(len(rows) - W + 1):
        window = rows[start:start + W]
        sets = [patch_set(a + r * P, y, P) for _, r in window]
        cover, choice = exact_cover(sets)
        q_to_rows = defaultdict(list)
        for local_idx, ((idx, r), qs) in enumerate(zip(window, sets)):
            for q in qs:
                q_to_rows[q].append((local_idx, idx, r))
        shared = {q: vals for q, vals in q_to_rows.items() if len(vals) >= 2}
        out.append({
            'P': P, 'a': a, 'death': death, 'pattern': pattern,
            'idx_range': (window[0][0], window[-1][0]),
            'r_range': (window[0][1], window[-1][1]),
            'sets': sets,
            'cover': cover,
            'choice': choice,
            'shared': shared,
        })
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='8009,16001,32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=20)
    parser.add_argument('--show', type=int, default=8)
    args = parser.parse_args()

    windows = []
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            windows.extend(window_records(P, args.y, death, a, holes, pattern, args.W))
    windows.sort(key=lambda x: (x['cover'], len(x['shared']), x['P']))
    print('W', args.W, 'windows', len(windows))
    for rank, win in enumerate(windows[:args.show], start=1):
        incidence = sum(len(s) for s in win['sets'])
        distinct = len({q for s in win['sets'] for q in s})
        print('window', rank, 'cover', win['cover'], 'P', win['P'], 'a', win['a'], 'idx', win['idx_range'], 'r', win['r_range'], 'incidence', incidence, 'distinct', distinct, 'raw_repeats', incidence - distinct, 'choice', win['choice'], 'pattern', win['pattern'])
        print('  sets')
        for i, qs in enumerate(win['sets'], start=1):
            print(' ', i, qs)
        print('  shared q -> local/global/r diffs divisible')
        for q, vals in sorted(win['shared'].items()):
            rs = [r for _, _, r in vals]
            diffs = [rs[i] - rs[0] for i in range(1, len(rs))]
            print(' ', q, vals, 'diffs', diffs, 'ok', all(d % q == 0 for d in diffs))


if __name__ == '__main__':
    main()
