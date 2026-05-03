#!/usr/bin/env python3
"""估计命中串所在短整数段中各 dyadic u 壳的理论容量与实际命中。"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from semiprime_chain_bipartite_energy import low_prime_rows
from semiprime_hit_run_profile import candidate_records, hit_runs, run_profile


def shell_capacity(P: int, n0: int, n1: int, small_primes: list[int]) -> tuple[Counter, Counter]:
    """粗略数短段 [n0,n1] 内每个 u 壳可产生的因子命中容量。"""
    B = math.isqrt(P)
    cap = Counter()
    distinct_u = Counter()
    for u in range(B + 1, P + 1):
        # 只把 u 当作大素因子证书；脚本用素数 u 贴近半素数主层。
        if u not in small_primes and any(u % q == 0 for q in small_primes if q * q <= u):
            continue
        first = ((n0 + u - 1) // u) * u
        if first > n1:
            continue
        count = (n1 - first) // u + 1
        shell = int(math.floor(math.log(max(u, B) / B, 2))) if u >= B else -1
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

    print("P row start runLen span actualShells capShells cap/actual distinctU")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        records_out = []
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
                    cap, distinct_u = shell_capacity(P, n0, n1, small_primes)
                    actual = Counter(prof["shells"])
                    total_actual = sum(actual.values())
                    total_cap = sum(cap.values())
                    records_out.append((prof["run_len"], total_actual, total_cap, row, start, n1 - n0 + 1, actual, cap, distinct_u))
        for run_len, total_actual, total_cap, row, start, span, actual, cap, distinct_u in sorted(records_out, key=lambda x: (x[0], x[2]), reverse=True)[: args.top]:
            actual_s = ",".join(f"s{k}:{v}" for k, v in sorted(actual.items()))
            cap_s = ",".join(f"s{k}:{v}" for k, v in sorted(cap.items()) if v)
            du_s = ",".join(f"s{k}:{v}" for k, v in sorted(distinct_u.items()) if v)
            ratio = total_cap / total_actual if total_actual else 0.0
            print(P, row, start, run_len, span, actual_s, cap_s, f"{ratio:.2f}", du_s)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
