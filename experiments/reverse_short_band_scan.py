#!/usr/bin/env python3
"""反向短带并集界扫描。

旧块级界：
    U_old = X/M * W_S
其中 W_S=sum_B 1/L_extra(B)，M=2310。

短带反向计数的粗严格形态：
    U_band <= (sum_{prime P<=X} P)/M * W_S
若不使用素数求和，可用 X(X+1)/(2M)*W_S。

注意：因为 sum P 约 X^2/(2 log X)，这个界通常比 U_old 大约 X/2 倍，
因此它不是替代旧界的强化；它只对 L>X^2 的“每骨架至多一”分析有结构意义。

用法示例：
    python3 experiments/reverse_short_band_scan.py --X 10000000 --c 1213 --params 100:55,180:120,220:154
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from skeleton_union_bound import M, q_options, union_weight_dp

RHO = 480 / 2310


def scan_one(c, W, S, X, prime_sum):
    holes = holes_for_c(c, W)
    opts = q_options(holes)
    weight = union_weight_dp(opts, S)
    old_block = X * weight / M
    band_prime = prime_sum * weight / M
    band_integer = (X * (X + 1) / 2) * weight / M
    windows = max(1, math.floor(RHO * X) - W + 1)
    return {
        'W': W,
        'S': S,
        'D': max(holes) - min(holes),
        'qopts': len(opts),
        'weight': weight,
        'old_block': old_block,
        'old_total': windows * old_block,
        'band_prime': band_prime,
        'band_prime_total': windows * band_prime,
        'band_integer': band_integer,
        'windows': windows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--params', default='100:55,180:120,220:154,260:188')
    args = parser.parse_args()
    primes = primes_upto(args.X)
    prime_sum = sum(primes)
    print('X c piX sumPrime', args.X, args.c, len(primes), prime_sum)
    print('W S D qopts weight old_block old_total band_prime band_prime_total ratio_band_old')
    for item in args.params.split(','):
        W, S = [int(x) for x in item.split(':')]
        row = scan_one(args.c, W, S, args.X, prime_sum)
        ratio = row['band_prime'] / row['old_block'] if row['old_block'] else math.inf
        print(
            W, S, row['D'], row['qopts'],
            f"{row['weight']:.6g}",
            f"{row['old_block']:.6g}",
            f"{row['old_total']:.6g}",
            f"{row['band_prime']:.6g}",
            f"{row['band_prime_total']:.6g}",
            f"{ratio:.6g}",
            flush=True,
        )


if __name__ == '__main__':
    main()
