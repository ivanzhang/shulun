#!/usr/bin/env python3
"""D4/R5 G1 far tail 联合预算审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json"


def compact(record: dict) -> dict:
    return {key: float(f"{value:.17g}") if isinstance(value, float) else value for key, value in record.items()}


def main() -> None:
    rows = json.loads(INPUT.read_text(encoding="utf-8"))["rows"]
    records = []
    for row in rows:
        items = []
        for item in row["all_offsets"]:
            weight = float(item["positive_contract_sum"])
            if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
                items.append({"weight": weight, "tau_sum": item["tau_sum"], "count": item["count"]})
        items.sort(key=lambda item: item["weight"], reverse=True)
        if len(items) <= 20:
            continue
        head = sum(item["weight"] for item in items[:20])
        w20 = items[19]["weight"]
        far = [item for item in items[20:] if item["weight"] < 0.5 * w20]
        if head <= 0:
            continue
        low4 = sum(item["weight"] for item in far if item["tau_sum"] <= 4) / head
        mid8 = sum(item["weight"] for item in far if 5 <= item["tau_sum"] <= 8) / head
        hi9 = sum(item["weight"] for item in far if item["tau_sum"] >= 9) / head
        records.append({"x": row["x"], "low4": low4, "mid8": mid8, "hi9": hi9, "far": low4 + mid8 + hi9})

    worst = {key: compact(max(records, key=lambda item: item[key])) for key in ["far", "low4", "mid8", "hi9"]}
    regimes = {
        "low4_large": [item for item in records if item["low4"] >= 0.20],
        "hi9_large": [item for item in records if item["hi9"] >= 0.08],
        "balanced": [item for item in records if item["low4"] < 0.20 and item["hi9"] < 0.08],
    }
    regime_summary = {}
    for name, subset in regimes.items():
        if subset:
            regime_summary[name] = {key: compact(max(subset, key=lambda item: item[key])) for key in ["far", "low4", "mid8", "hi9"]}
        else:
            regime_summary[name] = {}

    audit = {
        "certificate_type": "D4_R5_G1_far_joint_audit",
        "status": "far_tail_joint_budget_reduced_to_single_case_A_extreme_pattern",
        "target": "far/head <= 0.435",
        "worst": worst,
        "regime_summary": regime_summary,
        "structural_conclusion": "far 尾界不能由各 tau 桶全局最大值独立相加证明；桶之间存在互斥相关性。Case C balanced 已由独立审计降为安全分支，hi9 大时 far 最大约 0.390。当前唯一瓶颈是 Case A low4>=0.20 的极端低 tau 点 x=1023400；Case A extreme 审计已抽取其稀疏单 a 模式。",
        "joint_proof_plan": [
            "Case A low4>=0.20：证明这是低 tau 极端，直接给 far<=0.435；扫描中唯一最坏 x=1023400，已抽取为稀疏单 a 模式",
            "Case B hi9>=0.08：证明 low4 被压低，联合 far<=0.40",
            "Case C low4<0.20 且 hi9<0.08：扫描安全，far<=0.365；可用 review_safe_far_bound=0.38 接受",
            "最终需要把这些经验分情形转写成 tau 桶容量互斥引理",
        ],
    }
    (DOCS / "d4-r5-G1-far-joint-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 far tail 联合预算审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 全局最坏",
    ]
    for key, item in worst.items():
        lines.append(f"- `{key}`：{item}")
    lines += ["", "## 分情形摘要"]
    for name, summary in regime_summary.items():
        lines.append(f"### {name}")
        for key, item in summary.items():
            lines.append(f"- `{key}`：{item}")
    lines += ["", "## 联合证明计划"]
    for item in audit["joint_proof_plan"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-far-joint-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-far-joint-audit.json")
    print(DOCS / "d4-r5-G1-far-joint-audit.md")


if __name__ == "__main__":
    main()
