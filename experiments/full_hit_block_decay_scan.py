#!/usr/bin/env python3
"""扫描候选骨架长度 R 块全被粗合数命中的总量比例 epsilon_R。"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def row_hits(P: int, row: int, flags: bytearray, plist: list[int], small_primes: list[int]) -> list[int]:
    """返回整行候选骨架上的粗合数命中序列。"""
    B = math.isqrt(P)
    hits = []
    for col in range(1, P + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        if flags[n]:
            hits.append(0)
            continue
        factors = tuple(factor_distinct(n, plist))
        hits.append(1 if factors and all(q > B for q in factors) else 0)
    return hits


def block_stats(bits: list[int], max_R: int) -> dict[int, tuple[int, int, float]]:
    """返回 R -> (总块数, 全命中块数, 比例)。"""
    out = {}
    H = len(bits)
    # 用连续 1 run 快速累计全命中块数。
    run_lengths = []
    cur = 0
    for bit in bits + [0]:
        if bit:
            cur += 1
        elif cur:
            run_lengths.append(cur)
            cur = 0
    for R in range(2, max_R + 1):
        total = max(0, H - R + 1)
        full = sum(max(0, run - R + 1) for run in run_lengths)
        out[R] = (total, full, full / total if total else 0.0)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001,8009")
    parser.add_argument("--top-rows", type=int, default=20)
    parser.add_argument("--max-R", type=int, default=18)
    args = parser.parse_args()

    print("P rows R totalBlocks fullBlocks epsilon meanCover indepCover epsOverIndep")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top_rows)
        agg_total = defaultdict(int)
        agg_full = defaultdict(int)
        total_hits = 0
        total_candidates = 0
        for row in rows:
            bits = row_hits(P, row, flags, plist, small_primes)
            total_hits += sum(bits)
            total_candidates += len(bits)
            stats = block_stats(bits, args.max_R)
            for R, (total, full, _eps) in stats.items():
                agg_total[R] += total
                agg_full[R] += full
        mean_cover = total_hits / total_candidates if total_candidates else 0.0
        for R in range(2, args.max_R + 1):
            total = agg_total[R]
            full = agg_full[R]
            eps = full / total if total else 0.0
            indep = mean_cover ** R
            print(P, len(rows), R, total, full, f"{eps:.6g}", f"{mean_cover:.4f}", f"{indep:.6g}", f"{(eps/indep if indep else 0.0):.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
