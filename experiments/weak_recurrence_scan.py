#!/usr/bin/env python3
"""§226 多 P 弱复现 k 扫描 - 验证 k > P 与 gcd(k, P) = 1 必要性。

对每个素数 P ≤ P_max, 扫描 k ∈ [2, K_max], 找所有弱复现行 k:
[(k-1)P+1, kP] 全合数。

统计:
- 弱复现 k 数量
- k > P 是否必然
- gcd(k, P) = 1 是否必然
- k 的算术特征 (素因子分解等)

用法:
    python3 experiments/weak_recurrence_scan.py --maxP 50 --maxK 200
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto


def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0: return False
    return True


def is_weak_recurrence(P, k):
    """[(k-1)P+1, kP] 全合数?"""
    for j in range(1, P + 1):
        if is_prime((k - 1) * P + j):
            return False
    return True


def first_prime_in_row(P, k):
    """行 k 内首个素数"""
    for j in range(1, P + 1):
        N = (k - 1) * P + j
        if is_prime(N):
            return (j, N)
    return None


def factor(n):
    """n 的素因子分解"""
    if n < 2: return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1: factors.append(n)
    return factors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=50)
    parser.add_argument('--maxK', type=int, default=300)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    print(f'§226 多 P 弱复现扫描 (P ≤ {args.maxP}, k ≤ {args.maxK})')
    print()
    print(f'{"P":>4} {"P²":>6} {"弱复现k":>10} {"k>P":>6} {"gcd(k,P)=1":>11} {"k分解":>20}')

    all_weak = []
    cnt_total = 0
    cnt_k_gt_P = 0
    cnt_coprime = 0

    for P in primes_upto(args.maxP):
        if P < 5: continue
        weak_ks = []
        for k in range(2, args.maxK + 1):
            if is_weak_recurrence(P, k):
                weak_ks.append(k)
        for k in weak_ks:
            cnt_total += 1
            k_gt_P = k > P
            coprime = math.gcd(k, P) == 1
            if k_gt_P: cnt_k_gt_P += 1
            if coprime: cnt_coprime += 1
            f = factor(k)
            f_str = '·'.join(map(str, f)) if f else str(k)
            all_weak.append((P, k, k_gt_P, coprime, f))
            print(f'{P:>4} {P*P:>6} {k:>10} {str(k_gt_P):>6} {str(coprime):>11} {f_str:>20}')

    print()
    print('=' * 70)
    print(f'总弱复现 (P, k) 对: {cnt_total}')
    print(f'其中 k > P: {cnt_k_gt_P} ({cnt_k_gt_P/max(1, cnt_total)*100:.1f}%)')
    print(f'其中 gcd(k, P) = 1: {cnt_coprime} ({cnt_coprime/max(1, cnt_total)*100:.1f}%)')

    # 验证猜想
    print()
    if cnt_total == cnt_k_gt_P:
        print(f'★ 猜想 1 (k > P): 实测全部成立')
    else:
        print(f'⚠ 猜想 1 (k > P): 有反例')
        for P, k, k_gt_P, _, _ in all_weak:
            if not k_gt_P:
                print(f'  反例: P={P}, k={k} ≤ P')

    if cnt_total == cnt_coprime:
        print(f'★ 猜想 2 (gcd(k, P) = 1): 实测全部成立')
    else:
        print(f'⚠ 猜想 2 (gcd(k, P) = 1): 有反例')
        for P, k, _, coprime, _ in all_weak:
            if not coprime:
                print(f'  反例: P={P}, k={k}, gcd={math.gcd(k, P)}')


if __name__ == '__main__':
    main()
