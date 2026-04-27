#!/usr/bin/env python3
"""纯同余层面的 H(a) 最大值扫描。

对 B11 模板的连续 W 个前洞，构造候选共享边 e=(i,j,q), q|r_j-r_i。
在给定 P 模 q 的情况下，每条边要求 a ≡ -r_i P (mod q)。
本脚本枚举 P 在模 M=2310 的单位剩余类，并用 CRT/增量字典寻找是否存在 a 同时命中 >=threshold 条边。

注意：这是纯同余可行性，不要求 a 是素数，也不要求这些边对应的洞全合数。

用法示例：
  python3 experiments/pure_congruence_H_scan.py --W 15 --threshold 4 --show 10
"""
import argparse
import itertools
import math
from collections import Counter, defaultdict

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
    """返回 n 的大于 y 的不同素因子。"""
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
    """候选边列表。"""
    edges = []
    for i, r in enumerate(holes):
        for j in range(i + 1, len(holes)):
            diff = holes[j] - r
            for q in gt_y_prime_factors(diff, y):
                edges.append((i, j, q, r, diff))
    return edges


def compatible_system(congruences):
    """判断 a≡b mod q 的系统是否兼容；q 为素数但可能重复。"""
    by_q = {}
    for q, b in congruences:
        b %= q
        if q in by_q and by_q[q] != b:
            return False
        by_q[q] = b
    return True


def max_H_for_window(holes, y, P_mod, threshold):
    """枚举边子集，判断最大可同时命中数；候选边数量很小，直接组合搜索。"""
    edges = candidate_edges(holes, y)
    best = 0
    witness = None
    # 先检查从大到小是否有兼容子集；实际边数约 10-15。
    for k in range(len(edges), 0, -1):
        if k < best:
            break
        found = False
        for subset in itertools.combinations(range(len(edges)), k):
            congruences = []
            for idx in subset:
                _, _, q, r, _ = edges[idx]
                congruences.append((q, (-r * (P_mod % q)) % q))
            if compatible_system(congruences):
                best = k
                witness = subset
                found = True
                break
        if found:
            break
    hit_threshold = best >= threshold
    return best, witness, edges, hit_threshold


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--threshold', type=int, default=4)
    parser.add_argument('--show', type=int, default=10)
    parser.add_argument('--patterns', type=int, default=2310)
    parser.add_argument('--Pmods', type=int, default=2310, help='枚举前多少个 P mod 2310 候选；默认全体')
    args = parser.parse_args()

    modulus = math.prod(primes_upto(args.y))
    c_limit = min(args.patterns, modulus)
    pmods = [p for p in range(min(args.Pmods, modulus)) if math.gcd(p, modulus) == 1]
    records = []
    hist = Counter()
    threshold_count = 0
    for pmod in pmods:
        for c in range(c_limit):
            holes = holes_for_c(c, args.y, args.W)
            best, witness, edges, hit = max_H_for_window(holes, args.y, pmod, args.threshold)
            hist[best] += 1
            if hit:
                threshold_count += 1
            if witness is not None:
                records.append((best, pmod, c, holes, witness, edges))
    records.sort(reverse=True, key=lambda x: x[0])
    print('y', args.y, 'W', args.W, 'threshold', args.threshold, 'pmods', len(pmods), 'patterns', c_limit, 'hist', sorted(hist.items()), 'threshold_count', threshold_count)
    print('top best pmod c holes witness_edges')
    for best, pmod, c, holes, witness, edges in records[:args.show]:
        wit = []
        for idx in witness:
            i, j, q, r, diff = edges[idx]
            b = (-r * (pmod % q)) % q
            wit.append((i + 1, j + 1, diff, q, b))
        print('record', best, 'pmod', pmod, 'c', c, 'holes', holes)
        print(' witness', wit)


if __name__ == '__main__':
    main()
