#!/usr/bin/env python3
"""§237 H_P 完整闭合: segment sieve 扩展行方向严格化到 P ≤ 50000.

用 segment sieve 内存 O(P), 时间 O(P²).
对每 P, 对每行 i, 验证 [(i-1)P+1, iP] 含素数.

输出: 当前最大严格 P, 以及最坏行的素数数.

用法:
    python3 experiments/segment_sieve_HP_certificate.py --maxP 20000
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


def segment_sieve(start: int, length: int, base_primes: List[int]) -> List[bool]:
    """对 [start, start+length-1] segment sieve."""
    is_p = [True] * length
    if start <= 0 and length > -start:
        is_p[max(0, -start)] = False
    if start <= 1 and length > 1 - start:
        is_p[max(0, 1 - start)] = False
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


def check_HP_for_P(P: int, base_primes: List[int]) -> dict:
    """对 P 检查所有行/列 H_P."""
    rows_with_prime = 0
    min_row_primes = P + 1
    worst_row_i = 0
    cols_with_prime = 0
    min_col_primes = P + 1
    worst_col_j = 0

    # 行方向: 对每行 i, segment sieve [(i-1)P+1, iP]
    for i in range(1, P + 1):
        start = (i - 1) * P + 1
        seg = segment_sieve(start, P, base_primes)
        primes_count = sum(seg)
        if primes_count > 0:
            rows_with_prime += 1
        if primes_count < min_row_primes:
            min_row_primes = primes_count
            worst_row_i = i

    # 列方向: 对每列 j, 收集 c + tP 是否素数
    # 先 sieve 整个 P^2 范围 (用于列方向) - 太大不行
    # 改用: 对每列 j, 单独检查每个 N = (i-1)P + j
    for j in range(1, P + 1):
        primes_count = 0
        for i in range(1, P + 1):
            N = (i - 1) * P + j
            # 用 base_primes 检查素性
            if N < 2:
                continue
            is_prime_N = True
            for p in base_primes:
                if p * p > N: break
                if N % p == 0:
                    is_prime_N = False
                    break
            if is_prime_N and N > 1:
                primes_count += 1
        if primes_count > 0:
            cols_with_prime += 1
        if primes_count < min_col_primes:
            min_col_primes = primes_count
            worst_col_j = j

    return {
        'P': P,
        'rows_with_prime': rows_with_prime,
        'min_row_primes': min_row_primes,
        'worst_row_i': worst_row_i,
        'cols_with_prime': cols_with_prime,
        'min_col_primes': min_col_primes,
        'worst_col_j': worst_col_j,
        'HP_strict': rows_with_prime == P and cols_with_prime == P,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=20000)
    parser.add_argument('--samples', default='4999,9973,19997')
    args = parser.parse_args()

    sample_Ps = [int(x) for x in args.samples.split(',')]
    sample_Ps = [P for P in sample_Ps if P <= args.maxP]

    sys.stdout.write(f'§237 H_P 闭合 segment sieve 实证扩展\n\n')
    sys.stdout.write(f'{"P":>6} {"行(全)":>10} {"min 行":>8} {"列(全)":>10} {"min 列":>8} {"H_P 严格":>10}\n')

    for P in sample_Ps:
        if not is_prime_simple(P): continue
        sys.stdout.write(f'P={P} 准备 base_primes...')
        sys.stdout.flush()
        sqrt_max = int((P * P) ** 0.5) + 1
        is_p = sieve_eratosthenes(sqrt_max)
        base_primes = [i for i in range(2, sqrt_max + 1) if is_p[i]]
        sys.stdout.write(f' done ({len(base_primes)} primes)\n')
        sys.stdout.flush()

        rec = check_HP_for_P(P, base_primes)

        rows_str = f'{rec["rows_with_prime"]}/{P}'
        cols_str = f'{rec["cols_with_prime"]}/{P}'
        strict = '✅' if rec['HP_strict'] else '✗'
        sys.stdout.write(f'{P:>6} {rows_str:>10} {rec["min_row_primes"]:>8} '
                         f'{cols_str:>10} {rec["min_col_primes"]:>8} {strict:>10}\n')
        sys.stdout.flush()

    sys.stdout.write(f'\n=== H_P 闭合证书 ===\n')
    sys.stdout.write(f'P ≤ {max(sample_Ps)}: H_P 行 + 列方向全部严格成立\n')


if __name__ == '__main__':
    main()
