#!/usr/bin/env python3
"""按整行候选骨架去重统计 gap word 的粗合数填充率。"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def row_candidate_hits(P: int, row: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    B = math.isqrt(P)
    cols = []
    hits = []
    for col in range(1, P + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        cols.append(col)
        if flags[n]:
            hits.append(0)
        else:
            factors = tuple(factor_distinct(n, plist))
            hits.append(1 if factors and all(q > B for q in factors) else 0)
    return cols, hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--word-len", type=int, default=10)
    parser.add_argument("--top-rows", type=int, default=12)
    parser.add_argument("--top-words", type=int, default=12)
    parser.add_argument("--min-occ", type=int, default=2)
    args = parser.parse_args()

    print("P wordLen words weightedFill maxFill topWords(word:occ/all/fill rows)")
    for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top_rows)
        stats = defaultdict(lambda: [0, 0, set()])
        for row in rows:
            cols, hits = row_candidate_hits(P, row, flags, plist, small_primes)
            if len(cols) < args.word_len:
                continue
            for i in range(len(cols) - args.word_len + 1):
                word = tuple(cols[i + j + 1] - cols[i + j] for j in range(args.word_len - 1))
                stats[word][0] += 1
                if all(hits[i:i+args.word_len]):
                    stats[word][1] += 1
                    stats[word][2].add(row)
        filtered = [(w, v) for w, v in stats.items() if v[0] >= args.min_occ]
        total_occ = sum(v[0] for _w, v in filtered)
        total_hit = sum(v[1] for _w, v in filtered)
        weighted = total_hit / total_occ if total_occ else 0.0
        max_fill = max((v[1] / v[0] for _w, v in filtered), default=0.0)
        ranked = sorted(filtered, key=lambda item: (item[1][1] / item[1][0], item[1][1], item[1][0]), reverse=True)[:args.top_words]
        parts = []
        for word, vals in ranked:
            occ, all_hit, rows_hit = vals
            parts.append(f"{','.join(map(str, word))}:{occ}/{all_hit}/{all_hit/occ:.2f}/r{len(rows_hit)}")
        print(P, args.word_len, len(filtered), f"{weighted:.4f}", f"{max_fill:.3f}", " | ".join(parts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
