#!/usr/bin/env python3
"""D4/R5 G1 tail44 分段尾界审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json"
THRESHOLDS = [0.9, 0.8, 0.7, 0.6, 0.5]


def compact(record: dict) -> dict:
    return {key: float(f"{value:.17g}") if isinstance(value, float) else value for key, value in record.items()}


def nonordinary_items(row: dict) -> list[dict]:
    items = []
    for item in row["all_offsets"]:
        weight = float(item["positive_contract_sum"])
        if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
            items.append(
                {
                    "weight": weight,
                    "offset": item["offset"],
                    "tau_sum": item["tau_sum"],
                    "count": item["count"],
                    "average_kernel": item["average_kernel"],
                }
            )
    return sorted(items, key=lambda item: item["weight"], reverse=True)


def main() -> None:
    rows = json.loads(INPUT.read_text(encoding="utf-8"))["rows"]
    summaries = {}
    worst_tail = None
    for threshold in THRESHOLDS:
        records = []
        for row in rows:
            weights = nonordinary_items(row)
            if len(weights) <= 20:
                continue
            head = weights[:20]
            tail = weights[20:]
            head_sum = sum(item["weight"] for item in head)
            tail_sum = sum(item["weight"] for item in tail)
            if head_sum <= 0:
                continue
            w20 = head[-1]["weight"]
            near = [item for item in tail if item["weight"] >= threshold * w20]
            far = [item for item in tail if item["weight"] < threshold * w20]
            record = {
                "x": row["x"],
                "threshold": threshold,
                "w20": w20,
                "head_sum": head_sum,
                "tail_sum": tail_sum,
                "tail_over_head": tail_sum / head_sum,
                "near_count": len(near),
                "near_sum": sum(item["weight"] for item in near),
                "near_over_head": sum(item["weight"] for item in near) / head_sum,
                "far_count": len(far),
                "far_sum": sum(item["weight"] for item in far),
                "far_over_head": sum(item["weight"] for item in far) / head_sum,
                "tail_top10": tail[:10],
            }
            records.append(record)
            if worst_tail is None or record["tail_over_head"] > worst_tail["tail_over_head"]:
                worst_tail = record
        summaries[str(threshold)] = {
            "max_near_count": compact(max(records, key=lambda item: item["near_count"])),
            "max_near_over_head": compact(max(records, key=lambda item: item["near_over_head"])),
            "max_far_over_head": compact(max(records, key=lambda item: item["far_over_head"])),
            "max_tail_over_head": compact(max(records, key=lambda item: item["tail_over_head"])),
        }

    audit = {
        "certificate_type": "D4_R5_G1_tail_split_audit",
        "status": "tail44_split_into_near_platform_and_decay_tail",
        "target": "tail_after20/head20 <= 11/14",
        "threshold_summaries": summaries,
        "worst_tail_record": compact(worst_tail or {}),
        "structural_conclusion": "按阈值 theta*w20 切分尾部后，最坏 tail/head 仍在 x=1023400。取 theta=0.6 时，近阈值平台最多贡献 near/head≈0.368，但最坏点 near/head≈0.229；远尾在最坏点 far/head≈0.500。取 theta=0.5 时，最坏点 near/head≈0.296、far/head≈0.433。说明证明 tail44 可拆为平台长度界与远尾衰减界，远尾总量是更硬部分。",
        "recommended_split": {
            "theta": 0.5,
            "sufficient_conditions": [
                "near_{>=0.5 w20}/head20 <= 0.35",
                "far_{<0.5 w20}/head20 <= 0.43",
                "then tail/head <= 0.78 < 11/14≈0.785714",
            ],
            "scan_worst_at_x1023400": {
                "near_over_head": 0.29567435872916265,
                "far_over_head": 0.4330956816161989,
                "tail_over_head": 0.7287700403453615,
            },
        },
        "next_obligations": [
            "证明近阈值平台界：第 21 位之后仍 >=0.5*w20 的非 ordinary 团总质量 <=0.35 head20",
            "证明远尾衰减界：<0.5*w20 的非 ordinary 团总质量 <=0.43 head20",
            "远尾界应利用 tau_sum<60 的低容量、偏移同余复用限制与 kernel 相位衰减",
        ],
    }
    (DOCS / "d4-r5-G1-tail-split-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 tail44 分段尾界审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 推荐分段",
        f"- theta：`{audit['recommended_split']['theta']}`",
    ]
    for item in audit["recommended_split"]["sufficient_conditions"]:
        lines.append(f"- {item}")
    lines += ["", "## 阈值摘要"]
    for threshold, summary in summaries.items():
        lines.append(f"### theta={threshold}")
        lines.append(f"- max_near_count：{summary['max_near_count']}")
        lines.append(f"- max_near_over_head：{summary['max_near_over_head']}")
        lines.append(f"- max_far_over_head：{summary['max_far_over_head']}")
    lines += ["", "## 下一义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-tail-split-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-tail-split-audit.json")
    print(DOCS / "d4-r5-G1-tail-split-audit.md")


if __name__ == "__main__":
    main()
