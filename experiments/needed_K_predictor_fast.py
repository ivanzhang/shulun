#!/usr/bin/env python3
"""快速预测使条件模型期望坏锚点数 < 1 的 K。\n\n用法示例：\n  python3 experiments/needed_K_predictor_fast.py --Ps 997,1999,4001,8009 --Kmax 80\n"""
import argparse
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from shared_patch_energy import front_holes


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def prime_anchors(P, A):
    """边界锚点短区间。"""
    flags = sieve(P)
    return [a for a in range(A + 1, P) if flags[a]]


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
        hole_map = {a: front_holes(P, a, args.y, args.Kmax) for a in anchors}
        max_r = max(r for holes in hole_map.values() for r in holes)
        flags = sieve(P * max_r + P)
        model_counts = [0.0] * (args.Kmax + 1)
        max_first = 0
        for a, holes in hole_map.items():
            first = None
            prod = 1.0
            for T, r in enumerate(holes, start=1):
                n = a + r * P
                if flags[n] and first is None:
                    first = T
                p_prime = min(0.95, C_y / max(2.0, math.log(n)))
                prod *= (1 - p_prime)
                model_counts[T] += prod
            max_first = max(max_first, first if first is not None else args.Kmax + 1)
        model_K = next((T for T in range(1, args.Kmax + 1) if model_counts[T] < 1), None)
        print(P, len(anchors), max_first, model_K, f'{math.log(P):.3f}', f'{(model_K or 0)/math.log(P):.3f}')


if __name__ == '__main__':
    main()
