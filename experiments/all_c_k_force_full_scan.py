#!/usr/bin/env python3
"""遍历所有 B11 单位相位 c，对每个 c 做 k 前缀强制完整扫描。

对每个 c 用 prefix_completion_bound.full_scan 找出 saving≥S 的所有前缀类型，
统计其中非零屏障数。任何 c 出现 nonzero>0 即给出 k 强制定理反例。

用法：
    python3 experiments/all_c_k_force_full_scan.py --W 100 --S 55 --k 11 \
        --X 1000000 --stateLimit 2000 --residueLimit 8 --maxC 30
"""
from __future__ import annotations

import argparse
import math
import sys
import time

sys.path.append('experiments')
from prefix_completion_bound import full_scan
from fixed_anchor_sieve_remainder import primes_upto
from skeleton_union_bound import M


def units_mod_M():
    return [c for c in range(1, M) if math.gcd(c, M) == 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--k', type=int, default=11)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=2000)
    parser.add_argument('--residueLimit', type=int, default=8)
    parser.add_argument('--keepSignature', type=int, default=12)
    parser.add_argument('--maxC', type=int, default=None,
                        help='只跑前 N 个单位相位（全 480 太慢时截断）')
    parser.add_argument('--show', type=int, default=10)
    args = parser.parse_args()

    cs = units_mod_M()
    if args.maxC:
        cs = cs[:args.maxC]
    print(f'扫描 {len(cs)} 个单位相位 c (W={args.W} S={args.S} k={args.k} X={args.X})')
    print(f'构建共享素数表 X={args.X}...', flush=True)
    primes = primes_upto(args.X)
    print(f'素数表大小 {len(primes)}', flush=True)

    summary = {
        'total_c': len(cs),
        'all_zero': 0,
        'has_nonzero': 0,
        'budget_exhausted': 0,
        'total_unique_prefixes': 0,
        'total_zero': 0,
        'total_nonzero': 0,
    }
    nonzero_records = []
    t0 = time.time()
    for i, c in enumerate(cs):
        result = full_scan(c, args.W, args.S, args.k, args.X,
                           state_limit=args.stateLimit,
                           residue_limit=args.residueLimit,
                           keep_signature=args.keepSignature,
                           verbose=False,
                           primes=primes)
        nz = result['nonzero_prefixes']
        summary['total_unique_prefixes'] += result['unique_prefixes_checked']
        summary['total_zero'] += result['zero_prefixes']
        summary['total_nonzero'] += nz
        if result['deadline_hit']:
            summary['budget_exhausted'] += 1
        if nz > 0:
            summary['has_nonzero'] += 1
            nonzero_records.append((c, nz, result['nonzero_examples'][:1]))
        else:
            summary['all_zero'] += 1
        elapsed = time.time() - t0
        if (i + 1) % 5 == 0 or nz > 0:
            print(f'  [{i+1}/{len(cs)}] c={c} prefixes={result["unique_prefixes_checked"]} '
                  f'nz={nz} t={elapsed:.0f}s', flush=True)

    print()
    print('=== 总结 ===')
    for k, v in summary.items():
        print(f'  {k}: {v}')
    if nonzero_records:
        print(f'\n=== 非零屏障 c 列表（前 {args.show}） ===')
        for c, nz, ex in nonzero_records[:args.show]:
            print(f'  c={c} nz={nz} example={ex}')
    else:
        print('\n所有 c 在搜索范围内 k 前缀强制成立！')


if __name__ == '__main__':
    main()
