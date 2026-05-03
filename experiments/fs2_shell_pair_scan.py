#!/usr/bin/env python3
"""按 dyadic u 壳扫描 FS2 二点相关偏差。"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def row_shell_hits(P: int, row: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    """返回候选骨架上每点的 u 壳；非粗半素数记为 None。"""
    B = math.isqrt(P)
    shells = []
    for col in range(1, P + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        if flags[n]:
            shells.append(None)
            continue
        factors = tuple(sorted(factor_distinct(n, plist)))
        if len(factors) == 2 and factors[0] > B:
            shell = int(math.floor(math.log(max(factors[0], B) / B, 2)))
            shells.append(shell)
        else:
            shells.append(None)
    return shells


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--top-rows", type=int, default=20)
    parser.add_argument("--max-lag", type=int, default=12)
    parser.add_argument("--top-pairs", type=int, default=12)
    args = parser.parse_args()

    print("P theta topShellPairRel pair:obs/exp/rel")
    for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top_rows)
        shell_counts = defaultdict(int)
        total_candidates = 0
        pair_counts = defaultdict(int)
        pair_totals = defaultdict(int)
        for row in rows:
            shells = row_shell_hits(P, row, flags, plist, small_primes)
            total_candidates += len(shells)
            for sh in shells:
                if sh is not None:
                    shell_counts[sh] += 1
            H = len(shells)
            for h in range(1, min(args.max_lag, H - 1) + 1):
                for i in range(H - h):
                    a = shells[i]
                    b = shells[i + h]
                    if a is not None and b is not None:
                        pair_counts[(a, b)] += 1
                    pair_totals[(a, b)] += 0  # 保持 defaultdict 类型，无实际用途
        theta = sum(shell_counts.values()) / total_candidates if total_candidates else 0.0
        shell_freq = {sh: count / total_candidates for sh, count in shell_counts.items()}
        rows_count = len(rows)
        # 总可比较位置近似为 sum_h sum_rows (H_row-h)，用每个壳对共享同一总量。
        total_pair_positions = 0
        for row in rows:
            H = len(row_shell_hits(P, row, flags, plist, small_primes))
            total_pair_positions += sum(max(0, H - h) for h in range(1, min(args.max_lag, H - 1) + 1))
        ranked = []
        for pair, obs in pair_counts.items():
            exp = total_pair_positions * shell_freq.get(pair[0], 0.0) * shell_freq.get(pair[1], 0.0)
            if exp <= 0:
                continue
            rel = (obs - exp) / exp
            ranked.append((abs(rel), rel, pair, obs, exp))
        ranked.sort(reverse=True)
        parts = []
        for _abs_rel, rel, pair, obs, exp in ranked[: args.top_pairs]:
            parts.append(f"{pair}:{obs}/{exp:.1f}/{rel:.2f}")
        max_rel = ranked[0][1] if ranked else 0.0
        print(P, f"{theta:.4f}", f"{max_rel:.3f}", " | ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
