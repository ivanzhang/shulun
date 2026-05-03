#!/usr/bin/env python3
"""D4 R5 低块同相团容量诊断。

用法示例：
  python3 experiments/d4_lowblock_phase_capacity.py \
    --x 1028143 --hi 400 --json docs/d4-r5-phase-capacity-x1028143.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

G = 0.5772156649015328606


def build(n: int) -> tuple[list[int], list[int]]:
    """构造除数函数和前缀和。"""
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
    """Dirichlet divisor problem 的中心化余项。"""
    return prefix[int(math.floor(y))] - y * (math.log(y) + 2 * G - 1)


def term_rows(x: int, hi: int, q: float, tau: list[int], prefix: list[int]) -> list[dict]:
    """逐 a 计算 contract 项和相位。"""
    rows = []
    active_hi = min(hi, math.isqrt(x))
    for a in range(1, active_hi + 1):
        k1 = int(math.floor(x / a))
        k2 = int(math.floor(2 * x / a))
        c_norm = 2 * tau[a] * delta(prefix, x / a) / (x ** 0.75)
        old_norm = 2 * tau[a] * delta(prefix, 2 * x / a) / ((2 * x) ** 0.75)
        contract = old_norm - q * c_norm
        rows.append(
            {
                "a": a,
                "tau": tau[a],
                "contract": contract,
                "positive_contract": max(0.0, contract),
                "c_norm": c_norm,
                "old_norm": old_norm,
                "frac_x_over_a": x / a - k1,
                "frac_2x_over_a": 2 * x / a - k2,
                "floor_x_over_a": k1,
                "floor_2x_over_a": k2,
            }
        )
    return rows


def phase_stats(rows: list[dict], threshold: float) -> dict:
    """统计正峰项在高相位区的容量。"""
    positive = [row for row in rows if row["positive_contract"] > 0]
    high_phase = [
        row
        for row in positive
        if row["frac_x_over_a"] >= threshold
        or row["frac_2x_over_a"] >= threshold
    ]
    total_pos = sum(row["positive_contract"] for row in positive)
    high_pos = sum(row["positive_contract"] for row in high_phase)
    return {
        "threshold": threshold,
        "positive_count": len(positive),
        "high_phase_count": len(high_phase),
        "positive_tau_sum": sum(row["tau"] for row in positive),
        "high_phase_tau_sum": sum(row["tau"] for row in high_phase),
        "positive_contract_sum": total_pos,
        "high_phase_contract_sum": high_pos,
        "high_phase_share": high_pos / total_pos if total_pos else 0.0,
        "top_high_phase": sorted(
            high_phase,
            key=lambda row: row["positive_contract"],
            reverse=True,
        )[:20],
    }


def interval_stats(rows: list[dict], bins: int) -> list[dict]:
    """按 {x/a} 相位分箱，查看正峰质量分布。"""
    buckets = []
    for i in range(bins):
        lo = i / bins
        hi = (i + 1) / bins
        selected = [
            row
            for row in rows
            if row["positive_contract"] > 0
            and lo <= row["frac_x_over_a"] < hi
        ]
        buckets.append(
            {
                "lo": lo,
                "hi": hi,
                "count": len(selected),
                "tau_sum": sum(row["tau"] for row in selected),
                "positive_contract_sum": sum(row["positive_contract"] for row in selected),
            }
        )
    return buckets


def offset_stats(x: int, rows: list[dict]) -> list[dict]:
    """按最小正偏移 h 统计 a | x+h 的正峰容量。"""
    grouped: dict[int, dict] = {}
    for row in rows:
        if row["positive_contract"] <= 0:
            continue
        a = row["a"]
        h = (-x) % a
        if h == 0:
            h = a
        item = grouped.setdefault(
            h,
            {
                "offset": h,
                "count": 0,
                "tau_sum": 0,
                "positive_contract_sum": 0.0,
                "kernel_weighted_sum": 0.0,
                "max_kernel": 0.0,
                "a_values": [],
            },
        )
        kernel = row["positive_contract"] / row["tau"] if row["tau"] else 0.0
        item["count"] += 1
        item["tau_sum"] += row["tau"]
        item["positive_contract_sum"] += row["positive_contract"]
        item["kernel_weighted_sum"] += row["tau"] * kernel
        item["max_kernel"] = max(item["max_kernel"], kernel)
        if len(item["a_values"]) < 80:
            item["a_values"].append(a)
    for item in grouped.values():
        item["average_kernel"] = (
            item["positive_contract_sum"] / item["tau_sum"]
            if item["tau_sum"]
            else 0.0
        )
        item["max_kernel_bound"] = item["tau_sum"] * item["max_kernel"]
        item["max_kernel_slack"] = (
            item["max_kernel_bound"] - item["positive_contract_sum"]
        )
    return sorted(
        grouped.values(),
        key=lambda item: item["positive_contract_sum"],
        reverse=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1_028_143)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--thresholds", default="0.5,0.6,0.7,0.8,0.9")
    parser.add_argument("--bins", type=int, default=10)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    tau, prefix = build(2 * args.x + 10)
    rows = term_rows(args.x, args.hi, args.q, tau, prefix)
    thresholds = [float(item) for item in args.thresholds.split(",") if item]
    payload = {
        "x": args.x,
        "hi": args.hi,
        "q": args.q,
        "total_contract": sum(row["contract"] for row in rows),
        "positive_contract_sum": sum(row["positive_contract"] for row in rows),
        "positive_count": sum(1 for row in rows if row["positive_contract"] > 0),
        "positive_tau_sum": sum(row["tau"] for row in rows if row["positive_contract"] > 0),
        "threshold_stats": [phase_stats(rows, threshold) for threshold in thresholds],
        "frac_x_bins": interval_stats(rows, args.bins),
        "offset_stats": offset_stats(args.x, rows)[:50],
        "top_positive": sorted(rows, key=lambda row: row["positive_contract"], reverse=True)[:30],
    }

    print(
        json.dumps(
            {
                "x": payload["x"],
                "total_contract": payload["total_contract"],
                "positive_contract_sum": payload["positive_contract_sum"],
                "positive_count": payload["positive_count"],
                "positive_tau_sum": payload["positive_tau_sum"],
            },
            indent=2,
        )
    )
    for stat in payload["threshold_stats"]:
        print(
            f"thr={stat['threshold']:.2f} count={stat['high_phase_count']} "
            f"tau={stat['high_phase_tau_sum']} share={stat['high_phase_share']:.6f}"
        )
    print("top offsets")
    for item in payload["offset_stats"][:10]:
        print(
            f"h={item['offset']} count={item['count']} tau={item['tau_sum']} "
            f"weight={item['positive_contract_sum']:.12f} "
            f"avgK={item['average_kernel']:.6e} maxK={item['max_kernel']:.6e}"
        )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
