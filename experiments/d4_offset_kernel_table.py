#!/usr/bin/env python3
"""D4 R5 固定偏移核表。

对 a|x+h 的偏移团，记录相位只由 h/a 决定这一离散结构，
并用实际 contract/tau 诊断平均核压缩。

用法示例：
  python3 experiments/d4_offset_kernel_table.py \
    --x 1028143 --h 17 --hi 400 --json docs/d4-r5-offset-kernel-x1028143-h17.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

G = 0.5772156649015328606


def build(n: int) -> tuple[list[int], list[int]]:
    """构造 tau 与前缀和。"""
    tau = [0] * (n + 1)
    for d in range(1, n + 1):
        for m in range(d, n + 1, d):
            tau[m] += 1
    prefix = [0] * (n + 1)
    total = 0
    for i in range(1, n + 1):
        total += tau[i]
        prefix[i] = total
    return tau, prefix


def delta(prefix: list[int], y: float) -> float:
    """中心化除数余项。"""
    return prefix[int(math.floor(y))] - y * (math.log(y) + 2 * G - 1)


def term(x: int, a: int, q: float, tau: list[int], prefix: list[int]) -> dict:
    """单个 a 的 contract 核。"""
    k1 = int(math.floor(x / a))
    k2 = int(math.floor(2 * x / a))
    c_norm = 2 * tau[a] * delta(prefix, x / a) / (x ** 0.75)
    old_norm = 2 * tau[a] * delta(prefix, 2 * x / a) / ((2 * x) ** 0.75)
    contract = old_norm - q * c_norm
    return {
        "a": a,
        "tau": tau[a],
        "contract": contract,
        "positive_contract": max(0.0, contract),
        "kernel": max(0.0, contract) / tau[a] if tau[a] else 0.0,
        "c_norm": c_norm,
        "old_norm": old_norm,
        "frac_x_over_a": x / a - k1,
        "frac_2x_over_a": 2 * x / a - k2,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1_028_143)
    parser.add_argument("--h", type=int, default=17)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    tau, prefix = build(2 * args.x + 10)
    rows = []
    for a in range(1, min(args.hi, math.isqrt(args.x)) + 1):
        if (args.x + args.h) % a != 0:
            continue
        row = term(args.x, a, args.q, tau, prefix)
        h_mod = args.h % a
        complement = (args.x + args.h) // a
        row.update(
            {
                "complement": complement,
                "log_complement": math.log(complement),
                "h_mod_a": h_mod,
                "phase_formula_x": 0.0 if h_mod == 0 else 1.0 - h_mod / a,
                "phase_formula_2x": ((-2.0 * h_mod / a) % 1.0),
                "phase_error_x": row["frac_x_over_a"] - (0.0 if h_mod == 0 else 1.0 - h_mod / a),
                "phase_error_2x": row["frac_2x_over_a"] - ((-2.0 * h_mod / a) % 1.0),
            }
        )
        rows.append(row)

    positive = [row for row in rows if row["positive_contract"] > 0]
    payload = {
        "x": args.x,
        "h": args.h,
        "hi": args.hi,
        "q": args.q,
        "divisor_count": len(rows),
        "positive_count": len(positive),
        "tau_sum": sum(row["tau"] for row in rows),
        "positive_tau_sum": sum(row["tau"] for row in positive),
        "positive_contract_sum": sum(row["positive_contract"] for row in positive),
        "average_kernel": (
            sum(row["positive_contract"] for row in positive)
            / sum(row["tau"] for row in positive)
            if positive
            else 0.0
        ),
        "max_kernel": max((row["kernel"] for row in positive), default=0.0),
        "phase_error_max": max(
            [abs(row["phase_error_x"]) for row in rows]
            + [abs(row["phase_error_2x"]) for row in rows]
            + [0.0]
        ),
        "weighted_log_complement": (
            sum(row["tau"] * row["kernel"] * row["log_complement"] for row in positive)
            / sum(row["positive_contract"] for row in positive)
            if positive and sum(row["positive_contract"] for row in positive)
            else 0.0
        ),
        "top_positive": sorted(positive, key=lambda row: row["positive_contract"], reverse=True)[:50],
        "rows": rows,
    }

    print(
        json.dumps(
            {k: v for k, v in payload.items() if k not in {"top_positive", "rows"}},
            indent=2,
        )
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
