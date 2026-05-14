#!/usr/bin/env python3
"""把 z=61 次级残量 pair 原子融合为残量深度格原子。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_secondary_residual_cell_fusion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.md
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
ATOM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.json"
SIGN_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.md"

NEXT_TARGET = "SevenResidualCellPhaseTemplateInvariantOrCellPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_secondary_residual_cell_fusion_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def cell_key(atom: dict[str, Any]) -> tuple[str, int, str]:
    """生成深度格键。"""
    return (atom["bucket"], atom["omega"], atom["shell"])


def profile_lookup(sign_data: dict[str, Any]) -> dict[tuple[str, int, str], dict[str, Any]]:
    """建立深度格到 profile 向量的索引。"""
    return {
        (row["bucket"], row["omega"], row["shell"]): row
        for row in sign_data["cell_rows"]
    }


def audit() -> dict[str, Any]:
    """执行残量格融合审计。"""
    atom_data = json.loads(ATOM_JSON.read_text(encoding="utf-8"))
    sign_data = json.loads(SIGN_JSON.read_text(encoding="utf-8"))
    profiles = profile_lookup(sign_data)
    residual_need_by_bucket = {
        row["bucket"]: row["residual_needed_ratio"]
        for row in atom_data["residual_rows"]
    }
    grouped: dict[tuple[str, int, str], dict[str, Any]] = {}
    for atom in atom_data["atom_rows"]:
        key = cell_key(atom)
        if key not in grouped:
            source_row = profiles[key]
            grouped[key] = {
                "bucket": atom["bucket"],
                "omega": atom["omega"],
                "shell": atom["shell"],
                "sign_word": atom["sign_word"],
                "selected_pair_credit_bucket_share": 0.0,
                "pairs": [],
                "profile_vector": [
                    {
                        "p": entry["p"],
                        "linear_remainder": entry["linear_remainder"],
                        "signed_bucket_share": entry["signed_bucket_share"],
                        "abs_bucket_share": entry["abs_bucket_share"],
                    }
                    for entry in source_row["profile_entries"]
                ],
                "cell_total_opposite_sign_credit_bucket_share": source_row[
                    "opposite_sign_credit_bucket_share"
                ],
                "cell_profile_crude_bucket_share": source_row["profile_crude_bucket_share"],
                "cell_net_bucket_share": source_row["cell_net_bucket_share"],
            }
        grouped[key]["selected_pair_credit_bucket_share"] += atom["bucket_abs_share"]
        grouped[key]["pairs"].append(
            {
                "pair_key": atom["pair_key"],
                "positive_p": atom["positive_p"],
                "negative_p": atom["negative_p"],
                "bucket_abs_share": atom["bucket_abs_share"],
                "cell_credit_share_from_pair": atom["cell_credit_share_from_pair"],
            }
        )

    cell_rows = sorted(
        grouped.values(),
        key=lambda row: (row["bucket"], -row["selected_pair_credit_bucket_share"]),
    )
    residual_rows = []
    for bucket, need in residual_need_by_bucket.items():
        cells = [row for row in cell_rows if row["bucket"] == bucket]
        selected_credit = sum(row["selected_pair_credit_bucket_share"] for row in cells)
        sign_word_credit: dict[str, float] = defaultdict(float)
        for row in cells:
            sign_word_credit[row["sign_word"]] += row["selected_pair_credit_bucket_share"]
        residual_rows.append(
            {
                "bucket": bucket,
                "residual_needed_ratio": need,
                "fused_cell_count": len(cells),
                "fused_cell_credit_ratio": selected_credit,
                "fused_cell_surplus_ratio": selected_credit - need,
                "fused_cells_cover_residual": selected_credit + 1e-12 >= need,
                "sign_word_credit": [
                    {
                        "sign_word": sign_word,
                        "credit_ratio": credit,
                        "credit_share_of_residual": safe_ratio(credit, need),
                    }
                    for sign_word, credit in sorted(
                        sign_word_credit.items(), key=lambda item: item[1], reverse=True
                    )
                ],
                "cells": cells,
            }
        )

    sign_word_global: dict[str, float] = defaultdict(float)
    for row in cell_rows:
        sign_word_global[row["sign_word"]] += row["selected_pair_credit_bucket_share"]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_secondary_residual_cell_fusion_router",
        "status": "z61_secondary_residual_nine_pair_atoms_fused_to_seven_cell_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": atom_data["p_list"],
        "z": atom_data["z"],
        "selected_pair_atom_count": atom_data["selected_atom_count"],
        "fused_cell_atom_count": len(cell_rows),
        "sample_fused_cells_cover_all_residuals": all(
            row["fused_cells_cover_residual"] for row in residual_rows
        ),
        "residual_cell_phase_template_proved": False,
        "cell_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "residual_rows": residual_rows,
        "cell_rows": cell_rows,
        "global_sign_word_credit": [
            {
                "sign_word": sign_word,
                "credit_ratio": credit,
            }
            for sign_word, credit in sorted(
                sign_word_global.items(), key=lambda item: item[1], reverse=True
            )
        ],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "9 个残量 pair 原子中有两组共享同一深度格，因此可融合为 7 个残量格原子。"
            "这些格原子保留完整 profile 向量与 sign word；下一步可直接证明 7 个格模板的相位不变量，"
            "或登记 Cell-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 次级残量格融合",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selected_pair_atom_count={result['selected_pair_atom_count']}",
        f"fused_cell_atom_count={result['fused_cell_atom_count']}",
        f"sample_fused_cells_cover_all_residuals={fmt_bool(result['sample_fused_cells_cover_all_residuals'])}",
        f"residual_cell_phase_template_proved={fmt_bool(result['residual_cell_phase_template_proved'])}",
        f"cell_pdec_excluded={fmt_bool(result['cell_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 残量格融合",
        "",
        "| bucket | residual need | fused cells | fused credit | surplus |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in result["residual_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['residual_needed_ratio'])} | "
            f"{row['fused_cell_count']} | {fmt_float(row['fused_cell_credit_ratio'])} | "
            f"{fmt_float(row['fused_cell_surplus_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 7 个残量格原子",
            "",
            "| bucket | omega | shell | signs | selected credit | pairs | profile vector |",
            "| --- | ---: | --- | --- | ---: | --- | --- |",
        ]
    )
    for row in result["cell_rows"]:
        pair_text = ", ".join(
            f"{pair['pair_key']}:{fmt_float(pair['bucket_abs_share'])}" for pair in row["pairs"]
        )
        vector_text = ", ".join(
            f"{entry['p']}:{fmt_float(entry['linear_remainder'])}"
            for entry in row["profile_vector"]
        )
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | `{row['sign_word']}` | "
            f"{fmt_float(row['selected_pair_credit_bucket_share'])} | "
            f"`{pair_text}` | `{vector_text}` |"
        )
    lines.extend(
        [
            "",
            "## 3. sign word 贡献",
            "",
            "| sign word | credit ratio |",
            "| --- | ---: |",
        ]
    )
    for row in result["global_sign_word_credit"]:
        lines.append(f"| `{row['sign_word']}` | {fmt_float(row['credit_ratio'])} |")
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：9 个 pair 原子融合成 7 个格原子的账本。",
            "- 未闭合：需要证明 7 个格模板的相位不变量，或登记 Cell-PDEC。",
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
                "selected_pair_atom_count": result["selected_pair_atom_count"],
                "fused_cell_atom_count": result["fused_cell_atom_count"],
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
