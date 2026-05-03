#!/usr/bin/env python3
"""采样分解筛余四阶中心矩的相等模式贡献。

对 H(a)=sum_r X_r(a)，四阶中心矩为 sum_{r1..r4} E_a prod_i (X_ri-p_ri)。
本脚本按四元组相等模式抽样估计每类总贡献，避免 P^4 全枚举。
"""
import argparse
import itertools
import random
from statistics import mean
from sieve_remainder_pair_correlation import alive_matrix


def pattern_type(tup):
    counts = sorted([tup.count(x) for x in set(tup)], reverse=True)
    return tuple(counts)


def sample_tuple(P, typ):
    """按指定相等模式均匀生成一个有序四元组。"""
    if typ == (4,):
        r = random.randrange(P)
        return (r, r, r, r)
    if typ == (3, 1):
        vals = random.sample(range(P), 2)
        arr = [vals[0]] * 3 + [vals[1]]
    elif typ == (2, 2):
        vals = random.sample(range(P), 2)
        arr = [vals[0], vals[0], vals[1], vals[1]]
    elif typ == (2, 1, 1):
        vals = random.sample(range(P), 3)
        arr = [vals[0], vals[0], vals[1], vals[2]]
    elif typ == (1, 1, 1, 1):
        arr = random.sample(range(P), 4)
    else:
        raise ValueError(typ)
    random.shuffle(arr)
    return tuple(arr)


def ordered_count(P, typ):
    """指定相等模式的有序四元组总数。"""
    if typ == (4,):
        return P
    if typ == (3, 1):
        return P * (P - 1) * 4
    if typ == (2, 2):
        return P * (P - 1) // 2 * 6
    if typ == (2, 1, 1):
        return P * (P - 1) * (P - 2) // 2 * 12
    if typ == (1, 1, 1, 1):
        return P * (P - 1) * (P - 2) * (P - 3)
    raise ValueError(typ)


def tuple_expectation(A, pr, tup):
    total = 0.0
    for row in A:
        prod = 1.0
        for r in tup:
            prod *= row[r] - pr[r]
        total += prod
    return total / len(A)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=503)
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--samples', type=int, default=3000)
    ap.add_argument('--seed', type=int, default=1)
    args = ap.parse_args()
    random.seed(args.seed)

    P = args.P
    A = alive_matrix(P, args.c)
    H = [sum(row) for row in A]
    mu = mean(H)
    fourth_direct = mean((h - mu) ** 4 for h in H)
    variance = mean((h - mu) ** 2 for h in H)
    pr = [mean(row[r] for row in A) for r in range(P)]

    print(f'P={P} c={args.c} rows={len(A)} meanH={mu:.6f} var={variance:.6f} fourthDirect={fourth_direct:.6f} kurt={fourth_direct/(variance*variance):.4f}')
    print('pattern count samples meanTerm absMeanTerm totalEstimate fracOfFourth')

    total_est = 0.0
    estimates = []
    for typ in [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]:
        n = ordered_count(P, typ)
        vals = [tuple_expectation(A, pr, sample_tuple(P, typ)) for _ in range(args.samples)]
        mt = mean(vals)
        amt = mean(abs(v) for v in vals)
        est = n * mt
        total_est += est
        estimates.append((typ, n, mt, amt, est))
    for typ, n, mt, amt, est in estimates:
        frac = est / fourth_direct if fourth_direct else 0.0
        print(f'{typ} {n} {args.samples} {mt:.8g} {amt:.8g} {est:.6f} {frac:.4f}')
    print(f'totalEstimate={total_est:.6f} ratioToDirect={total_est/fourth_direct if fourth_direct else 0:.4f}')


if __name__ == '__main__':
    main()
