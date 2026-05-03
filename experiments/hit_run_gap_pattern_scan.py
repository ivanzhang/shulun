#!/usr/bin/env python3
"""扫描候选骨架长命中串的列间距模式与小素数屏障。"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from semiprime_chain_bipartite_energy import low_prime_rows
from semiprime_hit_run_profile import candidate_records, hit_runs


def gap_pattern(records: list[dict], lo: int, hi: int, small_primes: list[int]) -> dict:
    """提取连续命中串的候选间距与间隙内被哪些小素数阻挡。"""
    seg = records[lo:hi+1]
    cols = [rec["col"] for rec in seg]
    ns = [rec["n"] for rec in seg]
    gaps = [b - a for a, b in zip(cols, cols[1:])]
    blockers = Counter()
    blocker_sets = []
    for a, b, n_a in zip(cols, cols[1:], ns):
        inner = []
        row_base = n_a - a
        for col in range(a + 1, b):
            n = row_base + col
            qs = [q for q in small_primes if n % q == 0]
            inner.extend(qs[:1])
        blockers.update(inner)
        blocker_sets.append(tuple(inner))
    return {
        "run_len": len(seg),
        "cols": cols,
        "gaps": gaps,
        "gap_word": ",".join(map(str, gaps)),
        "gap_med": sorted(gaps)[len(gaps)//2] if gaps else 0,
        "gap_max": max(gaps) if gaps else 0,
        "gap_counter": dict(Counter(gaps)),
        "top_blockers": blockers.most_common(5),
        "blocker_entropy_support": len(blockers),
        "blocker_sets": blocker_sets,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001,8009")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()

    print("P row start runLen span gapMed gapMax gapWord topBlockers blockerSupport")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        out = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                records = candidate_records(P, row, start, length, flags, plist, small_primes)
                for lo, hi in hit_runs(records):
                    if hi - lo + 1 < 4:
                        continue
                    prof = gap_pattern(records, lo, hi, small_primes)
                    span = prof["cols"][-1] - prof["cols"][0] + 1
                    out.append((prof["run_len"], span, row, start, prof))
        for _run_len, span, row, start, prof in sorted(out, key=lambda x: (x[0], x[1]), reverse=True)[: args.top]:
            blockers = ",".join(f"{q}:{v}" for q, v in prof["top_blockers"])
            print(P, row, start, prof["run_len"], span, prof["gap_med"], prof["gap_max"], prof["gap_word"], blockers, prof["blocker_entropy_support"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
