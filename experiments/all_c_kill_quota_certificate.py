#!/usr/bin/env python3
"""遍历所有 B11 单位相位 c，对每个 c 验证 k+1 强制的杀死配额证书。

策略：每个 c 上跑 k_below 完整扫描得到非零屏障前缀 N_c；
然后对每个 (P_below, P_witness) 计算 M_kill 并检查 M_kill < S - prefix_saving。

任何 (c, P_below, P_witness) 不满足该不等式即为"杀死配额证书未通过"，
需要更细分析。

用法：
    python3 experiments/all_c_kill_quota_certificate.py --W 100 --S 55 \
        --kBelow 10 --X 1000000 --stateLimit 1500 --residueLimit 8 --maxC 480
"""
from __future__ import annotations

import argparse
import math
import sys
import time

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from kill_quota_certificate import certify_c, kill_quota
from prefix_completion_bound import full_scan, residue_rows_ranked
from skeleton_union_bound import M, q_residue_options
from b11_segment_cover_branch import holes_for_c


def units_mod_M():
    return [c for c in range(1, M) if math.gcd(c, M) == 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kBelow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=1500)
    parser.add_argument('--residueLimit', type=int, default=8)
    parser.add_argument('--quotaResidueLimit', type=int, default=24)
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
    }
    failing_records = []
    t0 = time.time()
    for i, c in enumerate(cs):
        # full_scan 找非零前缀
        scan = full_scan(c, args.W, args.S, args.kBelow, args.X,
                         state_limit=args.stateLimit,
                         residue_limit=args.residueLimit,
                         primes=primes, verbose=False)
        nonzero = scan['nonzero_examples']
        if not nonzero:
            summary['no_nonzero_prefix'] += 1
            elapsed = time.time() - t0
            if (i + 1) % 20 == 0:
                print(f'  [{i+1}/{len(cs)}] c={c} no nonzero (saving<S 内不需证书) t={elapsed:.0f}s',
                      flush=True)
            continue

        # 对每个 nonzero prefix 跑 kill_quota
        holes = holes_for_c(c, args.W)
        opts = q_residue_options(holes)
        rows = residue_rows_ranked(opts, args.quotaResidueLimit)

        c_pass = 0
        c_fail = 0
        for prefix_tuple, _, witness_list in nonzero:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = args.S - prefix_saving
            for witness in witness_list:
                P = witness[0] if isinstance(witness, tuple) else witness
                quota = kill_quota(prefix, P, rows, residue_limit=args.quotaResidueLimit)
                summary['total_witnesses'] += 1
                if quota['M_kill'] < need:
                    c_pass += 1
                    summary['pass_witnesses'] += 1
                else:
                    c_fail += 1
                    summary['fail_witnesses'] += 1
                    failing_records.append((c, P, prefix_saving, quota['M_kill'], need, prefix))

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
    if failing_records:
        print(f'=== 失败 (c, P, prefix_saving, M_kill, need) 前 {args.show} 个 ===')
        for c, P, ps, mk, nd, _ in failing_records[:args.show]:
            print(f'  c={c} P={P} prefix_saving={ps} M_kill={mk} need={nd}')
    else:
        print('所有 c 的杀死配额证书通过！')


if __name__ == '__main__':
    main()
