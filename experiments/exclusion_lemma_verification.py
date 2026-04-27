#!/usr/bin/env python3
"""§228 大因子互斥引理数值验证 (新版本)。

验证内容:
1. 引理本身: 距离 < √P 的两 √P-粗合数不共享 > √P 因子
2. |R| 上界: 平均 |R|, |R| ≤ P log 2 (经典) vs |R| ≤ P log 2 / 2 (互斥改进)
3. (R, q) 对计数: 单 R 元素 ≥ 2 因子 → 总对数 ≥ 2|R|

用法:
    python3 experiments/exclusion_lemma_verification.py --P 1009
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True


def factor_distinct(n: int) -> list:
    if n < 2: return []
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def smallest_prime_factor(n: int) -> int:
    if n < 2: return n
    if n % 2 == 0: return 2
    for p in range(3, int(n**0.5) + 2, 2):
        if n % p == 0: return p
    return n


def analyze_row(P: int, i: int, sqrt_P: int) -> dict:
    """行 i 的 A/R 分类与因子结构"""
    A_set = []
    R_set = []
    primes_set = []
    for j in range(1, P + 1):
        N = (i - 1) * P + j
        if N < 2:
            continue
        spf = smallest_prime_factor(N)
        if spf == N:
            primes_set.append((j, N))
            continue
        if spf <= sqrt_P:
            A_set.append((j, N, spf))
        else:
            R_set.append((j, N, spf))
    return {'A': A_set, 'R': R_set, 'primes': primes_set}


def check_exclusion(R_set, sqrt_P: int) -> int:
    """检查互斥引理: 距离 < √P 的两 R 元素不共享 > √P 因子"""
    R_factors = []
    for j, N, _ in R_set:
        f = factor_distinct(N)
        large_f = set(p for p in f if p > sqrt_P)
        R_factors.append((j, large_f))

    violations = 0
    for a in range(len(R_factors)):
        for b in range(a + 1, len(R_factors)):
            j1, f1 = R_factors[a]
            j2, f2 = R_factors[b]
            if abs(j1 - j2) < sqrt_P:
                if f1 & f2:
                    violations += 1
    return violations


def count_factor_pairs(R_set, sqrt_P: int) -> int:
    """计 (N, q) 对: q | N, q > √P, N ∈ R"""
    pair_count = 0
    for j, N, _ in R_set:
        f = factor_distinct(N)
        for q in f:
            if q > sqrt_P:
                pair_count += 1
    return pair_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=1009)
    parser.add_argument('--maxRows', type=int, default=None)
    args = parser.parse_args()

    P = args.P
    if not is_prime(P):
        sys.stderr.write(f'警告: P={P} 不是素数\n')

    sqrt_P = math.isqrt(P)
    rows_to_scan = min(args.maxRows or P, P)

    sys.stdout.write(f'§228 大因子互斥引理实证 P={P}, √P ≈ {sqrt_P}\n')
    sys.stdout.write(f'扫描 {rows_to_scan} 行\n\n')

    total_violations = 0
    total_R = 0
    total_pairs = 0
    max_R = 0
    sum_total_composite = 0

    for i in range(1, rows_to_scan + 1):
        rec = analyze_row(P, i, sqrt_P)
        A = rec['A']
        R = rec['R']
        violations = check_exclusion(R, sqrt_P)
        pairs = count_factor_pairs(R, sqrt_P)

        if len(R) > max_R:
            max_R = len(R)
        total_R += len(R)
        total_pairs += pairs
        total_violations += violations
        sum_total_composite += len(A) + len(R)

    sys.stdout.write('=== 互斥引理验证 ===\n')
    sys.stdout.write(f'总扫描行数: {rows_to_scan}\n')
    sys.stdout.write(f'总互斥引理违例数: {total_violations}\n')
    if total_violations == 0:
        sys.stdout.write(f'★ 互斥引理在 P={P} 全 {rows_to_scan} 行验证通过\n')
    sys.stdout.write('\n')

    sys.stdout.write('=== |R| 统计 ===\n')
    avg_R = total_R / rows_to_scan
    sys.stdout.write(f'最大 |R|: {max_R}\n')
    sys.stdout.write(f'平均 |R|: {avg_R:.2f}\n')
    sys.stdout.write(f'平均 |R| / P: {avg_R / P:.4f}\n')
    sys.stdout.write('\n')

    sys.stdout.write('=== |R| 上界比较 ===\n')
    sys.stdout.write(f'经典 P · log 2: {P * math.log(2):.1f}\n')
    sys.stdout.write(f'互斥改进 P · log 2 / 2: {P * math.log(2) / 2:.1f}\n')
    sys.stdout.write(f'平凡上界 P: {P}\n')
    sys.stdout.write('\n')

    sys.stdout.write('=== (R, q) 对计数 ===\n')
    avg_pairs = total_pairs / rows_to_scan
    sys.stdout.write(f'平均 (R, q) 对数: {avg_pairs:.2f}\n')
    sys.stdout.write(f'平均 2|R|: {2 * avg_R:.2f}\n')
    sys.stdout.write(f'平均比值 (对数 / |R|): {avg_pairs / max(1, avg_R):.3f} (≥ 2 期望)\n')
    sys.stdout.write('\n')

    sys.stdout.write('=== |A| + |R| 总合数 ===\n')
    avg_total = sum_total_composite / rows_to_scan
    sys.stdout.write(f'平均合数数: {avg_total:.1f} ({avg_total/P:.4f} P)\n')
    sys.stdout.write(f'平均素数数: {P - avg_total:.1f} ({(P-avg_total)/P:.4f} P)\n')


if __name__ == '__main__':
    main()
