#!/usr/bin/env python3
"""扫描危险窗口中小筛候选集的局部 Fourier 小谱与间距均匀性。

用法示例：
  python3 experiments/semiprime_candidate_spectrum_scan.py --Ps 503,1009 --top 4

输出字段说明：
  maxSpecNorm  为非零频谱最大值除以候选数；越小表示越接近小谱。
  l2SpecNorm   为非零频谱二范数除以候选数；由 Parseval 约为 sqrt((M-H)/H)。
  pairChi2     为短差分对计数相对均匀模型的卡方型偏差。
"""
from __future__ import annotations

import argparse
import cmath
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def candidate_columns(P: int, row: int, start: int, length: int, small_primes: list[int]) -> list[int]:
    """返回窗口内避开 <=sqrt(P) 小素因子的列坐标。"""
    end = min(P, start + length - 1)
    cols = []
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if all(n % q != 0 for q in small_primes):
            cols.append(col)
    return cols


def classify_counts(P: int, row: int, cols: list[int], flags: bytearray, plist: list[int]) -> tuple[int, int, int]:
    """统计候选中的素数、粗半素数、三粗及以上。"""
    B = math.isqrt(P)
    prime_count = 0
    semi_count = 0
    triple_count = 0
    for col in cols:
        n = (row - 1) * P + col
        if flags[n]:
            prime_count += 1
            continue
        factors = factor_distinct(n, plist)
        if all(q > B for q in factors):
            if len(factors) == 2:
                semi_count += 1
            elif len(factors) >= 3:
                triple_count += 1
    return prime_count, semi_count, triple_count


def spectrum_metrics(cols: list[int], modulus: int) -> tuple[float, float, int]:
    """计算候选列在局部循环长度 modulus 上的非零 Fourier 小谱指标。"""
    H = len(cols)
    if H == 0 or modulus <= 1:
        return 0.0, 0.0, 0
    positions = [c % modulus for c in cols]
    max_abs = 0.0
    sum_sq = 0.0
    max_freq = 0
    for freq in range(1, modulus):
        total = 0j
        for pos in positions:
            angle = -2.0 * math.pi * freq * pos / modulus
            total += complex(math.cos(angle), math.sin(angle))
        mag = abs(total)
        sum_sq += mag * mag
        if mag > max_abs:
            max_abs = mag
            max_freq = freq
    return max_abs / H, math.sqrt(sum_sq) / H, max_freq


def pair_chi2(cols: list[int], max_gap: int) -> tuple[float, int, int]:
    """用短差分对计数检测二阶间距均匀性。"""
    H = len(cols)
    if H < 2 or max_gap < 1:
        return 0.0, 0, 0
    colset = set(cols)
    counts = []
    for gap in range(1, max_gap + 1):
        counts.append(sum(1 for c in cols if c + gap in colset))
    total_pairs = sum(counts)
    expected = total_pairs / max_gap if max_gap else 0.0
    if expected == 0:
        return 0.0, total_pairs, 0
    chi2 = sum((count - expected) ** 2 / expected for count in counts) / max_gap
    return chi2, total_pairs, max(counts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003")
    parser.add_argument("--rows", default="", help="指定行号；为空时选低素数行")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    parser.add_argument("--mod-factor", type=float, default=4.0, help="局部 Fourier 模长约为该倍数 sqrt(P)")
    parser.add_argument("--gap-factor", type=float, default=1.0, help="差分检测到该倍数 sqrt(P)")
    args = parser.parse_args()

    print("P row start len cand prime semi triple cover maxSpecNorm maxFreq l2SpecNorm pairChi2 pairTotal pairMax")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = [int(x) for x in args.rows.split(",") if x.strip()] if args.rows else low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        modulus = max(2, int(args.mod_factor * math.sqrt(P)))
        max_gap = max(1, int(args.gap_factor * math.sqrt(P)))
        records = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                cols = candidate_columns(P, row, start, length, small_primes)
                if not cols:
                    continue
                prime_count, semi_count, triple_count = classify_counts(P, row, cols, flags, plist)
                cover = (semi_count + triple_count) / len(cols)
                max_spec, l2_spec, max_freq = spectrum_metrics(cols, modulus)
                chi2, pair_total, pair_max = pair_chi2(cols, max_gap)
                records.append((prime_count, -cover, -len(cols), row, start, len(cols), semi_count, triple_count, cover, max_spec, max_freq, l2_spec, chi2, pair_total, pair_max))
        for rec in sorted(records)[: args.top]:
            prime_count, neg_cover, neg_cand, row, start, cand, semi_count, triple_count, cover, max_spec, max_freq, l2_spec, chi2, pair_total, pair_max = rec
            print(P, row, start, length, cand, prime_count, semi_count, triple_count, f"{cover:.3f}", f"{max_spec:.3f}", max_freq, f"{l2_spec:.3f}", f"{chi2:.3f}", pair_total, pair_max)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
