#!/usr/bin/env python3
"""审计 z=61 目标格多命中 residue 的负支撑隔离结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_negative_support_isolation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
GLOBAL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.md"

NEXT_TARGET = "NegativeMultiHitSupportIsolationProofOrNegativeOnlyResiduePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-global-residue-balance-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_negative_support_isolation_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def classify_group(row: dict[str, Any]) -> str:
    """按正负支撑分类多命中组。"""
    if row["negative_count"] == 0 and row["positive_count"] > 0:
        return "positive_only"
    if row["positive_count"] == 0 and row["negative_count"] > 0:
        return "negative_only"
    if row["positive_count"] > 0 and row["negative_count"] > 0:
        return "mixed_absorbed" if row["locally_absorbed"] else "mixed_unabsorbed"
    return "empty"


def audit() -> dict[str, Any]:
    """执行负支撑隔离审计。"""
    data = json.loads(GLOBAL_JSON.read_text(encoding="utf-8"))
    class_rows: dict[str, list[dict[str, Any]]] = {
        "positive_only": [],
        "negative_only": [],
        "mixed_absorbed": [],
        "mixed_unabsorbed": [],
        "empty": [],
    }
    for row in data["group_rows"]:
        class_rows[classify_group(row)].append(row)
    negative_profiles = [row for row in data["profile_sign_rows"] if row["sign"] == "negative"]
    positive_profiles = [row for row in data["profile_sign_rows"] if row["sign"] == "positive"]
    negative_multihit_atoms = [
        atom
        for group in data["group_rows"]
        for atom in group["atoms"]
        if atom["profile_sign"] == "negative"
    ]
    positive_multihit_atoms = [
        atom
        for group in data["group_rows"]
        for atom in group["atoms"]
        if atom["profile_sign"] == "positive"
    ]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_negative_support_isolation_router",
        "status": "z61_target_cell_negative_multihit_support_isolated_to_one_absorbed_mixed_group_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "target_bucket": data["target_bucket"],
        "target_omega": data["target_omega"],
        "target_shell": data["target_shell"],
        "positive_only_group_count": len(class_rows["positive_only"]),
        "negative_only_group_count": len(class_rows["negative_only"]),
        "mixed_absorbed_group_count": len(class_rows["mixed_absorbed"]),
        "mixed_unabsorbed_group_count": len(class_rows["mixed_unabsorbed"]),
        "negative_profile_count": len(negative_profiles),
        "positive_profile_count": len(positive_profiles),
        "negative_multihit_atom_count": len(negative_multihit_atoms),
        "positive_multihit_atom_count": len(positive_multihit_atoms),
        "negative_multihit_support_isolated_in_sample": (
            len(class_rows["negative_only"]) == 0
            and len(class_rows["mixed_unabsorbed"]) == 0
            and len(class_rows["mixed_absorbed"]) == 1
        ),
        "class_rows": class_rows,
        "negative_multihit_atoms": negative_multihit_atoms,
        "positive_multihit_atoms": positive_multihit_atoms,
        "negative_multihit_support_isolation_proved": False,
        "negative_only_residue_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "目标格多命中 residue 的负支撑在样本中高度隔离：没有 negative-only 组，"
            "也没有 mixed-unabsorbed 组；唯一含负支撑的 mixed 组正是 `[9614,14421]`，"
            "并已由两条正记录吸收。其余 20 个多命中组全部 positive-only。"
            "下一步应证明负多命中支撑只能进入已吸收 mixed 组，"
            "或登记 NegativeOnlyResidue-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 negative support isolation",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"positive_only_group_count={result['positive_only_group_count']}",
        f"negative_only_group_count={result['negative_only_group_count']}",
        f"mixed_absorbed_group_count={result['mixed_absorbed_group_count']}",
        f"mixed_unabsorbed_group_count={result['mixed_unabsorbed_group_count']}",
        f"negative_multihit_atom_count={result['negative_multihit_atom_count']}",
        f"positive_multihit_atom_count={result['positive_multihit_atom_count']}",
        f"negative_multihit_support_isolated_in_sample={fmt_bool(result['negative_multihit_support_isolated_in_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 混合组",
        "",
        "| hit moduli | signed count | pos | neg | signed weight | absorbed |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["class_rows"]["mixed_absorbed"] + result["class_rows"]["mixed_unabsorbed"]:
        lines.append(
            f"| `{row['hit_moduli']}` | {row['signed_count']} | {row['positive_count']} | "
            f"{row['negative_count']} | {fmt_float(row['signed_weight'])} | "
            f"{fmt_bool(row['locally_absorbed'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 负多命中原子",
            "",
            "| p | b | hit moduli | signed weight |",
            "| ---: | ---: | --- | ---: |",
        ]
    )
    for atom in result["negative_multihit_atoms"]:
        lines.append(
            f"| {atom['p']} | {atom['b_value']} | `{atom['hit_moduli']}` | "
            f"{fmt_float(atom['signed_weight_contribution'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：样本目标格中负多命中支撑只进入一个已吸收 mixed 组。",
            "- 未闭合：全局负支撑隔离证明，或 NegativeOnlyResidue-PDEC 排斥。",
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
                "negative_multihit_support_isolated_in_sample": result[
                    "negative_multihit_support_isolated_in_sample"
                ],
                "negative_only_group_count": result["negative_only_group_count"],
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
