#!/usr/bin/env python3
"""固定模板单步补丁事件的包含-排除重叠统计。

用法示例：
  python3 experiments/patch_overlap_inclusion.py --P 8009 --step 3 --top 8
"""
import argparse
import itertools
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def survivor_before_step(P, A, y, K, target_step):
    """返回每个模板在 target_step 前的幸存者和该步 r。"""
    rows = []
    for group in template_groups(P, A, y, K):
        survivors = set(group['anchors'])
        for idx, r in enumerate(group['holes'], start=1):
            if idx == target_step:
                rows.append((group['pattern'], r, survivors))
                break
            survivors = {a for a in survivors if covered_by_patch(P, a, r, y)}
    return rows


def event_primes_for_step(P, y, r, survivors):
    """该步可能出现的补丁素数集合。"""
    if not survivors:
        return []
    Q = max(math.isqrt(a + r * P) for a in survivors)
    return [q for q in primes_upto(Q) if q > y and q != P]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=8009)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--step', type=int, default=3)
    parser.add_argument('--top', type=int, default=8)
    args = parser.parse_args()

    rows = survivor_before_step(args.P, args.A, args.y, args.K, args.step)
    total_before = 0
    total_union = 0
    total_s1 = 0
    total_s2 = 0
    total_s3_sample = 0
    worst = []
    for pat, r, survivors in rows:
        n = len(survivors)
        if n == 0:
            continue
        total_before += n
        qs = event_primes_for_step(args.P, args.y, r, survivors)
        q_hits = Counter()
        pair_hits = Counter()
        triple_hits = 0
        union_count = 0
        for a in survivors:
            hit_qs = [q for q in qs if (a + r * args.P) % q == 0]
            if hit_qs:
                union_count += 1
            for q in hit_qs:
                q_hits[q] += 1
            for pair in itertools.combinations(hit_qs, 2):
                pair_hits[pair] += 1
            triple_hits += math.comb(len(hit_qs), 3) if len(hit_qs) >= 3 else 0
        s1 = sum(q_hits.values())
        s2 = sum(pair_hits.values())
        s3 = triple_hits
        ie2 = s1 - s2
        ie3 = s1 - s2 + s3
        total_union += union_count
        total_s1 += s1
        total_s2 += s2
        total_s3_sample += s3
        worst.append((abs(union_count - ie2), n, union_count, s1, s2, s3, pat, r, q_hits.most_common(5)))

    print('P', args.P, 'step', args.step, 'before', total_before, 'union', total_union, 'keep_rate', f'{total_union/total_before if total_before else 0:.4f}')
    print('S1', total_s1, 'S2', total_s2, 'S3', total_s3_sample, 'IE2', total_s1-total_s2, 'IE3', total_s1-total_s2+total_s3_sample)
    print('ratios S1/N S2/N S3/N union/S1')
    print(f'{total_s1/total_before:.4f}', f'{total_s2/total_before:.4f}', f'{total_s3_sample/total_before:.4f}', f'{total_union/total_s1 if total_s1 else 0:.4f}')
    print('worst_templates abs_err_ie2 size union s1 s2 s3 pat r top_hits')
    for rec in sorted(worst, reverse=True)[:args.top]:
        print('worst', rec)


if __name__ == '__main__':
    main()
