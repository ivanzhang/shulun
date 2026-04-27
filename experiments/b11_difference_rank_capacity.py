#!/usr/bin/env python3
"""纯 B11 差分共享秩容量。

对 B11 连续 W 个前洞窗口，只看高度差允许的 q>11 共享。
对每个 q，若窗口中某个 mod q 类有 m 个洞，则该 q 可贡献秩 m-1。
求 sum_q max_b(count_q,b-1)_+，这是纯差分层面 R 的宽上界。

用法示例：
  python3 experiments/b11_difference_rank_capacity.py --W 15 --show 10
"""
import argparse
import math
from collections import Counter, defaultdict
from fixed_anchor_sieve_remainder import primes_upto


def holes_for_c(c, y, W):
    M = math.prod(primes_upto(y))
    holes = []
    r = 1
    while len(holes) < W:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def prime_factors_gt(n, y, primes):
    out = []
    x = n
    for p in primes:
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


def rank_capacity(holes, y):
    span = holes[-1] - holes[0]
    primes = primes_upto(max(2, span + 1))
    qs = set()
    for i, r in enumerate(holes):
        for s in holes[i + 1:]:
            qs.update(prime_factors_gt(s - r, y, primes))
    details = []
    total = 0
    for q in sorted(qs):
        cnt = Counter(r % q for r in holes)
        residue, m = max(cnt.items(), key=lambda kv: kv[1])
        if m >= 2:
            total += m - 1
            details.append((q, residue, m, m - 1, [r for r in holes if r % q == residue]))
    return total, details


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--show', type=int, default=10)
    parser.add_argument('--patterns', type=int, default=2310)
    args = parser.parse_args()
    M = math.prod(primes_upto(args.y))
    records = []
    hist = Counter()
    for c in range(min(args.patterns, M)):
        holes = holes_for_c(c, args.y, args.W)
        cap, details = rank_capacity(holes, args.y)
        hist[cap] += 1
        records.append((cap, c, holes, details))
    records.sort(reverse=True, key=lambda x: x[0])
    print('y', args.y, 'W', args.W, 'patterns', min(args.patterns, M), 'hist', sorted(hist.items()), 'max', records[0][0])
    for cap, c, holes, details in records[:args.show]:
        print('record cap', cap, 'c', c, 'holes', holes)
        print(' details', details)


if __name__ == '__main__':
    main()
