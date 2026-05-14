#!/usr/bin/env python3
"""把 z=61 深度格权函数偏差拆成 P-profile 抵消账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_prime_b_sieve_router as sieve
import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router as weight_router
import prime_matrix_square_phase_lowalpha_z61_kernel_depth_cancellation_router as depth
import prime_matrix_square_phase_lowalpha_z61_mobius_kernel_normal_form_router as kernel_form
import prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router as source


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
WEIGHT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json"
DEPTH_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "CrossPProfileCancellationOrProfileWeightPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json",
    "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_value_profiles(p_list: list[int]) -> tuple[dict[int, Counter[int]], list[int]]:
    """按 P 收集 b 多重序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = sieve.envelope.primes_from_flags(flags, trial_limit)
    profiles: dict[int, Counter[int]] = {}
    for p in p_list:
        values = [int(candidate["b"]) for candidate in sieve.collect_prime_a_candidates(p, flags, trial_primes)]
        profiles[p] = Counter(values)
    return profiles, trial_primes


def profile_linear(
    value_counter: Counter[int],
    moduli: dict[int, float],
) -> tuple[float, float, int, float, int | None]:
    """计算单个 P-profile 对一个深度格的实际和模型偏差。"""
    value_count = sum(value_counter.values())
    model_mean = sum(k_value / modulus for modulus, k_value in moduli.items())
    actual_sum = 0.0
    max_weight = 0.0
    max_weight_value: int | None = None
    nonzero_values = 0
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
    expected_sum = value_count * model_mean
    return actual_sum - expected_sum, model_mean, nonzero_values, max_weight, max_weight_value


