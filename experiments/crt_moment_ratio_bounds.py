#!/usr/bin/env python3
"""汇总 CRT 矩传递所需的常数边界。

用法示例：
  python3 experiments/crt_moment_ratio_bounds.py --Ps 4001,8009,16001 --K 8 --minN 100
"""
import argparse
import sys

sys.path.append('experiments')
from crt_moment_transfer import scan


def parse_ps(text):
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='4001,8009,16001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=8)
    parser.add_argument('--minN', type=int, default=100)
    args = parser.parse_args()
    rows = []
    for P in parse_ps(args.Ps):
        stats = scan(P, args.A, args.y, args.K)
        for idx, st in stats.items():
            N = st['N']
            if N < args.minN:
                continue
            ratios = [st[f'M{j}'] / st[f'L{j}'] if st[f'L{j}'] else 0 for j in range(1, 5)]
            rows.append((P, idx, N, ratios, st))
    print('count', len(rows), 'minN', args.minN)
    for j in range(1, 5):
        vals = [(r[3][j-1], r[0], r[1], r[2]) for r in rows]
        print('M%d/L%d min' % (j,j), min(vals), 'max', max(vals))
    # IE bound with empirical constants that hold in sample for N>=minN.
    c1 = max(r[3][0] for r in rows)
    c2 = min(r[3][1] for r in rows)
    c3 = max(r[3][2] for r in rows)
    print('empirical_constants c1_max c2_min c3_max', f'{c1:.3f}', f'{c2:.3f}', f'{c3:.3f}')
    worst = []
    for P, idx, N, ratios, st in rows:
        L1 = st['L1'] / N
        L2 = st['L2'] / N
        L3 = st['L3'] / N
        bound = c1 * L1 - c2 * L2 + c3 * L3
        actual = (st['M1'] - st['M2'] + st['M3']) / N
        worst.append((bound, actual, P, idx, N, L1))
    print('worst_bound', max(worst))
    print('worst_actual', max(worst, key=lambda x: x[1]))

if __name__ == '__main__':
    main()
