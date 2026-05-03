#!/usr/bin/env python3
"""扫描小筛候选骨架 A 与 sqrt(P)-粗半素数点过程 S 的短差分相关。

核心思想：单独半素数容量不矛盾，真正需要检测的是 S 是否异常贴合 A。
本脚本在窗口 K 内构造：
  A(c)=1_{n 避开 q<=sqrt(P)}
  S(c)=1_{n=uv, u,v>sqrt(P) 且 u,v 为素数}
并计算平衡短差分相关、重叠率与 singular-series 型粗期望的偏差。

用法示例：
  python3 experiments/skeleton_semiprime_correlation_scan.py --Ps 503,1009 --top 5
"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def window_arrays(P: int, row: int, start: int, length: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    """返回窗口列坐标上的 A、S 数组。"""
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    A = []
    S = []
    prime_candidates = 0
    triple = 0
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        is_a = all(n % q != 0 for q in small_primes)
        A.append(1 if is_a else 0)
        is_s = 0
        if is_a:
            if flags[n]:
                prime_candidates += 1
            else:
                factors = tuple(sorted(factor_distinct(n, plist)))
                if len(factors) == 2 and factors[0] > B:
                    is_s = 1
                elif len(factors) >= 3 and all(q > B for q in factors):
                    triple += 1
        S.append(is_s)
    return A, S, prime_candidates, triple


def centered_corr(A: list[int], S: list[int], max_h: int) -> dict:
    """计算 A 与 S 的平衡短差分相关。"""
    L = len(A)
    if L == 0:
        return {}
    mean_a = sum(A) / L
    mean_s = sum(S) / L
    norm_a = math.sqrt(sum((x - mean_a) ** 2 for x in A))
    norm_s = math.sqrt(sum((x - mean_s) ** 2 for x in S))
    max_abs = 0.0
    max_h_hit = 0
    l1 = 0.0
    l2 = 0.0
    raw_overlap = sum(1 for a, s in zip(A, S) if a and s)
    expected_overlap = sum(A) * mean_s
    for h in range(-max_h, max_h + 1):
        if h == 0:
            pairs = [(i, i) for i in range(L)]
        elif h > 0:
            pairs = [(i, i + h) for i in range(L - h)]
        else:
            pairs = [(i - h, i) for i in range(L + h)]
        if not pairs:
            continue
        corr = sum((A[i] - mean_a) * (S[j] - mean_s) for i, j in pairs)
        denom = max(1e-12, norm_a * norm_s)
        val = corr / denom
        abs_val = abs(val)
        l1 += abs_val
        l2 += val * val
        if abs_val > max_abs:
            max_abs = abs_val
            max_h_hit = h
    return {
        "mean_a": mean_a,
        "mean_s": mean_s,
        "sum_a": sum(A),
        "sum_s": sum(S),
        "raw_overlap": raw_overlap,
        "expected_overlap": expected_overlap,
        "overlap_ratio": raw_overlap / sum(A) if sum(A) else 0.0,
        "lift": raw_overlap / expected_overlap if expected_overlap else 0.0,
        "max_corr": max_abs,
        "max_h": max_h_hit,
        "l1_corr": l1,
        "l2_corr": math.sqrt(l2),
    }


def candidate_hit_runs(A: list[int], S: list[int]) -> int:
    """候选骨架上连续 S 命中的最长长度。"""
    best = cur = 0
    for a, s in zip(A, S):
        if not a:
            continue
        if s:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--rows", default="")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    parser.add_argument("--h-factor", type=float, default=1.0, help="max_h = h-factor * sqrt(P)")
    args = parser.parse_args()

    print("P row start len A S prime triple cover lift maxCorr maxH l1Corr l2Corr maxRun")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = [int(x) for x in args.rows.split(",") if x.strip()] if args.rows else low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        max_h = max(1, int(args.h_factor * math.sqrt(P)))
        records = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                A, S, prime_candidates, triple = window_arrays(P, row, start, length, flags, plist, small_primes)
                stats = centered_corr(A, S, max_h)
                if not stats or stats["sum_a"] == 0:
                    continue
                cover = (stats["sum_s"] + triple) / stats["sum_a"]
                max_run = candidate_hit_runs(A, S)
                records.append((prime_candidates, -cover, -stats["sum_a"], row, start, triple, stats, max_run))
        for prime_candidates, neg_cover, neg_a, row, start, triple, stats, max_run in sorted(records)[: args.top]:
            print(
                P, row, start, length, stats["sum_a"], stats["sum_s"], prime_candidates, triple,
                f"{-neg_cover:.3f}", f"{stats['lift']:.2f}", f"{stats['max_corr']:.3f}", stats["max_h"],
                f"{stats['l1_corr']:.2f}", f"{stats['l2_corr']:.2f}", max_run,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
