#!/usr/bin/env python3
"""审计 z=61 双臂覆盖的内部靶向结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_two_arm_internal_structure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.md
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
TWO_ARM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.md"

NEXT_TARGET = "SingleTargetArmAndReciprocalExitArmInvariantOrArmStructurePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_two_arm_internal_structure_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行双臂内部结构审计。"""
    two_arm = json.loads(TWO_ARM_JSON.read_text(encoding="utf-8"))
    arm_rows = []
    for arm in two_arm["arm_rows"]:
        pair_credit: dict[str, float] = defaultdict(float)
        target_credit: dict[str, float] = defaultdict(float)
        shell_credit: dict[str, float] = defaultdict(float)
        omega_credit: dict[int, float] = defaultdict(float)
        for cell in arm["cells"]:
            pair_credit[cell["pair_key"]] += cell["credit_ratio"]
            target = cell["pair_key"].split("->")[1]
            target_credit[target] += cell["credit_ratio"]
            shell_credit[cell["shell"]] += cell["credit_ratio"]
            omega_credit[cell["omega"]] += cell["credit_ratio"]
        pair_rows = [
            {
                "pair_key": pair_key,
                "credit_ratio": credit,
                "share_of_arm": safe_ratio(credit, arm["credit_ratio"]),
            }
            for pair_key, credit in sorted(pair_credit.items(), key=lambda item: item[1], reverse=True)
        ]
        target_rows = [
            {
                "negative_p": int(target),
                "credit_ratio": credit,
                "share_of_arm": safe_ratio(credit, arm["credit_ratio"]),
            }
            for target, credit in sorted(target_credit.items(), key=lambda item: item[1], reverse=True)
        ]
        shell_rows = [
            {"shell": shell, "credit_ratio": credit, "share_of_arm": safe_ratio(credit, arm["credit_ratio"])}
            for shell, credit in sorted(shell_credit.items(), key=lambda item: item[1], reverse=True)
        ]
        omega_rows = [
            {"omega": omega, "credit_ratio": credit, "share_of_arm": safe_ratio(credit, arm["credit_ratio"])}
            for omega, credit in sorted(omega_credit.items(), key=lambda item: item[1], reverse=True)
        ]
        arm_rows.append(
            {
                "positive_p": arm["positive_p"],
                "credit_ratio": arm["credit_ratio"],
                "target_count": len(target_rows),
                "pair_count": len(pair_rows),
                "is_single_target_arm": len(target_rows) == 1,
                "has_exit_target": len(target_rows) > 1,
                "pair_rows": pair_rows,
                "target_rows": target_rows,
                "shell_rows": shell_rows,
                "omega_rows": omega_rows,
                "cells": arm["cells"],
            }
        )
    single_target_arms = [row for row in arm_rows if row["is_single_target_arm"]]
    exit_arms = [row for row in arm_rows if row["has_exit_target"]]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_two_arm_internal_structure_router",
        "status": "z61_two_arm_cover_split_into_single_target_and_exit_arm_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": two_arm["p_list"],
        "z": two_arm["z"],
        "unbalanced_residual_needed_ratio": two_arm["unbalanced_residual_needed_ratio"],
        "unique_five_cell_cover_credit_ratio": two_arm["unique_five_cell_cover_credit_ratio"],
        "arm_count": len(arm_rows),
        "single_target_arm_count": len(single_target_arms),
        "exit_arm_count": len(exit_arms),
        "single_target_plus_exit_arm_schema_materialized": (
            len(arm_rows) == 2 and len(single_target_arms) == 1 and len(exit_arms) == 1
        ),
        "single_target_arm_and_exit_arm_invariant_proved": False,
        "arm_structure_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "arm_rows": arm_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "双臂覆盖内部结构进一步分裂：`36739` 臂是单靶向臂，全部指向 `200003`；"
            "`200003` 臂是互反加出口臂，主要指向 `36739`，另有出口指向 `10007`。"
            "因此下一步可证明单靶向臂与出口臂的组合不变量，或登记 ArmStructure-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 双臂内部结构",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"arm_count={result['arm_count']}",
        f"single_target_arm_count={result['single_target_arm_count']}",
        f"exit_arm_count={result['exit_arm_count']}",
        "single_target_plus_exit_arm_schema_materialized="
        f"{fmt_bool(result['single_target_plus_exit_arm_schema_materialized'])}",
        f"single_target_arm_and_exit_arm_invariant_proved={fmt_bool(result['single_target_arm_and_exit_arm_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 臂画像",
        "",
        "| positive P | credit | targets | pairs | single target | has exit |",
        "| ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for arm in result["arm_rows"]:
        lines.append(
            f"| {arm['positive_p']} | {fmt_float(arm['credit_ratio'])} | "
            f"{arm['target_count']} | {arm['pair_count']} | "
            f"{fmt_bool(arm['is_single_target_arm'])} | {fmt_bool(arm['has_exit_target'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. pair / target 明细",
            "",
            "| positive P | kind | key | credit | share of arm |",
            "| ---: | --- | --- | ---: | ---: |",
        ]
    )
    for arm in result["arm_rows"]:
        for row in arm["pair_rows"]:
            lines.append(
                f"| {arm['positive_p']} | pair | `{row['pair_key']}` | "
                f"{fmt_float(row['credit_ratio'])} | {fmt_float(row['share_of_arm'])} |"
            )
        for row in arm["target_rows"]:
            lines.append(
                f"| {arm['positive_p']} | target | `{row['negative_p']}` | "
                f"{fmt_float(row['credit_ratio'])} | {fmt_float(row['share_of_arm'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：双臂覆盖的内部 pair/target 结构账本。",
            "- 未闭合：证明单靶向臂与出口臂组合不变量，或登记 ArmStructure-PDEC。",
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
                "single_target_plus_exit_arm_schema_materialized": result[
                    "single_target_plus_exit_arm_schema_materialized"
                ],
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
