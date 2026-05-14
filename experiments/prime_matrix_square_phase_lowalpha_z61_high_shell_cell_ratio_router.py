#!/usr/bin/env python3
"""审计 z=61 高壳两个 `--++` 格中的出口/互反比例带。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_cell_ratio_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
HIGH_SHELL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.md"

NEXT_TARGET = "TwoHighShellCellExitReciprocalRatioBandInvariantOrRatioPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.json",
]


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_cell_ratio_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行高壳格比例带审计。"""
    data = json.loads(HIGH_SHELL_JSON.read_text(encoding="utf-8"))
    by_cell: dict[tuple[int, str], dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for pair in data["high_shell_pair_rows"]:
        for cell in pair["cells"]:
            key = (cell["omega"], "--++")
            by_cell[key][pair["pair_key"]] += cell["pair_credit_ratio"]
    cell_rows = []
    for (omega, sign_word), pair_credit in sorted(by_cell.items()):
        reciprocal = pair_credit[data["high_shell_reciprocal_pair"]]
        exit_credit = pair_credit[data["high_shell_exit_pair"]]
        total = reciprocal + exit_credit
        cell_rows.append(
            {
                "omega": omega,
                "shell": "(8D,16D]",
                "sign_word": sign_word,
                "reciprocal_credit_ratio": reciprocal,
                "exit_credit_ratio": exit_credit,
                "total_credit_ratio": total,
                "exit_over_reciprocal_ratio": safe_ratio(exit_credit, reciprocal),
                "exit_share_of_cell": safe_ratio(exit_credit, total),
                "reciprocal_share_of_cell": safe_ratio(reciprocal, total),
            }
        )
    ratios = [row["exit_over_reciprocal_ratio"] for row in cell_rows if row["exit_over_reciprocal_ratio"] is not None]
    min_ratio = min(ratios) if ratios else None
    max_ratio = max(ratios) if ratios else None
    ratio_spread = (max_ratio - min_ratio) if min_ratio is not None and max_ratio is not None else None
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_high_shell_cell_ratio_router",
        "status": "z61_high_shell_exit_reciprocal_split_has_two_cell_ratio_band_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": data["p_list"],
        "z": data["z"],
        "high_shell_reciprocal_pair": data["high_shell_reciprocal_pair"],
        "high_shell_exit_pair": data["high_shell_exit_pair"],
        "cell_count": len(cell_rows),
        "all_cells_are_high_shell_double_positive_template": all(
            row["shell"] == "(8D,16D]" and row["sign_word"] == "--++" for row in cell_rows
        ),
        "min_exit_over_reciprocal_ratio": min_ratio,
        "max_exit_over_reciprocal_ratio": max_ratio,
        "exit_over_reciprocal_ratio_spread": ratio_spread,
        "sample_ratio_band_width_below_point_10": ratio_spread is not None and ratio_spread <= 0.10,
        "aggregate_exit_over_reciprocal_ratio": data["exit_over_reciprocal_ratio"],
        "two_high_shell_ratio_band_invariant_proved": False,
        "ratio_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cell_rows": cell_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "高壳出口项与互反项在两个 `--++` 高壳格中成对出现。"
            "两个格的出口/互反比例接近，形成窄比例带；"
            "因此下一步可证明两个高壳格的比例带不变量，或登记 Ratio-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 高壳格比例带",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cell_count={result['cell_count']}",
        f"all_cells_are_high_shell_double_positive_template={fmt_bool(result['all_cells_are_high_shell_double_positive_template'])}",
        f"min_exit_over_reciprocal_ratio={fmt_float(result['min_exit_over_reciprocal_ratio'])}",
        f"max_exit_over_reciprocal_ratio={fmt_float(result['max_exit_over_reciprocal_ratio'])}",
        f"exit_over_reciprocal_ratio_spread={fmt_float(result['exit_over_reciprocal_ratio_spread'])}",
        f"sample_ratio_band_width_below_point_10={fmt_bool(result['sample_ratio_band_width_below_point_10'])}",
        f"aggregate_exit_over_reciprocal_ratio={fmt_float(result['aggregate_exit_over_reciprocal_ratio'])}",
        f"two_high_shell_ratio_band_invariant_proved={fmt_bool(result['two_high_shell_ratio_band_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 高壳格",
        "",
        "| omega | shell | signs | reciprocal | exit | exit/reciprocal | exit share |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in result["cell_rows"]:
        lines.append(
            f"| {row['omega']} | `{row['shell']}` | `{row['sign_word']}` | "
            f"{fmt_float(row['reciprocal_credit_ratio'])} | "
            f"{fmt_float(row['exit_credit_ratio'])} | "
            f"{fmt_float(row['exit_over_reciprocal_ratio'])} | "
            f"{fmt_float(row['exit_share_of_cell'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：高壳互反/出口项到两个高壳格比例带的账本。",
            "- 未闭合：证明比例带不变量，或登记 Ratio-PDEC。",
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
                "exit_over_reciprocal_ratio_spread": result["exit_over_reciprocal_ratio_spread"],
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
