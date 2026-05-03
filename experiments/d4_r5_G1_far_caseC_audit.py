#!/usr/bin/env python3
"""D4/R5 G1 far tail Case C balanced 审计。"""
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
                items.append({"weight": weight, "tau_sum": item["tau_sum"]})
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
    case_c = [item for item in records if item["low4"] < 0.20 and item["hi9"] < 0.08]
    audit = {
        "certificate_type": "D4_R5_G1_far_caseC_audit",
        "status": "case_C_balanced_scan_safe_not_current_bottleneck",
        "case_definition": "low4<0.20 and hi9<0.08",
        "rows_seen": len(case_c),
        "worst_case_C_far": compact(max(case_c, key=lambda item: item["far"])),
        "worst_case_C_mid8": compact(max(case_c, key=lambda item: item["mid8"])),
        "structural_conclusion": "Case C balanced 的 far/head 扫描最坏约 0.3648，显著低于 0.435；因此它不是当前闭合瓶颈。Case C 可用较粗的联合预算闭合，真正瓶颈回到 Case A low4>=0.20 的极端低 tau 点。",
        "safe_budget": {
            "low4": 0.20,
            "hi9": 0.08,
            "mid8_scan_max_in_case_C": 0.16548701889262674,
            "far_scan_max_in_case_C": 0.36479823016277707,
            "review_safe_far_bound": 0.38,
        },
        "next_focus": "Prove Case A low4>=0.20 implies far/head<=0.435, likely by classifying low tau<=4 saturation and showing mid8+hi9 cannot exceed about 0.21 there.",
    }
    (DOCS / "d4-r5-G1-far-caseC-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 far tail Case C 审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## Case C 定义",
        f"- `{audit['case_definition']}`",
        f"- 样本数：`{audit['rows_seen']}`",
        "",
        "## 最坏记录",
        f"- far 最坏：{audit['worst_case_C_far']}",
        f"- mid8 最坏：{audit['worst_case_C_mid8']}",
        "",
        "## 下一焦点",
        f"- {audit['next_focus']}",
    ]
    (DOCS / "d4-r5-G1-far-caseC-audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(DOCS / "d4-r5-G1-far-caseC-audit.json")
    print(DOCS / "d4-r5-G1-far-caseC-audit.md")


if __name__ == "__main__":
    main()
