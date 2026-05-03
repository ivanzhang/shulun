#!/usr/bin/env python3
"""粗共享簇的奇异级数权重扫描。

对同一粗素数 q 命中的簇 {0,t1 q,t2 q,...}，计算小筛权重
  W/prod pB^r
按簇大小 r 与 t 模式统计。用于判断高阶簇是否被小素数阻断。

用法示例：
  python3 experiments/shared_cluster_singular_weight.py --Ps 503,1009,2003 --C 6 --max-r 5
"""
import argparse
import itertools
import math
from collections import defaultdict

from high_threshold_margin_fast import sieve, primes


def singular_weight(offsets, small):
    weight = 1.0
    for p in small:
        residues = {h % p for h in offsets}
        if len(residues) >= p:
            return 0.0
        weight *= (1 - len(residues) / p)
    return weight


def parity_pattern(ts):
    vals = [0] + [t % 2 for t in ts]
    return 'parity_ok' if len(set(vals)) == 1 else 'parity_blocked'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=6.0)
    ap.add_argument('--max-r', type=int, default=5)
    args = ap.parse_args()
    print('P C L r pattern count meanRatio minRatio maxRatio zeroRate')
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
            ts_all = list(range(1, max_t + 1))
            for r in range(2, min(args.max_r, len(ts_all) + 1) + 1):
                for ts in itertools.combinations(ts_all, r - 1):
                    offsets = [0] + [t * q for t in ts]
                    ratio = singular_weight(offsets, small) / (pB ** r)
                    stats[(r, parity_pattern(ts))].append(ratio)
        for key in sorted(stats):
            vals = stats[key]
            zeros = sum(1 for x in vals if x == 0.0)
            r, pattern = key
            print(P, args.C, L, r, pattern, len(vals), f'{sum(vals)/len(vals):.6f}', f'{min(vals):.6f}', f'{max(vals):.6f}', f'{zeros/len(vals):.3f}')


if __name__ == '__main__':
    main()
