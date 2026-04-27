#!/usr/bin/env python3
"""§216 扩展 P_cand 范围到 10⁸ 的全枚举证书。

§215 在 P_cand ≤ 10⁷ 全枚举验证全 9 反例 c 通过。本节扩展到 P_cand ≤ 10⁸,
对应 H_P 列方向严格 P ≤ 33333.

策略:
1. 不重新跑 full_scan, 直接用已知 9 反例 c 的 prefix
2. 对每 prefix 全枚举 P_cand ∈ [2, 10⁸], 验证三条件
3. 加 sieve of Eratosthenes 加速素性检验

用法:
    python3 experiments/extended_p_certificate.py --PCandMax 100000000
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


def sieve_primes(N: int) -> bytearray:
    """0/1 布尔 sieve, [2, N]."""
    s = bytearray([1]) * (N + 1)
    s[0] = 0
    s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, N + 1, i):
                s[j] = 0
    return s


def is_probable_prime(n: int) -> bool:
    """Miller-Rabin (确定性 < 3.3 × 10^14, 用前 8 个 witness)."""
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


def enumerate_for_c(c: int, W: int, S: int, k_low: int, X_full: int,
                    P_cand_max: int, sieve: bytearray) -> dict:
    """对单 c 找反例 prefix, 然后 P_cand 全枚举."""
    primes_for_scan = primes_upto(X_full)
    result = full_scan(c, W, S, k_low, X_full,
                      state_limit=8000, residue_limit=14, primes=primes_for_scan)
    nz = result['nonzero_examples']
    if not nz:
        return {'c': c, 'no_nz': True}

    # 用第一个 nonzero prefix
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

    r_optimals = {}
    for q in chosen_qs:
        r, H = hot_optimal_r(holes, q)
        r_optimals[q] = r

    modulus_required = modulus_pre
    for q in chosen_qs:
        modulus_required *= q

    # 全枚举 P_cand ≤ P_cand_max 满足三条件
    print(f'  c={c}: prefix_saving={prefix_saving}, need={need}, '
          f'modulus_required=10^{math.log10(modulus_required):.1f}', flush=True)
    print(f'  搜索 P_cand ∈ [2, {P_cand_max:_}], chosen_qs={chosen_qs}', flush=True)

    found = []
    n_tested = 0
    t0 = time.time()
    for P_cand in range(2, P_cand_max + 1):
        if P_cand >= modulus_pre:
            break
        if not sieve[P_cand]:
            continue  # 不是素数
        n_tested += 1
        A_old = (-residue * P_cand) % modulus_pre
        if A_old > P_cand:
            continue  # anchor barrier 不满足
        # r_unkill 全命中最优 hot
        all_match = True
        for q in chosen_qs:
            try:
                P_inv = pow(P_cand % q, -1, q)
            except ValueError:
                all_match = False
                break
            r_uk = (-A_old * P_inv) % q
            if r_uk != r_optimals[q]:
                all_match = False
                break
        if all_match:
            found.append((P_cand, A_old))
            if len(found) >= 3:
                break

    elapsed = time.time() - t0
    return {
        'c': c,
        'prefix_saving': prefix_saving,
        'need': need,
        'modulus_required_log10': math.log10(modulus_required),
        'chosen_qs': chosen_qs,
        'r_optimals': r_optimals,
        'P_cand_max': P_cand_max,
        'n_primes_tested': n_tested,
        'found': found,
        'elapsed_sec': round(elapsed, 1),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cList', default='59,101,353,619,961,1343,1609,1789,2309')
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--XFull', type=int, default=1_000_000,
                        help='full_scan 范围（用来找反例 prefix）')
    parser.add_argument('--PCandMax', type=int, default=100_000_000,
                        help='P_cand 全枚举上限')
    args = parser.parse_args()

    c_list = [int(x) for x in args.cList.split(',')]

    print(f'§216 扩展 P_cand 全枚举证书')
    print(f'参数: W={args.W}, S={args.S}, k_low={args.kLow}')
    print(f'P_cand_max = {args.PCandMax:_} (= 10^{math.log10(args.PCandMax):.1f})')
    print(f'对应 H_P 列方向 P ≤ {args.PCandMax // 3000:_}')
    print()
    print(f'构建 sieve 到 {args.PCandMax:_}...', flush=True)
    t0 = time.time()
    sieve = sieve_primes(args.PCandMax)
    print(f'sieve 完成 ({time.time()-t0:.1f}s)', flush=True)

    summary = []
    for c in c_list:
        print(f'--- c={c} ---', flush=True)
        rec = enumerate_for_c(c, args.W, args.S, args.kLow,
                             args.XFull, args.PCandMax, sieve)
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
            print(f'  ★ P_cand ≤ {args.PCandMax:_} 内无反例 ({rec["n_primes_tested"]:_} 素数测试, {rec["elapsed_sec"]}s)')
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
        print(f'★★★ H_P 列方向严格成立: P ≤ {args.PCandMax // 3000:_} ★★★')
        print(f'    (基于 P_cand 全枚举 ≤ {args.PCandMax:_})')


if __name__ == '__main__':
    main()
