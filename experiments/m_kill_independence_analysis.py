#!/usr/bin/env python3
"""§210 M_kill 的解析上界：r_unkill_q 在不同 q 上的相关性研究。

§204+§207 实测：所有反例 (prefix, P) 满足 margin=need-M_kill≥2，且最小余量稳定 = 2。
本节给出该现象的解析解释。

核心问题：M_kill = Σ_q min(last_cap, max(0, H_holes(q, r_unkill_q)-1))
其中 r_unkill_q = -A_old · P^{-1} (mod q)。

每 q 上：r_unkill_q 是确定值，依赖 (prefix, P)。
不同 q 之间：r_unkill_q 是否独立、是否在 q-余数集上均匀分布？

如果独立均匀，则：
- E[(H_holes(q,r)-1)_+] = sum_cap_q / q
- E[M_kill] ≈ Σ_q sum_cap_q/q
- Var[M_kill] ≤ Σ_q (variance per q)

可用 Chernoff 给 P[M_kill ≥ need] 上界。

本节实施：
1. 对 c=2309 收集所有 (prefix, P) 反例对应的 r_unkill 序列
2. 测量 r_unkill_q 的分布（与均匀分布的 KL 散度）
3. 给出 M_kill 的实测值与解析期望对比

用法：
    python3 experiments/m_kill_independence_analysis.py --c 2309
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from analytic_kill_quota import analytic_M_kill, holes_count_at_residue
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase
from prefix_completion_bound import full_scan
from skeleton_union_bound import q_residue_options


def collect_runkill_sequences(c, W, S, k_low, X):
    """对 c 上所有 (prefix, P) 反例收集 r_unkill_q 序列。"""
    primes = primes_upto(X)
    holes = holes_for_c(c, W)
    result = full_scan(c, W, S, k_low, X,
                       state_limit=20000, residue_limit=24,
                       primes=primes, verbose=False)

    runkill_records = []
    for prefix_tuple, _, witness_list in result['nonzero_examples']:
        prefix = list(prefix_tuple)
        prefix_saving = sum(t[2] for t in prefix)
        used = {t[0] for t in prefix}
        last_cap = prefix[-1][2]
        residue, modulus = prefix_phase(prefix)
        for witness in witness_list:
            P = witness[0]
            A_old = prefix_anchor_from_phase(residue, modulus, P)
            # 对每个未用 q，记录 r_unkill_q
            r_unkill_seq = {}
            D = max(holes) - min(holes)
            for q in primes_upto(D):
                if q <= 11 or q in used:
                    continue
                try:
                    P_inv = pow(P % q, -1, q)
                except ValueError:
                    continue
                r_unkill_seq[q] = (-A_old * P_inv) % q
            runkill_records.append({
                'prefix': prefix,
                'P': P,
                'A_old': A_old,
                'prefix_saving': prefix_saving,
                'need': S - prefix_saving,
                'last_cap': last_cap,
                'r_unkill_seq': r_unkill_seq,
            })
    return runkill_records, holes


def compute_per_q_stats(holes, q_set):
    """对每个 q 计算 H_holes 分布与最大 cap。"""
    stats = {}
    for q in q_set:
        counts = Counter()
        for h in holes:
            counts[h % q] += 1
        H_values = list(counts.values())
        H_dist = Counter(H_values)
        max_H = max(H_values) if H_values else 0
        sum_cap = sum(h - 1 for h in H_values if h >= 2)
        n_hot = sum(1 for h in H_values if h >= 2)
        stats[q] = {
            'max_H': max_H,
            'sum_cap': sum_cap,
            'n_hot': n_hot,
            'n_distinct_r': len(H_values),
            'H_dist': dict(H_dist),
        }
    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--cList', default=None,
                        help='多 c 用逗号分隔, e.g. 961,1343,2309')
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    args = parser.parse_args()

    if args.cList:
        c_list = [int(x) for x in args.cList.split(',')]
    else:
        c_list = [args.c]

    print(f'§210 M_kill 解析分析: c_list={c_list}, k_low={args.kLow}')
    print()
    records = []
    holes_per_c = {}
    for c in c_list:
        recs, holes = collect_runkill_sequences(c, args.W, args.S, args.kLow, args.X)
        for rec in recs:
            rec['c'] = c
            records.append(rec)
        holes_per_c[c] = holes
        print(f'  c={c}: {len(recs)} 反例')

    print(f'反例 (prefix, P) 总数: {len(records)}')
    holes = holes_per_c[c_list[-1]] if c_list else []

    if not records:
        return

    # 收集所有 q
    all_qs = set()
    for rec in records:
        all_qs |= set(rec['r_unkill_seq'].keys())
    all_qs = sorted(all_qs)
    print(f'未用 q 集合大小: {len(all_qs)}')

    # 每 q 的 stats
    q_stats = compute_per_q_stats(holes, all_qs)

    # 收集每个 q 的实际 r_unkill 出现频率
    r_observed = defaultdict(Counter)
    for rec in records:
        for q, r in rec['r_unkill_seq'].items():
            r_observed[q][r] += 1

    # 比较：对每个 q 看 r_unkill 是否落在 hot 区域 (H_holes ≥ 2)
    n_hot_landings = 0
    n_total = 0
    margins = []
    print('\n每 (c, prefix, P) 的 M_kill 与 hot landings:')
    print(f'{"i":>3} {"c":>5} {"P":>10} {"M_kill":>7} {"need":>5} {"margin":>7} {"hot":>5}/{"qs":>3}')
    for i, rec in enumerate(records):
        used = {t[0] for t in rec['prefix']}
        c_for_holes = rec['c']
        local_holes = holes_per_c[c_for_holes]
        M_kill = analytic_M_kill(local_holes, rec['A_old'], rec['P'], used, rec['last_cap'])['M_kill']
        hot = 0
        for q, r in rec['r_unkill_seq'].items():
            H = holes_count_at_residue(local_holes, q, r)
            if H >= 2:
                hot += 1
                n_hot_landings += 1
            n_total += 1
        margin = rec['need'] - M_kill
        margins.append(margin)
        print(f'{i:>3} {rec["c"]:>5} {rec["P"]:>10} {M_kill:>7} {rec["need"]:>5} {margin:>7} {hot:>5}/{len(rec["r_unkill_seq"]):>3}')

    print(f'\n总 hot landings: {n_hot_landings}/{n_total}, ratio={n_hot_landings/max(1,n_total):.3f}')
    if margins:
        print(f'margin 分布: min={min(margins)}, max={max(margins)}, mean={sum(margins)/len(margins):.2f}')

    # 比较：随机 r 模型下的预期 hot rate
    expected_hot = sum(stat['n_hot'] / stat['n_distinct_r']
                       if stat['n_distinct_r'] else 0
                       for stat in q_stats.values()) / max(1, len(q_stats))
    # 严格：hot rate per q = n_hot/q (因为 r ∈ [0, q-1])
    expected_hot_per_q = sum(stat['n_hot'] / q for q, stat in q_stats.items()) / max(1, len(q_stats))
    print(f'\n随机模型下预期 hot rate (n_hot/q): {expected_hot_per_q:.3f}')
    print(f'实测 hot rate: {n_hot_landings/max(1,n_total):.3f}')

    # 看每 q 的 r_unkill 分布（是否均匀）
    print('\n每 q 的 r_unkill 分布（前 5 个 q）:')
    for q in sorted(all_qs)[:5]:
        observed = r_observed[q]
        if not observed:
            continue
        hot_r_observed = sum(c for r, c in observed.items()
                              if holes_count_at_residue(holes, q, r) >= 2)
        total = sum(observed.values())
        print(f'  q={q}: observed_r_count={len(observed)}, total={total}, '
              f'hot_landings={hot_r_observed}, n_hot/q={q_stats[q]["n_hot"]}/{q}')


if __name__ == '__main__':
    main()
