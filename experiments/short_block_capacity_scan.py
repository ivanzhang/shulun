#!/usr/bin/env python3
"""扫描正常窗口内候选短块全命中的窗口级容量缺口。"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

from gap_word_capacity_scan import candidate_hits
from high_threshold_margin_fast import primes, sieve
from semiprime_chain_bipartite_energy import low_prime_rows


def block_ratio(bits: list[int], block_len: int) -> tuple[int, int, float]:
    """返回候选序列中长度 block_len 全命中块的数量、总块数和比例。"""
    total = max(0, len(bits) - block_len + 1)
    if total == 0:
        return 0, 0, 0.0
    full = 0
    run = 0
    for bit in bits + [0]:
        if bit:
            run += 1
            continue
        if run >= block_len:
            full += run - block_len + 1
        run = 0
    return full, total, full / total


def percentile(values: list[float], q: float) -> float:
    """计算简单经验分位数。"""
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round(q * (len(ordered) - 1)))))
    return ordered[idx]


def scan(P: int, top_rows: int, window_factor: float, stride_factor: float, max_R: int, min_candidates: int):
    """扫描低素数行的滑动窗口，返回每个 R 的窗口级容量统计。"""
    B = math.isqrt(P)
    limit = P * P + P
    flags = sieve(limit)
    plist = primes(flags, limit)
    small_primes = primes(sieve(B), B)
    rows = low_prime_rows(P, flags, top_rows)
    length = max(1, int(window_factor * math.sqrt(P)))
    stride = max(1, int(stride_factor * math.sqrt(P)))

    ratios: dict[int, list[float]] = defaultdict(list)
    covers: list[float] = []
    window_count = 0
    full_window_count = 0
    min_H = 10**18
    max_H = 0

    for row in rows:
        max_start = max(1, P - length + 1)
        starts = sorted(set(list(range(1, max_start + 1, stride)) + [max_start]))
        for start in starts:
            _cols, hits = candidate_hits(P, row, start, length, flags, plist, small_primes)
            H = len(hits)
            if H < min_candidates:
                continue
            window_count += 1
            min_H = min(min_H, H)
            max_H = max(max_H, H)
            cover = sum(hits) / H if H else 0.0
            covers.append(cover)
            if cover == 1.0:
                full_window_count += 1
            for R in range(2, max_R + 1):
                _full, total, ratio = block_ratio(hits, R)
                if total:
                    ratios[R].append(ratio)
    return {
        "rows": len(rows),
        "windows": window_count,
        "full_windows": full_window_count,
        "min_H": 0 if min_H == 10**18 else min_H,
        "max_H": max_H,
        "cover_mean": sum(covers) / len(covers) if covers else 0.0,
        "cover_p95": percentile(covers, 0.95),
        "cover_max": max(covers) if covers else 0.0,
        "ratios": ratios,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001,8009")
    parser.add_argument("--top-rows", type=int, default=20)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    parser.add_argument("--max-R", type=int, default=12)
    parser.add_argument("--min-candidates", type=int, default=8)
    args = parser.parse_args()

    print("P rows windows fullWindows Hmin Hmax coverMean coverP95 coverMax R mean p95 p99 max gammaMax Kmean Kmax")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        result = scan(P, args.top_rows, args.window_factor, args.stride_factor, args.max_R, args.min_candidates)
        for R in range(2, args.max_R + 1):
            vals = result["ratios"].get(R, [])
            mean = sum(vals) / len(vals) if vals else 0.0
            p95 = percentile(vals, 0.95)
            p99 = percentile(vals, 0.99)
            max_ratio = max(vals) if vals else 0.0
            theta = result["cover_mean"]
            indep = theta ** R if theta else 0.0
            k_mean = mean / indep if indep else 0.0
            k_max = max_ratio / indep if indep else 0.0
            print(
                P,
                result["rows"],
                result["windows"],
                result["full_windows"],
                result["min_H"],
                result["max_H"],
                f"{result['cover_mean']:.4f}",
                f"{result['cover_p95']:.4f}",
                f"{result['cover_max']:.4f}",
                R,
                f"{mean:.6f}",
                f"{p95:.6f}",
                f"{p99:.6f}",
                f"{max_ratio:.6f}",
                f"{1.0 - max_ratio:.6f}",
                f"{k_mean:.3f}",
                f"{k_max:.3f}",
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
