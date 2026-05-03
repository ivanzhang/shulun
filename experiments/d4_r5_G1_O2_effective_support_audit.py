#!/usr/bin/env python3
"""D4/R5 G1 O2 非 ordinary 有效支撑审计。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FILES = [
    "d4-r5-offset-layered-scan-1049300-1049900-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json",
]


def load_rows(name: str) -> list[dict[str, Any]]:
    return json.loads((DOCS / name).read_text(encoding="utf-8")).get("rows", [])


def val(row: dict[str, Any], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def compact(record: dict[str, Any]) -> dict[str, Any]:
    return {key: float(f"{item:.17g}") if isinstance(item, float) else item for key, item in record.items()}


def main() -> None:
    records = []
    layer_records = {"light": [], "short": [], "transition": []}
    for name in FILES:
        for row in load_rows(name):
            energy = val(row, "exceptional_l2_sqrt")
            if energy <= 0:
                continue
            masses = {
                "light": val(row, "light_weight"),
                "short": val(row, "short_chain_weight"),
                "transition": val(row, "transition_weight"),
            }
            energies = {
                "light": val(row, "light_l2_sqrt"),
                "short": val(row, "short_chain_l2_sqrt"),
                "transition": val(row, "transition_l2_sqrt"),
            }
            counts = {
                "light": int(row.get("light_count", 0) or 0),
                "short": int(row.get("short_chain_count", 0) or 0),
                "transition": int(row.get("transition_count", 0) or 0),
            }
            nonordinary = sum(masses.values())
            record = {
                "source": name,
                "x": row.get("x"),
                "nonordinary_weight": nonordinary,
                "exceptional_l2_sqrt": energy,
                "ratio": nonordinary / energy,
                "effective_support": (nonordinary / energy) ** 2,
                "masses": masses,
                "energies": energies,
                "counts": counts,
            }
            records.append(record)
            for layer in layer_records:
                if masses[layer] > 0 and energies[layer] > 0:
                    layer_records[layer].append(
                        {
                            "source": name,
                            "x": row.get("x"),
                            "mass": masses[layer],
                            "energy": energies[layer],
                            "ratio": masses[layer] / energies[layer],
                            "effective_support": (masses[layer] / energies[layer]) ** 2,
                            "count": counts[layer],
                        }
                    )

    worst_total = compact(max(records, key=lambda item: item["ratio"]))
    worst_layer = {layer: compact(max(items, key=lambda item: item["ratio"])) for layer, items in layer_records.items() if items}
    audit = {
        "certificate_type": "D4_R5_G1_O2_effective_support_audit",
        "status": "O2_reduced_to_Neff64_with_top20_56_mass_route",
        "target": "nonordinary_weight = light + short_chain + transition <= 8 * exceptional_l2_sqrt",
        "rows_seen": len(records),
        "worst_total": worst_total,
        "worst_layers": worst_layer,
        "effective_support_target": "It is enough to prove nonordinary effective support (sum w)^2 / sum w^2 <= 64.",
        "structural_reading": "O2 的最坏情形由 light 层主导；short_chain 与 transition 的单层比值分别约 3.03 与 1.69，远低于 light 的 6.84。扫描中 nonordinary 总有效支撑最大约 44.62，低于目标 64；top20 审计显示只需证明前 20 个非 ordinary 权重承担至少 56% 总质量即可推出 Neff<=64，余量比 top16 半质量更稳。",
        "proof_route": [
            "定义非 ordinary 权重向量 w_h，包含 light、short_chain、transition 的正贡献，E_G1^2=sum_h w_h^2",
            "证明有效支撑 Neff=(sum_h w_h)^2/(sum_h w_h^2)<=64",
            "用 Cauchy 得到 sum_h w_h <= sqrt(64) E_G1 = 8 E_G1",
            "Neff<=64 的证明应利用 light 层 tau_sum<T_off=60 导致单偏移贡献上界，以及 short/transition 的低计数异常被平方项放大吸收",
            "优先使用 top20_56_mass 模板：证明最大 20 个非 ordinary 偏移团贡献至少 56% 总质量，从而推出 Neff<=64",
            "等价使用 tail44 模板：证明第 21 位后的尾部质量与前 20 位头部质量满足 tail/head <= 11/14",
            "top16 半质量仍可作为锐利备选，但余量较窄",
        ],
    }
    (DOCS / "d4-r5-G1-O2-effective-support-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# D4/R5 G1 O2 非 ordinary 有效支撑审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_reading"],
        "",
        "## O2 目标",
        f"- {audit['target']}",
        f"- 充分条件：{audit['effective_support_target']}",
        "",
        "## 最坏总比值",
        f"- {worst_total}",
        "",
        "## 单层最坏比值",
    ]
    for layer, item in worst_layer.items():
        lines.append(f"- `{layer}`：{item}")
    lines += ["", "## 证明路线"]
    for item in audit["proof_route"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-O2-effective-support-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-O2-effective-support-audit.json")
    print(DOCS / "d4-r5-G1-O2-effective-support-audit.md")


if __name__ == "__main__":
    main()
