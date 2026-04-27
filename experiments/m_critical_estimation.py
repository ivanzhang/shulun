#!/usr/bin/env python3
"""§212 m_critical 与 modulus_required 精确估计。

按 §211.7 路径:
1. 对每 prefix in N_c, 计算 M_kill 累积函数 M_kill(m) = top m 个 q 的 max cap 之和
2. 找 m_critical = min m s.t. M_kill(m) ≥ need
3. 计算 modulus_required = M_pre · ∏_{q∈top_m_critical} q
4. 用 Linnik 估计：该 modulus 类内最小素数 ≳ modulus_required^{1/某指数}
5. 比较与 X 的关系

输出每 c 的 (m_critical, modulus_required, Linnik 下界, X 比较)。

用法：
    python3 experiments/m_critical_estimation.py --cList 961,1343,2309
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
    """q 上 max cap (under last_cap) for hot 区域 (H ≥ 2)."""
    counts = defaultdict(int)
    for h in holes:
        counts[h % q] += 1
    H_values = list(counts.values())
    max_H = max(H_values) if H_values else 1
    return min(last_cap, max(0, max_H - 1))


def estimate_m_critical(prefix, holes, need: int, last_cap: int) -> dict:
    """对单个 prefix 估计 m_critical 与 modulus_required."""
    used = {t[0] for t in prefix}
    residue, M_pre = prefix_phase(prefix)

    # 列出所有未用 q 与对应最大 hot cap
    Y = 11
    D = max(holes) - min(holes) if holes else 0
    primes_q = [p for p in primes_upto(D) if p > Y and p not in used]

    # 对每 q 计算 max cap
    q_caps = []
    for q in primes_q:
        cap = hot_caps_per_q(holes, q, last_cap)
        if cap > 0:
            q_caps.append((q, cap))
    # 按 cap 降序，q 升序
    q_caps.sort(key=lambda x: (-x[1], x[0]))

    # 计算 M_kill(m) 累积
    cum_M = 0
    m_critical = None
    cum_mod_log10 = math.log10(M_pre)
    for m, (q, cap) in enumerate(q_caps, 1):
        cum_M += cap
        cum_mod_log10 += math.log10(q)
        if cum_M >= need:
            m_critical = m
            break

    if m_critical is None:
        return {
            'prefix_saving': sum(t[2] for t in prefix),
            'need': need,
            'M_pre': M_pre,
            'log10_M_pre': math.log10(M_pre),
            'sum_max_cap': cum_M,
            'm_critical': None,  # M_kill 总和不达 need ⇒ 任何 P 都通过
            'unconditional_pass': True,
            'q_caps_top10': q_caps[:10],
        }
    else:
        # modulus_required = M_pre · ∏_{i=1}^{m_critical} q_i
        modulus_required_log10 = math.log10(M_pre)
        for i in range(m_critical):
            modulus_required_log10 += math.log10(q_caps[i][0])

        # Linnik 估计：最坏 P ≳ modulus_required^{1/L} 但实际现代估计是
        # P_min(a, m) ≪ m^L for 某 L = 5 (Xylouris)，但这是平均；
        # GRH 下 P_min(a, m) ~ m · log²m
        # 我们用保守: P_min ≳ modulus_required (类似 Bertrand 类)
        return {
            'prefix_saving': sum(t[2] for t in prefix),
            'need': need,
            'M_pre': M_pre,
            'log10_M_pre': math.log10(M_pre),
            'log10_modulus_required': modulus_required_log10,
            'm_critical': m_critical,
            'top_qs': [q for q, _ in q_caps[:m_critical]],
            'unconditional_pass': False,
            'q_caps_top10': q_caps[:10],
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--cList', default=None)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--useKnownPrefix', action='store_true')
    args = parser.parse_args()

    if args.cList:
        c_list = [int(x) for x in args.cList.split(',')]
    else:
        c_list = [args.c]

    primes = primes_upto(args.X)
    log10_X = math.log10(args.X)
    print(f'§212 m_critical 估计 W={args.W} S={args.S} kLow={args.kLow} X={args.X}')
    print(f'log10(X) = {log10_X:.2f}')
    print()

    summary_records = []
    for c in c_list:
        print(f'--- c={c} ---')
        holes = holes_for_c(c, args.W)
        result = full_scan(c, args.W, args.S, args.kLow, args.X,
                           state_limit=8000, residue_limit=14, primes=primes)
        nonzero = result['nonzero_examples']
        if not nonzero:
            print(f'  无 nonzero prefix')
            continue
        for prefix_tuple, _, witness_list in nonzero:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            last_cap = prefix[-1][2]
            est = estimate_m_critical(prefix, holes, need, last_cap)

            print(f'  prefix_saving={prefix_saving} need={need} last_cap={last_cap}')
            print(f'  log10(M_pre) = {est["log10_M_pre"]:.2f}')
            if est['unconditional_pass']:
                print(f'  ★ M_kill 上界 {est["sum_max_cap"]} < need={need}: 无条件通过！')
            else:
                print(f'  m_critical = {est["m_critical"]}')
                print(f'  log10(modulus_required) = {est["log10_modulus_required"]:.2f}')
                print(f'  比较 log10(X) = {log10_X:.2f}')
                # 最简单的估计：假设 P_min ~ modulus_required (Linnik 上界)
                gap = est['log10_modulus_required'] - log10_X
                print(f'  log10(modulus_required) - log10(X) = {gap:.2f}')
                if gap > 0:
                    print(f'  ★ modulus_required > X: 反例 P 必须 ≳ 10^{est["log10_modulus_required"]:.0f}, 远超 X')
                print(f'  top_qs (前 {est["m_critical"]}): {est["top_qs"]}')
            print(f'  q_caps_top10: {est["q_caps_top10"]}')
            print()
            summary_records.append((c, est))

    print('=' * 60)
    print('总结')
    print('=' * 60)
    if summary_records:
        max_gap = max(r[1].get('log10_modulus_required', 0) - log10_X for r in summary_records
                       if not r[1].get('unconditional_pass'))
        print(f'最大 log10(modulus_required) - log10(X) = {max_gap:.2f}')
        unconditional_pass_count = sum(1 for r in summary_records if r[1].get('unconditional_pass'))
        print(f'无条件通过的 prefix 数: {unconditional_pass_count}/{len(summary_records)}')


if __name__ == '__main__':
    main()
