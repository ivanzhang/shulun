#!/usr/bin/env python3
"""共享秩 R 与高选项洞补偿关系扫描。

统计局部窗口中：R、N>=2/3/4、unique、cover、incidence、distinct 的关系。
目标检验：共享越多是否伴随高选项洞/高 incidence，从而 cover 不低。

用法示例：
  python3 experiments/shared_rank_compensation_scan.py --Ps 32003,64007,128021,256019 --K 35 --W 15 --top-records 20
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
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > Y and q <= root and q != P)


def collect_records(P, A, y, K):
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


def stats(P, a, window):
    sets = [patch_set(a + r * P, P) for _, r in window]
    sizes = [len(s) for s in sets]
    q_to_rows = defaultdict(list)
    for idx, ((_, r), qs) in enumerate(zip(window, sets), start=1):
        for q in qs:
            q_to_rows[q].append((idx, r))
    R = sum(len(v) - 1 for v in q_to_rows.values() if len(v) >= 2)
    H = sum(len(v) * (len(v) - 1) // 2 for v in q_to_rows.values() if len(v) >= 2)
    incidence = sum(sizes)
    distinct = len(q_to_rows)
    return {
        'R': R,
        'H': H,
        'cover': exact_cover_size(sets),
        'incidence': incidence,
        'distinct': distinct,
        'unique': sum(1 for x in sizes if x == 1),
        'ge2': sum(1 for x in sizes if x >= 2),
        'ge3': sum(1 for x in sizes if x >= 3),
        'ge4': sum(1 for x in sizes if x >= 4),
        'sizes': sizes,
        'shared': {q: v for q, v in q_to_rows.items() if len(v) >= 2},
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
    by_R = defaultdict(list)
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            if len(prefix) < args.W:
                continue
            indexed = list(enumerate(prefix, start=1))
            for start in range(len(indexed) - args.W + 1):
                window = indexed[start:start + args.W]
                st = stats(P, a, window)
                row = (P, a, (window[0][0], window[-1][0]), (window[0][1], window[-1][1]), st, pattern)
                rows.append(row)
                by_R[st['R']].append(row)

    print('summary_by_R R count min_cover max_cover min_unique max_ge2 min_ge3 max_ge3 max_ge4 avg_incidence')
    for R in sorted(by_R):
        vals = by_R[R]
        print(R, len(vals), min(v[4]['cover'] for v in vals), max(v[4]['cover'] for v in vals), min(v[4]['unique'] for v in vals), max(v[4]['ge2'] for v in vals), min(v[4]['ge3'] for v in vals), max(v[4]['ge3'] for v in vals), max(v[4]['ge4'] for v in vals), f'{sum(v[4]["incidence"] for v in vals)/len(vals):.2f}')

    rows.sort(key=lambda x: (x[4]['R'], x[4]['ge3'], x[4]['ge4'], -x[4]['cover']), reverse=True)
    print('top R/ge3 windows')
    print('rank P a idx r R H cover unique ge2 ge3 ge4 incidence distinct sizes shared pattern')
    for rank, (P, a, idx_range, r_range, st, pattern) in enumerate(rows[:args.show], start=1):
        print(rank, P, a, idx_range, r_range, st['R'], st['H'], st['cover'], st['unique'], st['ge2'], st['ge3'], st['ge4'], st['incidence'], st['distinct'], st['sizes'], {q: vals for q, vals in sorted(st['shared'].items())}, pattern)


if __name__ == '__main__':
    main()
