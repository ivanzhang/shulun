#!/usr/bin/env python3
"""审计 z=61 核心因子残差身份中的精确商锁。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_core_quotient_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.md"

NEXT_TARGET = "CoreQuotientLockGlobalExclusionOrQuotientLockPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_core_quotient_lock_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def positive_integer_solution_rows(limit: int) -> list[dict[str, Any]]:
    """枚举消元公式的正整数解，用作机器校验。"""
    rows = []
    for a in range(1, limit + 1):
        denominator = a * a - 126
        numerator = 2 * a - 117
        if denominator == 0:
            continue
        b = Fraction(numerator, denominator)
        if b.denominator != 1 or b.numerator <= 0:
            continue
        c_numerator = a * b.numerator - 2
        if c_numerator % 9 != 0:
            continue
        c = c_numerator // 9
        if c <= 0:
            continue
        q4 = 2 * b.numerator - 1
        q2 = 3 * c + 2
        if a * c + 6 == 7 * q4 and a * b.numerator + 4 == 3 * q2:
            rows.append({"a": a, "b": b.numerator, "c": c, "q4": q4, "q2": q2})
    return rows


def small_a_table() -> list[dict[str, str]]:
    """列出正解可能区间中的小 a 候选。"""
    rows = []
    for a in range(1, 12):
        denominator = a * a - 126
        numerator = 2 * a - 117
        value = Fraction(numerator, denominator)
        rows.append(
            {
                "a": str(a),
                "b_formula": f"{value.numerator}/{value.denominator}"
                if value.denominator != 1
                else str(value.numerator),
                "positive_integer": str(value.denominator == 1 and value.numerator > 0).lower(),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行精确商锁审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    a, b, c = source["core_factorization"]
    q4 = source["q4"]
    q2 = source["q2"]
    q4_quotient = (a * c + 6) // q4
    q2_quotient = (a * b + 4) // q2
    q4_exact = a * c + 6 == q4_quotient * q4
    q2_exact = a * b + 4 == q2_quotient * q2
    solution_rows = positive_integer_solution_rows(10000)
    selected_solution = {"a": a, "b": b, "c": c, "q4": q4, "q2": q2}

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_core_quotient_lock_router",
        "status": "z61_core_factor_residue_identities_reduced_to_unique_quotient_lock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "core_factorization": [a, b, c],
        "q4": q4,
        "q2": q2,
        "q4_lock_equation": "a*c+6=7*(2*b-1)",
        "q2_lock_equation": "a*b+4=3*(3*c+2)",
        "q4_exact_quotient": q4_quotient,
        "q2_exact_quotient": q2_quotient,
        "q4_exact_quotient_lock_closed": q4_exact and q4_quotient == 7,
        "q2_exact_quotient_lock_closed": q2_exact and q2_quotient == 3,
        "eliminated_b_formula": "b=(2*a-117)/(a^2-126)",
        "selected_solution": selected_solution,
        "positive_integer_solution_scan_limit": 10000,
        "positive_integer_solution_rows": solution_rows,
        "positive_integer_solution_unique_in_scan": solution_rows == [selected_solution],
        "small_a_exclusion_table": small_a_table(),
        "sign_exclusion_for_a_ge_12": (
            "12<=a<=58 gives numerator<0<denominator; "
            "a>=59 gives 0<(2a-117)/(a^2-126)<1; "
            "therefore only a<=11 needs finite checking."
        ),
        "quotient_lock_unique_positive_integer_solution_proved": solution_rows == [selected_solution],
        "core_quotient_lock_global_exclusion_proved": False,
        "quotient_lock_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "核心因子残差身份可压成两个精确商锁：`a*c+6=7*(2*b-1)` 与 "
            "`a*b+4=3*(3*c+2)`。消去 `c` 得 `b=(2a-117)/(a^2-126)`；"
            "正整数解被符号区间和 `a<=11` 的有限检查压成唯一解 "
            "`(a,b,c)=(11,19,23)`，从而 `q4=37,q2=71`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 core quotient lock",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"q4_exact_quotient_lock_closed={fmt_bool(result['q4_exact_quotient_lock_closed'])}",
        f"q2_exact_quotient_lock_closed={fmt_bool(result['q2_exact_quotient_lock_closed'])}",
        f"eliminated_b_formula={result['eliminated_b_formula']}",
        f"positive_integer_solution_unique_in_scan={fmt_bool(result['positive_integer_solution_unique_in_scan'])}",
        f"quotient_lock_unique_positive_integer_solution_proved={fmt_bool(result['quotient_lock_unique_positive_integer_solution_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确商锁",
        "",
        "| side | equation | quotient | closed |",
        "| --- | --- | ---: | --- |",
        f"| q4 | `{result['q4_lock_equation']}` | {result['q4_exact_quotient']} | "
        f"{fmt_bool(result['q4_exact_quotient_lock_closed'])} |",
        f"| q2 | `{result['q2_lock_equation']}` | {result['q2_exact_quotient']} | "
        f"{fmt_bool(result['q2_exact_quotient_lock_closed'])} |",
        "",
        "## 2. 消元",
        "",
        "设 `q4=2b-1`、`q2=3c+2`，两个商锁为：",
        "",
        "```text",
        "ac+6=7(2b-1),",
        "ab+4=3(3c+2).",
        "```",
        "",
        "第二式给 `c=(ab-2)/9`。代回第一式得：",
        "",
        "```text",
        "b(a^2-126)=2a-117,",
        "b=(2a-117)/(a^2-126).",
        "```",
        "",
        result["sign_exclusion_for_a_ge_12"],
        "",
        "## 3. 小 a 有限检查",
        "",
        "| a | b formula | positive integer |",
        "| ---: | ---: | --- |",
    ]
    for row in result["small_a_exclusion_table"]:
        lines.append(f"| {row['a']} | `{row['b_formula']}` | {row['positive_integer']} |")
    lines.extend(
        [
            "",
            "## 4. 正整数解",
            "",
            "| a | b | c | q4 | q2 |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["positive_integer_solution_rows"]:
        lines.append(f"| {row['a']} | {row['b']} | {row['c']} | {row['q4']} | {row['q2']} |")
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：同一精确商锁模板下，正整数解唯一，必为 `11,19,23`。",
            "- 未闭合：全局排斥该唯一商锁模板作为反例贴边源，或登记并排斥 QuotientLock-PDEC。",
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
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "quotient_lock_unique_positive_integer_solution_proved": result[
                    "quotient_lock_unique_positive_integer_solution_proved"
                ],
                "selected_solution": result["selected_solution"],
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
