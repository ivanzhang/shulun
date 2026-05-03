#!/usr/bin/env python3
"""扫描正常窗口中的粗半素数证书链结构。

用法示例：
  python3 experiments/semiprime_certificate_chain_scan.py --Ps 503,1009 --top 8
"""
from __future__ import annotations

import argparse
import math
from collections import Counter, defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct


def classify_window(P: int, row: int, start: int, length: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    """返回窗口中的小筛候选与粗半素数证书统计。"""
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    candidates = []
    primes_in_candidates = []
    semiprime_certs = []
    triple_or_more = []
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        candidates.append(col)
        if flags[n]:
            primes_in_candidates.append(col)
            continue
        factors = factor_distinct(n, plist)
        if all(q > B for q in factors):
            if len(factors) == 2:
                semiprime_certs.append((col, factors[0], factors[1]))
            else:
                triple_or_more.append((col, tuple(factors)))
    factor_positions = defaultdict(list)
    for col, u, v in semiprime_certs:
        factor_positions[u].append(col)
        factor_positions[v].append(col)
    reused = {q: cols for q, cols in factor_positions.items() if len(cols) > 1}
    close_reuse = []
    for q, cols in reused.items():
        cols = sorted(cols)
        for a, b in zip(cols, cols[1:]):
            if b - a < B:
                close_reuse.append((q, a, b, b - a))
    # 贪心估计最大“独立证书”数：每个半素数选一个尚未用过的大因子。
    used = set()
    independent = 0
    for col, u, v in sorted(semiprime_certs, key=lambda item: min(len(factor_positions[item[1]]), len(factor_positions[item[2]]))):
        if u not in used:
            used.add(u); independent += 1
        elif v not in used:
            used.add(v); independent += 1
    return {
        "row": row,
        "start": start,
        "end": end,
        "length": end - start + 1,
        "candidates": len(candidates),
        "prime_candidates": len(primes_in_candidates),
        "semiprimes": len(semiprime_certs),
        "triples": len(triple_or_more),
        "distinct_large_factors": len(factor_positions),
        "reused_factors": len(reused),
        "reuse_edges": sum(len(cols) - 1 for cols in reused.values()),
        "close_reuse": len(close_reuse),
        "independent_greedy": independent,
        "semiprime_ratio": len(semiprime_certs) / len(candidates) if candidates else 0.0,
        "covered_ratio": (len(semiprime_certs) + len(triple_or_more)) / len(candidates) if candidates else 0.0,
    }


def low_prime_rows(P: int, flags: bytearray, top: int) -> list[int]:
    """选素数最少的行，模拟最危险行。"""
    rows = []
    for row in range(1, P + 1):
        count = sum(1 for col in range(1, P + 1) if flags[(row - 1) * P + col])
        rows.append((count, row))
    return [row for _count, row in sorted(rows)[:top]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003")
    parser.add_argument("--rows", default="", help="指定行号；为空时选低素数行")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0, help="窗口长度 = factor * sqrt(P)")
    parser.add_argument("--stride-factor", type=float, default=1.0, help="步长 = factor * sqrt(P)")
    args = parser.parse_args()

    print("P row start length cand prime semi triple covered semiratio distinctLarge reused reuseEdges closeReuse indep")
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
            for start in range(1, P + 1, stride):
                if start + length - 1 > P:
                    start = max(1, P - length + 1)
                records.append(classify_window(P, row, start, length, flags, plist, small_primes))
                if start + length - 1 >= P:
                    break
        # 输出最危险：素数候选少、覆盖率高、候选多。
        records.sort(key=lambda r: (r["prime_candidates"], -r["covered_ratio"], -r["candidates"]))
        for rec in records[: args.top]:
            print(
                P,
                rec["row"],
                rec["start"],
                rec["length"],
                rec["candidates"],
                rec["prime_candidates"],
                rec["semiprimes"],
                rec["triples"],
                f"{rec['covered_ratio']:.3f}",
                f"{rec['semiprime_ratio']:.3f}",
                rec["distinct_large_factors"],
                rec["reused_factors"],
                rec["reuse_edges"],
                rec["close_reuse"],
                rec["independent_greedy"],
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
