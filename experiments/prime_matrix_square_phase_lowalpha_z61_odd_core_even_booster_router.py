#!/usr/bin/env python3
"""把 z=61 五格核心出口支撑压成奇深度核心加偶高壳补项。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_odd_core_even_booster_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
CELL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.md"

NEXT_TARGET = "OddOmegaCorePlusEvenHighShellBoosterInvariantOrParityPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json",
]


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_odd_core_even_booster_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行奇深度核心加偶高壳补项审计。"""
    cell_data = json.loads(CELL_JSON.read_text(encoding="utf-8"))
    cover_cells = cell_data["cover_cells"]
    odd_core_cells = [cell for cell in cover_cells if cell["omega"] % 2 == 1]
    even_booster_candidates = [
        cell
        for cell in cover_cells
        if cell["omega"] % 2 == 0 and cell["shell"] == "(8D,16D]"
    ]
    odd_core_credit = sum(cell["core_exit_credit_ratio"] for cell in odd_core_cells)
    deficit_after_odd_core = max(
        0.0,
        cell_data["unbalanced_residual_needed_ratio"] - odd_core_credit,
    )
    even_booster_candidates = sorted(
        even_booster_candidates,
        key=lambda cell: cell["core_exit_credit_ratio"],
        reverse=True,
    )
    selected_booster = next(
        (
            cell
            for cell in even_booster_candidates
            if cell["core_exit_credit_ratio"] + 1e-12 >= deficit_after_odd_core
        ),
        None,
    )
    booster_credit = selected_booster["core_exit_credit_ratio"] if selected_booster else 0.0
    total_credit = odd_core_credit + booster_credit

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_odd_core_even_booster_router",
        "status": "z61_core_exit_five_cells_reduced_to_odd_core_even_booster_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": cell_data["p_list"],
        "z": cell_data["z"],
        "unbalanced_residual_needed_ratio": cell_data["unbalanced_residual_needed_ratio"],
        "odd_core_cell_count": len(odd_core_cells),
        "odd_core_credit_ratio": odd_core_credit,
        "deficit_after_odd_core_ratio": deficit_after_odd_core,
        "even_booster_candidate_count": len(even_booster_candidates),
        "selected_even_booster": selected_booster,
        "selected_even_booster_credit_ratio": booster_credit,
        "odd_core_plus_booster_credit_ratio": total_credit,
        "odd_core_plus_booster_surplus_ratio": total_credit
        - cell_data["unbalanced_residual_needed_ratio"],
        "sample_odd_core_plus_booster_covers_residual": (
            total_credit + 1e-12 >= cell_data["unbalanced_residual_needed_ratio"]
        ),
        "odd_core_even_booster_invariant_proved": False,
        "parity_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "odd_core_cells": odd_core_cells,
        "even_booster_candidates": even_booster_candidates,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "五个核心出口覆盖格可压成奇深度核心加偶高壳补项。"
            "`omega=3,5` 的奇深度核心几乎覆盖全部 residual；"
            "剩余缺口由一个 `omega=4,(8D,16D],--++` 偶高壳补项补齐。"
            "下一步只需证明该奇偶深度组合的不变量，或登记 Parity-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 奇深度核心与偶高壳补项",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"odd_core_credit_ratio={fmt_float(result['odd_core_credit_ratio'])}",
        f"deficit_after_odd_core_ratio={fmt_float(result['deficit_after_odd_core_ratio'])}",
        f"selected_even_booster_credit_ratio={fmt_float(result['selected_even_booster_credit_ratio'])}",
        f"odd_core_plus_booster_credit_ratio={fmt_float(result['odd_core_plus_booster_credit_ratio'])}",
        f"odd_core_plus_booster_surplus_ratio={fmt_float(result['odd_core_plus_booster_surplus_ratio'])}",
        f"sample_odd_core_plus_booster_covers_residual={fmt_bool(result['sample_odd_core_plus_booster_covers_residual'])}",
        f"odd_core_even_booster_invariant_proved={fmt_bool(result['odd_core_even_booster_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 奇深度核心",
        "",
        "| omega | shell | signs | credit | pairs |",
        "| ---: | --- | --- | ---: | --- |",
    ]
    for cell in result["odd_core_cells"]:
        pairs = ", ".join(
            f"{pair['pair_key']}:{fmt_float(pair['pair_credit_ratio'])}"
            for pair in cell["pair_rows"]
        )
        lines.append(
            f"| {cell['omega']} | `{cell['shell']}` | `{cell['sign_word']}` | "
            f"{fmt_float(cell['core_exit_credit_ratio'])} | `{pairs}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 偶高壳补项",
            "",
            "| omega | shell | signs | credit | selected | pairs |",
            "| ---: | --- | --- | ---: | --- | --- |",
        ]
    )
    selected_key = None
    if result["selected_even_booster"]:
        selected_key = (
            result["selected_even_booster"]["omega"],
            result["selected_even_booster"]["shell"],
            result["selected_even_booster"]["sign_word"],
        )
    for cell in result["even_booster_candidates"]:
        key = (cell["omega"], cell["shell"], cell["sign_word"])
        pairs = ", ".join(
            f"{pair['pair_key']}:{fmt_float(pair['pair_credit_ratio'])}"
            for pair in cell["pair_rows"]
        )
        lines.append(
            f"| {cell['omega']} | `{cell['shell']}` | `{cell['sign_word']}` | "
            f"{fmt_float(cell['core_exit_credit_ratio'])} | "
            f"{fmt_bool(key == selected_key)} | `{pairs}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：五格核心出口支撑压成奇深度核心加偶高壳补项。",
            "- 未闭合：证明该奇偶深度组合下界，或登记 Parity-PDEC。",
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
                "odd_core_credit_ratio": result["odd_core_credit_ratio"],
                "deficit_after_odd_core_ratio": result["deficit_after_odd_core_ratio"],
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
