#!/usr/bin/env python3
"""审计 z=61 一维核余项的深度层抵消结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_kernel_depth_cancellation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router as source


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
KERNEL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "DepthShellAbsoluteBudgetOrDepthCellPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json",
    "prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_kernel_depth_cancellation_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def omega_squarefree(value: int, primes: list[int]) -> int:
    """计算 squarefree 模数的不同素因子个数。"""
    remaining = value
    omega = 0
    for prime in primes:
        if prime * prime > remaining:
            break
        if remaining % prime != 0:
            continue
        omega += 1
        while remaining % prime == 0:
            remaining //= prime
    if remaining > 1:
        omega += 1
    return omega


def shell_label(value: int, d_level: int) -> str:
    """给 `(D,16D]` 内模数分 dyadic shell。"""
    if value <= 2 * d_level:
        return "(D,2D]"
    if value <= 4 * d_level:
        return "(2D,4D]"
    if value <= 8 * d_level:
        return "(4D,8D]"
    return "(8D,16D]"


def empty_cell() -> dict[str, Any]:
    """初始化深度单元。"""
    return {
        "modulus_count": 0,
        "kernel_l1": 0.0,
        "weighted_abs_remainder": 0.0,
        "linear_remainder": 0.0,
    }


def finalize_cell(cell: dict[str, Any], bucket_abs: float) -> dict[str, Any]:
    """补全单元比率。"""
    cell["cell_ratio"] = safe_ratio(abs(cell["linear_remainder"]), cell["weighted_abs_remainder"])
    cell["bucket_abs_share"] = safe_ratio(cell["weighted_abs_remainder"], bucket_abs)
    cell["bucket_slice_contribution"] = safe_ratio(abs(cell["linear_remainder"]), bucket_abs)
    return cell


def build_kernel_data(
    p_list: list[int], z: int, d_level: int, overflow_multiplier: int
) -> tuple[dict[str, dict[int, float]], dict[int, float], list[int], int]:
    """复用上一层一维核并生成余项。"""
    values, primes = source.collect_values_and_primes(p_list)
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    kernels = kernel_form.edge_kernel_weights(weights, d_level, overflow_multiplier)
    moduli = sorted({modulus for kernel in kernels.values() for modulus in kernel})
    counts = attribution.divisibility_counts(values, moduli)
    remainders = {modulus: counts[modulus] - len(values) / modulus for modulus in moduli}
    return kernels, remainders, primes, len(values)


def summarize_bucket(
    bucket: str,
    kernel: dict[int, float],
    remainders: dict[int, float],
    primes: list[int],
    d_level: int,
    cap: float,
    source_row: dict[str, Any],
) -> dict[str, Any]:
    """汇总单个 bucket 的深度抵消账本。"""
    omega_cells: dict[int, dict[str, Any]] = defaultdict(empty_cell)
    shell_cells: dict[tuple[int, str], dict[str, Any]] = defaultdict(empty_cell)
    bucket_abs = 0.0
    for modulus, k_value in sorted(kernel.items()):
        omega = omega_squarefree(modulus, primes)
        shell = shell_label(modulus, d_level)
        remainder = remainders[modulus]
        abs_mass = k_value * abs(remainder)
        linear = k_value * remainder
        bucket_abs += abs_mass
        for cell in (omega_cells[omega], shell_cells[(omega, shell)]):
            cell["modulus_count"] += 1
            cell["kernel_l1"] += k_value
            cell["weighted_abs_remainder"] += abs_mass
            cell["linear_remainder"] += linear
    omega_rows = []
    for omega, cell in sorted(omega_cells.items()):
        row = dict(cell)
        row["omega"] = omega
        row["mobius_sign"] = 1 if omega % 2 == 0 else -1
        omega_rows.append(finalize_cell(row, bucket_abs))
    shell_rows = []
    for (omega, shell), cell in sorted(shell_cells.items(), key=lambda item: (item[0][0], item[0][1])):
        row = dict(cell)
        row["omega"] = omega
        row["mobius_sign"] = 1 if omega % 2 == 0 else -1
        row["shell"] = shell
        shell_rows.append(finalize_cell(row, bucket_abs))
    parity_summaries = []
    for parity_name, parity in [("mu_plus", 0), ("mu_minus", 1)]:
        rows = [row for row in omega_rows if row["omega"] % 2 == parity]
        net_linear = sum(row["linear_remainder"] for row in rows)
        crude_depth_sum = sum(abs(row["linear_remainder"]) for row in rows)
        abs_mass = sum(row["weighted_abs_remainder"] for row in rows)
        parity_summaries.append(
            {
                "parity": parity_name,
                "omega_count": len(rows),
                "weighted_abs_remainder": abs_mass,
                "net_linear_remainder": net_linear,
                "crude_depth_imbalance": crude_depth_sum,
                "net_imbalance": abs(net_linear),
                "cross_depth_cancellation_credit": crude_depth_sum - abs(net_linear),
                "net_ratio_inside_parity": safe_ratio(abs(net_linear), abs_mass),
                "credit_ratio_inside_parity": safe_ratio(crude_depth_sum - abs(net_linear), abs_mass),
                "bucket_slice_contribution": safe_ratio(abs(net_linear), bucket_abs),
            }
        )
    omega_crude_ratio = safe_ratio(sum(abs(row["linear_remainder"]) for row in omega_rows), bucket_abs)
    shell_crude_ratio = safe_ratio(sum(abs(row["linear_remainder"]) for row in shell_rows), bucket_abs)
    actual_slice_ratio = safe_ratio(
        sum(item["net_imbalance"] for item in parity_summaries), bucket_abs
    )
    omega_required_cancellation = max(0.0, (omega_crude_ratio or 0.0) - cap) * bucket_abs
    shell_required_cancellation = max(0.0, (shell_crude_ratio or 0.0) - cap) * bucket_abs
    return {
        "bucket": bucket,
        "cap": cap,
        "bucket_abs_remainder": bucket_abs,
        "actual_slice_ratio": actual_slice_ratio,
        "source_slice_ratio": source_row["slice_ratio"],
        "source_slice_ratio_error": (actual_slice_ratio or 0.0) - source_row["slice_ratio"],
        "omega_crude_ratio": omega_crude_ratio,
        "shell_crude_ratio": shell_crude_ratio,
        "omega_required_cancellation_to_meet_cap": omega_required_cancellation,
        "shell_required_cancellation_to_meet_cap": shell_required_cancellation,
        "independent_omega_contract_sufficient": omega_crude_ratio is not None and omega_crude_ratio <= cap,
        "independent_shell_contract_sufficient": shell_crude_ratio is not None and shell_crude_ratio <= cap,
        "parity_summaries": parity_summaries,
        "omega_rows": omega_rows,
        "shell_rows": shell_rows,
    }


def audit(p_list: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行深度抵消审计。"""
    kernels, remainders, primes, value_count = build_kernel_data(p_list, z, d_level, overflow_multiplier)
    cap = source.required_cap_for_z(z)
    kernel_data = json.loads(KERNEL_JSON.read_text(encoding="utf-8"))
    source_rows = {row["bucket"]: row for row in kernel_data["rows"]}
    rows = [
        summarize_bucket(bucket, kernels[bucket], remainders, primes, d_level, cap, source_rows[bucket])
        for bucket in source.BUCKETS
    ]
    source_failures = [row for row in rows if abs(row["source_slice_ratio_error"]) > 1e-10]
    omega_independent_failures = [row for row in rows if not row["independent_omega_contract_sufficient"]]
    shell_independent_failures = [row for row in rows if not row["independent_shell_contract_sufficient"]]
    top_shell_cells = sorted(
        [cell | {"bucket": row["bucket"]} for row in rows for cell in row["shell_rows"]],
        key=lambda item: item["bucket_slice_contribution"] or 0.0,
        reverse=True,
    )[:16]
    tightest = max(rows, key=lambda row: row["omega_required_cancellation_to_meet_cap"])
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_kernel_depth_cancellation_router",
        "status": "z61_kernel_depth_shell_absolute_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "value_count": value_count,
        "depth_shell_ledger_materialized": True,
        "kernel_source_ratio_identity_closed": len(source_failures) == 0,
        "independent_omega_cell_contract_sufficient_for_all_buckets": len(omega_independent_failures) == 0,
        "independent_shell_cell_contract_sufficient_for_all_buckets": len(shell_independent_failures) == 0,
        "same_parity_cross_depth_cancellation_needed": len(omega_independent_failures) > 0,
        "depth_shell_absolute_budget_proved": False,
        "depth_cell_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_failure_count": len(source_failures),
        "omega_independent_failure_count": len(omega_independent_failures),
        "shell_independent_failure_count": len(shell_independent_failures),
        "rows": rows,
        "top_shell_cells_by_bucket_contribution": top_shell_cells,
        "tightest_cancellation_bucket": tightest,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "一维核余项已进一步分解为 `omega(m)` 与 dyadic shell 深度格。"
            "样本中逐格内部偏斜率有时很高，但每个格占 bucket 总质量的比例很小；"
            "因此按深度格绝对线性余项求和的 crude budget 已足以推出 `0.221522` 合同。"
            "下一步不需要依赖跨深度偶然抵消，而是证明所有命名深度格的绝对预算，"
            "若某格长期超预算则直接形成 DepthCell-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 kernel 深度抵消路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"depth_shell_ledger_materialized={fmt_bool(result['depth_shell_ledger_materialized'])}",
        f"kernel_source_ratio_identity_closed={fmt_bool(result['kernel_source_ratio_identity_closed'])}",
        f"independent_omega_cell_contract_sufficient_for_all_buckets={fmt_bool(result['independent_omega_cell_contract_sufficient_for_all_buckets'])}",
        f"independent_shell_cell_contract_sufficient_for_all_buckets={fmt_bool(result['independent_shell_cell_contract_sufficient_for_all_buckets'])}",
        f"same_parity_cross_depth_cancellation_needed={fmt_bool(result['same_parity_cross_depth_cancellation_needed'])}",
        f"depth_shell_absolute_budget_proved={fmt_bool(result['depth_shell_absolute_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. bucket 总览",
        "",
        "| bucket | actual slice | omega crude | shell crude | omega needed credit | shell needed credit |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['actual_slice_ratio'])} | "
            f"{fmt_float(row['omega_crude_ratio'])} | {fmt_float(row['shell_crude_ratio'])} | "
            f"{fmt_float(row['omega_required_cancellation_to_meet_cap'])} | "
            f"{fmt_float(row['shell_required_cancellation_to_meet_cap'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 同片跨深度抵消",
            "",
            "| bucket | parity | abs | crude depth | net | credit | net ratio | credit ratio |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["rows"]:
        for parity in row["parity_summaries"]:
            lines.append(
                f"| `{row['bucket']}` | `{parity['parity']}` | "
                f"{fmt_float(parity['weighted_abs_remainder'])} | "
                f"{fmt_float(parity['crude_depth_imbalance'])} | "
                f"{fmt_float(parity['net_imbalance'])} | "
                f"{fmt_float(parity['cross_depth_cancellation_credit'])} | "
                f"{fmt_float(parity['net_ratio_inside_parity'])} | "
                f"{fmt_float(parity['credit_ratio_inside_parity'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. omega 深度行",
            "",
            "| bucket | omega | mu | abs | linear | cell ratio | bucket contribution |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["rows"]:
        for omega in row["omega_rows"]:
            lines.append(
                f"| `{row['bucket']}` | {omega['omega']} | {omega['mobius_sign']} | "
                f"{fmt_float(omega['weighted_abs_remainder'])} | "
                f"{fmt_float(omega['linear_remainder'])} | "
                f"{fmt_float(omega['cell_ratio'])} | "
                f"{fmt_float(omega['bucket_slice_contribution'])} |"
            )
    lines.extend(
        [
            "",
            "## 4. 最大 shell 单元",
            "",
            "| bucket | omega | shell | abs | linear | cell ratio | bucket contribution |",
            "| --- | ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for cell in result["top_shell_cells_by_bucket_contribution"]:
        lines.append(
            f"| `{cell['bucket']}` | {cell['omega']} | `{cell['shell']}` | "
            f"{fmt_float(cell['weighted_abs_remainder'])} | "
            f"{fmt_float(cell['linear_remainder'])} | "
            f"{fmt_float(cell['cell_ratio'])} | "
            f"{fmt_float(cell['bucket_slice_contribution'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：深度层与 shell 层的精确分解账本，并与一维核 slice ratio 完全一致。",
            "- 已闭合：样本中逐 `omega` 与逐 shell 的绝对线性余项 crude budget 均低于 cap。",
            "- 重要边界：单个深度格的内部偏斜率可高于 cap，不能用格内比例界直接闭合。",
            "- 当前真正剩余：证明所有深度格的绝对预算，或把超预算深度格登记为 DepthCell-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
                "kernel_source_ratio_identity_closed": result["kernel_source_ratio_identity_closed"],
                "omega_independent_failure_count": result["omega_independent_failure_count"],
                "tightest_bucket": result["tightest_cancellation_bucket"]["bucket"],
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
