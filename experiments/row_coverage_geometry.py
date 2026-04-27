#!/usr/bin/env python3
"""§220 几何斜线 + 位移碎片化 数值实证。

对 P×P 方阵的每一行 i ∈ [1, P]，计算：

1. 每条 q-斜线在第 i 行的覆盖位置 R_q^{(i)} = {j : j ≡ -(i-1)P (mod q)}
2. 全覆盖率 |⋃_q R_q^{(i)}| / P
3. 未覆盖位置（即素数候选）数

验证：
- 第 1 行（i=1）覆盖率 = (P - π(P) - 1) / P  (除 1 与素数)
- 第 i ≥ 2 行覆盖率 ~ 1 - e^{-γ}/log(iP) < 1
- 未覆盖位置数 ≥ 1 (即每行有素数)

用法:
    python3 experiments/row_coverage_geometry.py --P 1009 --show 5
"""
from __future__ import annotations

import argparse
import math
import sys
from typing import List

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto


def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0: return False
    return True


def row_coverage(P: int, i: int) -> dict:
    """计算第 i 行的几何覆盖结构。"""
    primes_le_P = primes_upto(P)
    covered = [False] * (P + 1)  # j ∈ [1, P]
    cover_count_per_q = {}

    # 遍历每个 q ≤ √(iP)（实际只需 q ≤ √(iP), 但用 P 上界）
    upper_q = int(math.isqrt(i * P)) + 1
    for q in primes_le_P:
        if q > upper_q:
            break
        if i == 1:
            # j ≡ 0 (mod q), j ∈ [1, P]: q, 2q, ..., ⌊P/q⌋·q
            r = 0
        else:
            r = (-(i - 1) * P) % q  # 即 q | (i-1)P + j ⇔ j ≡ r (mod q)
        cnt = 0
        # j 从 r 开始（如果 r=0, 从 q 开始；否则从 r 开始）
        start = r if r > 0 else q
        for j in range(start, P + 1, q):
            if 1 <= j <= P and not covered[j]:
                covered[j] = True
            cnt += 1
        cover_count_per_q[q] = cnt

    # 未覆盖位置
    uncovered = [j for j in range(1, P + 1) if not covered[j]]
    # 每个未覆盖 j 对应 N_{i,j}, 检查是否素数
    uncovered_with_status = []
    for j in uncovered:
        N = (i - 1) * P + j
        uncovered_with_status.append((j, N, is_prime(N)))

    return {
        'i': i,
        'P': P,
        'q_count': len(cover_count_per_q),
        'upper_q': upper_q,
        'covered_count': sum(covered[1:]),
        'uncovered_count': len(uncovered),
        'coverage_rate': sum(covered[1:]) / P,
        'mertens_bound': 1 - math.exp(-0.5772156649) / math.log(max(2, upper_q)),
        'uncovered_positions': uncovered_with_status,
        'primes_in_row': sum(1 for _, _, is_p in uncovered_with_status if is_p),
        'composites_in_uncovered': sum(1 for _, _, is_p in uncovered_with_status if not is_p),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=1009)
    parser.add_argument('--rows', default=None,
                        help='指定行号列表，逗号分隔；默认 1, 2, P/2, P-1, P')
    parser.add_argument('--show', type=int, default=5)
    parser.add_argument('--all', action='store_true', help='扫描所有 P 行')
    args = parser.parse_args()

    P = args.P
    if not is_prime(P):
        print(f'警告: P={P} 不是素数')

    if args.rows:
        rows = [int(r) for r in args.rows.split(',')]
    elif args.all:
        rows = list(range(1, P + 1))
    else:
        rows = sorted(set([1, 2, P // 2, P - 1, P]))

    print(f'§220 行方向几何覆盖实证: P={P}, |rows|={len(rows)}')
    print(f'{"i":>5} {"q数":>4} {"上界q":>6} {"覆盖":>6} {"未覆盖":>7} {"覆盖率":>8} {"Mertens":>9} {"行内素数":>9}')

    min_primes = float('inf')
    rows_no_prime = []
    for i in rows:
        rec = row_coverage(P, i)
        if rec['primes_in_row'] < min_primes:
            min_primes = rec['primes_in_row']
        if rec['primes_in_row'] == 0:
            rows_no_prime.append(i)
        print(f'{i:>5} {rec["q_count"]:>4} {rec["upper_q"]:>6} '
              f'{rec["covered_count"]:>6} {rec["uncovered_count"]:>7} '
              f'{rec["coverage_rate"]:>8.4f} {rec["mertens_bound"]:>9.4f} '
              f'{rec["primes_in_row"]:>9}')
        if i in (1, 2, P) and len(rec['uncovered_positions']) <= args.show + 5:
            for j, N, is_p in rec['uncovered_positions'][:args.show]:
                print(f'    j={j} N={N} prime={is_p}')

    print()
    print(f'最小行内素数: {min_primes}')
    print(f'无素数的行: {rows_no_prime}')
    if not rows_no_prime:
        print(f'★ 所有 {len(rows)} 行都含素数（H_P 行方向 P={P} 严格成立）')


if __name__ == '__main__':
    main()
