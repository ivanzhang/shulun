#!/usr/bin/env python3
"""检验四点中心化核的一阶/二阶投影退化。

固定部分坐标，对剩余坐标平均中心化核 K(R)=sum_S (-p)^(4-|S|)P(S)。
若一阶投影近 0，则 P^3 单碰撞层应消失；二阶投影对应配对主项。
"""
import argparse
import random
from statistics import mean, pstdev
from high_threshold_margin_fast import sieve, primes


def prob_subset(vals, small):
    if not vals:
        return 1.0
    prob = 1.0
    for q in small:
        nu = len({v % q for v in vals})
        if nu >= q:
            return 0.0
        prob *= 1 - nu / q
    return prob


def kernel(R, small, p):
    total = 0.0
    for mask in range(16):
        vals = [R[i] for i in range(4) if (mask >> i) & 1]
        total += ((-p) ** (4 - len(vals))) * prob_subset(vals, small)
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=1009)
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--outer-samples', type=int, default=80)
    ap.add_argument('--inner-samples', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=1)
    args = ap.parse_args()
    random.seed(args.seed)
    flags = sieve(args.P)
    root = primes(flags, args.P)
    small = [q for q in root if q <= int(args.c * args.P)]
    p = prob_subset([0], small)
    p4 = p ** 4

    one_proj = []
    two_proj = []
    two_diag_proj = []
    for _ in range(args.outer_samples):
        r0 = random.randrange(args.P)
        vals = []
        for _ in range(args.inner_samples):
            rest = random.sample(range(args.P), 3)
            vals.append(kernel([r0] + rest, small, p))
        one_proj.append(mean(vals) / p4)

        a, b = random.sample(range(args.P), 2)
        vals = []
        for _ in range(args.inner_samples):
            rest = random.sample(range(args.P), 2)
            vals.append(kernel([a,b] + rest, small, p))
        two_proj.append(mean(vals) / p4)

        # 强相关二点：令 b=a+d，d取小偶数，观察二阶投影是否显著。
        d = random.choice([2,4,6,10,12,30,60,210])
        a = random.randrange(args.P - d)
        b = a + d
        vals = []
        for _ in range(args.inner_samples):
            rest = random.sample(range(args.P), 2)
            vals.append(kernel([a,b] + rest, small, p))
        two_diag_proj.append(mean(vals) / p4)

    print(f'P={args.P} p={p:.8g} p4={p4:.8g} outer={args.outer_samples} inner={args.inner_samples}')
    for name, arr in [('one', one_proj), ('two_random', two_proj), ('two_corr', two_diag_proj)]:
        print(name, 'mean', f'{mean(arr):.6g}', 'std', f'{pstdev(arr):.6g}', 'maxAbs', f'{max(abs(x) for x in arr):.6g}')

if __name__ == '__main__':
    main()
