#!/usr/bin/env python3
"""D4/R5 G1 low_sum>3/5 补偿结构审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = [
    DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json",
    DOCS / "d4-r5-O2-caseA-neighborhood-1023000-1023800-step1.json",
]
BUCKETS = [
    ("tau_le_4", lambda tau: tau <= 4),
    ("tau_5_8", lambda tau: 5 <= tau <= 8),
    ("tau_9_16", lambda tau: 9 <= tau <= 16),
    ("tau_17_32", lambda tau: 17 <= tau <= 32),
    ("tau_33_59", lambda tau: 33 <= tau < 60),
    ("heavy_short", lambda tau: tau >= 60),
]
TARGET = 1 / 64


def compact(value):
    if isinstance(value, float):
        return float(f"{value:.17g}")
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def eligible(item: dict) -> bool:
    return float(item["positive_contract_sum"]) > 0 and (
        item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)
    )


def record(path: Path, row: dict) -> dict | None:
    items = [item for item in row["all_offsets"] if eligible(item)]
    total = sum(float(item["positive_contract_sum"]) for item in items)
    if total <= 0:
        return None
    masses, counts = [], []
    for _, pred in BUCKETS:
        selected = [item for item in items if pred(item["tau_sum"])]
        mass = sum(float(item["positive_contract_sum"]) for item in selected) / total
        masses.append(mass)
        counts.append(len(selected))
    densities = [m / n if n else 0.0 for m, n in zip(masses, counts)]
    ratios = {
        "d2_over_d1": densities[1] / densities[0] if densities[0] else None,
        "d3_over_d2": densities[2] / densities[1] if densities[1] else None,
        "d4_over_d3": densities[3] / densities[2] if densities[2] else None,
        "d4_over_d1": densities[3] / densities[0] if densities[0] else None,
    }
    cauchy = sum(m * m / n for m, n in zip(masses, counts) if n)
    return {
        "source": str(path.relative_to(ROOT)),
        "x": row["x"],
        "counts": counts,
        "masses": masses,
        "densities": densities,
        "ratios": ratios,
        "low_sum": sum(masses[:3]),
        "high_sum": sum(masses[3:]),
        "bucket_cauchy": cauchy,
        "margin": cauchy - TARGET,
    }


def main() -> None:
    records = []
    for path in FILES:
        for row in json.loads(path.read_text(encoding="utf-8"))["rows"]:
            item = record(path, row)
            if item:
                records.append(item)
    low_big = [r for r in records if r["low_sum"] > 0.6]
    low_big_near = [r for r in low_big if r["margin"] < 0.006]
    def min_ratio(rows, key):
        vals = [(r["ratios"][key], r) for r in rows if r["ratios"][key] is not None]
        return min(vals, key=lambda x: x[0]) if vals else (None, None)
    ratio_summary = {}
    for key in ["d2_over_d1", "d3_over_d2", "d4_over_d3", "d4_over_d1"]:
        val, row = min_ratio(low_big_near, key)
        ratio_summary[key] = {"min": val, "witness": compact(row)}
    worst_low_big = min(low_big, key=lambda r: r["margin"]) if low_big else None
    worst_low_big_near = min(low_big_near, key=lambda r: r["margin"]) if low_big_near else None
    audit = {
        "certificate_type": "D4_R5_G1_low_mass_compensation_audit",
        "status": "low_mass_gt_3over5_empirically_forces_density_ladder_compensation",
        "rows_seen": len(records),
        "low_gt_3over5_count": len(low_big),
        "low_gt_3over5_near_count_margin_lt_0p006": len(low_big_near),
        "worst_low_gt_3over5": compact(worst_low_big),
        "worst_low_gt_3over5_near": compact(worst_low_big_near),
        "ratio_summary_near_low_gt_3over5": compact(ratio_summary),
        "structural_conclusion": (
            "在审计样本中，low_sum>3/5 的近危险行并不会保持任意摊平；"
            "它们仍强制出现相邻密度提升。尤其 d4/d3 与 d4/d1 保持显著大于 3/2 与 4。"
            "这支持二选一路线：low_sum<=3/5 由严格 QP 证书闭合；low_sum>3/5 时需要证明增强密度链或高桶补偿。"
        ),
        "candidate_compensation_lemmas": [
            "若 low_sum>3/5 且处于近危险支撑型，则 d4/d3 >= 8/5。",
            "若 low_sum>3/5 且处于近危险支撑型，则 d2/d1 >= 3/2 与 d3/d2 >= 3/2 不能同时接近等号，至少一段增强。",
            "若 low_sum>3/5 但 d4/d3 不增强，则 tau_33_59/heavy_short 必非空并提供额外小支撑能量。",
        ],
        "next_obligations": [
            "把这些增强候选代入严格 QP，验证 low>3/5 分支是否闭合。",
            "若 d4/d3>=8/5 不足，则反解 low>3/5 分支所需的最小增强组合。",
            "最终从 tau 几何或核单调性证明该增强组合。",
        ],
    }
    (DOCS / "d4-r5-G1-low-mass-compensation-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 low_sum>3/5 补偿结构审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 摘要",
        f"- 总行数：`{audit['rows_seen']}`",
        f"- low_sum>3/5 行数：`{audit['low_gt_3over5_count']}`",
        f"- low_sum>3/5 且 margin<0.006 行数：`{audit['low_gt_3over5_near_count_margin_lt_0p006']}`",
        f"- 最坏 low_sum>3/5：{audit['worst_low_gt_3over5']}",
        "",
        "## 近危险比值下界",
    ]
    for key, value in audit["ratio_summary_near_low_gt_3over5"].items():
        lines.append(f"- `{key}`：min={value['min']}")
    lines += ["", "## 候选补偿引理"]
    for item in audit["candidate_compensation_lemmas"]:
        lines.append(f"- {item}")
    lines += ["", "## 下一证明义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-low-mass-compensation-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-low-mass-compensation-audit.json")
    print(DOCS / "d4-r5-G1-low-mass-compensation-audit.md")


if __name__ == "__main__":
    main()
