#!/usr/bin/env python3
"""把 coprime boundary 双线性块转成加权 signed budget 合同。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_bilinear_block_budget_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
BILINEAR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json"
SPLIT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.md"

NEXT_TARGET = "WeightedBilinearBlockSignedBudgetOrLocalizedBlockPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json",
    "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_bilinear_block_budget_contract_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行加权 budget 合同审计。"""
    bilinear = json.loads(BILINEAR_JSON.read_text(encoding="utf-8"))
    split = json.loads(SPLIT_JSON.read_text(encoding="utf-8"))
    target_by_z = {
        int(row["z"]): row["required_equal_split_angle"]
        for row in split["rows"]
        if row["required_equal_split_angle"] is not None
    }
    rows = []
    block_rows = []
    for row in bilinear["rows"]:
        z = int(row["z"])
        total_abs = float(row["total"]["abs_contribution"])
        if total_abs <= 0:
            rows.append(
                {
                    "z": z,
                    "target_angle": target_by_z.get(z),
                    "block_weighted_signed_budget": None,
                    "sample_contract_pass": True,
                    "target_slack": None,
                    "total_abs": total_abs,
                }
            )
            continue
        weighted_budget = 0.0
        for block in row["balance_buckets"]:
            share = block["abs_share_of_total"] or 0.0
            signed_over_abs = block["signed_over_abs"] or 0.0
            weighted = share * signed_over_abs
            weighted_budget += weighted
            block_rows.append(
                {
                    "z": z,
                    "bucket": block["bucket"],
                    "abs_share": share,
                    "signed_over_abs": signed_over_abs,
                    "weighted_budget": weighted,
                    "signed_contribution": block["signed_contribution"],
                    "abs_contribution": block["abs_contribution"],
                }
            )
        target = target_by_z.get(z)
        rows.append(
            {
                "z": z,
                "target_angle": target,
                "block_weighted_signed_budget": weighted_budget,
                "total_signed_over_abs_no_cancellation": weighted_budget,
                "sample_contract_pass": target is None or weighted_budget <= target,
                "target_slack": None if target is None else target - weighted_budget,
                "total_abs": total_abs,
            }
        )
    failures = [row for row in rows if not row["sample_contract_pass"]]
    worst_block = max(block_rows, key=lambda item: item["weighted_budget"], default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_bilinear_block_budget_contract_router",
        "status": "bilinear_block_weighted_budget_contract_closed_bounds_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "weighted_block_budget_contract_closed": True,
        "sample_satisfies_weighted_block_budget": len(failures) == 0,
        "balanced_block_dispersion_bound_proved": False,
        "unbalanced_endpoint_pdec_excluded": False,
        "localized_block_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "block_rows": block_rows,
        "worst_weighted_block": worst_block,
        "sample_failure_count": len(failures),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "coprime boundary 双线性块的验收不应要求每个块单独小于总角度阈值；"
            "正确充分条件是加权预算 `sum_b mass_share_b * signed_ratio_b <= theta_z`。"
            "这一步闭合了块级预算如何推出 coprime edge 角度界的合同。"
            "若合同失败，失败必定位到具体 `(z,bucket)`，成为 LocalizedBlock-PDEC；"
            "若合同通过，下一步只需证明各块的 signed ratio 预算。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 双线性块 signed budget 合同",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"weighted_block_budget_contract_closed={fmt_bool(result['weighted_block_budget_contract_closed'])}",
        f"sample_satisfies_weighted_block_budget={fmt_bool(result['sample_satisfies_weighted_block_budget'])}",
        f"balanced_block_dispersion_bound_proved={fmt_bool(result['balanced_block_dispersion_bound_proved'])}",
        f"unbalanced_endpoint_pdec_excluded={fmt_bool(result['unbalanced_endpoint_pdec_excluded'])}",
        f"localized_block_pdec_excluded={fmt_bool(result['localized_block_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. z 层预算",
        "",
        "| z | target angle | weighted block budget | slack | pass |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {fmt_float(row['target_angle'])} | "
            f"{fmt_float(row['block_weighted_signed_budget'])} | "
            f"{fmt_float(row['target_slack'])} | `{fmt_bool(row['sample_contract_pass'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 块级贡献",
            "",
            "| z | bucket | abs share | signed/abs | weighted budget |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for block in result["block_rows"]:
        lines.append(
            f"| {block['z']} | `{block['bucket']}` | {fmt_float(block['abs_share'])} | "
            f"{fmt_float(block['signed_over_abs'])} | {fmt_float(block['weighted_budget'])} |"
        )
    worst = result["worst_weighted_block"]
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：块级 signed ratio 的加权预算推出 coprime edge 角度界。",
            "- 未闭合：balanced/mid 块 signed ratio 预算。",
            "- 未闭合：unbalanced/far endpoint PDEC 排斥或 signed ratio 预算。",
        ]
    )
    if worst is not None:
        lines.append(
            f"- 当前最大加权块为 `z={worst['z']}, {worst['bucket']}`，贡献 "
            f"`{fmt_float(worst['weighted_budget'])}`。"
        )
    lines.extend(
        [
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
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "sample_failure_count": result["sample_failure_count"],
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
