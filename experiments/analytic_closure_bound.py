#!/usr/bin/env python3
"""解析闭合界：D,S -> m -> Lmin -> anchor expectation。

使用模1155单位集合短区间精确最大函数 U(n)：
cap(q) <= U(floor(D/(2q))+1)-1。
这比 rho*n+E 的粗界更紧，仍不依赖 B11 模板枚举。
"""
import argparse
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from slope_capacity_lift_bound import first_available_product, anchor_expectation_bound

Y = 11
M0 = 3 * 5 * 7 * 11
SMALL = (3, 5, 7, 11)

_UNIT_MAX_CACHE = {}


def unit_pattern():
    return [all(x % p for p in SMALL) for x in range(M0)]


def max_units(n):
    """模1155任意连续 n 个位置最多单位数。"""
    if n in _UNIT_MAX_CACHE:
        return _UNIT_MAX_CACHE[n]
    pattern = unit_pattern()
    total = sum(pattern)
    full, rem = divmod(n, M0)
    base = full * total
    if rem == 0:
        _UNIT_MAX_CACHE[n] = base
        return base
    doubled = pattern + pattern
    pref = [0]
    for value in doubled:
        pref.append(pref[-1] + int(value))
    result = base + max(pref[i + rem] - pref[i] for i in range(M0))
    _UNIT_MAX_CACHE[n] = result
    return result


def cap_bound(D, q):
    n = D // (2 * q) + 1
    return max(0, max_units(n) - 1)


def analytic_m(D, S):
    qs = [p for p in primes_upto(max(13, D)) if p > Y]
    caps = [(q, cap_bound(D, q)) for q in qs]
    caps = [(q, c) for q, c in caps if c > 0]
    caps.sort(key=lambda x: (-x[1], x[0]))
    total = 0
    used = []
    for q, c in caps:
        total += c
        used.append((q, c))
        if total >= S:
            return len(used), total, used, caps
    return None, total, used, caps


def run_case(D, S, X):
    m, total, used, caps = analytic_m(D, S)
    if m is None:
        return {'D': D, 'S': S, 'impossible': True, 'capacity': total, 'caps': caps[:20]}
    Lmin, min_qs = first_available_product(m)
    expect = anchor_expectation_bound(X, Lmin)
    return {
        'D': D,
        'S': S,
        'm': m,
        'capacity': total,
        'used_by_capacity': used,
        'Lmin': Lmin,
        'log10Lmin': math.log10(Lmin),
        'sqrtLmin': math.isqrt(Lmin),
        'min_qs': min_qs,
        'X': X,
        'anchor_expect': expect,
        'caps_top': caps[:20],
    }


def print_case(rec):
    if rec.get('impossible'):
        print('D', rec['D'], 'S', rec['S'], 'impossible capacity', rec['capacity'], 'caps_top', rec['caps'])
        return
    print('D', rec['D'], 'S', rec['S'], 'm', rec['m'], 'capacity', rec['capacity'])
    print('used_by_capacity', rec['used_by_capacity'])
    print('Lmin', rec['Lmin'], 'log10Lmin', f'{rec["log10Lmin"]:.3f}', 'sqrtLmin', rec['sqrtLmin'], 'min_qs', rec['min_qs'])
    print('X', rec['X'], 'anchor_expect', f'{rec["anchor_expect"]:.6g}')
    print('caps_top', rec['caps_top'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--D', type=int, default=150)
    parser.add_argument('--S', type=int, default=15)
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--cases', default='')
    args = parser.parse_args()

    if args.cases:
        print('D S m log10Lmin anchor_expect used_by_capacity')
        for item in args.cases.split(','):
            if not item.strip():
                continue
            D, S = [int(x) for x in item.split(':')]
            rec = run_case(D, S, args.X)
            if rec.get('impossible'):
                print(D, S, 'impossible', 'NA', 'NA', rec['caps'][:10])
            else:
                print(D, S, rec['m'], f'{rec["log10Lmin"]:.3f}', f'{rec["anchor_expect"]:.6g}', rec['used_by_capacity'], flush=True)
        return

    print_case(run_case(args.D, args.S, args.X))


if __name__ == '__main__':
    main()
