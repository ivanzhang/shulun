#!/usr/bin/env python3
"""检验二点奇异级数加权平均的增长。

模型比值 S2(d)=prod_{q<=y} local_pair(q,d)/(1-1/q)^2。
当 d 为奇数且 q=2 不整除 d 时，local_pair=0。
目标观察 sum_{d<P} (P-d)(S2(d)-1) 的大小。
"""
import argparse
import math
from statistics import mean
from high_threshold_margin_fast import sieve, primes


def factor_distinct(n, root):
    out = []
    x = n
    for q in root:
        if q * q > x:
            break
        if x % q == 0:
            out.append(q)
            while x % q == 0:
                x //= q
    if x > 1:
        out.append(x)
    return out


def base_constant(small):
    # 对偶数 d：q=2 局部比为 2；奇素数未碰撞基线为 (1-2/q)/(1-1/q)^2。
    c = 1.0
    for q in small:
        if q == 2:
            c *= 2.0
        else:
            c *= (1 - 2 / q) / ((1 - 1 / q) ** 2)
    return c


def s2_ratio_from_factors(d, small_set, c0):
    if d % 2:
        return 0.0
    ratio = c0
    for q in factor_distinct(d, []):
        if q != 2 and q in small_set:
            # 从未碰撞局部 (1-2/q) 改为碰撞局部 (1-1/q)
            ratio *= ((1 - 1 / q) / (1 - 2 / q))
    return ratio


def s2_ratio_direct(d, small):
    ratio = 1.0
    for q in small:
        single = 1 - 1 / q
        if d % q == 0:
            pair = 1 - 1 / q
        else:
            pair = 1 - 2 / q
            if pair <= 0:
                return 0.0
        ratio *= pair / (single * single)
    return ratio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003,4001,8009')
    ap.add_argument('--c', type=float, default=0.8)
    ap.add_argument('--top', type=int, default=8)
    args = ap.parse_args()
    print('P y pi_y avgS weightedExcess weightedExcess/(PlogP) absWeighted/(PlogP) maxS maxD')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        flags = sieve(P)
        root = primes(flags, P)
        y = int(args.c * P)
        small = [q for q in root if q <= y]
        values = []
        weighted = 0.0
        abs_weighted = 0.0
        maxS = -1.0
        maxD = None
        # 直接计算，P<=数万足够快
        for d in range(1, P):
            s = s2_ratio_direct(d, small)
            values.append(s)
            term = (P - d) * (s - 1)
            weighted += term
            abs_weighted += abs(term)
            if s > maxS:
                maxS, maxD = s, d
        denom = P * math.log(P)
        print(f'{P} {y} {len(small)} {mean(values):.6f} {weighted:.3f} {weighted/denom:.6f} {abs_weighted/denom:.6f} {maxS:.3f} {maxD}')
        top_rows = sorted(((s, d) for d, s in enumerate(values, start=1)), reverse=True)[:args.top]
        print(' topS', ', '.join(f'd={d}:S={s:.2f}' for s, d in top_rows))


if __name__ == '__main__':
    main()
