#!/usr/bin/env python3
"""§214 全 480 c 的 modulus_required 证书。

对每 c 找反例 prefix，跑 DP 求 min modulus_required，
判断是否 modulus_required ≫ X (即 (⋆_∞) 严格成立的密度论证)。

输出每 c 的 (反例数, min log10(modulus_required), gap with X)。

用法：
    python3 experiments/full_modulus_certificate.py
"""
from __future__ import annotations

import argparse
import math
import sys
import time

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from min_modulus_for_need import min_log_modulus_for_need, hot_caps_per_q
from prefix_barrier_library import prefix_phase
from prefix_completion_bound import full_scan
from skeleton_union_bound import M as M_b11


def units_mod_M():
    return [c for c in range(1, M_b11) if math.gcd(c, M_b11) == 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=1500)
    parser.add_argument('--residueLimit', type=int, default=7)
    parser.add_argument('--maxC', type=int, default=None)
    args = parser.parse_args()

    cs = units_mod_M()
    if args.maxC:
        cs = cs[:args.maxC]

    primes = primes_upto(args.X)
    log10_X = math.log10(args.X)
    Y = 11

    print(f'§214 全 c 的 min modulus_required 证书')
    print(f'参数: W={args.W} S={args.S} kLow={args.kLow} X={args.X}')
    print(f'log10(X) = {log10_X:.2f}')
    print(f'扫描 {len(cs)} 个 c...', flush=True)
    print()

    nonzero_cs = []
    summary_records = []
    t0 = time.time()
    for i, c in enumerate(cs):
        result = full_scan(c, args.W, args.S, args.kLow, args.X,
                           state_limit=args.stateLimit,
                           residue_limit=args.residueLimit,
                           primes=primes, verbose=False)
        nonzero = result['nonzero_examples']
        if not nonzero:
            if (i + 1) % 50 == 0:
                elapsed = time.time() - t0
                print(f'  [{i+1}/{len(cs)}] c={c} no_nz t={elapsed:.0f}s', flush=True)
            continue
        nonzero_cs.append(c)
        # 对该 c 跑 DP
        holes = holes_for_c(c, args.W)
        D = max(holes) - min(holes)
        for prefix_tuple, _, witness_list in nonzero:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            last_cap = prefix[-1][2]
            used = {t[0] for t in prefix}
            residue, M_pre = prefix_phase(prefix)
            log10_M_pre = math.log10(M_pre)

            # 列出所有未用 q 与 max cap (cap ≤ last_cap, hot only)
            q_cap_list = []
            for q in primes_upto(D):
                if q <= Y or q in used:
                    continue
                cap = hot_caps_per_q(holes, q, last_cap)
                if cap > 0:
                    q_cap_list.append((q, cap))

            log_min_q, chosen_qs = min_log_modulus_for_need(q_cap_list, need)
            if log_min_q is None:
                # M_kill_max < need，无条件通过
                summary_records.append({
                    'c': c, 'prefix_saving': prefix_saving, 'need': need,
                    'unconditional_pass': True,
                    'log10_modulus_required': None,
                })
                print(f'  c={c} ★ M_kill_max < need={need} (无条件通过)', flush=True)
                continue
            log_modulus_required = log10_M_pre + log_min_q
            gap = log_modulus_required - log10_X
            summary_records.append({
                'c': c, 'prefix_saving': prefix_saving, 'need': need,
                'log10_M_pre': log10_M_pre,
                'log10_modulus_required': log_modulus_required,
                'gap': gap,
                'chosen_qs': chosen_qs,
            })
            elapsed = time.time() - t0
            P = witness_list[0][0] if witness_list else None
            print(f'  c={c:>5} P={P:<10} need={need} '
                  f'log10(modulus_req)={log_modulus_required:.2f} '
                  f'gap={gap:.2f} chosen_qs={chosen_qs} t={elapsed:.0f}s', flush=True)

    elapsed = time.time() - t0
    print()
    print('=' * 60)
    print('总结')
    print('=' * 60)
    print(f'总 c 数: {len(cs)}')
    print(f'有 nonzero prefix 的 c 数: {len(nonzero_cs)}')
    print(f'反例 c 列表: {sorted(nonzero_cs)}')
    if summary_records:
        gaps = [r['gap'] for r in summary_records if 'gap' in r]
        if gaps:
            print(f'\n反例 prefix 数: {len(summary_records)}')
            print(f'min log10(modulus_required) = {min(r["log10_modulus_required"] for r in summary_records if r.get("log10_modulus_required")):.2f}')
            print(f'min gap = {min(gaps):.2f}')
            print(f'max gap = {max(gaps):.2f}')
            print(f'avg gap = {sum(gaps)/len(gaps):.2f}')

            # X 内候选数估计
            print(f'\n密度论证:')
            print(f'  对每 c, [0, X] 内反例 P ≡ a (mod modulus_required) 的候选数 ≤ ⌈X/modulus_required⌉')
            for r in summary_records:
                if 'log10_modulus_required' in r and r['log10_modulus_required']:
                    log_x_over_m = log10_X - r['log10_modulus_required']
                    print(f'  c={r["c"]}: log10(X/modulus_required) = {log_x_over_m:.2f}, '
                          f'候选数 ≤ 10^{log_x_over_m:.0f} = {"≪ 1" if log_x_over_m < -1 else "?"}')

    print(f'\n总耗时: {elapsed:.0f}s')


if __name__ == '__main__':
    main()
