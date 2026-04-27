#!/usr/bin/env python3
"""§216 一般化参数 W 下的证书：把 §204+§215 推广到任意 W。

策略：固定 S=W·0.55, k_low=10, X=30·P·W·10^k 适当大。对所有 c 反例做完整证书。

用法：
    python3 experiments/general_W_certificate.py --W 200 --S 110 --kLow 10 --X 10000000
"""
from __future__ import annotations

import argparse
import math
import sys
import time
from typing import List

sys.path.append('experiments')
from analytic_kill_quota import analytic_M_kill
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase
from prefix_completion_bound import full_scan
from skeleton_union_bound import M as B11_M


def units_mod_M():
    return [c for c in range(1, B11_M) if math.gcd(c, B11_M) == 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=200)
    parser.add_argument('--S', type=int, default=110)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--stateLimit', type=int, default=2000)
    parser.add_argument('--residueLimit', type=int, default=10)
    parser.add_argument('--maxC', type=int, default=None)
    args = parser.parse_args()

    cs = units_mod_M()
    if args.maxC:
        cs = cs[:args.maxC]

    print(f'§216 一般化 W 证书: W={args.W}, S={args.S}, k_low={args.kLow}, X={args.X}')
    print(f'扫描 {len(cs)} 个相位 c (state={args.stateLimit}, residue={args.residueLimit})')

    print('构建素数表...', flush=True)
    primes = primes_upto(args.X)
    print(f'素数表 {len(primes)}', flush=True)

    summary = {
        'total_c': len(cs),
        'no_nonzero': 0,
        'has_nonzero': 0,
        'pass_witnesses': 0,
        'fail_witnesses': 0,
        'worst_M_kill': 0,
        'worst_margin': 999,
    }
    fails = []
    nz_records = []
    t0 = time.time()
    for i, c in enumerate(cs):
        result = full_scan(c, args.W, args.S, args.kLow, args.X,
                           state_limit=args.stateLimit,
                           residue_limit=args.residueLimit,
                           primes=primes, verbose=False)
        nz = result['nonzero_examples']
        if not nz:
            summary['no_nonzero'] += 1
            elapsed = time.time() - t0
            if (i + 1) % 30 == 0:
                print(f'  [{i+1}/{len(cs)}] c={c} no_nz t={elapsed:.0f}s', flush=True)
            continue
        summary['has_nonzero'] += 1
        holes = holes_for_c(c, args.W)
        c_pass, c_fail = 0, 0
        for prefix_tuple, _, witness_list in nz:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            last_cap = prefix[-1][2]
            used = {t[0] for t in prefix}
            residue, modulus = prefix_phase(prefix)
            for w in witness_list:
                P = w[0]
                A = prefix_anchor_from_phase(residue, modulus, P)
                quota = analytic_M_kill(holes, A, P, used, last_cap)
                M_kill = quota['M_kill']
                margin = need - M_kill
                if M_kill < need:
                    c_pass += 1
                    summary['pass_witnesses'] += 1
                else:
                    c_fail += 1
                    summary['fail_witnesses'] += 1
                    fails.append((c, P, prefix_saving, M_kill, need, prefix))
                if M_kill > summary['worst_M_kill']:
                    summary['worst_M_kill'] = M_kill
                if margin < summary['worst_margin']:
                    summary['worst_margin'] = margin
        nz_records.append((c, len(nz), c_pass, c_fail))
        elapsed = time.time() - t0
        if c_fail > 0 or len(nz) > 0:
            print(f'  [{i+1}/{len(cs)}] c={c} nz={len(nz)} pass={c_pass} fail={c_fail} t={elapsed:.0f}s', flush=True)

    elapsed = time.time() - t0
    print()
    print('=' * 60)
    print('=== 最终总结 ===')
    print('=' * 60)
    for k, v in summary.items():
        print(f'  {k}: {v}')
    print(f'\n非零屏障 c 列表 (共 {len(nz_records)}):')
    for c, n_nz, n_pass, n_fail in nz_records:
        print(f'  c={c} nz={n_nz} pass={n_pass} fail={n_fail}')
    if fails:
        print(f'\n失败 (M_kill ≥ need) 列表:')
        for c, P, ps, M, n, _ in fails[:10]:
            print(f'  c={c} P={P} ps={ps} M={M} need={n}')
    else:
        if summary['has_nonzero'] > 0:
            print(f'\n★ 全部 {summary["pass_witnesses"]} 个 (prefix, witness) 通过 (⋆)')
        else:
            print(f'\n★★ 全 {len(cs)} c 在 W={args.W}, S={args.S} 下无非零屏障 prefix')
            print(f'   即 §216 一般化 W 证书在该参数下空集通过')
    print(f'\n总耗时 {elapsed:.0f}s ({elapsed/60:.1f} min)')


if __name__ == '__main__':
    main()
