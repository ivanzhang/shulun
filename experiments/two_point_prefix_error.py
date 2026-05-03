#!/usr/bin/env python3
"""检验二点奇异级数前缀误差 A(x)=sum_{d<=x}(S2(d)-1)。"""
import argparse
import math
from high_threshold_margin_fast import sieve, primes
from two_point_singular_average import s2_ratio_direct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=8009)
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--points', default='')
    args = ap.parse_args()
    P = args.P
    flags = sieve(P)
    root = primes(flags, P)
    y = int(args.c * P)
    small = [q for q in root if q <= y]
    if args.points:
        points = [int(x) for x in args.points.split(',') if x.strip()]
    else:
        raw = [10,20,30,50,80,100,150,200,300,500,800,1000,1500,2000,3000,5000,8000]
        points = [x for x in raw if x < P]
        if P-1 not in points:
            points.append(P-1)
    point_set = set(points)
    prefix = 0.0
    max_abs = (0.0, 0)
    print(f'P={P} y={y} pi_y={len(small)}')
    print('x A(x) A/logx A/sqrtx avgS_prefix')
    for d in range(1, P):
        s = s2_ratio_direct(d, small)
        prefix += s - 1.0
        if abs(prefix) > max_abs[0]:
            max_abs = (abs(prefix), d)
        if d in point_set:
            lx = math.log(max(d, 2))
            print(f'{d} {prefix:.6f} {prefix/lx:.6f} {prefix/math.sqrt(d):.6f} {1+prefix/d:.6f}')
    print(f'maxAbsPrefix {max_abs[0]:.6f} at {max_abs[1]} ratioLog {max_abs[0]/math.log(P):.6f}')


if __name__ == '__main__':
    main()
