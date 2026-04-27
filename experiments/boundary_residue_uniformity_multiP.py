#!/usr/bin/env python3
"""多 P 边界锚点模 q 均匀性汇总。

用法示例：
  python3 experiments/boundary_residue_uniformity_multiP.py --Ps 541,997,1321 --qmax 100
"""
import argparse
import sys
from collections import Counter

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from zero_repair_boundary_scan import boundary_events


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='541,661,797,997,1151,1321,1439')
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--qmax', type=int, default=100)
    args = parser.parse_args()

    worst = []
    for P in parse_ps(args.Ps):
        anchors = [x['a'] for x in boundary_events(P, args.y, P) if args.A < x['a'] < P]
        N = len(anchors)
        max_ratio = 0.0
        max_add = 0.0
        arg_ratio = None
        arg_add = None
        for q in primes_upto(args.qmax):
            if q <= args.y or q == P:
                continue
            counter = Counter(a % q for a in anchors)
            max_count = max(counter.values(), default=0)
            avg = N / q
            ratio = max_count / max(1e-9, avg)
            add = max_count - avg
            if ratio > max_ratio:
                max_ratio = ratio
                arg_ratio = (q, max_count, avg)
            if add > max_add:
                max_add = add
                arg_add = (q, max_count, avg)
        worst.append((P, N, max_ratio, max_add, arg_ratio, arg_add))
        print('P', P, 'N', N, 'max_ratio', f'{max_ratio:.2f}', 'at', arg_ratio, 'max_add', f'{max_add:.2f}', 'at', arg_add)
    print('global_max_ratio', max(worst, key=lambda x: x[2]))
    print('global_max_add', max(worst, key=lambda x: x[3]))


if __name__ == '__main__':
    main()
