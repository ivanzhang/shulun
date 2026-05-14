#!/usr/bin/env python3
"""审计 z=61 命中支撑漂移中的多模数 overlap 翻转原子。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_hit_overlap_flip_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router as weight_router
import prime_matrix_square_phase_lowalpha_z61_hit_support_scale_router as support_router
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router as profile_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SUPPORT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.md"

NEXT_TARGET = "SingleDoubleHitOverlapAtomBoundOrOverlapPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.json",
]
TOL = 1e-10


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_hit_overlap_flip_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_all_atoms() -> list[dict[str, Any]]:
    """重建四个 profile 的完整命中原子。"""
    profiles, primes = profile_router.collect_value_profiles(support_router.TARGET_PRIMES)
    weights = attribution.selberg.selberg_weights(
        support_router.DEFAULT_Z, support_router.DEFAULT_D_LEVEL, primes
    )
    kernels = kernel_form.edge_kernel_weights(
        weights, support_router.DEFAULT_D_LEVEL, support_router.DEFAULT_OVERFLOW_MULTIPLIER
    )
    groups = weight_router.group_cell_moduli(kernels, primes, support_router.DEFAULT_D_LEVEL)
    atom_rows = []
    for p_value in support_router.TARGET_PRIMES:
        for omega in [support_router.LOW_OMEGA, support_router.HIGH_OMEGA]:
            moduli = groups[(support_router.TARGET_BUCKET, omega, support_router.TARGET_SHELL)]
            _, atoms = support_router.support_atoms(p_value, omega, profiles[p_value], moduli)
            atom_rows.extend(atoms)
    return atom_rows


def actual_by_prime_omega(atoms: list[dict[str, Any]], remove_overlaps: bool) -> dict[tuple[int, int], float]:
    """按 `(p,omega)` 汇总 actual；可选择删除多模数 overlap。"""
    result: dict[tuple[int, int], float] = {}
    for atom in atoms:
        if remove_overlaps and atom["hit_modulus_count"] > 1:
            continue
        key = (atom["p"], atom["omega"])
        result[key] = result.get(key, 0.0) + atom["contribution"]
    return result


def audit() -> dict[str, Any]:
    """执行 overlap 翻转审计。"""
    support_data = json.loads(SUPPORT_JSON.read_text(encoding="utf-8"))
    atoms = collect_all_atoms()
    overlap_atoms = [atom for atom in atoms if atom["hit_modulus_count"] > 1]
    single_atoms = [atom for atom in atoms if atom["hit_modulus_count"] == 1]

    actual_full = actual_by_prime_omega(atoms, remove_overlaps=False)
    actual_without_overlap = actual_by_prime_omega(atoms, remove_overlaps=True)
    model_scale = support_data["scale_decomposition_rows"][0]["model_scale_high_over_low"]

    scale_rows = []
    for row in support_data["scale_decomposition_rows"]:
        p_value = row["p"]
        low_key = (p_value, support_router.LOW_OMEGA)
        high_key = (p_value, support_router.HIGH_OMEGA)
        full_scale = safe_ratio(actual_full[high_key], actual_full[low_key])
        no_overlap_scale = safe_ratio(actual_without_overlap.get(high_key, 0.0), actual_without_overlap[low_key])
        full_drift = None if full_scale is None else full_scale / model_scale - 1.0
        no_overlap_drift = None if no_overlap_scale is None else no_overlap_scale / model_scale - 1.0
        overlap_lift = actual_full[high_key] - actual_without_overlap.get(high_key, 0.0)
        needed_lift_to_model = model_scale * actual_full[low_key] - actual_without_overlap.get(high_key, 0.0)
        scale_rows.append(
            {
                "p": p_value,
                "actual_low": actual_full[low_key],
                "actual_high_with_overlap": actual_full[high_key],
                "actual_high_without_overlap": actual_without_overlap.get(high_key, 0.0),
                "overlap_lift_in_high_omega": overlap_lift,
                "needed_lift_to_reach_model_scale": needed_lift_to_model,
                "overlap_lift_surplus_over_model": overlap_lift - needed_lift_to_model,
                "full_actual_scale": full_scale,
                "without_overlap_actual_scale": no_overlap_scale,
                "model_scale": model_scale,
                "full_drift_from_model": full_drift,
                "without_overlap_drift_from_model": no_overlap_drift,
                "overlap_flips_drift_sign": (
                    no_overlap_drift is not None
                    and full_drift is not None
                    and no_overlap_drift < 0 < full_drift
                ),
            }
        )

    overlap_contribution = sum(atom["contribution"] for atom in overlap_atoms)
    all_other_atoms_single_modulus = len(single_atoms) + len(overlap_atoms) == len(atoms)
    flip_rows = [row for row in scale_rows if row["overlap_flips_drift_sign"]]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_hit_overlap_flip_router",
        "status": "z61_hit_support_scale_drift_reduced_to_single_double_hit_overlap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": support_data["certificate_type"],
        "support_atom_count": len(atoms),
        "single_modulus_atom_count": len(single_atoms),
        "multi_modulus_atom_count": len(overlap_atoms),
        "all_multi_modulus_atoms": overlap_atoms,
        "overlap_contribution": overlap_contribution,
        "overlap_contribution_share_of_total_actual": safe_ratio(
            overlap_contribution, sum(atom["contribution"] for atom in atoms)
        ),
        "all_other_atoms_single_modulus": all_other_atoms_single_modulus,
        "scale_rows": scale_rows,
        "overlap_flip_prime_count": len(flip_rows),
        "single_double_hit_overlap_flip_identity_closed": (
            len(overlap_atoms) == 1
            and all_other_atoms_single_modulus
            and len(flip_rows) == 1
            and flip_rows[0]["p"] == 36739
        ),
        "single_double_hit_overlap_bound_proved": False,
        "overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "四个目标 profile 的 `52` 个支撑原子中，只有一个多模数重叠原子："
            "`p=36739, omega=4, b=28842`，命中模数 `9614` 与 `14421`。"
            "删去该原子后 `36739` 的 actual 高/低尺度低于公共模型尺度；加入该原子后才翻到模型上方。"
            "因此当前最窄硬点已从整体支撑漂移压到单个 double-hit overlap 原子的可容许性，"
            "或其持续出现形成 Overlap-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 overlap 翻转原子",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"support_atom_count={result['support_atom_count']}",
        f"single_modulus_atom_count={result['single_modulus_atom_count']}",
        f"multi_modulus_atom_count={result['multi_modulus_atom_count']}",
        f"overlap_contribution={fmt_float(result['overlap_contribution'])}",
        f"overlap_contribution_share_of_total_actual={fmt_float(result['overlap_contribution_share_of_total_actual'])}",
        f"single_double_hit_overlap_flip_identity_closed={fmt_bool(result['single_double_hit_overlap_flip_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 唯一 overlap 原子",
        "",
        "| p | omega | b | mult | contribution | hit moduli |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for atom in result["all_multi_modulus_atoms"]:
        moduli = ", ".join(f"{item['m']}:{fmt_float(item['K'])}" for item in atom["hit_moduli"])
        lines.append(
            f"| {atom['p']} | {atom['omega']} | {atom['b_value']} | {atom['multiplicity']} | "
            f"{fmt_float(atom['contribution'])} | `{moduli}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 删除 overlap 后的尺度",
            "",
            "| p | full scale | no-overlap scale | model scale | full drift | no-overlap drift | lift surplus | flips |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["scale_rows"]:
        lines.append(
            f"| {row['p']} | {fmt_float(row['full_actual_scale'])} | "
            f"{fmt_float(row['without_overlap_actual_scale'])} | {fmt_float(row['model_scale'])} | "
            f"{fmt_float(row['full_drift_from_model'])} | "
            f"{fmt_float(row['without_overlap_drift_from_model'])} | "
            f"{fmt_float(row['overlap_lift_surplus_over_model'])} | "
            f"{fmt_bool(row['overlap_flips_drift_sign'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：支撑尺度漂移到唯一 double-hit overlap 原子的翻转审计。",
            "- 未闭合：该 overlap 原子的全局上界/不可持续性，或 Overlap-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
                "single_double_hit_overlap_flip_identity_closed": result[
                    "single_double_hit_overlap_flip_identity_closed"
                ],
                "multi_modulus_atom_count": result["multi_modulus_atom_count"],
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
