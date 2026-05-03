#!/usr/bin/env python3
"""D4/R5 G1 统一 exceptional 能量接口审计。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCAN_FILES = [
    "d4-r5-offset-layered-scan-1049300-1049900-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json",
]


def rows(name: str) -> list[dict[str, Any]]:
    return json.loads((DOCS / name).read_text(encoding="utf-8")).get("rows", [])


def val(row: dict[str, Any], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def compact(record: dict[str, Any]) -> dict[str, Any]:
    out = {}
    for key, item in record.items():
        out[key] = float(f"{item:.17g}") if isinstance(item, float) else item
    return out


def main() -> None:
    records = []
    for name in SCAN_FILES:
        for row in rows(name):
            L = val(row, "positive_contract_sum")
            exceptional_energy = val(row, "exceptional_l2_sqrt")
            exceptional_mass = val(row, "transition_weight") + val(row, "short_chain_weight") + val(row, "light_weight")
            ordinary = val(row, "ordinary_weight")
            if exceptional_energy > 0:
                records.append(
                    {
                        "source": name,
                        "x": row.get("x"),
                        "L": L,
                        "ordinary_weight": ordinary,
                        "nonordinary_exceptional_mass": exceptional_mass,
                        "exceptional_l2_sqrt": exceptional_energy,
                        "L_over_exceptional_l2_sqrt": L / exceptional_energy,
                        "nonordinary_over_exceptional_l2_sqrt": exceptional_mass / exceptional_energy,
                        "ordinary_over_exceptional_l2_sqrt": ordinary / exceptional_energy,
                    }
                )

    worst_L = compact(max(records, key=lambda item: item["L_over_exceptional_l2_sqrt"]))
    worst_nonordinary = compact(max(records, key=lambda item: item["nonordinary_over_exceptional_l2_sqrt"]))
    worst_ordinary = compact(max(records, key=lambda item: item["ordinary_over_exceptional_l2_sqrt"]))
    needed = 18.113
    audit = {
        "certificate_type": "D4_R5_G1_unified_exceptional_energy_audit",
        "status": "unified_exceptional_Aeff_candidate_has_scan_margin_not_yet_theorem",
        "rows_seen": len(records),
        "candidate_interface": "E_G1 := exceptional_l2_sqrt, controlling the full mutually exclusive mass L",
        "threshold_reference": "For L_cap=0.48 and eta=0.015, sufficient A_eff <= 18.113...",
        "worst_L_over_exceptional": worst_L,
        "worst_nonordinary_over_exceptional": worst_nonordinary,
        "worst_ordinary_over_exceptional": worst_ordinary,
        "scan_margin_to_18p113": needed - worst_L["L_over_exceptional_l2_sqrt"],
        "structural_reading": "若将 G1 能量口径改为单一 exceptional_l2_sqrt，则 ordinary、transition、short_chain、light 的总正质量 L 在扫描中统一受控，最坏 A_eff 约 12.6822，距离 18.113 仍有约 5.43 余量。这避免了对同一 exceptional 能量的分层重复使用问题。",
        "theorem_obligation": [
            "证明 exceptional_l2_sqrt 的定义覆盖 transition/short_chain/light 三层，且 ordinary 层也可被同一 exceptional 场的 L2 半范数控制",
            "将 Lyapunov 能量 E_* 从分层 sqrt 和改写为统一 exceptional 能量或证明两者的安全替代关系",
            "以 A_eff=13 或 A_eff=14 作为显式定理常数，重新检查 D_* >= 0.015 的参数余量",
            "确认统一 exceptional 能量在递归尺度 j 下可传递，并不破坏 stable payment telescope",
        ],
    }
    (DOCS / "d4-r5-G1-unified-exceptional-energy-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# D4/R5 G1 统一 exceptional 能量接口审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_reading"],
        "",
        "## 核心比值",
        f"- 行数：`{audit['rows_seen']}`",
        f"- 阈值参考：{audit['threshold_reference']}",
        f"- 最坏 `L/exceptional_l2_sqrt`：{worst_L}",
        f"- 最坏非 ordinary 质量比：{worst_nonordinary}",
        f"- 最坏 ordinary 质量比：{worst_ordinary}",
        f"- 对 18.113 的扫描余量：`{audit['scan_margin_to_18p113']}`",
        "",
        "## 定理化义务",
    ]
    for item in audit["theorem_obligation"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-unified-exceptional-energy-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-unified-exceptional-energy-audit.json")
    print(DOCS / "d4-r5-G1-unified-exceptional-energy-audit.md")


if __name__ == "__main__":
    main()
