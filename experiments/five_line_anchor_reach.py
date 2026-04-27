#!/usr/bin/env python3
"""五线骨架第一行锚点可达性扫描。

只检查 CRT 给出的 a=(-lambda P mod L) 是否落在 1..P 且为素数，
不做全窗口分解，用于估计五线骨架第一次可能 lift 的尺度。

用法示例：
    python3 experiments/five_line_anchor_reach.py --maxP 10000000 --show 20
"""
import argparse
import sys
from collections import Counter

sys.path.append('experiments')
from five_line_lift_scan import candidate_skeletons, residue_lambda
from fixed_anchor_sieve_remainder import primes_upto

BAD_Q = {2, 3, 5, 7, 11, 13, 17, 19, 23, 31}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=10_000_000)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    primes = primes_upto(args.maxP)
    prime_set = set(primes)
    skeletons = [(i, sk, *residue_lambda(sk[0], sk[4])) for i, sk in enumerate(candidate_skeletons(), 1)]
    hits = []
    hist = Counter()
    best_ratio = []

    for sk_id, sk, lam, modulus in skeletons:
        c, holes, residue13, triple_rows, chosen, model_cover = sk
        min_ratio = (10.0, None, None)
        local_hits = 0
        for P in primes:
            if P in BAD_Q:
                continue
            a = (-lam * (P % modulus)) % modulus
            if a == 0:
                a = modulus
            ratio = a / P
            if ratio < min_ratio[0]:
                min_ratio = (ratio, P, a)
            if a < P and a in prime_set:
                local_hits += 1
                hits.append((P, a, sk_id, c, residue13, lam, modulus, ratio))
        hist[local_hits] += 1
        best_ratio.append((min_ratio[0], min_ratio[1], min_ratio[2], sk_id, c, residue13, lam, modulus, local_hits))

    hits.sort()
    best_ratio.sort()
    print('maxP', args.maxP, 'skeletons', len(skeletons), 'total_anchor_hits', len(hits), 'hit_hist_by_skeleton', sorted(hist.items()))
    print('first_hits: P a sk c res13 ratio')
    for row in hits[:args.show]:
        P, a, sk_id, c, residue13, _lam, _modulus, ratio = row
        print(P, a, sk_id, c, residue13, f'{ratio:.6f}')
    print('best_ratios: ratio P a sk c res13 local_hits')
    for row in best_ratio[:args.show]:
        ratio, P, a, sk_id, c, residue13, _lam, _modulus, local_hits = row
        print(f'{ratio:.6f}', P, a, sk_id, c, residue13, local_hits)


if __name__ == '__main__':
    main()
