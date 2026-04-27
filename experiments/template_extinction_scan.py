#!/usr/bin/env python3
"""扫描固定模板覆盖筛的最大灭绝深度。

用法示例：
  python3 experiments/template_extinction_scan.py --Ps 997,1999,4001 --K 30
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from template_cover_sieve import template_groups, covered_by_patch


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def extinction_depth(P, A, y, K):
    """返回所有模板的最晚灭绝深度。"""
    groups = template_groups(P, A, y, K)
    worst = []
    for group in groups:
        survivors = set(group['anchors'])
        extinct_at = None
        for idx, r in enumerate(group['holes'], start=1):
            survivors = {a for a in survivors if covered_by_patch(P, a, r, y)}
            if not survivors:
                extinct_at = idx
                break
        if extinct_at is None:
            extinct_at = K + 1
        worst.append((extinct_at, len(group['anchors']), group['pattern'], group['holes'], len(survivors)))
    return sorted(worst, reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='997,1999,4001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=30)
    parser.add_argument('--top', type=int, default=5)
    args = parser.parse_args()

    print('P max_extinct_at logP ratio top')
    for P in parse_ps(args.Ps):
        worst = extinction_depth(P, args.A, args.y, args.K)
        max_ext = worst[0][0]
        print('P', P, 'max_extinct_at', max_ext, 'logP', f'{math.log(P):.3f}', 'ratio', f'{max_ext/math.log(P):.3f}')
        for rec in worst[:args.top]:
            print('  worst', rec[0], 'size', rec[1], 'remaining', rec[4], 'pat', rec[2], 'holes', rec[3][:min(args.K, 12)])


if __name__ == '__main__':
    main()
