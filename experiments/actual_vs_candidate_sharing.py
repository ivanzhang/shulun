#!/usr/bin/env python3
"""候选差分共享边 vs 实际共享边。

纯 B11 高度差会产生很多候选共享边，但实际共享还要求 q 出现在两个 n=a+rP 的补丁集合中。
本脚本在局部窗口中同时计算候选边最大匹配与实际共享节省，量化二者差距。

用法示例：
  python3 experiments/actual_vs_candidate_sharing.py --Ps 128021,256019 --K 35 --y 11 --W 15 --top-records 20 --show 12
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def gt_y_prime_factors(n, y):
    """返回 n 的大于 y 的不同素因子。"""
    out = []
    x = n
    for p in primes_upto(math.isqrt(x) + 1):
        if p * p > x:
            break
        if x % p == 0:
            if p > y:
                out.append(p)
            while x % p == 0:
                x //= p
    if x > 1 and x > y:
        out.append(x)
    return out


def max_matching_size(n, edges):
    """小图最大匹配。"""
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    from functools import lru_cache
    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 0
        i = (mask & -mask).bit_length() - 1
        best = dp(mask & ~(1 << i))
        rest = mask & ~(1 << i)
        for j in adj[i]:
            if rest & (1 << j):
                best = max(best, 1 + dp(rest & ~(1 << j)))
        return best
    return dp((1 << n) - 1)


def collect_records(P, A, y, K):
    """收集死亡最晚记录。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, 0) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, length in states:
                qs = patch_set(a + r * P, y, P)
                if qs:
                    nxt.append((a, length + 1))
                elif length:
                    records.append((idx, a, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, length in states:
            if length:
                records.append((K + 1, a, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def window_stats(P, y, a, window):
    """计算候选与实际共享。"""
    rs = [r for _, r in window]
    sets = [set(patch_set(a + r * P, y, P)) for r in rs]
    candidate_edges = []
    actual_edges = []
    actual_labels = []
    for i in range(len(rs)):
        for j in range(i + 1, len(rs)):
            cand_qs = gt_y_prime_factors(abs(rs[j] - rs[i]), y)
            if cand_qs:
                candidate_edges.append((i, j))
            common = sets[i] & sets[j]
            if common:
                actual_edges.append((i, j))
                actual_labels.append((i, j, rs[j] - rs[i], tuple(sorted(common))))
    incidence = sum(len(s) for s in sets)
    distinct = len(set().union(*sets)) if sets else 0
    return {
        'candidate_edges': candidate_edges,
        'candidate_matching': max_matching_size(len(rs), candidate_edges),
        'actual_edges': actual_edges,
        'actual_matching': max_matching_size(len(rs), actual_edges),
        'actual_labels': actual_labels,
        'raw_repeats': incidence - distinct,
        'incidence': incidence,
        'distinct': distinct,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=20)
    parser.add_argument('--show', type=int, default=12)
    args = parser.parse_args()

    rows = []
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            if len(prefix) < args.W:
                continue
            indexed = list(enumerate(prefix, start=1))
            for start in range(len(indexed) - args.W + 1):
                window = indexed[start:start + args.W]
                st = window_stats(P, args.y, a, window)
                rows.append((st['raw_repeats'], st['actual_matching'], st['candidate_matching'], len(st['candidate_edges']), len(st['actual_edges']), P, a, (window[0][0], window[-1][0]), (window[0][1], window[-1][1]), st, pattern))
    rows.sort(reverse=True)
    print('rows', len(rows))
    print('rank raw_repeats actual_matching candidate_matching candidate_edges actual_edges P a idx r actual_labels pattern')
    for rank, row in enumerate(rows[:args.show], start=1):
        raw, am, cm, ce, ae, P, a, idx_range, r_range, st, pattern = row
        print(rank, raw, am, cm, ce, ae, P, a, idx_range, r_range, st['actual_labels'], pattern)


if __name__ == '__main__':
    main()
