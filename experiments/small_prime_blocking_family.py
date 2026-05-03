#!/usr/bin/env python3
"""小素数阻断族实验：粗共享差分模式的奇异级数权重。

对二点共享模式 H={0,d}, d=tq，q in (sqrt(P), L]，统计
  W(H)=prod_{p<=B}(1-nu_p(H)/p)
并与独立基准 pB^2 比较。
同时给出按 t 奇偶、q 层的权重压缩比例。

用法示例：
  python3 experiments/small_prime_blocking_family.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import sieve, primes


def q_bucket(q, B):
    ratio = q / B
    if ratio <= 1.5:
        return '(1,1.5]B'
    if ratio <= 2.0:
        return '(1.5,2]B'
    if ratio <= 3.0:
        return '(2,3]B'
    return '(3,C]B'


def singular_weight(offsets, small):
    weight = 1.0
    for p in small:
        residues = {h % p for h in offsets}
        if len(residues) >= p:
            return 0.0
        weight *= (1 - len(residues) / p)
    return weight


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L pB group count meanRatio minRatio maxRatio zeroRate')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        small = primes(sieve(B), B)
        large_qs = [q for q in primes(sieve(L), L) if q > B]
        pB = 1.0
        for p in small:
            pB *= (1 - 1 / p)
        stats = defaultdict(list)
        for q in large_qs:
            max_t = (L - 1) // q
            for t in range(1, max_t + 1):
                d = t * q
                ratio = singular_weight([0, d], small) / (pB * pB)
                group = f'{q_bucket(q, B)}|t_{"odd" if t % 2 else "even"}'
                stats[group].append(ratio)
        for group in sorted(stats):
            vals = stats[group]
            zeros = sum(1 for x in vals if x == 0.0)
            print(
                P,
                args.C,
                L,
                f'{pB:.6f}',
                group,
                len(vals),
                f'{sum(vals)/len(vals):.6f}',
                f'{min(vals):.6f}',
                f'{max(vals):.6f}',
                f'{zeros/len(vals):.3f}',
            )


if __name__ == '__main__':
    main()
