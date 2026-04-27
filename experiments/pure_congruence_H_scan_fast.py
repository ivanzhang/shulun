#!/usr/bin/env python3
"""快速纯同余 H(a) 扫描。

对每个窗口与 P mod 2310，候选边只给出 a mod q 的命中要求。
按 q 分组后，同一 q 只能选择同一个剩余类；H 最大值就是各 q 组中出现次数最多的剩余类计数之和。

用法示例：
  python3 experiments/pure_congruence_H_scan_fast.py --W 15 --show 10
"""
import argparse
import math
from collections import Counter, defaultdict

from fixed_anchor_sieve_remainder import primes_upto


def holes_for_c(c, y, count):
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


def candidate_edges(holes, y):
    edges = []
    for i, r in enumerate(holes):
        for j in range(i + 1, len(holes)):
            diff = holes[j] - r
            for q in gt_y_prime_factors(diff, y):
                edges.append((i, j, q, r, diff))
    return edges


def max_H_fast(edges, pmod):
    """最大兼容同余命中数，并返回见证。"""
    groups = defaultdict(list)
    for edge in edges:
        i, j, q, r, diff = edge
        b = (-r * (pmod % q)) % q
        groups[q].append((b, edge))
    total = 0
    witness = []
    for q, items in groups.items():
        by_b = defaultdict(list)
        for b, edge in items:
            by_b[b].append(edge)
        b, best_edges = max(by_b.items(), key=lambda kv: len(kv[1]))
        total += len(best_edges)
        witness.extend((q, b, edge) for edge in best_edges)
    return total, witness


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--show', type=int, default=10)
    parser.add_argument('--patterns', type=int, default=2310)
    args = parser.parse_args()

    modulus = math.prod(primes_upto(args.y))
    pmods = [p for p in range(modulus) if math.gcd(p, modulus) == 1]
    records = []
    hist = Counter()
    for pmod in pmods:
        for c in range(min(args.patterns, modulus)):
            holes = holes_for_c(c, args.y, args.W)
            edges = candidate_edges(holes, args.y)
            best, witness = max_H_fast(edges, pmod)
            hist[best] += 1
            records.append((best, pmod, c, holes, witness, edges))
    records.sort(reverse=True, key=lambda x: x[0])
    print('y', args.y, 'W', args.W, 'pmods', len(pmods), 'patterns', min(args.patterns, modulus), 'hist_top', sorted(hist.items())[-10:], 'max', records[0][0])
    print('top best pmod c holes witness')
    for best, pmod, c, holes, witness, edges in records[:args.show]:
        print('record', best, 'pmod', pmod, 'c', c, 'edge_count', len(edges), 'holes', holes)
        print(' witness', [(edge[0]+1, edge[1]+1, edge[4], q, b) for q,b,edge in witness])


if __name__ == '__main__':
    main()
