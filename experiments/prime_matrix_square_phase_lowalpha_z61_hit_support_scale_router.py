#!/usr/bin/env python3
"""审计 z=61 actual 命中尺度漂移的支撑原子分解。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_hit_support_scale_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router as weight_router
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router as profile_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
ACTUAL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.md"

TARGET_BUCKET = "unbalanced<=8"
TARGET_SHELL = "(8D,16D]"
LOW_OMEGA = 3
HIGH_OMEGA = 4
TARGET_PRIMES = [10007, 36739]
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
TOL = 1e-10

NEXT_TARGET = "HitMultiplicityMeanWeightScaleBoundOrSupportAtomPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_hit_support_scale_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def support_atoms(
    p_value: int,
    omega: int,
    value_counter: dict[int, int],
    moduli: dict[int, float],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """物化一个 profile 的非零命中支撑原子。"""
    atoms = []
    actual_sum = 0.0
    for value, multiplicity in sorted(value_counter.items()):
        hit_moduli = [(modulus, k_value) for modulus, k_value in sorted(moduli.items()) if value % modulus == 0]
        weight = sum(k_value for _, k_value in hit_moduli)
        if weight <= 0:
            continue
        contribution = multiplicity * weight
        actual_sum += contribution
        atoms.append(
            {
                "p": p_value,
                "omega": omega,
                "b_value": value,
                "multiplicity": multiplicity,
                "weight": weight,
                "contribution": contribution,
                "hit_modulus_count": len(hit_moduli),
                "hit_moduli": [
                    {"m": modulus, "K": k_value}
                    for modulus, k_value in hit_moduli
                ],
            }
        )
    nonzero_multiplicity = sum(atom["multiplicity"] for atom in atoms)
    mean_hit_weight = safe_ratio(actual_sum, nonzero_multiplicity)
    value_count = sum(value_counter.values())
    summary = {
        "p": p_value,
        "omega": omega,
        "value_count": value_count,
        "distinct_hit_value_count": len(atoms),
        "hit_multiplicity": nonzero_multiplicity,
        "hit_multiplicity_share": safe_ratio(nonzero_multiplicity, value_count),
        "actual_sum": actual_sum,
        "mean_hit_weight": mean_hit_weight,
        "max_atom_contribution": max((atom["contribution"] for atom in atoms), default=0.0),
        "max_atom_share_of_actual": safe_ratio(max((atom["contribution"] for atom in atoms), default=0.0), actual_sum),
    }
    return summary, atoms


def audit() -> dict[str, Any]:
    """执行命中支撑尺度审计。"""
    actual_data = json.loads(ACTUAL_JSON.read_text(encoding="utf-8"))
    profiles, primes = profile_router.collect_value_profiles(TARGET_PRIMES)
    weights = attribution.selberg.selberg_weights(DEFAULT_Z, DEFAULT_D_LEVEL, primes)
    kernels = kernel_form.edge_kernel_weights(weights, DEFAULT_D_LEVEL, DEFAULT_OVERFLOW_MULTIPLIER)
    groups = weight_router.group_cell_moduli(kernels, primes, DEFAULT_D_LEVEL)

    summary_rows = []
    atom_rows = []
    summary_by_key: dict[tuple[int, int], dict[str, Any]] = {}
    for p_value in TARGET_PRIMES:
        for omega in [LOW_OMEGA, HIGH_OMEGA]:
            moduli = groups[(TARGET_BUCKET, omega, TARGET_SHELL)]
            summary, atoms = support_atoms(p_value, omega, profiles[p_value], moduli)
            summary_rows.append(summary)
            atom_rows.extend(atoms)
            summary_by_key[(p_value, omega)] = summary

    scale_rows = []
    max_identity_error = 0.0
    for p_value in TARGET_PRIMES:
        low = summary_by_key[(p_value, LOW_OMEGA)]
        high = summary_by_key[(p_value, HIGH_OMEGA)]
        hit_scale = safe_ratio(high["hit_multiplicity"], low["hit_multiplicity"])
        mean_weight_scale = safe_ratio(high["mean_hit_weight"], low["mean_hit_weight"])
        actual_scale = safe_ratio(high["actual_sum"], low["actual_sum"])
        product_scale = None if hit_scale is None or mean_weight_scale is None else hit_scale * mean_weight_scale
        identity_error = None if actual_scale is None or product_scale is None else actual_scale - product_scale
        if identity_error is not None:
            max_identity_error = max(max_identity_error, abs(identity_error))
        model_scale = actual_data["model_scale_high_over_low"]
        drift = None if actual_scale is None else actual_scale / model_scale - 1.0
        scale_rows.append(
            {
                "p": p_value,
                "low_hit_multiplicity": low["hit_multiplicity"],
                "high_hit_multiplicity": high["hit_multiplicity"],
                "hit_multiplicity_scale": hit_scale,
                "low_mean_hit_weight": low["mean_hit_weight"],
                "high_mean_hit_weight": high["mean_hit_weight"],
                "mean_hit_weight_scale": mean_weight_scale,
                "actual_scale_high_over_low": actual_scale,
                "product_scale": product_scale,
                "scale_factor_identity_error": identity_error,
                "model_scale_high_over_low": model_scale,
                "actual_scale_drift_from_model": drift,
            }
        )

    top_atoms = sorted(atom_rows, key=lambda row: row["contribution"], reverse=True)[:24]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_hit_support_scale_router",
        "status": "z61_actual_hit_scale_drift_reduced_to_support_count_and_mean_weight_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": actual_data["certificate_type"],
        "target_bucket": TARGET_BUCKET,
        "target_shell": TARGET_SHELL,
        "low_omega": LOW_OMEGA,
        "high_omega": HIGH_OMEGA,
        "target_primes": TARGET_PRIMES,
        "support_summary_rows": summary_rows,
        "scale_decomposition_rows": scale_rows,
        "support_atom_count": len(atom_rows),
        "top_support_atoms": top_atoms,
        "support_scale_identity_closed": max_identity_error <= TOL,
        "max_scale_factor_identity_error": max_identity_error,
        "hit_multiplicity_mean_weight_scale_bound_proved": False,
        "support_atom_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "actual 命中尺度已无损拆成 `命中重数升阶 * 命中平均权重升阶`。"
            "`10007` 从 omega=3 到 4 的命中重数由 `1` 到 `2`，但平均命中权重下降，"
            "所以实际尺度低于公共模型尺度；`36739` 的命中重数由 `20` 到 `31`，"
            "同时平均命中权重上升，因此实际尺度略高于公共模型尺度。"
            "下一步只需控制这两个支撑因子的相对漂移，或把持续异常登记为 SupportAtom-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 命中支撑尺度路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"support_atom_count={result['support_atom_count']}",
        f"support_scale_identity_closed={fmt_bool(result['support_scale_identity_closed'])}",
        f"max_scale_factor_identity_error={fmt_float(result['max_scale_factor_identity_error'])}",
        f"hit_multiplicity_mean_weight_scale_bound_proved={fmt_bool(result['hit_multiplicity_mean_weight_scale_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 支撑汇总",
        "",
        "| p | omega | hits | hit share | actual | mean hit weight | max atom share |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["support_summary_rows"]:
        lines.append(
            f"| {row['p']} | {row['omega']} | {row['hit_multiplicity']} | "
            f"{fmt_float(row['hit_multiplicity_share'])} | {fmt_float(row['actual_sum'])} | "
            f"{fmt_float(row['mean_hit_weight'])} | {fmt_float(row['max_atom_share_of_actual'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 尺度分解",
            "",
            "| p | hit scale | mean weight scale | product | actual scale | model scale | drift |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["scale_decomposition_rows"]:
        lines.append(
            f"| {row['p']} | {fmt_float(row['hit_multiplicity_scale'])} | "
            f"{fmt_float(row['mean_hit_weight_scale'])} | {fmt_float(row['product_scale'])} | "
            f"{fmt_float(row['actual_scale_high_over_low'])} | "
            f"{fmt_float(row['model_scale_high_over_low'])} | "
            f"{fmt_float(row['actual_scale_drift_from_model'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最大支撑原子",
            "",
            "| p | omega | b | mult | weight | contribution | hit moduli |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["top_support_atoms"]:
        lines.append(
            f"| {row['p']} | {row['omega']} | {row['b_value']} | {row['multiplicity']} | "
            f"{fmt_float(row['weight'])} | {fmt_float(row['contribution'])} | "
            f"{row['hit_modulus_count']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：actual 尺度漂移到支撑重数与平均权重两因子的精确分解。",
            "- 未闭合：支撑重数/平均权重相对漂移的全局上界，或 SupportAtom-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "support_scale_identity_closed": result["support_scale_identity_closed"],
                "support_atom_count": result["support_atom_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
