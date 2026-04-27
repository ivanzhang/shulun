#!/usr/bin/env python3
"""按 B_y 前洞模式统计坏前缀衰减。

用法示例：
  python3 experiments/pattern_bad_prefix.py --P 4001 --Kmax 15
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

sys.path.append('experiments')
from demand_side_bad_prefix import prefix_profile, prime_anchors
from fixed_anchor_sieve_remainder import primes_upto
from shared_patch_energy import front_holes


def pattern_id(P, a, y):
    """B_y 洞模式由小模数覆盖锚点决定。"""
    return tuple((-a * pow(P, -1, p)) % p for p in primes_upto(y))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=4001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--Kmax', type=int, default=15)
    parser.add_argument('--top', type=int, default=12)
    args = parser.parse_args()

    anchors = prime_anchors(args.P, args.A)
    groups = defaultdict(list)
    for a in anchors:
        groups[pattern_id(args.P, a, args.y)].append(a)

    skeleton_primes = primes_upto(args.y)
    C_y = math.prod(skeleton_primes) / math.prod(q - 1 for q in skeleton_primes)
    records = []
    for pat, vals in groups.items():
        survive = Counter()
        model = Counter()
        max_first = 0
        common_holes = None
        for a in vals:
            first, rows = prefix_profile(args.P, a, args.y, args.Kmax)
            max_first = max(max_first, first if first is not None else args.Kmax + 1)
            holes = tuple(x['r'] for x in rows)
            if common_holes is None:
                common_holes = holes
            elif common_holes != holes:
                common_holes = ('mixed',)
            prod = 1.0
            for T, row in enumerate(rows, start=1):
                if all(not x['prime'] for x in rows[:T]):
                    survive[T] += 1
                prod *= 1 - min(0.95, C_y / max(2.0, math.log(row['n'])))
                model[T] += prod
        T = min(args.Kmax, 10)
        rate = survive[T] / len(vals)
        model_rate = model[T] / len(vals)
        records.append((rate, model_rate, len(vals), max_first, pat, common_holes, survive[T]))

    print('P', args.P, 'N', len(anchors), 'patterns', len(groups), 'Kmax', args.Kmax)
    print('largest_groups size max_first pat first_holes')
    for pat, vals in sorted(groups.items(), key=lambda kv: -len(kv[1]))[:args.top]:
        holes = front_holes(args.P, vals[0], args.y, min(args.Kmax, 10))
        print('group', len(vals), max(prefix_profile(args.P, a, args.y, args.Kmax)[0] or args.Kmax+1 for a in vals), pat, holes)
    print('worst_by_T10 rate model size max_first survivors pat holes')
    for rec in sorted(records, reverse=True)[:args.top]:
        rate, model_rate, size, max_first, pat, holes, surv = rec
        print('worst', f'{rate:.4f}', f'{model_rate:.4f}', size, max_first, surv, pat, holes[:10] if isinstance(holes, tuple) else holes)


if __name__ == '__main__':
    main()
