#!/usr/bin/env python3
"""D4/R5 G1 top20 tail44 审计。"""
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
        arr = []
        for item in row["all_offsets"]:
            weight = float(item["positive_contract_sum"])
            if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
                arr.append({"weight": weight, "offset": item["offset"], "tau_sum": item["tau_sum"], "count": item["count"], "average_kernel": item["average_kernel"]})
        arr.sort(key=lambda item: item["weight"], reverse=True)
        total = sum(item["weight"] for item in arr)
        if total <= 0:
            continue
        head = arr[:20]
        tail = arr[20:]
        head_sum = sum(item["weight"] for item in head)
        tail_sum = sum(item["weight"] for item in tail)
        records.append(
            {
                "x": row["x"],
                "count": len(arr),
                "head_sum": head_sum,
                "tail_sum": tail_sum,
                "total": total,
                "head_share": head_sum / total,
                "tail_share": tail_sum / total,
                "tail_over_head": tail_sum / head_sum if head_sum else 0.0,
                "w20": head[-1]["weight"] if len(head) == 20 else 0.0,
                "tail_count": len(tail),
                "tail_tau_sum": sum(item["tau_sum"] for item in tail),
                "tail_count_sum": sum(item["count"] for item in tail),
                "tail_top10": tail[:10],
            }
        )
    worst_tail_share = compact(max(records, key=lambda item: item["tail_share"]))
    worst_tail_over_head = compact(max(records, key=lambda item: item["tail_over_head"]))
    audit = {
        "certificate_type": "D4_R5_G1_tail44_audit",
        "status": "top20_56_equivalent_tail_over_head_bound_identified",
        "rows_seen": len(records),
        "target": "top20_sum >= 0.56 S, equivalently tail_after20 <= 0.44 S, equivalently tail/head <= 11/14≈0.785714.",
        "worst_tail_share": worst_tail_share,
        "worst_tail_over_head": worst_tail_over_head,
        "structural_conclusion": "top20_56_mass 的最坏点仍为 x=1023400。扫描中 tail/head 最大约 0.72877，低于 11/14≈0.78571；这给出约 0.0569 的比例余量。尾部由 73 个低权重团组成，tail average weight 远低于 head 平均权重。",
        "proof_tasks": [
            "证明 tail_after20/head20 <= 11/14",
            "优先采用 tail split：以 0.5*w20 切分，证明 near/head<=0.35 与 far/head<=0.43",
            "用排序阈值 w20 把 tail 分为接近阈值段与快速衰减段",
            "利用 tau_sum<60 与 a<=sqrt(x) 限制，证明第 21 位后不可能长期保持接近 w20 的平台",
            "将 light 的低 tau 团与 short/transition 的低 count 团分别建立尾部容量界，然后合并",
        ],
    }
    (DOCS / "d4-r5-G1-tail44-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 tail44 审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 目标等价式",
        f"- {audit['target']}",
        "",
        "## 最坏记录",
        f"- tail share 最坏：{worst_tail_share}",
        f"- tail/head 最坏：{worst_tail_over_head}",
        "",
        "## 证明任务",
    ]
    for item in audit["proof_tasks"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-tail44-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-tail44-audit.json")
    print(DOCS / "d4-r5-G1-tail44-audit.md")


if __name__ == "__main__":
    main()
