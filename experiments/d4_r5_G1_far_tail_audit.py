#!/usr/bin/env python3
"""D4/R5 G1 far tail 分桶容量审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-O2-alloffsets-1e6-1p1e6-step100-T60.json"
BUCKETS = [
    ("tau_le_4", lambda item: item["tau_sum"] <= 4),
    ("tau_5_8", lambda item: 5 <= item["tau_sum"] <= 8),
    ("tau_9_16", lambda item: 9 <= item["tau_sum"] <= 16),
    ("tau_17_32", lambda item: 17 <= item["tau_sum"] <= 32),
    ("tau_33_59", lambda item: 33 <= item["tau_sum"] < 60),
    ("heavy_short", lambda item: item["tau_sum"] >= 60),
]


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
                items.append({"weight": weight, "offset": item["offset"], "tau_sum": item["tau_sum"], "count": item["count"], "average_kernel": item["average_kernel"]})
        items.sort(key=lambda item: item["weight"], reverse=True)
        if len(items) <= 20:
            continue
        head_sum = sum(item["weight"] for item in items[:20])
        w20 = items[19]["weight"]
        far = [item for item in items[20:] if item["weight"] < 0.5 * w20]
        if head_sum <= 0:
            continue
        bucket_values = {}
        for name, predicate in BUCKETS:
            selected = [item for item in far if predicate(item)]
            bucket_values[name] = {
                "count": len(selected),
                "sum": sum(item["weight"] for item in selected),
                "over_head": sum(item["weight"] for item in selected) / head_sum,
            }
        records.append(
            {
                "x": row["x"],
                "head_sum": head_sum,
                "w20": w20,
                "far_count": len(far),
                "far_sum": sum(item["weight"] for item in far),
                "far_over_head": sum(item["weight"] for item in far) / head_sum,
                "bucket_values": bucket_values,
                "far_top10": far[:10],
            }
        )

    worst_far = compact(max(records, key=lambda item: item["far_over_head"]))
    bucket_worst = {}
    for name, _ in BUCKETS:
        bucket_worst[name] = compact(max(records, key=lambda item: item["bucket_values"][name]["over_head"]))

    audit = {
        "certificate_type": "D4_R5_G1_far_tail_audit",
        "status": "far_tail_reduced_to_low_tau_buckets",
        "rows_seen": len(records),
        "target": "far_{<0.5w20}/head20 <= 0.43",
        "worst_far": worst_far,
        "bucket_worst": bucket_worst,
        "structural_conclusion": "far 最坏仍在 x=1023400，far/head≈0.4331，略高于目标 0.43，说明当前 0.43 常数过紧；若放宽到 0.435，则扫描通过。far 质量几乎完全来自 tau_sum<=8 且 count<=2 的低容量团：tau<=4 贡献约 0.225H，5<=tau<=8 贡献约 0.145H。tau>=9 的总贡献很小。",
        "recommended_adjustment": {
            "near_bound": 0.35,
            "far_bound": 0.435,
            "combined": 0.785,
            "target_11_over_14": 11 / 14,
            "passes_tail44": 0.35 + 0.435 < 11 / 14,
        },
        "proof_obligations": [
            "F1: tau_sum<=4 far bucket <=0.23 head20",
            "F2: 5<=tau_sum<=8 far bucket <=0.17 head20",
            "F3: tau_sum>=9 far bucket <=0.035 head20",
            "Then far/head <=0.435 and near/head<=0.35 imply tail/head<=0.785<11/14",
        ],
    }
    (DOCS / "d4-r5-G1-far-tail-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 far tail 分桶容量审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 推荐常数调整",
    ]
    for key, value in audit["recommended_adjustment"].items():
        lines.append(f"- `{key}`：{value}")
    lines += ["", "## far 最坏记录", f"- {worst_far}", "", "## 分桶最坏"]
    for name, item in bucket_worst.items():
        lines.append(f"- `{name}`：x={item['x']}, over_head={item['bucket_values'][name]['over_head']}, count={item['bucket_values'][name]['count']}")
    lines += ["", "## 证明义务"]
    for item in audit["proof_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-far-tail-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-far-tail-audit.json")
    print(DOCS / "d4-r5-G1-far-tail-audit.md")


if __name__ == "__main__":
    main()
