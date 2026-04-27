#!/usr/bin/env python3
"""高 cover 分支扫描。

对真实长尾/构造骨架不直接分解，而在形状模型层面：
给定 T,c 的最优覆盖，统计 cover 高时需要多少单点补丁、多少不同 q，
并估计如果 cover>theta*T，则至少需要多少不同斜率/补丁。

用法示例：
    python3 experiments/high_cover_branch_scan.py --T 30 --theta 0.5 --show 20
    python3 experiments/high_cover_branch_scan.py --Tlist 20,25,30,36,40 --theta 0.5
"""
import argparse
import sys
from collections import Counter

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c, min_cover_fast


def scan_T(T, theta):
    rows = []
    hist = Counter()
    for c in range(M):
        holes = holes_for_c(c, T)
        best = min_cover_fast(holes)
        q_count = len(best['chosen'])
        shared_covered = best['covered']
        singles = T - shared_covered
        cover = best['cover']
        rows.append((cover, q_count, singles, best['saving'], c, holes, best['chosen']))
        hist[(cover, q_count, singles)] += 1
    high = [r for r in rows if r[0] > theta * T]
    low = [r for r in rows if r[0] <= theta * T]
    return rows, high, low, hist


def print_summary(T, theta):
    rows, high, low, _hist = scan_T(T, theta)
    print('T', T, 'theta', theta, 'total', len(rows), 'low_count', len(low), 'high_count', len(high))
    for name, arr in [('low', low), ('high', high), ('all', rows)]:
        if not arr:
            print(name, 'empty')
            continue
        covers = [r[0] for r in arr]
        qcounts = [r[1] for r in arr]
        singles = [r[2] for r in arr]
        savings = [r[3] for r in arr]
        print(name, 'cover_range', (min(covers), max(covers)), 'q_range', (min(qcounts), max(qcounts)), 'singles_range', (min(singles), max(singles)), 'saving_range', (min(savings), max(savings)))
        print(name, 'min_cover_records', sorted(arr, key=lambda r: (r[0], r[1], r[2], r[4]))[:5])
        print(name, 'max_singles_records', sorted(arr, key=lambda r: (-r[2], r[0], r[4]))[:5])


def print_detail(T, theta, show):
    rows, high, low, _hist = scan_T(T, theta)
    rows.sort(key=lambda r: (-r[2], r[0], r[4]))
    print('rank c cover q_count singles saving holes chosen')
    for i, (cover, q_count, singles, saving, c, holes, chosen) in enumerate(rows[:show], 1):
        sig = [(q, res, tuple(holes[j] for j in idxs)) for q, res, idxs, _mask in chosen]
        print(i, c, cover, q_count, singles, saving, holes, sig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--Tlist', default='')
    parser.add_argument('--theta', type=float, default=0.5)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()
    if args.Tlist:
        for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
            print_summary(T, args.theta)
            print('---', flush=True)
    else:
        print_summary(args.T, args.theta)
        print_detail(args.T, args.theta, args.show)


if __name__ == '__main__':
    main()
