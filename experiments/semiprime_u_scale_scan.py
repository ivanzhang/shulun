#!/usr/bin/env python3
"""扫描危险窗口中粗半素数证书的 u 尺度分布。

对 n=uv, u<=v, u,v>sqrt(P)，统计 u/P^a 的指数 a、v/u 比例、以及窗口内命中间距。
"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows


def collect_window(P, row, start, length, flags, plist, small_primes):
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    certs = []
    left = []
    prime_count = 0
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        left.append(col)
        if flags[n]:
            prime_count += 1
            continue
        factors = factor_distinct(n, plist)
        if len(factors) == 2 and all(q > B for q in factors):
            u, v = sorted(factors)
            certs.append((col, n, u, v))
    return left, prime_count, certs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()
    print("P row start len cand prime semi amin aavg amax uMin/P^0.5 uMed/P^0.5 v/u_med gapMed gapMax bins")
    for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        B = math.isqrt(P)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        records = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                left, prime_count, certs = collect_window(P, row, start, length, flags, plist, small_primes)
                if not left or not certs:
                    continue
                cover = (len(left) - prime_count) / len(left)
                records.append((prime_count, -cover, -len(left), row, start, left, certs))
        for _pc, _negcover, _negleft, row, start, left, certs in sorted(records)[: args.top]:
            us = [u for _c, _n, u, _v in certs]
            ratios = [v / u for _c, _n, u, v in certs]
            exps = [math.log(u, P) for u in us]
            cols = sorted(c for c, _n, _u, _v in certs)
            gaps = [b - a for a, b in zip(cols, cols[1:])]
            bins = Counter(int((a - 0.5) / 0.05) for a in exps)
            bin_str = ";".join(f"{0.5+0.05*k:.2f}-{0.55+0.05*k:.2f}:{v}" for k, v in sorted(bins.items()))
            us_sorted = sorted(us)
            print(
                P, row, start, length, len(left), sum(1 for c in left if all(c != cert[0] for cert in certs)), len(certs),
                f"{min(exps):.3f}", f"{sum(exps)/len(exps):.3f}", f"{max(exps):.3f}",
                f"{min(us)/(P**0.5):.2f}", f"{us_sorted[len(us)//2]/(P**0.5):.2f}",
                f"{sorted(ratios)[len(ratios)//2]:.2f}",
                (sorted(gaps)[len(gaps)//2] if gaps else 0), (max(gaps) if gaps else 0), bin_str,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
