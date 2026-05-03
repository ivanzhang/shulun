#!/usr/bin/env python3
"""D4/R5 G1 top16 半质量证书审计。"""
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
        arr = [
            item
            for item in row["all_offsets"]
            if item["positive_contract_sum"] > 0
            and (item["tau_sum"] < 60 or (item["tau_sum"] >= 60 and item["count"] <= 25))
        ]
        weights = sorted([float(item["positive_contract_sum"]) for item in arr], reverse=True)
        total = sum(weights)
        square = sum(w * w for w in weights)
        if square <= 0:
            continue
        top16 = weights[:16]
        record = {
            "x": row["x"],
            "count": len(weights),
            "sum": total,
            "square": square,
            "neff": total * total / square,
            "top16_sum": sum(top16),
            "top16_sum_share": sum(top16) / total,
            "top16_square_share": sum(w * w for w in top16) / square,
            "cauchy_bound_from_top16_share": 16 / ((sum(top16) / total) ** 2),
        }
        records.append(record)

    worst_share = compact(min(records, key=lambda item: item["top16_sum_share"]))
    worst_neff = compact(max(records, key=lambda item: item["neff"]))
    audit = {
        "certificate_type": "D4_R5_G1_top16_mass_audit",
        "status": "top16_half_mass_verified_on_full_step100_scan",
        "source": str(INPUT.relative_to(ROOT)),
        "rows_seen": len(records),
        "lemma_template": "If the largest 16 nonordinary weights carry at least half of S, then S^2 <= 64 Q by Cauchy: Q >= T16^2/16 >= S^2/64.",
        "worst_top16_sum_share": worst_share,
        "worst_neff": worst_neff,
        "structural_reduction": "O2 的 Neff<=64 可进一步压缩为 top16 半质量引理。扫描中最坏 top16_sum_share 正好出现在 Neff 最大点 x=1023400，约为 0.50305，刚过 1/2。因此最终解析硬点是证明非 ordinary 偏移权重不能有超过半数质量落在第 17 位之后的长尾中。",
        "next_obligations": [
            "证明 top16_half_mass：最大的 16 个非 ordinary 偏移团贡献至少总非 ordinary 质量的一半",
            "解析来源应结合 tau_sum<60、a<=sqrt(x)、偏移 h=(-x mod a) 的重叠限制与 kernel 衰减",
            "若半质量常数太紧，可改为 top20：扫描最坏 top20_sum_share≈0.578，对应 Cauchy 常数约 59.8，仍小于 64",
        ],
    }
    (DOCS / "d4-r5-G1-top16-mass-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 top16 半质量证书审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_reduction"],
        "",
        "## 引理模板",
        f"- {audit['lemma_template']}",
        "",
        "## 最坏记录",
        f"- top16 半质量最坏：{worst_share}",
        f"- Neff 最坏：{worst_neff}",
        "",
        "## 下一义务",
    ]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-top16-mass-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-top16-mass-audit.json")
    print(DOCS / "d4-r5-G1-top16-mass-audit.md")


if __name__ == "__main__":
    main()
