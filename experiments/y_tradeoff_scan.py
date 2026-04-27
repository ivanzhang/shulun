#!/usr/bin/env python3
"""扫描小骨架 y 的权衡：模式密度、前洞高度、U+M3 收缩余量。

用法示例：
  python3 experiments/y_tradeoff_scan.py --P 32003 --ys 7,11,13 --K 8
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from d_distribution_m2_global import scan
from fixed_anchor_sieve_remainder import primes_upto


def parse_ys(text):
    """解析 y 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def skeleton_summary(y, K, shift_step=1):
    """计算骨架周期、密度和所有模式前 K 洞最大高度。"""
    small = primes_upto(y)
    M = math.prod(small)
    phi = math.prod(p - 1 for p in small)
    max_last = 0
    # 只在 M 不太大时全枚举；当前 y<=13 可接受。
    for c in range(0, M, max(1, shift_step)):
        holes = []
        r = 1
        while len(holes) < K:
            if math.gcd((r - c) % M, M) == 1:
                holes.append(r)
            r += 1
        max_last = max(max_last, holes[-1])
    return M, phi, phi / M, max_last


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=32003)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--ys', type=str, default='7,11,13')
    parser.add_argument('--K', type=int, default=8)
    parser.add_argument('--minN', type=int, default=200)
    parser.add_argument('--shift-step', type=int, default=1)
    args = parser.parse_args()

    print('P', args.P, 'K', args.K)
    print('y M phi density max_last_hole max_sum_U_M3 max_lambda steps_used')
    for y in parse_ys(args.ys):
        M, phi, density, max_last = skeleton_summary(y, args.K, args.shift_step)
        stats = scan(args.P, args.A, y, args.K)
        max_sum = 0.0
        max_lam = 0.0
        steps = 0
        for idx in range(1, args.K + 1):
            st = stats[idx]
            dist = st['dist']
            N = sum(dist.values())
            if N < args.minN:
                continue
            U = N - dist[0]
            M3 = sum(math.comb(d, 3) * c for d, c in dist.items() if d >= 3)
            max_sum = max(max_sum, (U + M3) / N)
            max_lam = max(max_lam, st['lam_sum'] / N)
            steps += 1
        print(y, M, phi, f'{density:.5f}', max_last, f'{max_sum:.4f}', f'{max_lam:.4f}', steps)


if __name__ == '__main__':
    main()
