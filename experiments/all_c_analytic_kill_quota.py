#!/usr/bin/env python3
"""遍历所有 B11 单位相位 c，用 §201 解析公式给出 k+1 强制的杀死配额证书。

与 all_c_kill_quota_certificate.py 不同：本脚本对每个 c 上的 (prefix, P_witness)
计算 M_kill 用 §201 公式（O(D log D)），而不是逐 (q, r) 枚举。
这给出无截断的真值 M_kill 上界。

但仍依赖 full_scan 找出 N_c（k_below 非零前缀集），故 c-级总时间仍受 full_scan 主导。

用法：
    python3 experiments/all_c_analytic_kill_quota.py --W 100 --S 55 \
        --kBelow 10 --X 1000000 --stateLimit 1500 --residueLimit 7
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
    parser.add_argument('--kBelow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=1500)
    parser.add_argument('--residueLimit', type=int, default=7)
    parser.add_argument('--maxC', type=int, default=None)
    parser.add_argument('--show', type=int, default=15)
    args = parser.parse_args()

    cs = units_mod_M()
    if args.maxC:
        cs = cs[:args.maxC]
    print(f'扫描 {len(cs)} 个相位 c (W={args.W} S={args.S} kBelow={args.kBelow} X={args.X})')
    print(f'构建共享素数表 X={args.X}...', flush=True)
    primes = primes_upto(args.X)
    print(f'素数表 {len(primes)}', flush=True)

    summary = {
        'total_c': len(cs),
        'no_nonzero_prefix': 0,
        'all_witnesses_pass': 0,
        'has_failing_witness': 0,
        'total_witnesses': 0,
        'pass_witnesses': 0,
        'fail_witnesses': 0,
        'mod_dominant_count': 0,
        'mod_not_dominant_count': 0,
    }
    failing = []
    t0 = time.time()
    for i, c in enumerate(cs):
        scan = full_scan(c, args.W, args.S, args.kBelow, args.X,
                         state_limit=args.stateLimit,
                         residue_limit=args.residueLimit,
                         primes=primes, verbose=False)
        nonzero = scan['nonzero_examples']
        if not nonzero:
            summary['no_nonzero_prefix'] += 1
            elapsed = time.time() - t0
            if (i + 1) % 20 == 0:
                print(f'  [{i+1}/{len(cs)}] c={c} no nonzero t={elapsed:.0f}s', flush=True)
            continue

        holes = holes_for_c(c, args.W)
        c_pass = 0
        c_fail = 0
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
                if base_modulus > P - A_old:
                    summary['mod_dominant_count'] += 1
                else:
                    summary['mod_not_dominant_count'] += 1
                quota = analytic_M_kill(holes, A_old, P, used_qs, last_cap)
                summary['total_witnesses'] += 1
                if quota['M_kill'] < need:
                    c_pass += 1
                    summary['pass_witnesses'] += 1
                else:
                    c_fail += 1
                    summary['fail_witnesses'] += 1
                    failing.append((c, P, A_old, prefix_saving, quota['M_kill'], need, prefix))

        if c_fail == 0:
            summary['all_witnesses_pass'] += 1
        else:
            summary['has_failing_witness'] += 1
        elapsed = time.time() - t0
        if c_fail > 0 or (i + 1) % 20 == 0:
            print(f'  [{i+1}/{len(cs)}] c={c} nz_prefixes={len(nonzero)} '
                  f'pass={c_pass} fail={c_fail} t={elapsed:.0f}s', flush=True)

    print()
    print('=== 总结 ===')
    for k, v in summary.items():
        print(f'  {k}: {v}')
    print()
    if failing:
        print(f'=== 失败 (c, P, A_old, prefix_saving, M_kill, need) 前 {args.show} 个 ===')
        for c, P, A, ps, mk, nd, _ in failing[:args.show]:
            print(f'  c={c} P={P} A={A} prefix_saving={ps} M_kill={mk} need={nd}')
    else:
        print('所有 c 的解析杀死配额证书通过（k+1 强制定理在搜索范围内成立）！')


if __name__ == '__main__':
    main()
