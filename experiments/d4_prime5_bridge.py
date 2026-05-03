#!/usr/bin/env python3
"""D4poly-K5 到 P<=5 的有限桥接审查。

用途：若最终目标只有限验证 P<=5，则理论必须从 P=7 起接管。
本脚本检查 7<=P<=149 内，每个奇素数 P 的 D4poly 单位化容量
是否大于区间 X<=P 内的实际 d4 余项需求。
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import explicit_threshold_ledger as ledger  # noqa: E402


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def d4_prefix(max_n: int) -> list[int]:
    tau = [0] * (max_n + 1)
    for divisor in range(1, max_n + 1):
        for multiple in range(divisor, max_n + 1, divisor):
            tau[multiple] += 1
    d4 = [0] * (max_n + 1)
    for left in range(1, max_n + 1):
        max_right = max_n // left
        for right in range(1, max_right + 1):
            d4[left * right] += tau[left] * tau[right]
    prefix = [0] * (max_n + 1)
    total = 0
    for n in range(1, max_n + 1):
        total += d4[n]
        prefix[n] = total
    return prefix


def main() -> None:
    parser = argparse.ArgumentParser(description="检查 D4poly 是否允许最终只验证 P<=5")
    parser.add_argument("--max-p", type=int, default=149, help="桥接检查上界，默认 149")
    parser.add_argument("--quiet", action="store_true", help="只输出摘要")
    parser.add_argument("--csv", type=Path, help="把逐素数桥接证书写入 CSV 文件")
    parser.add_argument("--json", type=Path, help="把逐素数桥接证书写入 JSON 文件")
    args = parser.parse_args()

    coeffs = ledger.d4poly_stieltjes_coeffs()
    prefix = d4_prefix(args.max_p)

    def p3(log_x: float) -> float:
        return sum(coef * (log_x ** index) for index, coef in enumerate(coeffs))

    def k_needed(x: int) -> float:
        if x < 3:
            return 0.0
        remainder = prefix[x] - x * p3(math.log(x))
        return max(0.0, remainder / (x ** 0.75))

    worst_margin = float("inf")
    worst_row: tuple[int, float, float, int] | None = None
    failures: list[tuple[int, float, float, int]] = []
    rows: list[dict[str, float | int]] = []
    for prime in range(7, args.max_p + 1):
        if not is_prime(prime):
            continue
        capacity = ledger.d4poly_k_capacity(coeffs, math.log(prime))["K_d4_max_allowed"]
        needs = [(k_needed(x), x) for x in range(3, prime + 1)]
        need, witness = max(needs)
        margin = capacity - need
        if margin < worst_margin:
            worst_margin = margin
            worst_row = (prime, capacity, need, witness)
        rows.append({
            "P": prime,
            "log_P": math.log(prime),
            "capacity": capacity,
            "need": need,
            "witness_X": witness,
            "margin": margin,
        })
        if margin <= 0.0:
            failures.append((prime, capacity, need, witness))
        if not args.quiet:
            print(f"P={prime} capacity={capacity:.9f} need={need:.9f} witness_X={witness} margin={margin:.9f}")

    if args.csv is not None:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["P", "log_P", "capacity", "need", "witness_X", "margin"])
            writer.writeheader()
            writer.writerows(rows)
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({"rows": rows, "worst": worst_row, "failures": failures}, ensure_ascii=False, indent=2))

    if failures:
        print(f"FAIL failures={len(failures)} worst={worst_row}")
        raise SystemExit(1)
    print(f"SUMMARY: D4 bridge passed for odd primes 7<=P<={args.max_p}; worst={worst_row}; margin={worst_margin:.9f}")


if __name__ == "__main__":
    main()
