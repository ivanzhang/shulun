#!/usr/bin/env python3
"""D4/R5 G1 A_eff 分层 Cauchy 审计。"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SCAN_FILES = [
    "d4-r5-offset-heavy-light-scan-1020000-1030000-step500.json",
    "d4-r5-offset-heavy-light-scan-1028000-1028300-step1.json",
    "d4-r5-offset-heavy-light-scan-1049300-1049900-step1-T60.json",
    "d4-r5-offset-heavy-light-scan-1088200-1088600-step1-T60.json",
    "d4-r5-offset-layered-scan-1049300-1049900-step1-T60.json",
    "d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json",
    "d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60.json",
]

SQRT_KEYS = [
    "transition_high_tail_l2_sqrt",
    "transition_low_start_l2_sqrt",
    "short_chain_l2_sqrt",
    "light_l2_sqrt",
]
WEIGHT_KEYS = [
    "transition_high_tail_weight",
    "transition_low_start_weight",
    "short_chain_weight",
    "light_weight",
]


def load_rows(name: str) -> list[dict[str, Any]]:
    path = DOCS / name
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return json.load(fh).get("rows", [])


def compact(record: dict[str, Any]) -> dict[str, Any]:
    return {key: (float(f"{value:.17g}") if isinstance(value, float) else value) for key, value in record.items()}


def main() -> None:
    ratios = []
    layer_ratios = []
    mass_gaps = []
    for name in SCAN_FILES:
        for row in load_rows(name):
            L = float(row.get("positive_contract_sum", 0.0) or 0.0)
            E = sum(float(row.get(key, 0.0) or 0.0) for key in SQRT_KEYS)
            covered_mass = sum(float(row.get(key, 0.0) or 0.0) for key in WEIGHT_KEYS)
            heavy_mass = float(row.get("heavy_weight", 0.0) or 0.0)
            ordinary_mass = float(row.get("ordinary_weight", 0.0) or 0.0)
            all_named_mass = covered_mass + heavy_mass + ordinary_mass
            mass_gaps.append(
                {
                    "source": name,
                    "x": row.get("x"),
                    "L": L,
                    "current_layer_mass": covered_mass,
                    "heavy_mass": heavy_mass,
                    "ordinary_mass": ordinary_mass,
                    "all_named_formal_sum": all_named_mass,
                    "current_mass_gap": L - covered_mass,
                    "formal_overlap_or_gap": L - all_named_mass,
                }
            )
            if E > 0:
                ratios.append({"source": name, "x": row.get("x"), "L": L, "E_star": E, "A_eff_observed": L / E})
            for weight_key, energy_key in zip(WEIGHT_KEYS, SQRT_KEYS):
                B = float(row.get(weight_key, 0.0) or 0.0)
                e = float(row.get(energy_key, 0.0) or 0.0)
                if e > 0:
                    layer_ratios.append({"source": name, "x": row.get("x"), "layer": weight_key, "B": B, "e": e, "ratio": B / e})

    floor_summaries = []
    for floor in [0.35, 0.4, 0.42, 0.45]:
        subset = [r for r in ratios if r["L"] >= floor]
        if subset:
            worst = max(subset, key=lambda r: r["A_eff_observed"])
            floor_summaries.append({"L_floor": floor, "count": len(subset), "max_A_eff_observed": compact(worst)})
        else:
            floor_summaries.append({"L_floor": floor, "count": 0})

    layer_worst = []
    for layer in WEIGHT_KEYS:
        subset = [r for r in layer_ratios if r["layer"] == layer]
        if subset:
            layer_worst.append(compact(max(subset, key=lambda r: r["ratio"])))

    mass_gap_summary = {
        "max_current_mass_gap": compact(max(mass_gaps, key=lambda r: r["current_mass_gap"])),
        "max_current_mass_gap": compact(max(mass_gaps, key=lambda r: r["current_mass_gap"])),
        "max_positive_formal_overlap_or_gap": compact(max(mass_gaps, key=lambda r: r["formal_overlap_or_gap"])),
        "max_negative_formal_overlap_or_gap": compact(min(mass_gaps, key=lambda r: r["formal_overlap_or_gap"])),
        "max_heavy_mass": compact(max(mass_gaps, key=lambda r: r["heavy_mass"])),
        "max_ordinary_mass": compact(max(mass_gaps, key=lambda r: r["ordinary_mass"])),
        "interpretation": "current_layer_mass 只含 transition_high_tail/transition_low_start/short_chain/light；若 current_mass_gap 为正，则当前 Cauchy 分层未覆盖全部 L。heavy/ordinary 与 short/light 可能是父类或重叠口径，不能形式相加当作互斥分解；formal_overlap_or_gap 仅用于暴露口径不互斥或数据字段不足。",
    }

    audit = {
        "certificate_type": "D4_R5_G1_Aeff_audit",
        "status": "Aeff_not_yet_proved_unified_exceptional_candidate_available",
        "target": "证明每层 B_i <= A_i e_i，并推出全局 A_eff 足够小，使得 L >= 0.48 时有 D_* >= 0.015",
        "threshold_calculation": {
            "needed_for_Lcap_0p48_eta_0p015": "A_eff <= L/(eta + L^2/20) = 18.113...",
            "warning": "观测 A_eff 在 L=0.413 时达到 17.32，在 L>=0.42 时达到 14.92；余量很窄，粗糙 A_eff 上界很可能失败",
        },
        "floor_summaries": floor_summaries,
        "layer_worst_ratios": layer_worst,
        "mass_gap_summary": mass_gap_summary,
        "structural_issue": "分层口径已由 partition refinement 审计修正：互斥分解应为 transition + short_chain + ordinary + light = L，而 heavy 是 transition/short_chain/ordinary 的父类监控量。进一步的 unified exceptional 审计发现，可尝试用单一 exceptional_l2_sqrt 控制全体 L，扫描最坏 A_eff 约 12.69，低于 18.113；当前剩余是把该候选提升为定理并证明递归尺度传递。",
        "minimal_remaining": [
            "采用互斥层分解 P_transition/P_short/P_ordinary/P_light，使所有 B_i 精确求和为 L_j，且 heavy 只作父类监控量",
            "采用统一 exceptional 能量 E_G1:=exceptional_l2_sqrt，避免分层重复使用同一能量",
            "证明 L_j <= A_eff E_G1,j，建议以 A_eff=13 或 14 为定理化常数目标",
            "证明统一 exceptional 能量在递归尺度传递中与 stable payment telescope 兼容",
        ],
    }
    (DOCS / "d4-r5-G1-Aeff-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# D4/R5 G1 A_eff 分层 Cauchy 审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_issue"],
        "",
        "## 阈值计算",
    ]
    for key, value in audit["threshold_calculation"].items():
        lines.append(f"- `{key}`：{value}")
    lines += ["", "## L 下界分组的局部最坏 A_eff"]
    for item in floor_summaries:
        lines.append(f"- `L>={item['L_floor']}`：count={item['count']}, worst={item.get('max_A_eff_observed')}")
    lines += ["", "## 分层最坏 B/e"]
    for item in layer_worst:
        lines.append(f"- `{item['layer']}`：ratio={item['ratio']}, x={item['x']}, source={item['source']}")
    lines += ["", "## 质量缺口诊断"]
    lines.append(audit["mass_gap_summary"]["interpretation"])
    for key in ["max_current_mass_gap", "max_positive_formal_overlap_or_gap", "max_negative_formal_overlap_or_gap", "max_heavy_mass", "max_ordinary_mass"]:
        lines.append(f"- `{key}`：{audit['mass_gap_summary'][key]}")
    lines += ["", "## 最小剩余"]
    for item in audit["minimal_remaining"]:
        lines.append(f"- {item}")
    lines.append("")
    (DOCS / "d4-r5-G1-Aeff-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print(DOCS / "d4-r5-G1-Aeff-audit.json")
    print(DOCS / "d4-r5-G1-Aeff-audit.md")


if __name__ == "__main__":
    main()
