#!/usr/bin/env python3
"""二阶能量按补丁对乘积分桶。

目标：观察 E2=sum C(|Q_i|,2) 的贡献来自哪些 qs 尺度，尤其小乘积
qs 是否足以解释大部分二阶交会。输出长尾样本中每个补丁对的 qs、所在洞高，
并按 dyadic bucket 汇总。

用法示例：
  python3 experiments/two_patch_energy_buckets.py --P 256019 --K 35 --y 11 --top 3
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回 n 的有效补丁素数。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def collect_records(P, A, y, K):
    """收集死亡最晚路径。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, ()) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, path in states:
                qs = patch_set(a + r * P, y, P)
                if qs:
                    nxt.append((a, path + (min(qs),)))
                elif path:
                    records.append((idx, a, path, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, path in states:
            if path:
                records.append((K + 1, a, path, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def bucket_label(value):
    """二进制尺度分桶。"""
    lo = 1 << (value.bit_length() - 1)
    hi = (lo << 1) - 1
    return f'{lo}-{hi}'


def analyze(P, y, death, a, holes):
    """返回补丁对列表与分桶统计。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    pairs = []
    for idx, r in enumerate(prefix, start=1):
        n = a + r * P
        qs = sorted(patch_set(n, y, P))
        for i, q in enumerate(qs):
            for s in qs[i + 1:]:
                pairs.append({'idx': idx, 'r': r, 'q': q, 's': s, 'prod': q * s, 'n': n, 'cofactor': n // (q * s)})
    buckets = Counter(bucket_label(x['prod']) for x in pairs)
    small_thresholds = [500, 1000, 2000, 5000, 10000, 50000, 100000]
    cumul = {thr: sum(1 for x in pairs if x['prod'] <= thr) for thr in small_thresholds}
    return prefix, pairs, buckets, cumul


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, required=True)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--top', type=int, default=3)
    parser.add_argument('--show-pairs', type=int, default=30)
    args = parser.parse_args()

    for rank, rec in enumerate(collect_records(args.P, args.A, args.y, args.K)[:args.top], start=1):
        death, a, path, holes, pattern = rec
        prefix, pairs, buckets, cumul = analyze(args.P, args.y, death, a, holes)
        T = len(prefix)
        print('record', rank, 'P', args.P, 'a', a, 'death', death, 'T', T, 'E2', len(pairs), 'E2_ratio', f'{len(pairs)/T if T else 0:.3f}', 'pattern', pattern)
        print('buckets', sorted(buckets.items(), key=lambda kv: int(kv[0].split('-')[0])))
        print('cumulative', sorted(cumul.items()))
        print('pairs idx r q s prod cofactor')
        for item in sorted(pairs, key=lambda x: x['prod'])[:args.show_pairs]:
            print(item['idx'], item['r'], item['q'], item['s'], item['prod'], item['cofactor'])
        print('---')


if __name__ == '__main__':
    main()
