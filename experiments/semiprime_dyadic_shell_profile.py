#!/usr/bin/env python3
"""分析危险窗口中粗半素数证书的 dyadic u 壳贡献。"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def window_profile(P, row, start, length, flags, plist, small_primes):
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    cand = prime = triple = 0
    shells = Counter()
    shell_cols = {}
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        cand += 1
        if flags[n]:
            prime += 1
            continue
        factors = factor_distinct(n, plist)
        if len(factors) == 2 and all(q > B for q in factors):
            u = min(factors)
            shell = int(math.floor(math.log(u / B, 2))) if u >= B else -1
            shells[shell] += 1
            shell_cols.setdefault(shell, []).append(col)
        elif len(factors) >= 3 and all(q > B for q in factors):
            triple += 1
    return cand, prime, triple, shells, shell_cols


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()
    print("P row start cand prime semi triple cover topShells shellGaps")
    for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
        B = math.isqrt(P)
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        records = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                cand, prime, triple, shells, shell_cols = window_profile(P, row, start, length, flags, plist, small_primes)
                if not cand:
                    continue
                semi = sum(shells.values())
                cover = (semi + triple) / cand
                records.append((prime, -cover, -cand, row, start, cand, semi, triple, shells, shell_cols))
        for prime, negcover, negcand, row, start, cand, semi, triple, shells, shell_cols in sorted(records)[: args.top]:
            top_shells = ",".join(
                f"[{B*(2**k):.0f},{B*(2**(k+1)):.0f}):{v}" for k, v in shells.most_common(5)
            )
            gap_parts = []
            for k, cols in sorted(shell_cols.items(), key=lambda item: -len(item[1]))[:3]:
                cols = sorted(cols)
                gaps = [b - a for a, b in zip(cols, cols[1:])]
                if gaps:
                    gap_parts.append(f"s{k}:med{sorted(gaps)[len(gaps)//2]} max{max(gaps)}")
                else:
                    gap_parts.append(f"s{k}:single")
            print(P, row, start, cand, prime, semi, triple, f"{(semi+triple)/cand:.3f}", top_shells, ";".join(gap_parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
