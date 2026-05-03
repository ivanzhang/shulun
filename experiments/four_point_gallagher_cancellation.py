#!/usr/bin/env python3
"""检验 distinct 四点中心化平均中的 Gallagher 主项抵消。

对随机 distinct R=(r1..r4)，计算各子集大小 j 的联合幸存概率平均 G_j，
再看 sum_j C(4,j)(-p)^(4-j) G_j 的取消程度。
"""
import argparse
import random
import itertools
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def prob_tuple(vals, small):
    if not vals:
        return 1.0
    prob = 1.0
    for q in small:
        nu = len({v % q for v in vals})
        if nu >= q:
            return 0.0
        prob *= 1 - nu / q
    return prob


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=2003)
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--samples', type=int, default=20000)
    ap.add_argument('--seed', type=int, default=1)
    args = ap.parse_args()
    random.seed(args.seed)
    flags = sieve(args.P)
    root = primes(flags, args.P)
    small = [q for q in root if q <= int(args.c * args.P)]
    p = prob_tuple([0], small)
    sums = {j: [] for j in range(5)}
    central_vals = []
    for _ in range(args.samples):
        R = random.sample(range(args.P), 4)
        Gj_for_R = {0: 1.0}
        for j in range(1, 5):
            vals = []
            for idxs in itertools.combinations(range(4), j):
                vals.append(prob_tuple([R[i] for i in idxs], small))
            Gj_for_R[j] = mean(vals)
            sums[j].append(Gj_for_R[j])
        sums[0].append(1.0)
        cent = 0.0
        for j in range(5):
            # 每个 R 内已有对子集取平均，因此乘 C(4,j)
            from math import comb
            cent += comb(4, j) * ((-p) ** (4 - j)) * Gj_for_R[j]
        central_vals.append(cent)
    print(f'P={args.P} c={args.c} p={p:.8g} samples={args.samples}')
    print('j G_j G_j/p^j relErr')
    for j in range(5):
        gj = mean(sums[j])
        base = p ** j
        print(j, f'{gj:.10g}', f'{gj/base if base else 0:.8g}', f'{(gj-base)/base if base else 0:.8g}')
    print('centralMean', f'{mean(central_vals):.10g}', 'central/p4', f'{mean(central_vals)/(p**4):.8g}', 'meanAbs/p4', f'{mean(abs(x) for x in central_vals)/(p**4):.8g}')
    # 展示中心化组合中各 j 项平均，观察大项抵消
    print('central terms by j')
    from math import comb
    for j in range(5):
        term = comb(4, j) * ((-p) ** (4 - j)) * mean(sums[j])
        print(j, f'{term:.10g}', f'{term/(p**4):.8g}')

if __name__ == '__main__':
    main()
