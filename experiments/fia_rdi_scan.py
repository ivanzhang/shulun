#!/usr/bin/env python3
"""FIA/RDI 扫描：倒数差集命中区间 B 的二重计数。"""
from __future__ import annotations

import argparse
from math import isqrt


def bucket_bounds(P: int, bucket: int) -> tuple[int, int]:
    d = isqrt(P)
    return (2 ** bucket) * d, min((2 ** (bucket + 1)) * d, P)


def count_rdi(P: int, I: tuple[int, int], B: tuple[int, int], A: int = 1) -> int:
    lo, hi = I
    blo, bhi = B
    invs = [(A * pow(x, -1, P)) % P for x in range(max(1, lo), min(hi, P))]
    count = 0
    for u in invs:
        for v in invs:
            w = (u - v) % P
            if blo <= w < bhi:
                count += 1
    return count


def scan(P: int, bucket: int, b_sizes: list[int], starts: list[int]) -> dict:
    I = bucket_bounds(P, bucket)
    n = max(0, min(I[1], P) - max(1, I[0]))
    rows = []
    for size in b_sizes:
        for start in starts:
            B = (start % P, min(P, start % P + size))
            if B[1] <= B[0]:
                continue
            c = count_rdi(P, I, B)
            main = (B[1] - B[0]) * n * n / P
            model = main + n + (B[1] - B[0])
            rows.append({
                "B": B,
                "count": c,
                "main": round(main, 3),
                "model_main+n+B": round(model, 3),
                "ratio_model": round(c / model, 3) if model else None,
                "excess_over_main": round(c - main, 3),
            })
    return {"P": P, "D": isqrt(P), "bucket": bucket, "I": I, "n": n, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=2003)
    parser.add_argument("--bucket", type=int, default=4)
    parser.add_argument("--b-sizes", nargs="+", type=int, default=[10, 30, 70, 210])
    parser.add_argument("--starts", nargs="+", type=int, default=[0, 17, 101, 503])
    args = parser.parse_args()
    print(scan(args.P, args.bucket, args.b_sizes, args.starts))


if __name__ == "__main__":
    main()
