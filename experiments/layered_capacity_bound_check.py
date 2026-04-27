#!/usr/bin/env python3
"""层级容量界检查。

用扫描得到的层级上限（例如 T<=40: cap>=4最多1个, cap>=3最多4个）
构造一个简洁的容量上界，并与实际最大 saving 对比。

用法示例：
    python3 experiments/layered_capacity_bound_check.py --Tlist 20,25,30,36,40
"""
import argparse
import sys
from collections import Counter

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c
from slope_capacity_lift_bound import capacity_profile


def layer_counts(profile):
    return {k: sum(1 for _q, cap in profile if cap >= k) for k in range(1, 8)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Tlist', default='20,25,30,36,40')
    args = parser.parse_args()
    print('T max_saving max_ge2 max_ge3 max_ge4 max_ge5 worst_c top_profile')
    for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
        max_saving = 0
        max_layers = {k: 0 for k in range(2, 6)}
        worst = None
        for c in range(M):
            holes = holes_for_c(c, T)
            profile = capacity_profile(holes)
            saving_capacity = sum(cap for _q, cap in profile)
            layers = layer_counts(profile)
            for k in max_layers:
                max_layers[k] = max(max_layers[k], layers[k])
            if saving_capacity > max_saving:
                max_saving = saving_capacity
                worst = (c, sorted(profile, key=lambda x: (-x[1], x[0]))[:25])
        print(T, max_saving, max_layers[2], max_layers[3], max_layers[4], max_layers[5], worst[0], worst[1])


if __name__ == '__main__':
    main()
