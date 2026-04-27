#!/usr/bin/env python3
"""§229 局部振荡引理数值验证。

对各 P, 验证: 长度 C·√P 的列段内必有素数 (在 [P, P²] 范围内).

实证测试:
1. 对各 P 与各行 i, 找最大素数空隙 g_max(i) = 行 i 内最大连续合数长度
2. 比较 g_max(i) 与 √P 的关系
3. 找最小 C 使 g_max ≤ C √P 严格成立

用法:
    python3 experiments/local_oscillation_lemma.py --maxP 5000
"""
import argparse
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0: return False
    return True


def max_composite_gap_in_row(P: int, i: int) -> int:
    """行 i 内最长连续合数串长度"""
    max_gap = 0
    cur_gap = 0
    for j in range(1, P + 1):
        N = (i - 1) * P + j
        if is_prime(N):
            cur_gap = 0
        else:
            cur_gap += 1
            if cur_gap > max_gap:
                max_gap = cur_gap
    return max_gap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=5000)
    parser.add_argument('--samples', default='101,251,503,1009,2003,4999')
    args = parser.parse_args()

    sample_Ps = [int(x) for x in args.samples.split(',')]

    sys.stdout.write(f'§229 局部振荡引理实证 (P 最大 {args.maxP})\n\n')

    sys.stdout.write(f'{"P":>6} {"sqrt P":>8} {"P²":>10} {"max gap":>9} {"max i":>6} '
                     f'{"gap/sqrt P":>11} {"gap/log²P":>10}\n')

    overall_max_C = 0
    for P in sample_Ps:
        if P > args.maxP:
            continue
        if not is_prime(P):
            continue
        sqrt_P = math.sqrt(P)
        log2P = math.log(P) ** 2

        max_overall_gap = 0
        max_i = 0
        for i in range(1, P + 1):
            g = max_composite_gap_in_row(P, i)
            if g > max_overall_gap:
                max_overall_gap = g
                max_i = i

        ratio_sqrt = max_overall_gap / sqrt_P
        ratio_log = max_overall_gap / log2P
        if ratio_sqrt > overall_max_C:
            overall_max_C = ratio_sqrt

        sys.stdout.write(f'{P:>6} {sqrt_P:>8.1f} {P*P:>10} {max_overall_gap:>9} '
                         f'{max_i:>6} {ratio_sqrt:>11.3f} {ratio_log:>10.3f}\n')

    sys.stdout.write(f'\n总体最大 gap / √P 比值: C ≥ {overall_max_C:.3f}\n')
    sys.stdout.write('\n=== 引理 229.1 实证 ===\n')
    sys.stdout.write(f'局部振荡引理: 长度 C₀ √P 列段必含素数\n')
    sys.stdout.write(f'实测 C₀ ≥ {overall_max_C:.3f} (在测试 P 范围内)\n')
    if overall_max_C < 2.0:
        sys.stdout.write(f'★ 实证 C₀ < 2.0, 与 Cramér 猜想 g(N) = O(log²N) 兼容\n')
    elif overall_max_C < 4.0:
        sys.stdout.write(f'实证 C₀ < 4.0, 接近 √P 量级\n')


if __name__ == '__main__':
    main()
