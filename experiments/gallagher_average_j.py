#!/usr/bin/env python3
"""采样检验 j=2,3,4 多点奇异级数平均误差。

S_j(R)=prod_q (1-nu_q(R)/q)/p^j，其中 p=prod_q(1-1/q)。
"""
import argparse
import random
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes


def singular_ratio(R, small, p):
    prob = 1.0
    for q in small:
        nu = len({r % q for r in R})
        if nu >= q:
            return 0.0
        prob *= 1 - nu / q
    return prob / (p ** len(R))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='1009,2003,4001')
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--samples', type=int, default=30000)
    ap.add_argument('--seed', type=int, default=1)
    args = ap.parse_args()
    random.seed(args.seed)
    print('P j meanS meanMinus1 scaledByP std max')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags = sieve(P)
        root = primes(flags, P)
        small = [q for q in root if q <= int(args.c * P)]
        p = 1.0
        for q in small:
            p *= 1 - 1 / q
        for j in [2,3,4]:
            vals = []
            for _ in range(args.samples):
                R = random.sample(range(P), j)
                vals.append(singular_ratio(R, small, p))
            m = mean(vals)
            print(P, j, f'{m:.8f}', f'{m-1:.8f}', f'{(m-1)*P:.4f}', f'{pstdev(vals):.4f}', f'{max(vals):.3f}')

if __name__ == '__main__':
    main()
