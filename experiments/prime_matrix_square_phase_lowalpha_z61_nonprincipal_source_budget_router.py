#!/usr/bin/env python3
"""把 z=61 非主正相位残量压成来源 P 预算。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_nonprincipal_source_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.md"

NEXT_TARGET = "UnbalancedTwoSourceNonprincipalCreditInvariantOrSourcePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_nonprincipal_source_budget_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def greedy_source_cover(rows: list[dict[str, Any]], target: float) -> list[dict[str, Any]]:
    """按来源贡献覆盖目标。"""
    total = 0.0
    result = []
    for row in sorted(rows, key=lambda item: item["credit_ratio"], reverse=True):
        if total >= target:
            break
        total += row["credit_ratio"]
        result.append({**row, "cumulative_credit_ratio": total})
    return result


def audit() -> dict[str, Any]:
    """执行来源 P 预算审计。"""
    extractor = json.loads(EXTRACTOR_JSON.read_text(encoding="utf-8"))
    bucket_rows = []
    for bucket in extractor["bucket_rows"]:
        source_credit: dict[int, float] = defaultdict(float)
        source_cells: dict[int, list[dict[str, Any]]] = defaultdict(list)
        source_pairs: dict[int, dict[str, float]] = defaultdict(lambda: defaultdict(float))
        for cell in bucket["all_secondary_cells"]:
            for pair in cell["secondary_pairs"]:
                positive_p = pair["positive_p"]
                source_credit[positive_p] += pair["pair_credit_ratio"]
                source_pairs[positive_p][pair["pair_key"]] += pair["pair_credit_ratio"]
                source_cells[positive_p].append(
                    {
                        "omega": cell["omega"],
                        "shell": cell["shell"],
                        "sign_word": cell["sign_word"],
                        "pair_key": pair["pair_key"],
                        "pair_credit_ratio": pair["pair_credit_ratio"],
                    }
                )
        source_rows = []
        for positive_p, credit in sorted(source_credit.items(), key=lambda item: item[1], reverse=True):
            source_rows.append(
                {
                    "positive_p": positive_p,
                    "credit_ratio": credit,
                    "credit_share_of_residual": safe_ratio(
                        credit,
                        bucket["residual_needed_ratio"],
                    ),
                    "cell_count_with_multiplicity": len(source_cells[positive_p]),
                    "pair_rows": [
                        {
                            "pair_key": pair_key,
                            "credit_ratio": pair_credit,
                        }
                        for pair_key, pair_credit in sorted(
                            source_pairs[positive_p].items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    ],
                    "cells": sorted(
                        source_cells[positive_p],
                        key=lambda item: item["pair_credit_ratio"],
                        reverse=True,
                    ),
                }
            )
        cover = greedy_source_cover(source_rows, bucket["residual_needed_ratio"])
        cover_credit = sum(row["credit_ratio"] for row in cover)
        bucket_rows.append(
            {
                "bucket": bucket["bucket"],
                "residual_needed_ratio": bucket["residual_needed_ratio"],
                "total_secondary_credit_ratio": bucket["computed_secondary_credit_ratio"],
                "source_count": len(source_rows),
                "cover_source_count": len(cover),
                "cover_credit_ratio": cover_credit,
                "cover_surplus_ratio": cover_credit - bucket["residual_needed_ratio"],
                "source_cover_sufficient": cover_credit + 1e-12 >= bucket["residual_needed_ratio"],
                "source_rows": source_rows,
                "cover_sources": cover,
            }
        )

    unbalanced = next(row for row in bucket_rows if row["bucket"] == "unbalanced<=8")
    mid = next(row for row in bucket_rows if row["bucket"] == "mid<=4")
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_nonprincipal_source_budget_router",
        "status": "z61_nonprincipal_secondary_reduced_to_source_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": extractor["p_list"],
        "z": extractor["z"],
        "principal_positive_p": extractor["principal_positive_p"],
        "source_budget_materialized": True,
        "sample_source_cover_all_residuals": all(row["source_cover_sufficient"] for row in bucket_rows),
        "mid_cover_sources": [row["positive_p"] for row in mid["cover_sources"]],
        "unbalanced_cover_sources": [row["positive_p"] for row in unbalanced["cover_sources"]],
        "unbalanced_cover_source_count": unbalanced["cover_source_count"],
        "source_credit_invariant_proved": False,
        "source_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "bucket_rows": bucket_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "非主正相位残量可进一步按来源 P 汇总。"
            "`mid<=4` 由 `200003` 一个来源单独覆盖；"
            "`unbalanced<=8` 由 `36739` 与 `200003` 两个来源覆盖，且不需要 `10007`。"
            "因此下一硬点压成两个来源的非主信用下界，或输出 Source-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 非主正相位来源预算",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"principal_positive_p={result['principal_positive_p']}",
        f"source_budget_materialized={fmt_bool(result['source_budget_materialized'])}",
        f"sample_source_cover_all_residuals={fmt_bool(result['sample_source_cover_all_residuals'])}",
        f"mid_cover_sources={','.join(str(item) for item in result['mid_cover_sources'])}",
        f"unbalanced_cover_sources={','.join(str(item) for item in result['unbalanced_cover_sources'])}",
        f"source_credit_invariant_proved={fmt_bool(result['source_credit_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 来源预算覆盖",
        "",
        "| bucket | residual need | total secondary | cover sources | cover credit | surplus |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['residual_needed_ratio'])} | "
            f"{fmt_float(row['total_secondary_credit_ratio'])} | "
            f"{row['cover_source_count']} | {fmt_float(row['cover_credit_ratio'])} | "
            f"{fmt_float(row['cover_surplus_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 来源明细",
            "",
            "| bucket | positive P | credit | credit/residual | top pairs |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for bucket in result["bucket_rows"]:
        for row in bucket["source_rows"]:
            pairs = ", ".join(
                f"{pair['pair_key']}:{fmt_float(pair['credit_ratio'])}"
                for pair in row["pair_rows"]
            )
            lines.append(
                f"| `{bucket['bucket']}` | {row['positive_p']} | "
                f"{fmt_float(row['credit_ratio'])} | "
                f"{fmt_float(row['credit_share_of_residual'])} | `{pairs}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 覆盖来源的主要单元",
            "",
            "| bucket | positive P | omega | shell | signs | pair | credit |",
            "| --- | ---: | ---: | --- | --- | --- | ---: |",
        ]
    )
    for bucket in result["bucket_rows"]:
        for source in bucket["cover_sources"]:
            for cell in source["cells"][:8]:
                lines.append(
                    f"| `{bucket['bucket']}` | {source['positive_p']} | "
                    f"{cell['omega']} | `{cell['shell']}` | `{cell['sign_word']}` | "
                    f"`{cell['pair_key']}` | {fmt_float(cell['pair_credit_ratio'])} |"
                )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：非主正相位 residual 到来源 P 预算的合并账本。",
            "- 剩余：证明 `unbalanced<=8` 的 `36739+200003` 两来源信用下界。",
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
                "sample_source_cover_all_residuals": result["sample_source_cover_all_residuals"],
                "unbalanced_cover_sources": result["unbalanced_cover_sources"],
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
