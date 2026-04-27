#!/usr/bin/env python3
"""验证零洞修复边界 R 的显式公式。

用法示例：
  python3 experiments/boundary_formula_check.py --P 997 --y 7
"""
import argparse
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import sieve
from zero_repair_boundary_scan import boundary_events


def boundary_R_formula(P, a):
    """对 1<a<P，边界 R 满足 floor(sqrt(a+(R-2)P))<a<=floor(sqrt(a+(R-1)P))。"""
    return (a * (a - 1)) // P + 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=997)
    parser.add_argument('--y', type=int, default=7)
    args = parser.parse_args()

    flags = sieve(args.P)
    formula = {(a, boundary_R_formula(args.P, a)) for a in range(1, args.P) if flags[a] and a > args.y}
    events = {(x['a'], x['R']) for x in boundary_events(args.P, args.y, args.P)}
    missing = sorted(formula - events)[:10]
    extra = sorted(events - formula)[:10]
    print('P', args.P, 'formula_count', len(formula), 'event_count', len(events), 'missing', len(formula - events), 'extra', len(events - formula))
    print('missing_sample', missing)
    print('extra_sample', extra)
    print('first10', sorted(formula)[:10])
    print('last10', sorted(formula)[-10:])


if __name__ == '__main__':
    main()
