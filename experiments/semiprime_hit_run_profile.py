#!/usr/bin/env python3
"""剖析候选骨架上连续粗合数命中串的证书结构。

用法示例：
  python3 experiments/semiprime_hit_run_profile.py --Ps 503,1009 --top 5
"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def candidate_records(P: int, row: int, start: int, length: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    """返回小筛候选记录，含粗合数命中与证书因子。"""
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    records = []
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        if flags[n]:
            records.append({"col": col, "n": n, "hit": 0, "kind": "prime", "factors": ()})
            continue
        factors = tuple(factor_distinct(n, plist))
        if all(q > B for q in factors):
            if len(factors) == 2:
                kind = "semi"
            elif len(factors) >= 3:
                kind = "triple"
            else:
                kind = "other"
            records.append({"col": col, "n": n, "hit": 1, "kind": kind, "factors": factors})
        else:
            records.append({"col": col, "n": n, "hit": 0, "kind": "other", "factors": factors})
    return records


def hit_runs(records: list[dict]) -> list[tuple[int, int]]:
    """返回连续 hit=1 的候选序号区间 [lo, hi]。"""
    runs = []
    lo = None
    for idx, rec in enumerate(records):
        if rec["hit"]:
            if lo is None:
                lo = idx
        elif lo is not None:
            runs.append((lo, idx - 1))
            lo = None
    if lo is not None:
        runs.append((lo, len(records) - 1))
    return runs


def run_profile(P: int, records: list[dict], lo: int, hi: int) -> dict:
    """计算一条命中串的尺度与壳切换统计。"""
    B = math.isqrt(P)
    seg = records[lo : hi + 1]
    cols = [rec["col"] for rec in seg]
    ns = [rec["n"] for rec in seg]
    min_factors = []
    max_factors = []
    shells = []
    kinds = Counter()
    all_large = []
    for rec in seg:
        factors = tuple(sorted(rec["factors"]))
        kinds[rec["kind"]] += 1
        if factors:
            min_factors.append(factors[0])
            max_factors.append(factors[-1])
            all_large.extend(factors)
            shell = int(math.floor(math.log(max(factors[0], B) / B, 2))) if factors[0] >= B else -1
            shells.append(shell)
    col_gaps = [b - a for a, b in zip(cols, cols[1:])]
    u_gaps = [abs(b - a) for a, b in zip(min_factors, min_factors[1:])]
    shell_switches = sum(1 for a, b in zip(shells, shells[1:]) if a != b)
    # 近似乘法斜率：相邻 n 差与相邻最小大因子差的比例，避免除零。
    slope_ratios = []
    for dn, du in zip([b - a for a, b in zip(ns, ns[1:])], [b - a for a, b in zip(min_factors, min_factors[1:])]):
        if du:
            slope_ratios.append(abs(dn / du))
    return {
        "run_len": hi - lo + 1,
        "col_span": cols[-1] - cols[0] + 1 if cols else 0,
        "col_gap_med": sorted(col_gaps)[len(col_gaps)//2] if col_gaps else 0,
        "col_gap_max": max(col_gaps) if col_gaps else 0,
        "u_min": min(min_factors) if min_factors else 0,
        "u_max": max(min_factors) if min_factors else 0,
        "u_med_over_B": (sorted(min_factors)[len(min_factors)//2] / B) if min_factors else 0.0,
        "v_med_over_u": (sorted([max_v / min_u for min_u, max_v in zip(min_factors, max_factors) if min_u])[len(min_factors)//2]) if min_factors else 0.0,
        "u_gap_med": sorted(u_gaps)[len(u_gaps)//2] if u_gaps else 0,
        "shells": dict(Counter(shells)),
        "shell_switches": shell_switches,
        "distinct_large": len(set(all_large)),
        "total_large": len(all_large),
        "kinds": dict(kinds),
        "slope_med": sorted(slope_ratios)[len(slope_ratios)//2] if slope_ratios else 0.0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--rows", default="")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()

    print("P row start cand prime cover runLen colSpan gapMed gapMax uMed/B vMed/u shells switch distinct/total kinds slopeMed")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = [int(x) for x in args.rows.split(",") if x.strip()] if args.rows else low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        profiles = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                records = candidate_records(P, row, start, length, flags, plist, small_primes)
                if not records:
                    continue
                prime_count = sum(1 for rec in records if rec["kind"] == "prime")
                cover = sum(rec["hit"] for rec in records) / len(records)
                for lo, hi in hit_runs(records):
                    prof = run_profile(P, records, lo, hi)
                    profiles.append((prof["run_len"], cover, len(records), -prime_count, row, start, prof))
        for _run_len, cover, cand, neg_prime, row, start, prof in sorted(profiles, key=lambda item: (item[0], item[1], item[2], item[3]), reverse=True)[: args.top]:
            shells = ",".join(f"s{k}:{v}" for k, v in sorted(prof["shells"].items()))
            kinds = ",".join(f"{k}:{v}" for k, v in sorted(prof["kinds"].items()))
            print(
                P, row, start, cand, -neg_prime, f"{cover:.3f}", prof["run_len"], prof["col_span"],
                prof["col_gap_med"], prof["col_gap_max"], f"{prof['u_med_over_B']:.2f}", f"{prof['v_med_over_u']:.2f}",
                shells, prof["shell_switches"], f"{prof['distinct_large']}/{prof['total_large']}", kinds, f"{prof['slope_med']:.2f}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
