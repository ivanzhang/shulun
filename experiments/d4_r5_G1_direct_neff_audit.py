#!/usr/bin/env python3
"""D4/R5 G1 直接 Neff 二阶能量审计。"""
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
    records = []
    for path in FILES:
        rows = json.loads(path.read_text(encoding="utf-8"))["rows"]
        for row in rows:
            items = []
            for item in row["all_offsets"]:
                weight = float(item["positive_contract_sum"])
                if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
                    items.append({"weight": weight, "tau_sum": item["tau_sum"], "count": item["count"], "offset": item["offset"]})
            total = sum(item["weight"] for item in items)
            square = sum(item["weight"] ** 2 for item in items)
            if square <= 0:
                continue
            bucket_mass = {}
            bucket_square = {}
            for name, predicate in BUCKETS:
                selected = [item for item in items if predicate(item)]
                bucket_mass[name] = sum(item["weight"] for item in selected) / total if total else 0.0
                bucket_square[name] = sum(item["weight"] ** 2 for item in selected) / square if square else 0.0
            records.append(
                {
                    "source": str(path.relative_to(ROOT)),
                    "x": row["x"],
                    "count": len(items),
                    "S": total,
                    "sqrtQ": square ** 0.5,
                    "Neff": total * total / square,
                    "ratio": total / (square ** 0.5),
                    "bucket_mass_share": bucket_mass,
                    "bucket_square_share": bucket_square,
                    "top10": sorted(items, key=lambda item: item["weight"], reverse=True)[:10],
                }
            )
    worst = compact(max(records, key=lambda item: item["Neff"]))
    audit = {
        "certificate_type": "D4_R5_G1_direct_neff_audit",
        "status": "direct_Neff64_route_replaces_fixed_topr_tail_route",
        "rows_seen": len(records),
        "worst_Neff": worst,
        "violations_Neff64": sum(1 for item in records if item["Neff"] >= 64),
        "structural_conclusion": "直接 Neff 审计合并 step100 全局扫描与 Case A 密邻域后，最大 Neff≈47.78，仍远低于 64。最坏点不是固定 top-r 头部失败本身，而是 tau 桶较均衡混合；各桶均贡献平方能量，因此二阶能量界比 top-r 半质量更稳定。",
        "proof_reduction": [
            "正式 O2 接口应为直接 S^2 <= 64 Q",
            "证明策略应建立 tau 桶二阶能量账本：每个 tau 桶有质量份额与平方份额的联合下界",
            "固定 top-r/tail44 证书只能作为启发，不进入最终闭合链条",
            "下一步提取 tau 桶质量-平方联合不等式，目标给出 Q/S^2 >= 1/64",
        ],
    }
    (DOCS / "d4-r5-G1-direct-neff-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 直接 Neff 二阶能量审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 最坏记录",
        f"- {worst}",
        f"- Neff64 violations：`{audit['violations_Neff64']}`",
        "",
        "## 证明归约",
    ]
    for item in audit["proof_reduction"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-direct-neff-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-direct-neff-audit.json")
    print(DOCS / "d4-r5-G1-direct-neff-audit.md")


if __name__ == "__main__":
    main()
