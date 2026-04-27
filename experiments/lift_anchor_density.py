#!/usr/bin/env python3
"""CRT lift 锚点密度扫描。

对固定差分链骨架 a == -lambda P mod L，扫描素数 P<=X，统计：
1. 是否存在整数锚点 a<P；
2. 该 a 是否为第一行素数；
3. 理论粗上界 sum P/L 与真实命中对比。

用法示例：
    python3 experiments/lift_anchor_density.py --c 1213 --T 15 --maxP 10000000
    python3 experiments/lift_anchor_density.py --c 1213 --T 25 --maxP 10000000
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c, min_cover_fast
from difference_chain_lift_obstruction import skeleton_lambda
from fixed_anchor_sieve_remainder import primes_upto

BAD_SMALL = {2, 3, 5, 7, 11}


def scan(c, T, maxP):
    holes = holes_for_c(c, T)
    best = min_cover_fast(holes)
    lam, modulus = skeleton_lambda(c, best['chosen'])
    primes = primes_upto(maxP)
    prime_set = set(primes)
    chosen_qs = {q for q, _res, _idxs, _mask in best['chosen']}

    integer_hits = 0
    prime_anchor_hits = 0
    sum_p_over_L = 0.0
    min_ratio = (10.0, None, None)
    first_hits = []

    for P in primes:
        if P in BAD_SMALL or P in chosen_qs:
            continue
        sum_p_over_L += P / modulus
        a = (-lam * (P % modulus)) % modulus
        if a == 0:
            a = modulus
        ratio = a / P
        if ratio < min_ratio[0]:
            min_ratio = (ratio, P, a)
        if a < P:
            integer_hits += 1
            is_prime_anchor = a in prime_set
            if is_prime_anchor:
                prime_anchor_hits += 1
            if len(first_hits) < 20:
                first_hits.append((P, a, is_prime_anchor, ratio))

    return {
        'c': c,
        'T': T,
        'cover': best['cover'],
        'ratio': best['cover'] / T,
        'chosen_count': len(chosen_qs),
        'max_q': max(chosen_qs) if chosen_qs else 0,
        'lambda': lam,
        'L': modulus,
        'log10L': math.log10(modulus),
        'sqrtL': math.isqrt(modulus),
        'maxP': maxP,
        'prime_count': len(primes),
        'sum_p_over_L': sum_p_over_L,
        'integer_hits': integer_hits,
        'prime_anchor_hits': prime_anchor_hits,
        'min_ratio': min_ratio,
        'first_hits': first_hits,
    }


def print_rec(rec):
    print(
        'c', rec['c'], 'T', rec['T'], 'cover', rec['cover'], 'ratio', f'{rec["ratio"]:.6f}',
        'chosen', rec['chosen_count'], 'max_q', rec['max_q'],
        'log10L', f'{rec["log10L"]:.3f}', 'sqrtL', rec['sqrtL']
    )
    print(
        'maxP', rec['maxP'], 'prime_count', rec['prime_count'],
        'sumP/L', f'{rec["sum_p_over_L"]:.6f}',
        'integer_hits', rec['integer_hits'], 'prime_anchor_hits', rec['prime_anchor_hits'],
        'min_ratio', rec['min_ratio']
    )
    print('first_hits', rec['first_hits'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--T', type=int, default=15)
    parser.add_argument('--maxP', type=int, default=10_000_000)
    parser.add_argument('--Tlist', default='')
    args = parser.parse_args()

    if args.Tlist:
        print('c T cover ratio chosen log10L sqrtL maxP sumP/L integer_hits prime_anchor_hits min_ratio')
        for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
            rec = scan(args.c, T, args.maxP)
            print(
                rec['c'], rec['T'], rec['cover'], f'{rec["ratio"]:.6f}', rec['chosen_count'],
                f'{rec["log10L"]:.3f}', rec['sqrtL'], rec['maxP'], f'{rec["sum_p_over_L"]:.6f}',
                rec['integer_hits'], rec['prime_anchor_hits'], rec['min_ratio'],
                flush=True,
            )
        return

    print_rec(scan(args.c, args.T, args.maxP))


if __name__ == '__main__':
    main()
