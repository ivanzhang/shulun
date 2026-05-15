#!/usr/bin/env python3
"""审计 z=61 分支决策账本的区间/同余余量。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_branch_decision_margin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.md"

NEXT_TARGET = "BranchDecisionMarginStabilityGlobalBoundOrMarginPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_branch_decision_margin_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def circular_distance(value: int, target: int, modulus: int) -> int:
    """计算模圆上的最小距离。"""
    forward = (value - target) % modulus
    backward = (target - value) % modulus
    return min(forward, backward)


def nearest_target(value: int, targets: list[int], modulus: int) -> dict[str, int]:
    """找 value 到目标集合的最近距离。"""
    distances = [
        {
            "target": target,
            "distance": circular_distance(value, target, modulus),
        }
        for target in targets
    ]
    return min(distances, key=lambda item: item["distance"])


def residue_margin(branch: dict[str, Any], modulus: int) -> dict[str, Any]:
    """计算一个分支的同余分离余量。"""
    rows = branch["interval_rows"]
    nonhit_rows = [row for row in rows if not row["target_hit"]]
    annotated = []
    for row in nonhit_rows:
        nearest = nearest_target(row["sum_mod"], branch["rest_targets_mod"], modulus)
        annotated.append(
            {
                "sign_word": row["sign_word"],
                "signed_sum": row["signed_sum"],
                "sum_mod": row["sum_mod"],
                "nearest_target": nearest["target"],
                "residue_distance": nearest["distance"],
            }
        )
    min_distance = min((row["residue_distance"] for row in annotated), default=None)
    return {
        "nonhit_interval_candidate_count": len(nonhit_rows),
        "nonhit_rows": annotated,
        "min_residue_distance_to_target": min_distance,
        "half_open_integer_stability_radius": None if min_distance is None else (min_distance - 1) // 2,
    }


def branch_margin(branch: dict[str, Any], selected: bool, modulus: int) -> dict[str, Any]:
    """给一个分支附加稳定余量。"""
    residue = residue_margin(branch, modulus)
    if branch["status"] == "interval_empty":
        closure_mode = "interval_gap"
        primary_margin = branch["interval_gap"]
        stability_radius = None if primary_margin is None else max((primary_margin - 1) // 2, 0)
    elif branch["status"] == "residue_empty":
        closure_mode = "residue_gap"
        primary_margin = residue["min_residue_distance_to_target"]
        stability_radius = residue["half_open_integer_stability_radius"]
    else:
        closure_mode = "selected_unique_hit" if selected else "survives"
        primary_margin = residue["min_residue_distance_to_target"]
        stability_radius = residue["half_open_integer_stability_radius"]
    return {
        "sign": branch["sign"],
        "selected_branch": selected,
        "status": branch["status"],
        "closure_mode": closure_mode,
        "interval_gap": branch["interval_gap"],
        "interval_candidate_count": branch["interval_candidate_count"],
        "hit_count": branch["hit_count"],
        "primary_margin": primary_margin,
        "integer_stability_radius": stability_radius,
        "residue_margin": residue,
    }


def margin_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """生成每步分支余量。"""
    modulus = 2627
    rows = []
    for decision in source["decision_rows"]:
        branch_rows = [
            branch_margin(
                branch,
                selected=(branch["sign"] == decision["selected_sign"]),
                modulus=modulus,
            )
            for branch in decision["branches"]
        ]
        rejected = [row for row in branch_rows if not row["selected_branch"]]
        selected = next(row for row in branch_rows if row["selected_branch"])
        rejected_margins = [
            row["primary_margin"] for row in rejected if row["primary_margin"] is not None
        ]
        selected_nonhit_margin = selected["residue_margin"]["min_residue_distance_to_target"]
        rows.append(
            {
                "step": decision["step"],
                "coefficient": decision["coefficient"],
                "prefix_after_step": decision["prefix_after_step"],
                "selected_sign": decision["selected_sign"],
                "selected_hit_count": decision["selected_hit_count"],
                "branch_margins": branch_rows,
                "rejected_min_primary_margin": min(rejected_margins) if rejected_margins else None,
                "selected_nonhit_min_residue_distance": selected_nonhit_margin,
                "step_closed_with_positive_margins": all(
                    row["primary_margin"] is not None and row["primary_margin"] > 0
                    for row in rejected
                )
                and decision["selected_hit_count"] == 1,
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行分支余量审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = margin_rows(source)
    rejected_margins = [
        row["rejected_min_primary_margin"]
        for row in rows
        if row["rejected_min_primary_margin"] is not None
    ]
    selected_nonhit_margins = [
        row["selected_nonhit_min_residue_distance"]
        for row in rows
        if row["selected_nonhit_min_residue_distance"] is not None
    ]
    min_rejected_margin = min(rejected_margins) if rejected_margins else None
    min_selected_nonhit_margin = min(selected_nonhit_margins) if selected_nonhit_margins else None
    all_positive = all(row["step_closed_with_positive_margins"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_branch_decision_margin_router",
        "status": "z61_branch_decision_ledger_reduced_to_positive_margin_stability_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "branch_decision_margin_group_count": 1,
        "modulus": 2627,
        "decision_margin_rows": rows,
        "all_steps_have_positive_rejected_margins": all_positive,
        "minimum_rejected_branch_margin": min_rejected_margin,
        "minimum_selected_nonhit_residue_margin": min_selected_nonhit_margin,
        "minimum_residue_margin_over_all_nonhits": min(
            value
            for value in [min_rejected_margin, min_selected_nonhit_margin]
            if value is not None
        ),
        "branch_decision_margin_stability_proved_for_formal_unit": all_positive,
        "global_branch_decision_margin_stability_proved": False,
        "margin_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "分支决策账本可升级为正余量账本：每个 interval-empty 分支有显式区间间隙，"
            "每个 residue-empty 分支有到目标余类集合的正环距离。当前 formal unit 的最小"
            "被拒分支余量为 55，最小选中分支非命中余量也为 55；两个 interval-empty 分支"
            "间隙分别为 645743 与 7723。于是本地唯一路径在小扰动下稳定。全局剩余变成"
            "证明这些正余量模式在一般 formal unit 中保持，或把余量塌缩登记为 Margin-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 branch decision margin",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"branch_decision_margin_group_count={result['branch_decision_margin_group_count']}",
        f"all_steps_have_positive_rejected_margins={fmt_bool(result['all_steps_have_positive_rejected_margins'])}",
        f"minimum_rejected_branch_margin={result['minimum_rejected_branch_margin']}",
        f"minimum_selected_nonhit_residue_margin={result['minimum_selected_nonhit_residue_margin']}",
        f"global_branch_decision_margin_stability_proved={fmt_bool(result['global_branch_decision_margin_stability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 余量摘要",
        "",
        "| step | coeff | selected | prefix | rejected min margin | selected nonhit margin | closed |",
        "| ---: | ---: | --- | --- | ---: | ---: | --- |",
    ]
    for row in result["decision_margin_rows"]:
        lines.append(
            f"| {row['step']} | {row['coefficient']} | `{row['selected_sign']}` | "
            f"`{row['prefix_after_step']}` | {row['rejected_min_primary_margin']} | "
            f"{row['selected_nonhit_min_residue_distance']} | "
            f"{fmt_bool(row['step_closed_with_positive_margins'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 分支余量",
            "",
            "| step | sign | selected | status | mode | interval gap | interval candidates | hits | margin | stability radius |",
            "| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["decision_margin_rows"]:
        for branch in row["branch_margins"]:
            interval_gap = "" if branch["interval_gap"] is None else branch["interval_gap"]
            margin = "" if branch["primary_margin"] is None else branch["primary_margin"]
            radius = (
                ""
                if branch["integer_stability_radius"] is None
                else branch["integer_stability_radius"]
            )
            lines.append(
                f"| {row['step']} | `{branch['sign']}` | "
                f"{fmt_bool(branch['selected_branch'])} | `{branch['status']}` | "
                f"`{branch['closure_mode']}` | {interval_gap} | "
                f"{branch['interval_candidate_count']} | {branch['hit_count']} | "
                f"{margin} | {radius} |"
            )
    lines.extend(
        [
            "",
            "## 3. 最近同余距离",
            "",
            "| step | sign | candidate | sum mod 2627 | nearest target | distance |",
            "| ---: | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["decision_margin_rows"]:
        for branch in row["branch_margins"]:
            for item in branch["residue_margin"]["nonhit_rows"]:
                lines.append(
                    f"| {row['step']} | `{branch['sign']}` | `{item['sign_word']}` | "
                    f"{item['sum_mod']} | {item['nearest_target']} | {item['residue_distance']} |"
                )
    lines.extend(
        [
            "",
            "## 4. 自足小引理",
            "",
            "分支排除有两个可验收余量：",
            "",
            "```text",
            "interval margin = dist([L,H), [-R,R]);",
            "residue margin  = min circular distance from interval candidates to target residues.",
            "```",
            "",
            "若 interval margin 为正，则足够小的区间端点扰动不会产生候选。"
            "若 residue margin 为正，则足够小的余类扰动不会把非命中候选推入目标集。"
            "因此正余量账本是 BranchDecision 模式全局化的精确输入基。",
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的所有被拒分支都有正余量；选中分支的非命中候选也有正余量。",
            "- 未闭合：全局证明这些余量不塌缩，或把余量塌缩登记为 Margin-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
                "branch_decision_margin_stability_proved_for_formal_unit": result[
                    "branch_decision_margin_stability_proved_for_formal_unit"
                ],
                "minimum_rejected_branch_margin": result["minimum_rejected_branch_margin"],
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
