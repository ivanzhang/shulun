#!/usr/bin/env python3
"""比较长命中串中各 u 壳的实际半素数命中与素余因子容量。"""
from __future__ import annotations

import argparse
import bisect
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from semiprime_chain_bipartite_energy import low_prime_rows
from semiprime_hit_run_profile import candidate_records, hit_runs, run_profile


def prime_shell_capacity(P: int, n0: int, n1: int, prime_list: list[int]) -> tuple[Counter, Counter]:
    """精确计数 n=uv 落入 [n0,n1]、u 与 v 均为素数且 u<=v 的壳容量。"""
    B = math.isqrt(P)
    cap = Counter()
    distinct_u = Counter()
    lo = bisect.bisect_right(prime_list, B)
    hi = bisect.bisect_right(prime_list, P)
    for u in prime_list[lo:hi]:
        v0 = max(u, (n0 + u - 1) // u)
        v1 = n1 // u
        if v0 > v1:
            continue
        count = bisect.bisect_right(prime_list, v1) - bisect.bisect_left(prime_list, v0)
        if count <= 0:
            continue
        shell = int(math.floor(math.log(max(u, B) / B, 2)))
        cap[shell] += count
        distinct_u[shell] += 1
    return cap, distinct_u


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()

    print("P row start runLen span actualSemiShells primeCapShells primeCap/actual distinctU")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        rows_out = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                records = candidate_records(P, row, start, length, flags, plist, small_primes)
                for lo, hi in hit_runs(records):
                    if hi - lo + 1 < 4:
                        continue
                    prof = run_profile(P, records, lo, hi)
                    n0 = records[lo]["n"]
                    n1 = records[hi]["n"]
                    cap, distinct_u = prime_shell_capacity(P, n0, n1, plist)
                    actual = Counter()
                    for rec in records[lo:hi+1]:
                        factors = tuple(sorted(rec["factors"]))
                        if len(factors) == 2 and factors[0] > B:
                            shell = int(math.floor(math.log(max(factors[0], B) / B, 2)))
                            actual[shell] += 1
                    total_actual = sum(actual.values())
                    total_cap = sum(cap.values())
                    if total_actual:
                        rows_out.append((prof["run_len"], total_actual, total_cap, row, start, n1 - n0 + 1, actual, cap, distinct_u))
        for run_len, total_actual, total_cap, row, start, span, actual, cap, distinct_u in sorted(rows_out, key=lambda x: (x[0], x[2]), reverse=True)[: args.top]:
            actual_s = ",".join(f"s{k}:{v}" for k, v in sorted(actual.items()))
            cap_s = ",".join(f"s{k}:{v}" for k, v in sorted(cap.items()) if v)
            du_s = ",".join(f"s{k}:{v}" for k, v in sorted(distinct_u.items()) if v)
            ratio = total_cap / total_actual if total_actual else 0.0
            print(P, row, start, run_len, span, actual_s, cap_s, f"{ratio:.2f}", du_s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
