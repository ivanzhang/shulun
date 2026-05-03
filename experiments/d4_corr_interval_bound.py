#!/usr/bin/env python3
"""D4 双曲线相关和的区间证书原型。

对给定 X 区间 [L,R]，用采样/端点计算 C(X)/X^(3/4) 的实际最大值，
用于设计后续可证明的 dyadic 证书。
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

GAMMA = 0.5772156649015328606


def build_tau_prefix(n: int):
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
    return A[int(math.floor(y))] - y * (math.log(y) + 2.0 * GAMMA - 1.0)


def corr_norm(x: int, tau: list[int], A: list[int]) -> tuple[float, float, float]:
    r = math.isqrt(x)
    corr = 0.0
    abs_corr = 0.0
    for a in range(1, r + 1):
        term = tau[a] * delta_real(A, x / a)
        corr += term
        abs_corr += abs(term)
    scale = x ** 0.75
    return 2.0 * corr / scale, 2.0 * abs_corr / scale, r


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1_000_000)
    parser.add_argument("--end", type=int, default=10_000_000)
    parser.add_argument("--step", type=int, default=1000)
    parser.add_argument("--json", type=Path, help="导出区间采样证书 JSON")
    args = parser.parse_args()
    tau, A = build_tau_prefix(args.end)
    best = (-1e99, None, None)
    best_abs = (-1e99, None, None)
    for x in range(args.start, args.end + 1, args.step):
        c, ac, r = corr_norm(x, tau, A)
        if c > best[0]:
            best = (c, x, r)
        if ac > best_abs[0]:
            best_abs = (ac, x, r)
    print(f"INTERVAL [{args.start},{args.end}] step={args.step} best_corr_norm={best[0]:.9f} at X={best[1]} sqrt={best[2]}")
    print(f"INTERVAL [{args.start},{args.end}] step={args.step} best_abs_corr_norm={best_abs[0]:.9f} at X={best_abs[1]} sqrt={best_abs[2]}")
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({
            "start": args.start,
            "end": args.end,
            "step": args.step,
            "best_corr_norm": best[0],
            "best_corr_x": best[1],
            "best_corr_sqrt": best[2],
            "best_abs_corr_norm": best_abs[0],
            "best_abs_corr_x": best_abs[1],
            "best_abs_corr_sqrt": best_abs[2],
        }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
