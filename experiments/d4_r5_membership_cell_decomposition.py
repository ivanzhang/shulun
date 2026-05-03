#!/usr/bin/env python3
"""D4/R5 成员关系签名单元分解。

用法示例：
  python3 experiments/d4_r5_membership_cell_decomposition.py \
    --units "1088472:1088477,1088496:1088499,1088506:1088507,1088551:1088555" \
    --H 80 --hi 400 --q 0.958 --threshold-tau 60 \
    --json docs/d4-r5-H80-membership-cell-decomposition.json

目的：
  对每个整数行计算 light/short/transition 偏移团成员签名，合并连续相同行，
  找出固定成员关系单元。若签名逐行变化，则全局证明需以整数行邻域为最小单元。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import d4_r5_layer_functional_certificate as layer_cert  # noqa: E402
from d4_lowblock_phase_capacity import offset_stats, term_rows  # noqa: E402


def group_signature(items: list[dict]) -> list[tuple[int, tuple[int, ...], int, int]]:
    """偏移团签名：offset、a 集、tau_sum、count。"""
    return sorted(
        (
            item["offset"],
            tuple(sorted(item.get("a_values", []))),
            item["tau_sum"],
            item["count"],
        )
        for item in items
    )


def row_signature(x: int, hi: int, q: float, threshold_tau: int, H: int, tau, prefix) -> dict:
    """计算一行的层成员签名。"""
    rows = term_rows(x, hi, q, tau, prefix)
    offsets = offset_stats(x, rows)
    light, transition, short_chain = layer_cert.classify_offsets(offsets, threshold_tau)
    prefix_light = [item for item in light if item["offset"] <= H]
    tail_light = [item for item in light if item["offset"] > H]
    signatures = {
        "prefix_light": group_signature(prefix_light),
        "tail_light": group_signature(tail_light),
        "light": group_signature(light),
        "transition": group_signature(transition),
        "short_chain": group_signature(short_chain),
    }
    canonical = json.dumps(signatures, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode()).hexdigest()[:16]
    return {
        "x": x,
        "digest": digest,
        "counts": {key: len(value) for key, value in signatures.items()},
        "a_counts": {
            key: sum(len(entry[1]) for entry in value)
            for key, value in signatures.items()
        },
        "signatures": signatures,
    }


def compress_runs(rows: list[dict]) -> list[dict]:
    """合并连续相同 digest。"""
    runs = []
    for row in rows:
        if runs and runs[-1]["digest"] == row["digest"] and runs[-1]["end"] + 1 == row["x"]:
            runs[-1]["end"] = row["x"]
            runs[-1]["length"] += 1
            runs[-1]["xs"].append(row["x"])
        else:
            runs.append(
                {
                    "start": row["x"],
                    "end": row["x"],
                    "length": 1,
                    "digest": row["digest"],
                    "counts": row["counts"],
                    "a_counts": row["a_counts"],
                    "xs": [row["x"]],
                }
            )
    return runs


def parse_units(raw: str) -> list[tuple[int, int]]:
    """解析闭区间单元。"""
    units = []
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        left, right = item.split(":", 1)
        units.append((int(left), int(right)))
    return units


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--units", default="1088472:1088477,1088496:1088499,1088506:1088507,1088551:1088555")
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    units = parse_units(args.units)
    max_end = max(end for _, end in units)
    tau, prefix = layer_cert.build(2 * max_end + 10)
    unit_payloads = []
    all_runs = []
    for unit_id, (start, end) in enumerate(units, 1):
        rows = [row_signature(x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix) for x in range(start, end + 1)]
        runs = compress_runs(rows)
        all_runs.extend({"unit_id": unit_id, **run} for run in runs)
        unit_payloads.append(
            {
                "unit_id": unit_id,
                "x_range": [start, end],
                "row_count": len(rows),
                "run_count": len(runs),
                "max_run_length": max(run["length"] for run in runs),
                "rows_compact": [
                    {"x": row["x"], "digest": row["digest"], "counts": row["counts"], "a_counts": row["a_counts"]}
                    for row in rows
                ],
                "runs": runs,
            }
        )
    payload = {
        "certificate_type": "D4-R5-H80-membership-cell-decomposition",
        "status": "integer-row signature decomposition; exact continuous cell boundaries still need rational neighbor intervals",
        "H": args.H,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "units": unit_payloads,
        "total_rows": sum(unit["row_count"] for unit in unit_payloads),
        "total_runs": len(all_runs),
        "max_run_length": max(run["length"] for run in all_runs),
        "all_rows_unique_membership": all(run["length"] == 1 for run in all_runs),
        "interpretation": "If all rows are unique, fixed-membership root certificates should be attached to row-neighborhood cells rather than larger H80 units.",
    }
    print(json.dumps({k: v for k, v in payload.items() if k != "units"}, ensure_ascii=False, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
