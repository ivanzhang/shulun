#!/usr/bin/env python3
"""§233 多层互斥引理 + 反例代数复杂度论证。

把 §228 的 √P 互斥引理推广到任意 α ∈ (0, 1/2):

> 多层互斥引理 (α): 行内距离 |c1-c2| < P^α 的两个 P^α-粗合数不共享 > P^α 因子。

实证:
1. 对不同 α, 验证多层互斥引理成立
2. 计算每层 R_α 的大小
3. 分析反例的"代数复杂度"

用法:
    python3 experiments/multilayer_exclusion.py --P 1009 --alphas 0.5,0.4,0.33,0.25
"""
import argparse
import math
import sys
from collections import defaultdict
from typing import List


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True


def factor_distinct(n: int) -> List[int]:
    if n < 2: return []
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors


def smallest_prime_factor(n: int) -> int:
    if n < 2: return n
    if n % 2 == 0: return 2
    for p in range(3, int(n**0.5) + 2, 2):
        if n % p == 0: return p
    return n


def analyze_row_layers(P: int, i: int, alphas: List[float]) -> dict:
    """对行 i 在多个 α 阈值上分析"""
    layers = {alpha: {'R': [], 'threshold': P ** alpha} for alpha in alphas}

    for j in range(1, P + 1):
        N = (i - 1) * P + j
        if N < 2: continue
        spf = smallest_prime_factor(N)
        if spf == N: continue  # 素数

        for alpha in alphas:
            threshold = P ** alpha
            if spf > threshold:
                layers[alpha]['R'].append((j, N, spf))

    return layers


def verify_multilayer_exclusion(R: list, threshold: float) -> int:
    """验证 |c1-c2| < threshold 的 R 元素不共享 > threshold 因子"""
    R_factors = []
    for j, N, _ in R:
        f = factor_distinct(N)
        large = set(p for p in f if p > threshold)
        R_factors.append((j, large))

    violations = 0
    for a in range(len(R_factors)):
        for b in range(a + 1, len(R_factors)):
            j1, f1 = R_factors[a]
            j2, f2 = R_factors[b]
            if abs(j1 - j2) < threshold:
                if f1 & f2:
                    violations += 1
    return violations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=1009)
    parser.add_argument('--alphas', default='0.5,0.4,0.33,0.25')
    parser.add_argument('--rowsToCheck', type=int, default=20)
    args = parser.parse_args()

    P = args.P
    if not is_prime(P):
        sys.stdout.write(f'警告: P={P} 不是素数\n')
        return

    alphas = [float(x) for x in args.alphas.split(',')]
    rows_to_check = min(args.rowsToCheck, P)

    sys.stdout.write(f'§233 多层互斥引理实证 P={P}\n')
    sys.stdout.write(f'阈值 α: {alphas}\n')
    sys.stdout.write(f'P^α: {[f"{P**a:.1f}" for a in alphas]}\n\n')

    # 全 P 行扫描每层
    layer_stats = {alpha: {'total_R': 0, 'total_violations': 0,
                           'max_R': 0, 'rows_scanned': 0} for alpha in alphas}

    for i in range(1, P + 1):
        layers = analyze_row_layers(P, i, alphas)
        for alpha in alphas:
            R = layers[alpha]['R']
            threshold = layers[alpha]['threshold']
            v = verify_multilayer_exclusion(R, threshold)
            layer_stats[alpha]['total_R'] += len(R)
            layer_stats[alpha]['total_violations'] += v
            if len(R) > layer_stats[alpha]['max_R']:
                layer_stats[alpha]['max_R'] = len(R)
            layer_stats[alpha]['rows_scanned'] += 1

    sys.stdout.write(f'{"α":>6} {"P^α":>8} {"avg|R_α|":>10} {"max|R_α|":>10} {"violations":>11} {"严格?":>6}\n')
    for alpha in alphas:
        stats = layer_stats[alpha]
        avg_R = stats['total_R'] / stats['rows_scanned']
        viol = stats['total_violations']
        strict = '✅' if viol == 0 else '⚠️'
        sys.stdout.write(f'{alpha:>6.3f} {P**alpha:>8.1f} {avg_R:>10.2f} '
                         f'{stats["max_R"]:>10} {viol:>11} {strict:>6}\n')

    sys.stdout.write(f'\n=== 多层互斥实证结论 ===\n')
    all_strict = all(layer_stats[a]['total_violations'] == 0 for a in alphas)
    if all_strict:
        sys.stdout.write(f'★ 所有 α ∈ {alphas} 多层互斥引理 P={P} 严格成立\n')
    else:
        sys.stdout.write(f'⚠️ 某些 α 出现违例\n')

    # 反例代数复杂度估计
    sys.stdout.write(f'\n=== 反例代数复杂度 ===\n')
    sys.stdout.write(f'设 H_P 反例 (行全合数) 存在.\n')
    sys.stdout.write(f'反例必同时满足:\n')
    for alpha in alphas:
        threshold = P ** alpha
        avg_R = layer_stats[alpha]['total_R'] / layer_stats[alpha]['rows_scanned']
        sys.stdout.write(f'  α={alpha}: 行 {alpha}-粗合数 ~ {avg_R:.0f} 个, 局部因子互斥\n')
    sys.stdout.write(f'多层互斥共同约束 → 反例代数自由度受限\n')


if __name__ == '__main__':
    main()
