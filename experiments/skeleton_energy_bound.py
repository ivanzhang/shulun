#!/usr/bin/env python3
"""B_y 前 K 洞的确定性共享能量上界。

用法示例：
  python3 experiments/skeleton_energy_bound.py --y 7 --Kmax 80
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import primes_upto


def skeleton_holes(c, y, K):
    """生成 gcd(r-c,M_y)=1 的前 K 个正高度。"""
    primes = primes_upto(y)
    M = math.prod(primes)
    holes = []
    r = 1
    while len(holes) < K:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def omega_gt_y(n, y):
    """n 的大于 y 的不同素因子数。"""
    count = 0
    x = n
    for p in primes_upto(math.isqrt(x) + 1):
        if p * p > x:
            break
        if x % p == 0:
            if p > y:
                count += 1
            while x % p == 0:
                x //= p
    if x > 1 and x > y:
        count += 1
    return count


def energy(holes, y):
    """共享补丁能量的确定性上界 sum omega_{>y}(|r-s|)。"""
    value = 0
    dist = Counter()
    for i, r in enumerate(holes):
        for s in holes[i + 1:]:
            w = omega_gt_y(abs(s - r), y)
            value += w
            dist[w] += 1
    return value, dist


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--Kmax', type=int, default=80)
    parser.add_argument('--shift-step', type=int, default=1)
    args = parser.parse_args()

    M = math.prod(primes_upto(args.y))
    shifts = range(0, M, max(1, args.shift_step))
    print(f'y={args.y}, M={M}, shifts={len(list(shifts))}, shift_step={args.shift_step}')
    print('K maxE avgE maxD argmax_c ratio_E_K2 dist_at_max')
    for K in [5, 10, 15, 20, 25, 30, 40, 60, args.Kmax]:
        vals = []
        best = None
        for c in shifts:
            holes = skeleton_holes(c, args.y, K)
            e, dist = energy(holes, args.y)
            rec = (e, holes[-1] - holes[0], c, dist)
            vals.append(rec)
            if best is None or rec > best:
                best = rec
        max_e, max_d, arg_c, dist = best
        avg_e = sum(v[0] for v in vals) / len(vals)
        print(K, max_e, f'{avg_e:.2f}', max_d, arg_c, f'{max_e/(K*K):.4f}', sorted(dist.items()))


if __name__ == '__main__':
    main()
