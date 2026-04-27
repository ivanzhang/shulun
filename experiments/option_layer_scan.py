#!/usr/bin/env python3
"""补丁选项层级 N_{>=k} 扫描。

对多个 P 的长尾样本，统计每个合数前缀中 |Q_i| 的层级比例：
N>=2, N>=3, N>=4，并记录最坏样本。这用于给“选项层级稀疏引理”找常数。

用法示例：
  python3 experiments/option_layer_scan.py --Ps 8009,16001,32003,64007,128021,256019 --K 35 --y 11 --top 20
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_count(n, y, P):
    """返回有效补丁素数数量。"""
    root = math.isqrt(n)
    return sum(1 for q, _ in factor(n) if q > y and q <= root and q != P)


def collect_records(P, A, y, K):
    """收集死亡路径；按死亡时间降序。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, 0) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, length in states:
                count = patch_count(a + r * P, y, P)
                if count:
                    nxt.append((a, length + 1))
                elif length:
                    records.append((idx, a, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, length in states:
            if length:
                records.append((K + 1, a, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def analyze(P, y, death, a, holes):
    """统计一个前缀的选项层级。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    counts = [patch_count(a + r * P, y, P) for r in prefix]
    T = len(counts)
    hist = Counter(counts)
    ge2 = sum(1 for c in counts if c >= 2)
    ge3 = sum(1 for c in counts if c >= 3)
    ge4 = sum(1 for c in counts if c >= 4)
    ge5 = sum(1 for c in counts if c >= 5)
    return {
        'T': T,
        'hist': hist,
        'ge2': ge2,
        'ge3': ge3,
        'ge4': ge4,
        'ge5': ge5,
        'max_options': max(counts) if counts else 0,
        'avg_options': sum(counts) / T if T else 0.0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='8009,16001,32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--top', type=int, default=20)
    args = parser.parse_args()

    worst = {'ge2': None, 'ge3': None, 'ge4': None, 'ge5': None, 'avg': None}
    print('P rank death a T ge2 ge2_ratio ge3 ge3_ratio ge4 ge4_ratio ge5 ge5_ratio avg_options max_options hist pattern')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        records = collect_records(P, args.A, args.y, args.K)[:args.top]
        for rank, rec in enumerate(records, start=1):
            death, a, holes, pattern = rec
            st = analyze(P, args.y, death, a, holes)
            T = st['T']
            ratios = {
                'ge2': st['ge2'] / T if T else 0,
                'ge3': st['ge3'] / T if T else 0,
                'ge4': st['ge4'] / T if T else 0,
                'ge5': st['ge5'] / T if T else 0,
                'avg': st['avg_options'],
            }
            for key, value in ratios.items():
                if worst[key] is None or value > worst[key][0]:
                    worst[key] = (value, P, rank, death, a, T, st['hist'], pattern)
            print(
                P, rank, death, a, T,
                st['ge2'], f'{ratios["ge2"]:.3f}',
                st['ge3'], f'{ratios["ge3"]:.3f}',
                st['ge4'], f'{ratios["ge4"]:.3f}',
                st['ge5'], f'{ratios["ge5"]:.3f}',
                f'{st["avg_options"]:.3f}', st['max_options'], sorted(st['hist'].items()), pattern,
            )
    print('worst_summary key value P rank death a T hist pattern')
    for key in ['ge2', 'ge3', 'ge4', 'ge5', 'avg']:
        value, P, rank, death, a, T, hist, pattern = worst[key]
        print(key, f'{value:.3f}', P, rank, death, a, T, sorted(hist.items()), pattern)


if __name__ == '__main__':
    main()