def audit(p_list: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行 P-profile 抵消审计。"""
    profiles, primes = collect_value_profiles(p_list)
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    kernels = kernel_form.edge_kernel_weights(weights, d_level, overflow_multiplier)
    groups = weight_router.group_cell_moduli(kernels, primes, d_level)
    depth_data = json.loads(DEPTH_JSON.read_text(encoding="utf-8"))
    bucket_abs = {row["bucket"]: row["bucket_abs_remainder"] for row in depth_data["rows"]}
    cap = source.required_cap_for_z(z)
    weight_data = json.loads(WEIGHT_JSON.read_text(encoding="utf-8"))
    cell_lookup = {
        (row["bucket"], row["omega"], row["shell"]): row
        for row in weight_data["rows"]
    }

    profile_rows = []
    cell_rows = []
    identity_failures = []
    bucket_profile_crude: dict[str, float] = defaultdict(float)
    bucket_cell_abs: dict[str, float] = defaultdict(float)
    bucket_profile_by_p: dict[tuple[str, int], float] = defaultdict(float)

    for key, moduli in sorted(groups.items()):
        bucket, omega, shell = key
        profile_linears = []
        for p in p_list:
            linear, model_mean, nonzero_values, max_weight, max_weight_value = profile_linear(profiles[p], moduli)
            value_count = sum(profiles[p].values())
            row = {
                "p": p,
                "bucket": bucket,
                "omega": omega,
                "mobius_sign": 1 if omega % 2 == 0 else -1,
                "shell": shell,
                "profile_value_count": value_count,
                "model_mean": model_mean,
                "linear_remainder": linear,
                "abs_linear_remainder": abs(linear),
                "bucket_abs_share_of_abs_linear": safe_ratio(abs(linear), bucket_abs[bucket]),
                "nonzero_value_count_with_multiplicity": nonzero_values,
                "nonzero_value_share": safe_ratio(nonzero_values, value_count),
                "max_weight": max_weight,
                "max_weight_value": max_weight_value,
                "max_weight_over_abs_linear": safe_ratio(max_weight, abs(linear)),
            }
            profile_rows.append(row)
            profile_linears.append(linear)
            bucket_profile_crude[bucket] += abs(linear)
            bucket_profile_by_p[(bucket, p)] += abs(linear)
        total_linear = sum(profile_linears)
        expected_total = cell_lookup[key]["linear_remainder"]
        error = total_linear - expected_total
        if abs(error) > 1e-8:
            identity_failures.append({"key": key, "error": error})
        bucket_cell_abs[bucket] += abs(total_linear)
        cell_rows.append(
            {
                "bucket": bucket,
                "omega": omega,
                "mobius_sign": 1 if omega % 2 == 0 else -1,
                "shell": shell,
                "profile_crude_abs": sum(abs(item) for item in profile_linears),
                "cell_net_abs": abs(total_linear),
                "profile_cancellation_credit": sum(abs(item) for item in profile_linears) - abs(total_linear),
                "profile_crude_bucket_share": safe_ratio(sum(abs(item) for item in profile_linears), bucket_abs[bucket]),
                "cell_net_bucket_share": safe_ratio(abs(total_linear), bucket_abs[bucket]),
                "profile_identity_error": error,
            }
        )

    bucket_rows = []
    for bucket in source.BUCKETS:
        profile_crude = bucket_profile_crude[bucket]
        cell_abs = bucket_cell_abs[bucket]
        bucket_rows.append(
            {
                "bucket": bucket,
                "cap": cap,
                "profile_crude_abs": profile_crude,
                "cell_abs": cell_abs,
                "bucket_abs": bucket_abs[bucket],
                "profile_crude_ratio": safe_ratio(profile_crude, bucket_abs[bucket]),
                "cell_abs_ratio": safe_ratio(cell_abs, bucket_abs[bucket]),
                "profile_cancellation_credit": profile_crude - cell_abs,
                "profile_cancellation_credit_ratio": safe_ratio(profile_crude - cell_abs, bucket_abs[bucket]),
                "profile_independent_budget_sufficient": profile_crude <= cap * bucket_abs[bucket],
                "profile_budget_required_credit": max(0.0, profile_crude - cap * bucket_abs[bucket]),
                "profile_by_p": [
                    {
                        "p": p,
                        "abs_linear_sum": bucket_profile_by_p[(bucket, p)],
                        "bucket_abs_share": safe_ratio(bucket_profile_by_p[(bucket, p)], bucket_abs[bucket]),
                    }
                    for p in p_list
                ],
            }
        )

    independent_failures = [row for row in bucket_rows if not row["profile_independent_budget_sufficient"]]
    top_profile_atoms = sorted(
        profile_rows, key=lambda row: row["bucket_abs_share_of_abs_linear"] or 0.0, reverse=True
    )[:20]
    top_cell_cancellations = sorted(
        cell_rows, key=lambda row: row["profile_cancellation_credit"] or 0.0, reverse=True
    )[:16]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router",
        "status": "z61_weight_function_profile_cancellation_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "p_list": p_list,
        "profile_value_counts": {str(p): sum(counter.values()) for p, counter in profiles.items()},
        "p_profile_decomposition_identity_closed": len(identity_failures) == 0,
        "profile_independent_budget_sufficient_for_all_buckets": len(independent_failures) == 0,
        "cross_p_profile_cancellation_needed": len(independent_failures) > 0,
        "cross_p_profile_cancellation_proved": False,
        "profile_weight_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "identity_failure_count": len(identity_failures),
        "profile_independent_failure_count": len(independent_failures),
        "bucket_rows": bucket_rows,
        "cell_rows": cell_rows,
        "top_profile_atoms": top_profile_atoms,
        "top_cell_cancellations": top_cell_cancellations,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "深度格权函数偏差已按来源素数 `P` 精确分解。"
            "样本显示逐 `P` 独立绝对预算对 balanced/mid/unbalanced 不足，"
            "因此真正剩余是跨 `P` profile 的系统抵消；若某个 `P`-profile 原子长期承担异常偏差，"
            "则直接形成 ProfileWeight-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 权函数 P-profile 抵消",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"p_profile_decomposition_identity_closed={fmt_bool(result['p_profile_decomposition_identity_closed'])}",
        f"profile_independent_budget_sufficient_for_all_buckets={fmt_bool(result['profile_independent_budget_sufficient_for_all_buckets'])}",
        f"cross_p_profile_cancellation_needed={fmt_bool(result['cross_p_profile_cancellation_needed'])}",
        f"cross_p_profile_cancellation_proved={fmt_bool(result['cross_p_profile_cancellation_proved'])}",
        f"profile_weight_pdec_excluded={fmt_bool(result['profile_weight_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. bucket profile 预算",
        "",
        "| bucket | profile crude | cell abs | cap | credit | required credit | independent sufficient |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['profile_crude_ratio'])} | "
            f"{fmt_float(row['cell_abs_ratio'])} | {fmt_float(row['cap'])} | "
            f"{fmt_float(row['profile_cancellation_credit_ratio'])} | "
            f"{fmt_float(safe_ratio(row['profile_budget_required_credit'], row['bucket_abs']))} | "
            f"{fmt_bool(row['profile_independent_budget_sufficient'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. bucket 按 P 的绝对贡献",
            "",
            "| bucket | P | abs linear/bucket abs |",
            "| --- | ---: | ---: |",
        ]
    )
    for row in result["bucket_rows"]:
        for profile in row["profile_by_p"]:
            lines.append(
                f"| `{row['bucket']}` | {profile['p']} | {fmt_float(profile['bucket_abs_share'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 最大 P-profile 原子",
            "",
            "| P | bucket | omega | shell | abs linear/bucket abs | nonzero share | max W/abs L |",
            "| ---: | --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["top_profile_atoms"]:
        lines.append(
            f"| {row['p']} | `{row['bucket']}` | {row['omega']} | `{row['shell']}` | "
            f"{fmt_float(row['bucket_abs_share_of_abs_linear'])} | "
            f"{fmt_float(row['nonzero_value_share'])} | "
            f"{fmt_float(row['max_weight_over_abs_linear'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 最大跨 P 抵消单元",
            "",
            "| bucket | omega | shell | profile crude share | cell net share | credit share |",
            "| --- | ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["top_cell_cancellations"]:
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | "
            f"{fmt_float(row['profile_crude_bucket_share'])} | "
            f"{fmt_float(row['cell_net_bucket_share'])} | "
            f"{fmt_float(safe_ratio(row['profile_cancellation_credit'], next(b['bucket_abs'] for b in result['bucket_rows'] if b['bucket'] == row['bucket'])))} |"
        )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：每个深度格权函数偏差到 `P`-profile 的精确分解。",
            "- 重要负结果：逐 `P` 独立绝对预算不足以闭合所有 bucket。",
            "- 当前真正剩余：证明跨 `P` profile 抵消，或将持续 profile 偏差登记为 ProfileWeight-PDEC。",
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
                "p_profile_decomposition_identity_closed": result[
                    "p_profile_decomposition_identity_closed"
                ],
                "profile_independent_failure_count": result["profile_independent_failure_count"],
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
