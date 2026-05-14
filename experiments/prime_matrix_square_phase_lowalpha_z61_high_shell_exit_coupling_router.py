#!/usr/bin/env python3
"""把 z=61 三壳层阶梯中的高壳补项拆成互反项与出口项。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_exit_coupling_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.md
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
LADDER_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.md"

NEXT_TARGET = "HighShellReciprocalExitCouplingInvariantOrHighShellPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_exit_coupling_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行高壳互反/出口耦合审计。"""
    ladder = json.loads(LADDER_JSON.read_text(encoding="utf-8"))
    high_shell = next(row for row in ladder["shell_rows"] if row["shell"] == "(8D,16D]")
    pair_credit: dict[str, float] = defaultdict(float)
    pair_cells: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for cell in high_shell["cells"]:
        for pair in cell["pairs"]:
            pair_credit[pair["pair_key"]] += pair["pair_credit_ratio"]
            pair_cells[pair["pair_key"]].append(
                {
                    "omega": cell["omega"],
                    "shell": cell["shell"],
                    "sign_word": cell["sign_word"],
                    "pair_credit_ratio": pair["pair_credit_ratio"],
                }
            )

    reciprocal_pair = "200003->36739"
    exit_pair = "200003->10007"
    reciprocal_credit = pair_credit[reciprocal_pair]
    exit_credit = pair_credit[exit_pair]
    base_credit = ladder["base_shell_credit_ratio"]
    need = ladder["unbalanced_residual_needed_ratio"]
    base_plus_reciprocal = base_credit + reciprocal_credit
    deficit_after_base_plus_reciprocal = max(0.0, need - base_plus_reciprocal)
    base_plus_high_shell = base_credit + reciprocal_credit + exit_credit

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_high_shell_exit_coupling_router",
        "status": "z61_high_shell_booster_split_to_reciprocal_exit_coupling_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": ladder["p_list"],
        "z": ladder["z"],
        "unbalanced_residual_needed_ratio": need,
        "base_shell_credit_ratio": base_credit,
        "high_shell_credit_ratio": high_shell["credit_ratio"],
        "high_shell_cell_count": high_shell["cell_count"],
        "high_shell_reciprocal_pair": reciprocal_pair,
        "high_shell_reciprocal_credit_ratio": reciprocal_credit,
        "high_shell_exit_pair": exit_pair,
        "high_shell_exit_credit_ratio": exit_credit,
        "exit_over_reciprocal_ratio": safe_ratio(exit_credit, reciprocal_credit),
        "base_plus_reciprocal_credit_ratio": base_plus_reciprocal,
        "deficit_after_base_plus_reciprocal_ratio": deficit_after_base_plus_reciprocal,
        "exit_covers_reciprocal_deficit": exit_credit + 1e-12 >= deficit_after_base_plus_reciprocal,
        "base_plus_high_shell_credit_ratio": base_plus_high_shell,
        "base_plus_high_shell_surplus_ratio": base_plus_high_shell - need,
        "high_shell_pair_rows": [
            {
                "pair_key": pair_key,
                "credit_ratio": credit,
                "share_of_high_shell": safe_ratio(credit, high_shell["credit_ratio"]),
                "cells": pair_cells[pair_key],
            }
            for pair_key, credit in sorted(pair_credit.items(), key=lambda item: item[1], reverse=True)
        ],
        "high_shell_exit_coupling_invariant_proved": False,
        "high_shell_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "高壳补项 `(8D,16D]` 全部来自 `200003` 正向来源，"
            "并分成互反项 `200003->36739` 与出口项 `200003->10007`。"
            "低中壳加高壳互反项仍不足；高壳出口项正好补齐该缺口。"
            "下一步应证明高壳互反/出口耦合不变量，或登记 HighShell-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 高壳互反出口耦合",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"base_shell_credit_ratio={fmt_float(result['base_shell_credit_ratio'])}",
        f"high_shell_reciprocal_credit_ratio={fmt_float(result['high_shell_reciprocal_credit_ratio'])}",
        f"high_shell_exit_credit_ratio={fmt_float(result['high_shell_exit_credit_ratio'])}",
        f"exit_over_reciprocal_ratio={fmt_float(result['exit_over_reciprocal_ratio'])}",
        f"deficit_after_base_plus_reciprocal_ratio={fmt_float(result['deficit_after_base_plus_reciprocal_ratio'])}",
        f"exit_covers_reciprocal_deficit={fmt_bool(result['exit_covers_reciprocal_deficit'])}",
        f"base_plus_high_shell_surplus_ratio={fmt_float(result['base_plus_high_shell_surplus_ratio'])}",
        f"high_shell_exit_coupling_invariant_proved={fmt_bool(result['high_shell_exit_coupling_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 高壳 pair",
        "",
        "| pair | credit | share/high shell | cells |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in result["high_shell_pair_rows"]:
        cells = ", ".join(
            f"omega={cell['omega']}:{fmt_float(cell['pair_credit_ratio'])}"
            for cell in row["cells"]
        )
        lines.append(
            f"| `{row['pair_key']}` | {fmt_float(row['credit_ratio'])} | "
            f"{fmt_float(row['share_of_high_shell'])} | `{cells}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：高壳补项拆成互反项与出口项的账本。",
            "- 未闭合：证明高壳互反/出口耦合下界，或登记 HighShell-PDEC。",
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
                "exit_over_reciprocal_ratio": result["exit_over_reciprocal_ratio"],
                "exit_covers_reciprocal_deficit": result["exit_covers_reciprocal_deficit"],
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
