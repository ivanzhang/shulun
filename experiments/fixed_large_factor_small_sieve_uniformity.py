#!/usr/bin/env python3
"""固定粗因子同余条件后，检验小模数筛剩余密度是否仍为乘积型。

模型：固定 P、窗口长度 L=C sqrt(P)、粗因子 q in (sqrt(P),L]。
对所有可形成共享边的二点模式 h2=h1+t*q（t>=1, h2<=L），统计这两个点同时避开所有 p<=sqrt(P) 的比例。
比较基准 p_B^2，并按 q 层/距离层输出。

用法示例：
  python3 experiments/fixed_large_factor_small_sieve_uniformity.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import sieve, primes


def bucket_q(q, B):
    ratio = q / B
    if ratio <= 1.5:
        return '(1,1.5]B'
    if ratio <= 2.0:
        return '(1.5,2]B'
    if ratio <= 3.0:
        return '(2,3]B'
    return '(3,C]B'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L pB bucket patterns pass ratio ratio_over_pB2')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        small = primes(sieve(B), B)
        large_qs = [q for q in primes(sieve(L), L) if q > B]
        pB = 1.0
        for p in small:
            pB *= (1 - 1 / p)
        stats = defaultdict(lambda: [0, 0])
        # 行参数 N=(row-1)P，在模小素数下遍历 row=1..P 足够观察均匀性。
        for q in large_qs:
            bq = bucket_q(q, B)
            max_t = (L - 1) // q
            for t in range(1, max_t + 1):
                for h1 in range(1, L - t * q + 1):
                    h2 = h1 + t * q
                    for row in range(1, P + 1):
                        n1 = (row - 1) * P + h1
                        n2 = (row - 1) * P + h2
                        stats[bq][0] += 1
                        if all(n1 % p and n2 % p for p in small):
                            stats[bq][1] += 1
        for bq in ['(1,1.5]B', '(1.5,2]B', '(2,3]B', '(3,C]B']:
            total, passed = stats[bq]
            if not total:
                continue
            ratio = passed / total
            print(P, args.C, L, f'{pB:.6f}', bq, total, passed, f'{ratio:.6f}', f'{ratio/(pB*pB):.3f}')


if __name__ == '__main__':
    main()
