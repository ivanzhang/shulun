#!/usr/bin/env python3
"""同态一致锚点 H 扫描。

枚举 P mod 2310 与 a mod 2310 的单位类，强制 B11 前洞模板
c ≡ -a P^{-1} (mod 2310)。然后生成连续 W 个前洞，枚举候选共享边
q|r_j-r_i，并统计固定锚点 a 是否满足 a ≡ -r_i P (mod q)。

这是比 pure_congruence 更贴近方阵的模型。

用法示例：
  python3 experiments/consistent_anchor_H_scan.py --W 15 --show 12
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import primes_upto


def holes_for_c(c, y, count):
    """生成 B_y 模板 c 的前 count 个洞高。"""
    M = math.prod(primes_upto(y))
    holes = []
    r = 1
    while len(holes) < count:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def gt_y_prime_factors(n, y, prime_cache):
    """返回 n 的大于 y 的不同素因子。"""
    out = []
    x = n
    for p in prime_cache:
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


def candidate_hits(Pmod, amod, holes, y, prime_cache, nonzero=True):
    """返回同态一致窗口中的 H 命中边。"""
    hits = []
    candidates = []
    for i, r in enumerate(holes):
        for j in range(i + 1, len(holes)):
            diff = holes[j] - r
            for q in gt_y_prime_factors(diff, y, prime_cache):
                required = (-r * (Pmod % q)) % q
                candidates.append((i, j, diff, q, required))
                if nonzero and required == 0:
                    continue
                if (amod - required) % q == 0:
                    hits.append((i, j, diff, q, required))
    return hits, candidates


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--show', type=int, default=12)
    parser.add_argument('--allow-zero', action='store_true')
    args = parser.parse_args()

    M = math.prod(primes_upto(args.y))
    units = [x for x in range(M) if math.gcd(x, M) == 1]
    prime_cache = primes_upto(200)
    hist = Counter()
    records = []
    for Pmod in units:
        invP = pow(Pmod, -1, M)
        for amod in units:
            c = (-amod * invP) % M
            holes = holes_for_c(c, args.y, args.W)
            hits, candidates = candidate_hits(Pmod, amod, holes, args.y, prime_cache, nonzero=not args.allow_zero)
            H = len(hits)
            hist[H] += 1
            if len(records) < args.show or H > records[-1][0]:
                records.append((H, Pmod, amod, c, holes, hits, len(candidates)))
                records.sort(reverse=True, key=lambda x: x[0])
                records = records[:args.show]
    print('y', args.y, 'W', args.W, 'units', len(units), 'pairs', len(units) ** 2, 'allow_zero', args.allow_zero, 'hist', sorted(hist.items()), 'max', records[0][0])
    print('top H Pmod amod c candidate_count holes hits')
    for H, Pmod, amod, c, holes, hits, candidate_count in records:
        print('record', H, 'Pmod', Pmod, 'amod', amod, 'c', c, 'candidate_count', candidate_count, 'holes', holes)
        print(' hits', [(i + 1, j + 1, diff, q, b) for i, j, diff, q, b in hits])


if __name__ == '__main__':
    main()
