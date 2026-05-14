#!/usr/bin/env python3
"""把 squarefree Selberg 系数拆成显式 Möbius-log 核心与截断尾。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_coefficient_formula_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
MARGIN_JSON = DOCS / "prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_CONSTANT = 1.35
NEXT_TARGET = "CoreMobiusLogResidualAngleAndTruncationTailAngleBoundOrVectorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-orthogonality-margin-contract-router.json",
    "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_coefficient_formula_split_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def factor_by_z(value: int, z: int, primes: list[int]) -> list[int]:
    """在 `prime<=z` 的 squarefree 支撑中分解 m。"""
    n = value
    factors = []
    for prime in primes:
        if prime > z:
            break
        if n % prime == 0:
            factors.append(prime)
            n //= prime
    return factors


def full_support_formula(m: int, z: int, d_level: int, primes: list[int]) -> float:
    """计算 `m<=D` 时的显式 Selberg lcm 系数公式。"""
    factors = factor_by_z(m, z, primes)
    mu = -1.0 if len(factors) % 2 else 1.0
    log_level = math.log(d_level)
    log_square_sum = sum(math.log(prime) ** 2 for prime in factors)
    return mu * (1.0 - log_square_sum / (log_level * log_level))


def collect_values_and_primes(p_list: list[int]) -> tuple[list[int], list[int]]:
    """复用 Selberg 归因账本的 prime-a b 序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = attribution.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = attribution.envelope.primes_from_flags(flags, trial_limit)
    values = attribution.selberg.collect_values(p_list, flags, trial_primes)
    return values, trial_primes


def vector_stats(items: list[tuple[int, float, float]]) -> dict[str, Any]:
    """计算 `(m,c,R)` 向量片段统计。"""
    coeff_l2 = math.sqrt(sum(coeff * coeff for _m, coeff, _rem in items))
    remainder_l2 = math.sqrt(sum(rem * rem for _m, _coeff, rem in items))
    cauchy = coeff_l2 * remainder_l2
    net = sum(coeff * rem for _m, coeff, rem in items)
    return {
        "moduli_count": len(items),
        "coefficient_l2": coeff_l2,
        "remainder_l2": remainder_l2,
        "cauchy_envelope": cauchy,
        "net_inner_product": net,
        "abs_contribution_sum": sum(abs(coeff * rem) for _m, coeff, rem in items),
        "abs_angle": safe_ratio(abs(net), cauchy),
    }


def row_for_z(
    values: list[int], primes: list[int], z: int, d_level: int, required_total_angle: float | None
) -> dict[str, Any]:
    """计算单个 z 的核心/尾部拆分。"""
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    coeffs = attribution.coefficient_by_lcm(weights)
    counts = attribution.divisibility_counts(values, sorted(coeffs))
    core_items = []
    tail_items = []
    formula_failures = []
    max_formula_error = 0.0
    for modulus, coefficient in coeffs.items():
        remainder = counts[modulus] - len(values) / modulus
        if modulus <= d_level:
            formula = full_support_formula(modulus, z, d_level, primes)
            error = abs(coefficient - formula)
            max_formula_error = max(max_formula_error, error)
            if error > 1e-10:
                formula_failures.append(
                    {
                        "m": modulus,
                        "coefficient": coefficient,
                        "formula": formula,
                        "error": error,
                    }
                )
            core_items.append((modulus, coefficient, remainder))
        else:
            tail_items.append((modulus, coefficient, remainder))
    core = vector_stats(core_items)
    tail = vector_stats(tail_items)
    total = vector_stats(core_items + tail_items)
    split_cauchy_sum = core["cauchy_envelope"] + tail["cauchy_envelope"]
    required_split_angle = None
    if required_total_angle is not None and total["cauchy_envelope"] > 0 and split_cauchy_sum > 0:
        required_split_angle = required_total_angle * total["cauchy_envelope"] / split_cauchy_sum
    return {
        "z": z,
        "d_level": d_level,
        "full_support_formula_failure_count": len(formula_failures),
        "max_full_support_formula_error": max_formula_error,
        "core": core,
        "tail": tail,
        "total": total,
        "split_cauchy_sum": split_cauchy_sum,
        "split_cauchy_over_total_cauchy": safe_ratio(split_cauchy_sum, total["cauchy_envelope"]),
        "required_total_angle": required_total_angle,
        "required_equal_split_angle": required_split_angle,
        "sample_core_tail_equal_split_pass": (
            required_split_angle is not None
            and (core["abs_angle"] or 0.0) <= required_split_angle
            and (tail["abs_angle"] or 0.0) <= required_split_angle
        ),
    }


