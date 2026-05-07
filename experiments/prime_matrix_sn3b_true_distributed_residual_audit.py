#!/usr/bin/env python3
"""审计 SN3-B 真分散残余质量。

用法示例：
  python3 experiments/prime_matrix_sn3b_true_distributed_residual_audit.py \
    --input docs/sn3_distributed_band_projection_audit_20260506.json \
    --out-prefix docs/sn3b_true_distributed_residual_audit_20260506

目标：
  在 SN3-A 已把中心化低模峰剥离为 PDEC/ColumnCRT 后，
  重新计算仍需 TrueDistributedDLS/KLS 吸收的未解释正质量。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def flatten_candidates(data: dict) -> list[dict]:
    """提取全部 SN-3 候选。"""
    return [item for record in data["records"] for item in record["candidates"]]


def residual_mass(candidate: dict) -> tuple[str, float]:
    """返回 SN3-A 后该候选仍未解释的正质量。"""
    route = candidate["sn3_centered_route"]
    excess = float(candidate["projection"]["excess"])
    if route["route"] == "true_distributed_dls_candidate":
        return "true_distributed", excess
    peak_mass = float(route["peak_share"]) * excess
    return "lowmod_residual", max(0.0, excess - peak_mass)


def build_report(data: dict) -> dict:
    """构造 SN3-B 残余报告。"""
    candidates = flatten_candidates(data)
    original_total = sum(float(item["projection"]["excess"]) for item in candidates)
    rows = defaultdict(
        lambda: {
            "p": None,
            "y": None,
            "required_tail_excess": None,
            "effective_unresolved": 0.0,
            "true_distributed_mass": 0.0,
            "lowmod_residual_mass": 0.0,
            "true_count": 0,
            "lowmod_residual_count": 0,
            "max_low_projection_peak": 0.0,
        }
    )
    route_counts = Counter()
    candidate_rows = []

    for item in candidates:
        kind, mass = residual_mass(item)
        route_counts[kind] += 1
        key = (item["p"], item["y"])
        row = rows[key]
        row["p"] = item["p"]
        row["y"] = item["y"]
        row["required_tail_excess"] = item["required_tail_excess"]
        row["effective_unresolved"] += mass
        row["max_low_projection_peak"] = max(
            row["max_low_projection_peak"],
            item["projection"]["max_centered_projection_peak_share"],
        )
        if kind == "true_distributed":
            row["true_distributed_mass"] += mass
            row["true_count"] += 1
        else:
            row["lowmod_residual_mass"] += mass
            row["lowmod_residual_count"] += 1
        candidate_rows.append(
            {
                "p": item["p"],
                "y": item["y"],
                "band": item["band"],
                "source_route": item["sn3_centered_route"]["route"],
                "effective_unresolved": mass,
                "original_excess": item["projection"]["excess"],
                "unresolved_over_required": (
                    mass / item["required_tail_excess"]
                    if item["required_tail_excess"] > 0
                    else 0.0
                ),
                "low_projection_peak": item["projection"][
                    "max_centered_projection_peak_share"
                ],
            }
        )

    row_list = []
    for row in rows.values():
        required = row["required_tail_excess"]
        row["effective_unresolved_over_required"] = (
            row["effective_unresolved"] / required if required > 0 else 0.0
        )
        row_list.append(dict(row))

    effective_total = sum(row["effective_unresolved"] for row in row_list)
    return {
        "source_parameters": data["parameters"],
        "summary": {
            "original_distributed_excess": original_total,
            "effective_unresolved_after_sn3a": effective_total,
            "removed_by_sn3a": original_total - effective_total,
            "removed_share": (
                (original_total - effective_total) / original_total
                if original_total > 0
                else 0.0
            ),
            "route_counts": dict(route_counts),
            "max_row_effective_unresolved_over_required": max(
                (row["effective_unresolved_over_required"] for row in row_list),
                default=0.0,
            ),
            "max_candidate_unresolved_over_required": max(
                (row["unresolved_over_required"] for row in candidate_rows),
                default=0.0,
            ),
            "max_true_low_projection_peak": max(
                (
                    row["low_projection_peak"]
                    for row in candidate_rows
                    if row["source_route"] == "true_distributed_dls_candidate"
                ),
                default=0.0,
            ),
        },
        "rows": sorted(
            row_list,
            key=lambda row: -row["effective_unresolved_over_required"],
        ),
        "candidates": sorted(
            candidate_rows,
            key=lambda row: -row["unresolved_over_required"],
        ),
    }


def write_markdown(report: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = report["summary"]
    params = report["source_parameters"]
    lines = [
        "# SN3-B 真分散残余审计",
        "",
        "**状态：** `sn3b_true_distributed_residual_audit_not_a_proof`",
        "",
        "## 来源",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `w_list`: `{params['w_list']}`",
        f"- `centered_return_share`: `{params['centered_return_share']}`",
        "",
        "## 摘要",
        "",
        f"- `original_distributed_excess`: `{summary['original_distributed_excess']:.6f}`",
        f"- `effective_unresolved_after_sn3a`: `{summary['effective_unresolved_after_sn3a']:.6f}`",
        f"- `removed_by_sn3a`: `{summary['removed_by_sn3a']:.6f}`",
        f"- `removed_share`: `{summary['removed_share']:.6f}`",
        f"- `route_counts`: `{summary['route_counts']}`",
        f"- `max_row_effective_unresolved_over_required`: `{summary['max_row_effective_unresolved_over_required']:.6f}`",
        f"- `max_candidate_unresolved_over_required`: `{summary['max_candidate_unresolved_over_required']:.6f}`",
        f"- `max_true_low_projection_peak`: `{summary['max_true_low_projection_peak']:.6f}`",
        "",
        "## 最紧行",
        "",
        "| P | y | effective/R | effective E | true E | lowmod residual | true count | residual count | max low peak |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["rows"][:16]:
        lines.append(
            f"| {row['p']} | {row['y']} | "
            f"{row['effective_unresolved_over_required']:.6f} | "
            f"{row['effective_unresolved']:.6f} | "
            f"{row['true_distributed_mass']:.6f} | "
            f"{row['lowmod_residual_mass']:.6f} | "
            f"{row['true_count']} | {row['lowmod_residual_count']} | "
            f"{row['max_low_projection_peak']:.6f} |"
        )

    lines.extend(
        [
            "",
            "## 解释",
            "",
            "该报告把 SN3-A 低模峰剥离后的正残余，与原本低维峰全小的 `TrueDistributedDLS` 候选合并。`effective/R` 是下一步高频 DLS/KLS 需要吸收的真实行级责任比例。",
            "",
            "这些数据不是证明；它们把 SN3-B 的证明目标定位为：对所有低维中心化峰低于阈值的残余质量，给出统一高频分散吸收，或由对偶失败返回新的命名出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/sn3_distributed_band_projection_audit_20260506.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/sn3b_true_distributed_residual_audit_20260506",
    )
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = build_report(data)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, prefix.with_suffix(".md"))
    print(json.dumps(report["summary"], ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
