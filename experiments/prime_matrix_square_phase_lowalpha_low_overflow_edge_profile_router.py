#!/usr/bin/env python3
"""把低超界 lcm tail 拆成 `(d,e)` 边界边画像。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_low_overflow_edge_profile_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.md
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


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "CoprimeBoundaryLCMEdgeAngleBoundOrSmallGCDOverflowPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_low_overflow_edge_profile_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_values_and_primes(p_list: list[int]) -> tuple[list[int], list[int]]:
    """复用 Selberg 归因账本的 prime-a b 序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = attribution.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = attribution.envelope.primes_from_flags(flags, trial_limit)
    values = attribution.selberg.collect_values(p_list, flags, trial_primes)
    return values, trial_primes


def empty_stats(label: str) -> dict[str, Any]:
    """创建空统计行。"""
    return {
        "label": label,
        "edge_count": 0,
        "signed_edge_contribution": 0.0,
        "abs_edge_contribution": 0.0,
        "positive_edge_count": 0,
        "weight_abs": 0.0,
        "weight_l2_square": 0.0,
        "remainder_l2_square_weighted": 0.0,
    }


def add_edge(stats: dict[str, Any], weight: float, remainder: float) -> None:
    """登记一条 `(d,e)` 边。"""
    contribution = weight * remainder
    stats["edge_count"] += 1
    stats["signed_edge_contribution"] += contribution
    stats["abs_edge_contribution"] += abs(contribution)
    stats["positive_edge_count"] += 1 if contribution >= 0 else 0
    stats["weight_abs"] += abs(weight)
    stats["weight_l2_square"] += weight * weight
    stats["remainder_l2_square_weighted"] += remainder * remainder


def finalize_stats(stats: dict[str, Any]) -> dict[str, Any]:
    """补齐派生统计。"""
    weight_l2 = math.sqrt(stats["weight_l2_square"])
    remainder_l2 = math.sqrt(stats["remainder_l2_square_weighted"])
    cauchy = weight_l2 * remainder_l2
    stats["edge_weight_l2"] = weight_l2
    stats["edge_remainder_l2"] = remainder_l2
    stats["edge_cauchy_envelope"] = cauchy
    stats["edge_abs_angle"] = safe_ratio(abs(stats["signed_edge_contribution"]), cauchy)
    stats["signed_over_abs"] = safe_ratio(abs(stats["signed_edge_contribution"]), stats["abs_edge_contribution"])
    return stats


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """计算单个 z 的低超界 `(d,e)` 边画像。"""
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    coeffs = attribution.coefficient_by_lcm(weights)
    counts = attribution.divisibility_counts(values, sorted(coeffs))
    remainders = {m: counts[m] - len(values) / m for m in coeffs}
    total = empty_stats("low-overflow")
    coprime = empty_stats("gcd=1")
    noncoprime = empty_stats("gcd>1")
    by_gcd: dict[int, dict[str, Any]] = defaultdict(lambda: empty_stats("placeholder"))
    items = list(weights.items())
    for d, lambda_d in items:
        for e, lambda_e in items:
            modulus = attribution.selberg.lcm(d, e)
            if modulus <= d_level or modulus > overflow_multiplier * d_level:
                continue
            gcd_value = math.gcd(d, e)
            weight = lambda_d * lambda_e
            remainder = remainders[modulus]
            add_edge(total, weight, remainder)
            if gcd_value == 1:
                add_edge(coprime, weight, remainder)
            else:
                add_edge(noncoprime, weight, remainder)
            by_gcd[gcd_value]["label"] = f"gcd={gcd_value}"
            by_gcd[gcd_value]["gcd"] = gcd_value
            add_edge(by_gcd[gcd_value], weight, remainder)
    total = finalize_stats(total)
    coprime = finalize_stats(coprime)
    noncoprime = finalize_stats(noncoprime)
    gcd_rows = [finalize_stats(row) for row in by_gcd.values()]
    gcd_rows.sort(key=lambda row: -row["abs_edge_contribution"])
    return {
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "total_low_overflow_edge": total,
        "coprime_edge": coprime,
        "noncoprime_edge": noncoprime,
        "coprime_abs_share": safe_ratio(coprime["abs_edge_contribution"], total["abs_edge_contribution"]),
        "coprime_weight_share": safe_ratio(coprime["weight_abs"], total["weight_abs"]),
        "top_gcd_rows": gcd_rows[:16],
    }


