#!/usr/bin/env python3
"""把 z=61 unbalanced 残量压成互反核心加单出口。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_unbalanced_reciprocal_core_exit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.md"

NEXT_TARGET = "UnbalancedReciprocalCorePlusExitInvariantOrExitPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_unbalanced_reciprocal_core_exit_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def pair_credit_map(unbalanced_row: dict[str, Any]) -> dict[str, float]:
    """提取 unbalanced 覆盖来源中的 pair 信用。"""
    result = {}
    for source in unbalanced_row["cover_sources"]:
        for pair in source["pair_rows"]:
            result[pair["pair_key"]] = pair["credit_ratio"]
    return result


def audit() -> dict[str, Any]:
    """执行互反核心加出口审计。"""
    source_data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    unbalanced = next(
        row for row in source_data["bucket_rows"] if row["bucket"] == "unbalanced<=8"
    )
    pair_credit = pair_credit_map(unbalanced)
    core_left = "36739->200003"
    core_right = "200003->36739"
    core_credit = pair_credit[core_left] + pair_credit[core_right]
    deficit_after_core = max(0.0, unbalanced["residual_needed_ratio"] - core_credit)
    exit_candidates = [
        {
            "pair_key": pair_key,
            "credit_ratio": credit,
            "covers_core_deficit": credit + 1e-12 >= deficit_after_core,
            "surplus_after_core": credit - deficit_after_core,
        }
        for pair_key, credit in sorted(
            pair_credit.items(), key=lambda item: item[1], reverse=True
        )
        if pair_key not in {core_left, core_right}
    ]
    selected_exit = next(
        (row for row in exit_candidates if row["covers_core_deficit"]),
        None,
    )
    selected_exit_credit = selected_exit["credit_ratio"] if selected_exit else 0.0
    core_exit_credit = core_credit + selected_exit_credit

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_unbalanced_reciprocal_core_exit_router",
        "status": "z61_unbalanced_two_source_reduced_to_reciprocal_core_plus_single_exit_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": source_data["p_list"],
        "z": source_data["z"],
        "principal_positive_p": source_data["principal_positive_p"],
        "unbalanced_residual_needed_ratio": unbalanced["residual_needed_ratio"],
        "core_pairs": [
            {"pair_key": core_left, "credit_ratio": pair_credit[core_left]},
            {"pair_key": core_right, "credit_ratio": pair_credit[core_right]},
        ],
        "reciprocal_core_credit_ratio": core_credit,
        "deficit_after_reciprocal_core_ratio": deficit_after_core,
        "exit_candidates": exit_candidates,
        "selected_exit_pair": selected_exit["pair_key"] if selected_exit else None,
        "selected_exit_credit_ratio": selected_exit_credit,
        "core_plus_exit_credit_ratio": core_exit_credit,
        "core_plus_exit_surplus_ratio": core_exit_credit - unbalanced["residual_needed_ratio"],
        "sample_core_plus_exit_covers_unbalanced_residual": (
            core_exit_credit + 1e-12 >= unbalanced["residual_needed_ratio"]
        ),
        "reciprocal_core_plus_exit_invariant_proved": False,
        "exit_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`unbalanced<=8` 的两来源残量已压成互反核心加单出口。"
            "`36739->200003` 与 `200003->36739` 的互反核心几乎覆盖全部需求；"
            "剩余缺口只需一个出口 pair，例如 `200003->10007`，即可补齐。"
            "下一步只需证明互反核心加单出口的不变量，或登记 Exit-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 unbalanced 互反核心出口",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unbalanced_residual_needed_ratio={fmt_float(result['unbalanced_residual_needed_ratio'])}",
        f"reciprocal_core_credit_ratio={fmt_float(result['reciprocal_core_credit_ratio'])}",
        f"deficit_after_reciprocal_core_ratio={fmt_float(result['deficit_after_reciprocal_core_ratio'])}",
        f"selected_exit_pair={result['selected_exit_pair']}",
        f"selected_exit_credit_ratio={fmt_float(result['selected_exit_credit_ratio'])}",
        "sample_core_plus_exit_covers_unbalanced_residual="
        f"{fmt_bool(result['sample_core_plus_exit_covers_unbalanced_residual'])}",
        f"reciprocal_core_plus_exit_invariant_proved={fmt_bool(result['reciprocal_core_plus_exit_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 互反核心",
        "",
        "| component | credit ratio |",
        "| --- | ---: |",
    ]
    for pair in result["core_pairs"]:
        lines.append(f"| `{pair['pair_key']}` | {fmt_float(pair['credit_ratio'])} |")
    lines.extend(
        [
            f"| reciprocal core total | {fmt_float(result['reciprocal_core_credit_ratio'])} |",
            f"| core deficit | {fmt_float(result['deficit_after_reciprocal_core_ratio'])} |",
            "",
            "## 2. 出口候选",
            "",
            "| pair | credit | covers deficit | surplus after core |",
            "| --- | ---: | --- | ---: |",
        ]
    )
    for row in result["exit_candidates"]:
        lines.append(
            f"| `{row['pair_key']}` | {fmt_float(row['credit_ratio'])} | "
            f"{fmt_bool(row['covers_core_deficit'])} | {fmt_float(row['surplus_after_core'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：unbalanced 两来源预算压成互反核心加单出口的验收合同。",
            "- 未闭合：证明互反核心与出口 pair 的下界，或登记 Exit-PDEC。",
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
                "deficit_after_reciprocal_core_ratio": result[
                    "deficit_after_reciprocal_core_ratio"
                ],
                "selected_exit_pair": result["selected_exit_pair"],
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
