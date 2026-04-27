#!/usr/bin/env python3
"""固定锚点筛余项分析。

研究列 AP：n_r=a+rP, 0<=r<P。
对每个高度窗口 [0,R)，只使用自洽小素数 q<=sqrt(a+(R-1)P) 的固定锚点覆盖：
    r == -a * P^{-1} (mod q)。
输出真实幸存数 H、独立模型期望 E、二阶包含-排除量 pair、覆盖重叠量，寻找最坏类的余项结构。

用法示例：
    python3 experiments/fixed_anchor_sieve_remainder.py --P 461 --a 22 --detail
    python3 experiments/fixed_anchor_sieve_remainder.py --scan --maxP 2000 --top 20
"""
import argparse
import math
from collections import Counter


def sieve(n):
    arr = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        arr[0:1] = b"\x00"
    if n >= 1:
        arr[1:2] = b"\x00"
    for p in range(2, math.isqrt(n) + 1):
        if arr[p]:
            arr[p * p:n + 1:p] = b"\x00" * (((n - p * p) // p) + 1)
    return arr


def primes_upto(n):
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def first_prime_r(P, a, prime_flags):
    for r in range(P):
        if prime_flags[a + r * P]:
            return r
    return None


def fixed_cover_stats(P, a, R=None, detail=False):
    if R is None:
        R = P
    if R <= 0:
        return None
    Q = math.isqrt(a + (R - 1) * P)
    qs = [q for q in primes_upto(min(P, Q)) if q != P]
    hit_count = [0] * R
    residues = []
    for q in qs:
        b = (-a * pow(P, -1, q)) % q
        residues.append((q, b))
        for r in range(b, R, q):
            hit_count[r] += 1
    H = sum(1 for x in hit_count if x == 0)
    covered = R - H
    total_hits = sum(hit_count)
    overlap_excess = total_hits - covered

    # 独立/密度模型：E = R * prod(1-1/q)
    prod = 1.0
    for q, _ in residues:
        prod *= (1.0 - 1.0 / q)
    E = R * prod

    # 精确一阶与二阶包含排除；交集由 CRT 唯一确定，计数只差端点 O(1)。
    single = 0
    for q, b in residues:
        if b < R:
            single += (R - 1 - b) // q + 1
    pair = 0
    pair_dev_from_R_over_qt = 0.0
    for i, (q, bq) in enumerate(residues):
        for t, bt in residues[i + 1:]:
            # 解 r=bq mod q, r=bt mod t
            inv = pow(q, -1, t)
            k = ((bt - bq) * inv) % t
            x0 = bq + q * k
            mod = q * t
            cnt = 0 if x0 >= R else (R - 1 - x0) // mod + 1
            pair += cnt
            pair_dev_from_R_over_qt += cnt - R / mod

    multiplicity = Counter(hit_count)
    max_mult = max(hit_count) if hit_count else 0
    # Buchstab/Mertens 级别的标准尺度：R/log(Q)，只作为归一化，不当作定理证明。
    scale = R / max(1.0, math.log(max(3, Q)))
    rec = {
        'P': P, 'a': a, 'R': R, 'Q': Q, 'q_count': len(qs),
        'H': H, 'covered': covered, 'total_hits': total_hits, 'overlap_excess': overlap_excess,
        'E': E, 'H_over_E': H / E if E else float('inf'),
        'H_over_scale': H / scale if scale else float('inf'),
        'single': single, 'pair': pair, 'pair_dev': pair_dev_from_R_over_qt,
        'max_mult': max_mult, 'multiplicity': multiplicity,
        'residues': residues,
        'survivors': [r for r, x in enumerate(hit_count) if x == 0],
        'unique': [r for r, x in enumerate(hit_count) if x == 1],
    }
    return rec


def print_rec(rec, detail=False):
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},Q={rec['Q']},q_count={rec['q_count']},"
        f"H={rec['H']},E={rec['E']:.3f},H/E={rec['H_over_E']:.3f},"
        f"H/(R/logQ)={rec['H_over_scale']:.3f},covered={rec['covered']},"
        f"hits={rec['total_hits']},overlap={rec['overlap_excess']},"
        f"single={rec['single']},pair={rec['pair']},pair_dev={rec['pair_dev']:.3f},"
        f"max_mult={rec['max_mult']}"
    )
    print('multiplicity=', sorted(rec['multiplicity'].items())[:12])
    print('first_survivors=', rec['survivors'][:30])
    if detail:
        print('residues(q,b)=', rec['residues'])
        print('unique_first=', rec['unique'][:80])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--a', type=int, default=22)
    ap.add_argument('--R', type=int, default=0)
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=1000)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()

    if args.scan:
        prime_flags = sieve(args.maxP * args.maxP)
        rows = []
        for P in primes_upto(args.maxP):
            if P < 3:
                continue
            worst_a, worst_R = 1, -1
            for a in range(1, P + 1):
                R0 = first_prime_r(P, a, prime_flags)
                if R0 is not None and R0 > worst_R:
                    worst_a, worst_R = a, R0
            rec = fixed_cover_stats(P, worst_a, R=P)
            rec['first_prime_R'] = worst_R
            rows.append(rec)
        rows.sort(key=lambda x: (-x['first_prime_R'], x['H'], -x['P']))
        for rec in rows[:args.top]:
            print(f"first_prime_R={rec['first_prime_R']}", end=',')
            print_rec(rec, detail=False)
    else:
        R = args.R or args.P
        print_rec(fixed_cover_stats(args.P, args.a, R=R), detail=args.detail)


if __name__ == '__main__':
    main()
