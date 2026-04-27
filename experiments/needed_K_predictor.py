#!/usr/bin/env python3
"""用条件模型预测使期望坏锚点数 < 1 所需 K。

用法示例：
  python3 experiments/needed_K_predictor.py --Ps 997,1999,4001 --Kmax 80
"""
import argparse
import math
import sys

sys.path.append('experiments')
from demand_side_bad_prefix import prefix_profile, prime_anchors
from fixed_anchor_sieve_remainder import primes_upto


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='997,1999,4001,8009')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--Kmax', type=int, default=80)
    args = parser.parse_args()

    skeleton_primes = primes_upto(args.y)
    C_y = math.prod(skeleton_primes) / math.prod(q - 1 for q in skeleton_primes)
    print('P N actual_max_first model_K_lt1 logP K_over_logP')
    for P in parse_ps(args.Ps):
        anchors = prime_anchors(P, args.A)
        model_counts = [0.0] * (args.Kmax + 1)
        max_first = 0
        for a in anchors:
            first, rows = prefix_profile(P, a, args.y, args.Kmax)
            first_key = first if first is not None else args.Kmax + 1
            max_first = max(max_first, first_key)
            prod = 1.0
            for T, row in enumerate(rows, start=1):
                p_prime = min(0.95, C_y / max(2.0, math.log(row['n'])))
                prod *= (1 - p_prime)
                model_counts[T] += prod
        model_K = next((T for T in range(1, args.Kmax + 1) if model_counts[T] < 1), None)
        print(P, len(anchors), max_first, model_K, f'{math.log(P):.3f}', f'{(model_K or 0)/math.log(P):.3f}')


if __name__ == '__main__':
    main()
