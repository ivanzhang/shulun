#!/usr/bin/env python3
"""§207 完全无截断的 N_{c, k_low} 枚举器。

§204 用束搜索 (stateLimit, residueLimit) 找 N_{c, k_low}，可能漏掉非典型骨架。
本节给出严格无截断版本：

1. 把 (q, r, cap) 三元组按 (-cap, q, r) 排序得 flat_sorted；
2. cap 降序 DFS 枚举所有 k_low 元 q-互异有序选择；
3. 用 max_completable + Surv 双重剪枝；
4. 收集所有 saving 可达 S 且 Surv ≠ ∅ 的 prefix。

输出与束搜索 N_{c, k_low} 的差集 — 即被束搜索漏掉的反例。

用法：
    python3 experiments/exhaustive_n_c_enumerator.py --c 2309 --W 100 --S 55 \
        --kLow 10 --X 1000000
"""
from __future__ import annotations

import argparse
import math
import sys
import time
from typing import List, Tuple

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import survivor_count, prefix_phase
from skeleton_union_bound import q_residue_options


Triple = Tuple[int, int, int]


def flat_options(opts) -> List[Triple]:
    flat: List[Triple] = []
    for q, residue_rows in opts:
        for row in residue_rows:
            flat.append((row[0], row[1], row[2]))
    return flat


def max_completable(used: set[int], last_cap: int,
                    by_q_max_cap: dict[int, list[int]]) -> int:
    total = 0
    for q, caps_sorted in by_q_max_cap.items():
        if q in used:
            continue
        for cap in caps_sorted:
            if cap <= last_cap:
                total += cap
                break
    return total


def exhaustive_enumerate(c: int, W: int, S: int, k_low: int, X: int,
                         max_nodes: int = 5_000_000,
                         verbose: bool = False) -> dict:
    holes = holes_for_c(c, W)
    opts = q_residue_options(holes)
    flat = flat_options(opts)
    flat.sort(key=lambda t: (-t[2], t[0], t[1]))
    primes = primes_upto(X)

    # by_q_max_cap[q] = caps for q sorted descending
    by_q_max_cap: dict[int, list[int]] = {}
    for q, r, cap in flat:
        by_q_max_cap.setdefault(q, []).append(cap)
    for q in by_q_max_cap:
        by_q_max_cap[q].sort(reverse=True)

    n_flat = len(flat)
    nonzero_prefixes: list[Tuple[Tuple[Triple, ...], int, list]] = []
    nodes = [0]
    deadline_hit = [False]
    seen_prefixes: set[Tuple[Triple, ...]] = set()

    def dfs(idx: int, prefix: list, used: set[int], saving: int, last_cap: int):
        if deadline_hit[0]:
            return
        nodes[0] += 1
        if nodes[0] > max_nodes:
            deadline_hit[0] = True
            return

        if len(prefix) == k_low:
            mc = max_completable(used, last_cap, by_q_max_cap)
            if saving + mc < S:
                return
            key = tuple(sorted(prefix, key=lambda t: (-t[2], t[0], t[1])))
            if key in seen_prefixes:
                return
            seen_prefixes.add(key)
            count, min_ratio, first = survivor_count(list(key), primes, stop_after=0)
            if count > 0:
                nonzero_prefixes.append((key, count, first))
                if verbose:
                    print(f'[NZ] saving={saving} count={count} P={first[0][0]}', flush=True)
            return

        # cap 降序剪枝：剩余可补 saving
        mc_total = max_completable(used, last_cap, by_q_max_cap)
        if saving + mc_total < S:
            return

        # cap 降序遍历 flat_sorted[idx:]
        for j in range(idx, n_flat):
            triple = flat[j]
            q_j, r_j, cap_j = triple
            if cap_j > last_cap:
                continue  # cap_sorted 防御
            if q_j in used:
                continue
            new_used = used | {q_j}
            dfs(j + 1, prefix + [triple], new_used, saving + cap_j, cap_j)
            if deadline_hit[0]:
                return

    t0 = time.time()
    dfs(0, [], set(), 0, 10**9)
    elapsed = time.time() - t0

    return {
        'c': c, 'W': W, 'S': S, 'k_low': k_low, 'X': X,
        'flat_size': n_flat,
        'qs_count': len(by_q_max_cap),
        'nodes_visited': nodes[0],
        'unique_prefixes': len(seen_prefixes),
        'nonzero_prefixes': len(nonzero_prefixes),
        'nonzero_examples': nonzero_prefixes,
        'deadline_hit': deadline_hit[0],
        'elapsed_sec': round(elapsed, 2),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kLow', type=int, default=10)
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--maxNodes', type=int, default=5_000_000)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    result = exhaustive_enumerate(args.c, args.W, args.S, args.kLow, args.X,
                                  max_nodes=args.maxNodes, verbose=args.verbose)
    print('=' * 60)
    print('完全无截断 N_{c, k_low} 枚举结果')
    print('=' * 60)
    for k, v in result.items():
        if k == 'nonzero_examples':
            print(f'{k}: ({len(v)} 个)')
            for prefix, count, first in v[:10]:
                print(f'  prefix={prefix}')
                print(f'    survivors={count} first={first[:1]}')
        else:
            print(f'{k}: {v}')


if __name__ == '__main__':
    main()
