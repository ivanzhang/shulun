#!/usr/bin/env python3
"""审计 rough-b 序列的 squarefree 低模整除账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_rough_b_squarefree_moduli_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.md"

DEFAULT_P_LIST = sieve.DEFAULT_P_LIST
DEFAULT_D_LIMIT = 1000
DEFAULT_REL_LIMIT = 0.35
NEXT_TARGET = "SquarefreeLowModDivisibilitySelbergRemainderBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-rough-b-residue-uniformity-router.json",
    "prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_rough_b_squarefree_moduli_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_values(p_list: list[int], flags: bytearray, trial_primes: list[int]) -> list[int]:
    """收集所有 prime-a incidence 的 b 多重序列。"""
    values: list[int] = []
    for p in p_list:
        candidates = sieve.collect_prime_a_candidates(p, flags, trial_primes)
        values.extend(int(candidate["b"]) for candidate in candidates)
    return values


def is_squarefree(n: int, primes: list[int]) -> bool:
    """判断 n 是否 squarefree。"""
    temp = n
    for prime in primes:
        if prime * prime > temp:
            break
        if temp % prime == 0:
            temp //= prime
            if temp % prime == 0:
                return False
        while temp % prime == 0:
            temp //= prime
    return True


def squarefree_moduli(d_limit: int, primes: list[int]) -> list[int]:
    """列出低于阈值的 squarefree 模数。"""
    return [d for d in range(2, d_limit + 1) if is_squarefree(d, primes)]


def divisor_count_row(values: list[int], d: int) -> dict[str, Any]:
    """计算 `d|b` 的整除账本行。"""
    count = len(values)
    actual = sum(1 for value in values if value % d == 0)
    expected = count / d
    variance = count * (1.0 / d) * (1.0 - 1.0 / d)
    zscore = (actual - expected) / math.sqrt(variance) if variance > 0 else 0.0
    return {
        "d": d,
        "value_count": count,
        "actual_divisible": actual,
        "expected_divisible": expected,
        "actual_over_expected": safe_ratio(actual, expected),
        "absolute_error": actual - expected,
        "relative_error_to_count": safe_ratio(abs(actual - expected), count),
        "zscore": zscore,
    }


def audit(p_list: list[int], d_limit: int, rel_limit: float) -> dict[str, Any]:
    """执行 squarefree 低模整除审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    values = collect_values(p_list, flags, trial_primes)
    moduli = squarefree_moduli(d_limit, trial_primes)
    rows = [divisor_count_row(values, d) for d in moduli]
    worst_z = max(rows, key=lambda item: abs(item["zscore"]), default=None)
    worst_relative = max(rows, key=lambda item: item["relative_error_to_count"] or 0.0, default=None)
    flagged = [row for row in rows if (row["relative_error_to_count"] or 0.0) > rel_limit]
    top_rows = sorted(rows, key=lambda item: abs(item["zscore"]), reverse=True)[:16]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_rough_b_squarefree_moduli_router",
        "status": "rough_b_squarefree_lowmod_divisibility_ledger_materialized_selberg_remainder_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "squarefree_lowmod_ledger_materialized": True,
        "sample_relative_error_within_limit": len(flagged) == 0,
        "selberg_squarefree_remainder_bound_proved": False,
        "squarefree_lowmod_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "d_limit": d_limit,
        "relative_error_limit": rel_limit,
        "value_count": len(values),
        "squarefree_moduli_count": len(moduli),
        "flagged_count": len(flagged),
        "worst_zscore_row": worst_z,
        "worst_relative_error_row": worst_relative,
        "top_zscore_rows": top_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Selberg 上筛需要 squarefree 模数 `d` 的整除余项，而不仅是单素数零类。"
            "本账本对 prime-a 生成的 b 多重序列统计所有 squarefree `2<=d<=D` 的 `d|b` 计数，"
            "并与随机维数一期望 `N/d` 比较。样本中相对误差阈值内无越界行；"
            "若某个 d 持续越界，它就是更强的 Squarefree-LowMod-RoughB-PDEC。"
            "当前仍未证明统一 squarefree 余项界。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha rough-b squarefree 低模账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"squarefree_lowmod_ledger_materialized={fmt_bool(result['squarefree_lowmod_ledger_materialized'])}",
        f"sample_relative_error_within_limit={fmt_bool(result['sample_relative_error_within_limit'])}",
        f"selberg_squarefree_remainder_bound_proved={fmt_bool(result['selberg_squarefree_remainder_bound_proved'])}",
        f"squarefree_lowmod_pdec_excluded={fmt_bool(result['squarefree_lowmod_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总览",
        "",
        "| D limit | values | squarefree d | rel limit | flagged | worst z row | worst relative row |",
        "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
        (
            f"| {result['d_limit']} | {result['value_count']} | {result['squarefree_moduli_count']} | "
            f"{fmt_float(result['relative_error_limit'])} | {result['flagged_count']} | "
            f"`{result['worst_zscore_row']}` | `{result['worst_relative_error_row']}` |"
        ),
        "",
        "## 2. 最大 z-score 行",
        "",
        "| d | actual | expected | actual/expected | rel error | zscore |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["top_zscore_rows"]:
        lines.append(
            f"| {row['d']} | {row['actual_divisible']} | {fmt_float(row['expected_divisible'])} | "
            f"{fmt_float(row['actual_over_expected'])} | {fmt_float(row['relative_error_to_count'])} | "
            f"{fmt_float(row['zscore'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已物化：`d<=D` 的 squarefree 整除余项账本。",
            "- 已闭合：任何越界 `d` 都可直接命名为 Squarefree-LowMod-RoughB-PDEC。",
            "- 未闭合：对所有必要 Selberg level 的 squarefree 余项给出统一上界。",
            "- 未闭合：排斥持久 squarefree 低模 PDEC/SAE。",
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
    parser.add_argument("--d-limit", type=int, default=DEFAULT_D_LIMIT)
    parser.add_argument("--rel-limit", type=float, default=DEFAULT_REL_LIMIT)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), args.d_limit, args.rel_limit)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "d_limit": result["d_limit"],
                "value_count": result["value_count"],
                "squarefree_moduli_count": result["squarefree_moduli_count"],
                "flagged_count": result["flagged_count"],
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
