#!/usr/bin/env python3
"""扫描候选骨架粗合数命中序列的三点 connected 偏差。"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def row_hits(P: int, row: int, flags: bytearray, plist: list[int], small_primes: list[int]) -> list[int]:
    B = math.isqrt(P)
    bits = []
    for col in range(1, P + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        if flags[n]:
            bits.append(0)
        else:
            factors = tuple(factor_distinct(n, plist))
            bits.append(1 if factors and all(q > B for q in factors) else 0)
    return bits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--top-rows", type=int, default=20)
    parser.add_argument("--max-lag", type=int, default=10)
    args = parser.parse_args()

    print("P rows theta maxRelTriple pair meanAbsRelTriple l2RelTriple")
    for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top_rows)
        total_hits = total_H = 0
        # 聚合所有 (h1,h2) 的三点矩。
        agg = defaultdict(lambda: [0, 0])
        for row in rows:
            bits = row_hits(P, row, flags, plist, small_primes)
            total_hits += sum(bits)
            total_H += len(bits)
            H = len(bits)
            for h1 in range(1, min(args.max_lag, H - 1) + 1):
                for h2 in range(h1 + 1, min(args.max_lag, H - 1) + 1):
                    total = H - h2
                    triple = sum(bits[i] * bits[i + h1] * bits[i + h2] for i in range(total))
                    agg[(h1, h2)][0] += total
                    agg[(h1, h2)][1] += triple
        theta = total_hits / total_H if total_H else 0.0
        rels = []
        for pair, (total, triple) in agg.items():
            expected = total * theta ** 3
            rel = (triple - expected) / max(expected, 1e-12)
            rels.append((pair, rel))
        max_pair, max_rel = max(rels, key=lambda item: abs(item[1])) if rels else ((0, 0), 0.0)
        mean_abs = sum(abs(r) for _p, r in rels) / len(rels) if rels else 0.0
        l2 = math.sqrt(sum(r*r for _p, r in rels) / len(rels)) if rels else 0.0
        print(P, len(rows), f"{theta:.4f}", f"{max_rel:.4f}", max_pair, f"{mean_abs:.4f}", f"{l2:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
