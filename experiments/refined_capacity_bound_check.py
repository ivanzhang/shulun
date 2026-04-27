#!/usr/bin/env python3
"""使用 480/1155 + E=5 的短区间容量界对照实际 cap。"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c
from slope_capacity_lift_bound import capacity_profile
from fixed_anchor_sieve_remainder import primes_upto

RHO_NUM = 480
RHO_DEN = 1155
E = 5
Y = 11


def refined_cap_bound(D, q):
    U = D // (2 * q)
    # 链 t 长度为 U+1，允许点 <= rho*(U+1)+E，cap=点数-1。
    return max(0, math.floor((RHO_NUM * (U + 1)) / RHO_DEN + E) - 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=40)
    args = parser.parse_args()
    violations = []
    total_gap = 0
    max_gap = 0
    checked = 0
    for c in range(M):
        holes = holes_for_c(c, args.T)
        D = max(holes) - min(holes)
        actual = dict(capacity_profile(holes))
        for q in [p for p in primes_upto(D) if p > Y]:
            a = actual.get(q, 0)
            b = refined_cap_bound(D, q)
            checked += 1
            if a > b:
                violations.append((c, q, D, a, b, holes))
            gap = b - a
            total_gap += gap
            max_gap = max(max_gap, gap)
    print('T', args.T, 'checked', checked, 'violations', len(violations), 'max_gap', max_gap, 'avg_gap', total_gap / checked if checked else 0)
    print('first_violations', violations[:5])


if __name__ == '__main__':
    main()
