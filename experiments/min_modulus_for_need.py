#!/usr/bin/env python3
"""§213 min modulus_required: 把 (⋆_∞) 路径精确化的最小 CRT 下界。

§212 用"cap 降序"贪心估计 modulus_required。本节用动态规划求精确最小值：

    minimize ∏_{q ∈ S} q
    subject to Σ_{q ∈ S} cap_max(q, last_cap) ≥ need
              S ⊂ unused_q_set

这给出"任何让 M_kill ≥ need 的 q 子集" 的最小可能 CRT 模数 — 是 (⋆_∞) 论证的真正紧下界。

DP: dp[saving] = min log_∏_q s.t. cum saving = saving
转移: dp[s + cap_q] = min(dp[s + cap_q], dp[s] + log(q))

用法：
    python3 experiments/min_modulus_for_need.py --c 2309 --kLow 10
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase
from prefix_completion_bound import full_scan


def hot_caps_per_q(holes, q, last_cap):
    counts = defaultdict(int)
    for h in holes:
        counts[h % q] += 1
    H_values = list(counts.values())
    max_H = max(H_values) if H_values else 1
    return min(last_cap, max(0, max_H - 1))


def min_log_modulus_for_need(q_cap_list, need: int) -> tuple[float | None, list]:
    """DP 求最小 ∑ log10(q) s.t. ∑ cap ≥ need."""
    if need <= 0:
        return 0.0, []

    # 用 saving 做状态：dp[s] = min log10(∏ q) s.t. cum saving = s
    cap_max = sum(c for _, c in q_cap_list)
    if cap_max < need:
        return None, []

    target = need
    dp = [float('inf')] * (cap_max + 1)
    parent = [None] * (cap_max + 1)
    dp[0] = 0.0

    for q, cap in q_cap_list:
        if cap <= 0:
            continue
        for s in range(cap_max, cap - 1, -1):
            prev = s - cap
            if dp[prev] + math.log10(q) < dp[s]:
                dp[s] = dp[prev] + math.log10(q)
                parent[s] = (prev, q)

    # 找最小 dp[s] for s ≥ target
    best_s = None
    best_log = float('inf')
    for s in range(target, cap_max + 1):
        if dp[s] < best_log:
            best_log = dp[s]
            best_s = s

    if best_s is None:
        return None, []

    # 重构 q 选择
    chosen = []
    cur = best_s
    while cur > 0 and parent[cur]:
        prev, q = parent[cur]
        chosen.append(q)
        cur = prev
    chosen.sort()
    return best_log, chosen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--cList', default=None)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    args = parser.parse_args()

    if args.cList:
        c_list = [int(x) for x in args.cList.split(',')]
    else:
        c_list = [args.c]

    primes = primes_upto(args.X)
    log10_X = math.log10(args.X)
    print(f'§213 min modulus_required: W={args.W} S={args.S} kLow={args.kLow} X={args.X}')
    print(f'log10(X) = {log10_X:.2f}')
    print()

    Y = 11
    for c in c_list:
        print(f'--- c={c} ---')
        holes = holes_for_c(c, args.W)
        result = full_scan(c, args.W, args.S, args.kLow, args.X,
                           state_limit=8000, residue_limit=14, primes=primes)
        nonzero = result['nonzero_examples']
        if not nonzero:
            print(f'  无 nonzero prefix')
            continue
        D = max(holes) - min(holes)
        for prefix_tuple, _, witness_list in nonzero:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            last_cap = prefix[-1][2]
            used = {t[0] for t in prefix}
            residue, M_pre = prefix_phase(prefix)
            log10_M_pre = math.log10(M_pre)

            # 列出所有未用 q 与 max cap
            q_cap_list = []
            for q in primes_upto(D):
                if q <= Y or q in used:
                    continue
                cap = hot_caps_per_q(holes, q, last_cap)
                if cap > 0:
                    q_cap_list.append((q, cap))

            log_min_q, chosen_qs = min_log_modulus_for_need(q_cap_list, need)
            if log_min_q is None:
                print(f'  prefix_saving={prefix_saving} need={need}: 无法达到 need (M_kill_max < need)')
                print(f'  ★ M_kill_max < need: 无条件通过')
                continue

            log_modulus_required = log10_M_pre + log_min_q
            gap = log_modulus_required - log10_X
            print(f'  prefix_saving={prefix_saving} need={need}')
            print(f'  log10(M_pre) = {log10_M_pre:.2f}')
            print(f'  log10(min ∏ q for need) = {log_min_q:.2f}')
            print(f'  log10(modulus_required) = {log_modulus_required:.2f}')
            print(f'  log10(modulus_required) - log10(X) = {gap:.2f}')
            print(f'  最优 q 选择 ({len(chosen_qs)} 个): {chosen_qs}')
            print(f'  ★ 任何让 M_kill≥need 的 P 必须 ≡ specific class (mod 10^{log_modulus_required:.0f})')
            # Linnik 估计
            for L in [2, 5]:
                P_min_log = log_modulus_required / L
                if P_min_log > log10_X:
                    print(f'  Linnik L={L}: P_min ≳ 10^{P_min_log:.2f} > X=10^{log10_X:.2f} ✓ 不可达')
                else:
                    print(f'  Linnik L={L}: P_min ≳ 10^{P_min_log:.2f} ≤ X=10^{log10_X:.2f} ✗ 可达')
            print()


if __name__ == '__main__':
    main()
