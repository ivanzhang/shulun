#!/usr/bin/env python3
"""路线 A：扫描 min_a |H_c(P,a)| - 2(π(P)-π(cP))。

若该余量 > 0，则由 q>cP>P/2 每个 q 最多命中两个 r，推出列 a 有素数。

用法：
  python3 experiments/high_threshold_margin_scan.py --Ps 251,503,1009,2003 --cs 0.72,0.75,0.8,0.85,0.9
"""
import argparse
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def scan(P, c):
    y = int(c * P)
    flags = sieve(P * P)
    root = primes_from_flags(flags, P)
    pi_tail = sum(1 for q in root if y < q < P)
    tail_bound = 2 * pi_tail
    min_rec = None
    for a in range(1, P):
        rec = record_for(P, a, y, flags, root)
        margin = rec['holes'] - tail_bound
        key = (margin, rec['holes'], rec['prime_holes'], a)
        if min_rec is None or key < min_rec[0]:
            min_rec = (key, rec)
    (margin, H, prime, a), rec = min_rec
    return {
        'P': P, 'c': c, 'y': y, 'pi_tail': pi_tail, 'tail_bound': tail_bound,
        'min_margin': margin, 'a': a, 'H': H, 'prime': prime, 'comp': rec['composite_holes'],
        'ratio': H / tail_bound if tail_bound else float('inf'),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='251,503,1009,2003')
    parser.add_argument('--cs', default='0.72,0.75,0.8,0.85,0.9')
    args = parser.parse_args()
    print('P c y piTail 2piTail minMargin ratio minA H prime comp')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for c in [float(x) for x in args.cs.split(',') if x.strip()]:
            rec = scan(P, c)
            print(f"{rec['P']} {rec['c']:.3f} {rec['y']} {rec['pi_tail']} {rec['tail_bound']} {rec['min_margin']} {rec['ratio']:.3f} {rec['a']} {rec['H']} {rec['prime']} {rec['comp']}")

if __name__ == '__main__':
    main()
