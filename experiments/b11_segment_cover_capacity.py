#!/usr/bin/env python3
"""B11 前洞长段全局形状覆盖容量。

对固定 B11 平移 c 的前 T 个洞，允许每个 q>11 选择一个余数类共享簇，
未覆盖洞用单点补丁，求整个 T 段的理论最小 cover。
这是检验重叠窗口补偿的核心模型。

用法示例：
    python3 experiments/b11_segment_cover_capacity.py --T 30 --show 10
    python3 experiments/b11_segment_cover_capacity.py --Tmin 15 --Tmax 35 --summary
"""
import argparse
from collections import Counter

from general_b11_shape_capacity import M, holes_for_c, min_cover_q_mutex


def scan_T(T, show):
    rows = []
    hist = Counter()
    for c in range(M):
        holes = holes_for_c(c, T)
        best = min_cover_q_mutex(holes)
        hist[best['cover']] += 1
        chosen = [(q, res, tuple(holes[i] for i in idxs)) for q, res, idxs, _mask in best['chosen']]
        rows.append((best['cover'], c, holes, chosen, best['mask'].bit_count()))
    rows.sort(key=lambda x: (x[0], x[1]))
    return hist, rows[:show]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--Tmin', type=int, default=15)
    parser.add_argument('--Tmax', type=int, default=30)
    parser.add_argument('--show', type=int, default=10)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args()

    if args.summary:
        print('T min_cover ratio hist')
        for T in range(args.Tmin, args.Tmax + 1):
            hist, _rows = scan_T(T, 0)
            m = min(hist)
            compact = ','.join(f'{k}:{v}' for k, v in sorted(hist.items()))
            print(T, m, f'{m/T:.6f}', compact, flush=True)
        return

    hist, rows = scan_T(args.T, args.show)
    m = min(hist)
    print('T', args.T, 'min_cover', m, 'ratio', f'{m/args.T:.6f}', 'hist', sorted(hist.items()))
    print('rank cover covered c holes chosen')
    for rank, (cover, c, holes, chosen, covered) in enumerate(rows, 1):
        print(rank, cover, covered, c, holes, chosen)


if __name__ == '__main__':
    main()
