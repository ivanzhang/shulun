#!/usr/bin/env python3
"""差分链 lift 障碍扫描器。

取固定 c,T 的最优差分链，把每个共享簇 q: r≡b mod q 转成：
    a + rP == 0 (mod q)
即 a == -b P (mod q)。
同时 B11 模板给出 a == -c P (mod 2310)。
合并得到 a == -lambda P (mod L)。
然后扫描素数 P 与第一行素数锚点 a，检查整段 T 个洞是否真实全合数。

用法示例：
    python3 experiments/difference_chain_lift_obstruction.py --c 1213 --T 30 --maxP 10000000 --show 10
    python3 experiments/difference_chain_lift_obstruction.py --c 1213 --T 36 --maxP 10000000 --show 10
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c, min_cover_fast
from fixed_anchor_sieve_remainder import primes_upto
from local_cover_min_scan import exact_cover_size

M = 2310
Y = 11
BAD_SMALL = {2, 3, 5, 7, 11}


def crt_pair(a1, m1, a2, m2):
    """合并互素同余 x=a1 mod m1, x=a2 mod m2。"""
    inv = pow(m1, -1, m2)
    k = ((a2 - a1) * inv) % m2
    return (a1 + m1 * k) % (m1 * m2), m1 * m2


def skeleton_lambda(c, chosen):
    """合并 B11 与共享簇余数，得到 lambda mod L。"""
    lam, modulus = c % M, M
    for q, residue, _idxs, _mask in chosen:
        if math.gcd(modulus, q) != 1:
            raise ValueError(f'非互素模数: {modulus}, {q}')
        lam, modulus = crt_pair(lam, modulus, residue % q, q)
    return lam, modulus


def factor_small(n, primes, limit, P):
    """返回有效补丁素因子。"""
    out = []
    x = n
    for p in primes:
        if p > limit or p * p > x:
            break
        if x % p == 0:
            if p > Y and p != P:
                out.append(p)
            while x % p == 0:
                x //= p
    if x > 1 and x <= limit and x > Y and x != P:
        out.append(x)
    return tuple(out)


def patch_sets(P, a, holes, factor_primes):
    """计算真实补丁集合；遇到素数洞则返回 None。"""
    sets = []
    for r in holes:
        n = a + r * P
        qs = factor_small(n, factor_primes, math.isqrt(n), P)
        if not qs:
            return None
        sets.append(qs)
    return sets


def qmask_from_sets(holes, sets):
    """补丁素数到覆盖洞列表。"""
    q_to = defaultdict(list)
    for r, qs in zip(holes, sets):
        for q in qs:
            q_to[q].append(r)
    return {q: rs for q, rs in q_to.items() if len(rs) >= 2}


def chosen_signature(holes, chosen):
    """输出共享簇签名。"""
    return [(q, residue, tuple(holes[i] for i in idxs)) for q, residue, idxs, _mask in chosen]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--maxP', type=int, default=10_000_000)
    parser.add_argument('--show', type=int, default=10)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.T)
    best = min_cover_fast(holes)
    chosen = best['chosen']
    lam, modulus = skeleton_lambda(args.c, chosen)

    primes = primes_upto(args.maxP)
    prime_set = set(primes)
    factor_primes = primes_upto(math.isqrt(args.maxP * (max(holes) + args.maxP)) + 1000)

    tested_lifts = 0
    prime_anchor = 0
    full = 0
    cover_hist = Counter()
    first_prime_gap_hist = Counter()
    records = []

    for P in primes:
        if P in BAD_SMALL or any(P == q for q, _res, _idxs, _mask in chosen):
            continue
        a0 = (-lam * (P % modulus)) % modulus
        if a0 == 0:
            a0 = modulus
        a = a0
        while a < P:
            tested_lifts += 1
            if a in prime_set:
                prime_anchor += 1
                sets = patch_sets(P, a, holes, factor_primes)
                if sets is not None:
                    full += 1
                    cover = exact_cover_size(sets)
                    cover_hist[cover] += 1
                    shared = qmask_from_sets(holes, sets)
                    records.append((cover, P, a, shared, sets))
                else:
                    # 记录第一个幸存素数洞的位置，用作灭绝指标。
                    first_bad = None
                    for idx, r in enumerate(holes):
                        n = a + r * P
                        qs = factor_small(n, factor_primes, math.isqrt(n), P)
                        if not qs:
                            first_bad = idx + 1
                            break
                    first_prime_gap_hist[first_bad] += 1
            a += modulus

    records.sort(key=lambda x: (x[0], x[1], x[2]))
    print('c', args.c, 'T', args.T, 'shape_cover', best['cover'], 'shape_ratio', f'{best["cover"]/args.T:.6f}')
    print('lambda', lam, 'modulus', modulus)
    print('holes', holes)
    print('chosen', chosen_signature(holes, chosen))
    print('maxP', args.maxP, 'tested_lifts', tested_lifts, 'prime_anchor', prime_anchor, 'full', full)
    print('cover_hist', sorted(cover_hist.items()), 'first_prime_gap_hist', sorted(first_prime_gap_hist.items()))
    for rank, (cover, P, a, shared, sets) in enumerate(records[:args.show], 1):
        print(rank, 'cover', cover, 'P', P, 'a', a)
        print('  shared', shared)
        print('  sets', sets)


if __name__ == '__main__':
    main()
