#!/usr/bin/env python3
"""前缀完成上界与 k 前缀强制有限证书工具。

第197-198节给出 k=11 前缀全相位零屏障的束搜索经验。本脚本提供两类工具：

1) max_completable_saving(used_qs, last_cap, opts):
   给定一组已选 q 与最低 cap，剩余 q 中容量 ≤ last_cap 的最大可补 saving。
   这是把"k 前缀强制"升级为有限证书的关键剪枝量。

2) full_scan(c, W, S, k, X, ...):
   类似 prefix_force_counterexample_search.search，但找到反例后不停止，
   累积所有"saving≥S 且前 k 前缀类型"的零/非零屏障统计。
   目的是给出"该 c 上 k 前缀强制是否成立"的完整证据。

用法：
    python3 experiments/prefix_completion_bound.py --c 2309 --W 100 --S 55 --k 10 \
        --X 1000000 --stateLimit 8000 --residueLimit 14
    python3 experiments/prefix_completion_bound.py --c 2309 --W 100 --S 55 --k 11 \
        --X 1000000 --stateLimit 8000 --residueLimit 14
"""
from __future__ import annotations

import argparse
import math
import sys
import time
from typing import Dict, List, Tuple

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_key, survivor_count
from skeleton_union_bound import q_residue_options


Triple = Tuple[int, int, int]


def residue_rows_ranked(opts, residue_limit: int):
    rows = []
    for q, residue_rows in opts:
        ranked = sorted(residue_rows, key=lambda row: (-row[2], row[1]))
        if residue_limit:
            ranked = ranked[:residue_limit]
        rows.append((q, ranked))
    rows.sort(key=lambda item: (-max(row[2] for row in item[1]), item[0]))
    return rows


def state_signature(chosen, keep: int):
    ordered = sorted(chosen, key=lambda row: (-row[2], row[0], row[1]))
    return tuple((row[0], row[1], row[2]) for row in ordered[:keep])


def remaining_max_caps(rows_after, exclude_qs: set[int]) -> List[int]:
    """rows_after 列表里每个 q 的最大 cap（剔除 exclude_qs）。"""
    out = []
    for q, choices in rows_after:
        if q in exclude_qs:
            continue
        out.append(choices[0][2])
    return out


def max_completable_with_cap(rows_after, exclude_qs: set[int], cap_ceiling: int) -> int:
    """剩余 q 中可补 saving 上界，限制每项 cap ≤ cap_ceiling。"""
    total = 0
    for q, choices in rows_after:
        if q in exclude_qs:
            continue
        for row in choices:
            cap = row[2]
            if cap <= cap_ceiling:
                total += cap
                break  # 每个 q 选一个最大可用
    return total


def full_scan(c: int, W: int, S: int, k: int, X: int,
              state_limit: int = 8000, residue_limit: int = 14,
              keep_signature: int = 12, verbose: bool = False,
              primes: list[int] | None = None) -> dict:
    """对 c 做与 codex 反例搜索同款的束扩展，但不在找到反例后停止。

    输出：
      checked_prefixes: 所有 saving≥S 且长度≥k 的唯一前缀类型集
      zero_count / nonzero_count: 零屏障 / 非零屏障数
      worst_examples: 前 5 个非零前缀及其 (P, A_R) 证人

    参数 primes：可外部传入素数表（批扫描时共享，避免重复构建）。
    """
    holes = holes_for_c(c, W)
    opts = q_residue_options(holes)
    rows = residue_rows_ranked(opts, residue_limit)
    if primes is None:
        primes = primes_upto(X)

    states: List[Tuple[int, List[Triple]]] = [(0, [])]
    checked_prefixes: Dict[tuple, Tuple[int, float | None, list]] = {}
    nonzero_examples: List[Tuple[tuple, int, list]] = []
    best_saving = 0
    visited_states = 0
    deadline = False
    t0 = time.time()

    for li, (q, choices) in enumerate(rows):
        if time.time() - t0 > 600:
            deadline = True
            break
        new_states = states[:]
        for saving, chosen in states:
            for row in choices:
                ns = saving + row[2]
                nchosen = chosen + [row]
                visited_states += 1
                if ns >= S and len(nchosen) >= k:
                    key, prefix = prefix_key(nchosen, k)
                    if key not in checked_prefixes:
                        count, min_ratio, first = survivor_count(prefix, primes, stop_after=0)
                        checked_prefixes[key] = (count, min_ratio, first)
                        if count > 0:
                            nonzero_examples.append((key, count, first))
                            if verbose:
                                print(f'[NONZERO] saving={ns} count={count} first={first[:1]}', flush=True)
                else:
                    new_states.append((ns, nchosen))
                if ns > best_saving:
                    best_saving = ns
        # 去重并限额：优先高 saving、相同前缀身份保留一份
        dedup: Dict[tuple, List[Triple]] = {}
        for saving, chosen in new_states:
            sig = (saving, state_signature(chosen, keep_signature))
            if sig not in dedup or len(chosen) < len(dedup[sig]):
                dedup[sig] = chosen
        compact = [(saving, chosen) for (saving, _), chosen in dedup.items()]
        compact.sort(key=lambda item: (-item[0], len(item[1])))
        states = compact[:state_limit]
        if verbose and (li + 1) % 5 == 0:
            print(f'[layer {li+1}/{len(rows)}] q={q} states={len(states)} '
                  f'checked={len(checked_prefixes)} nz={len(nonzero_examples)}', flush=True)

    elapsed = time.time() - t0
    zero_count = sum(1 for v in checked_prefixes.values() if v[0] == 0)
    nonzero_count = len(checked_prefixes) - zero_count
    return {
        'c': c, 'W': W, 'S': S, 'k': k, 'X': X,
        'state_limit': state_limit, 'residue_limit': residue_limit,
        'unique_prefixes_checked': len(checked_prefixes),
        'zero_prefixes': zero_count,
        'nonzero_prefixes': nonzero_count,
        'best_saving_seen': best_saving,
        'visited_state_extensions': visited_states,
        'final_states': len(states),
        'elapsed_sec': round(elapsed, 2),
        'deadline_hit': deadline,
        'nonzero_examples': nonzero_examples,
        'verdict': (
            'budget_exhausted' if deadline else
            ('counterexample_found' if nonzero_count > 0 else 'all_zero_in_search')
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--k', type=int, default=11)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=8000)
    parser.add_argument('--residueLimit', type=int, default=14)
    parser.add_argument('--keepSignature', type=int, default=12)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    result = full_scan(
        args.c, args.W, args.S, args.k, args.X,
        state_limit=args.stateLimit,
        residue_limit=args.residueLimit,
        keep_signature=args.keepSignature,
        verbose=args.verbose,
    )
    for key, value in result.items():
        if key == 'nonzero_examples':
            for ex in value:
                print('  nonzero_example', ex)
        else:
            print(key, value)


if __name__ == '__main__':
    main()
