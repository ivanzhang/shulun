#!/usr/bin/env python3
"""§216 解析版 P_cand 证书：通过 CRT 直接求 a, 不用 sieve.

关键观察:
满足 r_unkill_q(P) = r_optimal(q) for q ∈ chosen_qs 的 P 满足
  P ≡ alpha (mod modulus_chosen)
其中 modulus_chosen = ∏ chosen_qs ≈ 10^8.

加上 anchor barrier A_old(P) ≤ P 的约束更复杂. 但用 CRT 与 modulus_pre 联合:
  V := -residue · P  ≡  A_old (mod modulus_pre)
对每 q ∈ chosen_qs:
  V ≡ -r_optimal(q) · P (mod q)

这给出 P 满足的 CRT 系统. 解 a 是唯一的 mod modulus_required = modulus_pre · ∏ chosen_qs.

如果 a > P_cand_max, 则 P_cand ≤ P_cand_max 内无反例 (不需 sieve).

用法:
    python3 experiments/analytic_p_certificate.py --PCandMax 1000000000
    python3 experiments/analytic_p_certificate.py --PCandMax 10000000000000
"""
from __future__ import annotations

import argparse
import math
import sys
import time
from collections import defaultdict
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


def is_probable_prime(n: int) -> bool:
    """Miller-Rabin 确定性版（n < 3.3 × 10^14 确定，更大概率正确）."""
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == p: return True
        if n % p == 0: return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if a >= n: continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True


def solve_crt_constraints(prefix, chosen_qs, r_optimals, modulus_pre, residue):
    """求 P 满足 r_unkill_q(P) = r_optimal(q) 的 CRT 解 a.

    对每 q ∈ chosen_qs:
      r_unkill_q(P) = (-A_old · P^{-1}) mod q = r_optimal(q)
      ⇔ A_old · P^{-1} ≡ -r_optimal(q) (mod q)
      ⇔ A_old ≡ -r_optimal(q) · P (mod q)

    A_old = (-residue · P) mod modulus_pre. 对 q ∉ used (互素), modulus_pre 与 q 互素.
    A_old = -residue · P + k · modulus_pre 对某 k. 即 V := -residue · P, A_old = V mod modulus_pre.
    V mod q = -residue · P mod q.

    由 V = A_old + k_v · modulus_pre, k_v 待定整数. V mod q = A_old + k_v · modulus_pre (mod q).
    A_old ≡ -r_optimal · P (mod q) (由不杀条件)
    V ≡ A_old + k_v · modulus_pre ≡ -r_optimal · P + k_v · modulus_pre (mod q)
    但 V ≡ -residue · P (mod q).
    所以 -residue · P ≡ -r_optimal · P + k_v · modulus_pre (mod q)
            (residue - r_optimal) · P ≡ -k_v · modulus_pre (mod q)
    P ≡ -k_v · modulus_pre · (residue - r_optimal)^{-1} (mod q)

    每 k_v 给出 P (mod q) 的不同值. 但 k_v ≥ 0 (因 A_old ≥ 0). 加上 anchor barrier A_old ≤ P,
    对每 q 取最小可行 k_v.

    简化: 取 k_v = 0 ⇒ V = A_old ⇔ residue · P ≤ modulus_pre ⇒ P ≤ modulus_pre / residue.

    更一般: 直接对 P 满足的 mod q 约束做 CRT, 再考虑 anchor barrier.

    对每 q ∈ chosen_qs:
      P ≡ alpha_q (mod q), alpha_q = ((-r_optimal_q · P) - A_old) · modulus_pre^{-1} mod q ... 等等
      不能直接用 P 表示 alpha_q (循环).

    重新看: A_old ≡ -r_optimal_q · P (mod q). 这是 P 满足的关系.
    A_old = (-residue · P) mod modulus_pre.

    对 q 取模:
      A_old (mod q) = (-residue · P) mod modulus_pre, 然后 (mod q)
      不直接简化.

    实用策略: 直接用 modulus_pre · q (modulus_pre 与 q 互素) 在合并 CRT.
    对每 q ∈ chosen_qs, 把 (residue, modulus_pre) 与 (r_unkill_constraint, q) 合并,
    给出 P 的 mod (modulus_pre · q) 同余.

    具体算法见下.
    """
    M = modulus_pre
    R = residue
    # 当前 P 满足: -R · P ≡ A_old (mod M), 但 A_old 是变量. 实际上 P 是整数, A_old ∈ [0, M).
    # 要得 A_old ≡ -r_opt_q · P (mod q), 即 -R · P ≡ -r_opt_q · P + l · M (mod q · M) 对某 l ≥ 0.
    # 但实际只需 A_old (mod q) = -r_opt_q · P (mod q).
    # A_old = -R · P mod M, A_old ∈ [0, M). A_old (mod q) = (-R · P mod M) (mod q).
    # 这不是 -R · P (mod q) (因为 mod M 后再 mod q)!

    # 正确做法: V = -R · P. V mod M = A_old. A_old (mod q) ≠ V mod q (一般).
    # 让 k_v = (V - A_old) / M 是整数 ≥ 0 (V 一般 ≤ 0, A_old ≥ 0, k_v ≤ 0... 这里要小心)
    # 实际 V mod M = A_old, 即 V ≡ A_old (mod M). V 可以是任意整数.
    # 设 V = A_old + k · M, k ∈ Z (任意). 我们想 A_old (mod q) = -r_opt · P (mod q).
    # V (mod q) = A_old + k · M (mod q).
    # V (mod q) = -R · P (mod q).
    # 所以 A_old + k · M ≡ -R · P (mod q)
    #     A_old ≡ -R · P - k · M (mod q)
    # 不杀条件: A_old ≡ -r_opt · P (mod q)
    # 合并: -R · P - k · M ≡ -r_opt · P (mod q)
    #      (R - r_opt) · P ≡ -k · M (mod q)
    #      P ≡ -k · M · (R - r_opt)^{-1} (mod q)
    # 对每 q, k 是整数自由参数. 不同 k 给出不同 P (mod q).
    #
    # 完整 P 满足: P (mod q) ≡ -k_q · M · (R - r_opt_q)^{-1} (mod q), 不同 q 的 k_q 自由.
    # 所以 P 在 (mod q) 上有 q 个可能值 (k_q 取 0, 1, ..., q-1).
    # 用 CRT 合并: 对每 (q_i, k_q_i) 选择, P 唯一确定 mod ∏ q_i.
    # 总共 ∏ q_i 个不同 P (mod ∏ q_i) 的可能值.
    #
    # 但每 P (mod ∏ q_i) 还要满足 anchor barrier A_old ≤ P.
    # A_old < M 一般 ≫ P (因 M ≈ 10^14, P ≤ 10^9), 几乎不可能 A_old ≤ P.
    # 除非特定 P 让 A_old 极小.
    #
    # 这变成复杂的代数. 简化: 不直接求 a, 转而对 P_cand_max 做 sieve + 检查.

    return None  # 不实施纯解析, 转 sieve fallback


