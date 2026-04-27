#!/usr/bin/env python3
"""二补丁/多补丁洞的结构扫描。

对死亡最晚的长尾样本，列出 |Q_i|>=2 的洞，分析：
- 多补丁洞比例；
- 补丁因子对乘积 q1*q2 的大小；
- 多补丁洞之间是否共享补丁；
- 多补丁洞在 B11 洞序列中的间距。

用法示例：
  python3 experiments/multipatch_hole_structure.py --P 256019 --K 35 --y 11 --top 3
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回 n 的有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def collect_records(P, A, y, K):
    """收集死亡最晚路径。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, ()) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            next_states = []
            for a, path in states:
                patches = patch_set(a + r * P, y, P)
                if patches:
                    next_states.append((a, path + (min(patches),)))
                elif path:
                    records.append((idx, a, path, group['holes'][:idx], group['pattern']))
            states = next_states
        for a, path in states:
            if path:
                records.append((K + 1, a, path, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def analyze(P, y, death, a, holes):
    """分析一个记录中的多补丁洞。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    rows = []
    for idx, r in enumerate(prefix, start=1):
        n = a + r * P
        qs = patch_set(n, y, P)
        rows.append((idx, r, n, qs))
    multi = [(idx, r, n, qs) for idx, r, n, qs in rows if len(qs) >= 2]

    q_to_positions = defaultdict(list)
    for idx, r, n, qs in rows:
        for q in qs:
            q_to_positions[q].append((idx, r))
    shared_q = {q: pos for q, pos in q_to_positions.items() if len(pos) >= 2}

    gaps = [multi[i][1] - multi[i - 1][1] for i in range(1, len(multi))]
    index_gaps = [multi[i][0] - multi[i - 1][0] for i in range(1, len(multi))]
    pair_products = []
    for idx, r, n, qs in multi:
        sorted_qs = sorted(qs)
        pair_products.append((idx, r, sorted_qs[0] * sorted_qs[1], sorted_qs[0], sorted_qs[1], n))

    return rows, multi, shared_q, gaps, index_gaps, pair_products


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, required=True)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--top', type=int, default=3)
    args = parser.parse_args()

    for rank, rec in enumerate(collect_records(args.P, args.A, args.y, args.K)[:args.top], start=1):
        death, a, path, holes, pattern = rec
        rows, multi, shared_q, gaps, index_gaps, pair_products = analyze(args.P, args.y, death, a, holes)
        T = len(rows)
        unique = sum(1 for _, _, _, qs in rows if len(qs) == 1)
        option_hist = Counter(len(qs) for _, _, _, qs in rows)
        print('record', rank, 'P', args.P, 'a', a, 'death', death, 'T', T, 'pattern', pattern)
        print('summary unique', unique, 'multi', len(multi), 'multi_ratio', f'{len(multi)/T if T else 0:.3f}', 'option_hist', sorted(option_hist.items()))
        print('multi_index_r_patches_pairprod')
        for idx, r, n, qs in multi:
            sq = sorted(qs)
            print(idx, r, qs, 'pairprod', sq[0] * sq[1], 'n_over_pair', n // (sq[0] * sq[1]))
        print('multi_r_gaps', gaps)
        print('multi_index_gaps', index_gaps)
        print('shared_q')
        for q, pos in sorted(shared_q.items()):
            print(q, pos, 'r_diffs', [pos[i][1] - pos[0][1] for i in range(1, len(pos))])
        print('pairprod_stats min max avg')
        if pair_products:
            vals = [x[2] for x in pair_products]
            print(min(vals), max(vals), f'{sum(vals)/len(vals):.1f}')
        else:
            print('-')
        print('---')


if __name__ == '__main__':
    main()
