#!/usr/bin/env python3
"""扫描危险窗口中“候选序号坐标”的粗半素数命中谱。

原始列坐标会被小筛 CRT 格点强烈污染；本脚本把窗口内小筛候选按顺序编号，
只研究这些候选上哪些位置被 sqrt(P)-粗半素数或三粗合数命中。

用法示例：
  python3 experiments/semiprime_hit_sequence_spectrum.py --Ps 503,1009 --top 4
"""
from __future__ import annotations

import argparse
import math

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def hit_sequence(P: int, row: int, start: int, length: int, flags: bytearray, plist: list[int], small_primes: list[int]) -> tuple[list[int], int, int, int]:
    """返回候选序号上的合数命中序列：1 表示粗合数，0 表示素数候选。"""
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    hits = []
    prime_count = 0
    semi_count = 0
    triple_count = 0
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        if flags[n]:
            hits.append(0)
            prime_count += 1
            continue
        factors = factor_distinct(n, plist)
        if all(q > B for q in factors):
            hits.append(1)
            if len(factors) == 2:
                semi_count += 1
            elif len(factors) >= 3:
                triple_count += 1
        else:
            hits.append(0)
    return hits, prime_count, semi_count, triple_count


def balanced_spectrum(bits: list[int]) -> tuple[float, float, int, int]:
    """计算命中序列减去均值后的 Fourier 谱。"""
    H = len(bits)
    if H <= 1:
        return 0.0, 0.0, 0, 0
    mean = sum(bits) / H
    max_abs = 0.0
    sum_sq = 0.0
    max_freq = 0
    for freq in range(1, H):
        re = 0.0
        im = 0.0
        for idx, bit in enumerate(bits):
            val = bit - mean
            angle = -2.0 * math.pi * freq * idx / H
            re += val * math.cos(angle)
            im += val * math.sin(angle)
        mag = math.hypot(re, im)
        sum_sq += mag * mag
        if mag > max_abs:
            max_abs = mag
            max_freq = freq
    ones = sum(bits)
    scale = math.sqrt(max(1e-12, H * mean * (1.0 - mean)))
    return max_abs / scale, math.sqrt(sum_sq) / scale, max_freq, ones


def longest_runs(bits: list[int]) -> tuple[int, int]:
    """返回最长连续命中和最长连续未命中长度。"""
    best_one = best_zero = cur_one = cur_zero = 0
    for bit in bits:
        if bit:
            cur_one += 1
            cur_zero = 0
        else:
            cur_zero += 1
            cur_one = 0
        best_one = max(best_one, cur_one)
        best_zero = max(best_zero, cur_zero)
    return best_one, best_zero


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003")
    parser.add_argument("--rows", default="")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()

    print("P row start len cand prime semi triple cover hitMaxSpec hitL2Spec hitMaxFreq maxHitRun maxGapRun")
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
                if not bits:
                    continue
                cover = sum(bits) / len(bits)
                max_spec, l2_spec, max_freq, _ones = balanced_spectrum(bits)
                max_hit_run, max_gap_run = longest_runs(bits)
                records.append((prime_count, -cover, -len(bits), row, start, len(bits), semi_count, triple_count, cover, max_spec, l2_spec, max_freq, max_hit_run, max_gap_run))
        for rec in sorted(records)[: args.top]:
            prime_count, neg_cover, neg_cand, row, start, cand, semi_count, triple_count, cover, max_spec, l2_spec, max_freq, max_hit_run, max_gap_run = rec
            print(P, row, start, length, cand, prime_count, semi_count, triple_count, f"{cover:.3f}", f"{max_spec:.3f}", f"{l2_spec:.3f}", max_freq, max_hit_run, max_gap_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
