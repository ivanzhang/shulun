#!/usr/bin/env python3
"""把 z=61 深度格绝对预算降为 b 序列权函数偏差。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_kernel_depth_cancellation_router as depth
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router as source


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEPTH_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "DepthCellWeightFunctionDiscrepancyOrWeightSpikePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json",
    "prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def build_inputs(
    p_list: list[int], z: int, d_level: int, overflow_multiplier: int
) -> tuple[list[int], dict[str, dict[int, float]], list[int]]:
    """生成 b 多重序列和一维核。"""
    values, primes = source.collect_values_and_primes(p_list)
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    kernels = kernel_form.edge_kernel_weights(weights, d_level, overflow_multiplier)
    return values, kernels, primes


def group_cell_moduli(
    kernels: dict[str, dict[int, float]], primes: list[int], d_level: int
) -> dict[tuple[str, int, str], dict[int, float]]:
    """按 `(bucket, omega, shell)` 分组模数核。"""
    groups: dict[tuple[str, int, str], dict[int, float]] = defaultdict(dict)
    for bucket, kernel in kernels.items():
        for modulus, k_value in kernel.items():
            omega = depth.omega_squarefree(modulus, primes)
            shell = depth.shell_label(modulus, d_level)
            groups[(bucket, omega, shell)][modulus] = k_value
    return groups


def summarize_cell(
    key: tuple[str, int, str],
    moduli: dict[int, float],
    value_counter: Counter[int],
    value_count: int,
    bucket_abs: float,
) -> dict[str, Any]:
    """计算一个深度格的权函数偏差。"""
    bucket, omega, shell = key
    model_mean = sum(k_value / modulus for modulus, k_value in moduli.items())
    actual_sum = 0.0
    max_weight = 0.0
    max_weight_value = None
    nonzero_values = 0
    second_moment_sum = 0.0
    for value, multiplicity in value_counter.items():
        weight = 0.0
        for modulus, k_value in moduli.items():
            if value % modulus == 0:
                weight += k_value
        if weight > 0:
            nonzero_values += multiplicity
        if weight > max_weight:
            max_weight = weight
            max_weight_value = value
        actual_sum += multiplicity * weight
        second_moment_sum += multiplicity * weight * weight
    expected_sum = value_count * model_mean
    linear_remainder = actual_sum - expected_sum
    abs_linear = abs(linear_remainder)
    weighted_abs_upper = sum(k_value * abs(value_count // modulus - value_count / modulus) for modulus, k_value in moduli.items())
    return {
        "bucket": bucket,
        "omega": omega,
        "mobius_sign": 1 if omega % 2 == 0 else -1,
        "shell": shell,
        "modulus_count": len(moduli),
        "kernel_l1": sum(moduli.values()),
        "model_mean": model_mean,
        "actual_sum": actual_sum,
        "expected_sum": expected_sum,
        "linear_remainder": linear_remainder,
        "abs_linear_remainder": abs_linear,
        "bucket_abs_share_of_abs_linear": safe_ratio(abs_linear, bucket_abs),
        "nonzero_value_count_with_multiplicity": nonzero_values,
        "nonzero_value_share": safe_ratio(nonzero_values, value_count),
        "max_weight": max_weight,
        "max_weight_value": max_weight_value,
        "max_weight_over_abs_linear": safe_ratio(max_weight, abs_linear),
        "second_moment_mean": second_moment_sum / value_count,
        "variance_proxy": second_moment_sum / value_count - model_mean * model_mean,
        "floor_model_abs_upper_diagnostic": weighted_abs_upper,
    }


def audit(p_list: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行深度格权函数偏差审计。"""
    values, kernels, primes = build_inputs(p_list, z, d_level, overflow_multiplier)
    value_counter = Counter(values)
    groups = group_cell_moduli(kernels, primes, d_level)
    depth_data = json.loads(DEPTH_JSON.read_text(encoding="utf-8"))
    bucket_abs = {row["bucket"]: row["bucket_abs_remainder"] for row in depth_data["rows"]}
    rows = [
        summarize_cell(key, moduli, value_counter, len(values), bucket_abs[key[0]])
        for key, moduli in sorted(groups.items())
    ]
    depth_lookup = {
        (row["bucket"], cell["omega"], cell["shell"]): cell
        for row in depth_data["rows"]
        for cell in row["shell_rows"]
    }
    identity_failures = []
    for row in rows:
        key = (row["bucket"], row["omega"], row["shell"])
        expected = depth_lookup[key]["linear_remainder"]
        error = row["linear_remainder"] - expected
        row["depth_cell_linear_identity_error"] = error
        if abs(error) > 1e-8:
            identity_failures.append({"key": key, "error": error})
    top_by_bucket_contribution = sorted(
        rows, key=lambda row: row["bucket_abs_share_of_abs_linear"] or 0.0, reverse=True
    )[:16]
    top_by_spike = sorted(
        rows, key=lambda row: row["max_weight_over_abs_linear"] or 0.0, reverse=True
    )[:16]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router",
        "status": "z61_depth_cell_reduced_to_weight_function_discrepancy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "value_count": len(values),
        "distinct_value_count": len(value_counter),
        "depth_cell_weight_function_identity_closed": len(identity_failures) == 0,
        "weight_spike_diagnostic_materialized": True,
        "depth_cell_weight_function_discrepancy_proved": False,
        "weight_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "identity_failure_count": len(identity_failures),
        "cell_count": len(rows),
        "rows": rows,
        "top_cells_by_bucket_contribution": top_by_bucket_contribution,
        "top_cells_by_weight_spike_ratio": top_by_spike,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "每个深度格的线性余项已精确写成 b 多重序列上的权函数均值偏差："
            "`L_C=sum_b mult(b) W_C(b)-N sum_{m in C}K_m/m`，其中 "
            "`W_C(b)=sum_{m|b,m in C}K_m`。"
            "因此 DepthShell 预算的剩余证明不再需要同时处理所有模数；"
            "它等价于这些显式权函数没有大均值偏差，或任何失败都会表现为权重尖峰/低模相关 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 深度格权函数路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"depth_cell_weight_function_identity_closed={fmt_bool(result['depth_cell_weight_function_identity_closed'])}",
        f"weight_spike_diagnostic_materialized={fmt_bool(result['weight_spike_diagnostic_materialized'])}",
        f"depth_cell_weight_function_discrepancy_proved={fmt_bool(result['depth_cell_weight_function_discrepancy_proved'])}",
        f"weight_spike_pdec_excluded={fmt_bool(result['weight_spike_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 权函数恒等式",
        "",
        "```text",
        "W_C(b)=sum_{m|b, m in C} K_m",
        "L_C=sum_b mult(b)W_C(b)-N*sum_{m in C}K_m/m.",
        "```",
        "",
        "该恒等式逐深度格精确匹配上一层 `linear_remainder`。",
        "",
        "## 2. 最大贡献深度格",
        "",
        "| bucket | omega | shell | moduli | abs linear/bucket abs | nonzero share | max W/abs L | identity err |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["top_cells_by_bucket_contribution"]:
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | {row['modulus_count']} | "
            f"{fmt_float(row['bucket_abs_share_of_abs_linear'])} | {fmt_float(row['nonzero_value_share'])} | "
            f"{fmt_float(row['max_weight_over_abs_linear'])} | "
            f"{fmt_float(row['depth_cell_linear_identity_error'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 权重尖峰诊断",
            "",
            "| bucket | omega | shell | max W value | max W | abs linear | max W/abs L | nonzero share |",
            "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["top_cells_by_weight_spike_ratio"]:
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | "
            f"{row['max_weight_value']} | {fmt_float(row['max_weight'])} | "
            f"{fmt_float(row['abs_linear_remainder'])} | {fmt_float(row['max_weight_over_abs_linear'])} | "
            f"{fmt_float(row['nonzero_value_share'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：每个深度格余项到 b 序列权函数均值偏差的精确恒等式。",
            "- 已物化：每个深度格的非零覆盖比例、最大权重和二阶矩诊断。",
            "- 未闭合：全局证明这些权函数均值偏差满足深度预算。",
            "- 若失败：失败格给出权重尖峰或低模相关 `WeightFunction-PDEC`。",
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
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z", type=int, default=DEFAULT_Z)
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--overflow-multiplier", type=int, default=DEFAULT_OVERFLOW_MULTIPLIER)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), args.z, args.d_level, args.overflow_multiplier)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "depth_cell_weight_function_identity_closed": result[
                    "depth_cell_weight_function_identity_closed"
                ],
                "cell_count": result["cell_count"],
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
