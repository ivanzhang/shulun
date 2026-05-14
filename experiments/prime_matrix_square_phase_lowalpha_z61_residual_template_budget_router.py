#!/usr/bin/env python3
"""把 z=61 七个残量格原子压成 sign-word 模板预算。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_residual_template_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-residual-template-budget-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-residual-template-budget-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-residual-template-budget-router.md
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
FUSION_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-residual-template-budget-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-residual-template-budget-router.md"

NEXT_TARGET = "UnbalancedFourTemplatePhaseInvariantOrTemplatePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_residual_template_budget_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def greedy_template_cover(rows: list[dict[str, Any]], target: float) -> list[dict[str, Any]]:
    """按模板贡献贪心覆盖残量。"""
    result = []
    total = 0.0
    for row in sorted(rows, key=lambda item: item["credit_ratio"], reverse=True):
        if total >= target:
            break
        total += row["credit_ratio"]
        result.append({**row, "cumulative_credit_ratio": total})
    return result


def audit() -> dict[str, Any]:
    """执行模板预算审计。"""
    fusion_data = json.loads(FUSION_JSON.read_text(encoding="utf-8"))
    bucket_rows = []
    template_rows = []
    for residual in fusion_data["residual_rows"]:
        bucket = residual["bucket"]
        grouped: dict[str, dict[str, Any]] = {}
        for cell in residual["cells"]:
            sign_word = cell["sign_word"]
            if sign_word not in grouped:
                grouped[sign_word] = {
                    "bucket": bucket,
                    "sign_word": sign_word,
                    "credit_ratio": 0.0,
                    "cell_count": 0,
                    "cells": [],
                }
            grouped[sign_word]["credit_ratio"] += cell["selected_pair_credit_bucket_share"]
            grouped[sign_word]["cell_count"] += 1
            grouped[sign_word]["cells"].append(
                {
                    "omega": cell["omega"],
                    "shell": cell["shell"],
                    "selected_pair_credit_bucket_share": cell[
                        "selected_pair_credit_bucket_share"
                    ],
                    "pairs": [pair["pair_key"] for pair in cell["pairs"]],
                }
            )
        rows = sorted(grouped.values(), key=lambda item: item["credit_ratio"], reverse=True)
        cover = greedy_template_cover(rows, residual["residual_needed_ratio"])
        cover_credit = sum(row["credit_ratio"] for row in cover)
        bucket_rows.append(
            {
                "bucket": bucket,
                "residual_needed_ratio": residual["residual_needed_ratio"],
                "template_count": len(rows),
                "cover_template_count": len(cover),
                "cover_credit_ratio": cover_credit,
                "cover_surplus_ratio": cover_credit - residual["residual_needed_ratio"],
                "templates_cover_residual": cover_credit + 1e-12 >= residual["residual_needed_ratio"],
                "template_rows": rows,
                "cover_templates": cover,
            }
        )
        template_rows.extend(rows)

    global_template_credit: dict[str, float] = defaultdict(float)
    for row in template_rows:
        global_template_credit[row["sign_word"]] += row["credit_ratio"]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_residual_template_budget_router",
        "status": "z61_residual_cells_reduced_to_sign_word_template_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": fusion_data["p_list"],
        "z": fusion_data["z"],
        "fused_cell_atom_count": fusion_data["fused_cell_atom_count"],
        "bucket_template_budget_materialized": True,
        "sample_templates_cover_all_residuals": all(
            row["templates_cover_residual"] for row in bucket_rows
        ),
        "bucket_template_obligation_count": sum(row["cover_template_count"] for row in bucket_rows),
        "unbalanced_template_count": next(
            row["cover_template_count"] for row in bucket_rows if row["bucket"] == "unbalanced<=8"
        ),
        "template_phase_invariant_proved": False,
        "template_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "bucket_rows": bucket_rows,
        "global_template_credit": [
            {"sign_word": sign_word, "credit_ratio": credit}
            for sign_word, credit in sorted(
                global_template_credit.items(), key=lambda item: item[1], reverse=True
            )
        ],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "7 个残量格原子已按 sign word 模板合并。"
            "`mid<=4` 只剩单一 `--++` 模板；`unbalanced<=8` 仍需四个模板合力。"
            "因此最终残量证明可集中到 unbalanced 的四模板相位不变量，"
            "或登记 Template-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 残量模板预算",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fused_cell_atom_count={result['fused_cell_atom_count']}",
        f"bucket_template_budget_materialized={fmt_bool(result['bucket_template_budget_materialized'])}",
        f"sample_templates_cover_all_residuals={fmt_bool(result['sample_templates_cover_all_residuals'])}",
        f"bucket_template_obligation_count={result['bucket_template_obligation_count']}",
        f"unbalanced_template_count={result['unbalanced_template_count']}",
        f"template_phase_invariant_proved={fmt_bool(result['template_phase_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. bucket 模板覆盖",
        "",
        "| bucket | residual need | templates | cover templates | cover credit | surplus |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['residual_needed_ratio'])} | "
            f"{row['template_count']} | {row['cover_template_count']} | "
            f"{fmt_float(row['cover_credit_ratio'])} | "
            f"{fmt_float(row['cover_surplus_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 模板明细",
            "",
            "| bucket | sign word | credit | cells | cell list |",
            "| --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in result["bucket_rows"]:
        for template in row["template_rows"]:
            cells = ", ".join(
                f"omega={cell['omega']},{cell['shell']}:{fmt_float(cell['selected_pair_credit_bucket_share'])}"
                for cell in template["cells"]
            )
            lines.append(
                f"| `{row['bucket']}` | `{template['sign_word']}` | "
                f"{fmt_float(template['credit_ratio'])} | "
                f"{template['cell_count']} | `{cells}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 全局模板贡献",
            "",
            "| sign word | credit |",
            "| --- | ---: |",
        ]
    )
    for row in result["global_template_credit"]:
        lines.append(f"| `{row['sign_word']}` | {fmt_float(row['credit_ratio'])} |")
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：7 个格原子到 sign-word 模板预算的合并账本。",
            "- 剩余：证明 `unbalanced<=8` 四模板相位不变量，或登记 Template-PDEC。",
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
                "bucket_template_obligation_count": result["bucket_template_obligation_count"],
                "unbalanced_template_count": result["unbalanced_template_count"],
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
