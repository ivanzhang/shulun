#!/usr/bin/env python3
"""D4 R5 偏移重轻分解区间扫描。

用法示例：
  python3 experiments/d4_offset_heavy_light_scan.py \
    --start 1020000 --end 1030000 --step 100 --hi 400 \
    --json docs/d4-r5-offset-heavy-light-scan-1020000-1030000-step100.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from d4_lowblock_phase_capacity import build, offset_stats, term_rows


def summarize_x(x: int, hi: int, q: float, threshold_tau: int, tau, prefix) -> dict:
    """汇总单个 x 的重轻偏移统计。"""
    rows = term_rows(x, hi, q, tau, prefix)
    offsets = offset_stats(x, rows)
    heavy = [item for item in offsets if item["tau_sum"] >= threshold_tau]
    light = [item for item in offsets if item["tau_sum"] < threshold_tau]
    ordinary = [item for item in heavy if item["count"] > 25]
    transition = [item for item in heavy if 20 < item["count"] <= 25]
    transition_high_tail = [
        item
        for item in transition
        if item["a_values"]
        and sum(1 for a in item["a_values"] if a >= 120) / len(item["a_values"]) >= 0.80
    ]
    transition_low_start = [item for item in transition if item not in transition_high_tail]
    short_chain = [item for item in heavy if item["count"] <= 20]
    exceptional = transition + short_chain + light
    light_l2 = sum(item["positive_contract_sum"] ** 2 for item in light)
    transition_l2 = sum(item["positive_contract_sum"] ** 2 for item in transition)
    transition_high_tail_l2 = sum(item["positive_contract_sum"] ** 2 for item in transition_high_tail)
    transition_low_start_l2 = sum(item["positive_contract_sum"] ** 2 for item in transition_low_start)
    short_chain_l2 = sum(item["positive_contract_sum"] ** 2 for item in short_chain)
    exceptional_l2 = sum(item["positive_contract_sum"] ** 2 for item in exceptional)
    heavy_bad = [item for item in ordinary if item["average_kernel"] > 5e-4]
    return {
        "x": x,
        "total_contract": sum(row["contract"] for row in rows),
        "positive_contract_sum": sum(row["positive_contract"] for row in rows),
        "offset_count": len(offsets),
        "heavy_count": len(heavy),
        "ordinary_count": len(ordinary),
        "transition_count": len(transition),
        "transition_high_tail_count": len(transition_high_tail),
        "transition_low_start_count": len(transition_low_start),
        "short_chain_count": len(short_chain),
        "light_count": len(light),
        "heavy_weight": sum(item["positive_contract_sum"] for item in heavy),
        "ordinary_weight": sum(item["positive_contract_sum"] for item in ordinary),
        "transition_weight": sum(item["positive_contract_sum"] for item in transition),
        "transition_high_tail_weight": sum(item["positive_contract_sum"] for item in transition_high_tail),
        "transition_low_start_weight": sum(item["positive_contract_sum"] for item in transition_low_start),
        "short_chain_weight": sum(item["positive_contract_sum"] for item in short_chain),
        "light_weight": sum(item["positive_contract_sum"] for item in light),
        "max_heavy_average_kernel": max([item["average_kernel"] for item in heavy] or [0.0]),
        "max_ordinary_average_kernel": max([item["average_kernel"] for item in ordinary] or [0.0]),
        "max_transition_average_kernel": max([item["average_kernel"] for item in transition] or [0.0]),
        "max_transition_high_tail_average_kernel": max([item["average_kernel"] for item in transition_high_tail] or [0.0]),
        "max_transition_low_start_average_kernel": max([item["average_kernel"] for item in transition_low_start] or [0.0]),
        "max_short_chain_average_kernel": max([item["average_kernel"] for item in short_chain] or [0.0]),
        "max_light_average_kernel": max([item["average_kernel"] for item in light] or [0.0]),
        "light_l2": light_l2,
        "light_l2_sqrt": math.sqrt(light_l2),
        "transition_l2": transition_l2,
        "transition_l2_sqrt": math.sqrt(transition_l2),
        "transition_high_tail_l2": transition_high_tail_l2,
        "transition_high_tail_l2_sqrt": math.sqrt(transition_high_tail_l2),
        "transition_low_start_l2": transition_low_start_l2,
        "transition_low_start_l2_sqrt": math.sqrt(transition_low_start_l2),
        "short_chain_l2": short_chain_l2,
        "short_chain_l2_sqrt": math.sqrt(short_chain_l2),
        "exceptional_l2": exceptional_l2,
        "exceptional_l2_sqrt": math.sqrt(exceptional_l2),
        "heavy_bad_count": len(heavy_bad),
        "top_offsets": offsets[:10],
        "top_heavy_bad": sorted(
            heavy_bad,
            key=lambda item: item["average_kernel"],
            reverse=True,
        )[:10],
        "top_ordinary": sorted(
            ordinary, key=lambda item: item["positive_contract_sum"], reverse=True
        )[:10],
        "top_short_chain": sorted(
            short_chain, key=lambda item: item["average_kernel"], reverse=True
        )[:10],
        "top_transition": sorted(
            transition, key=lambda item: item["average_kernel"], reverse=True
        )[:10],
        "top_transition_high_tail": sorted(
            transition_high_tail, key=lambda item: item["positive_contract_sum"], reverse=True
        )[:10],
        "top_transition_low_start": sorted(
            transition_low_start, key=lambda item: item["average_kernel"], reverse=True
        )[:10],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=1_020_000)
    parser.add_argument("--end", type=int, default=1_030_000)
    parser.add_argument("--step", type=int, default=100)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=50)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--quiet", action="store_true", help="只输出最终摘要")
    parser.add_argument("--store-all-offsets", action="store_true", help="在每行保存全部偏移统计，文件会较大")
    args = parser.parse_args()

    tau, prefix = build(2 * args.end + 10)
    rows = []
    for x in range(args.start, args.end, args.step):
        row = summarize_x(x, args.hi, args.q, args.threshold_tau, tau, prefix)
        if args.store_all_offsets:
            term_data = term_rows(x, args.hi, args.q, tau, prefix)
            row["all_offsets"] = offset_stats(x, term_data)
        rows.append(row)
        if not args.quiet:
            print(
                f"x={x} total={row['total_contract']:.6f} "
                f"maxHeavyAvg={row['max_heavy_average_kernel']:.6e} "
                f"lightL2={row['light_l2_sqrt']:.6f} bad={row['heavy_bad_count']}"
            )

    payload = {
        "start": args.start,
        "end": args.end,
        "step": args.step,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "max_total_contract": max(row["total_contract"] for row in rows),
        "max_positive_contract_sum": max(row["positive_contract_sum"] for row in rows),
        "max_heavy_average_kernel": max(row["max_heavy_average_kernel"] for row in rows),
        "max_ordinary_average_kernel": max(row["max_ordinary_average_kernel"] for row in rows),
        "max_transition_average_kernel": max(row["max_transition_average_kernel"] for row in rows),
        "max_transition_high_tail_average_kernel": max(row["max_transition_high_tail_average_kernel"] for row in rows),
        "max_transition_low_start_average_kernel": max(row["max_transition_low_start_average_kernel"] for row in rows),
        "max_short_chain_average_kernel": max(row["max_short_chain_average_kernel"] for row in rows),
        "max_light_l2_sqrt": max(row["light_l2_sqrt"] for row in rows),
        "max_transition_l2_sqrt": max(row["transition_l2_sqrt"] for row in rows),
        "max_transition_high_tail_l2_sqrt": max(row["transition_high_tail_l2_sqrt"] for row in rows),
        "max_transition_low_start_l2_sqrt": max(row["transition_low_start_l2_sqrt"] for row in rows),
        "max_short_chain_l2_sqrt": max(row["short_chain_l2_sqrt"] for row in rows),
        "max_exceptional_l2_sqrt": max(row["exceptional_l2_sqrt"] for row in rows),
        "max_heavy_bad_count": max(row["heavy_bad_count"] for row in rows),
        "worst_total_row": max(rows, key=lambda row: row["total_contract"]),
        "worst_heavy_average_row": max(rows, key=lambda row: row["max_heavy_average_kernel"]),
        "worst_ordinary_average_row": max(rows, key=lambda row: row["max_ordinary_average_kernel"]),
        "worst_exceptional_l2_row": max(rows, key=lambda row: row["exceptional_l2_sqrt"]),
        "worst_short_chain_l2_row": max(rows, key=lambda row: row["short_chain_l2_sqrt"]),
        "worst_transition_l2_row": max(rows, key=lambda row: row["transition_l2_sqrt"]),
        "worst_transition_high_tail_l2_row": max(rows, key=lambda row: row["transition_high_tail_l2_sqrt"]),
        "worst_transition_low_start_l2_row": max(rows, key=lambda row: row["transition_low_start_l2_sqrt"]),
        "worst_light_l2_row": max(rows, key=lambda row: row["light_l2_sqrt"]),
        "rows": rows,
    }
    print(
        "SUMMARY "
        f"max_total={payload['max_total_contract']:.6f} "
        f"max_ord_avg={payload['max_ordinary_average_kernel']:.6e} "
        f"max_exc_l2={payload['max_exceptional_l2_sqrt']:.6f}"
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
