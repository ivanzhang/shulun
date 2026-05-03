#!/usr/bin/env python3
"""扫描粗半素数证书链的二部图能量。

左侧为小筛候选洞位置，右侧为 >sqrt(P) 的大因子证书；边表示该因子整除候选数。

用法示例：
  python3 experiments/semiprime_chain_bipartite_energy.py --Ps 503,1009 --top 8
"""
from __future__ import annotations

import argparse
import math
from collections import Counter, defaultdict

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct


def low_prime_rows(P: int, flags: bytearray, top: int) -> list[int]:
    rows = []
    for row in range(1, P + 1):
        count = sum(1 for col in range(1, P + 1) if flags[(row - 1) * P + col])
        rows.append((count, row))
    return [row for _count, row in sorted(rows)[:top]]


def window_graph(P: int, row: int, start: int, length: int, flags: bytearray, plist: list[int], small_primes: list[int]):
    B = math.isqrt(P)
    end = min(P, start + length - 1)
    left = []
    edges = []
    prime_left = 0
    triple_left = 0
    for col in range(start, end + 1):
        n = (row - 1) * P + col
        if any(n % q == 0 for q in small_primes):
            continue
        left.append(col)
        if flags[n]:
            prime_left += 1
            continue
        factors = factor_distinct(n, plist)
        large = [q for q in factors if q > B]
        if len(large) == len(factors) == 2:
            for q in large:
                edges.append((col, q))
        elif len(large) >= 3 and len(large) == len(factors):
            triple_left += 1
            for q in large:
                edges.append((col, q))
    right_to_left = defaultdict(list)
    left_to_right = defaultdict(list)
    for col, q in edges:
        right_to_left[q].append(col)
        left_to_right[col].append(q)
    reused_gaps = []
    for q, cols in right_to_left.items():
        cols = sorted(cols)
        for a, b in zip(cols, cols[1:]):
            reused_gaps.append(b - a)
    # 右侧一阶/二阶能量：sum deg, sum deg^2；复用越大，二阶能量越大。
    degrees = [len(cols) for cols in right_to_left.values()]
    edge_count = len(edges)
    right_count = len(degrees)
    energy2 = sum(d * d for d in degrees)
    collision = sum(d * (d - 1) // 2 for d in degrees)
    # 位置间距：候选洞的局部密度/连续链尺度。
    left_gaps = [b - a for a, b in zip(left, left[1:])]
    return {
        "row": row,
        "start": start,
        "end": end,
        "length": end - start + 1,
        "left": len(left),
        "prime_left": prime_left,
        "triple_left": triple_left,
        "semiprime_left": sum(1 for col, qs in left_to_right.items() if len(qs) == 2),
        "edges": edge_count,
        "right": right_count,
        "energy2": energy2,
        "collision": collision,
        "max_right_degree": max(degrees) if degrees else 0,
        "reused_factors": sum(1 for d in degrees if d > 1),
        "min_reuse_gap": min(reused_gaps) if reused_gaps else 0,
        "avg_left_gap": sum(left_gaps) / len(left_gaps) if left_gaps else 0.0,
        "max_left_gap": max(left_gaps) if left_gaps else 0,
        "covered_nonprime": len(left) - prime_left,
        "cover_ratio": (len(left) - prime_left) / len(left) if left else 0.0,
        "semiprime_ratio": sum(1 for col, qs in left_to_right.items() if len(qs) == 2) / len(left) if left else 0.0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003")
    parser.add_argument("--rows", default="")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()
    print("P row start len left prime nonprime semi triple edges right E2 coll maxDeg reused minReuseGap avgGap maxGap cover semiRatio")
    for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
        B = math.isqrt(P)
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small_primes = primes(sieve(B), B)
        rows = [int(x) for x in args.rows.split(",") if x.strip()] if args.rows else low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        recs = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride))
            starts.append(max_start)
            for start in sorted(set(starts)):
                if start < 1 or start > max_start:
                    continue
                recs.append(window_graph(P, row, start, length, flags, plist, small_primes))
        recs.sort(key=lambda r: (r["prime_left"], -r["cover_ratio"], -r["left"]))
        for r in recs[: args.top]:
            print(
                P, r["row"], r["start"], r["length"], r["left"], r["prime_left"], r["covered_nonprime"],
                r["semiprime_left"], r["triple_left"], r["edges"], r["right"], r["energy2"], r["collision"],
                r["max_right_degree"], r["reused_factors"], r["min_reuse_gap"], f"{r['avg_left_gap']:.2f}", r["max_left_gap"],
                f"{r['cover_ratio']:.3f}", f"{r['semiprime_ratio']:.3f}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
