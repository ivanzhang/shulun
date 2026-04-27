#!/usr/bin/env python3
"""多 P 前洞全合数生存率汇总。

用法示例：
  python3 experiments/bad_prefix_multiP.py --Ps 997,1999,4001 --Kmax 20
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from demand_side_bad_prefix import prefix_profile, prime_anchors
from fixed_anchor_sieve_remainder import primes_upto


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='541,997,1999,4001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--Kmax', type=int, default=20)
    args = parser.parse_args()

    skeleton_primes = primes_upto(args.y)
    C_y = math.prod(skeleton_primes) / math.prod(q - 1 for q in skeleton_primes)
    total_N = 0
    survive = Counter()
    expected_survive_weight = Counter()
    print('P N max_first avg_first')
    for P in parse_ps(args.Ps):
        anchors = prime_anchors(P, args.A)
        total_N += len(anchors)
        firsts = []
        for a in anchors:
            first, rows = prefix_profile(P, a, args.y, args.Kmax)
            first_key = first if first is not None else args.Kmax + 1
            firsts.append(first_key)
            prod = 1.0
            for T, row in enumerate(rows, start=1):
                if not row['prime'] and all(not x['prime'] for x in rows[:T]):
                    survive[T] += 1
                p_prime = min(0.95, C_y / max(2.0, math.log(row['n'])))
                prod *= (1 - p_prime)
                expected_survive_weight[T] += prod
        print(P, len(anchors), max(firsts), f'{sum(firsts)/len(firsts):.3f}')
    print('merged_N', total_N, 'Cy', f'{C_y:.3f}')
    print('T actual_survivors actual_rate cond_model_rate ratio')
    for T in range(1, args.Kmax + 1):
        actual_rate = survive[T] / total_N if total_N else 0
        model_rate = expected_survive_weight[T] / total_N if total_N else 0
        ratio = actual_rate / model_rate if model_rate else 0
        print(T, survive[T], f'{actual_rate:.5f}', f'{model_rate:.5f}', f'{ratio:.3f}')


if __name__ == '__main__':
    main()
