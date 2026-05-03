#!/usr/bin/env python3
"""用除数展开分解二点奇异级数前缀误差。"""
import argparse
import math
from high_threshold_margin_fast import sieve, primes


def build_b_values(limit, small_primes):
    # 生成 m<=limit 的奇方自由 b(m)=prod 1/(q-2)，q<=y。
    vals = [(1, 1.0)]
    for q in small_primes:
        if q == 2 or q > limit:
            continue
        add = []
        w = 1.0 / (q - 2)
        for m, b in vals:
            nm = m * q
            if nm <= limit:
                add.append((nm, b * w))
        vals.extend(add)
    vals.sort()
    return vals


def cy_value(small):
    c = 1.0
    for q in small:
        if q >= 3:
            c *= 1.0 - 1.0 / ((q - 1) * (q - 1))
    return c


def exact_prefix_from_b(x, cy, bvals):
    total = 0.0
    floor_err = 0.0
    main_partial = 0.0
    for m, b in bvals:
        if m <= x // 2:
            total += b * (x // (2 * m))
            real = x / (2 * m)
            main_partial += b * real
            floor_err += b * ((x // (2 * m)) - real)
    even_sum = 2 * cy * total
    main = 2 * cy * main_partial
    return even_sum - x, main - x, 2 * cy * floor_err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=20011)
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--points', default='100,200,500,1000,2000,5000,10000,20000')
    args = ap.parse_args()
    P = args.P
    flags = sieve(P)
    root = primes(flags, P)
    y = int(args.c * P)
    small = [q for q in root if q <= y]
    cy = cy_value(small)
    max_x = min(P - 1, max(int(v) for v in args.points.split(',') if v.strip()))
    bvals = build_b_values(max_x // 2, small)
    total_mass_partial = cy * sum(b / m for m, b in bvals)
    print(f'P={P} y={y} cy={cy:.8f} bCount={len(bvals)} partialMass={total_mass_partial:.8f}')
    print('x A_exact mainMinusX floorErr inferredTail xTailApprox')
    for x in [int(v) for v in args.points.split(',') if v.strip() and int(v) < P]:
        A, main_minus_x, floor_err = exact_prefix_from_b(x, cy, bvals)
        # A = mainMinusX + floorErr；其中 mainMinusX = -x * tail_mass_approx（相对完整质量1）
        print(f'{x} {A:.6f} {main_minus_x:.6f} {floor_err:.6f} {-main_minus_x:.6f}')


if __name__ == '__main__':
    main()
