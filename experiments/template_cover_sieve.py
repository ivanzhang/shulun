#!/usr/bin/env python3
"""固定前洞模板的补丁剩余类覆盖筛。

用法示例：
  python3 experiments/template_cover_sieve.py --P 4001 --K 15 --top 10
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

sys.path.append('experiments')
from demand_side_bad_prefix import prime_anchors, prefix_profile
from fixed_anchor_sieve_remainder import primes_upto
from pattern_bad_prefix import pattern_id
from shared_patch_energy import front_holes


def template_groups(P, A, y, K):
    """按模式分组，并记录每组前 K 洞模板。"""
    groups = defaultdict(list)
    for a in prime_anchors(P, A):
        groups[pattern_id(P, a, y)].append(a)
    out = []
    for pat, anchors in groups.items():
        holes = tuple(front_holes(P, anchors[0], y, K))
        out.append({'pattern': pat, 'anchors': anchors, 'holes': holes})
    return out


def covered_by_patch(P, a, r, y):
    """判断 L=a+rP 是否被允许补丁素数覆盖。"""
    n = a + r * P
    Q = math.isqrt(n)
    return any(n % q == 0 for q in primes_upto(Q) if q > y and q != P)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=4001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=15)
    parser.add_argument('--top', type=int, default=10)
    args = parser.parse_args()

    groups = template_groups(args.P, args.A, args.y, args.K)
    records = []
    for group in groups:
        anchors = group['anchors']
        holes = group['holes']
        survivors = set(anchors)
        step = []
        for idx, r in enumerate(holes, start=1):
            before = len(survivors)
            # 在该洞为合数/被补丁覆盖者继续幸存；若是素数洞则死亡。
            survivors = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}
            after = len(survivors)
            step.append((idx, r, before, after, after / before if before else 0.0))
        records.append({'pattern': group['pattern'], 'size': len(anchors), 'holes': holes, 'survivors': len(survivors), 'step': step})

    print('P', args.P, 'groups', len(groups), 'K', args.K)
    print('worst_templates survivors size pattern holes')
    for rec in sorted(records, key=lambda x: (-x['survivors'], -x['size']))[:args.top]:
        print('template', rec['survivors'], rec['size'], rec['pattern'], rec['holes'])
        print('  step', rec['step'])
    aggregate = Counter()
    aggregate_before = Counter()
    for rec in records:
        for idx, r, before, after, rate in rec['step']:
            aggregate[idx] += after
            aggregate_before[idx] += before
    print('aggregate_step idx before after rate')
    for idx in range(1, args.K + 1):
        before = aggregate_before[idx]
        after = aggregate[idx]
        print(idx, before, after, f'{after / before if before else 0:.4f}')


if __name__ == '__main__':
    main()
