#!/usr/bin/env python3
"""多 P 汇总小骨架洞序号条件素数率。

用法示例：
  python3 experiments/hole_rate_multiP.py --Ps 541,997,1321,1439 --Kmax 20
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import collect_stats


def parse_ps(text):
    """解析逗号分隔的素数 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='541,997,1321,1439')
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--Kmax', type=int, default=20)
    args = parser.parse_args()

    skeleton_primes = primes_upto(args.y)
    C_y = math.prod(skeleton_primes) / math.prod(q - 1 for q in skeleton_primes)
    merged = defaultdict(lambda: [0, 0, 0.0])

    print(f"Ps={args.Ps}, y={args.y}, Cy={C_y:.6f}, Kmax={args.Kmax}")
    print('per_P P rows mean_ratio first_ratio last_ratio')
    for P in parse_ps(args.Ps):
        rows, stats = collect_stats(P, args.y, args.A, args.Kmax)
        ratios = []
        for idx in range(1, args.Kmax + 1):
            total, primes, invlog_sum = stats[idx]
            if not total:
                continue
            avg = invlog_sum / total
            expected = C_y * avg
            ratio = (primes / total) / expected if expected else 0.0
            ratios.append(ratio)
            merged[idx][0] += total
            merged[idx][1] += primes
            merged[idx][2] += invlog_sum
        first_ratio = ratios[0] if ratios else 0.0
        last_ratio = ratios[-1] if ratios else 0.0
        mean_ratio = sum(ratios) / len(ratios) if ratios else 0.0
        print('per_P', P, len(rows), f"{mean_ratio:.3f}", f"{first_ratio:.3f}", f"{last_ratio:.3f}")

    print('merged idx total primes rate expected ratio')
    for idx in range(1, args.Kmax + 1):
        total, primes, invlog_sum = merged[idx]
        if not total:
            continue
        rate = primes / total
        expected = C_y * invlog_sum / total
        ratio = rate / expected if expected else 0.0
        print('merged', idx, total, primes, f"{rate:.4f}", f"{expected:.4f}", f"{ratio:.3f}")


if __name__ == '__main__':
    main()
