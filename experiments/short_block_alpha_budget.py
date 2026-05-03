#!/usr/bin/env python3
"""计算 R0 短块主项缺口所需的 singular factor 平均放大预算。

用法示例：
  python3 experiments/short_block_alpha_budget.py --R 8
  python3 experiments/short_block_alpha_budget.py --theta 0.882493041988 --K 2.0 --R 8
"""
from __future__ import annotations

import argparse
import math


def default_theta() -> float:
    """返回精细半素数+三粗因子覆盖常数。"""
    gamma = 0.5772156649015329
    semiprime = math.exp(gamma) * math.log(3.0) / 4.0
    theta3 = 0.393316030635
    return semiprime + theta3


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--R", type=int, default=8, help="短块长度 R0")
    parser.add_argument("--theta", type=float, default=None, help="单点粗合数覆盖上界")
    parser.add_argument("--K", type=float, default=2.0, help="singular factor 加权平均放大因子")
    args = parser.parse_args()

    theta = default_theta() if args.theta is None else args.theta
    base = theta ** args.R
    alpha = args.K * base
    k_critical = 1.0 / base if base else float("inf")
    gamma = max(0.0, (1.0 - alpha) / 2.0)

    print("R theta theta^R K alpha=(K theta^R) Kcrit gamma=(1-alpha)/2")
    print(
        args.R,
        f"{theta:.12f}",
        f"{base:.12f}",
        f"{args.K:.6f}",
        f"{alpha:.12f}",
        f"{k_critical:.6f}",
        f"{gamma:.12f}",
    )

    print("\nK sensitivity")
    for K in [1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.7]:
        alpha_k = K * base
        print(f"K={K:.2f} alpha={alpha_k:.6f} gap={1-alpha_k:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
