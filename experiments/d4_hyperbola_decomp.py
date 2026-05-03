#!/usr/bin/env python3
"""分析 D4 双曲线公式中各误差项的实际贡献。"""
from __future__ import annotations

import argparse
import math

GAMMA = 0.5772156649015328606
GAMMA1 = -0.0728158454836767249
GAMMA2 = -0.00969036319287231848


def p3(log_x: float) -> float:
    coeffs = [
        -1.0 + 4.0 * GAMMA - 6.0 * GAMMA * GAMMA + 4.0 * GAMMA1 + 4.0 * GAMMA**3 - 12.0 * GAMMA * GAMMA1 + 2.0 * GAMMA2,
        1.0 - 4.0 * GAMMA + 6.0 * GAMMA * GAMMA - 4.0 * GAMMA1,
        -0.5 + 2.0 * GAMMA,
        1.0 / 6.0,
    ]
    return sum(c * log_x**i for i, c in enumerate(coeffs))


def arrays(n: int):
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    A = [0] * (n + 1)
    run = 0
    for i in range(1, n + 1):
        run += tau[i]
        A[i] = run
    return tau, A


def delta_real(A: list[int], y: float) -> float:
    floor_y = int(math.floor(y))
    return A[floor_y] - y * (math.log(y) + 2.0 * GAMMA - 1.0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xs", nargs="*", type=int, default=[720, 5040, 1000000])
    args = parser.parse_args()
    max_x = max(args.xs)
    tau, A = arrays(max_x)
    for x in args.xs:
        r = math.isqrt(x)
        s1 = sum(tau[a] / a for a in range(1, r + 1))
        s2 = sum(tau[a] * math.log(a) / a for a in range(1, r + 1))
        lead = 2.0 * x * ((math.log(x) + 2.0 * GAMMA - 1.0) * s1 - s2)
        delta_r = delta_real(A, math.sqrt(x))
        square = -(A[r] ** 2)
        corr = 0.0
        abs_corr = 0.0
        for a in range(1, r + 1):
            term = tau[a] * delta_real(A, x / a)
            corr += term
            abs_corr += abs(term)
        corr *= 2.0
        abs_corr *= 2.0
        d4 = sum(tau[a] * A[x // a] for a in range(1, x + 1))
        rem = d4 - x * p3(math.log(x))
        poly_main = x * p3(math.log(x))
        print(
            f"X={x} rem={rem:.6f} rem_norm={rem/x**0.75:.6f} "
            f"corr={corr:.6f} corr_norm={corr/x**0.75:.6f} "
            f"abs_corr_norm={abs_corr/x**0.75:.6f} sqrt={r}"
        )
        print(
            f"  lead-poly={(lead-poly_main)/x**0.75:.6f} "
            f"square={square/x**0.75:.6f} delta_r={delta_r:.6f} "
            f"sum_norm={(lead+corr+square-poly_main)/x**0.75:.6f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
