#!/usr/bin/env python3
"""补丁命中数 d(a) 的阶乘矩扫描。

用法示例：
  python3 experiments/factorial_moment_scan.py --Ps 997,1999,4001,8009,16001 --K 8
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups, covered_by_patch


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def comb(n, k):
    """小组合数。"""
    if n < k:
        return 0
    return math.comb(n, k)


def scan_P(P, A, y, K):
    """逐步统计 d 的阶乘矩。"""
    stats = defaultdict(lambda: {'N': 0, 'U': 0, 'M1': 0, 'M2': 0, 'M3': 0, 'M4': 0, 'lambda_sum': 0.0})
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if not survivors:
                break
            for a in survivors:
                n = a + r * P
                patches = [q for q, _ in factor(n) if q > y and q <= math.isqrt(n) and q != P]
                d = len(patches)
                stats[idx]['N'] += 1
                stats[idx]['U'] += 1 if d >= 1 else 0
                stats[idx]['M1'] += comb(d, 1)
                stats[idx]['M2'] += comb(d, 2)
                stats[idx]['M3'] += comb(d, 3)
                stats[idx]['M4'] += comb(d, 4)
                # 该点自然 lambda。
                qsum = sum(1 / q for q in range(1, 2))  # 占位避免导入额外函数。
            survivors = {a for a in survivors if covered_by_patch(P, a, r, y)}
    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='997,1999,4001,8009,16001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=8)
    args = parser.parse_args()

    print('P step N U keep M1/N M2/N M3/N M4/N IE3/N poisson_lambda_est')
    for P in parse_ps(args.Ps):
        stats = scan_P(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            s = stats[idx]
            N = s['N']
            if not N:
                continue
            ie3 = s['M1'] - s['M2'] + s['M3']
            # 用 M1 作为 lambda 估计，Poisson union=1-exp(-lambda)。
            lam = s['M1'] / N
            print(P, idx, N, s['U'], f'{s["U"]/N:.4f}', f'{s["M1"]/N:.4f}', f'{s["M2"]/N:.4f}', f'{s["M3"]/N:.4f}', f'{s["M4"]/N:.5f}', f'{ie3/N:.4f}', f'{1-math.exp(-lam):.4f}')


if __name__ == '__main__':
    main()
