#!/usr/bin/env python3
"""D4/R5 G1 六桶质量阈值反解审计。"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-G1-six-bucket-simplex-audit.json"
TARGET = 1 / 64


def compact(value):
    if isinstance(value, float):
        return float(f"{value:.17g}")
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def min_energy_with_group_mass(counts: list[int], group: list[int], group_mass: float) -> float:
    """固定一组桶总质量下界时的最小六桶 Cauchy。"""
    other = [idx for idx in range(len(counts)) if idx not in group]
    group_den = sum(counts[idx] for idx in group)
    other_den = sum(counts[idx] for idx in other)
    value = 0.0
    if group_den:
        value += group_mass * group_mass / group_den
    if other_den:
        value += (1 - group_mass) * (1 - group_mass) / other_den
    return value


def threshold_for_group(counts: list[int], group: list[int]) -> float | None:
    """反解最小组质量，使粗并 Cauchy 达到目标。"""
    group_den = sum(counts[idx] for idx in group)
    other_den = sum(counts[idx] for idx in range(len(counts)) if idx not in group)
    if group_den <= 0:
        return None
    if other_den <= 0:
        return math.sqrt(TARGET * group_den)
    a = 1 / group_den + 1 / other_den
    b = -2 / other_den
    c = 1 / other_den - TARGET
    disc = b * b - 4 * a * c
    if disc < 0:
        return 0.0
    roots = sorted([(-b - math.sqrt(disc)) / (2 * a), (-b + math.sqrt(disc)) / (2 * a)])
    candidates = [root for root in roots if 0 <= root <= 1]
    if not candidates:
        return 0.0 if min_energy_with_group_mass(counts, group, 0.0) >= TARGET else 1.0
    # 当组为高桶时，需要超过较大根；当组为中间桶时也取达到目标的右侧门槛。
    return candidates[-1]


def main() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    groups = {
        "tau_17_32": [3],
        "tau_17_59": [3, 4],
        "tau_ge_17": [3, 4, 5],
        "tau_9_32": [2, 3],
        "tau_9_59": [2, 3, 4],
    }
    rows = []
    for item in data["nearest_count_vectors"][:20]:
        counts = item["counts"]
        masses = item["worst_masses"]
        row = {
            "counts": counts,
            "worst_x": item["worst_x"],
            "actual_margin": item["worst_margin"],
            "actual_masses": masses,
            "groups": {},
        }
        for name, idxs in groups.items():
            actual = sum(masses[idx] for idx in idxs)
            threshold = threshold_for_group(counts, idxs)
            row["groups"][name] = {
                "actual_mass": actual,
                "required_mass_by_two_block_relaxation": threshold,
                "margin": None if threshold is None else actual - threshold,
            }
        rows.append(row)
    best_group_summary = {}
    for name in groups:
        margins = [row["groups"][name]["margin"] for row in rows if row["groups"][name]["margin"] is not None]
        best_group_summary[name] = {
            "min_margin_top20_vectors": min(margins),
            "max_required_top20_vectors": max(row["groups"][name]["required_mass_by_two_block_relaxation"] or 0 for row in rows),
            "min_actual_top20_vectors": min(row["groups"][name]["actual_mass"] for row in rows),
        }
    audit = {
        "certificate_type": "D4_R5_G1_bucket_mass_threshold_audit",
        "status": "tau_9_59_or_tau_ge17_mass_thresholds_are_plausible_but_need_structural_proof",
        "target_Q_over_S2": TARGET,
        "group_summary": compact(best_group_summary),
        "top20_threshold_rows": compact(rows),
        "structural_conclusion": (
            "对近危险支撑向量反解可见，单独 tau_17_32 质量下界通常过强；"
            "tau>=17 或 tau=9..59 的合并质量阈值更自然。"
            "但二块反解只是充分条件，正式证明仍应回到六桶二次型；"
            "最有希望的定理化约束是：低 tau 支撑接近饱和时，中高 tau 总质量存在强制下界。"
        ),
        "proof_obligations": [
            "证明低三桶支撑数大时，tau>=17 或 tau=9..59 的质量不能低于反解门槛。",
            "把该质量下界代入六桶二次型，而非二块粗并，以保留额外余量。",
            "若统一质量下界太强，则按近危险 n 向量分族证明局部阈值。",
        ],
    }
    (DOCS / "d4-r5-G1-bucket-mass-threshold-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# D4/R5 G1 桶质量阈值反解审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 组质量阈值摘要",
    ]
    for name, summary in audit["group_summary"].items():
        lines.append(f"- `{name}`：{summary}")
    lines += ["", "## 证明义务"]
    for item in audit["proof_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-bucket-mass-threshold-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-bucket-mass-threshold-audit.json")
    print(DOCS / "d4-r5-G1-bucket-mass-threshold-audit.md")


if __name__ == "__main__":
    main()
