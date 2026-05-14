#!/usr/bin/env python3
"""审计 z=61 负 profile 交叉行列式的 actual/expected 分裂。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_negative_determinant_actual_expected_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.md
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
CROSS_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-determinant-actual-expected-router.md"

TARGET_BUCKET = "unbalanced<=8"
TARGET_SHELL = "(8D,16D]"
LOW_OMEGA = 3
HIGH_OMEGA = 4
EXIT_NEGATIVE_P = 10007
RECIPROCAL_NEGATIVE_P = 36739
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
TOL = 1e-10

NEXT_TARGET = "ActualHitScaleDriftBoundOrHitSupportPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_negative_determinant_actual_expected_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def cell_profile_summary(
    p_value: int,
    omega: int,
    moduli: dict[int, float],
    value_counter: dict[int, int],
) -> dict[str, Any]:
    """计算一个来源素数在目标深度格上的 actual/expected 分解。"""
    linear, model_mean, nonzero_values, max_weight, max_weight_value = profile_router.profile_linear(
        value_counter, moduli
    )
    value_count = sum(value_counter.values())
    expected = value_count * model_mean
    actual = expected + linear
    return {
        "p": p_value,
        "omega": omega,
        "value_count": value_count,
        "model_mean": model_mean,
        "actual_sum": actual,
        "expected_sum": expected,
        "linear_remainder": linear,
        "deficit_abs": expected - actual,
        "nonzero_value_count_with_multiplicity": nonzero_values,
        "nonzero_value_share": safe_ratio(nonzero_values, value_count),
        "max_weight": max_weight,
        "max_weight_value": max_weight_value,
        "actual_over_expected": safe_ratio(actual, expected),
    }


def audit() -> dict[str, Any]:
    """执行 actual/expected 分裂审计。"""
    cross_data = json.loads(CROSS_JSON.read_text(encoding="utf-8"))
    p_list = [EXIT_NEGATIVE_P, RECIPROCAL_NEGATIVE_P]
    profiles, primes = profile_router.collect_value_profiles(p_list)
    weights = attribution.selberg.selberg_weights(DEFAULT_Z, DEFAULT_D_LEVEL, primes)
    kernels = kernel_form.edge_kernel_weights(weights, DEFAULT_D_LEVEL, DEFAULT_OVERFLOW_MULTIPLIER)
    groups = weight_router.group_cell_moduli(kernels, primes, DEFAULT_D_LEVEL)

    summaries: dict[tuple[int, int], dict[str, Any]] = {}
    for omega in [LOW_OMEGA, HIGH_OMEGA]:
        moduli = groups[(TARGET_BUCKET, omega, TARGET_SHELL)]
        for p_value in p_list:
            summaries[(p_value, omega)] = cell_profile_summary(p_value, omega, moduli, profiles[p_value])

    exit_low = summaries[(EXIT_NEGATIVE_P, LOW_OMEGA)]
    exit_high = summaries[(EXIT_NEGATIVE_P, HIGH_OMEGA)]
    recip_low = summaries[(RECIPROCAL_NEGATIVE_P, LOW_OMEGA)]
    recip_high = summaries[(RECIPROCAL_NEGATIVE_P, HIGH_OMEGA)]

    a_low = exit_low["deficit_abs"]
    a_high = exit_high["deficit_abs"]
    b_low = recip_low["deficit_abs"]
    b_high = recip_high["deficit_abs"]
    determinant = a_high * b_low - a_low * b_high

    mu_low = exit_low["model_mean"]
    mu_high = exit_high["model_mean"]
    n_exit = exit_low["value_count"]
    n_recip = recip_low["value_count"]
    actual_exit_low = exit_low["actual_sum"]
    actual_exit_high = exit_high["actual_sum"]
    actual_recip_low = recip_low["actual_sum"]
    actual_recip_high = recip_high["actual_sum"]

    # 展开 (N_e mu_h-A_eh)(N_r mu_l-A_rl)-(N_e mu_l-A_el)(N_r mu_h-A_rh)；
    # 纯模型项 N_e N_r mu_h mu_l 精确抵消，剩下三项。
    recip_actual_component = n_exit * (mu_low * actual_recip_high - mu_high * actual_recip_low)
    exit_actual_component = n_recip * (mu_high * actual_exit_low - mu_low * actual_exit_high)
    actual_cross_component = actual_exit_high * actual_recip_low - actual_exit_low * actual_recip_high
    component_sum = recip_actual_component + exit_actual_component + actual_cross_component
    split_error = determinant - component_sum

    model_scale = safe_ratio(mu_high, mu_low)
    exit_actual_scale = safe_ratio(actual_exit_high, actual_exit_low)
    recip_actual_scale = safe_ratio(actual_recip_high, actual_recip_low)
    exit_actual_scale_drift = None
    recip_actual_scale_drift = None
    if model_scale is not None:
        if exit_actual_scale is not None:
            exit_actual_scale_drift = exit_actual_scale / model_scale - 1.0
        if recip_actual_scale is not None:
            recip_actual_scale_drift = recip_actual_scale / model_scale - 1.0

    normalized_denominator = b_low * b_high
    components = [
        {
            "name": "reciprocal_actual_against_common_model",
            "value": recip_actual_component,
            "share_of_determinant": safe_ratio(recip_actual_component, determinant),
            "normalized_value": safe_ratio(recip_actual_component, normalized_denominator),
        },
        {
            "name": "exit_actual_against_common_model",
            "value": exit_actual_component,
            "share_of_determinant": safe_ratio(exit_actual_component, determinant),
            "normalized_value": safe_ratio(exit_actual_component, normalized_denominator),
        },
        {
            "name": "actual_cross_correction",
            "value": actual_cross_component,
            "share_of_determinant": safe_ratio(actual_cross_component, determinant),
            "normalized_value": safe_ratio(actual_cross_component, normalized_denominator),
        },
    ]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_negative_determinant_actual_expected_router",
        "status": "z61_negative_cross_determinant_split_to_actual_expected_hit_scale_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": cross_data["certificate_type"],
        "target_bucket": TARGET_BUCKET,
        "target_shell": TARGET_SHELL,
        "low_omega": LOW_OMEGA,
        "high_omega": HIGH_OMEGA,
        "exit_negative_p": EXIT_NEGATIVE_P,
        "reciprocal_negative_p": RECIPROCAL_NEGATIVE_P,
        "model_mean_low": mu_low,
        "model_mean_high": mu_high,
        "model_scale_high_over_low": model_scale,
        "exit_actual_scale_high_over_low": exit_actual_scale,
        "reciprocal_actual_scale_high_over_low": recip_actual_scale,
        "exit_actual_scale_drift_from_model": exit_actual_scale_drift,
        "reciprocal_actual_scale_drift_from_model": recip_actual_scale_drift,
        "cross_determinant": determinant,
        "cross_determinant_source_value": cross_data["cross_determinant"],
        "cross_determinant_source_error": determinant - cross_data["cross_determinant"],
        "component_sum": component_sum,
        "actual_expected_split_error": split_error,
        "actual_expected_split_identity_closed": abs(split_error) <= TOL,
        "source_determinant_match_closed": abs(determinant - cross_data["cross_determinant"]) <= TOL,
        "normalized_cross_determinant": safe_ratio(determinant, normalized_denominator),
        "component_rows": components,
        "profile_rows": [
            exit_low,
            exit_high,
            recip_low,
            recip_high,
        ],
        "actual_hit_scale_drift_bound_proved": False,
        "hit_support_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "负 profile 交叉行列式的纯模型项完全抵消，剩余只由实际命中和模型均值之间的"
            "升阶尺度漂移决定。样本中公共模型尺度为 `mu4/mu3≈2.049869`；"
            "`10007` 的实际命中尺度低于模型约 8.72%，`36739` 的实际命中尺度高于模型约 1.53%。"
            "因此下一步最窄硬点是证明这种相反尺度漂移受控，或把持续漂移登记为 HitSupport-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 负行列式 actual/expected 分裂",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"model_scale_high_over_low={fmt_float(result['model_scale_high_over_low'])}",
        f"exit_actual_scale_high_over_low={fmt_float(result['exit_actual_scale_high_over_low'])}",
        f"reciprocal_actual_scale_high_over_low={fmt_float(result['reciprocal_actual_scale_high_over_low'])}",
        f"exit_actual_scale_drift_from_model={fmt_float(result['exit_actual_scale_drift_from_model'])}",
        f"reciprocal_actual_scale_drift_from_model={fmt_float(result['reciprocal_actual_scale_drift_from_model'])}",
        f"cross_determinant={fmt_float(result['cross_determinant'])}",
        f"actual_expected_split_error={fmt_float(result['actual_expected_split_error'])}",
        f"actual_expected_split_identity_closed={fmt_bool(result['actual_expected_split_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 四个 profile",
        "",
        "| p | omega | value count | actual | expected | deficit | nonzero share | actual/expected |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["profile_rows"]:
        lines.append(
            f"| {row['p']} | {row['omega']} | {row['value_count']} | "
            f"{fmt_float(row['actual_sum'])} | {fmt_float(row['expected_sum'])} | "
            f"{fmt_float(row['deficit_abs'])} | {fmt_float(row['nonzero_value_share'])} | "
            f"{fmt_float(row['actual_over_expected'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 行列式三项分裂",
            "",
            "纯模型项在交叉行列式中抵消，只剩两个 actual-vs-model 项和一个 actual 交叉修正项。",
            "",
            "| component | value | normalized | share of determinant |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["component_rows"]:
        lines.append(
            f"| `{row['name']}` | {fmt_float(row['value'])} | "
            f"{fmt_float(row['normalized_value'])} | {fmt_float(row['share_of_determinant'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：交叉行列式到 actual/expected 命中尺度漂移的精确分裂。",
            "- 未闭合：实际命中尺度漂移的全局上界，或 HitSupport-PDEC 排斥。",
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
                "actual_expected_split_identity_closed": result["actual_expected_split_identity_closed"],
                "exit_actual_scale_drift_from_model": result["exit_actual_scale_drift_from_model"],
                "reciprocal_actual_scale_drift_from_model": result["reciprocal_actual_scale_drift_from_model"],
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
