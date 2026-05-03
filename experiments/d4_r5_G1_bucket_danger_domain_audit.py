#!/usr/bin/env python3
"""D4/R5 G1 联合桶 Cauchy 危险域审计。"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = [
    DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json",
    DOCS / "d4-r5-O2-caseA-neighborhood-1023000-1023800-step1.json",
]
TARGET = 1 / 64
BUCKETS = [
    ("tau_le_4", lambda tau: tau <= 4),
    ("tau_5_8", lambda tau: 5 <= tau <= 8),
    ("tau_9_16", lambda tau: 9 <= tau <= 16),
    ("tau_17_32", lambda tau: 17 <= tau <= 32),
    ("tau_33_59", lambda tau: 33 <= tau < 60),
    ("heavy_short", lambda tau: tau >= 60),
]
LOW = ("tau_le_4", "tau_5_8", "tau_9_16")
HIGH = ("tau_17_32", "tau_33_59", "heavy_short")


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


def required_high_mass(low_count: int, high_count: int) -> float | None:
    if low_count <= 0:
        return 0.0
    if high_count <= 0:
        return None
    # 解 (1-h)^2/low_count + h^2/high_count = 1/64。
    a = 1 / low_count + 1 / high_count
    b = -2 / low_count
    c = 1 / low_count - TARGET
    disc = b * b - 4 * a * c
    if disc < 0:
        return 0.0
    roots = [(-b - math.sqrt(disc)) / (2 * a), (-b + math.sqrt(disc)) / (2 * a)]
    feasible = [root for root in roots if 0 <= root <= 1]
    if not feasible:
        return 0.0 if (1 / low_count) >= TARGET else 1.0
    return max(feasible)


def main() -> None:
    records = []
    for path in FILES:
        for row in json.loads(path.read_text(encoding="utf-8"))["rows"]:
            items = [item for item in row["all_offsets"] if eligible(item)]
            total = sum(float(item["positive_contract_sum"]) for item in items)
            if total <= 0:
                continue
            masses = {}
            counts = {}
            for name, pred in BUCKETS:
                selected = [item for item in items if pred(item["tau_sum"])]
                masses[name] = sum(float(item["positive_contract_sum"]) for item in selected) / total
                counts[name] = len(selected)
            low_mass = sum(masses[name] for name in LOW)
            high_mass = sum(masses[name] for name in HIGH)
            low_count = sum(counts[name] for name in LOW)
            high_count = sum(counts[name] for name in HIGH)
            cauchy_2block = 0.0
            if low_count:
                cauchy_2block += low_mass * low_mass / low_count
            if high_count:
                cauchy_2block += high_mass * high_mass / high_count
            req = required_high_mass(low_count, high_count)
            records.append(
                {
                    "source": str(path.relative_to(ROOT)),
                    "x": row["x"],
                    "low_mass_tau_le_16": low_mass,
                    "high_mass_tau_ge_17": high_mass,
                    "low_count_tau_le_16": low_count,
                    "high_count_tau_ge_17": high_count,
                    "required_high_mass_for_2block_target": req,
                    "high_mass_margin": None if req is None else high_mass - req,
                    "two_block_cauchy": cauchy_2block,
                }
            )
    worst_margin = min(
        [record for record in records if record["high_mass_margin"] is not None],
        key=lambda record: record["high_mass_margin"],
    )
    worst_2block = min(records, key=lambda record: record["two_block_cauchy"])
    violations = [record for record in records if record["two_block_cauchy"] < TARGET]
    audit = {
        "certificate_type": "D4_R5_G1_bucket_danger_domain_audit",
        "status": "two_block_coarsening_insufficient_need_three_or_six_bucket_constraints",
        "target_Q_over_S2": TARGET,
        "rows_seen": len(records),
        "two_block_violations": len(violations),
        "worst_high_mass_margin": compact(worst_margin),
        "worst_two_block_cauchy": compact(worst_2block),
        "structural_conclusion": (
            "把六个 tau 桶粗并为 low=tau<=16 与 high=tau>=17 后，"
            "Cauchy 下界会丢失过多结构，样本中已有二块下界低于 1/64 的记录。"
            "因此正式证明不能只用一个高 tau 总质量条件；必须保留三到六桶的层叠约束，"
            "尤其是 tau_17_32 与 tau_33_59/heavy_short 的小支撑高质量效应。"
        ),
        "next_proof_target": [
            "保留六桶 Cauchy 形式 sum_i m_i^2/n_i，而不是二块粗并。",
            "证明每个 n 向量对应的危险单纯形与 tau 几何质量约束不相交。",
            "优先提取可证的相邻桶迁移约束：若低桶支撑数大，则中高桶质量下界同步抬升。",
        ],
    }
    (DOCS / "d4-r5-G1-bucket-danger-domain-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# D4/R5 G1 桶危险域审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 二块粗并测试",
        f"- 行数：`{audit['rows_seen']}`",
        f"- 二块下界违例：`{audit['two_block_violations']}`",
        f"- 最小高质量余量：{audit['worst_high_mass_margin']}",
        f"- 最坏二块 Cauchy：{audit['worst_two_block_cauchy']}",
        "",
        "## 下一证明目标",
    ]
    for item in audit["next_proof_target"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-bucket-danger-domain-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-bucket-danger-domain-audit.json")
    print(DOCS / "d4-r5-G1-bucket-danger-domain-audit.md")


if __name__ == "__main__":
    main()
