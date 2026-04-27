#!/usr/bin/env python3
"""§218 显式 CRT 解 a 的精确计算。

对 c=2309 等反例 c, 用 CRT 求出 a 的精确整数值（不全枚举 P_cand）。
然后比较 a 与各种 X 值, 给出对应 H_P 列方向 P 上限。

关键代数推导:
  P 满足 r_unkill_q(P) = r_opt_q for q ∈ chosen_qs
  ⇔ A_old(P) ≡ -r_opt_q · P (mod q) for all q ∈ chosen_qs

  用 V = -residue · P (整数)
  V mod modulus_pre = A_old
  V mod q = -residue · P mod q

  A_old (mod q) = V - k_v · modulus_pre (mod q) (k_v 自由整数)
  -r_opt_q · P ≡ V mod q - k_v · modulus_pre (mod q)
  -r_opt_q · P ≡ -residue · P - k_v · modulus_pre (mod q)
  (residue - r_opt_q) · P ≡ k_v · modulus_pre (mod q)
  P ≡ k_v · modulus_pre · (residue - r_opt_q)^{-1} (mod q)

每 (k_v_q for q ∈ chosen_qs) 给出 P 的不同同余 (mod modulus_chosen).
我们想找最小 P 使 (1) 同时满足所有 q 同余 (2) anchor barrier (3) 素数.

实施 CRT 解 a 的最小化, 在所有 (k_v_q) 选择上扫描.

用法:
    python3 experiments/explicit_a_value.py --c 2309
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict
from itertools import product
from typing import List

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from min_modulus_for_need import hot_caps_per_q, min_log_modulus_for_need
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase
from prefix_completion_bound import full_scan


def hot_optimal_r(holes, q):
    counts = defaultdict(int)
    for h in holes:
        counts[h % q] += 1
    if not counts:
        return None, 0
    max_H = max(counts.values())
    rs = sorted(r for r, c in counts.items() if c == max_H)
    return rs[0], max_H


def crt_combine(constraints):
    """[(a_i, m_i)] CRT 合并, 返回 (a, m)."""
    a, m = 0, 1
    for a_i, m_i in constraints:
        g = math.gcd(m, m_i)
        if g != 1:
            if (a - a_i) % g != 0:
                return None, None
            # 使用扩展 CRT
            from math import gcd
            new_m = m * m_i // g
            # 解 a + m·k ≡ a_i (mod m_i)
            t = ((a_i - a) // g)
            mp = m // g
            mip = m_i // g
            try:
                inv = pow(mp, -1, mip)
            except ValueError:
                return None, None
            k = (t * inv) % mip
            a = a + m * k
            m = new_m
            a = a % m
        else:
            inv = pow(m, -1, m_i)
            k = ((a_i - a) * inv) % m_i
            a = a + m * k
            m = m * m_i
            a = a % m
    return a, m


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--XFull', type=int, default=1_000_000)
    parser.add_argument('--maxKvCombos', type=int, default=1000,
                        help='扫描的 (k_v_q) 组合上限')
    args = parser.parse_args()

    primes = primes_upto(args.XFull)
    result = full_scan(args.c, args.W, args.S, args.kLow, args.XFull,
                       state_limit=8000, residue_limit=14, primes=primes)
    nz = result['nonzero_examples']
    if not nz:
        print(f'c={args.c} 无 nonzero prefix')
        return

    prefix_tuple = nz[0][0]
    prefix = list(prefix_tuple)
    prefix_saving = sum(t[2] for t in prefix)
    need = args.S - prefix_saving
    last_cap = prefix[-1][2]
    used = {t[0] for t in prefix}
    residue, modulus_pre = prefix_phase(prefix)

    holes = holes_for_c(args.c, args.W)
    Y = 11
    D = max(holes) - min(holes)
    q_cap_list = []
    for q in primes_upto(D):
        if q <= Y or q in used:
            continue
        cap = hot_caps_per_q(holes, q, last_cap)
        if cap > 0:
            q_cap_list.append((q, cap))
    log_min, chosen_qs = min_log_modulus_for_need(q_cap_list, need)
    if log_min is None:
        print(f'c={args.c} 无条件通过')
        return

    r_optimals = {q: hot_optimal_r(holes, q)[0] for q in chosen_qs}

    print(f'§218 c={args.c} 显式 a 计算')
    print(f'prefix={prefix}')
    print(f'prefix_saving={prefix_saving}, need={need}, last_cap={last_cap}')
    print(f'modulus_pre = {modulus_pre} ≈ 10^{math.log10(modulus_pre):.2f}')
    print(f'residue = {residue}')
    print(f'chosen_qs = {chosen_qs}')
    print(f'r_optimals = {r_optimals}')

    modulus_chosen = 1
    for q in chosen_qs:
        modulus_chosen *= q
    modulus_required = modulus_pre * modulus_chosen
    print(f'modulus_chosen = {modulus_chosen} ≈ 10^{math.log10(modulus_chosen):.2f}')
    print(f'modulus_required = {modulus_required} ≈ 10^{math.log10(modulus_required):.2f}')
    print()

    # 对每 q ∈ chosen_qs, P 满足 P ≡ k_v_q · modulus_pre · (residue - r_opt_q)^{-1} (mod q)
    # 不同 k_v_q 给出 q 个可能 P (mod q).
    # 总共 ∏ q ≈ 10^8 种 (k_v_q) 组合.
    # 完整扫描太慢. 我们选 k_v_q = 0 给出 P ≡ 0 (mod q), 但这要求 q | P (即 P 不是素数除非 P = q).
    # k_v_q = 1, 2, ... 给不同 P (mod q).

    # 对每个组合, CRT 求 P (mod modulus_chosen). 然后用 anchor barrier + 素性检查.
    # 这里: 列出几个组合的 a 值看分布.

    # 简化: 取 k_v_q = 1 for all q (即第一个非零位移)
    # 实际上是任意 (k_v_q) 都给可能的 P. 让我对 k_v_q ∈ {1, 2} 扫描所有组合.

    print('扫描 k_v_q ∈ [1, k_max], 找让 P 极小的 a:')

    P_min_a = None
    P_min_combo = None
    n_scanned = 0
    k_max = max(2, int(args.maxKvCombos ** (1.0 / len(chosen_qs))))
    for combo in product(range(1, k_max + 1), repeat=len(chosen_qs)):
        constraints = []
        for q, k_v in zip(chosen_qs, combo):
            try:
                inv = pow((residue - r_optimals[q]) % q, -1, q)
            except ValueError:
                break
            P_mod_q = (k_v * modulus_pre * inv) % q
            constraints.append((P_mod_q, q))
        else:
            a, m = crt_combine(constraints)
            if a is None:
                continue
            n_scanned += 1
            # 取 P = a (最小满足同余的正整数)
            if a == 0:
                a = m
            if P_min_a is None or a < P_min_a:
                P_min_a = a
                P_min_combo = combo
        if n_scanned >= args.maxKvCombos:
            break

    print(f'扫描 {n_scanned} 个 k_v_q 组合, 最小 a = {P_min_a}')
    print(f'对应 (k_v_q) = {P_min_combo}')

    if P_min_a is not None:
        print(f'log10(P_min_a) = {math.log10(P_min_a):.2f}')
        print(f'modulus_chosen = {modulus_chosen}')
        print(f'P_min_a / modulus_chosen = {P_min_a / modulus_chosen:.3f}')
        # 对应 H_P 列方向 P 上限
        print(f'若反例 P = a 存在, 对应 H_P 列方向破坏点 P_max = {P_min_a // 3000}')

        # 验证 a 是否真满足条件
        A_old_a = (-residue * P_min_a) % modulus_pre
        print(f'A_old(a) = {A_old_a}')
        print(f'A_old(a) ≤ a? {A_old_a <= P_min_a}')
        for q in chosen_qs:
            try:
                P_inv = pow(P_min_a % q, -1, q)
                r_uk = (-A_old_a * P_inv) % q
                print(f'  q={q}: r_unkill = {r_uk}, r_opt = {r_optimals[q]}, match? {r_uk == r_optimals[q]}')
            except ValueError:
                print(f'  q={q}: P_inv 不存在')

        # 是否素数
        def is_prime(n):
            if n < 2: return False
            for d in range(2, int(n**0.5)+1):
                if n % d == 0: return False
            return True
        if P_min_a < 10**12:
            print(f'is_prime(a) = {is_prime(P_min_a)}')


if __name__ == '__main__':
    main()
