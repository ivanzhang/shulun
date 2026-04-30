#!/usr/bin/env python3
"""有限验证 P×P 方阵行列素数命题。

用法示例：
  python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json
  python3 experiments/verify_small_prime_square.py --max-p 10000 --out docs/finite-verify-10000.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve(limit: int) -> list[bool]:
    """返回 0..limit 的素数布尔表。"""
    is_prime = [False, False] + [True] * max(0, limit - 1)
    for n in range(2, int(limit ** 0.5) + 1):
        if is_prime[n]:
            step = n
            start = n * n
            is_prime[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)
    return is_prime


def primes_upto(limit: int, is_prime: list[bool]) -> list[int]:
    """列出不超过 limit 的奇素数。"""
    return [n for n in range(3, limit + 1) if is_prime[n]]


def verify_p(p: int, is_prime: list[bool]) -> dict[str, object]:
    """验证单个 P 的每行、每列是否至少含一个素数。"""
    row_counts: list[int] = []
    bad_rows: list[int] = []
    for row in range(1, p + 1):
        start = (row - 1) * p + 1
        count = sum(1 for value in range(start, start + p) if is_prime[value])
        row_counts.append(count)
        if count == 0:
            bad_rows.append(row)

    col_counts: list[int] = []
    bad_cols: list[int] = []
    for col in range(1, p + 1):
        count = sum(1 for row in range(1, p + 1) if is_prime[(row - 1) * p + col])
        col_counts.append(count)
        if count == 0:
            bad_cols.append(col)

    return {
        "P": p,
        "ok": not bad_rows and not bad_cols,
        "bad_rows": bad_rows,
        "bad_cols": bad_cols,
        "min_row_prime_count": min(row_counts),
        "min_col_prime_count": min(col_counts),
        "total_primes_in_square": sum(row_counts),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--max-log", type=float, help="验证 P<=floor(exp(max-log))")
    group.add_argument("--max-p", type=int, help="验证 P<=max-p")
    parser.add_argument("--out", type=Path, required=True, help="输出 JSON 证书路径")
    args = parser.parse_args()

    max_p = int(math.floor(math.exp(args.max_log))) if args.max_log is not None else args.max_p
    max_value = max_p * max_p
    is_prime = sieve(max_value)
    primes = primes_upto(max_p, is_prime)

    records = [verify_p(p, is_prime) for p in primes]
    failures = [record for record in records if not record["ok"]]
    certificate = {
        "max_p": max_p,
        "max_value_checked": max_value,
        "odd_prime_count": len(primes),
        "ok": not failures,
        "failures": failures,
        "worst_min_row_prime_count": min((r["min_row_prime_count"] for r in records), default=None),
        "worst_min_col_prime_count": min((r["min_col_prime_count"] for r in records), default=None),
        "records": records,
    }
    args.out.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: certificate[k] for k in certificate if k != "records"}, ensure_ascii=False, indent=2))
    return 0 if certificate["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
