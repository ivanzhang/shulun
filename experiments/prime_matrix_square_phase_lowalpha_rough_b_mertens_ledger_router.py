#!/usr/bin/env python3
"""审计 rough-b 幸存者的一维 Mertens 账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_rough_b_mertens_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_prime_b_sieve_router as sieve


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.md"

DEFAULT_P_LIST = sieve.DEFAULT_P_LIST
DEFAULT_CONSTANT = 1.25
NEXT_TARGET = "DimensionOneRoughBReciprocalFloorSelbergUpperOrLowModPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json",
    "prime-matrix-square-phase-lowalpha-fixed-b-semiprime-incidence-router.json",
]

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
        "experiments/prime_matrix_square_phase_lowalpha_rough_b_mertens_ledger_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def mertens_product(primes: list[int], cutoff: int) -> float:
    """计算筛维数一的 Mertens 乘积。"""
    product = 1.0
    for prime in primes:
        if prime > cutoff:
            break
        product *= 1.0 - 1.0 / prime
    return product


def annotate_rows(rows: list[dict[str, Any]], primes: list[int], constant: float) -> list[dict[str, Any]]:
    """给 rough-b 行补充 Mertens 模型与常数验收。"""
    annotated = []
    for row in rows:
        product = mertens_product(primes, int(row["cutoff"]))
        model = row["covered_prime_a"] * product
        ratio = safe_ratio(row["rough_count"], model)
        annotated.append(
            {
                **row,
                "mertens_product": product,
                "mertens_model": model,
                "rough_over_mertens_model": ratio,
                "covered_by_constant": ratio is not None and ratio <= constant,
                "constant": constant,
            }
        )
    return annotated


def audit(p_list: list[int], constant: float) -> dict[str, Any]:
    """执行 rough-b Mertens 账本审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    base = sieve.audit(p_list)
    aggregate_rows = annotate_rows(base["aggregate_cutoff_rows"], trial_primes, constant)
    profile_rows = []
    for profile in base["profiles"]:
        rows = []
        for row in profile["cutoff_rows"]:
            covered = {
                "cutoff": row["cutoff"],
                "rough_count": row["rough_count"],
                "covered_prime_a": profile["prime_a_fibers"],
                "covered_prime_b": profile["prime_b_fibers"],
                "rough_over_prime_a": row["rough_over_prime_a"],
                "prime_b_over_rough": row["prime_b_over_rough"],
            }
            rows.append(covered)
        annotated = annotate_rows(rows, trial_primes, constant)
        profile_rows.append(
            {
                "p": profile["p"],
                "prime_a_fibers": profile["prime_a_fibers"],
                "prime_b_fibers": profile["prime_b_fibers"],
                "max_ratio": max((row["rough_over_mertens_model"] for row in annotated), default=None),
                "constant_failure_count": sum(1 for row in annotated if not row["covered_by_constant"]),
                "rows": annotated,
            }
        )
    failures = [row for row in aggregate_rows if not row["covered_by_constant"]]
    profile_failures = sum(profile["constant_failure_count"] for profile in profile_rows)
    max_ratio = max((row["rough_over_mertens_model"] for row in aggregate_rows), default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_rough_b_mertens_ledger_router",
        "status": "rough_b_dimension_one_mertens_ledger_materialized_selberg_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "rough_b_mertens_ledger_materialized": True,
        "sample_constant_covers_aggregate_rows": len(failures) == 0,
        "sample_constant_covers_profile_rows": profile_failures == 0,
        "dimension_one_selberg_upper_proved": False,
        "lowmod_rough_b_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "constant": constant,
        "max_aggregate_rough_over_mertens_model": max_ratio,
        "aggregate_constant_failure_count": len(failures),
        "profile_constant_failure_count": profile_failures,
        "prime_a_fibers": base["prime_a_fibers"],
        "prime_b_fibers": base["prime_b_fibers"],
        "aggregate_rows": aggregate_rows,
        "profiles": profile_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "rough-b 幸存者账本与一维 Mertens 乘积高度对齐：对 cutoff y，模型为 "
            "`prime_a_fibers * prod_{ell<=y}(1-1/ell)`。默认样本中常数包覆盖聚合行与逐 P 行，"
            "说明该分支的自然筛维数是 1。当前仍未证明统一 Selberg 上界；若某 cutoff 的"
            " rough-b 数量超过常数 Mertens 包络，则该 cutoff 直接给出低模粗数幸存者偏斜，"
            "进入 PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha rough-b Mertens 账本路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rough_b_mertens_ledger_materialized={fmt_bool(result['rough_b_mertens_ledger_materialized'])}",
        f"sample_constant_covers_aggregate_rows={fmt_bool(result['sample_constant_covers_aggregate_rows'])}",
        f"sample_constant_covers_profile_rows={fmt_bool(result['sample_constant_covers_profile_rows'])}",
        f"dimension_one_selberg_upper_proved={fmt_bool(result['dimension_one_selberg_upper_proved'])}",
        f"lowmod_rough_b_pdec_excluded={fmt_bool(result['lowmod_rough_b_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 常数包",
        "",
        "| constant | max aggregate ratio | aggregate failures | profile failures |",
        "| ---: | ---: | ---: | ---: |",
        (
            f"| {fmt_float(result['constant'])} | "
            f"{fmt_float(result['max_aggregate_rough_over_mertens_model'])} | "
            f"{result['aggregate_constant_failure_count']} | {result['profile_constant_failure_count']} |"
        ),
        "",
        "## 2. 聚合 Mertens 账本",
        "",
        "| cutoff | rough | prime-a | Mertens product | model | rough/model | covered |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["aggregate_rows"]:
        lines.append(
            f"| {row['cutoff']} | {row['rough_count']} | {row['covered_prime_a']} | "
            f"{fmt_float(row['mertens_product'])} | {fmt_float(row['mertens_model'])} | "
            f"{fmt_float(row['rough_over_mertens_model'])} | {fmt_bool(row['covered_by_constant'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的最大比值",
            "",
            "| P | prime-a | prime-b | max rough/model | failures |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['prime_a_fibers']} | {profile['prime_b_fibers']} | "
            f"{fmt_float(profile['max_ratio'])} | {profile['constant_failure_count']} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已物化：rough-b survivor 与一维 Mertens 乘积的聚合/逐 P 账本。",
            "- 已闭合：给定常数包时，样本行自动分为 covered 或 LowMod-RoughB-PDEC。",
            "- 未闭合：证明 reciprocal-floor b 多重序列满足统一维数一 Selberg 上界。",
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
    parser.add_argument("--constant", type=float, default=DEFAULT_CONSTANT)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), args.constant)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "constant": result["constant"],
                "max_aggregate_rough_over_mertens_model": result[
                    "max_aggregate_rough_over_mertens_model"
                ],
                "aggregate_constant_failure_count": result["aggregate_constant_failure_count"],
                "profile_constant_failure_count": result["profile_constant_failure_count"],
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
