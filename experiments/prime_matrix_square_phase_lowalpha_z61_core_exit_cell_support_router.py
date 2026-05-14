#!/usr/bin/env python3
"""把 z=61 unbalanced 互反核心加出口压成格支撑合同。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_core_exit_cell_support_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.md
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
EXTRACTOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json"
CORE_EXIT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.md"

NEXT_TARGET = "FiveCoreExitCellSupportInvariantOrCellExitPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json",
    "prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_core_exit_cell_support_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def cell_key(cell: dict[str, Any]) -> tuple[int, str, str]:
    """生成格键。"""
    return (cell["omega"], cell["shell"], cell["sign_word"])


def greedy_cover(cells: list[dict[str, Any]], target: float) -> list[dict[str, Any]]:
    """按格信用从大到小覆盖目标。"""
    total = 0.0
    result = []
    for cell in sorted(cells, key=lambda item: item["core_exit_credit_ratio"], reverse=True):
        if total >= target:
            break
        total += cell["core_exit_credit_ratio"]
        result.append({**cell, "cumulative_core_exit_credit_ratio": total})
    return result


def audit() -> dict[str, Any]:
    """执行核心出口格支撑审计。"""
    extractor = json.loads(EXTRACTOR_JSON.read_text(encoding="utf-8"))
    core_exit = json.loads(CORE_EXIT_JSON.read_text(encoding="utf-8"))
    selected_pairs = {pair["pair_key"] for pair in core_exit["core_pairs"]}
    selected_pairs.add(core_exit["selected_exit_pair"])
    unbalanced = next(
        row for row in extractor["bucket_rows"] if row["bucket"] == "unbalanced<=8"
    )

    grouped: dict[tuple[int, str, str], dict[str, Any]] = {}
    for cell in unbalanced["all_secondary_cells"]:
        hits = [
            pair for pair in cell["secondary_pairs"] if pair["pair_key"] in selected_pairs
        ]
        if not hits:
            continue
        key = cell_key(cell)
        if key not in grouped:
            grouped[key] = {
                "bucket": "unbalanced<=8",
                "omega": cell["omega"],
                "shell": cell["shell"],
                "sign_word": cell["sign_word"],
                "core_exit_credit_ratio": 0.0,
                "pair_rows": [],
                "profile_vector": cell["profile_vector"],
                "cell_secondary_credit_ratio": cell["secondary_credit_ratio"],
                "cell_profile_crude_bucket_share": cell["profile_crude_bucket_share"],
                "cell_net_bucket_share": cell["cell_net_bucket_share"],
                "cell_opposite_sign_credit_bucket_share": cell[
                    "opposite_sign_credit_bucket_share"
                ],
            }
        for pair in hits:
            grouped[key]["core_exit_credit_ratio"] += pair["pair_credit_ratio"]
            grouped[key]["pair_rows"].append(
                {
                    "pair_key": pair["pair_key"],
                    "pair_credit_ratio": pair["pair_credit_ratio"],
                }
            )

    cell_rows = sorted(
        grouped.values(),
        key=lambda item: item["core_exit_credit_ratio"],
        reverse=True,
    )
    cover_cells = greedy_cover(cell_rows, core_exit["unbalanced_residual_needed_ratio"])
    cover_credit = sum(cell["core_exit_credit_ratio"] for cell in cover_cells)
    omitted_cells = [
        cell
        for cell in cell_rows
        if cell_key(cell) not in {cell_key(item) for item in cover_cells}
    ]
    sign_word_credit: dict[str, float] = defaultdict(float)
    omega_credit: dict[int, float] = defaultdict(float)
    for cell in cover_cells:
        sign_word_credit[cell["sign_word"]] += cell["core_exit_credit_ratio"]
        omega_credit[cell["omega"]] += cell["core_exit_credit_ratio"]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_core_exit_cell_support_router",
        "status": "z61_unbalanced_core_exit_reduced_to_five_support_cells_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": extractor["p_list"],
        "z": extractor["z"],
        "selected_core_exit_pairs": sorted(selected_pairs),
        "unbalanced_residual_needed_ratio": core_exit["unbalanced_residual_needed_ratio"],
        "core_plus_exit_credit_ratio": core_exit["core_plus_exit_credit_ratio"],
        "all_core_exit_cell_count": len(cell_rows),
        "cover_cell_count": len(cover_cells),
        "cover_credit_ratio": cover_credit,
        "cover_surplus_ratio": cover_credit - core_exit["unbalanced_residual_needed_ratio"],
        "sample_five_cells_cover_unbalanced_residual": (
            cover_credit + 1e-12 >= core_exit["unbalanced_residual_needed_ratio"]
        ),
        "omitted_cell_count": len(omitted_cells),
        "cell_support_invariant_proved": False,
        "cell_exit_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cell_rows": cell_rows,
        "cover_cells": cover_cells,
        "omitted_cells": omitted_cells,
        "cover_sign_word_credit": [
            {"sign_word": sign_word, "credit_ratio": credit}
            for sign_word, credit in sorted(
                sign_word_credit.items(), key=lambda item: item[1], reverse=True
            )
        ],
        "cover_omega_credit": [
            {"omega": omega, "credit_ratio": credit}
            for omega, credit in sorted(
                omega_credit.items(), key=lambda item: item[1], reverse=True
            )
        ],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "互反核心加出口的 pair 信用可按格支撑合并。"
            "总共有 6 个支撑格；去掉最小的 `omega=4,(4D,8D],--++` 后，"
            "剩余 5 个格仍覆盖 `unbalanced<=8` 残量。"
            "下一步只需证明这 5 个格支撑的不变量，或登记 CellExit-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 核心出口格支撑",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"core_plus_exit_credit_ratio={fmt_float(result['core_plus_exit_credit_ratio'])}",
        f"all_core_exit_cell_count={result['all_core_exit_cell_count']}",
        f"cover_cell_count={result['cover_cell_count']}",
        f"cover_credit_ratio={fmt_float(result['cover_credit_ratio'])}",
        f"cover_surplus_ratio={fmt_float(result['cover_surplus_ratio'])}",
        f"sample_five_cells_cover_unbalanced_residual={fmt_bool(result['sample_five_cells_cover_unbalanced_residual'])}",
        f"cell_support_invariant_proved={fmt_bool(result['cell_support_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 覆盖格",
        "",
        "| omega | shell | signs | credit | cumulative | pairs | profile vector |",
        "| ---: | --- | --- | ---: | ---: | --- | --- |",
    ]
    for cell in result["cover_cells"]:
        pairs = ", ".join(
            f"{pair['pair_key']}:{fmt_float(pair['pair_credit_ratio'])}"
            for pair in cell["pair_rows"]
        )
        vector = ", ".join(
            f"{entry['p']}:{fmt_float(entry['linear_remainder'])}"
            for entry in cell["profile_vector"]
        )
        lines.append(
            f"| {cell['omega']} | `{cell['shell']}` | `{cell['sign_word']}` | "
            f"{fmt_float(cell['core_exit_credit_ratio'])} | "
            f"{fmt_float(cell['cumulative_core_exit_credit_ratio'])} | "
            f"`{pairs}` | `{vector}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 省略格",
            "",
            "| omega | shell | signs | credit | pairs |",
            "| ---: | --- | --- | ---: | --- |",
        ]
    )
    for cell in result["omitted_cells"]:
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
            "## 3. cover 分组",
            "",
            "| group | value | credit |",
            "| --- | --- | ---: |",
        ]
    )
    for row in result["cover_sign_word_credit"]:
        lines.append(f"| sign word | `{row['sign_word']}` | {fmt_float(row['credit_ratio'])} |")
    for row in result["cover_omega_credit"]:
        lines.append(f"| omega | `{row['omega']}` | {fmt_float(row['credit_ratio'])} |")
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：核心出口 pair 信用到 5 个覆盖格的压缩账本。",
            "- 未闭合：证明这 5 个格的支撑不变量，或登记 CellExit-PDEC。",
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
                "cover_cell_count": result["cover_cell_count"],
                "cover_credit_ratio": result["cover_credit_ratio"],
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
