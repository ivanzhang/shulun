#!/usr/bin/env python3
"""审计 G1 容量--缺陷二择中的能量口径。

比较三种局部可计算能量：
1. layer_l2_sum: 各层 l2 直接相加；
2. layer_sqrt_sum: 各层 l2_sqrt 相加；
3. offset_square_sum: 以 top_offsets 的 positive_contract_sum 按偏移团平方求和。

目的不是证明全局结论，而是找出哪个口径与容量支付 Lyapunov 最兼容。
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SCAN_FILES = [
    "d4-r5-offset-heavy-light-scan-1020000-1030000-step500.json",
    "d4-r5-offset-heavy-light-scan-1028000-1028300-step1.json",
    "d4-r5-offset-heavy-light-scan-1049300-1049900-step1-T60.json",
    "d4-r5-offset-heavy-light-scan-1088200-1088600-step1-T60.json",
    "d4-r5-offset-layered-scan-1049300-1049900-step1-T60.json",
    "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60.json",
]

L2_KEYS = [
    "transition_high_tail_l2",
    "transition_low_start_l2",
    "short_chain_l2",
    "light_l2",
]
SQRT_KEYS = [
    "transition_high_tail_l2_sqrt",
    "transition_low_start_l2_sqrt",
    "short_chain_l2_sqrt",
    "light_l2_sqrt",
]


def load_rows(name: str) -> list[dict[str, Any]]:
    with (DOCS / name).open(encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("rows", [])


def metrics(row: dict[str, Any]) -> dict[str, float]:
    L = float(row.get("positive_contract_sum", 0.0) or 0.0)
    layer_l2 = sum(float(row.get(key, 0.0) or 0.0) for key in L2_KEYS)
    layer_sqrt = sum(float(row.get(key, 0.0) or 0.0) for key in SQRT_KEYS)
    offset_square = sum(
        float(item.get("positive_contract_sum", 0.0) or 0.0) ** 2
        for item in row.get("top_offsets", [])
    )
    return {
        "x": row.get("x"),
        "L": L,
        "layer_l2": layer_l2,
        "layer_sqrt_sum": layer_sqrt,
        "offset_square_sum": offset_square,
        "D_layer_l2": layer_l2 - L * L / 20.0,
        "D_layer_sqrt_sum": layer_sqrt - L * L / 20.0,
        "D_offset_square": offset_square - L * L / 20.0,
    }


def compact(record: dict[str, Any]) -> dict[str, Any]:
    return {k: (float(f"{v:.17g}") if isinstance(v, float) else v) for k, v in record.items()}


def summarize(records: list[dict[str, Any]], floor: float) -> dict[str, Any]:
    subset = [r for r in records if r["L"] >= floor]
    if not subset:
        return {"L_floor": floor, "count": 0}
    out = {"L_floor": floor, "count": len(subset)}
    for key in ["D_layer_l2", "D_layer_sqrt_sum", "D_offset_square"]:
        out[f"min_{key}"] = min(r[key] for r in subset)
        out[f"argmin_{key}"] = compact(min(subset, key=lambda r: r[key]))
    out["max_L"] = max(r["L"] for r in subset)
    out["argmax_L"] = compact(max(subset, key=lambda r: r["L"]))
    return compact(out)


def main() -> None:
    file_summaries = []
    all_records: list[dict[str, Any]] = []
    for name in SCAN_FILES:
        rows = load_rows(name)
        records = [metrics(row) | {"source": name} for row in rows]
        all_records.extend(records)
        file_summaries.append(
            {
                "source": name,
                "row_count": len(records),
                "floors": [summarize(records, floor) for floor in [0.35, 0.4, 0.42, 0.45]],
            }
        )

    global_summary = [summarize(all_records, floor) for floor in [0.35, 0.4, 0.42, 0.45]]
    audit = {
        "certificate_type": "D4/R5 G1 Lyapunov energy convention audit",
        "status": "local_multiwindow_audit_only_global_Lyapunov_not_yet_proved",
        "energy_conventions": {
            "layer_l2": "sum of layer *_l2 fields; too weak locally because D_layer_l2 can be negative in high-capacity rows",
            "layer_sqrt_sum": "sum of layer *_l2_sqrt fields; locally gives positive high-capacity defect margin",
            "offset_square_sum": "sum over offset groups of positive_contract_sum^2; also too weak for the current normalization",
        },
        "global_floor_summary": global_summary,
        "file_summaries": file_summaries,
        "recommended_next_definition": {
            "capacity": "L = row positive_contract_sum on the payment convention",
            "energy": "E_* = sum of layer l2_sqrt resources, until a proof identifies the exact invariant Lyapunov energy",
            "defect": "D_* = E_* - L^2/20",
            "local_observation": "For all audited rows with L>=0.45, D_* remains positive with margin recorded above.",
            "warning": "This is not a proof. The next proof obligation is to derive E_* from the same algebraic identity used in stable capacity payment.",
        },
    }
    out = DOCS / "d4-r5-G1-lyapunov-energy-audit.json"
    with out.open("w", encoding="utf-8") as fh:
        json.dump(audit, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(out)
    print(json.dumps(global_summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
