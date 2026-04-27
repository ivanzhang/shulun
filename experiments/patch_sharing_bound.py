#!/usr/bin/env python3
"""补丁共享上界验证。

严格事实：若同一个 q>y 同时补两个洞 r,s，则 q | (r-s)。
因此 q 的共享能力完全受洞距集合 D={|r-s|} 的素因子限制。
本脚本计算：
- 理论可共享补丁 q 集合：q>y 且 q | 某个洞距；
- 实际共享 q 是否包含其中；
- 当 y > R/2 时，大补丁不可能共享，只能一洞一补。

用法示例：
    python3 experiments/patch_sharing_bound.py --P 461 --a 22 --R 81 --y 13 --detail
    python3 experiments/patch_sharing_bound.py --scan --maxP 2000 --y 13 --top 20
"""
import argparse
import math
from collections import Counter, defaultdict

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from hole_factor_constraints import record as factor_record


def prime_factors_set(n):
    out = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.add(n)
    return out


def sharing_record(P, a, R, y):
    rec = factor_record(P, a, R, y)
    holes = rec['holes']
    Q = rec['Q']
    distance_prime_counter = Counter()
    possible_shared = set()
    distance_examples = defaultdict(list)
    for i, r in enumerate(holes):
        for s in holes[i+1:]:
            d = abs(s - r)
            for p in prime_factors_set(d):
                if y < p <= Q:
                    possible_shared.add(p)
                    distance_prime_counter[p] += 1
                    if len(distance_examples[p]) < 5:
                        distance_examples[p].append((r, s, d))
    actual_shared = {q for q, rs, gaps, ok in rec['shared']}
    return {
        **rec,
        'possible_shared': sorted(possible_shared),
        'actual_shared': sorted(actual_shared),
        'missing_possible': sorted(possible_shared - actual_shared),
        'unexpected_actual': sorted(actual_shared - possible_shared),
        'distance_prime_counter': distance_prime_counter,
        'distance_examples': dict(distance_examples),
        'no_share_if_y_gt_R2': y > R / 2,
        'share_capacity_bound': len(holes) + sum(distance_prime_counter.values()),
    }


def print_record(rec, detail=False):
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},y={rec['y']},holes={rec['hole_count']},"
        f"actual_shared={rec['actual_shared']},possible_shared={rec['possible_shared']},"
        f"unexpected={rec['unexpected_actual']},dist_prime_events={sum(rec['distance_prime_counter'].values())},"
        f"patch_hits={sum(len(row['patch']) for row in rec['rows'])},"
        f"share_cap_bound={rec['share_capacity_bound']}"
    )
    if detail:
        print('holes=', rec['holes'])
        print('distance_prime_counter=', sorted(rec['distance_prime_counter'].items()))
        print('distance_examples=', rec['distance_examples'])
        print('actual shared detail=', [(q, rs) for q, rs, gaps, ok in rec['shared']])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--a', type=int, default=22)
    ap.add_argument('--R', type=int, default=0)
    ap.add_argument('--y', type=int, default=13)
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=2000)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()
    if args.scan:
        flags = sieve(args.maxP * args.maxP)
        out = []
        for P in primes_upto(args.maxP):
            if P < 3:
                continue
            worst_a, worst_R = 1, -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_a, worst_R = a, r0
            if worst_R > 0:
                out.append(sharing_record(P, worst_a, worst_R, args.y))
        out.sort(key=lambda x: (-x['R'], -len(x['actual_shared'])))
        for rec in out[:args.top]:
            print_record(rec, detail=False)
    else:
        R = args.R
        if not R:
            flags = sieve(args.P * args.P)
            R = first_prime_r(args.P, args.a, flags)
        print_record(sharing_record(args.P, args.a, R, args.y), detail=args.detail)


if __name__ == '__main__':
    main()
