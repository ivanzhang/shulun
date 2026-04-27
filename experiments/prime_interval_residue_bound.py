#!/usr/bin/env python3
"""素数短区间 A<a<P 在模 q 上的平凡桶界与实际桶。

用法示例：
  python3 experiments/prime_interval_residue_bound.py --P 1999 --qmax 150
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=1999)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--qmax', type=int, default=150)
    args = parser.parse_args()

    flags = sieve(args.P)
    anchors = [a for a in range(args.A + 1, args.P) if flags[a]]
    N = len(anchors)
    print(f'P={args.P}, A={args.A}, N={N}')
    print('q max_count interval_trivial ceilPq ratio_to_Nq')
    for q in primes_upto(args.qmax):
        if q == args.P:
            continue
        counter = Counter(a % q for a in anchors)
        max_count = max(counter.values(), default=0)
        # 不用素数性，仅短区间长度给出的严格平凡上界。
        interval_trivial = (args.P - args.A - 2) // q + 1
        ratio = max_count / (N / q) if N else 0
        print(q, max_count, interval_trivial, math.ceil(args.P / q), f'{ratio:.2f}')


if __name__ == '__main__':
    main()
