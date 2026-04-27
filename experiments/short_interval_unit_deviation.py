#!/usr/bin/env python3
"""模1155单位集合的短区间偏差常数。

计算任意长度 n 的连续区间中，最多包含多少个与1155互素的剩余类，
并比较 (480/1155)n 的偏差。
这给出 2q 链短区间 B11 允许点上界。

用法示例：
    python3 experiments/short_interval_unit_deviation.py --nmax 200
"""
import argparse
import math

M0 = 3 * 5 * 7 * 11
PHI = 480
SMALL = (3, 5, 7, 11)


def unit_pattern():
    return [all(x % p for p in SMALL) for x in range(M0)]


def max_units_by_length(nmax):
    pattern = unit_pattern()
    doubled = pattern + pattern
    pref = [0]
    for v in doubled:
        pref.append(pref[-1] + int(v))
    out = []
    max_excess = 0.0
    max_excess_row = None
    for n in range(1, nmax + 1):
        full, rem = divmod(n, M0)
        base = full * PHI
        if rem == 0:
            mx = base
        else:
            mx = base + max(pref[i + rem] - pref[i] for i in range(M0))
        expected = PHI * n / M0
        excess = mx - expected
        if excess > max_excess:
            max_excess = excess
            max_excess_row = (n, mx, expected, excess)
        out.append((n, mx, expected, excess))
    return out, max_excess_row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nmax', type=int, default=300)
    parser.add_argument('--show', type=int, default=60)
    args = parser.parse_args()
    rows, maxrow = max_units_by_length(args.nmax)
    print('M0', M0, 'phi', PHI, 'density', PHI / M0, 'nmax', args.nmax)
    print('max_excess_row', maxrow, 'ceil_excess', math.ceil(maxrow[3]))
    print('n max_units expected excess')
    for n, mx, exp, exc in rows[:args.show]:
        print(n, mx, f'{exp:.6f}', f'{exc:.6f}')
    print('tail_samples')
    for n, mx, exp, exc in rows[max(0, len(rows)-20):]:
        print(n, mx, f'{exp:.6f}', f'{exc:.6f}')


if __name__ == '__main__':
    main()
