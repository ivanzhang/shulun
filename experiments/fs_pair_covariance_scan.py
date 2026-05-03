#!/usr/bin/env python3
"""扫描候选骨架上粗合数命中序列的二点 connected 协方差。"""
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


def pair_cov(bits: list[int], max_lag: int):
    H = len(bits)
    theta = sum(bits) / H if H else 0.0
    out = []
    for h in range(1, min(max_lag, H - 1) + 1):
        total = H - h
        pair = sum(bits[i] * bits[i + h] for i in range(total))
        expected = total * theta * theta
        cov = pair - expected
        norm = total * max(theta * theta, 1e-12)
        out.append((h, total, pair, expected, cov, cov / norm if norm else 0.0))
    return theta, out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001,8009")
    parser.add_argument("--top-rows", type=int, default=20)
    parser.add_argument("--max-lag", type=int, default=20)
    args = parser.parse_args()

    print("P rows theta maxRelCov argMax meanAbsRel l2Rel lagSummary")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top_rows)
        agg = defaultdict(lambda: [0, 0.0, 0.0])  # total, pair, expected
        total_hits = total_H = 0
        for row in rows:
            bits = row_hits(P, row, flags, plist, small_primes)
            total_hits += sum(bits)
            total_H += len(bits)
            theta, covs = pair_cov(bits, args.max_lag)
            for h, total, pair, expected, _cov, _rel in covs:
                agg[h][0] += total
                agg[h][1] += pair
                agg[h][2] += expected
        theta_global = total_hits / total_H if total_H else 0.0
        rels = []
        parts = []
        for h in sorted(agg):
            total, pair, expected = agg[h]
            cov = pair - expected
            rel = cov / max(expected, 1e-12)
            rels.append((h, rel))
            if h <= 8:
                parts.append(f"h{h}:{rel:.3f}")
        max_h, max_rel = max(rels, key=lambda item: abs(item[1])) if rels else (0, 0.0)
        mean_abs = sum(abs(r) for _h, r in rels) / len(rels) if rels else 0.0
        l2 = math.sqrt(sum(r*r for _h, r in rels) / len(rels)) if rels else 0.0
        print(P, len(rows), f"{theta_global:.4f}", f"{max_rel:.4f}", max_h, f"{mean_abs:.4f}", f"{l2:.4f}", " ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
