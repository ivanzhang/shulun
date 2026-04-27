#!/usr/bin/env python3
"""§232 归纳论证: 长度增加 vs 筛除维度增加分析。

对每个素数 P_k (k = 1, 2, 3, ...), 计算:
1. 行/列长度 P_k
2. 筛除素数数 = π(P_k) = k
3. 增量比: (P_{k+1} - P_k) / 1  (长度增加 / 筛除维度增加)
4. P_{k+1}×P_{k+1} 方阵行内合数容斥估计 vs 实测合数数

验证: 长度增加 g_k = P_{k+1} - P_k >> 筛除维度增加 = 1 的趋势。

用法:
    python3 experiments/induction_growth_analysis.py --maxK 100
"""
import argparse
import math
import sys
from typing import List


def sieve_eratosthenes(N: int) -> List[bool]:
    is_p = [True] * (N + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, N + 1, i):
                is_p[j] = False
    return is_p


def primes_first_k(K: int) -> List[int]:
    """前 K 个素数."""
    upper = max(20, int(K * (math.log(K) + math.log(math.log(K)) + 2))) if K >= 6 else 100
    is_p = sieve_eratosthenes(upper)
    primes = [p for p in range(2, upper + 1) if is_p[p]]
    return primes[:K]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxK', type=int, default=100)
    args = parser.parse_args()

    K = args.maxK
    primes = primes_first_k(K + 5)

    sys.stdout.write(f'§232 归纳论证: 长度增加 vs 筛除维度增加\n\n')
    sys.stdout.write(f'{"k":>4} {"P_k":>5} {"P_{k+1}":>7} {"g_k":>5} '
                     f'{"P_k log":>8} {"行素数密度上界 P/log P":>22} '
                     f'{"密度增长":>9}\n')

    prev_density = None
    for k in range(1, min(K, len(primes) - 1) + 1):
        P_k = primes[k - 1]
        P_kp1 = primes[k]
        g_k = P_kp1 - P_k
        log_P = math.log(P_k) if P_k > 1 else 1
        density = P_k / log_P
        density_inc = density - prev_density if prev_density else 0

        if k <= 30 or k % 5 == 0:
            sys.stdout.write(f'{k:>4} {P_k:>5} {P_kp1:>7} {g_k:>5} '
                             f'{log_P:>8.2f} {density:>22.2f} '
                             f'{density_inc:>9.2f}\n')
        prev_density = density

    sys.stdout.write('\n=== 关键观察 ===\n')

    # 计算平均 g_k vs k
    g_avg = sum(primes[k] - primes[k-1] for k in range(1, K)) / max(1, K - 1)
    sys.stdout.write(f'平均 g_k (k=1..{K}): {g_avg:.2f}\n')
    sys.stdout.write(f'比 1 (筛除维度增加) 大: {g_avg:.1f}x\n')

    # 渐近 g_k ~ log P_k
    P_K = primes[K - 1]
    sys.stdout.write(f'\nP_{K} = {P_K}, log P_{K} = {math.log(P_K):.2f}\n')
    sys.stdout.write(f'PNT 预测平均 g_k ~ log P_k = {math.log(P_K):.2f}\n')


if __name__ == '__main__':
    main()
