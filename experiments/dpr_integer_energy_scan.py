#!/usr/bin/env python3
"""DPR-int 扫描：整数区间倒数投影二阶能量。"""
from __future__ import annotations

import argparse
from collections import Counter
from math import isqrt


def bucket_bounds(P: int, bucket: int) -> tuple[int, int]:
    d = isqrt(P)
    return (2 ** bucket) * d, min((2 ** (bucket + 1)) * d, P)


def scan(P: int, A: int, bucket: int, e_values: list[int]) -> dict:
    lo, hi = bucket_bounds(P, bucket)
    vals = [(A * pow(n, -1, P)) % P for n in range(max(1, lo + 1), hi)]
    n = len(vals)
    rows = []
    for e in e_values:
        counts = Counter(v % e for v in vals)
        second = sum(x * x for x in counts.values())
        model = n * n / e + n
        rows.append({
            "e": e,
            "n": n,
            "classes": len(counts),
            "max": max(counts.values(), default=0),
            "second": second,
            "model": round(model, 3),
            "ratio": round(second / model, 3) if model else None,
        })
    return {"P": P, "A": A, "D": isqrt(P), "bucket": bucket, "range": (lo, hi), "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--A", type=int, default=219)
    parser.add_argument("--bucket", type=int, default=4)
    parser.add_argument("--e", nargs="+", type=int, default=[2, 3, 5, 7, 10, 30, 70, 210])
    args = parser.parse_args()
    print(scan(args.P, args.A, args.bucket, args.e))


if __name__ == "__main__":
    main()