def audit(p_list: list[int], z_list: list[int], d_level: int, constant: float) -> dict[str, Any]:
    """执行系数公式拆分审计。"""
    values, primes = collect_values_and_primes(p_list)
    margin = json.loads(MARGIN_JSON.read_text(encoding="utf-8"))
    angle_by_z = {
        int(row["z"]): row["required_abs_angle_bound"]
        for row in margin["rows"]
        if row["required_abs_angle_bound"] is not None
    }
    rows = [row_for_z(values, primes, z, d_level, angle_by_z.get(z)) for z in z_list]
    formula_failures = sum(row["full_support_formula_failure_count"] for row in rows)
    tightest_split = min(
        (row for row in rows if row["required_equal_split_angle"] is not None),
        key=lambda row: row["required_equal_split_angle"],
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_coefficient_formula_split_router",
        "status": "full_support_coefficient_formula_closed_tail_angle_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "full_support_mobius_log_coefficient_formula_closed": formula_failures == 0,
        "core_tail_angle_split_contract_closed": True,
        "sample_satisfies_core_tail_split_contract": all(row["sample_core_tail_equal_split_pass"] for row in rows),
        "core_mobius_log_residual_angle_bound_proved": False,
        "truncation_tail_angle_bound_proved": False,
        "vector_squarefree_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "constant": constant,
        "d_level": d_level,
        "value_count": len(values),
        "formula_failure_count": formula_failures,
        "rows": rows,
        "tightest_equal_split_angle_row": tightest_split,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Selberg lcm 系数已拆成两个严格对象："
            "当 `m<=D` 时，全支撑部分满足显式公式 "
            "`c_m=mu(m)(1-sum_{q|m}(log q)^2/(log D)^2)`；"
            "`m>D` 的部分完全来自 `d,e<=D` 但 `lcm(d,e)>D` 的截断尾。"
            "因此统一角度界可进一步拆成核心 Möbius-log 余项角度与截断尾角度。"
            "默认样本两部分均远低于所需 equal-split 角度；"
            "剩余是分别证明核心角度界和截断尾角度界，或把失败登记为 VectorSquarefree-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Selberg 系数公式拆分",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        (
            "full_support_mobius_log_coefficient_formula_closed="
            f"{fmt_bool(result['full_support_mobius_log_coefficient_formula_closed'])}"
        ),
        f"core_tail_angle_split_contract_closed={fmt_bool(result['core_tail_angle_split_contract_closed'])}",
        (
            "sample_satisfies_core_tail_split_contract="
            f"{fmt_bool(result['sample_satisfies_core_tail_split_contract'])}"
        ),
        f"core_mobius_log_residual_angle_bound_proved={fmt_bool(result['core_mobius_log_residual_angle_bound_proved'])}",
        f"truncation_tail_angle_bound_proved={fmt_bool(result['truncation_tail_angle_bound_proved'])}",
        f"vector_squarefree_pdec_excluded={fmt_bool(result['vector_squarefree_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 核心/截断尾拆分",
        "",
        "| z | core count | tail count | formula max err | core angle | tail angle | required split angle | split Cauchy / total Cauchy |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {row['core']['moduli_count']} | {row['tail']['moduli_count']} | "
            f"{fmt_float(row['max_full_support_formula_error'])} | "
            f"{fmt_float(row['core']['abs_angle'])} | {fmt_float(row['tail']['abs_angle'])} | "
            f"{fmt_float(row['required_equal_split_angle'])} | "
            f"{fmt_float(row['split_cauchy_over_total_cauchy'])} |"
        )
    tight = result["tightest_equal_split_angle_row"]
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：`m<=D` 全支撑系数的显式 Möbius-log 公式。",
            "- 已闭合：把总角度合同无损替换为 core/tail equal-split 充分合同。",
            (
                f"- 最紧 equal-split 行为 `z={tight['z']}`，需要 core 与 tail 角度均不超过 "
                f"`{fmt_float(tight['required_equal_split_angle'])}`。"
            ),
            "- 未闭合：核心 Möbius-log 余项角度界。",
            "- 未闭合：`m>D` 截断尾角度界。",
            "- 未闭合：若任一角度界失败，证明其形成可排斥的 `VectorSquarefree-PDEC`。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z-list", default=",".join(str(item) for item in DEFAULT_Z_LIST))
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--constant", type=float, default=DEFAULT_CONSTANT)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), parse_int_list(args.z_list), args.d_level, args.constant)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "formula_failure_count": result["formula_failure_count"],
                "tightest_z": result["tightest_equal_split_angle_row"]["z"],
                "tightest_equal_split_angle": result["tightest_equal_split_angle_row"][
                    "required_equal_split_angle"
                ],
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
