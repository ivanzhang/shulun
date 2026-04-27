#!/usr/bin/env python3
"""§231 H_P 综合证书 - 行 + 列 + 多斜率对角线实证.

把 §206 元层面框架 (任意几何 R 形状) 落地到具体实证. 对每 P 验证:

1. **行方向**: A_{i,j} = (i-1)P + j, 行 i ∈ [1, P]
2. **列方向**: A_{i,j} = (i-1)P + j, 列 j ∈ [1, P]
3. **主对角线**: A_{i,i} = 1 + (i-1)(P+1), i ∈ [1, P]
4. **反对角线**: A_{i, P+1-i} = (i-1)P + P+1-i = i(P-1) + 1, i ∈ [1, P]
5. **偏斜线 (斜率 k)**: A_{i, ((i-1)*k mod P) + 1}, k ∈ [2, k_max]

每个方向都是 P×P 方阵的"几何刚性子集 R", 长度 P.

H_P 综合: 对所有几何 R 形状, P×P 方阵的 R 含素数.

用法:
    python3 experiments/unified_HP_certificate.py --maxP 1009 --slopes 1,2,3
"""
import argparse
import math
import sys
from typing import List, Tuple


def sieve_eratosthenes(N: int) -> List[bool]:
    """[0, N] 内素数布尔表."""
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


def check_row(P: int, sieve: List[bool]) -> Tuple[int, int, int]:
    """所有 P 行是否都含素数. 返回 (含素数行数, 最坏行 i, 最坏行素数数)."""
    rows_with_prime = 0
    worst_i = 0
    worst_prime_count = P + 1
    for i in range(1, P + 1):
        cnt = sum(1 for j in range(1, P + 1) if sieve[(i-1)*P + j])
        if cnt > 0:
            rows_with_prime += 1
        if cnt < worst_prime_count:
            worst_prime_count = cnt
            worst_i = i
    return rows_with_prime, worst_i, worst_prime_count


def check_col(P: int, sieve: List[bool]) -> Tuple[int, int, int]:
    """所有 P 列是否都含素数."""
    cols_with_prime = 0
    worst_j = 0
    worst_count = P + 1
    for j in range(1, P + 1):
        cnt = sum(1 for i in range(1, P + 1) if sieve[(i-1)*P + j])
        if cnt > 0:
            cols_with_prime += 1
        if cnt < worst_count:
            worst_count = cnt
            worst_j = j
    return cols_with_prime, worst_j, worst_count


def check_diagonal(P: int, sieve: List[bool]) -> int:
    """主对角线 A_{i,i} = 1 + (i-1)(P+1)."""
    cnt = sum(1 for i in range(1, P + 1) if sieve[1 + (i-1)*(P+1)] if 1 + (i-1)*(P+1) <= P*P)
    return cnt


def check_anti_diagonal(P: int, sieve: List[bool]) -> int:
    """反对角线 A_{i, P+1-i} = (i-1)P + P+1-i = i(P-1) + 1."""
    cnt = 0
    for i in range(1, P + 1):
        N = (i-1)*P + (P+1-i)
        if 1 <= N <= P*P and sieve[N]:
            cnt += 1
    return cnt


def check_slope_line(P: int, k: int, sieve: List[bool]) -> int:
    """偏斜率 k: A_{i, j} where j = ((i-1)*k mod P) + 1, i ∈ [1, P]."""
    cnt = 0
    seen = set()
    for i in range(1, P + 1):
        j = ((i-1)*k) % P + 1
        N = (i-1)*P + j
        if N in seen:
            continue
        seen.add(N)
        if 1 <= N <= P*P and sieve[N]:
            cnt += 1
    return cnt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=1009)
    parser.add_argument('--samples', default='101,251,503,1009,2003')
    parser.add_argument('--slopes', default='1,2,3,5')
    args = parser.parse_args()

    sample_Ps = [int(x) for x in args.samples.split(',')]
    sample_Ps = [P for P in sample_Ps if P <= args.maxP]
    slopes = [int(x) for x in args.slopes.split(',')]

    sys.stdout.write(f'§231 H_P 综合证书: 行 + 列 + 对角线 + 偏斜线\n')
    sys.stdout.write(f'P 测试: {sample_Ps}, 斜率: {slopes}\n\n')

    sys.stdout.write(f'{"P":>5} {"行(全/总)":>10} {"列(全/总)":>10} '
                     f'{"主对角线":>9} {"反对角线":>9} ')
    for k in slopes:
        sys.stdout.write(f'{f"slope={k}":>9} ')
    sys.stdout.write('\n')

    summary = {'rows_full': 0, 'cols_full': 0,
               'diag_full': 0, 'antidiag_full': 0,
               'slope_full': {k: 0 for k in slopes}}

    for P in sample_Ps:
        if not is_prime_simple(P):
            continue
        sys.stdout.write(f'sieve N=P²={P*P}...')
        sys.stdout.flush()
        sieve = sieve_eratosthenes(P * P)
        sys.stdout.write(' done. ')
        sys.stdout.flush()

        # Row
        rows_p, worst_i, worst_prime = check_row(P, sieve)
        # Col
        cols_p, worst_j, worst_col_prime = check_col(P, sieve)
        # Diagonals
        diag = check_diagonal(P, sieve)
        antidiag = check_anti_diagonal(P, sieve)
        slope_results = {k: check_slope_line(P, k, sieve) for k in slopes}

        rows_str = f'{rows_p}/{P}'
        cols_str = f'{cols_p}/{P}'

        sys.stdout.write(f'\n{P:>5} {rows_str:>10} {cols_str:>10} '
                         f'{diag:>9} {antidiag:>9} ')
        for k in slopes:
            sys.stdout.write(f'{slope_results[k]:>9} ')
        sys.stdout.write('\n')
        sys.stdout.write(f'      最坏行 i={worst_i} 素数数={worst_prime}, '
                         f'最坏列 j={worst_j} 素数数={worst_col_prime}\n')
        sys.stdout.flush()

        if rows_p == P:
            summary['rows_full'] += 1
        if cols_p == P:
            summary['cols_full'] += 1
        if diag > 0:
            summary['diag_full'] += 1
        if antidiag > 0:
            summary['antidiag_full'] += 1
        for k in slopes:
            if slope_results[k] > 0:
                summary['slope_full'][k] += 1

    n_p = sum(1 for P in sample_Ps if is_prime_simple(P))
    sys.stdout.write(f'\n=== H_P 综合证书总结 ===\n')
    sys.stdout.write(f'测试 P 数: {n_p}\n')
    sys.stdout.write(f'★ 行方向全部 {n_p} 个 P 严格成立: {summary["rows_full"] == n_p}\n')
    sys.stdout.write(f'★ 列方向全部 {n_p} 个 P 严格成立: {summary["cols_full"] == n_p}\n')
    sys.stdout.write(f'★ 主对角线全部 P 含素数: {summary["diag_full"] == n_p}\n')
    sys.stdout.write(f'★ 反对角线全部 P 含素数: {summary["antidiag_full"] == n_p}\n')
    for k in slopes:
        sys.stdout.write(f'★ 斜率 {k} 线全部 P 含素数: {summary["slope_full"][k] == n_p}\n')


if __name__ == '__main__':
    main()
