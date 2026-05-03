#!/usr/bin/env python3
"""D4K5 尾段总余项证书原型：相关和 + lead/square 残差。"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

GAMMA = 0.5772156649015328606
GAMMA1 = -0.0728158454836767249
GAMMA2 = -0.00969036319287231848


def build_tau_prefix(n: int):
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    pref = [0] * (n + 1)
    run = 0
    for i in range(1, n + 1):
        run += tau[i]
        pref[i] = run
    return tau, pref


def p3(log_x: float) -> float:
    coeffs = [
        -1.0 + 4.0 * GAMMA - 6.0 * GAMMA * GAMMA + 4.0 * GAMMA1 + 4.0 * GAMMA**3 - 12.0 * GAMMA * GAMMA1 + 2.0 * GAMMA2,
        1.0 - 4.0 * GAMMA + 6.0 * GAMMA * GAMMA - 4.0 * GAMMA1,
        -0.5 + 2.0 * GAMMA,
        1.0 / 6.0,
    ]
    return sum(c * log_x**i for i, c in enumerate(coeffs))


def delta_real(A: list[int], y: float) -> float:
    return A[int(math.floor(y))] - y * (math.log(y) + 2.0 * GAMMA - 1.0)


def corr(x: int, tau: list[int], A: list[int]) -> float:
    return 2.0 * sum(tau[a] * delta_real(A, x / a) for a in range(1, math.isqrt(x) + 1))


def lead_square_residual(x: int, tau: list[int], A: list[int]) -> float:
    r = math.isqrt(x)
    s1 = sum(tau[a] / a for a in range(1, r + 1))
    s2 = sum(tau[a] * math.log(a) / a for a in range(1, r + 1))
    lead = 2.0 * x * ((math.log(x) + 2.0 * GAMMA - 1.0) * s1 - s2)
    square = -(A[r] ** 2)
    return lead + square - x * p3(math.log(x))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1_000_000)
    parser.add_argument("--end", type=int, default=1_010_000)
    parser.add_argument("--step", type=int, default=100)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    tau, A = build_tau_prefix(args.end)
    best_total = (-1e100, None, None, None)
    best_res = (-1e100, None)
    for x in range(args.start, args.end + 1, args.step):
        c = corr(x, tau, A)
        r = lead_square_residual(x, tau, A)
        total = (c + r) / (x ** 0.75)
        res_norm = r / (x ** 0.75)
        if total > best_total[0]:
            best_total = (total, x, c / (x ** 0.75), res_norm)
        if res_norm > best_res[0]:
            best_res = (res_norm, x)
    payload = {
        "start": args.start,
        "end": args.end,
        "step": args.step,
        "best_total_norm": best_total[0],
        "best_total_x": best_total[1],
        "corr_norm_at_best": best_total[2],
        "residual_norm_at_best": best_total[3],
        "best_residual_norm": best_res[0],
        "best_residual_x": best_res[1],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
