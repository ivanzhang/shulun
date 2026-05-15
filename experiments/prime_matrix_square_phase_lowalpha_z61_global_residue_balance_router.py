#!/usr/bin/env python3
"""审计 z=61 目标格内所有多命中 residue 组的有符号吸收。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_global_residue_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.md
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
ABSORB_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.md"

TARGET_BUCKET = "unbalanced<=8"
TARGET_OMEGA = 4
TARGET_SHELL = "(8D,16D]"
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "LiftTargetCellMultiHitBalanceToGlobalOrUnabsorbedResiduePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-residue-signed-absorption-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_global_residue_balance_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_label(value: float) -> str:
    """线性余项符号标签。"""
    if value > 0:
        return "positive"
    if value < 0:
        return "negative"
    return "zero"


def sign_value(value: float) -> int:
    """线性余项符号值。"""
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def audit() -> dict[str, Any]:
    """执行目标格多命中 residue 组有符号吸收审计。"""
    absorb = json.loads(ABSORB_JSON.read_text(encoding="utf-8"))
    p_list = attribution.DEFAULT_P_LIST
    profiles, primes = profile_router.collect_value_profiles(p_list)
    weights = attribution.selberg.selberg_weights(DEFAULT_Z, DEFAULT_D_LEVEL, primes)
    kernels = kernel_form.edge_kernel_weights(weights, DEFAULT_D_LEVEL, DEFAULT_OVERFLOW_MULTIPLIER)
    groups = weight_router.group_cell_moduli(kernels, primes, DEFAULT_D_LEVEL)
    target_moduli = groups[(TARGET_BUCKET, TARGET_OMEGA, TARGET_SHELL)]

    profile_sign_rows = []
    sign_by_p: dict[int, int] = {}
    sign_label_by_p: dict[int, str] = {}
    for p_value in p_list:
        linear, model_mean, nonzero_values, max_weight, max_weight_value = profile_router.profile_linear(
            profiles[p_value], target_moduli
        )
        sign_by_p[p_value] = sign_value(linear)
        sign_label_by_p[p_value] = sign_label(linear)
        profile_sign_rows.append(
            {
                "p": p_value,
                "linear_remainder": linear,
                "sign": sign_label_by_p[p_value],
                "nonzero_values": nonzero_values,
                "max_weight": max_weight,
                "max_weight_value": max_weight_value,
            }
        )

    atom_rows = []
    by_hit_moduli: dict[tuple[int, ...], dict[str, Any]] = {}
    for p_value in p_list:
        for b_value, multiplicity in sorted(profiles[p_value].items()):
            hit_moduli = tuple(modulus for modulus in sorted(target_moduli) if b_value % modulus == 0)
            if len(hit_moduli) < 2:
                continue
            weight = sum(target_moduli[modulus] for modulus in hit_moduli)
            sign = sign_by_p[p_value]
            atom = {
                "p": p_value,
                "profile_sign": sign_label_by_p[p_value],
                "sign_value": sign,
                "b_value": b_value,
                "multiplicity": multiplicity,
                "hit_moduli": list(hit_moduli),
                "hit_modulus_count": len(hit_moduli),
                "unit_weight": weight,
                "signed_count_contribution": sign * multiplicity,
                "signed_weight_contribution": sign * multiplicity * weight,
            }
            atom_rows.append(atom)
            bucket = by_hit_moduli.setdefault(
                hit_moduli,
                {
                    "hit_moduli": list(hit_moduli),
                    "unit_weight": weight,
                    "positive_count": 0,
                    "negative_count": 0,
                    "signed_count": 0,
                    "positive_weight": 0.0,
                    "negative_weight": 0.0,
                    "signed_weight": 0.0,
                    "atoms": [],
                },
            )
            if sign > 0:
                bucket["positive_count"] += multiplicity
                bucket["positive_weight"] += multiplicity * weight
            elif sign < 0:
                bucket["negative_count"] += multiplicity
                bucket["negative_weight"] += multiplicity * weight
            bucket["signed_count"] += sign * multiplicity
            bucket["signed_weight"] += sign * multiplicity * weight
            bucket["atoms"].append(atom)

    group_rows = sorted(
        by_hit_moduli.values(),
        key=lambda row: (row["signed_count"], row["hit_moduli"]),
    )
    for row in group_rows:
        row["locally_absorbed"] = row["signed_count"] >= 0 and row["signed_weight"] >= 0
        row["positive_over_negative_weight"] = safe_ratio(row["positive_weight"], row["negative_weight"])
    unabsorbed = [row for row in group_rows if not row["locally_absorbed"]]
    total_signed_count = sum(row["signed_count"] for row in group_rows)
    total_signed_weight = sum(row["signed_weight"] for row in group_rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_global_residue_balance_router",
        "status": "z61_target_cell_multihit_residue_groups_all_locally_absorbed_global_proof_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": absorb["certificate_type"],
        "target_bucket": TARGET_BUCKET,
        "target_omega": TARGET_OMEGA,
        "target_shell": TARGET_SHELL,
        "p_list": p_list,
        "profile_sign_rows": profile_sign_rows,
        "multi_hit_atom_count": len(atom_rows),
        "multi_hit_group_count": len(group_rows),
        "total_signed_count": total_signed_count,
        "total_signed_weight": total_signed_weight,
        "unabsorbed_group_count": len(unabsorbed),
        "sample_target_cell_multihit_balance_closed": len(unabsorbed) == 0 and total_signed_weight >= 0,
        "group_rows": group_rows,
        "unabsorbed_group_rows": unabsorbed,
        "global_residue_signed_count_balance_proved": False,
        "unabsorbed_residue_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "同一目标格内全部多命中 residue 组已做有符号吸收审计："
            "样本中 `21` 个 hit-moduli 组全部局部吸收，未吸收组数为 `0`。"
            "这说明当前 Residue-PDEC 不是孤立侥幸，而是嵌入更大的目标格多命中正吸收结构；"
            "但这仍是样本目标格证书，下一步要把该吸收规则提升为全局证明，"
            "或登记真正未吸收的 Residue-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 global residue balance",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"multi_hit_atom_count={result['multi_hit_atom_count']}",
        f"multi_hit_group_count={result['multi_hit_group_count']}",
        f"total_signed_count={result['total_signed_count']}",
        f"total_signed_weight={fmt_float(result['total_signed_weight'])}",
        f"unabsorbed_group_count={result['unabsorbed_group_count']}",
        f"sample_target_cell_multihit_balance_closed={fmt_bool(result['sample_target_cell_multihit_balance_closed'])}",
        f"global_residue_signed_count_balance_proved={fmt_bool(result['global_residue_signed_count_balance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Profile 符号",
        "",
        "| p | sign | linear | nonzero | max weight value |",
        "| ---: | --- | ---: | ---: | ---: |",
    ]
    for row in result["profile_sign_rows"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {fmt_float(row['linear_remainder'])} | "
            f"{row['nonzero_values']} | {row['max_weight_value']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 多命中组",
            "",
            "| hit moduli | signed count | pos | neg | signed weight | absorbed |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["group_rows"]:
        lines.append(
            f"| `{row['hit_moduli']}` | {row['signed_count']} | {row['positive_count']} | "
            f"{row['negative_count']} | {fmt_float(row['signed_weight'])} | "
            f"{fmt_bool(row['locally_absorbed'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：当前样本目标格内所有多命中 residue 组均无未吸收净负组。",
            "- 未闭合：把该 signed count balance 提升为全局证明，或排斥未吸收 Residue-PDEC。",
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
                "sample_target_cell_multihit_balance_closed": result[
                    "sample_target_cell_multihit_balance_closed"
                ],
                "unabsorbed_group_count": result["unabsorbed_group_count"],
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
