#!/usr/bin/env python3
"""候选共享边的锚点同余容量扫描。

对长尾样本的连续 W 窗口：
- 由高度差生成候选边 (i,j,q), q | r_j-r_i；
- 每条候选边要求 a ≡ -r_i P (mod q)；
- 统计固定锚点 a 实际满足多少候选边同余类；
- 与真实补丁共享边比较。

用法示例：
  python3 experiments/anchor_congruence_capacity.py --Ps 128021,256019 --K 35 --y 11 --W 15 --top-records 20 --show 12
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

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
    """统计窗口中候选边、锚点满足边、真实共享边。"""
    rs = [r for _, r in window]
    sets = [set(patch_set(a + r * P, y, P)) for r in rs]
    candidate = []
    anchor_hit = []
    actual = []
    by_q = Counter()
    anchor_by_q = Counter()
    for i in range(len(rs)):
        for j in range(i + 1, len(rs)):
            for q in gt_y_prime_factors(rs[j] - rs[i], y):
                required = (-rs[i] * P) % q
                hit = (a - required) % q == 0
                is_actual = q in sets[i] and q in sets[j]
                item = (i, j, rs[j] - rs[i], q, required)
                candidate.append(item)
                by_q[q] += 1
                if hit:
                    anchor_hit.append(item)
                    anchor_by_q[q] += 1
                if is_actual:
                    actual.append(item)
    incidence = sum(len(s) for s in sets)
    distinct = len(set().union(*sets)) if sets else 0
    return {
        'candidate': candidate,
        'anchor_hit': anchor_hit,
        'actual': actual,
        'raw_repeats': incidence - distinct,
        'by_q': by_q,
        'anchor_by_q': anchor_by_q,
        'sets': sets,
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
                rows.append((len(st['anchor_hit']), len(st['actual']), st['raw_repeats'], len(st['candidate']), P, a, (window[0][0], window[-1][0]), (window[0][1], window[-1][1]), st, pattern))
    rows.sort(reverse=True)
    print('rows', len(rows))
    print('rank anchor_hits actual_edges raw_repeats candidate_edges P a idx r anchor_by_q actual_items anchor_hit_items pattern')
    for rank, row in enumerate(rows[:args.show], start=1):
        anchor_hits, actual_edges, raw_repeats, candidate_edges, P, a, idx_range, r_range, st, pattern = row
        print(rank, anchor_hits, actual_edges, raw_repeats, candidate_edges, P, a, idx_range, r_range, sorted(st['anchor_by_q'].items()), st['actual'], st['anchor_hit'], pattern)


if __name__ == '__main__':
    main()
