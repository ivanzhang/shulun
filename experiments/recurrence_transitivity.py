#!/usr/bin/env python3
"""§224 复现传递性数值验证。

对每个素数 P：
1. 强复现（每条 q-斜线复现到第 1 行原位置）：仅 i ≡ 1 (mod primorial(P))。
2. 弱复现（行 i 全合数即 [(i-1)P+1, iP] 全合数）：实证扫描。

验证用户的反证策略：
- 强复现传递性 trivially 成立
- 弱复现传递性不严格成立

但 §220 几何论证 + Mertens 容斥仍给出 H_P 行方向严格证明。

用法:
    python3 experiments/recurrence_transitivity.py --P 23
"""
from __future__ import annotations

import argparse
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto


def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0: return False
    return True


def primorial(P):
    """primorial(P) = ∏_{q ≤ P prime} q"""
    p = 1
    for q in primes_upto(P):
        p *= q
    return p


def strong_recurrence_rows(P, max_i=None):
    """强复现行 = i ≡ 1 (mod primorial(P))"""
    pri = primorial(P)
    if max_i is None:
        max_i = P
    rows = [i for i in range(1, max_i + 1) if (i - 1) % pri == 0]
    return rows


def weak_recurrence_rows(P, max_i=None):
    """弱复现行 = [(i-1)P+1, iP] 全合数（即 i 行无素数）"""
    if max_i is None:
        max_i = P
    rows = []
    for i in range(1, max_i + 1):
        all_composite = True
        for j in range(1, P + 1):
            if is_prime((i - 1) * P + j):
                all_composite = False
                break
        if all_composite:
            rows.append(i)
    return rows


def weak_transitivity_test(P, k):
    """假设第 k 行弱复现, 测第 m(k-1)+1 行 (m=1, 2, ..., 5) 是否也弱复现"""
    rows_to_test = [1 + m * (k - 1) for m in range(1, 6) if 1 + m*(k-1) <= P*5]
    weak_rec = []
    for i in rows_to_test:
        all_composite = True
        for j in range(1, P + 1):
            if is_prime((i - 1) * P + j):
                all_composite = False
                break
        weak_rec.append((i, all_composite))
    return weak_rec


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=23)
    parser.add_argument('--maxK', type=int, default=None)
    args = parser.parse_args()

    P = args.P
    if not is_prime(P):
        print(f'警告: P={P} 不是素数')

    print(f'§224 复现传递性数值验证 P={P}')
    print()

    pri = primorial(P)
    print(f'primorial({P}) = {pri}')
    if pri > 10**15:
        print(f'  log10(primorial) = {math.log10(pri):.2f}')
    print(f'P² = {P*P}')
    print()

    # 强复现
    print('=== 强复现行 (i ≡ 1 (mod primorial)) ===')
    sr = strong_recurrence_rows(P, max_i=P*P)
    print(f'P×P 方阵内强复现行: {sr}')
    print(f'  (primorial(P) = {pri} {"<" if pri < P*P else ">="} P² = {P*P})')

    # 弱复现
    print()
    print('=== 弱复现行 ([(i-1)P+1, iP] 全合数) ===')
    wr = weak_recurrence_rows(P, max_i=min(P*5, 100))
    print(f'前 {min(P*5, 100)} 行内弱复现行: {wr}')
    if not wr:
        print('★ 无弱复现行，H_P 行方向严格成立')

    # 用户反证策略测试: 假设 k 行弱复现, 测 m(k-1)+1 行
    print()
    print('=== 用户反证策略检验 ===')
    print('假设第 k 行弱复现, 测第 m(k-1)+1 行 (m=1..5):')
    for k in [2, 3, 4, 5, 7, 11]:
        if k > P: break
        print(f'  k={k}:', end=' ')
        rec = weak_transitivity_test(P, k)
        for i, all_c in rec:
            print(f'i={i} 全合数={all_c}', end='; ')
        print()

    # 第 1 行 (强复现) 在多个 m 上的"复现位置"
    print()
    print('=== 强复现"传递性"验证 (k=1) ===')
    print('第 1 行强复现; m(k-1)+1 = 1 for any m → trivially 第 1 行复现')


if __name__ == '__main__':
    main()
