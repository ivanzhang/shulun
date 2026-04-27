#!/usr/bin/env python3
"""纯 B11 前洞窗口的差分共享图最大匹配。

不使用具体 P,a，只枚举 B11 模板 c mod 2310 的连续 W 个前洞高度。
若两个洞高差 d 含有 q>11 的素因子，则它们存在候选共享边。
计算候选共享边图的最大匹配数，检验“最多3条”是否仅由洞高差决定。

用法示例：
  python3 experiments/b11_difference_matching.py --W 15 --patterns 2310 --show 12
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import primes_upto


def holes_for_c(c, y, count):
    """生成 B_y 模板 c 的前 count 个洞高。"""
    small = primes_upto(y)
    modulus = math.prod(small)
    holes = []
    r = 1
    while len(holes) < count:
        if math.gcd((r - c) % modulus, modulus) == 1:
            holes.append(r)
        r += 1
    return holes


def gt_y_prime_factors(n, y):
    """返回 n 中大于 y 的不同素因子。"""
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


def max_matching_size(n, edges):
    """小图最大匹配，暴力回溯。"""
    adj = [set() for _ in range(n)]
    for i, j, _ in edges:
        adj[i].add(j)
        adj[j].add(i)

    from functools import lru_cache

    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 0
        i = (mask & -mask).bit_length() - 1
        best = dp(mask & ~(1 << i))
        rest = mask & ~(1 << i)
        for j in adj[i]:
            if rest & (1 << j):
                best = max(best, 1 + dp(rest & ~(1 << j)))
        return best

    return dp((1 << n) - 1)


def edge_data(holes, y):
    """候选共享边：高度差含 q>y。"""
    edges = []
    for i, r in enumerate(holes):
        for j in range(i + 1, len(holes)):
            diff = holes[j] - r
            qs = gt_y_prime_factors(diff, y)
            if qs:
                edges.append((i, j, tuple(qs)))
    return edges


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--patterns', type=int, default=2310)
    parser.add_argument('--show', type=int, default=12)
    args = parser.parse_args()

    modulus = math.prod(primes_upto(args.y))
    limit = min(args.patterns, modulus)
    records = []
    hist = Counter()
    for c in range(limit):
        holes = holes_for_c(c, args.y, args.W)
        edges = edge_data(holes, args.y)
        matching = max_matching_size(args.W, edges)
        span = holes[-1] - holes[0]
        hist[matching] += 1
        records.append((matching, len(edges), span, c, holes, edges))

    records.sort(reverse=True)
    print('y', args.y, 'W', args.W, 'patterns', limit, 'hist', sorted(hist.items()))
    print('top matching edge_count span c holes edges')
    for matching, edge_count, span, c, holes, edges in records[:args.show]:
        print('record', matching, edge_count, span, c, holes)
        print(' edges', [(i + 1, j + 1, holes[j] - holes[i], qs) for i, j, qs in edges])


if __name__ == '__main__':
    main()
