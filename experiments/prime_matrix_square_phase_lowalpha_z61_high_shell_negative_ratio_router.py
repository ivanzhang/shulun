#!/usr/bin/env python3
"""审计 z=61 高壳出口/互反比的负 profile 来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_negative_ratio_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
CELL_RATIO_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.json"
PROFILE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.md"

TARGET_BUCKET = "unbalanced<=8"
TARGET_SHELL = "(8D,16D]"
TARGET_SIGN_WORD = "--++"
NEGATIVE_EXIT_P = 10007
NEGATIVE_RECIPROCAL_P = 36739
POSITIVE_COMPANION_P = 83561
POSITIVE_SOURCE_P = 200003
TOL = 1e-12

NEXT_TARGET = "HighShellNegativeProfileRatioBandInvariantOrNegativeRatioPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json",
]


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_negative_ratio_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def profile_cell_index(profile_data: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """索引目标 bucket 中两个高壳 `--++` profile 格。"""
    indexed = {}
    for row in profile_data["cell_rows"]:
        if (
            row["bucket"] == TARGET_BUCKET
            and row["shell"] == TARGET_SHELL
            and row["sign_word"] == TARGET_SIGN_WORD
        ):
            indexed[row["omega"]] = row
    return indexed


def get_profile_value(profile_row: dict[str, Any], prime: int) -> float:
    """按来源素数取 profile 线性余项。"""
    for entry in profile_row["profile_entries"]:
        if entry["p"] == prime:
            return entry["linear_remainder"]
    raise KeyError(f"missing profile prime {prime}")


def audit() -> dict[str, Any]:
    """执行负 profile 比例同一性审计。"""
    cell_data = json.loads(CELL_RATIO_JSON.read_text(encoding="utf-8"))
    profile_data = json.loads(PROFILE_JSON.read_text(encoding="utf-8"))
    indexed_profile = profile_cell_index(profile_data)

    rows = []
    ratio_errors = []
    share_errors = []
    for cell in cell_data["cell_rows"]:
        omega = cell["omega"]
        profile = indexed_profile[omega]
        negative_exit = get_profile_value(profile, NEGATIVE_EXIT_P)
        negative_reciprocal = get_profile_value(profile, NEGATIVE_RECIPROCAL_P)
        positive_companion = get_profile_value(profile, POSITIVE_COMPANION_P)
        positive_source = get_profile_value(profile, POSITIVE_SOURCE_P)

        negative_exit_abs = abs(negative_exit)
        negative_reciprocal_abs = abs(negative_reciprocal)
        negative_total_abs = negative_exit_abs + negative_reciprocal_abs
        negative_profile_ratio = safe_ratio(negative_exit_abs, negative_reciprocal_abs)
        negative_exit_share = safe_ratio(negative_exit_abs, negative_total_abs)
        negative_reciprocal_share = safe_ratio(negative_reciprocal_abs, negative_total_abs)
        positive_profile_ratio = safe_ratio(positive_source, positive_companion)

        ratio_error = (
            None
            if negative_profile_ratio is None
            else cell["exit_over_reciprocal_ratio"] - negative_profile_ratio
        )
        exit_share_error = (
            None if negative_exit_share is None else cell["exit_share_of_cell"] - negative_exit_share
        )
        reciprocal_share_error = (
            None
            if negative_reciprocal_share is None
            else cell["reciprocal_share_of_cell"] - negative_reciprocal_share
        )
        if ratio_error is not None:
            ratio_errors.append(abs(ratio_error))
        if exit_share_error is not None:
            share_errors.append(abs(exit_share_error))
        if reciprocal_share_error is not None:
            share_errors.append(abs(reciprocal_share_error))

        rows.append(
            {
                "bucket": TARGET_BUCKET,
                "omega": omega,
                "shell": cell["shell"],
                "sign_word": cell["sign_word"],
                "profile_vector_order": [
                    NEGATIVE_EXIT_P,
                    NEGATIVE_RECIPROCAL_P,
                    POSITIVE_COMPANION_P,
                    POSITIVE_SOURCE_P,
                ],
                "profile_vector": [
                    negative_exit,
                    negative_reciprocal,
                    positive_companion,
                    positive_source,
                ],
                "exit_credit_ratio": cell["exit_credit_ratio"],
                "reciprocal_credit_ratio": cell["reciprocal_credit_ratio"],
                "exit_over_reciprocal_ratio": cell["exit_over_reciprocal_ratio"],
                "negative_exit_profile_abs": negative_exit_abs,
                "negative_reciprocal_profile_abs": negative_reciprocal_abs,
                "negative_profile_abs_ratio": negative_profile_ratio,
                "ratio_identity_error": ratio_error,
                "exit_share_of_cell": cell["exit_share_of_cell"],
                "negative_exit_share": negative_exit_share,
                "exit_share_identity_error": exit_share_error,
                "reciprocal_share_of_cell": cell["reciprocal_share_of_cell"],
                "negative_reciprocal_share": negative_reciprocal_share,
                "reciprocal_share_identity_error": reciprocal_share_error,
                "positive_source_profile": positive_source,
                "positive_companion_profile": positive_companion,
                "positive_source_over_companion_ratio": positive_profile_ratio,
            }
        )

    max_ratio_error = max(ratio_errors) if ratio_errors else None
    max_share_error = max(share_errors) if share_errors else None
    ratio_band = [row["negative_profile_abs_ratio"] for row in rows if row["negative_profile_abs_ratio"] is not None]
    min_ratio = min(ratio_band) if ratio_band else None
    max_ratio = max(ratio_band) if ratio_band else None
    ratio_spread = (max_ratio - min_ratio) if min_ratio is not None and max_ratio is not None else None

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_high_shell_negative_ratio_router",
        "status": "z61_high_shell_exit_reciprocal_ratio_equals_negative_profile_ratio_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": cell_data["z"],
        "target_bucket": TARGET_BUCKET,
        "target_shell": TARGET_SHELL,
        "target_sign_word": TARGET_SIGN_WORD,
        "positive_source_pair": f"{POSITIVE_SOURCE_P}->{NEGATIVE_RECIPROCAL_P}/{NEGATIVE_EXIT_P}",
        "negative_profile_ratio": f"|L_{NEGATIVE_EXIT_P}|/|L_{NEGATIVE_RECIPROCAL_P}|",
        "cell_count": len(rows),
        "max_ratio_identity_error": max_ratio_error,
        "max_share_identity_error": max_share_error,
        "high_shell_negative_profile_ratio_identity_closed": (
            max_ratio_error is not None and max_ratio_error <= TOL and max_share_error is not None and max_share_error <= TOL
        ),
        "min_negative_profile_ratio": min_ratio,
        "max_negative_profile_ratio": max_ratio,
        "negative_profile_ratio_spread": ratio_spread,
        "matches_previous_exit_reciprocal_ratio_band": (
            min_ratio == cell_data["min_exit_over_reciprocal_ratio"]
            and max_ratio == cell_data["max_exit_over_reciprocal_ratio"]
            and ratio_spread == cell_data["exit_over_reciprocal_ratio_spread"]
        ),
        "negative_ratio_band_invariant_proved": False,
        "negative_ratio_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cell_rows": rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "高壳两个 `--++` 格中的出口/互反信用比并非新的自由比例，"
            "而是同一正来源 `200003` 向两个负 profile 端点输送信用时的目标负质量比："
            f"`|L_{NEGATIVE_EXIT_P}|/|L_{NEGATIVE_RECIPROCAL_P}|`。"
            "因此上一层比例带硬点被压成两个负 profile 质量比的稳定性问题；"
            "仍需证明该负 profile 比例带不变量，或登记 NegativeRatio-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 高壳负 profile 比例路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cell_count={result['cell_count']}",
        f"max_ratio_identity_error={fmt_float(result['max_ratio_identity_error'])}",
        f"max_share_identity_error={fmt_float(result['max_share_identity_error'])}",
        f"high_shell_negative_profile_ratio_identity_closed={fmt_bool(result['high_shell_negative_profile_ratio_identity_closed'])}",
        f"min_negative_profile_ratio={fmt_float(result['min_negative_profile_ratio'])}",
        f"max_negative_profile_ratio={fmt_float(result['max_negative_profile_ratio'])}",
        f"negative_profile_ratio_spread={fmt_float(result['negative_profile_ratio_spread'])}",
        f"negative_ratio_band_invariant_proved={fmt_bool(result['negative_ratio_band_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确同一性",
        "",
        "在同一正来源 `200003` 下，规范运输信用对目标负端点成比例，故每个高壳格满足：",
        "",
        "```text",
        "credit(200003->10007) / credit(200003->36739) = |L_10007| / |L_36739|",
        "```",
        "",
        "| omega | profile `[10007,36739,83561,200003]` | exit/reciprocal | negative ratio | error | pos 200003/83561 |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in result["cell_rows"]:
        vector = ", ".join(fmt_float(value) for value in row["profile_vector"])
        lines.append(
            f"| {row['omega']} | `[{vector}]` | "
            f"{fmt_float(row['exit_over_reciprocal_ratio'])} | "
            f"{fmt_float(row['negative_profile_abs_ratio'])} | "
            f"{fmt_float(row['ratio_identity_error'])} | "
            f"{fmt_float(row['positive_source_over_companion_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：高壳出口/互反比例到账本负 profile 质量比的精确同一性。",
            "- 未闭合：两个负 profile 质量比的全局稳定下界/上界，或 NegativeRatio-PDEC 排斥。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "identity_closed": result["high_shell_negative_profile_ratio_identity_closed"],
                "negative_profile_ratio_spread": result["negative_profile_ratio_spread"],
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
