#!/usr/bin/env python3
"""在候选骨架坐标上扫描半素数命中序列的非零滞后相关。"""
from __future__ import annotations

import argparse
import math

from high_threshold_margin_fast import primes, sieve
from semiprime_chain_bipartite_energy import low_prime_rows
from semiprime_hit_sequence_spectrum import hit_sequence


def lag_stats(bits: list[int], max_lag: int) -> dict:
    """排除 h=0，计算命中序列的平衡滞后相关与 runs。"""
    H = len(bits)
    if H <= 2:
        return {}
    mean = sum(bits) / H
    var = mean * (1 - mean)
    if var <= 0:
        return {"mean": mean, "max_lag_corr": 0.0, "arg_lag": 0, "l1": 0.0, "l2": 0.0, "max_run": H if mean == 1 else 0}
    max_lag = min(max_lag, H - 1)
    max_abs = 0.0
    arg_lag = 0
    l1 = 0.0
    l2 = 0.0
    for h in range(1, max_lag + 1):
        corr = sum((bits[i] - mean) * (bits[i + h] - mean) for i in range(H - h))
        denom = (H - h) * var
        val = corr / denom if denom else 0.0
        abs_val = abs(val)
        l1 += abs_val
        l2 += val * val
        if abs_val > max_abs:
            max_abs = abs_val
            arg_lag = h
    best = cur = 0
    for bit in bits:
        if bit:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return {"mean": mean, "max_lag_corr": max_abs, "arg_lag": arg_lag, "l1": l1, "l2": math.sqrt(l2), "max_run": best}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--rows", default="")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    parser.add_argument("--lag-factor", type=float, default=0.5, help="max lag = lag-factor * candidate count")
    args = parser.parse_args()

    print("P row start len cand prime semi triple cover maxLagCorr argLag l1Lag l2Lag maxRun")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = [int(x) for x in args.rows.split(",") if x.strip()] if args.rows else low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        records = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                bits, prime_count, semi_count, triple_count = hit_sequence(P, row, start, length, flags, plist, small_primes)
                if len(bits) <= 2:
                    continue
                max_lag = max(1, int(args.lag_factor * len(bits)))
                stats = lag_stats(bits, max_lag)
                cover = (semi_count + triple_count) / len(bits)
                records.append((prime_count, -cover, -len(bits), row, start, len(bits), semi_count, triple_count, stats))
        for prime_count, neg_cover, neg_cand, row, start, cand, semi_count, triple_count, stats in sorted(records)[: args.top]:
            print(
                P, row, start, length, cand, prime_count, semi_count, triple_count, f"{-neg_cover:.3f}",
                f"{stats['max_lag_corr']:.3f}", stats["arg_lag"], f"{stats['l1']:.2f}", f"{stats['l2']:.2f}", stats["max_run"],
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
