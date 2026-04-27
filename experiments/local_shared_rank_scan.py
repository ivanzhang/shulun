#!/usr/bin/env python3
"""实际长尾窗口的共享秩 R 扫描。

对连续 W 个 B11 前洞窗口统计：
  R=sum_q(m_q-1)_+
  H=sum_q C(m_q,2)
  cover
其中 m_q 是补丁 q 在窗口中出现的洞数。目标验证 R<=3 并分析最坏结构。

用法示例：
  python3 experiments/local_shared_rank_scan.py --Ps 32003,64007,128021,256019 --K 35 --W 15 --top-records 20 --show 20
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups
from local_cover_min_scan import exact_cover_size

Y = 11


def patch_set(n, P):
    """返回有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > Y and q <= root and q != P)


def collect_records(P, A, y, K):
    """收集死亡最晚记录。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, 0) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, length in states:
                qs = patch_set(a + r * P, P)
                if qs:
                    nxt.append((a, length + 1))
                elif length:
                    records.append((idx, a, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, length in states:
            if length:
                records.append((K + 1, a, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def window_stats(P, a, window):
    """计算窗口共享秩与覆盖数。"""
    sets = [patch_set(a + r * P, P) for _, r in window]
    q_to_rows = defaultdict(list)
    for local_idx, ((global_idx, r), qs) in enumerate(zip(window, sets), start=1):
        for q in qs:
            q_to_rows[q].append((local_idx, global_idx, r))
    shared = {q: rows for q, rows in q_to_rows.items() if len(rows) >= 2}
    R = sum(len(rows) - 1 for rows in shared.values())
    H = sum(len(rows) * (len(rows) - 1) // 2 for rows in shared.values())
    incidence = sum(len(s) for s in sets)
    distinct = len(q_to_rows)
    cover = exact_cover_size(sets)
    return {
        'sets': sets,
        'shared': shared,
        'R': R,
        'H': H,
        'incidence': incidence,
        'distinct': distinct,
        'cover': cover,
        'sizes': [len(s) for s in sets],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=20)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    rows = []
    hist_R = Counter()
    hist_cover = Counter()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            if len(prefix) < args.W:
                continue
            indexed = list(enumerate(prefix, start=1))
            for start in range(len(indexed) - args.W + 1):
                window = indexed[start:start + args.W]
                st = window_stats(P, a, window)
                hist_R[st['R']] += 1
                hist_cover[st['cover']] += 1
                rows.append((st['R'], st['H'], -st['cover'], P, a, (window[0][0], window[-1][0]), (window[0][1], window[-1][1]), st, pattern))
    rows.sort(reverse=True)
    print('windows', len(rows), 'R_hist', sorted(hist_R.items()), 'cover_hist', sorted(hist_cover.items()))
    print('rank R H cover P a idx r incidence distinct sizes shared pattern')
    for rank, row in enumerate(rows[:args.show], start=1):
        R, H, neg_cover, P, a, idx_range, r_range, st, pattern = row
        print(rank, R, H, -neg_cover, P, a, idx_range, r_range, st['incidence'], st['distinct'], st['sizes'], {q: vals for q, vals in sorted(st['shared'].items())}, pattern)


if __name__ == '__main__':
    main()
