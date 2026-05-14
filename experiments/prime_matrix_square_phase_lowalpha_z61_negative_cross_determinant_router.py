#!/usr/bin/env python3
"""审计 z=61 高壳负 profile 比例带的 2x2 交叉行列式形式。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_negative_cross_determinant_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
NEGATIVE_RATIO_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.md"

NEXT_TARGET = "NegativeProfileTwoOmegaCrossDeterminantBoundOrDeterminantPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.json",
]
TOL = 1e-12


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_negative_cross_determinant_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行 2x2 交叉行列式审计。"""
    data = json.loads(NEGATIVE_RATIO_JSON.read_text(encoding="utf-8"))
    rows = sorted(data["cell_rows"], key=lambda row: row["omega"])
    if len(rows) != 2:
        raise ValueError("expected exactly two high-shell negative rows")

    low, high = rows
    a_low = low["negative_exit_profile_abs"]
    b_low = low["negative_reciprocal_profile_abs"]
    a_high = high["negative_exit_profile_abs"]
    b_high = high["negative_reciprocal_profile_abs"]

    low_ratio = safe_ratio(a_low, b_low)
    high_ratio = safe_ratio(a_high, b_high)
    ratio_spread = None if low_ratio is None or high_ratio is None else high_ratio - low_ratio
    cross_determinant = a_high * b_low - a_low * b_high
    normalized_cross_determinant = safe_ratio(cross_determinant, b_low * b_high)
    exit_scale = safe_ratio(a_high, a_low)
    reciprocal_scale = safe_ratio(b_high, b_low)
    scale_ratio = None if exit_scale is None or reciprocal_scale is None else safe_ratio(exit_scale, reciprocal_scale)
    relative_scale_gap = None if scale_ratio is None else scale_ratio - 1.0
    log_scale_gap = None
    if exit_scale is not None and reciprocal_scale is not None and exit_scale > 0 and reciprocal_scale > 0:
        log_scale_gap = math.log(exit_scale) - math.log(reciprocal_scale)

    determinant_identity_error = (
        None if ratio_spread is None or normalized_cross_determinant is None else ratio_spread - normalized_cross_determinant
    )
    scale_identity_error = None
    if relative_scale_gap is not None and low_ratio is not None and high_ratio is not None:
        scale_identity_error = high_ratio / low_ratio - 1.0 - relative_scale_gap

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_negative_cross_determinant_router",
        "status": "z61_negative_profile_ratio_band_reduced_to_two_by_two_cross_determinant_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "target_bucket": data["target_bucket"],
        "target_shell": data["target_shell"],
        "target_sign_word": data["target_sign_word"],
        "low_omega": low["omega"],
        "high_omega": high["omega"],
        "negative_exit_prime": 10007,
        "negative_reciprocal_prime": 36739,
        "low_negative_exit_abs": a_low,
        "low_negative_reciprocal_abs": b_low,
        "high_negative_exit_abs": a_high,
        "high_negative_reciprocal_abs": b_high,
        "low_negative_ratio": low_ratio,
        "high_negative_ratio": high_ratio,
        "ratio_spread": ratio_spread,
        "cross_determinant": cross_determinant,
        "normalized_cross_determinant": normalized_cross_determinant,
        "determinant_identity_error": determinant_identity_error,
        "determinant_identity_closed": (
            determinant_identity_error is not None and abs(determinant_identity_error) <= TOL
        ),
        "exit_abs_scale_high_over_low": exit_scale,
        "reciprocal_abs_scale_high_over_low": reciprocal_scale,
        "scale_ratio_exit_over_reciprocal": scale_ratio,
        "relative_scale_gap": relative_scale_gap,
        "log_scale_gap": log_scale_gap,
        "scale_identity_error": scale_identity_error,
        "scale_gap_identity_closed": scale_identity_error is not None and abs(scale_identity_error) <= TOL,
        "sample_ratio_band_width_below_point_10": ratio_spread is not None and 0 <= ratio_spread <= 0.10,
        "cross_determinant_bound_point_10_holds_in_sample": (
            normalized_cross_determinant is not None and 0 <= normalized_cross_determinant <= 0.10
        ),
        "negative_cross_determinant_bound_proved": False,
        "determinant_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "两个高壳负 profile 比例带已等价改写为一个 2x2 交叉行列式界："
            "`ratio_spread=(a4*b3-a3*b4)/(b3*b4)`，其中 "
            "`a=|L_10007|`、`b=|L_36739|`。"
            "样本中 `a` 的 omega 升阶尺度只比 `b` 的尺度高约 8.79%，"
            "因此下一步最窄硬点是证明该交叉行列式/尺度失配有全局上界，"
            "或把持续失配登记为 Determinant-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 负 profile 交叉行列式",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"low_omega={result['low_omega']}",
        f"high_omega={result['high_omega']}",
        f"low_negative_ratio={fmt_float(result['low_negative_ratio'])}",
        f"high_negative_ratio={fmt_float(result['high_negative_ratio'])}",
        f"ratio_spread={fmt_float(result['ratio_spread'])}",
        f"cross_determinant={fmt_float(result['cross_determinant'])}",
        f"normalized_cross_determinant={fmt_float(result['normalized_cross_determinant'])}",
        f"determinant_identity_error={fmt_float(result['determinant_identity_error'])}",
        f"exit_abs_scale_high_over_low={fmt_float(result['exit_abs_scale_high_over_low'])}",
        f"reciprocal_abs_scale_high_over_low={fmt_float(result['reciprocal_abs_scale_high_over_low'])}",
        f"relative_scale_gap={fmt_float(result['relative_scale_gap'])}",
        f"negative_cross_determinant_bound_proved={fmt_bool(result['negative_cross_determinant_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价式",
        "",
        "令 `a_i=|L_10007(omega=i)|`，`b_i=|L_36739(omega=i)|`。两个比例的带宽满足：",
        "",
        "```text",
        "a_4/b_4 - a_3/b_3 = (a_4*b_3 - a_3*b_4)/(b_3*b_4)",
        "```",
        "",
        "因此证明比例带宽小，等价于证明 `a` 相对 `b` 的升阶尺度没有产生大交叉行列式。",
        "",
        "## 2. 证明边界",
        "",
        "- 已闭合：比例带到账本 2x2 交叉行列式的精确等价。",
        "- 未闭合：交叉行列式全局上界，或 Determinant-PDEC 排斥。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 3. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
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
                "determinant_identity_closed": result["determinant_identity_closed"],
                "normalized_cross_determinant": result["normalized_cross_determinant"],
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
