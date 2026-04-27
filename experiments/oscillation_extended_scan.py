#!/usr/bin/env python3
"""§230 局部振荡引理大规模实证 - 用 sieve 加速到 P ≤ 50000.

对每个 P, 用 sieve 一次性筛出 [1, P²] 内素数, 然后对每行 i 计算 max gap.
比之前 P=4999 trial division 快百倍.

关键测量:
- 实证 C₀ ≈ max gap / √P 随 P 的趋势
- 实证 C₀ * = max gap / log² P 的稳定性
- 给出局部振荡引理"近 √P"的实证范围

用法:
    python3 experiments/oscillation_extended_scan.py --maxP 10000
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


def sieve_segment(start: int, length: int, base_primes: List[int]) -> List[bool]:
    """对 [start, start+length-1] 做 segment sieve."""
    is_p = [True] * length
    if start == 0:
        is_p[0] = False
        if length > 1:
            is_p[1] = False
    elif start == 1:
        is_p[0] = False
    for p in base_primes:
        if p * p > start + length:
            break
        first = max(p * p, ((start + p - 1) // p) * p)
        for j in range(first, start + length, p):
            is_p[j - start] = False
    return is_p


def is_prime_simple(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True


def max_gap_for_P(P: int, base_primes: List[int]) -> tuple:
    """对每个 P, 跑全 P 行, 找 max gap (连续合数最长串)."""
    overall_max = 0
    overall_max_i = 0
    overall_max_pos = 0
    for i in range(1, P + 1):
        start = (i - 1) * P + 1
        is_p_seg = sieve_segment(start, P, base_primes)
        cur = 0
        for k, p in enumerate(is_p_seg):
            if p:
                cur = 0
            else:
                cur += 1
                if cur > overall_max:
                    overall_max = cur
                    overall_max_i = i
                    overall_max_pos = start + k
    return overall_max, overall_max_i, overall_max_pos


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=10000)
    parser.add_argument('--samples', default='101,251,503,1009,2003,4999,9973')
    args = parser.parse_args()

    sample_Ps = [int(x) for x in args.samples.split(',')]
    sample_Ps = [P for P in sample_Ps if P <= args.maxP]

    sys.stdout.write(f'§230 局部振荡引理大规模实证 (sieve 加速)\n')
    sys.stdout.write(f'P 测试: {sample_Ps}\n\n')

    sys.stdout.write(f'{"P":>6} {"P²":>10} {"sqrt P":>8} {"max gap":>9} {"行 i":>6} '
                     f'{"位置 N":>10} {"gap/√P":>8} {"gap/log²P":>10}\n')

    max_C_sqrt = 0
    max_C_log2 = 0
    for P in sample_Ps:
        if not is_prime_simple(P):
            continue
        # 构造小素数表 (筛 base, ≤ √(P²) = P)
        sqrt_max = int((P * P) ** 0.5) + 1
        is_p = sieve_eratosthenes(sqrt_max)
        base_primes = [i for i in range(2, sqrt_max + 1) if is_p[i]]

        max_g, max_i, max_pos = max_gap_for_P(P, base_primes)
        sqrt_P = math.sqrt(P)
        log2P = math.log(P) ** 2
        ratio_sqrt = max_g / sqrt_P
        ratio_log2 = max_g / log2P
        if ratio_sqrt > max_C_sqrt:
            max_C_sqrt = ratio_sqrt
        if ratio_log2 > max_C_log2:
            max_C_log2 = ratio_log2

        sys.stdout.write(f'{P:>6} {P*P:>10} {sqrt_P:>8.1f} {max_g:>9} {max_i:>6} '
                         f'{max_pos:>10} {ratio_sqrt:>8.3f} {ratio_log2:>10.3f}\n')
        sys.stdout.flush()

    sys.stdout.write(f'\n=== 总结 ===\n')
    sys.stdout.write(f'实证 max gap / √P 上界 C₀ ≤ {max_C_sqrt:.3f}\n')
    sys.stdout.write(f'实证 max gap / log² P 上界 C₀* ≤ {max_C_log2:.3f}\n')
    sys.stdout.write(f'\n振荡引理形式 1: 长度 ≥ {max_C_sqrt:.1f} √P 列段含素数 (实证)\n')
    sys.stdout.write(f'振荡引理形式 2: 长度 ≥ {max_C_log2:.1f} log² P 列段含素数 (实证, Cramér 形式)\n')


if __name__ == '__main__':
    main()
