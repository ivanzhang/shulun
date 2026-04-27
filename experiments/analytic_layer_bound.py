#!/usr/bin/env python3
"""2q 间隔解析层级界对照。

若同一 q 余数类中的 B11 前洞同奇偶，则相邻高度差至少 2q，
故 cap>=j 需要 q<=D/(2j)。本脚本比较解析上界与实际 A_j 最大值。

用法示例：
    python3 experiments/analytic_layer_bound.py --Tlist 20,25,30,36,40,60
"""
import argparse
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c
from slope_capacity_lift_bound import capacity_profile
from fixed_anchor_sieve_remainder import primes_upto

Y = 11


def actual_max_layers(T):
    max_layers = defaultdict(int)
    max_D = 0
    min_D = 10**9
    for c in range(M):
        holes = holes_for_c(c, T)
        D = max(holes) - min(holes)
        max_D = max(max_D, D)
        min_D = min(min_D, D)
        profile = capacity_profile(holes)
        for j in range(1, 10):
            val = sum(1 for _q, cap in profile if cap >= j)
            max_layers[j] = max(max_layers[j], val)
    return min_D, max_D, dict(max_layers)


def analytic_bound(D, j):
    return len([p for p in primes_upto(D // (2 * j)) if p > Y])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Tlist', default='20,25,30,36,40,60')
    args = parser.parse_args()
    print('T minD maxD j actual_Aj bound_maxD')
    for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
        minD, maxD, layers = actual_max_layers(T)
        for j in range(1, 7):
            print(T, minD, maxD, j, layers.get(j, 0), analytic_bound(maxD, j))
        print('---')


if __name__ == '__main__':
    main()