def audit(p_list: list[int], z_list: list[int], d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行低超界边画像审计。"""
    values, primes = collect_values_and_primes(p_list)
    rows = [row_for_z(values, primes, z, d_level, overflow_multiplier) for z in z_list]
    active_rows = [row for row in rows if row["total_low_overflow_edge"]["edge_count"] > 0]
    min_coprime_share = min((row["coprime_abs_share"] for row in active_rows), default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_low_overflow_edge_profile_router",
        "status": "low_overflow_lcm_edge_profile_materialized_edge_bounds_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "low_overflow_edge_profile_materialized": True,
        "coprime_boundary_edge_channel_identified": True,
        "small_gcd_overflow_channel_identified": True,
        "coprime_boundary_edge_angle_bound_proved": False,
        "small_gcd_overflow_pdec_excluded": False,
        "low_overflow_shell_angle_bound_proved": False,
        "row_column_unconditional_closed": False,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "value_count": len(values),
        "minimum_coprime_abs_share": min_coprime_share,
        "rows": rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "低超界 tail 可从 `m` 层进一步剥成 `(d,e)` 边："
            "`sum_{D<lcm(d,e)<=16D} lambda_d lambda_e R_lcm(d,e)`。"
            "样本中主通道是 `gcd(d,e)=1` 的 coprime boundary lcm 边，"
            "其余为小 gcd overflow 通道。"
            "因此低超界角度失败可被命名为 coprime boundary edge 异常或 small-gcd overflow PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 低超界 lcm 边画像",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"low_overflow_edge_profile_materialized={fmt_bool(result['low_overflow_edge_profile_materialized'])}",
        f"coprime_boundary_edge_channel_identified={fmt_bool(result['coprime_boundary_edge_channel_identified'])}",
        f"small_gcd_overflow_channel_identified={fmt_bool(result['small_gcd_overflow_channel_identified'])}",
        f"coprime_boundary_edge_angle_bound_proved={fmt_bool(result['coprime_boundary_edge_angle_bound_proved'])}",
        f"small_gcd_overflow_pdec_excluded={fmt_bool(result['small_gcd_overflow_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. coprime vs small-gcd",
        "",
        "| z | low edges | total abs | coprime abs share | coprime weight share | coprime angle | noncoprime angle |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {row['total_low_overflow_edge']['edge_count']} | "
            f"{fmt_float(row['total_low_overflow_edge']['abs_edge_contribution'])} | "
            f"{fmt_float(row['coprime_abs_share'])} | {fmt_float(row['coprime_weight_share'])} | "
            f"{fmt_float(row['coprime_edge']['edge_abs_angle'])} | "
            f"{fmt_float(row['noncoprime_edge']['edge_abs_angle'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 主要 gcd 通道",
            "",
            "| z | gcd | edges | abs contribution | signed/abs | angle |",
            "| ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["rows"]:
        for gcd_row in row["top_gcd_rows"][:8]:
            lines.append(
                f"| {row['z']} | `{gcd_row['label']}` | {gcd_row['edge_count']} | "
                f"{fmt_float(gcd_row['abs_edge_contribution'])} | "
                f"{fmt_float(gcd_row['signed_over_abs'])} | {fmt_float(gcd_row['edge_abs_angle'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已物化：低超界 lcm shell 的 `(d,e)` 边画像。",
            "- 已压缩：低超界失败二分为 coprime boundary edge 与 small-gcd overflow。",
            "- 未闭合：coprime boundary edge 角度界。",
            "- 未闭合：small-gcd overflow PDEC 排斥或吸收。",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z-list", default=",".join(str(item) for item in DEFAULT_Z_LIST))
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--overflow-multiplier", type=int, default=DEFAULT_OVERFLOW_MULTIPLIER)
    args = parser.parse_args()
    result = audit(
        parse_int_list(args.p_list),
        parse_int_list(args.z_list),
        args.d_level,
        args.overflow_multiplier,
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "minimum_coprime_abs_share": result["minimum_coprime_abs_share"],
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
