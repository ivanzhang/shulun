#!/usr/bin/env python3
"""把 z=61 的跨 P-profile 抵消压成反号信用下界。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_profile_sign_pattern_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.md
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
import prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router as source
import prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router as profile_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
WEIGHT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json"
DEPTH_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json"
PROFILE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "ProfileOppositeSignCreditLowerBoundOrProfileSignDefectPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json",
    "prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json",
    "prime-matrix-square-phase-lowalpha-z61-weight-profile-cancellation-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_profile_sign_pattern_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_word(values: list[float], tolerance: float = 1e-12) -> str:
    """把 profile 向量转成符号字。"""
    chars = []
    for value in values:
        if value > tolerance:
            chars.append("+")
        elif value < -tolerance:
            chars.append("-")
        else:
            chars.append("0")
    return "".join(chars)


def count_sign_changes(word: str) -> int:
    """统计去零后的相邻符号变化次数。"""
    reduced = [char for char in word if char != "0"]
    return sum(1 for left, right in zip(reduced, reduced[1:]) if left != right)


def signed_vector_stats(values: list[float]) -> dict[str, Any]:
    """计算跨 P 向量的反号信用。"""
    positive = sum(value for value in values if value > 0)
    negative = -sum(value for value in values if value < 0)
    crude = positive + negative
    net = sum(values)
    minority = min(positive, negative)
    credit = crude - abs(net)
    word = sign_word(values)
    return {
        "sign_word": word,
        "sign_changes": count_sign_changes(word),
        "has_both_signs": positive > 0 and negative > 0,
        "positive_mass": positive,
        "negative_mass": negative,
        "minority_mass": minority,
        "profile_crude_abs": crude,
        "cell_net_abs": abs(net),
        "signed_net": net,
        "opposite_sign_credit": credit,
        "opposite_sign_credit_identity_error": credit - 2 * minority,
        "minority_share_of_crude": safe_ratio(minority, crude),
        "dominant_share_of_crude": safe_ratio(max(positive, negative), crude),
        "max_profile_abs_share": safe_ratio(max((abs(value) for value in values), default=0.0), crude),
    }


def load_bucket_abs() -> dict[str, float]:
    """读取 bucket 的绝对质量基准。"""
    depth_data = json.loads(DEPTH_JSON.read_text(encoding="utf-8"))
    return {row["bucket"]: row["bucket_abs_remainder"] for row in depth_data["rows"]}


def load_weight_lookup() -> dict[tuple[str, int, str], dict[str, Any]]:
    """读取上一层深度格 signed 余项。"""
    weight_data = json.loads(WEIGHT_JSON.read_text(encoding="utf-8"))
    return {
        (row["bucket"], row["omega"], row["shell"]): row
        for row in weight_data["rows"]
    }


def summarize_cell(
    key: tuple[str, int, str],
    moduli: dict[int, float],
    p_list: list[int],
    profiles: dict[int, Any],
    bucket_abs: float,
    expected_linear: float,
) -> dict[str, Any]:
    """汇总一个深度格的 P-profile 符号向量。"""
    bucket, omega, shell = key
    profile_entries = []
    values = []
    for p in p_list:
        linear, model_mean, nonzero_values, max_weight, max_weight_value = profile_router.profile_linear(
            profiles[p], moduli
        )
        value_count = sum(profiles[p].values())
        values.append(linear)
        profile_entries.append(
            {
                "p": p,
                "linear_remainder": linear,
                "abs_linear_remainder": abs(linear),
                "signed_bucket_share": safe_ratio(linear, bucket_abs),
                "abs_bucket_share": safe_ratio(abs(linear), bucket_abs),
                "profile_value_count": value_count,
                "model_mean": model_mean,
                "nonzero_value_count_with_multiplicity": nonzero_values,
                "nonzero_value_share": safe_ratio(nonzero_values, value_count),
                "max_weight": max_weight,
                "max_weight_value": max_weight_value,
            }
        )
    stats = signed_vector_stats(values)
    identity_error = stats["signed_net"] - expected_linear
    row = {
        "bucket": bucket,
        "omega": omega,
        "mobius_sign": 1 if omega % 2 == 0 else -1,
        "shell": shell,
        "profile_entries": profile_entries,
        "profile_vector": values,
        "profile_identity_error": identity_error,
        "profile_crude_bucket_share": safe_ratio(stats["profile_crude_abs"], bucket_abs),
        "cell_net_bucket_share": safe_ratio(stats["cell_net_abs"], bucket_abs),
        "opposite_sign_credit_bucket_share": safe_ratio(stats["opposite_sign_credit"], bucket_abs),
        "sign_defect_risk_score": (
            (safe_ratio(stats["profile_crude_abs"], bucket_abs) or 0.0)
            * (1.0 - (stats["minority_share_of_crude"] or 0.0))
        ),
    }
    row.update(stats)
    return row


def audit(p_list: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行 profile 符号信用审计。"""
    profiles, primes = profile_router.collect_value_profiles(p_list)
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    kernels = kernel_form.edge_kernel_weights(weights, d_level, overflow_multiplier)
    groups = weight_router.group_cell_moduli(kernels, primes, d_level)
    bucket_abs = load_bucket_abs()
    weight_lookup = load_weight_lookup()
    cap = source.required_cap_for_z(z)

    cell_rows = []
    identity_failures = []
    credit_identity_failures = []
    bucket_acc: dict[str, dict[str, Any]] = {
        bucket: {
            "profile_crude_abs": 0.0,
            "cell_net_abs": 0.0,
            "opposite_sign_credit": 0.0,
            "mixed_sign_crude_abs": 0.0,
            "single_sign_crude_abs": 0.0,
            "candidate_credit_abs": 0.0,
            "profile_abs_by_p": {p: 0.0 for p in p_list},
            "profile_signed_by_p": {p: 0.0 for p in p_list},
        }
        for bucket in source.BUCKETS
    }

    for key, moduli in sorted(groups.items()):
        expected = weight_lookup[key]["linear_remainder"]
        row = summarize_cell(key, moduli, p_list, profiles, bucket_abs[key[0]], expected)
        cell_rows.append(row)
        if abs(row["profile_identity_error"]) > 1e-8:
            identity_failures.append(
                {"key": key, "profile_identity_error": row["profile_identity_error"]}
            )
        if abs(row["opposite_sign_credit_identity_error"]) > 1e-8:
            credit_identity_failures.append(
                {"key": key, "credit_identity_error": row["opposite_sign_credit_identity_error"]}
            )
        acc = bucket_acc[key[0]]
        acc["profile_crude_abs"] += row["profile_crude_abs"]
        acc["cell_net_abs"] += row["cell_net_abs"]
        acc["opposite_sign_credit"] += row["opposite_sign_credit"]
        if row["has_both_signs"]:
            acc["mixed_sign_crude_abs"] += row["profile_crude_abs"]
        else:
            acc["single_sign_crude_abs"] += row["profile_crude_abs"]
        if row["sign_changes"] >= 2 and (row["minority_share_of_crude"] or 0.0) >= 0.25:
            acc["candidate_credit_abs"] += row["opposite_sign_credit"]
        for entry in row["profile_entries"]:
            p = entry["p"]
            acc["profile_abs_by_p"][p] += entry["abs_linear_remainder"]
            acc["profile_signed_by_p"][p] += entry["linear_remainder"]

    bucket_rows = []
    for bucket in source.BUCKETS:
        acc = bucket_acc[bucket]
        required_credit = max(0.0, acc["profile_crude_abs"] - cap * bucket_abs[bucket])
        credit_margin = acc["opposite_sign_credit"] - required_credit
        bucket_rows.append(
            {
                "bucket": bucket,
                "cap": cap,
                "bucket_abs": bucket_abs[bucket],
                "profile_crude_abs": acc["profile_crude_abs"],
                "cell_net_abs": acc["cell_net_abs"],
                "required_credit_to_meet_cap": required_credit,
                "opposite_sign_credit": acc["opposite_sign_credit"],
                "opposite_sign_credit_margin": credit_margin,
                "sample_credit_covers_required": credit_margin >= -1e-8,
                "profile_crude_ratio": safe_ratio(acc["profile_crude_abs"], bucket_abs[bucket]),
                "cell_net_ratio": safe_ratio(acc["cell_net_abs"], bucket_abs[bucket]),
                "required_credit_ratio": safe_ratio(required_credit, bucket_abs[bucket]),
                "opposite_sign_credit_ratio": safe_ratio(acc["opposite_sign_credit"], bucket_abs[bucket]),
                "opposite_sign_credit_margin_ratio": safe_ratio(credit_margin, bucket_abs[bucket]),
                "mixed_sign_crude_ratio": safe_ratio(acc["mixed_sign_crude_abs"], bucket_abs[bucket]),
                "single_sign_crude_ratio": safe_ratio(acc["single_sign_crude_abs"], bucket_abs[bucket]),
                "candidate_credit_ratio": safe_ratio(acc["candidate_credit_abs"], bucket_abs[bucket]),
                "profile_by_p": [
                    {
                        "p": p,
                        "signed_sum": acc["profile_signed_by_p"][p],
                        "abs_sum": acc["profile_abs_by_p"][p],
                        "signed_bucket_share": safe_ratio(acc["profile_signed_by_p"][p], bucket_abs[bucket]),
                        "abs_bucket_share": safe_ratio(acc["profile_abs_by_p"][p], bucket_abs[bucket]),
                    }
                    for p in p_list
                ],
            }
        )

    top_credit_cells = sorted(
        cell_rows, key=lambda row: row["opposite_sign_credit_bucket_share"] or 0.0, reverse=True
    )[:16]
    top_sign_defect_risks = sorted(
        cell_rows, key=lambda row: row["sign_defect_risk_score"], reverse=True
    )[:16]
    top_single_sign_cells = [
        row
        for row in sorted(cell_rows, key=lambda item: item["profile_crude_bucket_share"] or 0.0, reverse=True)
        if not row["has_both_signs"]
    ][:16]
    sample_credit_failures = [
        row for row in bucket_rows if not row["sample_credit_covers_required"]
    ]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_profile_sign_pattern_router",
        "status": "z61_profile_opposite_sign_credit_reduction_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "p_list": p_list,
        "profile_value_counts": {str(p): sum(counter.values()) for p, counter in profiles.items()},
        "profile_sign_vector_identity_closed": len(identity_failures) == 0,
        "opposite_sign_credit_identity_closed": len(credit_identity_failures) == 0,
        "sample_opposite_sign_credit_covers_required_for_all_buckets": len(sample_credit_failures) == 0,
        "opposite_sign_credit_lower_bound_proved": False,
        "profile_sign_defect_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "identity_failure_count": len(identity_failures),
        "credit_identity_failure_count": len(credit_identity_failures),
        "sample_credit_failure_count": len(sample_credit_failures),
        "bucket_rows": bucket_rows,
        "cell_rows": cell_rows,
        "top_opposite_sign_credit_cells": top_credit_cells,
        "top_sign_defect_risks": top_sign_defect_risks,
        "top_single_sign_cells": top_single_sign_cells,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "跨 P-profile 抵消已被压成精确反号信用恒等式："
            "`sum_P |L_P|-|sum_P L_P|=2 min(sum_{L_P>0}L_P, sum_{L_P<0}|L_P|)`。"
            "因此 profile 独立预算不足时，真正要证明的是每个 bucket 有足够反号质量信用；"
            "若某个 bucket 长期缺少反号信用，就给出 ProfileSignDefect-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 profile 符号信用路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"profile_sign_vector_identity_closed={fmt_bool(result['profile_sign_vector_identity_closed'])}",
        f"opposite_sign_credit_identity_closed={fmt_bool(result['opposite_sign_credit_identity_closed'])}",
        "sample_opposite_sign_credit_covers_required_for_all_buckets="
        f"{fmt_bool(result['sample_opposite_sign_credit_covers_required_for_all_buckets'])}",
        f"opposite_sign_credit_lower_bound_proved={fmt_bool(result['opposite_sign_credit_lower_bound_proved'])}",
        f"profile_sign_defect_pdec_excluded={fmt_bool(result['profile_sign_defect_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 反号信用恒等式",
        "",
        "对固定深度格 `C`，设 `L_P(C)` 为来源 `P` 的 profile 线性余项，则",
        "",
        "```text",
        "credit(C)=sum_P |L_P(C)|-|sum_P L_P(C)|",
        "         =2*min(sum_{L_P>0} L_P, sum_{L_P<0} |L_P|).",
        "```",
        "",
        "这把“跨 P 抵消”改写为可验收的反号质量下界。",
        "",
        "## 2. bucket 信用账本",
        "",
        "| bucket | crude | net | cap | need credit | sign credit | margin | mixed crude | single crude |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['profile_crude_ratio'])} | "
            f"{fmt_float(row['cell_net_ratio'])} | {fmt_float(row['cap'])} | "
            f"{fmt_float(row['required_credit_ratio'])} | "
            f"{fmt_float(row['opposite_sign_credit_ratio'])} | "
            f"{fmt_float(row['opposite_sign_credit_margin_ratio'])} | "
            f"{fmt_float(row['mixed_sign_crude_ratio'])} | "
            f"{fmt_float(row['single_sign_crude_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. bucket 按 P 的 signed/abs 聚合",
            "",
            "| bucket | P | signed/bucket abs | abs/bucket abs |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["bucket_rows"]:
        for profile in row["profile_by_p"]:
            lines.append(
                f"| `{row['bucket']}` | {profile['p']} | "
                f"{fmt_float(profile['signed_bucket_share'])} | "
                f"{fmt_float(profile['abs_bucket_share'])} |"
            )
    lines.extend(
        [
            "",
            "## 4. 最大反号信用单元",
            "",
            "| bucket | omega | shell | signs | changes | crude | net | credit | minority | max profile |",
            "| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["top_opposite_sign_credit_cells"]:
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | `{row['sign_word']}` | "
            f"{row['sign_changes']} | {fmt_float(row['profile_crude_bucket_share'])} | "
            f"{fmt_float(row['cell_net_bucket_share'])} | "
            f"{fmt_float(row['opposite_sign_credit_bucket_share'])} | "
            f"{fmt_float(row['minority_share_of_crude'])} | "
            f"{fmt_float(row['max_profile_abs_share'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最大符号缺陷风险单元",
            "",
            "| bucket | omega | shell | signs | crude | net | minority | risk |",
            "| --- | ---: | --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["top_sign_defect_risks"]:
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | `{row['sign_word']}` | "
            f"{fmt_float(row['profile_crude_bucket_share'])} | "
            f"{fmt_float(row['cell_net_bucket_share'])} | "
            f"{fmt_float(row['minority_share_of_crude'])} | "
            f"{fmt_float(row['sign_defect_risk_score'])} |"
        )
    lines.extend(
        [
            "",
            "## 6. 证明边界",
            "",
            "- 已闭合：profile signed 向量逐格合回上一层 `linear_remainder`。",
            "- 已闭合：跨 P 抵消等价于逐格反号信用 `2*minority`。",
            "- 样本事实：四个 bucket 的反号信用均超过把 crude 压到 cap 所需的最低信用。",
            "- 未闭合：需要证明这种反号信用下界对一般反例链强制成立，或登记 ProfileSignDefect-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 7. 依赖哈希",
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
                "profile_sign_vector_identity_closed": result["profile_sign_vector_identity_closed"],
                "opposite_sign_credit_identity_closed": result["opposite_sign_credit_identity_closed"],
                "sample_credit_failure_count": result["sample_credit_failure_count"],
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
