#!/usr/bin/env python3
"""有限核验 Chebyshev theta 函数上界。

用法示例：
  python3 experiments/check_theta_cheb.py --max-x 2000000 --constant 1.04
  python3 experiments/check_theta_cheb.py --max-x 10000000 --constant 1.01 --json

说明：
  该脚本只验证有限区间 2<=x<=max_x，不替代大范围显式解析估计。
  它用于生成 tiny 层 C_Cheb 的小范围核验表。
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass


@dataclass
class ThetaCheckResult:
    max_x: int
    constant: float
    max_ratio: float
    max_ratio_at: int
    first_failure_at: int | None
    first_failure_ratio: float | None
    ok: bool


def check_theta(max_x: int, constant: float) -> ThetaCheckResult:
    if max_x < 2:
        raise SystemExit("--max-x 必须至少为 2。")
    if constant <= 0:
        raise SystemExit("--constant 必须为正数。")

    # Eratosthenes 筛；bytearray 便于中等范围快速核验。
    is_prime = bytearray(b"\x01") * (max_x + 1)
    is_prime[0:2] = b"\x00\x00"
    limit = int(max_x**0.5)
    for value in range(2, limit + 1):
        if is_prime[value]:
            start = value * value
            is_prime[start : max_x + 1 : value] = b"\x00" * (((max_x - start) // value) + 1)

    theta = 0.0
    max_ratio = 0.0
    max_ratio_at = 2
    first_failure_at: int | None = None
    first_failure_ratio: float | None = None

    for value in range(2, max_x + 1):
        if is_prime[value]:
            theta += math.log(value)
        ratio = theta / value
        if ratio > max_ratio:
            max_ratio = ratio
            max_ratio_at = value
        if first_failure_at is None and ratio > constant:
            first_failure_at = value
            first_failure_ratio = ratio

    return ThetaCheckResult(
        max_x=max_x,
        constant=constant,
        max_ratio=max_ratio,
        max_ratio_at=max_ratio_at,
        first_failure_at=first_failure_at,
        first_failure_ratio=first_failure_ratio,
        ok=first_failure_at is None,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="有限核验 theta(x) <= C x")
    parser.add_argument("--max-x", type=int, required=True, help="有限核验上界")
    parser.add_argument("--constant", type=float, default=1.04, help="待核验常数 C")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args()

    result = check_theta(args.max_x, args.constant)
    if args.json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
        return
    print(f"theta(x) <= {result.constant} x for 2 <= x <= {result.max_x}: {result.ok}")
    print(f"max theta(x)/x = {result.max_ratio:.12f} at x = {result.max_ratio_at}")
    if not result.ok:
        print(f"first failure at x = {result.first_failure_at}, ratio = {result.first_failure_ratio:.12f}")


if __name__ == "__main__":
    main()
