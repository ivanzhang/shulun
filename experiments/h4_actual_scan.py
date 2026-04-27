#!/usr/bin/env python3
"""快速扫描实际 H4：直接按幸存点分解补丁因子，而不枚举所有四元组。

用法示例：
  python3 experiments/h4_actual_scan.py --Ps 997,1999,4001,8009 --K 12
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups, covered_by_patch


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def h4_scan_for_P(P, A, y, K):
    """返回每步实际 H4 与四重以上点数量。"""
    step = defaultdict(lambda: {'before': 0, 'h4': 0, 'deg_ge4': 0, 'max_deg': 0, 'examples': []})
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if not survivors:
                break
            stat = step[idx]
            stat['before'] += len(survivors)
            next_survivors = set()
            for a in survivors:
                n = a + r * P
                patches = [q for q, _ in factor(n) if q > y and q <= math.isqrt(n) and q != P]
                deg = len(patches)
                if deg:
                    next_survivors.add(a)
                if deg >= 4:
                    stat['deg_ge4'] += 1
                    stat['h4'] += math.comb(deg, 4)
                    stat['max_deg'] = max(stat['max_deg'], deg)
                    if len(stat['examples']) < 5:
                        stat['examples'].append((a, r, n, patches))
            survivors = next_survivors
    return step


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='997,1999,4001,8009')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    args = parser.parse_args()

    print('P step before deg_ge4 H4 max_deg H4_per_before examples')
    for P in parse_ps(args.Ps):
        stats = h4_scan_for_P(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            s = stats[idx]
            if not s['before']:
                continue
            print(P, idx, s['before'], s['deg_ge4'], s['h4'], s['max_deg'], f"{s['h4']/s['before']:.6f}", s['examples'][:2])


if __name__ == '__main__':
    main()
