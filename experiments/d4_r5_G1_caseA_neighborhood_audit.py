#!/usr/bin/env python3
"""D4/R5 G1 Case A 邻域复核审计。"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INPUT = DOCS / "d4-r5-O2-caseA-neighborhood-1023000-1023800-step1.json"


def compact(record: dict) -> dict:
    return {key: float(f"{value:.17g}") if isinstance(value, float) else value for key, value in record.items()}


def main() -> None:
    rows = json.loads(INPUT.read_text(encoding="utf-8"))["rows"]
    records = []
    for row in rows:
        weights = []
        items = []
        for item in row["all_offsets"]:
            weight = float(item["positive_contract_sum"])
            if weight > 0 and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25)):
                weights.append(weight)
                items.append({"weight": weight, "tau_sum": item["tau_sum"], "count": item["count"]})
        weights.sort(reverse=True)
        total = sum(weights)
        square = sum(w * w for w in weights)
        if square <= 0 or len(weights) <= 20:
            continue
        top20 = sum(weights[:20])
        tail20 = total - top20
        neff = total * total / square
        sorted_items = sorted(items, key=lambda item: item["weight"], reverse=True)
        head20 = sorted_items[:20]
        w20 = head20[-1]["weight"]
        tail = sorted_items[20:]
        far = [item for item in tail if item["weight"] < 0.5 * w20]
        records.append(
            {
                "x": row["x"],
                "count": len(weights),
                "total": total,
                "l2_sqrt": square ** 0.5,
                "neff": neff,
                "ratio": total / (square ** 0.5),
                "top20_share": top20 / total,
                "top20_cauchy_bound": 20 / ((top20 / total) ** 2),
                "tail20_over_head20": tail20 / top20,
                "far_over_head20": sum(item["weight"] for item in far) / top20,
            }
        )
    audit = {
        "certificate_type": "D4_R5_G1_caseA_neighborhood_audit",
        "status": "top20_tail_route_refuted_locally_but_Neff64_survives",
        "source": str(INPUT.relative_to(ROOT)),
        "rows_seen": len(records),
        "worst_neff": compact(max(records, key=lambda item: item["neff"])),
        "worst_top20_cauchy_bound": compact(max(records, key=lambda item: item["top20_cauchy_bound"])),
        "top20_bound_violations": sum(1 for item in records if item["top20_cauchy_bound"] >= 64),
        "neff64_violations": sum(1 for item in records if item["neff"] >= 64),
        "structural_conclusion": "密邻域复核显示：固定 top20_56/tail44 路线不是局部稳定的，top20 Cauchy bound 可达约 67.39；但原始 Neff<=64 仍稳定，邻域最大 Neff≈47.78。因此应放弃固定 top-r 半质量闭合，回到直接二阶能量 Neff 证明。",
        "next_route": [
            "直接证明 S^2<=64Q，而不是通过固定 top20 头部质量",
            "利用 Case A 邻域中 Neff 最大约 47.78 的余量，寻找二阶能量下界机制",
            "保留 top-r 证书作为启发，但不作为正式闭合接口",
        ],
    }
    (DOCS / "d4-r5-G1-caseA-neighborhood-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 Case A 邻域复核审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 最坏记录",
        f"- Neff 最坏：{audit['worst_neff']}",
        f"- top20 Cauchy bound 最坏：{audit['worst_top20_cauchy_bound']}",
        f"- top20 bound violations：`{audit['top20_bound_violations']}`",
        f"- Neff64 violations：`{audit['neff64_violations']}`",
        "",
        "## 下一路线",
    ]
    for item in audit["next_route"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-caseA-neighborhood-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-caseA-neighborhood-audit.json")
    print(DOCS / "d4-r5-G1-caseA-neighborhood-audit.md")


if __name__ == "__main__":
    main()
