#!/usr/bin/env python3
"""§234 Brun-Buchstab 半线性筛严格化 H_P 行方向.

实证关键量:
1. S(P, √P) = #{N ∈ [(i-1)P+1, iP] : q_min(N) > √P} (√P-粗数)
2. |R_i| = #{N ∈ S : N 合数} (√P-粗合数)
3. 行内素数数 = #{N : N 是素数} = S - |R_i|

Brun-Buchstab 渐近预测:
- S(P, √P) ~ 2 log 2 · P / log P ≈ 1.386 P/log P
- |R_i| ~ (2 log 2 - 1) · P / log P ≈ 0.386 P/log P
- 素数数 ~ P / log P (PNT)

实证目标:
- 验证 Brun-Buchstab 估计精度
- 找具体 P_0 使 |R_i| 严格 < S(P, √P), 即素数 ≥ 1
- 计算严格 H_P 行方向的具体 P_0 阈值

用法:
    python3 experiments/brun_buchstab_certificate.py --maxP 5000
"""
import argparse
import math
import sys
from typing import List, Tuple


def sieve_eratosthenes(N: int) -> List[bool]:
    is_p = [True] * (N + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, N + 1, i):
                is_p[j] = False
    return is_p


def is_prime_simple(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True


def smallest_prime_factor(n: int) -> int:
    if n < 2: return n
    if n % 2 == 0: return 2
    for p in range(3, int(n**0.5) + 2, 2):
        if n % p == 0: return p
    return n


def analyze_row_BB(P: int, i: int, sieve: List[bool]) -> Tuple[int, int, int]:
    """行 i 内 (S, |R_i|, 素数数) 计算."""
    sqrt_P = math.isqrt(P)
    S = 0
    R_count = 0
    prime_count = 0
    for j in range(1, P + 1):
        N = (i - 1) * P + j
        if N < 2: continue
        if sieve[N]:  # 是素数
            S += 1  # 素数也是 √P-粗
            prime_count += 1
        else:
            spf = smallest_prime_factor(N)
            if spf > sqrt_P:
                S += 1
                R_count += 1
    return S, R_count, prime_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=2003)
    parser.add_argument('--samples', default='101,251,503,1009,2003')
    args = parser.parse_args()

    sample_Ps = [int(x) for x in args.samples.split(',')]
    sample_Ps = [P for P in sample_Ps if P <= args.maxP]

    sys.stdout.write(f'§234 Brun-Buchstab 实证 P ≤ {args.maxP}\n\n')

    sys.stdout.write(f'{"P":>5} {"行 i":>5} {"S":>5} {"|R_i|":>6} {"素数":>5} '
                     f'{"S/(P/logP)":>11} {"|R|/(P/logP)":>13} {"素数/(P/logP)":>14}\n')

    for P in sample_Ps:
        if not is_prime_simple(P): continue
        sieve = sieve_eratosthenes(P * P)
        sqrt_P = math.isqrt(P)
        log_P = math.log(P)
        unit = P / log_P  # P/log P 单位

        # 测试几个代表行
        test_rows = [1, 2, P // 4, P // 2, P]
        for i in test_rows:
            S, R, primes = analyze_row_BB(P, i, sieve)
            S_norm = S / unit
            R_norm = R / unit
            P_norm = primes / unit
            sys.stdout.write(f'{P:>5} {i:>5} {S:>5} {R:>6} {primes:>5} '
                             f'{S_norm:>11.3f} {R_norm:>13.3f} {P_norm:>14.3f}\n')
        sys.stdout.write('\n')

    sys.stdout.write(f'=== Brun-Buchstab 渐近预测 ===\n')
    sys.stdout.write(f'S(P, √P) ~ 2 log 2 ≈ 1.386 (单位 P/log P)\n')
    sys.stdout.write(f'|R_i|     ~ 2 log 2 - 1 ≈ 0.386\n')
    sys.stdout.write(f'素数数    ~ 1.0 (PNT)\n')
    sys.stdout.write(f'\n严格 H_P 行方向: 素数 = S - |R| ≥ 1, 即 |R| < S\n')

    # 全 P 行扫描找最坏 (R/S 比例最高) 行
    sys.stdout.write(f'\n=== 全 P 行扫描: 最坏 |R|/S 比 ===\n')
    sys.stdout.write(f'{"P":>5} {"max |R|/S":>12} {"min 素数":>10} {"最坏行 i":>10}\n')
    for P in sample_Ps:
        if not is_prime_simple(P): continue
        sieve = sieve_eratosthenes(P * P)
        max_ratio = 0
        max_i = 0
        min_primes = P + 1
        worst_i = 0
        for i in range(1, P + 1):
            S, R, primes = analyze_row_BB(P, i, sieve)
            if S > 0:
                ratio = R / S
                if ratio > max_ratio:
                    max_ratio = ratio
                    max_i = i
            if primes < min_primes:
                min_primes = primes
                worst_i = i
        sys.stdout.write(f'{P:>5} {max_ratio:>12.4f} {min_primes:>10} {worst_i:>10}\n')


if __name__ == '__main__':
    main()
