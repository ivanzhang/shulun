#!/usr/bin/env python3
"""扫描补丁命中数二阶非退化比 sum d^2 / sum d。

用法示例：
  python3 experiments/d_second_moment_ratio.py --Ps 4001,8009,16001 --K 10
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

sys.path.append('experiments')
from d_distribution_m2_global import scan


def parse_ps(text):
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='4001,8009,16001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=10)
    parser.add_argument('--minN', type=int, default=50)
    args = parser.parse_args()

    rows = []
    print('P step N sumd sumd2 ratio c_excess M2_over_M1 dist')
    for P in parse_ps(args.Ps):
        stats = scan(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            st = stats[idx]
            dist = st['dist']
            N = sum(dist.values())
            if N < args.minN:
                continue
            sumd = st['d_sum']
            sumd2 = st['d2_sum']
            M2 = (sumd2 - sumd) / 2
            ratio = sumd2 / sumd if sumd else 0
            rows.append((ratio, P, idx, N, dist))
            print(P, idx, N, sumd, sumd2, f'{ratio:.3f}', f'{ratio-1:.3f}', f'{M2/sumd if sumd else 0:.3f}', dict(sorted(dist.items())))
    print('min_ratio', min(rows) if rows else None)
    print('max_ratio', max(rows) if rows else None)


if __name__ == '__main__':
    main()
