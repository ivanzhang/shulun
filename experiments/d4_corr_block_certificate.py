#!/usr/bin/env python3
"""D4 相关和 C(X) 的 floor 分段严格上界原型。

目标：对 X in [L,R] 证明 C(X)=2 sum_{a<=sqrt(X)} tau(a) Delta(X/a) <= B X^(3/4)。
当前版本用 a-block 分割，对每块用端点网格上确界近似，作为严格证书设计原型。
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
    pref_tau = [0] * (n + 1)
    run = 0
    for i in range(1, n + 1):
        run += tau[i]
        pref_tau[i] = run
    A = pref_tau
    return tau, pref_tau, A


def delta_real(A: list[int], y: float) -> float:
    return A[int(math.floor(y))] - y * (math.log(y) + 2.0 * GAMMA - 1.0)


def delta_real_derivative(y: float) -> float:
    # 在 floor(y) 固定的开区间内，Delta(y)=const-y(log y+2gamma-1)。
    return -(math.log(y) + 2.0 * GAMMA)


def corr_exact(x: int, tau: list[int], A: list[int]) -> float:
    total = 0.0
    for a in range(1, math.isqrt(x) + 1):
        total += tau[a] * delta_real(A, x / a)
    return 2.0 * total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, default=1_000_000)
    parser.add_argument("--end", type=int, default=1_010_000)
    parser.add_argument("--block", type=int, default=10)
    parser.add_argument("--x-step", type=int, default=100)
    parser.add_argument("--endpoint", action="store_true", help="使用 floor(X/a) 端点枚举替代 X 网格采样")
    parser.add_argument("--json", type=Path, help="导出块证书 JSON")
    args = parser.parse_args()

    tau, pref_tau, A = build_tau_prefix(args.end)
    sqrt_r = math.isqrt(args.end)
    block_bounds = []
    for lo in range(1, sqrt_r + 1, args.block):
        hi = min(sqrt_r, lo + args.block - 1)
        weight = pref_tau[hi] - pref_tau[lo - 1]
        best_sum = -1e100
        best_x = None
        if args.endpoint:
            candidates = {args.start, args.end}
            for a in range(lo, hi + 1):
                # a <= sqrt(X) changes at X=a^2.
                if args.start <= a * a <= args.end:
                    candidates.add(a * a)
                    if a * a + 1 <= args.end:
                        candidates.add(a * a + 1)
                m_min = max(1, args.start // a - 2)
                m_max = args.end // a + 2
                for m in range(m_min, m_max + 1):
                    for x0 in (a * m, a * (m + 1)):
                        if args.start <= x0 <= args.end:
                            candidates.add(x0)
                        if args.start <= x0 - 1 <= args.end:
                            candidates.add(x0 - 1)
                        if args.start <= x0 + 1 <= args.end:
                            candidates.add(x0 + 1)
            for x in sorted(candidates):
                local_hi = min(hi, math.isqrt(x))
                if local_hi < lo:
                    continue
                val = sum(tau[a] * delta_real(A, x / a) for a in range(lo, local_hi + 1))
                if val > best_sum:
                    best_sum = val
                    best_x = x
        else:
            # 原型：保留块内符号和，而不是对每块取正部上界。
            for x in range(args.start, args.end + 1, args.x_step):
                local_hi = min(hi, math.isqrt(x))
                if local_hi < lo:
                    continue
                val = sum(tau[a] * delta_real(A, x / a) for a in range(lo, local_hi + 1))
                if val > best_sum:
                    best_sum = val
                    best_x = x
        block_bounds.append((lo, hi, weight, best_sum, best_x, 2.0 * best_sum))
    bound = sum(row[-1] for row in block_bounds)
    exact_best = (-1e100, None)
    for x in range(args.start, args.end + 1, args.x_step):
        val = corr_exact(x, tau, A)
        norm = val / (x ** 0.75)
        if norm > exact_best[0]:
            exact_best = (norm, x)
    norm_bound = bound / (args.start ** 0.75)
    mode = "endpoint" if args.endpoint else f"grid x_step={args.x_step}"
    print(f"INTERVAL [{args.start},{args.end}] block={args.block} mode={mode}")
    print(f"prototype_bound_norm={norm_bound:.9f} blocks={len(block_bounds)}")
    print(f"sample_exact_best_norm={exact_best[0]:.9f} at X={exact_best[1]}")
    print("top_blocks:")
    for row in sorted(block_bounds, key=lambda r: r[-1], reverse=True)[:10]:
        print(row)
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps({
            "start": args.start,
            "end": args.end,
            "block": args.block,
            "mode": "endpoint" if args.endpoint else "grid",
            "x_step": args.x_step,
            "prototype_bound_norm": norm_bound,
            "sample_exact_best_norm": exact_best[0],
            "sample_exact_best_x": exact_best[1],
            "blocks": [
                {
                    "lo": row[0],
                    "hi": row[1],
                    "weight": row[2],
                    "best_sum": row[3],
                    "best_x": row[4],
                    "contribution_bound": row[5],
                }
                for row in block_bounds
            ],
        }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
