#!/usr/bin/env python3
"""统计四补丁候选乘积落入前洞数值范围的稀疏性。

用法示例：
  python3 experiments/h4_candidate_products.py --P 16001 --rmax 100
"""
import argparse
import itertools
import math
from collections import Counter

from fixed_anchor_sieve_remainder import primes_upto


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=16001)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--rmax', type=int, default=100)
    args = parser.parse_args()

    nmax = args.P * args.rmax + args.P
    Q = math.isqrt(nmax)
    primes = [q for q in primes_upto(Q) if q > args.y]
    count_by_r = Counter()
    total = 0
    small = []
    for quad in itertools.combinations(primes, 4):
        prod = math.prod(quad)
        if prod > nmax:
            break
        total += 1
        if len(small) < 15:
            small.append((quad, prod))
        # 若 n=a+rP，a<P，则 r=floor(n/P)。这里只看乘积自身的高度层。
        count_by_r[prod // args.P] += 1
    print('P', args.P, 'nmax', nmax, 'Q', Q, 'prime_count', len(primes), 'quad_products_le_nmax', total)
    print('first_products', small)
    print('top_height_layers', count_by_r.most_common(20))


if __name__ == '__main__':
    main()
