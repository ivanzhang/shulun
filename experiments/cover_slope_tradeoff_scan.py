#!/usr/bin/env python3
"""cover 与共享斜率数量 |Q| 的权衡扫描。

目标：验证“低 cover 必须使用许多不同 q”的形状侧下界。
对每个 c,T 求最优形状 cover，同时记录 chosen_count、covered、saving。

用法示例：
    python3 experiments/cover_slope_tradeoff_scan.py --T 25 --show 20
    python3 experiments/cover_slope_tradeoff_scan.py --Tlist 15,20,25,30 --summary
"""
import argparse
from collections import Counter, defaultdict
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c, min_cover_fast


def scan_T(T):
    rows = []
    hist = Counter()
    by_cover = defaultdict(list)
    for c in range(M):
        holes = holes_for_c(c, T)
        best = min_cover_fast(holes)
        q_count = len(best['chosen'])
        max_cluster = max((idxs.__len__() for _q, _res, idxs, _mask in best['chosen']), default=1)
        rec = {
            'T': T,
            'c': c,
            'cover': best['cover'],
            'ratio': best['cover'] / T,
            'q_count': q_count,
            'covered': best['covered'],
            'saving': best['saving'],
            'max_cluster': max_cluster,
            'holes': holes,
            'chosen': best['chosen'],
        }
        hist[(best['cover'], q_count)] += 1
        by_cover[best['cover']].append(rec)
        rows.append(rec)
    return rows, hist, by_cover


def print_summary(T):
    rows, _hist, by_cover = scan_T(T)
    print('T', T, 'min_cover', min(by_cover), 'max_saving', max(r['saving'] for r in rows))
    print('cover count min_q max_q avg_q min_saving max_saving examples')
    for cover in sorted(by_cover):
        arr = by_cover[cover]
        qs = [r['q_count'] for r in arr]
        savings = [r['saving'] for r in arr]
        examples = ','.join(str(r['c']) for r in sorted(arr, key=lambda x: (x['q_count'], x['c']))[:5])
        print(cover, len(arr), min(qs), max(qs), f'{sum(qs)/len(qs):.3f}', min(savings), max(savings), examples)


def print_detail(T, show):
    rows, _hist, _by_cover = scan_T(T)
    rows.sort(key=lambda r: (r['cover'], -r['q_count'], r['c']))
    print('rank T c cover ratio q_count saving covered max_cluster chosen')
    for i, r in enumerate(rows[:show], 1):
        holes = r['holes']
        chosen = [(q, res, tuple(holes[j] for j in idxs)) for q, res, idxs, _mask in r['chosen']]
        print(i, T, r['c'], r['cover'], f'{r["ratio"]:.6f}', r['q_count'], r['saving'], r['covered'], r['max_cluster'], chosen)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=25)
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
