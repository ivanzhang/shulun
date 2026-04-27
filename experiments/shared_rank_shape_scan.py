#!/usr/bin/env python3
"""共享秩形状分类扫描。

对实际窗口统计共享簇大小 multiset，如 [2,2,2] 表示三个补丁各命中两点，R=3；
并对纯差分容量窗口统计候选簇大小，找 R>=4 的抽象形状。

用法示例：
  python3 experiments/shared_rank_shape_scan.py --Ps 32003,64007,128021,256019 --K 35 --W 15 --top-records 20
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups

Y = 11
M = 2310


def patch_set(n, P):
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > Y and q <= root and q != P)


def collect_records(P, A, y, K):
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, 0) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, length in states:
                qs = patch_set(a + r * P, P)
                if qs:
                    nxt.append((a, length + 1))
                elif length:
                    records.append((idx, a, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, length in states:
            if length:
                records.append((K + 1, a, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def actual_shape(P, a, window):
    q_to_rs = defaultdict(list)
    for _, r in window:
        for q in patch_set(a + r * P, P):
            q_to_rs[q].append(r)
    clusters = sorted((len(v) for v in q_to_rs.values() if len(v) >= 2), reverse=True)
    R = sum(x - 1 for x in clusters)
    return R, tuple(clusters), {q: v for q, v in q_to_rs.items() if len(v) >= 2}


def holes_for_c(c, W):
    holes = []
    r = 1
    while len(holes) < W:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def candidate_shape(holes):
    # 对每个 q，取最大 residue class 作为候选簇大小。
    span = holes[-1] - holes[0]
    qs = set()
    primes = primes_upto(span + 1)
    for i, r in enumerate(holes):
        for s in holes[i + 1:]:
            d = s - r
            x = d
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    if p > Y:
                        qs.add(p)
                    while x % p == 0:
                        x //= p
            if x > 1 and x > Y:
                qs.add(x)
    clusters = []
    detail = {}
    for q in sorted(qs):
        by = defaultdict(list)
        for r in holes:
            by[r % q].append(r)
        vals = sorted(by.values(), key=len, reverse=True)
        if vals and len(vals[0]) >= 2:
            clusters.append(len(vals[0]))
            detail[q] = vals[0]
    clusters.sort(reverse=True)
    R = sum(x - 1 for x in clusters)
    return R, tuple(clusters), detail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=20)
    parser.add_argument('--show', type=int, default=10)
    args = parser.parse_args()

    actual_hist = Counter()
    actual_records = []
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            if len(prefix) < args.W:
                continue
            indexed = list(enumerate(prefix, start=1))
            for start in range(len(indexed) - args.W + 1):
                window = indexed[start:start + args.W]
                R, shape, detail = actual_shape(P, a, window)
                actual_hist[(R, shape)] += 1
                actual_records.append((R, shape, P, a, (window[0][0], window[-1][0]), (window[0][1], window[-1][1]), detail, pattern))

    cand_hist = Counter()
    cand_records = []
    for c in range(M):
        holes = holes_for_c(c, args.W)
        R, shape, detail = candidate_shape(holes)
        cand_hist[(R, shape)] += 1
        cand_records.append((R, shape, c, holes, detail))

    print('actual_shape_hist')
    for key, count in sorted(actual_hist.items()):
        print(key, count)
    print('actual_top')
    for rec in sorted(actual_records, reverse=True)[:args.show]:
        print(rec)
    print('candidate_shape_hist_top')
    for key, count in sorted(cand_hist.items(), key=lambda kv: (-kv[0][0], kv[0][1]))[:20]:
        print(key, count)
    print('candidate_top')
    for rec in sorted(cand_records, reverse=True)[:args.show]:
        print(rec)


if __name__ == '__main__':
    main()
