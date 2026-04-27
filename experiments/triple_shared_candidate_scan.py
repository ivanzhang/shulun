#!/usr/bin/env python3
"""三点共享簇候选与实际实现扫描。

纯差分中若某 q>11 的同余类在 15 洞窗口中出现至少 3 个洞，则是三点共享候选。
本脚本统计：
1. B11 模板中三点候选的形状；
2. 实际长尾窗口中是否有同一补丁 q 命中三个洞；
3. 若没有，输出最接近的候选与实际命中情况。

用法示例：
  python3 experiments/triple_shared_candidate_scan.py --Ps 32003,64007,128021,256019 --K 35 --W 15 --top-records 20
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


def holes_for_c(c, W):
    holes = []
    r = 1
    while len(holes) < W:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def candidate_triples(holes):
    span = holes[-1] - holes[0]
    out = []
    for q in primes_upto(span + 1):
        if q <= Y:
            continue
        by = defaultdict(list)
        for r in holes:
            by[r % q].append(r)
        for residue, rs in by.items():
            if len(rs) >= 3:
                out.append((q, residue, tuple(rs)))
    return out


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


def actual_triples(P, a, window):
    q_to_rs = defaultdict(list)
    for _, r in window:
        for q in patch_set(a + r * P, P):
            q_to_rs[q].append(r)
    return {q: rs for q, rs in q_to_rs.items() if len(rs) >= 3}


def candidate_actual_hits(P, a, holes):
    triples = candidate_triples(holes)
    rows = []
    for q, residue, rs in triples:
        hit_rs = [r for r in rs if q in patch_set(a + r * P, P)]
        rows.append((len(hit_rs), q, residue, rs, tuple(hit_rs)))
    return sorted(rows, reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=20)
    parser.add_argument('--show', type=int, default=12)
    args = parser.parse_args()

    cand_hist = Counter()
    cand_examples = []
    for c in range(M):
        holes = holes_for_c(c, args.W)
        triples = candidate_triples(holes)
        cand_hist[len(triples)] += 1
        if triples:
            cand_examples.append((len(triples), c, holes, triples))
    cand_examples.sort(reverse=True)

    actual_count = 0
    near = []
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for death, a, holes, pattern in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            prefix = holes[:death - 1] if death <= len(holes) else holes
            if len(prefix) < args.W:
                continue
            indexed = list(enumerate(prefix, start=1))
            for start in range(len(indexed) - args.W + 1):
                window = indexed[start:start + args.W]
                win_holes = [r for _, r in window]
                triples = actual_triples(P, a, window)
                if triples:
                    actual_count += 1
                hits = candidate_actual_hits(P, a, win_holes)
                if hits:
                    near.append((hits[0][0], P, a, (window[0][0], window[-1][0]), (window[0][1], window[-1][1]), hits[:3], triples, pattern))
    near.sort(reverse=True)

    print('candidate_triple_count_hist', sorted(cand_hist.items()))
    print('candidate_examples')
    for rec in cand_examples[:args.show]:
        print(rec)
    print('actual_triple_windows', actual_count)
    print('nearest_actual_hits')
    for rec in near[:args.show]:
        print(rec)


if __name__ == '__main__':
    main()