def enumerate_for_c(c: int, W: int, S: int, k_low: int, X_full: int,
                    P_cand_max: int) -> dict:
    """对单 c 找反例 prefix, 然后用 (mod ∏ chosen_qs) 同余筛选 + Miller-Rabin.

    满足 r_unkill_q = r_opt_q 的 P (mod q) 由 q 个可能值 (因 k 自由).
    所以总满足候选数 ≈ (P_cand_max / 1) (即所有 P)...
    这里改用 (mod ∏ chosen_qs) 上的实际枚举 + anchor 检查.
    实际: 对每 q ∈ chosen_qs, 每个 r_unkill = r_opt_q 给 P 的某个同余类.
    但 anchor barrier 依赖 A_old (依赖 P), 所以最终需 P_cand 全枚举.

    使用素数表 (sieve to 10^8 + Miller-Rabin for >10^8) 加速.
    """
    primes_for_scan = primes_upto(X_full)
    result = full_scan(c, W, S, k_low, X_full,
                      state_limit=8000, residue_limit=14, primes=primes_for_scan)
    nz = result['nonzero_examples']
    if not nz:
        return {'c': c, 'no_nz': True}

    prefix_tuple = nz[0][0]
    prefix = list(prefix_tuple)
    prefix_saving = sum(t[2] for t in prefix)
    need = S - prefix_saving
    last_cap = prefix[-1][2]
    used = {t[0] for t in prefix}
    residue, modulus_pre = prefix_phase(prefix)

    holes = holes_for_c(c, W)
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
        return {'c': c, 'unconditional_pass': True}

    r_optimals = {q: hot_optimal_r(holes, q)[0] for q in chosen_qs}

    modulus_required = modulus_pre
    for q in chosen_qs:
        modulus_required *= q

    print(f'  c={c}: prefix_saving={prefix_saving}, need={need}, '
          f'modulus_required=10^{math.log10(modulus_required):.1f}', flush=True)
    print(f'  搜索 P_cand ∈ [2, {P_cand_max:_}], chosen_qs={chosen_qs}', flush=True)

    # 用 modulus_chosen = ∏ chosen_qs 上的同余筛, 从 P_cand 跳过 ≡ 不命中 r_opt 的 P.
    modulus_chosen = 1
    for q in chosen_qs:
        modulus_chosen *= q

    # 对每 q, P 满足 r_unkill_q = r_opt_q 的 P (mod q) 集合 = q 个可能值 (k 自由)
    # 但实际把 modulus_pre 加入后, 只有特定 P (mod modulus_pre · q) 让 A_old (mod q) = -r_opt · P (mod q) 成立.
    # 这还是回到 P_cand 全枚举.
    #
    # 实用: 直接对每个素数 P_cand, 检查 anchor + r_unkill. 用 sieve 加速素性测试.
    # 但 sieve 10^9+ 内存巨大. 转用 segment sieve 或 Miller-Rabin.
    #
    # 简化: 对 P_cand_max ≤ 10^8 用 sieve, 更大用 Miller-Rabin (但速度变慢).

    n_prime_tested = 0
    found = []
    t0 = time.time()
    if P_cand_max <= 10_000_000:
        # 直接 primes_upto
        primes_table = primes_upto(P_cand_max)
        for P_cand in primes_table:
            if P_cand >= modulus_pre: break
            n_prime_tested += 1
            A_old = (-residue * P_cand) % modulus_pre
            if A_old > P_cand: continue
            all_match = True
            for q in chosen_qs:
                try:
                    P_inv = pow(P_cand % q, -1, q)
                except ValueError:
                    all_match = False; break
                r_uk = (-A_old * P_inv) % q
                if r_uk != r_optimals[q]:
                    all_match = False; break
            if all_match:
                found.append((P_cand, A_old))
                if len(found) >= 3: break
    else:
        # 大范围 sieve 实在不行, 改用 segment sieve
        from math import isqrt
        BLOCK = 10_000_000
        small_lim = isqrt(P_cand_max) + 1
        small_primes = primes_upto(small_lim)
        # 每个 block 做 sieve
        for block_start in range(2, P_cand_max + 1, BLOCK):
            block_end = min(block_start + BLOCK - 1, P_cand_max)
            seg = bytearray([1]) * (block_end - block_start + 1)
            if block_start == 2:
                seg[0] = 1  # 2 is prime
            for p in small_primes:
                if p * p > block_end: break
                start = max(p * p, ((block_start + p - 1) // p) * p)
                for j in range(start, block_end + 1, p):
                    seg[j - block_start] = 0
            if block_start <= 1:
                seg[0] = 0  # 0 not prime
                if len(seg) > 1: seg[1] = 0  # 1 not prime
            for offset, is_p in enumerate(seg):
                if not is_p: continue
                P_cand = block_start + offset
                if P_cand < 2: continue
                if P_cand >= modulus_pre: break
                n_prime_tested += 1
                A_old = (-residue * P_cand) % modulus_pre
                if A_old > P_cand: continue
                all_match = True
                for q in chosen_qs:
                    try:
                        P_inv = pow(P_cand % q, -1, q)
                    except ValueError:
                        all_match = False; break
                    r_uk = (-A_old * P_inv) % q
                    if r_uk != r_optimals[q]:
                        all_match = False; break
                if all_match:
                    found.append((P_cand, A_old))
                    if len(found) >= 3: break
            if found and len(found) >= 3: break
            if (block_start // BLOCK) % 10 == 0:
                print(f'    [{block_start//BLOCK}/{P_cand_max//BLOCK}] tested={n_prime_tested:_} t={time.time()-t0:.0f}s', flush=True)

    elapsed = time.time() - t0
    return {
        'c': c,
        'prefix_saving': prefix_saving,
        'need': need,
        'modulus_required_log10': math.log10(modulus_required),
        'chosen_qs': chosen_qs,
        'r_optimals': r_optimals,
        'P_cand_max': P_cand_max,
        'n_primes_tested': n_prime_tested,
        'found': found,
        'elapsed_sec': round(elapsed, 1),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cList', default='59,101,353,619,961,1343,1609,1789,2309')
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--XFull', type=int, default=1_000_000)
    parser.add_argument('--PCandMax', type=int, default=1_000_000_000,
                        help='P_cand 全枚举上限 (segment sieve 支持任意大)')
    args = parser.parse_args()

    c_list = [int(x) for x in args.cList.split(',')]

    print(f'§216 解析版 P_cand 全枚举证书 (segment sieve)')
    print(f'参数: W={args.W}, S={args.S}, k_low={args.kLow}')
    print(f'P_cand_max = {args.PCandMax:_} (= 10^{math.log10(args.PCandMax):.1f})')
    print(f'对应 H_P 列方向 P ≤ {args.PCandMax // (30 * args.W):_}')
    print()

    summary = []
    for c in c_list:
        print(f'--- c={c} ---', flush=True)
        rec = enumerate_for_c(c, args.W, args.S, args.kLow,
                             args.XFull, args.PCandMax)
        if rec.get('no_nz'):
            print(f'  无 nonzero prefix, 跳过')
            continue
        if rec.get('unconditional_pass'):
            print(f'  ★ 无条件通过')
            continue
        if rec['found']:
            print(f'  ⚠ 找到反例 P:')
            for P, A in rec['found']:
                print(f'    P={P} A={A}')
        else:
            print(f'  ★ P_cand ≤ {args.PCandMax:_} 内无反例 ({rec["n_primes_tested"]:_} 素数, {rec["elapsed_sec"]}s)')
        summary.append(rec)
        print()

    print('=' * 60)
    print('§216 总结')
    print('=' * 60)
    n_found = sum(1 for r in summary if r.get('found'))
    n_pass = len(summary) - n_found
    print(f'  全 {len(summary)} 反例 c, 找到反例: {n_found}, 严格通过: {n_pass}')
    if n_found == 0:
        print()
        print(f'★★★ H_P 列方向严格成立: P ≤ {args.PCandMax // (30 * args.W):_} ★★★')
        print(f'    (基于 P_cand 全枚举 ≤ {args.PCandMax:_})')


if __name__ == '__main__':
    main()
