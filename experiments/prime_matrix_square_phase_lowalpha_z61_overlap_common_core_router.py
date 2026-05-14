#!/usr/bin/env python3
"""审计 z=61 唯一 double-hit overlap 的 2/3 common-core 结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_overlap_common_core_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router as bilinear
import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router as weight_router
import prime_matrix_square_phase_lowalpha_z61_hit_support_scale_router as support_router
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router as profile_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OVERLAP_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.md"

NEXT_TARGET = "TwoThreeCommonCoreOverlapAtomBoundOrCommonCorePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json",
]
TOL = 1e-10


def factor_distinct(value: int) -> list[int]:
    """返回不同素因子列表。"""
    factors = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_overlap_common_core_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def edge_rows_for_modulus(modulus: int, weights: dict[int, float], target_bucket: str) -> list[dict[str, Any]]:
    """列出一个模数在目标 bucket 中的 coprime 边分解。"""
    rows = []
    for d_value, lambda_d in sorted(weights.items()):
        if modulus % d_value != 0:
            continue
        e_value = modulus // d_value
        if e_value not in weights or math.gcd(d_value, e_value) != 1:
            continue
        bucket = bilinear.balance_bucket(d_value, e_value)
        if bucket != target_bucket:
            continue
        edge_weight = abs(lambda_d * weights[e_value])
        rows.append(
            {
                "d": d_value,
                "e": e_value,
                "bucket": bucket,
                "ratio": max(d_value, e_value) / min(d_value, e_value),
                "lambda_d": lambda_d,
                "lambda_e": weights[e_value],
                "abs_lambda_product": edge_weight,
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行 common-core overlap 审计。"""
    overlap_data = json.loads(OVERLAP_JSON.read_text(encoding="utf-8"))
    atom = overlap_data["all_multi_modulus_atoms"][0]
    b_value = atom["b_value"]
    hit_moduli = [item["m"] for item in atom["hit_moduli"]]
    hit_weights = {item["m"]: item["K"] for item in atom["hit_moduli"]}
    core = math.gcd(*hit_moduli)
    prefixes = [modulus // core for modulus in hit_moduli]
    lcm_value = math.lcm(*hit_moduli)

    profiles, primes = profile_router.collect_value_profiles(support_router.TARGET_PRIMES)
    weights = attribution.selberg.selberg_weights(
        support_router.DEFAULT_Z, support_router.DEFAULT_D_LEVEL, primes
    )
    kernels = kernel_form.edge_kernel_weights(
        weights, support_router.DEFAULT_D_LEVEL, support_router.DEFAULT_OVERFLOW_MULTIPLIER
    )
    groups = weight_router.group_cell_moduli(kernels, primes, support_router.DEFAULT_D_LEVEL)
    target_moduli = groups[(support_router.TARGET_BUCKET, support_router.HIGH_OMEGA, support_router.TARGET_SHELL)]
    target_dividing_moduli = [modulus for modulus in sorted(target_moduli) if b_value % modulus == 0]

    modulus_rows = []
    max_kernel_error = 0.0
    for modulus in hit_moduli:
        edge_rows = edge_rows_for_modulus(modulus, weights, support_router.TARGET_BUCKET)
        edge_sum = sum(row["abs_lambda_product"] for row in edge_rows)
        kernel_error = edge_sum - hit_weights[modulus]
        max_kernel_error = max(max_kernel_error, abs(kernel_error))
        modulus_rows.append(
            {
                "m": modulus,
                "prefix": modulus // core,
                "factorization": factor_distinct(modulus),
                "edge_count_in_target_bucket": len(edge_rows),
                "edge_weight_sum": edge_sum,
                "kernel_weight": hit_weights[modulus],
                "kernel_identity_error": kernel_error,
                "edge_rows": edge_rows,
            }
        )

    core_kernel_rows = []
    for bucket, kernel in kernels.items():
        if core in kernel:
            core_kernel_rows.append(
                {
                    "bucket": bucket,
                    "omega": len(factor_distinct(core)),
                    "shell": weight_router.depth.shell_label(core, support_router.DEFAULT_D_LEVEL)
                    if hasattr(weight_router, "depth")
                    else None,
                    "kernel_weight": kernel[core],
                }
            )

    overlap_contribution_from_moduli = sum(hit_weights[modulus] for modulus in hit_moduli)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_overlap_common_core_router",
        "status": "z61_single_double_hit_overlap_reduced_to_two_three_common_core_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": overlap_data["certificate_type"],
        "target_bucket": support_router.TARGET_BUCKET,
        "target_shell": support_router.TARGET_SHELL,
        "target_omega": support_router.HIGH_OMEGA,
        "overlap_p": atom["p"],
        "b_value": b_value,
        "b_factorization": factor_distinct(b_value),
        "hit_moduli": hit_moduli,
        "hit_moduli_factorizations": {str(modulus): factor_distinct(modulus) for modulus in hit_moduli},
        "common_core": core,
        "common_core_factorization": factor_distinct(core),
        "common_core_squarefree": math.prod(factor_distinct(core)) == core,
        "common_core_omega": len(factor_distinct(core)),
        "prefixes": prefixes,
        "prefixes_are_two_three": sorted(prefixes) == [2, 3],
        "prefixes_coprime": math.gcd(*prefixes) == 1,
        "b_equals_lcm_of_hit_moduli": b_value == lcm_value,
        "b_over_common_core": b_value // core,
        "target_dividing_moduli": target_dividing_moduli,
        "target_dividing_moduli_exactly_hit_moduli": target_dividing_moduli == sorted(hit_moduli),
        "modulus_rows": modulus_rows,
        "max_kernel_edge_identity_error": max_kernel_error,
        "kernel_edge_decomposition_closed": max_kernel_error <= TOL,
        "core_kernel_rows": core_kernel_rows,
        "overlap_contribution_from_moduli": overlap_contribution_from_moduli,
        "overlap_contribution_source": atom["contribution"],
        "overlap_contribution_identity_error": overlap_contribution_from_moduli - atom["contribution"],
        "two_three_common_core_identity_closed": (
            sorted(prefixes) == [2, 3]
            and math.gcd(*prefixes) == 1
            and b_value == lcm_value
            and target_dividing_moduli == sorted(hit_moduli)
            and max_kernel_error <= TOL
            and abs(overlap_contribution_from_moduli - atom["contribution"]) <= TOL
        ),
        "two_three_common_core_overlap_bound_proved": False,
        "common_core_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "唯一 double-hit overlap 已压成 `C=4807=11*19*23` 的 `2C/3C` common-core 原子："
            "`9614=2C`、`14421=3C`、`b=28842=6C=lcm(2C,3C)`。"
            "在目标格中，`b` 只命中这两个模数；其贡献正是两个目标 bucket kernel 权重之和。"
            "下一步最窄硬点是证明这种 `2/3` common-core 原子不能持续超过允许容量，"
            "或把它登记为 CommonCore-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 overlap common-core 路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"b_value={result['b_value']}",
        f"common_core={result['common_core']}",
        f"prefixes={result['prefixes']}",
        f"b_equals_lcm_of_hit_moduli={fmt_bool(result['b_equals_lcm_of_hit_moduli'])}",
        f"target_dividing_moduli_exactly_hit_moduli={fmt_bool(result['target_dividing_moduli_exactly_hit_moduli'])}",
        f"kernel_edge_decomposition_closed={fmt_bool(result['kernel_edge_decomposition_closed'])}",
        f"two_three_common_core_identity_closed={fmt_bool(result['two_three_common_core_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Common-Core 原子",
        "",
        "| object | value | factorization |",
        "| --- | ---: | --- |",
        f"| `C` | {result['common_core']} | `{result['common_core_factorization']}` |",
        f"| `2C` | {result['hit_moduli'][0]} | `{result['hit_moduli_factorizations'][str(result['hit_moduli'][0])]}` |",
        f"| `3C` | {result['hit_moduli'][1]} | `{result['hit_moduli_factorizations'][str(result['hit_moduli'][1])]}` |",
        f"| `b` | {result['b_value']} | `{result['b_factorization']}` |",
        "",
        "## 2. 目标 bucket 边分解",
        "",
        "| m | prefix | edge count | kernel | edge sum | identity error |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["modulus_rows"]:
        lines.append(
            f"| {row['m']} | {row['prefix']} | {row['edge_count_in_target_bucket']} | "
            f"{fmt_float(row['kernel_weight'])} | {fmt_float(row['edge_weight_sum'])} | "
            f"{fmt_float(row['kernel_identity_error'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：唯一 overlap 到 `2C/3C` common-core 原子的精确等价与边权分解。",
            "- 未闭合：`2/3` common-core overlap 原子的全局容量界，或 CommonCore-PDEC 排斥。",
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
                "two_three_common_core_identity_closed": result["two_three_common_core_identity_closed"],
                "target_dividing_moduli": result["target_dividing_moduli"],
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
