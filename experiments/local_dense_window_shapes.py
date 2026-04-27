#!/usr/bin/env python3
"""最密局部窗口形状分析。

枚举长尾样本中连续 W 个前洞窗口，找出多补丁洞数量最多的窗口；输出窗口洞高、
多补丁位置、每个多补丁洞的补丁集合、二阶模 qs 以及这些模之间的最小乘积/重复情况。

用法示例：
  python3 experiments/local_dense_window_shapes.py --Ps 32003,64007,128021,256019 --K 35 --y 11 --W 15 --top-records 8 --top-windows 10
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


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


def pair_products(qs):
    """列出补丁集合的所有二阶乘积。"""
    out = []
    qs = sorted(qs)
    for i, q in enumerate(qs):
        for s in qs[i + 1:]:
            out.append((q, s, q * s))
    return out


def dense_windows(P, y, death, a, holes, pattern, W):
    """返回一个记录中所有窗口的密度描述。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    rows = []
    for idx, r in enumerate(prefix, start=1):
        qs = patch_set(a + r * P, y, P)
        rows.append({'idx': idx, 'r': r, 'qs': qs, 'multi': len(qs) >= 2, 'pairs': pair_products(qs)})
    out = []
    for start in range(0, max(0, len(rows) - W + 1)):
        window = rows[start:start + W]
        multi_rows = [row for row in window if row['multi']]
        all_pairs = [(row['idx'], row['r'], q, s, prod) for row in multi_rows for q, s, prod in row['pairs']]
        pair_mods = [prod for *_, prod in all_pairs]
        q_counts = defaultdict(int)
        for row in multi_rows:
            for q in row['qs']:
                q_counts[q] += 1
        shared_q = {q: c for q, c in q_counts.items() if c >= 2}
        out.append({
            'P': P, 'a': a, 'death': death, 'T': len(prefix), 'pattern': pattern,
            'start_idx': window[0]['idx'], 'end_idx': window[-1]['idx'],
            'start_r': window[0]['r'], 'end_r': window[-1]['r'],
            'span_r': window[-1]['r'] - window[0]['r'],
            'multi_count': len(multi_rows),
            'multi_rows': multi_rows,
            'pair_count': len(all_pairs),
            'min_pair_mod': min(pair_mods) if pair_mods else 0,
            'max_pair_mod': max(pair_mods) if pair_mods else 0,
            'shared_q': shared_q,
        })
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--top-records', type=int, default=8)
    parser.add_argument('--top-windows', type=int, default=10)
    args = parser.parse_args()

    windows = []
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for rec in collect_records(P, args.A, args.y, args.K)[:args.top_records]:
            death, a, holes, pattern = rec
            windows.extend(dense_windows(P, args.y, death, a, holes, pattern, args.W))
    windows.sort(key=lambda x: (x['multi_count'], x['pair_count'], -x['span_r']), reverse=True)

    print('W', args.W, 'windows', len(windows))
    for rank, win in enumerate(windows[:args.top_windows], start=1):
        print('window', rank, 'P', win['P'], 'a', win['a'], 'death', win['death'], 'T', win['T'], 'idx', (win['start_idx'], win['end_idx']), 'r', (win['start_r'], win['end_r']), 'span', win['span_r'], 'multi', win['multi_count'], 'pair_count', win['pair_count'], 'min_pair_mod', win['min_pair_mod'], 'max_pair_mod', win['max_pair_mod'], 'shared_q', sorted(win['shared_q'].items()), 'pattern', win['pattern'])
        print('  multi idx r qs pairmods')
        for row in win['multi_rows']:
            print(' ', row['idx'], row['r'], row['qs'], [prod for _, _, prod in row['pairs']])


if __name__ == '__main__':
    main()
