#!/usr/bin/env python3
"""D4/R5 G1 统一 exceptional 能量定理化路线审计。"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = [
    "d4-r5-offset-layered-scan-1049300-1049900-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json",
]
TARGET = 18.113


def load_rows(name: str) -> list[dict[str, Any]]:
    return json.loads((DOCS / name).read_text(encoding="utf-8")).get("rows", [])


def v(row: dict[str, Any], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def compact(record: dict[str, Any]) -> dict[str, Any]:
    return {key: float(f"{val:.17g}") if isinstance(val, float) else val for key, val in record.items()}


def main() -> None:
    records = []
    for name in FILES:
        for row in load_rows(name):
            energy = v(row, "exceptional_l2_sqrt")
            if energy <= 0:
                continue
            ordinary = v(row, "ordinary_weight")
            nonordinary = v(row, "transition_weight") + v(row, "short_chain_weight") + v(row, "light_weight")
            count_nonordinary = int(row.get("transition_count", 0) or 0) + int(row.get("short_chain_count", 0) or 0) + int(row.get("light_count", 0) or 0)
            records.append(
                {
                    "source": name,
                    "x": row.get("x"),
                    "L": ordinary + nonordinary,
                    "ordinary_weight": ordinary,
                    "nonordinary_weight": nonordinary,
                    "exceptional_l2_sqrt": energy,
                    "ordinary_ratio": ordinary / energy,
                    "nonordinary_ratio": nonordinary / energy,
                    "total_ratio": (ordinary + nonordinary) / energy,
                    "nonordinary_count": count_nonordinary,
                    "offset_count": int(row.get("offset_count", 0) or 0),
                    "ordinary_count": int(row.get("ordinary_count", 0) or 0),
                }
            )

    worst = {field: compact(max(records, key=lambda item: item[field])) for field in ["ordinary_ratio", "nonordinary_ratio", "total_ratio", "nonordinary_count", "offset_count"]}
    constants = []
    for ordinary_const in [7.5, 8.0, 8.25, 8.5]:
        for nonordinary_const in [6.75, 7.0, 7.5, 8.0, math.sqrt(102), math.sqrt(110)]:
            total = ordinary_const + nonordinary_const
            constants.append(
                {
                    "A_ordinary": ordinary_const,
                    "A_nonordinary": float(nonordinary_const),
                    "A_total": float(total),
                    "margin_to_18p113": float(TARGET - total),
                    "passes": total <= TARGET,
                }
            )
    good = [item for item in constants if item["passes"]]
    best_simple = min(good, key=lambda item: (item["A_total"], item["A_ordinary"], item["A_nonordinary"])) if good else None

    audit = {
        "certificate_type": "D4_R5_G1_unified_theoremization_audit",
        "status": "reduced_to_two_analytic_lemmas_Aordinary_and_Anonordinary",
        "target_Aeff": TARGET,
        "rows_seen": len(records),
        "worst_observed": worst,
        "recommended_constants": {
            "scan_tight": {"A_ordinary": 7.5, "A_nonordinary": 6.75, "A_total": 14.25, "margin": TARGET - 14.25},
            "review_safe": {"A_ordinary": 8.0, "A_nonordinary": 8.0, "A_total": 16.0, "margin": TARGET - 16.0},
            "support_cauchy_if_N_le_102": {"A_ordinary": 8.0, "A_nonordinary": math.sqrt(102), "A_total": 8.0 + math.sqrt(102), "margin": TARGET - (8.0 + math.sqrt(102))},
            "support_cauchy_if_N_le_110": {"A_ordinary": 8.0, "A_nonordinary": math.sqrt(110), "A_total": 8.0 + math.sqrt(110), "margin": TARGET - (8.0 + math.sqrt(110))},
        },
        "best_simple_passing_combo": best_simple,
        "structural_reduction": "统一 exceptional 路线可化为两个解析引理：ordinary_weight <= A_o E_G1 与 nonordinary_weight <= A_x E_G1。扫描最坏分别约 7.3343 与 6.6796；因此取 A_o=8, A_x=8 可给 A_eff=16，较 18.113 有约 2.113 余量。粗 Cauchy 支撑数路线若只知 N<=110 则 A_o+sqrt(N)>18.113，不足；所以非 ordinary 层应证明加权/有效支撑常数 A_x<=8，而不是只用裸支撑数上界。",
        "analytic_obligations": [
            "O1 ordinary 影子能量引理：证明 ordinary_weight <= 8 exceptional_l2_sqrt",
            "O2 非 ordinary 有效支撑引理：证明 transition+short_chain+light <= 8 exceptional_l2_sqrt；已由 O2 审计压缩为 Neff<=64",
            "O3 能量语义引理：证明 E_G1=exceptional_l2_sqrt 在递归尺度下与 D_* 定义同型，并可替代旧分层 E_*",
            "O4 支付兼容引理：用 E_G1 改写后 stable payment telescope 的符号与望远镜求和不变",
        ],
    }
    (DOCS / "d4-r5-G1-unified-theoremization-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 统一 exceptional 能量定理化审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_reduction"],
        "",
        "## 最坏观测",
    ]
    for key, item in worst.items():
        lines.append(f"- `{key}`：{item}")
    lines += ["", "## 推荐常数"]
    for key, item in audit["recommended_constants"].items():
        lines.append(f"- `{key}`：{item}")
    lines += ["", "## 解析义务"]
    for item in audit["analytic_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-unified-theoremization-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-unified-theoremization-audit.json")
    print(DOCS / "d4-r5-G1-unified-theoremization-audit.md")


if __name__ == "__main__":
    main()
