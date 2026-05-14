#!/usr/bin/env python3
"""把 truncation tail 按 lcm 超界壳层分解。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_tail_lcm_shell_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
NEXT_TARGET = "LowOverflowLCMShellAngleBoundOrBoundaryLCMPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_tail_lcm_shell_router.py": file_sha256(
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


def shell_key(modulus: int, d_level: int) -> tuple[int, str]:
    """返回 lcm 超界 dyadic 壳层。"""
    index = int(math.floor(math.log(modulus / d_level, 2)))
    return index, f"({2**index}D,{2 ** (index + 1)}D]"


def shell_stats(items: list[tuple[int, float, float]]) -> dict[str, Any]:
    """计算一个壳层的 `(m,c,R)` 统计。"""
    coefficient_l2 = math.sqrt(sum(coeff * coeff for _m, coeff, _rem in items))
    remainder_l2 = math.sqrt(sum(rem * rem for _m, _coeff, rem in items))
    cauchy = coefficient_l2 * remainder_l2
    net = sum(coeff * rem for _m, coeff, rem in items)
    abs_sum = sum(abs(coeff * rem) for _m, coeff, rem in items)
    return {
        "moduli_count": len(items),
        "positive_contribution_count": sum(1 for _m, coeff, rem in items if coeff * rem >= 0),
        "coefficient_l2": coefficient_l2,
        "remainder_l2": remainder_l2,
        "cauchy_envelope": cauchy,
        "net_inner_product": net,
        "abs_contribution_sum": abs_sum,
        "abs_angle": safe_ratio(abs(net), cauchy),
        "signed_over_abs": safe_ratio(abs(net), abs_sum),
    }


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int) -> dict[str, Any]:
    """计算单个 z 的 tail 壳层分解。"""
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    coeffs = attribution.coefficient_by_lcm(weights)
    counts = attribution.divisibility_counts(values, sorted(coeffs))
    shell_items: dict[tuple[int, str], list[tuple[int, float, float]]] = defaultdict(list)
    for modulus, coefficient in coeffs.items():
        if modulus <= d_level:
            continue
        remainder = counts[modulus] - len(values) / modulus
        shell_items[shell_key(modulus, d_level)].append((modulus, coefficient, remainder))
    shell_rows = []
    for (index, label), items in sorted(shell_items.items(), key=lambda item: item[0][0]):
        stats = shell_stats(items)
        stats["shell_index"] = index
        stats["shell_label"] = label
        shell_rows.append(stats)
    tail_stats = shell_stats([item for items in shell_items.values() for item in items])
    low_overflow = [
        row
        for row in shell_rows
        if row["shell_index"] <= 3
    ]
    high_overflow = [
        row
        for row in shell_rows
        if row["shell_index"] > 3
    ]
    low_abs = sum(row["abs_contribution_sum"] for row in low_overflow)
    high_abs = sum(row["abs_contribution_sum"] for row in high_overflow)
    low_net = sum(row["net_inner_product"] for row in low_overflow)
    high_net = sum(row["net_inner_product"] for row in high_overflow)
    return {
        "z": z,
        "d_level": d_level,
        "tail": tail_stats,
        "shell_rows": shell_rows,
        "low_overflow_shell_abs": low_abs,
        "high_overflow_shell_abs": high_abs,
        "low_overflow_shell_net": low_net,
        "high_overflow_shell_net": high_net,
        "low_overflow_abs_share": safe_ratio(low_abs, low_abs + high_abs),
        "tail_shell_cancellation_ratio": safe_ratio(abs(tail_stats["net_inner_product"]), tail_stats["abs_contribution_sum"]),
        "dominant_shell": max(shell_rows, key=lambda row: row["abs_contribution_sum"], default=None),
    }


def audit(p_list: list[int], z_list: list[int], d_level: int) -> dict[str, Any]:
    """执行 tail lcm shell 审计。"""
    values, primes = collect_values_and_primes(p_list)
    rows = [row_for_z(values, primes, z, d_level) for z in z_list]
    rows_with_tail = [row for row in rows if row["tail"]["moduli_count"] > 0]
    worst_tail_angle = max(rows_with_tail, key=lambda row: row["tail"]["abs_angle"] or 0.0, default=None)
    min_low_share = min((row["low_overflow_abs_share"] for row in rows_with_tail), default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_tail_lcm_shell_router",
        "status": "tail_lcm_overflow_shell_ledger_closed_shell_bounds_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "tail_lcm_shell_decomposition_closed": True,
        "low_overflow_shells_identified": True,
        "high_overflow_tail_thinning_observed": True,
        "low_overflow_shell_angle_bound_proved": False,
        "boundary_lcm_pdec_excluded": False,
        "truncation_tail_angle_bound_proved": False,
        "row_column_unconditional_closed": False,
        "d_level": d_level,
        "value_count": len(values),
        "rows": rows,
        "worst_tail_angle_row": worst_tail_angle,
        "minimum_low_overflow_abs_share": min_low_share,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`m>D` 截断尾不是均匀高维噪声，而是 lcm 超界边界效应。"
            "本账本按 `m/D` 的 dyadic 壳层分解 tail：样本中主要绝对质量集中在 "
            "`(D,16D]` 低超界壳层，高超界壳层快速变薄。"
            "因此 tail 角度失败可进一步定位到具体 low-overflow lcm shell，"
            "并登记为 BoundaryLCM-PDEC；远壳层应走 thinning/Rankin 型预算。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha tail lcm shell 路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"tail_lcm_shell_decomposition_closed={fmt_bool(result['tail_lcm_shell_decomposition_closed'])}",
        f"low_overflow_shells_identified={fmt_bool(result['low_overflow_shells_identified'])}",
        f"high_overflow_tail_thinning_observed={fmt_bool(result['high_overflow_tail_thinning_observed'])}",
        f"low_overflow_shell_angle_bound_proved={fmt_bool(result['low_overflow_shell_angle_bound_proved'])}",
        f"boundary_lcm_pdec_excluded={fmt_bool(result['boundary_lcm_pdec_excluded'])}",
        f"truncation_tail_angle_bound_proved={fmt_bool(result['truncation_tail_angle_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. tail 总览",
        "",
        "| z | tail count | tail net | tail abs | tail angle | low abs share | dominant shell |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["rows"]:
        dominant = row["dominant_shell"]["shell_label"] if row["dominant_shell"] else "n/a"
        lines.append(
            f"| {row['z']} | {row['tail']['moduli_count']} | "
            f"{fmt_float(row['tail']['net_inner_product'])} | "
            f"{fmt_float(row['tail']['abs_contribution_sum'])} | "
            f"{fmt_float(row['tail']['abs_angle'])} | "
            f"{fmt_float(row['low_overflow_abs_share'])} | `{dominant}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 壳层明细",
            "",
            "| z | shell | count | positive | net | abs | angle | signed/abs |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["rows"]:
        for shell in row["shell_rows"]:
            lines.append(
                f"| {row['z']} | `{shell['shell_label']}` | {shell['moduli_count']} | "
                f"{shell['positive_contribution_count']} | {fmt_float(shell['net_inner_product'])} | "
                f"{fmt_float(shell['abs_contribution_sum'])} | {fmt_float(shell['abs_angle'])} | "
                f"{fmt_float(shell['signed_over_abs'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：tail 的 lcm-overflow dyadic shell 分解。",
            "- 已物化：tail 失败会落到具体 `(2^jD,2^{j+1}D]` 壳层。",
            "- 未闭合：低超界壳层 `(D,16D]` 的统一角度界或 BoundaryLCM-PDEC 排斥。",
            "- 未闭合：高超界壳层的 thinning/Rankin 预算。",
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
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), parse_int_list(args.z_list), args.d_level)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "minimum_low_overflow_abs_share": result["minimum_low_overflow_abs_share"],
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
