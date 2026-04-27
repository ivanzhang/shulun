#!/usr/bin/env python3
"""全模板聚合的补丁命中数 d(a) 分布与 M2 下界诊断。

用法示例：
  python3 experiments/d_distribution_m2_global.py --Ps 4001,8009,16001 --K 8
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups, covered_by_patch
from fixed_anchor_sieve_remainder import primes_upto


def parse_ps(text):
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def lambda_for(P, y, n):
    return sum(1/q for q in primes_upto(math.isqrt(n)) if q > y and q != P)


def scan(P, A, y, K):
    stats = defaultdict(lambda: {'dist': Counter(), 'lam_sum': 0.0, 'lam2_sum': 0.0, 'd_sum': 0, 'd2_sum': 0})
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if not survivors:
                break
            next_survivors = set()
            st = stats[idx]
            for a in survivors:
                n = a + r * P
                d = len([q for q, _ in factor(n) if q > y and q <= math.isqrt(n) and q != P])
                lam = lambda_for(P, y, n)
                st['dist'][d] += 1
                st['d_sum'] += d
                st['d2_sum'] += d*d
                st['lam_sum'] += lam
                st['lam2_sum'] += lam*lam
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

    print('P step N avg_d avg_lambda M2/L2 d0 d1 d2 d3 d4plus')
    for P in parse_ps(args.Ps):
        stats = scan(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            st = stats[idx]
            dist = st['dist']
            N = sum(dist.values())
            if N < args.minN:
                continue
            M2 = sum(math.comb(d, 2) * c for d, c in dist.items() if d >= 2)
            L2 = st['lam2_sum'] / 2
            d4plus = sum(c for d, c in dist.items() if d >= 4)
            print(P, idx, N, f'{st["d_sum"]/N:.3f}', f'{st["lam_sum"]/N:.3f}', f'{M2/L2 if L2 else 0:.3f}', dist[0], dist[1], dist[2], dist[3], d4plus)


if __name__ == '__main__':
    main()
