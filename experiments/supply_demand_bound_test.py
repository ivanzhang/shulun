#!/usr/bin/env python3
"""测试平凡模桶供给界是否足以推出供需矛盾。

用法示例：
  python3 experiments/supply_demand_bound_test.py --P 997 --K 20
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from hole_index_prime_rate import factor, isprimefac
from shared_patch_energy import front_holes


def prime_anchors(P, A):
    """边界锚点除 a=P 外即第一行素数短区间。"""
    flags = sieve(P)
    return [a for a in range(A + 1, P) if flags[a]]


def trivial_bucket(P, A, q):
    """短区间中任一模 q 桶的严格平凡上界。"""
    return (P - A - 2) // q + 1


def exact_bucket(anchors, q):
    """实际最大桶。"""
    counts = Counter(a % q for a in anchors)
    return max(counts.values(), default=0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=997)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=20)
    args = parser.parse_args()

    anchors = prime_anchors(args.P, args.A)
    N = len(anchors)
    demand = 0
    actual_patch_records = 0
    r_values = set()
    max_n = 0
    for a in anchors:
        holes = front_holes(args.P, a, args.y, args.K)
        for r in holes:
            r_values.add(r)
            n = a + r * args.P
            max_n = max(max_n, n)
            fac = factor(n)
            if not isprimefac(fac, n):
                demand += 1
                actual_patch_records += sum(1 for q, _ in fac if args.y < q <= math.isqrt(n) and q != args.P)

    Q = math.isqrt(max_n)
    primes = [q for q in primes_upto(Q) if q > args.y and q != args.P]
    trivial_supply = sum(trivial_bucket(args.P, args.A, q) for q in primes for _ in r_values)
    exact_supply = sum(exact_bucket(anchors, q) for q in primes for _ in r_values)
    print('P', args.P, 'N', N, 'K', args.K, 'distinct_r', len(r_values), 'Q', Q)
    print('demand_composite_holes', demand, 'actual_patch_records', actual_patch_records)
    print('trivial_supply_upper', trivial_supply, 'ratio_supply_demand', f'{trivial_supply / max(1,demand):.2f}')
    print('exact_bucket_supply_upper', exact_supply, 'ratio_supply_demand', f'{exact_supply / max(1,demand):.2f}')
    print('note', '若供给上界仍大于需求，则仅靠模桶界无法闭合，需要加入每个 a 的共享能量/每个 q 的高度兼容。')


if __name__ == '__main__':
    main()
