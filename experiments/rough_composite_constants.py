#!/usr/bin/env python3
"""复核行方向粗合数覆盖常数。

用法示例：
  python3 experiments/rough_composite_constants.py
"""
from __future__ import annotations

import math


def simpson_integral(func, a: float, b: float, n: int = 200_000) -> float:
    """用 Simpson 公式做稳定数值积分。"""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = func(a) + func(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * func(a + i * h)
    return total * h / 3.0


def main() -> int:
    gamma = 0.5772156649015329
    semiprime = math.exp(gamma) * math.log(3.0) / 4.0
    integrand = lambda t: 4.0 * math.log(2.0 - t) / ((1.0 + t) * (3.0 - t))
    i3 = simpson_integral(integrand, 0.0, 1.0)
    theta3 = math.exp(gamma) * i3 / 2.0
    total = semiprime + theta3
    print(f"I3={i3:.15f}")
    print(f"semiprime_const={semiprime:.15f}")
    print(f"theta3_model={theta3:.15f}")
    print(f"total_cover={total:.15f}")
    print(f"raw_gap={1.0 - total:.15f}")
    print(f"half_gap={(1.0 - total) / 2.0:.15f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
