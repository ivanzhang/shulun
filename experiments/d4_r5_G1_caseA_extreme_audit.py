#!/usr/bin/env python3
"""D4/R5 G1 far Case A 极端低 tau 模式审计。"""
from __future__ import annotations

import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-O2-worst-x1023400-all-offsets.json"


def compact(record: dict) -> dict:
    return {key: float(f"{value:.17g}") if isinstance(value, float) else value for key, value in record.items()}


def main() -> None:
    row = json.loads(INPUT.read_text(encoding="utf-8"))["rows"][0]
    items = []
    for item in row["all_offsets"]:
        weight = float(item["positive_contract_sum"])
        if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
            items.append({"weight": weight, "offset": item["offset"], "tau_sum": item["tau_sum"], "count": item["count"], "average_kernel": item["average_kernel"], "a_values": item.get("a_values", [])})
    items.sort(key=lambda item: item["weight"], reverse=True)
    head = items[:20]
    w20 = head[-1]["weight"]
    far = [item for item in items[20:] if item["weight"] < 0.5 * w20]
    low4 = [item for item in far if item["tau_sum"] <= 4]
    midhi = [item for item in far if item["tau_sum"] >= 5]
    all_a = [a for item in low4 for a in item["a_values"]]
    a_buckets = {}
    for label, lo, hi in [("1_100", 1, 100), ("101_150", 101, 150), ("151_200", 151, 200), ("201_250", 201, 250), ("251_300", 251, 300), ("301_350", 301, 350), ("351_400", 351, 400)]:
        a_buckets[label] = sorted(a for a in all_a if lo <= a <= hi)
    head_sum = sum(item["weight"] for item in head)
    audit = {
        "certificate_type": "D4_R5_G1_caseA_extreme_audit",
        "status": "case_A_single_extreme_pattern_extracted",
        "x": row["x"],
        "head_sum": head_sum,
        "w20": w20,
        "far_over_head": sum(item["weight"] for item in far) / head_sum,
        "low4_over_head": sum(item["weight"] for item in low4) / head_sum,
        "midhi_over_head": sum(item["weight"] for item in midhi) / head_sum,
        "low4_count": len(low4),
        "low4_tau_distribution": dict(collections.Counter(item["tau_sum"] for item in low4)),
        "low4_a_count": len(all_a),
        "low4_a_unique": len(set(all_a)),
        "low4_a_min": min(all_a),
        "low4_a_max": max(all_a),
        "low4_a_buckets": a_buckets,
        "low4_rows": low4,
        "structural_conclusion": "Case A 在 step100 全样本中只有 x=1023400 一个极端模式。其 low4 far 尾部由 37 个偏移团、39 个互异 a 值构成，几乎全是 count=1 或 2 的稀疏单 a 团；a 主要位于 101--400 的高区间。当前可走两条路线：有限模式证书覆盖该极端邻域，或证明高 a、低 tau、单 a 团的排序尾质量上界。",
        "proof_options": [
            "有限模式路线：围绕 x=1023400 扩展邻域，证明 low4>=0.20 只能出现于可枚举有限模式，并逐一验证 far<=0.435",
            "解析路线：证明 tau_sum<=4 且 count<=2 的高 a 偏移团在第 21 位后总质量 <=0.23 head20",
            "联动路线：若 low4>=0.20，则 mid8+hi9<=0.21；扫描极端中 mid8+hi9≈0.2079",
        ],
    }
    (DOCS / "d4-r5-G1-caseA-extreme-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 Case A 极端低 tau 模式审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 核心指标",
        f"- x：`{audit['x']}`",
        f"- far/head：`{audit['far_over_head']}`",
        f"- low4/head：`{audit['low4_over_head']}`",
        f"- midhi/head：`{audit['midhi_over_head']}`",
        f"- low4 tau 分布：`{audit['low4_tau_distribution']}`",
        f"- low4 a 唯一数：`{audit['low4_a_unique']}`，范围 `{audit['low4_a_min']}..{audit['low4_a_max']}`",
        "",
        "## a 分桶",
    ]
    for label, values in a_buckets.items():
        lines.append(f"- `{label}`：count={len(values)}, values={values}")
    lines += ["", "## 证明路线"]
    for item in audit["proof_options"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-caseA-extreme-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-caseA-extreme-audit.json")
    print(DOCS / "d4-r5-G1-caseA-extreme-audit.md")


if __name__ == "__main__":
    main()
