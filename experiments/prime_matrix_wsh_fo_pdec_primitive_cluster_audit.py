#!/usr/bin/env python3
"""审计 FO-PDEC 对偶聚簇中的 primitive event 去重结构。

用法示例：
  python3 experiments/prime_matrix_wsh_fo_pdec_primitive_cluster_audit.py

目的：
  显式阈值账本中的最佳投影 ell=199,h=95 质量为 4。但这些方程可能来自
  嵌套长块或相邻筛层复用的同一个物理候选。该脚本按不同口径去重：

  1. equation：原始多重方程；
  2. block-local：按 (block_index,candidate,factor)；
  3. layer-local：按 (q,candidate,factor)；
  4. physical：按 (candidate,factor)。

注意：这是审稿防误用账本，不是全局闭合证明。
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable


def fourier_for_events(events: list[dict], factor: int, frequency: int) -> dict:
    """按给定事件列表计算 Fourier 值与支撑弧。"""
    counts = Counter(event["target_residue"] for event in events)
    total = 0j
    for residue, count in counts.items():
        total += count * cmath.exp(2j * math.pi * frequency * residue / factor)
    transformed = Counter(
        (frequency * event["target_residue"]) % factor for event in events
    )
    points = sorted(transformed)
    unique_points = sorted(set(points))
    if len(unique_points) <= 1:
        arc_length = 0
        arc_start = unique_points[0] if unique_points else None
        arc_end = unique_points[0] if unique_points else None
    else:
        gaps = []
        for index, point in enumerate(unique_points):
            next_point = unique_points[(index + 1) % len(unique_points)]
            gaps.append(((next_point - point) % factor, point, next_point))
        max_gap, gap_start, gap_end = max(gaps)
        arc_length = factor - max_gap
        arc_start = gap_end
        arc_end = gap_start
    mass = len(events)
    magnitude = abs(total)
    return {
        "mass": mass,
        "support_size": len(counts),
        "max_fourier_at_frequency": magnitude,
        "mass_defect": mass - magnitude,
        "relative_defect": (mass - magnitude) / mass if mass else 0.0,
        "dual_arc_length": arc_length,
        "dual_arc_start": arc_start,
        "dual_arc_end": arc_end,
        "original_residues": [
            {"residue": residue, "load": load} for residue, load in counts.most_common()
        ],
        "dual_residues": [
            {"residue": residue, "load": load}
            for residue, load in transformed.most_common()
        ],
    }


def dedupe(events: list[dict], key_fn: Callable[[dict], tuple]) -> tuple[list[dict], dict]:
    """按键去重，并记录每个 primitive event 的来源。"""
    buckets: defaultdict[tuple, list[dict]] = defaultdict(list)
    for event in events:
        buckets[key_fn(event)].append(event)
    primitive = []
    for key, rows in buckets.items():
        row = dict(rows[0])
        row["primitive_key"] = list(key)
        row["multiplicity"] = len(rows)
        row["sources"] = [
            {
                "block_index": source["block_index"],
                "offset_row_index": source["offset_row_index"],
                "p": source["p"],
                "q": source["q"],
                "source_row": source["source_row"],
            }
            for source in rows
        ]
        primitive.append(row)
    primitive.sort(key=lambda row: tuple(row["primitive_key"]))
    multiplicities = Counter(row["multiplicity"] for row in primitive)
    return primitive, {
        "primitive_count": len(primitive),
        "multiplicity_histogram": [
            {"multiplicity": value, "count": count}
            for value, count in sorted(multiplicities.items())
        ],
        "max_multiplicity": max(multiplicities, default=0),
    }


def build_audit(source: dict, factor: int, frequency: int) -> dict:
    """构造 primitive cluster 审计。"""
    events = [
        equation
        for equation in source["equations"]
        if equation["explaining_factor"] == factor
    ]
    modes = {
        "equation": lambda event: (
            event["offset_row_index"],
            event["candidate"],
            event["explaining_factor"],
        ),
        "block_local": lambda event: (
            event["block_index"],
            event["candidate"],
            event["explaining_factor"],
        ),
        "layer_local": lambda event: (
            event["q"],
            event["candidate"],
            event["explaining_factor"],
        ),
        "physical": lambda event: (
            event["candidate"],
            event["explaining_factor"],
        ),
    }
    mode_rows = []
    for name, key_fn in modes.items():
        primitive, dedupe_summary = dedupe(events, key_fn)
        row = {
            "mode": name,
            **dedupe_summary,
            **fourier_for_events(primitive, factor, frequency),
            "events": primitive,
        }
        mode_rows.append(row)
    return {
        "status": "finite_fo_pdec_primitive_cluster_audit_not_global_proof",
        "parameters": {"factor": factor, "frequency": frequency},
        "summary": {
            "raw_event_count": len(events),
            "modes": [
                {
                    key: row[key]
                    for key in [
                        "mode",
                        "primitive_count",
                        "max_multiplicity",
                        "mass",
                        "support_size",
                        "max_fourier_at_frequency",
                        "mass_defect",
                        "dual_arc_length",
                    ]
                }
                for row in mode_rows
            ],
        },
        "modes": mode_rows,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# FO-PDEC Primitive Cluster 去重审计",
        "",
        "**状态：** `finite_fo_pdec_primitive_cluster_audit_not_global_proof`",
        "",
        "本文档检查最佳投影中的短弧聚簇是否由独立坏窗方程构成，还是由嵌套块/跨层复用导致的多重计数。它防止把非独立重复误当成全局 `PDEC` 质量。",
        "",
        "## 参数",
        "",
        f"- `ell`: `{params['factor']}`。",
        f"- `h`: `{params['frequency']}`。",
        "",
        "## 去重模式摘要",
        "",
        "| mode | primitive | max mult | mass | support | Fourier | mass defect | dual arc |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["summary"]["modes"]:
        lines.append(
            "| {mode} | {primitive} | {mult} | {mass} | {support} | {fourier:.6f} | {defect:.6f} | {arc} |".format(
                mode=row["mode"],
                primitive=row["primitive_count"],
                mult=row["max_multiplicity"],
                mass=row["mass"],
                support=row["support_size"],
                fourier=row["max_fourier_at_frequency"],
                defect=row["mass_defect"],
                arc=row["dual_arc_length"],
            )
        )
    lines.extend(
        [
            "",
            "## 物理事件",
            "",
            "| candidate | factor | residue | dual residue | multiplicity | sources |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    physical = next(row for row in result["modes"] if row["mode"] == "physical")
    factor = params["factor"]
    frequency = params["frequency"]
    for event in physical["events"]:
        dual = (frequency * event["target_residue"]) % factor
        lines.append(
            "| {candidate} | {factor} | {residue} | {dual} | {mult} | {sources} |".format(
                candidate=event["candidate"],
                factor=event["explaining_factor"],
                residue=event["target_residue"],
                dual=dual,
                mult=event["multiplicity"],
                sources=event["sources"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "若正式坏窗集合 `S` 是多重集合并且确实包含嵌套块/跨层复用，那么 equation 模式的阈值可以使用；若正式 `S` 必须按物理候选去重，则阈值应降到 physical 模式。当前最佳聚簇的质量差异正是最后证明义务：必须证明多重计数合法，或改用 primitive 事件并重新给出 `PDEC/SAE` 排斥。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.json",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-wsh-fo-pdec-primitive-cluster-audit",
    )
    parser.add_argument("--factor", type=int, default=199)
    parser.add_argument("--frequency", type=int, default=95)
    args = parser.parse_args()
    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = build_audit(source, args.factor, args.frequency)
    output_prefix = Path(args.out_prefix)
    output_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, output_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
