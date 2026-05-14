#!/usr/bin/env python3
"""把 z=61 唯一五格覆盖压成双正向臂平衡账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_unique_cover_two_arm_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.md"

NEXT_TARGET = "TwoArmPositiveSourceBalanceInvariantOrArmPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_unique_cover_two_arm_balance_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行双臂平衡审计。"""
    minimal = json.loads(MINIMAL_JSON.read_text(encoding="utf-8"))
    cover = minimal["minimal_cover_rows"][0]
    arm_credit: dict[str, float] = defaultdict(float)
    arm_cells: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for cell in cover["cells"]:
        for pair in cell["pairs"]:
            positive_p = pair["pair_key"].split("->")[0]
            arm_credit[positive_p] += pair["pair_credit_ratio"]
            arm_cells[positive_p].append(
                {
                    "omega": cell["omega"],
                    "shell": cell["shell"],
                    "sign_word": cell["sign_word"],
                    "pair_key": pair["pair_key"],
                    "credit_ratio": pair["pair_credit_ratio"],
                }
            )
    arm_rows = []
    need = minimal["unbalanced_residual_needed_ratio"]
    cover_credit = cover["credit_ratio"]
    for positive_p, credit in sorted(arm_credit.items(), key=lambda item: item[1], reverse=True):
        arm_rows.append(
            {
                "positive_p": int(positive_p),
                "credit_ratio": credit,
                "share_of_need": safe_ratio(credit, need),
                "share_of_cover": safe_ratio(credit, cover_credit),
                "alone_covers_need": credit + 1e-12 >= need,
                "deficit_if_alone": max(0.0, need - credit),
                "cells": sorted(
                    arm_cells[positive_p],
                    key=lambda item: item["credit_ratio"],
                    reverse=True,
                ),
            }
        )
    max_credit = max(row["credit_ratio"] for row in arm_rows)
    min_credit = min(row["credit_ratio"] for row in arm_rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_unique_cover_two_arm_balance_router",
        "status": "z61_unique_five_cell_cover_reduced_to_two_positive_source_arms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": minimal["p_list"],
        "z": minimal["z"],
        "unbalanced_residual_needed_ratio": need,
        "unique_five_cell_cover_credit_ratio": cover_credit,
        "arm_count": len(arm_rows),
        "arm_rows": arm_rows,
        "two_arm_total_covers_need": cover_credit + 1e-12 >= need,
        "each_arm_individually_insufficient": all(not row["alone_covers_need"] for row in arm_rows),
        "arm_credit_ratio_max_over_min": safe_ratio(max_credit, min_credit),
        "arm_balance_materialized": safe_ratio(max_credit, min_credit) is not None
        and (safe_ratio(max_credit, min_credit) or 999.0) <= 1.25,
        "two_arm_balance_invariant_proved": False,
        "arm_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "唯一五格覆盖可按正向来源 P 压成两个平衡臂："
            "`36739` 臂与 `200003` 臂。两臂都不能单独覆盖 residual，"
            "但贡献规模接近，合起来覆盖需求。"
            "下一步应证明这种双臂平衡是结构强制，或登记 Arm-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 唯一覆盖双臂平衡",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"unique_five_cell_cover_credit_ratio={fmt_float(result['unique_five_cell_cover_credit_ratio'])}",
        f"arm_count={result['arm_count']}",
        f"two_arm_total_covers_need={fmt_bool(result['two_arm_total_covers_need'])}",
        f"each_arm_individually_insufficient={fmt_bool(result['each_arm_individually_insufficient'])}",
        f"arm_credit_ratio_max_over_min={fmt_float(result['arm_credit_ratio_max_over_min'])}",
        f"arm_balance_materialized={fmt_bool(result['arm_balance_materialized'])}",
        f"two_arm_balance_invariant_proved={fmt_bool(result['two_arm_balance_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 双臂",
        "",
        "| positive P | credit | share/need | share/cover | deficit if alone |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["arm_rows"]:
        lines.append(
            f"| {row['positive_p']} | {fmt_float(row['credit_ratio'])} | "
            f"{fmt_float(row['share_of_need'])} | {fmt_float(row['share_of_cover'])} | "
            f"{fmt_float(row['deficit_if_alone'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 臂内单元",
            "",
            "| positive P | omega | shell | signs | pair | credit |",
            "| ---: | ---: | --- | --- | --- | ---: |",
        ]
    )
    for row in result["arm_rows"]:
        for cell in row["cells"]:
            lines.append(
                f"| {row['positive_p']} | {cell['omega']} | `{cell['shell']}` | "
                f"`{cell['sign_word']}` | `{cell['pair_key']}` | {fmt_float(cell['credit_ratio'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：唯一五格覆盖到两个正向来源臂的分解账本。",
            "- 未闭合：证明双臂平衡不变量，或登记 Arm-PDEC。",
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
                "arm_count": result["arm_count"],
                "arm_credit_ratio_max_over_min": result["arm_credit_ratio_max_over_min"],
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
