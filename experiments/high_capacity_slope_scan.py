#!/usr/bin/env python3
"""全局高容量斜率扫描。

统计所有 B11 模板前 T 个洞中，cap_H(q)>=k 的 q 数量上限，
用于证明“高容量斜率很少”。

用法示例：
    python3 experiments/high_capacity_slope_scan.py --T 30 --show 20
    python3 experiments/high_capacity_slope_scan.py --Tlist 20,25,30,36,40 --summary
"""
import argparse
from collections import Counter, defaultdict
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c
from slope_capacity_lift_bound import capacity_profile


def scan_T(T):
    rows = []
    hist = defaultdict(Counter)
    max_by_k = defaultdict(lambda: (0, None, None))
    for c in range(M):
        holes = holes_for_c(c, T)
        profile = capacity_profile(holes)
        counts = {k: sum(1 for _q, cap in profile if cap >= k) for k in range(1, 8)}
        top = sorted(profile, key=lambda x: (-x[1], x[0]))[:20]
        for k, val in counts.items():
            hist[k][val] += 1
            if val > max_by_k[k][0]:
                max_by_k[k] = (val, c, top)
        rows.append((counts, c, top, holes))
    return rows, hist, max_by_k


def print_summary(T):
    _rows, hist, max_by_k = scan_T(T)
    print('T', T)
    for k in range(1, 7):
        val, c, top = max_by_k[k]
        print('cap_ge', k, 'max_count', val, 'at_c', c, 'hist', sorted(hist[k].items()), 'top', top)


def print_detail(T, show):
    rows, _hist, _max_by_k = scan_T(T)
    rows.sort(key=lambda row: (-row[0][3], -row[0][2], -row[0][1], row[1]))
    print('rank c ge1 ge2 ge3 ge4 ge5 ge6 top holes')
    for i, (counts, c, top, holes) in enumerate(rows[:show], 1):
        print(i, c, counts[1], counts[2], counts[3], counts[4], counts[5], counts[6], top, holes)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--Tlist', default='')
    parser.add_argument('--show', type=int, default=20)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args()

    if args.Tlist:
        for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
            print_summary(T)
            print('---', flush=True)
    elif args.summary:
        print_summary(args.T)
    else:
        print_detail(args.T, args.show)


if __name__ == '__main__':
    main()
