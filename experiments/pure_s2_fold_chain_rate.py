#!/usr/bin/env python3
"""纯 S2 折返链数量增长率扫描。

对 q∈(B,2B] prime 且 q-2 prime 的集合 A，纯链基本为 A 的有序不同配对。
输出 |A| 与 |A|^2 量级，验证 Brun 上界形态 |A| << B/log^2 B。

用法示例：
  python3 experiments/pure_s2_fold_chain_rate.py --Ps 1009,2003,4001,8009,16001,32003,64007
"""
import argparse
import math

from high_threshold_margin_fast import sieve, primes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='1009,2003,4001,8009,16001,32003,64007')
    args = ap.parse_args()
    print('P B A chainOrdered A_over_B_log2 chain_over_B2_log4')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        flags = sieve(2 * B + 10)
        qs = [q for q in primes(flags, 2 * B + 10) if B < q <= 2 * B and q - 2 > B and flags[q - 2]]
        A = len(qs)
        chain = A * (A - 1)
        logB = math.log(max(B, 3))
        print(P, B, A, chain, f'{A * logB * logB / B:.3f}', f'{chain * logB**4 / (B*B):.3f}', qs[:12])


if __name__ == '__main__':
    main()
