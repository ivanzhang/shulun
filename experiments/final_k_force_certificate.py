#!/usr/bin/env python3
"""§203 最终 k+1 强制定理严格证书：全 480 c × k_low=10 完整证书。

把 §200-§202 的证明骨架闭合到目标命题：
对每 c 的 N_{c, k_low}，对每个 (prefix, P_witness) 用 §201 解析 M_kill 公式
验证 M_kill < need。所有通过即完成 k_low+1 强制定理（在搜索范围内）的严格证明。

输出：
- 全局总结：c 数、N_{c, k_low} 元素总数、(prefix, P) 三元组数、通过数、最坏 (M_kill, need, margin)
- 失败列表：任何不通过的三元组

用法：
    python3 experiments/final_k_force_certificate.py --W 100 --S 55 \
        --kLow 10 --X 1000000 --stateLimit 4000 --residueLimit 10
"""
from __future__ import annotations

import argparse
import math
import sys
import time

sys.path.append('experiments')
from analytic_kill_quota import analytic_M_kill
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase
from prefix_completion_bound import full_scan
from skeleton_union_bound import M


def units_mod_M():
    return [c for c in range(1, M) if math.gcd(c, M) == 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=4000)
    parser.add_argument('--residueLimit', type=int, default=10)
    parser.add_argument('--maxC', type=int, default=None)
    parser.add_argument('--show', type=int, default=15)
    args = parser.parse_args()

    cs = units_mod_M()
    if args.maxC:
        cs = cs[:args.maxC]
    print(f'最终证书 W={args.W} S={args.S} kLow={args.kLow} X={args.X}')
    print(f'扫描 {len(cs)} 个 c (state={args.stateLimit} residue={args.residueLimit})')
    print(f'构建素数表...', flush=True)
    primes = primes_upto(args.X)
    print(f'素数表 {len(primes)}', flush=True)

    summary = {
        'total_c': len(cs),
        'no_nonzero_c': 0,
        'has_nonzero_c': 0,
        'fail_c': 0,
        'total_witnesses': 0,
        'pass_witnesses': 0,
        'fail_witnesses': 0,
        'worst_M_kill': 0,
        'worst_margin': 9999,
        'worst_record': None,
    }
    fail_list = []
    margin_distribution = []
    t0 = time.time()
    for i, c in enumerate(cs):
        scan = full_scan(c, args.W, args.S, args.kLow, args.X,
                         state_limit=args.stateLimit,
                         residue_limit=args.residueLimit,
                         primes=primes, verbose=False)
        nonzero = scan['nonzero_examples']
        if not nonzero:
            summary['no_nonzero_c'] += 1
            elapsed = time.time() - t0
            if (i + 1) % 30 == 0:
                print(f'  [{i+1}/{len(cs)}] c={c} no_nz t={elapsed:.0f}s', flush=True)
            continue

        summary['has_nonzero_c'] += 1
        holes = holes_for_c(c, args.W)
        c_fails = 0
        for prefix_tuple, _, witness_list in nonzero:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            last_cap = prefix[-1][2]
            used_qs = {t[0] for t in prefix}
            base_residue, base_modulus = prefix_phase(prefix)
            for witness in witness_list:
                P = witness[0] if isinstance(witness, tuple) else witness
                A_old = prefix_anchor_from_phase(base_residue, base_modulus, P)
                quota = analytic_M_kill(holes, A_old, P, used_qs, last_cap)
                M_kill = quota['M_kill']
                margin = need - M_kill
                summary['total_witnesses'] += 1
                margin_distribution.append(margin)
                if M_kill > summary['worst_M_kill']:
                    summary['worst_M_kill'] = M_kill
                if margin < summary['worst_margin']:
                    summary['worst_margin'] = margin
                    summary['worst_record'] = (c, P, A_old, prefix_saving, M_kill, need, prefix)
                if M_kill < need:
                    summary['pass_witnesses'] += 1
                else:
                    summary['fail_witnesses'] += 1
                    c_fails += 1
                    fail_list.append((c, P, A_old, prefix_saving, M_kill, need, prefix))
        if c_fails > 0:
            summary['fail_c'] += 1

        elapsed = time.time() - t0
        if c_fails > 0 or (i + 1) % 30 == 0:
            print(f'  [{i+1}/{len(cs)}] c={c} nz={len(nonzero)} '
                  f'fails={c_fails} t={elapsed:.0f}s', flush=True)

    elapsed = time.time() - t0
    print()
    print('=' * 60)
    print('=== 最终证书总结 ===')
    print('=' * 60)
    for k, v in summary.items():
        if k != 'worst_record':
            print(f'  {k}: {v}')
    rec = summary['worst_record']
    if rec:
        c, P, A, ps, M, n, _ = rec
        print(f'  worst_record: c={c} P={P} A_old={A} prefix_saving={ps} M_kill={M} need={n} margin={n-M}')
    print()
    if fail_list:
        print(f'=== 失败列表（共 {len(fail_list)}） 前 {args.show} ===')
        for c, P, A, ps, M, n, _ in fail_list[:args.show]:
            print(f'  c={c} P={P} A={A} ps={ps} M_kill={M} need={n}')
    else:
        print(f'★★★ 全 {summary["total_witnesses"]} 个 (prefix, witness) 三元组全部通过！ ★★★')
        print(f'k+1 强制定理在 W={args.W} S={args.S} k_low={args.kLow} X={args.X} 范围内严格证明完成。')
    print()
    print(f'总耗时 {elapsed:.0f}s ({elapsed/60:.1f} min)')

    # margin 分布
    if margin_distribution:
        margin_distribution.sort()
        print()
        print('=== margin 分布 ===')
        for q in [0.0, 0.05, 0.25, 0.5, 0.75, 0.95, 1.0]:
            idx = int(q * (len(margin_distribution) - 1))
            print(f'  {int(q*100):>3}% : margin = {margin_distribution[idx]}')


if __name__ == '__main__':
    main()
