#!/usr/bin/env python3
"""按候选骨架 gap word 统计全粗半素数填充容量。"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def candidate_hits(P: int, row: int, start: int, length: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    """返回窗口中的候选列与是否为粗半素数/三粗命中。"""
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    cols = []
    hits = []
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        cols.append(col)
        if flags[n]:
            hits.append(0)
            continue
        factors = tuple(factor_distinct(n, plist))
        hits.append(1 if factors and all(q > B for q in factors) else 0)
    return cols, hits


def scan_words(P: int, word_len: int, top_rows: int, window_factor: float, stride_factor: float):
    """扫描所有危险行窗口中的 gap word 统计。"""
    B = math.isqrt(P)
    limit = P * P + P
    flags = sieve(limit)
    plist = primes(flags, limit)
    small_primes = primes(sieve(B), B)
    rows = low_prime_rows(P, flags, top_rows)
    length = max(1, int(window_factor * math.sqrt(P)))
    stride = max(1, int(stride_factor * math.sqrt(P)))
    stats = defaultdict(lambda: [0, 0, 0])  # occurrences, all_hit, any_prime_or_gap
    for row in rows:
        max_start = max(1, P - length + 1)
        starts = list(range(1, max_start + 1, stride)) + [max_start]
        for start in sorted(set(starts)):
            cols, hits = candidate_hits(P, row, start, length, flags, plist, small_primes)
            if len(cols) < word_len:
                continue
            for i in range(0, len(cols) - word_len + 1):
                word = tuple(cols[i + j + 1] - cols[i + j] for j in range(word_len - 1))
                block_hits = hits[i:i+word_len]
                stats[word][0] += 1
                if all(block_hits):
                    stats[word][1] += 1
                else:
                    stats[word][2] += 1
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--word-len", type=int, default=6, help="候选块长度 R；gap word 长度为 R-1")
    parser.add_argument("--top-rows", type=int, default=8)
    parser.add_argument("--top-words", type=int, default=12)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    parser.add_argument("--min-occ", type=int, default=3)
    args = parser.parse_args()

    print("P wordLen totalWords minFill maxFill weightedFill topWords(word: occ/all/fill)")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        stats = scan_words(P, args.word_len, args.top_rows, args.window_factor, args.stride_factor)
        filtered = [(word, vals) for word, vals in stats.items() if vals[0] >= args.min_occ]
        total_occ = sum(vals[0] for _word, vals in filtered)
        total_hit = sum(vals[1] for _word, vals in filtered)
        fills = [vals[1] / vals[0] for _word, vals in filtered if vals[0]]
        min_fill = min(fills) if fills else 0.0
        max_fill = max(fills) if fills else 0.0
        weighted = total_hit / total_occ if total_occ else 0.0
        ranked = sorted(filtered, key=lambda item: (item[1][1] / item[1][0], item[1][0]), reverse=True)[: args.top_words]
        parts = []
        for word, vals in ranked:
            occ, all_hit, _miss = vals
            parts.append(f"{','.join(map(str, word))}:{occ}/{all_hit}/{all_hit/occ:.2f}")
        print(P, args.word_len, len(filtered), f"{min_fill:.3f}", f"{max_fill:.3f}", f"{weighted:.3f}", " | ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
