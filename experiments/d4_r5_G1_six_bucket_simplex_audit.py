#!/usr/bin/env python3
"""D4/R5 G1 六桶危险单纯形审计。"""
from __future__ import annotations

import json
from collections import defaultdict
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


def record_for(path: Path, row: dict) -> dict | None:
    items = [item for item in row["all_offsets"] if eligible(item)]
    total = sum(float(item["positive_contract_sum"]) for item in items)
    if total <= 0:
        return None
    masses = []
    counts = []
    bucket_avg = []
    for _, pred in BUCKETS:
        selected = [item for item in items if pred(item["tau_sum"])]
        mass = sum(float(item["positive_contract_sum"]) for item in selected) / total
        count = len(selected)
        masses.append(mass)
        counts.append(count)
        bucket_avg.append(mass / count if count else 0.0)
    cauchy = sum(m * m / n for m, n in zip(masses, counts) if n)
    return {
        "source": str(path.relative_to(ROOT)),
        "x": row["x"],
        "counts": counts,
        "masses": masses,
        "bucket_avg_mass_per_cell": bucket_avg,
        "bucket_cauchy_Q_over_S2": cauchy,
        "margin": cauchy - TARGET,
        "low_mass_tau_le_16": sum(masses[:3]),
        "mid_high_mass_tau_17_59": masses[3] + masses[4],
        "heavy_mass": masses[5],
        "support_count": sum(counts),
    }


def main() -> None:
    records = []
    by_counts = defaultdict(list)
    for path in FILES:
        for row in json.loads(path.read_text(encoding="utf-8"))["rows"]:
            record = record_for(path, row)
            if not record:
                continue
            records.append(record)
            by_counts[tuple(record["counts"])].append(record)

    vector_summaries = []
    for counts, rows in by_counts.items():
        worst = min(rows, key=lambda item: item["bucket_cauchy_Q_over_S2"])
        vector_summaries.append(
            {
                "counts": list(counts),
                "rows": len(rows),
                "worst_x": worst["x"],
                "worst_source": worst["source"],
                "worst_cauchy": worst["bucket_cauchy_Q_over_S2"],
                "worst_margin": worst["margin"],
                "worst_masses": worst["masses"],
                "min_low_mass_tau_le_16": min(item["low_mass_tau_le_16"] for item in rows),
                "max_low_mass_tau_le_16": max(item["low_mass_tau_le_16"] for item in rows),
                "min_mid_high_mass_tau_17_59": min(item["mid_high_mass_tau_17_59"] for item in rows),
                "max_mid_high_mass_tau_17_59": max(item["mid_high_mass_mass_tau_17_59"] if False else item["mid_high_mass_tau_17_59"] for item in rows),
                "min_heavy_mass": min(item["heavy_mass"] for item in rows),
                "max_heavy_mass": max(item["heavy_mass"] for item in rows),
            }
        )
    vector_summaries.sort(key=lambda item: item["worst_margin"])
    dangerous_near = [item for item in vector_summaries if item["worst_margin"] < 0.003]
    worst_records = sorted(records, key=lambda item: item["margin"])[:20]

    # 经验提取：在最危险 20 条里，检查中高桶质量是否有统一下界。
    min_constraints = {
        "top20_min_tau_17_32_mass": min(item["masses"][3] for item in worst_records),
        "top20_min_tau_17_59_mass": min(item["masses"][3] + item["masses"][4] for item in worst_records),
        "top20_min_tau_ge_17_mass": min(item["masses"][3] + item["masses"][4] + item["masses"][5] for item in worst_records),
        "top20_max_tau_le_16_mass": max(item["low_mass_tau_le_16"] for item in worst_records),
        "top20_min_bucket4_avg": min(item["bucket_avg_mass_per_cell"][3] for item in worst_records),
    }

    audit = {
        "certificate_type": "D4_R5_G1_six_bucket_simplex_audit",
        "status": "six_bucket_danger_domain_localized_to_few_count_patterns",
        "target_Q_over_S2": TARGET,
        "rows_seen": len(records),
        "distinct_count_vectors": len(vector_summaries),
        "near_danger_count_vectors_margin_lt_0p003": len(dangerous_near),
        "worst_records": compact(worst_records),
        "nearest_count_vectors": compact(vector_summaries[:20]),
        "top20_empirical_constraints": compact(min_constraints),
        "structural_conclusion": (
            "六桶 Cauchy 的最危险区域集中在少数支撑向量上，而不是全局任意分布。"
            "最危险样本共同表现为 tau_17_32 桶具有显著质量，且每格平均质量明显高于低 tau 桶。"
            "因此下一步证明应转向局部危险向量排除：固定 n 向量后，用 tau_17_32 的最小质量/密度约束把单纯形从目标以下推回目标以上。"
        ),
        "proof_obligations": [
            "对每个近危险 n 向量，写出二次型 F_n(m)=sum m_i^2/n_i-1/64。",
            "从斜线互斥或 tau 层定义证明 tau_17_32 桶质量下界，或证明低三桶质量上界。",
            "优先闭合最坏两个支撑向量：(36,24,15,14,0,1) 与 (40,21,21,11,2,0)。",
        ],
    }
    (DOCS / "d4-r5-G1-six-bucket-simplex-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# D4/R5 G1 六桶危险单纯形审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 概览",
        f"- 行数：`{audit['rows_seen']}`",
        f"- 不同支撑向量：`{audit['distinct_count_vectors']}`",
        f"- margin < 0.003 的近危险支撑向量：`{audit['near_danger_count_vectors_margin_lt_0p003']}`",
        f"- top20 经验约束：{audit['top20_empirical_constraints']}",
        "",
        "## 最近危险支撑向量",
    ]
    for item in audit["nearest_count_vectors"][:10]:
        lines.append(f"- counts={item['counts']}, worst_x={item['worst_x']}, margin={item['worst_margin']}, masses={item['worst_masses']}")
    lines += ["", "## 证明义务"]
    for item in audit["proof_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-six-bucket-simplex-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-six-bucket-simplex-audit.json")
    print(DOCS / "d4-r5-G1-six-bucket-simplex-audit.md")


if __name__ == "__main__":
    main()
