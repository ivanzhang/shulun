#!/usr/bin/env python3
"""把 z=61 唯一五格覆盖压成三壳层阶梯合同。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_three_shell_ladder_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.md
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
MINIMAL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json"
TWO_ARM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.md"

NEXT_TARGET = "ThreeShellLadderSupportInvariantOrShellPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json",
    "prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_three_shell_ladder_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行三壳层阶梯审计。"""
    minimal = json.loads(MINIMAL_JSON.read_text(encoding="utf-8"))
    two_arm = json.loads(TWO_ARM_JSON.read_text(encoding="utf-8"))
    cover_cells = minimal["minimal_cover_rows"][0]["cells"]
    need = minimal["unbalanced_residual_needed_ratio"]

    shell_credit: dict[str, float] = defaultdict(float)
    shell_cells: dict[str, list[dict[str, Any]]] = defaultdict(list)
    shell_pair_credit: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for cell in cover_cells:
        shell = cell["shell"]
        shell_credit[shell] += cell["credit_ratio"]
        shell_cells[shell].append(cell)
        for pair in cell["pairs"]:
            shell_pair_credit[shell][pair["pair_key"]] += pair["pair_credit_ratio"]

    shell_order = ["(2D,4D]", "(4D,8D]", "(8D,16D]"]
    shell_rows = []
    cumulative = 0.0
    for shell in shell_order:
        credit = shell_credit[shell]
        cumulative += credit
        shell_rows.append(
            {
                "shell": shell,
                "credit_ratio": credit,
                "share_of_need": safe_ratio(credit, need),
                "cumulative_credit_ratio": cumulative,
                "cumulative_deficit_ratio": max(0.0, need - cumulative),
                "cell_count": len(shell_cells[shell]),
                "cells": shell_cells[shell],
                "pair_rows": [
                    {
                        "pair_key": pair_key,
                        "credit_ratio": pair_credit,
                        "share_of_shell": safe_ratio(pair_credit, credit),
                    }
                    for pair_key, pair_credit in sorted(
                        shell_pair_credit[shell].items(),
                        key=lambda item: item[1],
                        reverse=True,
                    )
                ],
            }
        )
    base_credit = shell_credit["(2D,4D]"] + shell_credit["(4D,8D]"]
    high_shell_credit = shell_credit["(8D,16D]"]
    deficit_after_base = max(0.0, need - base_credit)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_three_shell_ladder_router",
        "status": "z61_unique_cover_reduced_to_three_shell_ladder_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": minimal["p_list"],
        "z": minimal["z"],
        "unbalanced_residual_needed_ratio": need,
        "cover_credit_ratio": minimal["minimal_cover_credit_ratio"],
        "shell_count": len([row for row in shell_rows if row["credit_ratio"] > 0]),
        "base_shell_credit_ratio": base_credit,
        "deficit_after_base_shells_ratio": deficit_after_base,
        "high_shell_credit_ratio": high_shell_credit,
        "high_shell_covers_base_deficit": high_shell_credit + 1e-12 >= deficit_after_base,
        "three_shell_ladder_covers_need": shell_rows[-1]["cumulative_credit_ratio"] + 1e-12 >= need,
        "single_target_plus_exit_schema_imported": two_arm[
            "single_target_plus_exit_arm_schema_materialized"
        ],
        "three_shell_ladder_invariant_proved": False,
        "shell_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "shell_rows": shell_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "唯一五格覆盖可重写为三壳层阶梯：`(2D,4D]`、`(4D,8D]`、`(8D,16D]`。"
            "低中两壳给出 base credit，但仍不足；高壳 `--++` 包正好补足缺口。"
            "因此下一步可证明三壳层阶梯支撑不变量，或登记 Shell-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 三壳层阶梯",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"base_shell_credit_ratio={fmt_float(result['base_shell_credit_ratio'])}",
        f"deficit_after_base_shells_ratio={fmt_float(result['deficit_after_base_shells_ratio'])}",
        f"high_shell_credit_ratio={fmt_float(result['high_shell_credit_ratio'])}",
        f"high_shell_covers_base_deficit={fmt_bool(result['high_shell_covers_base_deficit'])}",
        f"three_shell_ladder_covers_need={fmt_bool(result['three_shell_ladder_covers_need'])}",
        f"three_shell_ladder_invariant_proved={fmt_bool(result['three_shell_ladder_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 壳层阶梯",
        "",
        "| shell | credit | share/need | cumulative | deficit after cumulative | cells |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["shell_rows"]:
        lines.append(
            f"| `{row['shell']}` | {fmt_float(row['credit_ratio'])} | "
            f"{fmt_float(row['share_of_need'])} | {fmt_float(row['cumulative_credit_ratio'])} | "
            f"{fmt_float(row['cumulative_deficit_ratio'])} | {row['cell_count']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 壳内 pair",
            "",
            "| shell | pair | credit | share/shell |",
            "| --- | --- | ---: | ---: |",
        ]
    )
    for row in result["shell_rows"]:
        for pair in row["pair_rows"]:
            lines.append(
                f"| `{row['shell']}` | `{pair['pair_key']}` | "
                f"{fmt_float(pair['credit_ratio'])} | {fmt_float(pair['share_of_shell'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：唯一五格覆盖到三壳层阶梯的分解账本。",
            "- 未闭合：证明低中壳 base 与高壳补项的阶梯支撑不变量，或登记 Shell-PDEC。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "deficit_after_base_shells_ratio": result["deficit_after_base_shells_ratio"],
                "high_shell_covers_base_deficit": result["high_shell_covers_base_deficit"],
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
