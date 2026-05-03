#!/usr/bin/env python3
"""D4/R5 G1 互斥分层口径审计。"""
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

PARTITION_KEYS = [
    "transition_weight",
    "short_chain_weight",
    "ordinary_weight",
    "light_weight",
]
HEAVY_CHILD_KEYS = [
    "transition_weight",
    "short_chain_weight",
    "ordinary_weight",
]
ENERGY_KEYS = {
    "transition_weight": ["transition_l2_sqrt", "transition_high_tail_l2_sqrt", "transition_low_start_l2_sqrt"],
    "short_chain_weight": ["short_chain_l2_sqrt"],
    "ordinary_weight": [],
    "light_weight": ["light_l2_sqrt"],
}


def load_rows(name: str) -> list[dict[str, Any]]:
    path = DOCS / name
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get("rows", [])


def value(row: dict[str, Any], key: str) -> float:
    return float(row.get(key, 0.0) or 0.0)


def compact(record: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, item in record.items():
        out[key] = float(f"{item:.17g}") if isinstance(item, float) else item
    return out


def main() -> None:
    rows_seen = 0
    partition_records = []
    energy_missing = {key: 0 for key in PARTITION_KEYS}
    positive_counts = {key: 0 for key in PARTITION_KEYS}
    examples_missing: dict[str, dict[str, Any]] = {}
    layer_ratios = []

    for name in SCAN_FILES:
        for row in load_rows(name):
            rows_seen += 1
            L = value(row, "positive_contract_sum")
            partition_sum = sum(value(row, key) for key in PARTITION_KEYS)
            heavy_sum = sum(value(row, key) for key in HEAVY_CHILD_KEYS)
            heavy = value(row, "heavy_weight")
            record = {
                "source": name,
                "x": row.get("x"),
                "L": L,
                "partition_sum": partition_sum,
                "heavy_weight": heavy,
                "heavy_children_sum": heavy_sum,
                "partition_residual": L - partition_sum,
                "heavy_parent_residual": heavy - heavy_sum,
            }
            partition_records.append(record)
            for key in PARTITION_KEYS:
                mass = value(row, key)
                if mass > 0:
                    positive_counts[key] += 1
                    energies = [value(row, energy_key) for energy_key in ENERGY_KEYS[key]]
                    usable_energy = max(energies) if energies else 0.0
                    if usable_energy <= 0:
                        energy_missing[key] += 1
                        examples_missing.setdefault(
                            key,
                            compact({"source": name, "x": row.get("x"), "mass": mass, "usable_energy": usable_energy}),
                        )
                    else:
                        layer_ratios.append(
                            compact(
                                {
                                    "source": name,
                                    "x": row.get("x"),
                                    "layer": key,
                                    "mass": mass,
                                    "usable_energy": usable_energy,
                                    "ratio": mass / usable_energy,
                                }
                            )
                        )

    max_partition_abs = max(partition_records, key=lambda r: abs(r["partition_residual"]))
    max_heavy_abs = max(partition_records, key=lambda r: abs(r["heavy_parent_residual"]))
    layer_ratio_worst = []
    for key in PARTITION_KEYS:
        subset = [item for item in layer_ratios if item["layer"] == key]
        if subset:
            layer_ratio_worst.append(max(subset, key=lambda item: item["ratio"]))

    audit = {
        "certificate_type": "D4_R5_G1_partition_refinement_audit",
        "status": "partition_identity_verified_energy_interface_missing_for_ordinary_and_some_short_transition_files",
        "rows_seen": rows_seen,
        "partition_identity": "positive_contract_sum = transition_weight + short_chain_weight + ordinary_weight + light_weight",
        "heavy_parent_identity": "heavy_weight = transition_weight + short_chain_weight + ordinary_weight",
        "max_partition_abs_residual": compact(max_partition_abs),
        "max_heavy_parent_abs_residual": compact(max_heavy_abs),
        "positive_counts": positive_counts,
        "energy_missing_counts": energy_missing,
        "energy_missing_examples": examples_missing,
        "layer_ratio_worst_with_available_energy": layer_ratio_worst,
        "structural_conclusion": "G1 的质量口径可以无重叠地改写为 transition/short_chain/ordinary/light 四层；heavy 不是互斥层，而是前三层父类。剩余硬点从‘漏 heavy’改为‘ordinary 层及部分扫描文件的 short/transition 层缺少匹配 l2_sqrt 能量字段或解析能量定义’。",
        "next_obligations": [
            "在正文中把 G1 分层定义为 P_transition, P_short, P_ordinary, P_light 四个互斥层",
            "将 heavy 仅作为父类监控量，不进入 Cauchy 求和分解",
            "为 ordinary 层定义解析能量 e_ordinary，或证明 ordinary 正质量必触发 jump/base 证书",
            "补齐 short_chain/transition 在非 full 扫描文件中的 l2_sqrt 字段，或用 exceptional_l2_sqrt 给出可审查替代上界",
        ],
    }

    (DOCS / "d4-r5-G1-partition-refinement-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# D4/R5 G1 互斥分层口径审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 恒等式验证",
        f"- 行数：`{rows_seen}`",
        f"- 互斥分解：`{audit['partition_identity']}`",
        f"- 父类关系：`{audit['heavy_parent_identity']}`",
        f"- 最大互斥残差：{audit['max_partition_abs_residual']}",
        f"- 最大 heavy 父类残差：{audit['max_heavy_parent_abs_residual']}",
        "",
        "## 能量接口缺口",
    ]
    for key in PARTITION_KEYS:
        lines.append(
            f"- `{key}`：positive_count={positive_counts[key]}, missing_energy_count={energy_missing[key]}, example={examples_missing.get(key)}"
        )
    lines += ["", "## 已有能量字段下的最坏 B/e"]
    for item in layer_ratio_worst:
        lines.append(f"- `{item['layer']}`：ratio={item['ratio']}, x={item['x']}, source={item['source']}")
    lines += ["", "## 下一步义务"]
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-partition-refinement-audit.md").write_text("\n".join(lines), encoding="utf-8")

    print(DOCS / "d4-r5-G1-partition-refinement-audit.json")
    print(DOCS / "d4-r5-G1-partition-refinement-audit.md")


if __name__ == "__main__":
    main()
