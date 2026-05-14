#!/usr/bin/env python3
"""审计 z=61 核心出口支撑格的最小覆盖性。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_core_exit_minimal_cover_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
CELL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json"
PARITY_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.md"

NEXT_TARGET = "UniqueFiveCellJointInvariantOrMinimalCoverPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json",
    "prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_core_exit_minimal_cover_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def cell_id(cell: dict[str, Any]) -> str:
    """生成格标识。"""
    return f"omega={cell['omega']}|shell={cell['shell']}|sign={cell['sign_word']}"


def subset_row(cells: list[dict[str, Any]], indices: tuple[int, ...]) -> dict[str, Any]:
    """生成子集记录。"""
    chosen = [cells[index] for index in indices]
    return {
        "indices": list(indices),
        "cell_ids": [cell_id(cell) for cell in chosen],
        "credit_ratio": sum(cell["core_exit_credit_ratio"] for cell in chosen),
        "cells": [
            {
                "omega": cell["omega"],
                "shell": cell["shell"],
                "sign_word": cell["sign_word"],
                "credit_ratio": cell["core_exit_credit_ratio"],
                "pairs": cell["pair_rows"],
            }
            for cell in chosen
        ],
    }


def audit() -> dict[str, Any]:
    """执行最小覆盖审计。"""
    cell_data = json.loads(CELL_JSON.read_text(encoding="utf-8"))
    parity_data = json.loads(PARITY_JSON.read_text(encoding="utf-8"))
    cells = sorted(
        cell_data["cell_rows"],
        key=lambda cell: cell["core_exit_credit_ratio"],
        reverse=True,
    )
    need = cell_data["unbalanced_residual_needed_ratio"]
    cover_rows_by_size = []
    minimal_cover_size = None
    minimal_cover_rows = []
    for size in range(1, len(cells) + 1):
        covers = []
        for indices in itertools.combinations(range(len(cells)), size):
            row = subset_row(cells, indices)
            if row["credit_ratio"] + 1e-12 >= need:
                covers.append(row)
        cover_rows_by_size.append({"size": size, "cover_count": len(covers)})
        if covers and minimal_cover_size is None:
            minimal_cover_size = size
            minimal_cover_rows = covers
            break
    chosen_ids = {cell_id(cell) for cell in cell_data["cover_cells"]}
    minimal_ids = set(minimal_cover_rows[0]["cell_ids"]) if minimal_cover_rows else set()
    omitted_rows = [
        {
            "cell_id": cell_id(cell),
            "credit_ratio": cell["core_exit_credit_ratio"],
            "credit_if_added_to_minimal_cover": minimal_cover_rows[0]["credit_ratio"]
            + cell["core_exit_credit_ratio"]
            if minimal_cover_rows
            else None,
            "cell": {
                "omega": cell["omega"],
                "shell": cell["shell"],
                "sign_word": cell["sign_word"],
                "pairs": cell["pair_rows"],
            },
        }
        for cell in cells
        if cell_id(cell) not in minimal_ids
    ]
    deletion_tests = []
    if minimal_cover_rows:
        minimal_cells = minimal_cover_rows[0]["cells"]
        for index, cell in enumerate(minimal_cells):
            remaining_credit = minimal_cover_rows[0]["credit_ratio"] - cell["credit_ratio"]
            deletion_tests.append(
                {
                    "removed_cell_id": f"omega={cell['omega']}|shell={cell['shell']}|sign={cell['sign_word']}",
                    "removed_credit_ratio": cell["credit_ratio"],
                    "remaining_credit_ratio": remaining_credit,
                    "remaining_deficit_ratio": max(0.0, need - remaining_credit),
                    "still_covers": remaining_credit + 1e-12 >= need,
                }
            )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_core_exit_minimal_cover_router",
        "status": "z61_core_exit_support_has_unique_five_cell_minimal_cover_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": cell_data["p_list"],
        "z": cell_data["z"],
        "unbalanced_residual_needed_ratio": need,
        "candidate_cell_count": len(cells),
        "minimal_cover_size": minimal_cover_size,
        "minimal_cover_count": len(minimal_cover_rows),
        "minimal_cover_unique": len(minimal_cover_rows) == 1,
        "minimal_cover_matches_selected_cover": minimal_ids == chosen_ids,
        "minimal_cover_credit_ratio": minimal_cover_rows[0]["credit_ratio"] if minimal_cover_rows else 0.0,
        "minimal_cover_surplus_ratio": (
            minimal_cover_rows[0]["credit_ratio"] - need if minimal_cover_rows else None
        ),
        "all_minimal_cells_indispensable": all(
            not row["still_covers"] for row in deletion_tests
        ),
        "odd_core_even_booster_identity_imported": parity_data[
            "sample_odd_core_plus_booster_covers_residual"
        ],
        "unique_five_cell_joint_invariant_proved": False,
        "minimal_cover_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cover_rows_by_size": cover_rows_by_size,
        "minimal_cover_rows": minimal_cover_rows,
        "omitted_rows": omitted_rows,
        "deletion_tests": deletion_tests,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "核心出口的 6 个支撑格中，覆盖 `unbalanced<=8` residual 的最小子集大小为 5，"
            "且最小覆盖唯一，正是上一层选中的五格。任意删除其中一格都会失去覆盖。"
            "因此下一步不能再靠选择策略压缩，只能证明这五格联合不变量，或登记 MinimalCover-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 核心出口最小覆盖",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"candidate_cell_count={result['candidate_cell_count']}",
        f"minimal_cover_size={result['minimal_cover_size']}",
        f"minimal_cover_count={result['minimal_cover_count']}",
        f"minimal_cover_unique={fmt_bool(result['minimal_cover_unique'])}",
        f"minimal_cover_matches_selected_cover={fmt_bool(result['minimal_cover_matches_selected_cover'])}",
        f"minimal_cover_credit_ratio={fmt_float(result['minimal_cover_credit_ratio'])}",
        f"minimal_cover_surplus_ratio={fmt_float(result['minimal_cover_surplus_ratio'])}",
        f"all_minimal_cells_indispensable={fmt_bool(result['all_minimal_cells_indispensable'])}",
        f"unique_five_cell_joint_invariant_proved={fmt_bool(result['unique_five_cell_joint_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最小覆盖",
        "",
        "| omega | shell | signs | credit | pairs |",
        "| ---: | --- | --- | ---: | --- |",
    ]
    if result["minimal_cover_rows"]:
        for cell in result["minimal_cover_rows"][0]["cells"]:
            pairs = ", ".join(
                f"{pair['pair_key']}:{fmt_float(pair['pair_credit_ratio'])}"
                for pair in cell["pairs"]
            )
            lines.append(
                f"| {cell['omega']} | `{cell['shell']}` | `{cell['sign_word']}` | "
                f"{fmt_float(cell['credit_ratio'])} | `{pairs}` |"
            )
    lines.extend(
        [
            "",
            "## 2. 删除测试",
            "",
            "| removed cell | removed credit | remaining credit | remaining deficit | still covers |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["deletion_tests"]:
        lines.append(
            f"| `{row['removed_cell_id']}` | {fmt_float(row['removed_credit_ratio'])} | "
            f"{fmt_float(row['remaining_credit_ratio'])} | "
            f"{fmt_float(row['remaining_deficit_ratio'])} | "
            f"{fmt_bool(row['still_covers'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 省略格",
            "",
            "| cell | credit |",
            "| --- | ---: |",
        ]
    )
    for row in result["omitted_rows"]:
        lines.append(f"| `{row['cell_id']}` | {fmt_float(row['credit_ratio'])} |")
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：6 个候选格的最小覆盖枚举。",
            "- 未闭合：证明唯一五格联合支撑下界，或登记 MinimalCover-PDEC。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "minimal_cover_size": result["minimal_cover_size"],
                "minimal_cover_unique": result["minimal_cover_unique"],
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
