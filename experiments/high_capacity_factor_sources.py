#!/usr/bin/env python3
"""高容量斜率的差分因子来源扫描。

若 cap_H(q)>=j，则存在 j+1 个洞同余 mod q；因此 q 整除这些洞相对某一点的所有差值，
也即 q 整除该簇差值的 gcd。本脚本列出全局最坏高容量簇及其差分 gcd。

用法示例：
    python3 experiments/high_capacity_factor_sources.py --T 40 --min-cap 3 --show 30
"""
import argparse
import math
from collections import defaultdict, Counter
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c
from fixed_anchor_sieve_remainder import primes_upto

Y = 11


def clusters_for_holes(holes):
    """返回所有 q 的最大簇信息。"""
    D = max(holes) - min(holes)
    out = []
    for q in [p for p in primes_upto(D) if p > Y]:
        by = defaultdict(list)
        for r in holes:
            by[r % q].append(r)
        for residue, rs in by.items():
            if len(rs) >= 2:
                diffs = [x - rs[0] for x in rs[1:]]
                g = 0
                for d in diffs:
                    g = math.gcd(g, d)
                out.append((q, len(rs) - 1, residue, tuple(rs), g))
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=40)
    parser.add_argument('--min-cap', type=int, default=3)
    parser.add_argument('--show', type=int, default=30)
    args = parser.parse_args()

    records = []
    q_counter = Counter()
    gcd_counter = Counter()
    for c in range(M):
        holes = holes_for_c(c, args.T)
        for q, cap, residue, rs, g in clusters_for_holes(holes):
            if cap >= args.min_cap:
                records.append((cap, q, c, residue, rs, g))
                q_counter[q] += 1
                gcd_counter[g] += 1
    records.sort(key=lambda x: (-x[0], x[1], x[2]))
    print('T', args.T, 'min_cap', args.min_cap, 'records', len(records))
    print('q_counter', q_counter.most_common(30))
    print('gcd_counter', gcd_counter.most_common(30))
    print('rank cap q c residue rs gcd gcd/q')
    for i, (cap, q, c, residue, rs, g) in enumerate(records[:args.show], 1):
        print(i, cap, q, c, residue, rs, g, g // q if q else None)


if __name__ == '__main__':
    main()
