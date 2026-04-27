#!/usr/bin/env python3
"""CRT 分布传递：实际 Mj 与自然筛矩 lambda^j/j! 对比。

用法示例：
  python3 experiments/crt_moment_transfer.py --Ps 4001,8009,16001 --K 8
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups, covered_by_patch


def parse_ps(text):
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def comb(n, k):
    return math.comb(n, k) if n >= k else 0


def lambda_for(P, y, n):
    Q = math.isqrt(n)
    return sum(1 / q for q in primes_upto(Q) if q > y and q != P)


def scan(P, A, y, K):
    stats = defaultdict(lambda: {'N': 0, 'M1': 0, 'M2': 0, 'M3': 0, 'M4': 0, 'L1': 0.0, 'L2': 0.0, 'L3': 0.0, 'L4': 0.0})
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if not survivors:
                break
            next_survivors = set()
            for a in survivors:
                n = a + r * P
                patches = [q for q, _ in factor(n) if q > y and q <= math.isqrt(n) and q != P]
                d = len(patches)
                lam = lambda_for(P, y, n)
                st = stats[idx]
                st['N'] += 1
                for j in range(1, 5):
                    st[f'M{j}'] += comb(d, j)
                    st[f'L{j}'] += (lam ** j) / math.factorial(j)
                if d >= 1:
                    next_survivors.add(a)
            survivors = next_survivors
    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='4001,8009,16001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=8)
    parser.add_argument('--minN', type=int, default=30)
    args = parser.parse_args()

    print('P step N M1/L1 M2/L2 M3/L3 M4/L4 M1N L1N M2N L2N M3N L3N')
    for P in parse_ps(args.Ps):
        stats = scan(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            st = stats[idx]
            N = st['N']
            if N < args.minN:
                continue
            ratios = []
            for j in range(1, 5):
                ratios.append(st[f'M{j}'] / st[f'L{j}'] if st[f'L{j}'] else 0.0)
            print(P, idx, N, *(f'{x:.3f}' for x in ratios), f'{st["M1"]/N:.3f}', f'{st["L1"]/N:.3f}', f'{st["M2"]/N:.3f}', f'{st["L2"]/N:.3f}', f'{st["M3"]/N:.3f}', f'{st["L3"]/N:.3f}')


if __name__ == '__main__':
    main()
