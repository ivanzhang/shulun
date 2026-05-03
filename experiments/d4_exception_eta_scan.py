#!/usr/bin/env python3
"""D4 R5 异常层 eta 阈值扫描。

用法：
  python3 experiments/d4_exception_eta_scan.py \
    --input docs/d4-r5-offset-layered-scan-1088200-1088600-step1-T60.json \
    --json docs/d4-r5-exception-eta-scan-1088200-1088600.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def exceptional_items(row: dict) -> list[dict]:
    """从全偏移分层行中提取异常层项；优先使用 all_offsets。"""
    if "all_offsets" in row:
        items = []
        for item in row["all_offsets"]:
            is_heavy = item["tau_sum"] >= 60
            count = item["count"]
            if is_heavy and count > 25:
                continue
            copied = dict(item)
            copied["layer"] = "exceptional_full"
            items.append(copied)
        return items
    items = []
    seen = set()
    for key, layer in [
        ("top_transition", "transition"),
        ("top_short_chain", "short_chain"),
        ("top_offsets", "light_or_top"),
    ]:
        for item in row.get(key, []):
            if key == "top_offsets" and item["tau_sum"] >= 60:
                continue
            ident = (item["offset"], tuple(item.get("a_values", [])))
            if ident in seen:
                continue
            seen.add(ident)
            copied = dict(item)
            copied["layer"] = layer
            items.append(copied)
    return items


def eta_stats(items: list[dict], eta: float) -> dict:
    """计算 eta 大团/小团统计。"""
    big = [item for item in items if item["positive_contract_sum"] > eta]
    small = [item for item in items if item["positive_contract_sum"] <= eta]
    small_l1 = sum(item["positive_contract_sum"] for item in small)
    small_l2 = math.sqrt(sum(item["positive_contract_sum"] ** 2 for item in small))
    total_l1 = small_l1 + sum(item["positive_contract_sum"] for item in big)
    total_l2 = math.sqrt(sum(item["positive_contract_sum"] ** 2 for item in items))
    return {
        "eta": eta,
        "big_count": len(big),
        "big_l1": sum(item["positive_contract_sum"] for item in big),
        "small_l1": small_l1,
        "small_l2": small_l2,
        "small_ratio": small_l1 / small_l2 if small_l2 else 0.0,
        "total_l1": total_l1,
        "total_l2_displayed": total_l2,
        "total_ratio_displayed": total_l1 / total_l2 if total_l2 else 0.0,
        "top_big": sorted(big, key=lambda item: item["positive_contract_sum"], reverse=True)[:10],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--etas", default="0.005,0.0075,0.01,0.015,0.02,0.025,0.03")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    etas = [float(value) for value in args.etas.split(",")]
    rows = []
    for row in data["rows"]:
        items = exceptional_items(row)
        stats = [eta_stats(items, eta) for eta in etas]
        rows.append(
            {
                "x": row["x"],
                "total_contract": row["total_contract"],
                "ordinary_weight": row["ordinary_weight"],
                "exceptional_l2_sqrt": row["exceptional_l2_sqrt"],
                "eta_stats": stats,
            }
        )
    summary = []
    for eta in etas:
        candidates = [(row, next(s for s in row["eta_stats"] if s["eta"] == eta)) for row in rows]
        summary.append(
            {
                "eta": eta,
                "max_big_count": max(stat["big_count"] for _, stat in candidates),
                "max_small_ratio": max(stat["small_ratio"] for _, stat in candidates),
                "max_total_ratio_displayed": max(stat["total_ratio_displayed"] for _, stat in candidates),
                "worst_big_count_x": max(candidates, key=lambda pair: pair[1]["big_count"])[0]["x"],
                "worst_small_ratio_x": max(candidates, key=lambda pair: pair[1]["small_ratio"])[0]["x"],
            }
        )
    payload = {"input": str(args.input), "etas": etas, "summary": summary, "rows": rows}
    print(json.dumps({"input": str(args.input), "summary": summary}, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
