#!/usr/bin/env python3
"""B11 前洞窗口的全局共享形状容量枚举。

不预设 q=13 三点簇，直接枚举所有 B11 平移 c 的前 W 个洞，
以及所有可共享的补丁斜率 q>11。由于窗口跨度有限，q 大于最大洞差时只能单点覆盖，
不会降低 cover，因此只需枚举到 max(holes)-min(holes)。

用法示例：
    python3 experiments/general_b11_shape_capacity.py --W 15 --show 20
"""
import argparse
import math
from collections import defaultdict, Counter

M = 2310
Y = 11


def sieve(n):
    """返回 n 以内素数布尔表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0:1] = b"\x00"
    if n >= 1:
        flags[1:2] = b"\x00"
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            flags[p * p:n + 1:p] = b"\x00" * (((n - p * p) // p) + 1)
    return flags


def primes_upto(n):
    """列出 n 以内素数。"""
    if n < 2:
        return []
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def holes_for_c(c, W):
    """给定 B11 平移 c，取前 W 个 B11 前洞高度。"""
    holes = []
    r = 1
    while len(holes) < W:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return tuple(holes)


def clusters_for_holes(holes):
    """列出所有能覆盖至少两个洞的 q-余数簇。"""
    span = max(holes) - min(holes)
    clusters = []
    for q in primes_upto(span):
        if q <= Y:
            continue
        by = defaultdict(list)
        for idx, r in enumerate(holes):
            by[r % q].append(idx)
        for residue, idxs in by.items():
            if len(idxs) >= 2:
                mask = sum(1 << i for i in idxs)
                clusters.append((q, residue, tuple(idxs), mask))
    return clusters


def min_cover_q_mutex(holes):
    """同一个 q 只能取一个余数簇，求共享形状理论最小 cover。"""
    W = len(holes)
    full = (1 << W) - 1
    by_q = defaultdict(list)
    for item in clusters_for_holes(holes):
        by_q[item[0]].append(item)
    groups = sorted(by_q.items(), key=lambda x: x[0])
    best = {'cover': W, 'chosen': [], 'mask': 0}

    suffix = [0] * (len(groups) + 1)
    for i in range(len(groups) - 1, -1, -1):
        suffix[i] = suffix[i + 1]
        for _q, _res, _idxs, mask in groups[i][1]:
            suffix[i] |= mask

    def dfs(i, covered, chosen):
        current = len(chosen) + (full ^ covered).bit_count()
        if current < best['cover']:
            best['cover'] = current
            best['chosen'] = chosen[:]
            best['mask'] = covered
        if i == len(groups):
            return
        if len(chosen) >= best['cover']:
            return
        optimistic = len(chosen) + (full ^ (covered | suffix[i])).bit_count()
        if optimistic >= best['cover']:
            return
        q, options = groups[i]
        dfs(i + 1, covered, chosen)
        for item in sorted(options, key=lambda x: -(x[3] & ~covered).bit_count()):
            gain = (item[3] & ~covered).bit_count()
            if gain >= 2:
                dfs(i + 1, covered | item[3], chosen + [item])

    dfs(0, 0, [])
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    rows = []
    hist = Counter()
    for c in range(M):
        holes = holes_for_c(c, args.W)
        best = min_cover_q_mutex(holes)
        hist[best['cover']] += 1
        rows.append((best['cover'], -best['mask'].bit_count(), c, holes, best))
    rows.sort()
    print('W', args.W, 'templates', M, 'cover_hist', sorted(hist.items()))
    print('rank cover covered c holes chosen')
    for rank, (cover, neg_cov, c, holes, best) in enumerate(rows[:args.show], 1):
        chosen = [(q, res, tuple(holes[i] for i in idxs)) for q, res, idxs, _mask in best['chosen']]
        print(rank, cover, -neg_cov, c, holes, chosen)


if __name__ == '__main__':
    main()
