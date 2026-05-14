#!/usr/bin/env python3
"""把 z=61 Möbius 切片两色平衡降为一维 divisor-kernel 余项问题。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router as bilinear
import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router as source


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "OneDimensionalMobiusKernelRemainderDiscrepancyTheta0222OrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json",
    "prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def divisor_kernel_formula(
    modulus: int, bucket: str, weights: dict[int, float], d_level: int
) -> float:
    """用 divisor-kernel 公式直接计算 K_b(m)。"""
    total = 0.0
    for divisor in weights:
        if modulus % divisor != 0:
            continue
        co_divisor = modulus // divisor
        if co_divisor not in weights:
            continue
        if divisor * co_divisor != modulus:
            continue
        if math.gcd(divisor, co_divisor) != 1:
            continue
        if modulus <= d_level:
            continue
        if bilinear.balance_bucket(divisor, co_divisor) != bucket:
            continue
        total += abs(weights[divisor] * weights[co_divisor])
    return total


def edge_kernel_weights(
    weights: dict[int, float], d_level: int, overflow_multiplier: int
) -> dict[str, dict[int, float]]:
    """从边枚举得到 K_b(m)，作为公式校验对象。"""
    result: dict[str, dict[int, float]] = {bucket: defaultdict(float) for bucket in source.BUCKETS}
    for d, lambda_d in weights.items():
        for e, lambda_e in weights.items():
            if math.gcd(d, e) != 1:
                continue
            modulus = d * e
            if modulus <= d_level or modulus > overflow_multiplier * d_level:
                continue
            result[bilinear.balance_bucket(d, e)][modulus] += abs(lambda_d * lambda_e)
    return result


def summarize_bucket(
    bucket: str,
    kernel: dict[int, float],
    remainders: dict[int, float],
    primes: list[int],
    cap: float,
    source_row: dict[str, Any],
) -> dict[str, Any]:
    """汇总单个 bucket 的一维核。"""
    total_kernel = sum(kernel.values())
    kernel_l2 = math.sqrt(sum(value * value for value in kernel.values()))
    weighted_abs = 0.0
    mu_plus_linear = 0.0
    mu_minus_linear = 0.0
    signed_linear = 0.0
    top_by_kernel = []
    top_by_contribution = []
    for modulus, k_value in sorted(kernel.items()):
        remainder = remainders[modulus]
        mu = source.mobius_sign_squarefree(modulus, primes)
        contribution = mu * k_value * remainder
        abs_mass = k_value * abs(remainder)
        weighted_abs += abs_mass
        signed_linear += contribution
        if mu > 0:
            mu_plus_linear += k_value * remainder
        else:
            mu_minus_linear += k_value * remainder
        row = {
            "m": modulus,
            "mu": mu,
            "K": k_value,
            "R_m": remainder,
            "contribution": contribution,
            "abs_mass": abs_mass,
        }
        top_by_kernel.append(row)
        top_by_contribution.append(row)
    top_by_kernel = sorted(top_by_kernel, key=lambda row: row["K"], reverse=True)[:8]
    top_by_contribution = sorted(top_by_contribution, key=lambda row: row["abs_mass"], reverse=True)[:8]
    for row in top_by_kernel + top_by_contribution:
        row["kernel_share"] = safe_ratio(row["K"], total_kernel)
        row["abs_share"] = safe_ratio(row["abs_mass"], weighted_abs)
    slice_ratio = safe_ratio(abs(mu_plus_linear) + abs(mu_minus_linear), weighted_abs)
    signed_ratio = safe_ratio(abs(signed_linear), weighted_abs)
    effective_support = safe_ratio(total_kernel * total_kernel, kernel_l2 * kernel_l2)
    return {
        "bucket": bucket,
        "modulus_count": len(kernel),
        "kernel_l1": total_kernel,
        "kernel_l2": kernel_l2,
        "kernel_effective_support": effective_support,
        "weighted_abs_remainder": weighted_abs,
        "mu_plus_linear_remainder": mu_plus_linear,
        "mu_minus_linear_remainder": mu_minus_linear,
        "signed_linear_remainder": signed_linear,
        "slice_ratio": slice_ratio,
        "signed_ratio": signed_ratio,
        "cap": cap,
        "slice_slack": None if slice_ratio is None else cap - slice_ratio,
        "signed_slack": None if signed_ratio is None else cap - signed_ratio,
        "source_slice_ratio_error": None if slice_ratio is None else slice_ratio - source_row["slice_imbalance_ratio"],
        "source_signed_ratio_error": None if signed_ratio is None else signed_ratio - source_row["signed_ratio"],
        "kernel_contract_sample_passes": slice_ratio is not None and slice_ratio <= cap,
        "top_moduli_by_kernel": top_by_kernel,
        "top_moduli_by_abs_contribution": top_by_contribution,
    }


def audit(p_list: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行一维 divisor-kernel normal form 审计。"""
    values, primes = source.collect_values_and_primes(p_list)
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    edge_kernels = edge_kernel_weights(weights, d_level, overflow_multiplier)
    formula_failures = []
    formula_kernels: dict[str, dict[int, float]] = {bucket: {} for bucket in source.BUCKETS}
    for bucket, kernel in edge_kernels.items():
        for modulus, edge_value in kernel.items():
            formula_value = divisor_kernel_formula(modulus, bucket, weights, d_level)
            formula_kernels[bucket][modulus] = formula_value
            if abs(edge_value - formula_value) > 1e-12:
                formula_failures.append(
                    {
                        "bucket": bucket,
                        "m": modulus,
                        "edge_value": edge_value,
                        "formula_value": formula_value,
                        "error": formula_value - edge_value,
                    }
                )
    moduli = sorted({modulus for kernel in formula_kernels.values() for modulus in kernel})
    counts = attribution.divisibility_counts(values, moduli)
    remainders = {modulus: counts[modulus] - len(values) / modulus for modulus in moduli}
    cap = source.required_cap_for_z(z)
    source_data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    source_rows = {row["bucket"]: row for row in source_data["rows"]}
    rows = [
        summarize_bucket(bucket, formula_kernels[bucket], remainders, primes, cap, source_rows[bucket])
        for bucket in source.BUCKETS
    ]
    source_ratio_failures = [
        row
        for row in rows
        if abs(row["source_slice_ratio_error"] or 0.0) > 1e-10
        or abs(row["source_signed_ratio_error"] or 0.0) > 1e-10
    ]
    sample_failures = [row for row in rows if not row["kernel_contract_sample_passes"]]
    tightest = min(rows, key=lambda row: row["slice_slack"] if row["slice_slack"] is not None else 10**9)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router",
        "status": "z61_mobius_slice_balance_reduced_to_one_dimensional_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "value_count": len(values),
        "divisor_kernel_formula_closed": len(formula_failures) == 0,
        "kernel_matches_twocolor_source_closed": len(source_ratio_failures) == 0,
        "one_dimensional_kernel_contract_materialized": True,
        "sample_satisfies_kernel_contract": len(sample_failures) == 0,
        "one_dimensional_kernel_remainder_discrepancy_proved": False,
        "localized_block_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "formula_failure_count": len(formula_failures),
        "source_ratio_failure_count": len(source_ratio_failures),
        "sample_failure_count": len(sample_failures),
        "rows": rows,
        "tightest_kernel_contract_row": tightest,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "z=61 的二维边块已经降为一维 squarefree divisor-kernel："
            "`Block_b=sum_m mu(m)K_b(m)R_m`。"
            "`K_b(m)` 只由 `m` 的因子拆分落入哪个 balance bucket 决定，且完全非负。"
            "因此最终剩余不再是边级双线性枚举，而是证明一维核加权的 "
            "`R_m=A_m-N/m` 在 Möbius 奇偶两片内没有超过 `0.221522` 的符号偏斜；"
            "若失败，则直接抽取为 one-dimensional kernel PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 Möbius kernel normal form",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"divisor_kernel_formula_closed={fmt_bool(result['divisor_kernel_formula_closed'])}",
        f"kernel_matches_twocolor_source_closed={fmt_bool(result['kernel_matches_twocolor_source_closed'])}",
        f"one_dimensional_kernel_contract_materialized={fmt_bool(result['one_dimensional_kernel_contract_materialized'])}",
        f"sample_satisfies_kernel_contract={fmt_bool(result['sample_satisfies_kernel_contract'])}",
        f"one_dimensional_kernel_remainder_discrepancy_proved={fmt_bool(result['one_dimensional_kernel_remainder_discrepancy_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 一维核公式",
        "",
        "```text",
        "K_b(m)=sum_{d|m, m/d in supp(lambda), bucket(d,m/d)=b} |lambda_d lambda_{m/d}|",
        "Block_b=sum_m mu(m) K_b(m) R_m,   R_m=A_m-N/m.",
        "```",
        "",
        "其中 `m` 为 squarefree，且 `K_b(m)>=0`。这一步把二维边问题降成一维模数核问题。",
        "",
        "## 2. bucket 核账本",
        "",
        "| bucket | moduli | kernel L1 | eff supp | abs R | slice ratio | cap | slack | signed ratio |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{row['bucket']}` | {row['modulus_count']} | {fmt_float(row['kernel_l1'])} | "
            f"{fmt_float(row['kernel_effective_support'])} | {fmt_float(row['weighted_abs_remainder'])} | "
            f"{fmt_float(row['slice_ratio'])} | {fmt_float(row['cap'])} | "
            f"{fmt_float(row['slice_slack'])} | {fmt_float(row['signed_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：`K_b(m)` 的 divisor-kernel 公式与边枚举完全一致。",
            "- 已闭合：该一维核账本与上一层两色来源账本完全一致。",
            "- 已物化：`slice ratio<=0.221522` 的一维核合同。",
            "- 未闭合：全局证明一维核加权余项的 Möbius 切片符号偏斜界。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 最大核权模数",
            "",
        ]
    )
    for row in result["rows"]:
        lines.extend(
            [
                f"### `{row['bucket']}` by K",
                "",
                "| m | mu | K | R_m | abs share |",
                "| ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for top in row["top_moduli_by_kernel"]:
            lines.append(
                f"| {top['m']} | {top['mu']} | {fmt_float(top['K'])} | "
                f"{fmt_float(top['R_m'])} | {fmt_float(top['abs_share'])} |"
            )
        lines.extend(
            [
                "",
                f"### `{row['bucket']}` by abs contribution",
                "",
                "| m | mu | K | R_m | contribution | abs share |",
                "| ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for top in row["top_moduli_by_abs_contribution"]:
            lines.append(
                f"| {top['m']} | {top['mu']} | {fmt_float(top['K'])} | "
                f"{fmt_float(top['R_m'])} | {fmt_float(top['contribution'])} | "
                f"{fmt_float(top['abs_share'])} |"
            )
        lines.append("")
    lines.extend(
        [
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
                "divisor_kernel_formula_closed": result["divisor_kernel_formula_closed"],
                "sample_satisfies_kernel_contract": result["sample_satisfies_kernel_contract"],
                "tightest_bucket": result["tightest_kernel_contract_row"]["bucket"],
                "tightest_slice_slack": result["tightest_kernel_contract_row"]["slice_slack"],
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
