#!/usr/bin/env python3
"""多补丁洞的局部窗口容量扫描。

对长尾样本，把 |Q_i|>=2 的洞视作标记点，统计任意连续 w 个 B11 前洞中
最多有多少个多补丁洞；也统计按高度长度 H 的窗口容量。这用于寻找局部排斥/容量上界。

用法示例：
  python3 experiments/multipatch_local_window_scan.py --Ps 32003,64007,128021,256019 --K 35 --y 11 --top 10
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
    """收集死亡最晚记录。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, 0) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, length in states:
                cnt = patch_count(a + r * P, y, P)
                if cnt:
                    nxt.append((a, length + 1))
                elif length:
                    records.append((idx, a, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, length in states:
            if length:
                records.append((K + 1, a, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def window_max_by_index(marked, T, widths):
    """连续 w 个洞索引窗口中的最大标记数。"""
    out = {}
    marks = [0] * T
    for idx in marked:
        if 1 <= idx <= T:
            marks[idx - 1] = 1
    prefix = [0]
    for value in marks:
        prefix.append(prefix[-1] + value)
    for w in widths:
        if w > T:
            out[w] = prefix[-1]
        else:
            out[w] = max(prefix[i + w] - prefix[i] for i in range(T - w + 1))
    return out


def window_max_by_height(marked_rs, heights):
    """高度长度 H 的窗口中最大标记数。"""
    rs = sorted(marked_rs)
    out = {}
    for H in heights:
        best = 0
        j = 0
        for i, r in enumerate(rs):
            while j < len(rs) and rs[j] <= r + H:
                j += 1
            best = max(best, j - i)
        out[H] = best
    return out


def analyze(P, y, death, a, holes):
    """分析单个长尾记录。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    counts = [patch_count(a + r * P, y, P) for r in prefix]
    marked = [idx for idx, cnt in enumerate(counts, start=1) if cnt >= 2]
    marked_rs = [prefix[idx - 1] for idx in marked]
    gaps_idx = [marked[i] - marked[i - 1] for i in range(1, len(marked))]
    gaps_r = [marked_rs[i] - marked_rs[i - 1] for i in range(1, len(marked_rs))]
    return {
        'T': len(prefix),
        'marked': marked,
        'marked_rs': marked_rs,
        'ge2': len(marked),
        'hist': Counter(counts),
        'gaps_idx': gaps_idx,
        'gaps_r': gaps_r,
        'win_idx': window_max_by_index(marked, len(prefix), [5, 8, 10, 12, 15]),
        'win_height': window_max_by_height(marked_rs, [10, 20, 30, 40, 60]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--top', type=int, default=10)
    args = parser.parse_args()

    global_idx_worst = {w: None for w in [5, 8, 10, 12, 15]}
    global_h_worst = {H: None for H in [10, 20, 30, 40, 60]}
    print('P rank death a T ge2 ratio hist marked_idx marked_r gaps_idx gaps_r win_idx win_height pattern')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for rank, rec in enumerate(collect_records(P, args.A, args.y, args.K)[:args.top], start=1):
            death, a, holes, pattern = rec
            st = analyze(P, args.y, death, a, holes)
            for w, val in st['win_idx'].items():
                if global_idx_worst[w] is None or val > global_idx_worst[w][0]:
                    global_idx_worst[w] = (val, P, rank, death, a, st['T'], st['marked'], pattern)
            for H, val in st['win_height'].items():
                if global_h_worst[H] is None or val > global_h_worst[H][0]:
                    global_h_worst[H] = (val, P, rank, death, a, st['T'], st['marked_rs'], pattern)
            print(P, rank, death, a, st['T'], st['ge2'], f'{st["ge2"]/st["T"] if st["T"] else 0:.3f}', sorted(st['hist'].items()), st['marked'], st['marked_rs'], st['gaps_idx'], st['gaps_r'], st['win_idx'], st['win_height'], pattern)
    print('worst_index_windows w max P rank death a T marked_idx pattern')
    for w, rec in global_idx_worst.items():
        print(w, *rec)
    print('worst_height_windows H max P rank death a T marked_r pattern')
    for H, rec in global_h_worst.items():
        print(H, *rec)


if __name__ == '__main__':
    main()
