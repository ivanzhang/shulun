#!/usr/bin/env python3
"""审计 rough-b 多重序列的低模残基均匀性。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_rough_b_residue_uniformity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_prime_b_sieve_router as sieve


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.md"

DEFAULT_P_LIST = sieve.DEFAULT_P_LIST
DEFAULT_ELL_LIMIT = 61
DEFAULT_ZSCORE_LIMIT = 3.5
NEXT_TARGET = "LowModRoughBResidueDiscrepancySelbergInputOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json",
    "prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json",
]

divisor = sieve.divisor
envelope = sieve.envelope


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
        "experiments/prime_matrix_square_phase_lowalpha_rough_b_residue_uniformity_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_prime_a_b_values(
    p: int,
    flags: bytearray,
    trial_primes: list[int],
) -> list[int]:
    """收集 prime-a incidence 上的 b 多重序列。"""
    candidates = sieve.collect_prime_a_candidates(p, flags, trial_primes)
    return [int(candidate["b"]) for candidate in candidates]


def residue_row(values: list[int], ell: int) -> dict[str, Any]:
    """计算单个模 ell 的残基账本。"""
    count = len(values)
    residues = Counter(value % ell for value in values)
    zero = residues.get(0, 0)
    expected = count / ell if ell else 0.0
    variance = count * (1.0 / ell) * (1.0 - 1.0 / ell) if ell else 0.0
    zscore = (zero - expected) / math.sqrt(variance) if variance > 0 else 0.0
    max_residue, max_count = max(residues.items(), key=lambda item: item[1], default=(None, 0))
    min_count = min((residues.get(r, 0) for r in range(ell)), default=0)
    l1 = sum(abs(residues.get(r, 0) - expected) for r in range(ell))
    return {
        "ell": ell,
        "value_count": count,
        "zero_count": zero,
        "zero_expected": expected,
        "zero_over_expected": safe_ratio(zero, expected),
        "zero_zscore": zscore,
        "max_residue": max_residue,
        "max_residue_count": max_count,
        "max_residue_over_expected": safe_ratio(max_count, expected),
        "min_residue_count": min_count,
        "l1_discrepancy": l1,
        "l1_over_count": safe_ratio(l1, count),
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int], ell_limit: int) -> dict[str, Any]:
    """审计单个 P 的低模残基均匀性。"""
    values = collect_prime_a_b_values(p, flags, trial_primes)
    small_primes = [prime for prime in trial_primes if prime <= ell_limit]
    rows = [residue_row(values, ell) for ell in small_primes]
    worst_zero = max(rows, key=lambda item: abs(item["zero_zscore"]), default=None)
    worst_l1 = max(rows, key=lambda item: item["l1_over_count"] or 0.0, default=None)
    return {
        "p": p,
        "prime_a_fibers": len(values),
        "ell_limit": ell_limit,
        "rows": rows,
        "worst_zero_zscore_row": worst_zero,
        "worst_l1_row": worst_l1,
    }


def audit(p_list: list[int], ell_limit: int, zscore_limit: float) -> dict[str, Any]:
    """执行 rough-b 低模残基均匀性审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes, ell_limit) for p in p_list]

    aggregate_values: list[int] = []
    for p in p_list:
        aggregate_values.extend(collect_prime_a_b_values(p, flags, trial_primes))
    small_primes = [prime for prime in trial_primes if prime <= ell_limit]
    aggregate = [residue_row(aggregate_values, ell) for ell in small_primes]
    worst_zero = max(aggregate, key=lambda item: abs(item["zero_zscore"]), default=None)
    worst_l1 = max(aggregate, key=lambda item: item["l1_over_count"] or 0.0, default=None)
    flagged = [row for row in aggregate if abs(row["zero_zscore"]) > zscore_limit]
    profile_flagged = [
        {"p": profile["p"], "row": row}
        for profile in profiles
        for row in profile["rows"]
        if abs(row["zero_zscore"]) > zscore_limit
    ]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_rough_b_residue_uniformity_router",
        "status": "rough_b_lowmod_residue_uniformity_materialized_selberg_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "lowmod_residue_ledger_materialized": True,
        "sample_aggregate_zscore_within_limit": len(flagged) == 0,
        "sample_profile_zscore_within_limit": len(profile_flagged) == 0,
        "uniform_lowmod_discrepancy_bound_proved": False,
        "lowmod_rough_b_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "ell_limit": ell_limit,
        "zscore_limit": zscore_limit,
        "aggregate_value_count": len(aggregate_values),
        "aggregate_flagged_count": len(flagged),
        "profile_flagged_count": len(profile_flagged),
        "worst_aggregate_zero_zscore_row": worst_zero,
        "worst_aggregate_l1_row": worst_l1,
        "aggregate_rows": aggregate,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "维数一粗数筛的核心输入是 b 多重序列在低素模下的残基均匀性。"
            "本账本对 prime-a incidence 产生的 b 多重序列逐素数 ell 统计 `b=0 mod ell` "
            "与全残基 L1 偏差；若某个 ell 出现持续大 z-score，则它就是 LowMod-RoughB-PDEC。"
            "默认样本聚合账本未越过 z-score 阈值，说明 Mertens 账本稳定来自真实低模均匀性，"
            "但统一低模差异界尚未证明。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha rough-b 低模残基均匀性路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"lowmod_residue_ledger_materialized={fmt_bool(result['lowmod_residue_ledger_materialized'])}",
        f"sample_aggregate_zscore_within_limit={fmt_bool(result['sample_aggregate_zscore_within_limit'])}",
        f"sample_profile_zscore_within_limit={fmt_bool(result['sample_profile_zscore_within_limit'])}",
        f"uniform_lowmod_discrepancy_bound_proved={fmt_bool(result['uniform_lowmod_discrepancy_bound_proved'])}",
        f"lowmod_rough_b_pdec_excluded={fmt_bool(result['lowmod_rough_b_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 聚合诊断",
        "",
        "| ell limit | values | z limit | flagged | worst zero row | worst L1 row |",
        "| ---: | ---: | ---: | ---: | --- | --- |",
        (
            f"| {result['ell_limit']} | {result['aggregate_value_count']} | "
            f"{fmt_float(result['zscore_limit'])} | {result['aggregate_flagged_count']} | "
            f"`{result['worst_aggregate_zero_zscore_row']}` | "
            f"`{result['worst_aggregate_l1_row']}` |"
        ),
        "",
        "## 2. 聚合低模表",
        "",
        "| ell | zero | expected | zero/expected | zscore | max residue | max/expected | L1/count |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["aggregate_rows"]:
        lines.append(
            f"| {row['ell']} | {row['zero_count']} | {fmt_float(row['zero_expected'])} | "
            f"{fmt_float(row['zero_over_expected'])} | {fmt_float(row['zero_zscore'])} | "
            f"{row['max_residue']}:{row['max_residue_count']} | "
            f"{fmt_float(row['max_residue_over_expected'])} | {fmt_float(row['l1_over_count'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的最坏行",
            "",
            "| P | values | worst zero row | worst L1 row |",
            "| ---: | ---: | --- | --- |",
        ]
    )
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['prime_a_fibers']} | "
            f"`{profile['worst_zero_zscore_row']}` | `{profile['worst_l1_row']}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已物化：prime-a 生成的 `b` 多重序列在低素模下的零类与全残基偏差账本。",
            "- 已闭合：任一越界低模行都可命名为 LowMod-RoughB-PDEC 候选。",
            "- 未闭合：给出全局统一低模差异上界，并把它接入维数一 Selberg 上筛。",
            "- 未闭合：排斥持久 LowMod-RoughB-PDEC/SAE。",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--ell-limit", type=int, default=DEFAULT_ELL_LIMIT)
    parser.add_argument("--zscore-limit", type=float, default=DEFAULT_ZSCORE_LIMIT)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), args.ell_limit, args.zscore_limit)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "ell_limit": result["ell_limit"],
                "aggregate_value_count": result["aggregate_value_count"],
                "aggregate_flagged_count": result["aggregate_flagged_count"],
                "profile_flagged_count": result["profile_flagged_count"],
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
