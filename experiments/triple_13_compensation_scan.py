#!/usr/bin/env python3
"""q=13 三点簇补偿扫描。

专门寻找含 q=13 三点候选的窗口，测试实际 lift 后：
- q=13 是否三点实现；
- 还能叠加多少其他共享簇；
- 总共享秩 R 是否超过 3。

用法示例：
  python3 experiments/triple_13_compensation_scan.py --maxP 120000 --max-a-per-class 200 --show 20
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from hole_index_prime_rate import factor, isprimefac

Y = 11
M = 2310


def holes_for_c(c, W):
    holes = []
    r = 1
    while len(holes) < W:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def triple_13_templates(W):
    out = []
    for c in range(M):
        holes = holes_for_c(c, W)
        by = defaultdict(list)
        for r in holes:
            by[r % 13].append(r)
        for residue, rs in by.items():
            if len(rs) >= 3:
                out.append((c, holes, residue, tuple(rs)))
    return out


def patch_set(n, P):
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > Y and q <= root and q != P)


def stats(P, a, holes):
    sets = []
    prime_pos = []
    for idx, r in enumerate(holes, start=1):
        n = a + r * P
        fac = factor(n)
        if isprimefac(fac, n):
            prime_pos.append(idx)
            sets.append(())
        else:
            sets.append(tuple(q for q, _ in fac if q > Y and q <= math.isqrt(n) and q != P))
    if prime_pos:
        return None, prime_pos, sets
    q_to_rs = defaultdict(list)
    for r, qs in zip(holes, sets):
        for q in qs:
            q_to_rs[q].append(r)
    shared = {q: rs for q, rs in q_to_rs.items() if len(rs) >= 2}
    R = sum(len(rs) - 1 for rs in shared.values())
    H = sum(len(rs) * (len(rs) - 1) // 2 for rs in shared.values())
    return {'R': R, 'H': H, 'shared': shared, 'sets': sets}, [], sets


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=120000)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--max-a-per-class', type=int, default=200)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    maxN = args.maxP * 200 + args.maxP
    primes = [p for p in primes_upto(args.maxP) if p > M]
    by_mod = defaultdict(list)
    for p in primes:
        by_mod[p % M].append(p)

    templates = triple_13_templates(args.W)
    print('triple_templates', len(templates), 'maxP', args.maxP)
    results = []
    fail = Counter()
    tested = 0
    for c, holes, residue, triple_rs in templates:
        # 一致条件 c=-aP^{-1}; 给定 Pmod，amod=-c*Pmod。
        for Pmod, Ps in by_mod.items():
            amod = (-c * Pmod) % M
            if math.gcd(amod, M) != 1:
                continue
            acands = by_mod.get(amod, [])
            for P in Ps:
                acount = 0
                for a in acands:
                    if a >= P:
                        break
                    acount += 1
                    if acount > args.max_a_per_class:
                        break
                    # 要 q=13 三点实际实现，先检查 a+rP 被13整除。
                    if any((a + r * P) % 13 != 0 for r in triple_rs):
                        continue
                    tested += 1
                    st, prime_pos, sets = stats(P, a, holes)
                    if st is None:
                        fail[prime_pos[0] if prime_pos else -1] += 1
                        continue
                    if 13 in st['shared'] and len(st['shared'][13]) >= 3:
                        results.append((st['R'], st['H'], P, a, c, residue, triple_rs, st['shared'], [len(s) for s in st['sets']], holes))
    results.sort(reverse=True, key=lambda x: (x[0], x[1]))
    print('tested_triple13_candidates', tested, 'full_composite_triple13', len(results), 'prime_fail', fail.most_common(8))
    print('rank R H P a c residue triple_rs shared sizes holes')
    for rank, rec in enumerate(results[:args.show], start=1):
        print(rank, *rec)


if __name__ == '__main__':
    main()
