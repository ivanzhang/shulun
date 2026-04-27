#!/usr/bin/env python3
"""多窗口 B11 形状覆盖容量摘要扫描。

复用 general_b11_shape_capacity 的严格形状模型，但只输出每个 W 的最小 cover、比例和直方图。

用法示例：
    python3 experiments/b11_shape_capacity_summary.py --Wmin 15 --Wmax 30
"""
import argparse
from collections import Counter

from general_b11_shape_capacity import M, holes_for_c, min_cover_q_mutex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Wmin', type=int, default=15)
    parser.add_argument('--Wmax', type=int, default=30)
    parser.add_argument('--show-best', type=int, default=3)
    args = parser.parse_args()

    print('W min_cover ratio cover_hist best_templates', flush=True)
    for W in range(args.Wmin, args.Wmax + 1):
        hist = Counter()
        best_rows = []
        for c in range(M):
            holes = holes_for_c(c, W)
            best = min_cover_q_mutex(holes)
            cover = best['cover']
            hist[cover] += 1
            chosen = [(q, res, tuple(holes[i] for i in idxs)) for q, res, idxs, _mask in best['chosen']]
            row = (cover, c, holes, chosen)
            if len(best_rows) < args.show_best:
                best_rows.append(row)
                best_rows.sort(key=lambda x: (x[0], x[1]))
            elif (cover, c) < (best_rows[-1][0], best_rows[-1][1]):
                best_rows[-1] = row
                best_rows.sort(key=lambda x: (x[0], x[1]))
        min_cover = min(hist)
        ratio = min_cover / W
        compact = ','.join(f'{k}:{v}' for k, v in sorted(hist.items()))
        templates = '; '.join(f'c={c},cover={cover},holes={holes},chosen={chosen}' for cover, c, holes, chosen in best_rows)
        print(W, min_cover, f'{ratio:.6f}', compact, templates, flush=True)


if __name__ == '__main__':
    main()
