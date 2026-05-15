#!/usr/bin/env python3
"""审计 z=61 signed-sum 唯一路径的分支决策账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_branch_decision_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SIGNED_SUM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json"
DOMINANT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json"
TERMINAL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.md"

NEXT_TARGET = "GlobalBranchDecisionPatternBoundOrBranchDecisionPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json",
    "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json",
    "prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_branch_decision_ledger_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_word(signs: tuple[int, ...]) -> str:
    """把 ±1 符号向量写成短字。"""
    return "".join("+" if sign > 0 else "-" for sign in signs)


def enumerate_rest(
    coefficients: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
) -> list[dict[str, Any]]:
    """枚举剩余 signed-sum 行。"""
    rows = []
    target_set = set(targets)
    for signs in product([1, -1], repeat=len(coefficients)):
        signed_sum = sum(sign * coefficient for sign, coefficient in zip(signs, coefficients))
        in_interval = interval_start <= signed_sum < interval_stop
        target_hit = signed_sum % modulus in target_set
        rows.append(
            {
                "sign_word": sign_word(signs),
                "signed_sum": signed_sum,
                "sum_mod": signed_sum % modulus,
                "in_interval": in_interval,
                "target_hit": target_hit,
                "full_hit": in_interval and target_hit,
            }
        )
    return rows


def interval_gap(interval_start: int, interval_stop: int, rest_abs: int) -> int | None:
    """若区间与 [-rest_abs,rest_abs] 不交，返回正间隙。"""
    if interval_stop <= -rest_abs:
        return -rest_abs - interval_stop
    if interval_start > rest_abs:
        return interval_start - rest_abs
    return None


def branch(
    coefficient: int,
    sign: int,
    rest: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
) -> dict[str, Any]:
    """固定一个符号分支并分类。"""
    next_start = interval_start - sign * coefficient
    next_stop = interval_stop - sign * coefficient
    next_targets = sorted({(target - sign * coefficient) % modulus for target in targets})
    rows = enumerate_rest(rest, next_start, next_stop, modulus, next_targets)
    interval_rows = [row for row in rows if row["in_interval"]]
    hits = [row for row in rows if row["full_hit"]]
    rest_abs = sum(abs(value) for value in rest)
    gap = interval_gap(next_start, next_stop, rest_abs)
    if hits:
        status = "survives"
    elif gap is not None:
        status = "interval_empty"
    else:
        status = "residue_empty"
    return {
        "coefficient": coefficient,
        "sign": "+" if sign > 0 else "-",
        "rest_coefficients": rest,
        "rest_abs_sum": rest_abs,
        "rest_interval_start": next_start,
        "rest_interval_stop": next_stop,
        "rest_targets_mod": next_targets,
        "interval_gap": gap,
        "interval_candidate_count": len(interval_rows),
        "hit_count": len(hits),
        "status": status,
        "interval_rows": interval_rows,
        "hits": hits,
    }


def decision_rows(
    peel_coefficients: list[int],
    selected_signs: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
) -> list[dict[str, Any]]:
    """沿唯一路径生成分支决策账本。"""
    rows = []
    remaining = peel_coefficients[:]
    current_start = interval_start
    current_stop = interval_stop
    current_targets = targets[:]
    prefix = ""
    for step, selected_sign in enumerate(selected_signs, start=1):
        coefficient = remaining[0]
        rest = remaining[1:]
        branches = [
            branch(coefficient, sign, rest, current_start, current_stop, modulus, current_targets)
            for sign in [1, -1]
        ]
        selected_branch = next(
            item for item in branches if item["sign"] == ("+" if selected_sign > 0 else "-")
        )
        rejected = [item for item in branches if item is not selected_branch]
        prefix += selected_branch["sign"]
        rows.append(
            {
                "step": step,
                "prefix_after_step": prefix,
                "coefficient": coefficient,
                "selected_sign": selected_branch["sign"],
                "selected_status": selected_branch["status"],
                "selected_hit_count": selected_branch["hit_count"],
                "rejected_statuses": [item["status"] for item in rejected],
                "branches": branches,
            }
        )
        current_start = selected_branch["rest_interval_start"]
        current_stop = selected_branch["rest_interval_stop"]
        current_targets = selected_branch["rest_targets_mod"]
        remaining = rest
    return rows


def audit() -> dict[str, Any]:
    """执行分支决策账本审计。"""
    signed_source = json.loads(SIGNED_SUM_JSON.read_text(encoding="utf-8"))
    dominant_source = json.loads(DOMINANT_JSON.read_text(encoding="utf-8"))
    terminal_source = json.loads(TERMINAL_JSON.read_text(encoding="utf-8"))
    signed_group = signed_source["signed_sum_rows"][0]
    dominant_group = dominant_source["dominant_peel_rows"][0]
    terminal_group = terminal_source["terminal_rows"][0]

    peel_coefficients = [
        dominant_group["dominant_coefficient"],
        dominant_group["second_coefficient"],
        *terminal_group["terminal_coefficients"],
    ]
    selected_signs = [1, 1, -1, -1, -1]
    selected_layer = next(
        row for row in signed_group["layer_rows"] if row["carry"] == signed_group["selected_carry"]
    )
    rows = decision_rows(
        peel_coefficients,
        selected_signs,
        selected_layer["interval_start"],
        selected_layer["interval_stop_exclusive"],
        signed_group["q2"] * signed_group["q4"],
        selected_layer["shifted_combined_sum_targets"],
    )
    rejected_statuses = [
        status for row in rows for status in row["rejected_statuses"]
    ]
    terminal_hits = rows[-1]["branches"][1]["hits"]
    all_rejected_closed = all(
        status in {"interval_empty", "residue_empty"} for status in rejected_statuses
    )
    selected_path_unique = (
        all(row["selected_hit_count"] == 1 for row in rows)
        and len(terminal_hits) == 1
        and terminal_hits[0]["sign_word"] == ""
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_branch_decision_ledger_router",
        "status": "z61_terminal_sign_forcing_reduced_to_branch_decision_ledger_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": terminal_source["certificate_type"],
        "target_bucket": signed_source["target_bucket"],
        "target_omega": signed_source["target_omega"],
        "target_shell": signed_source["target_shell"],
        "branch_decision_group_count": 1,
        "peel_coefficients": peel_coefficients,
        "selected_peel_sign_word": "++---",
        "selected_original_sign_word": "--++-",
        "decision_rows": rows,
        "rejected_statuses": rejected_statuses,
        "all_rejected_branches_closed": all_rejected_closed,
        "selected_path_unique": selected_path_unique,
        "branch_decision_ledger_closed": all_rejected_closed and selected_path_unique,
        "global_branch_decision_pattern_bound_proved": False,
        "branch_decision_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "当前 z=61 signed-sum 唯一路径可整理为 5 步分支决策账本。"
            "所选路径为 peel 坐标 `++---`，对应原 CRT 符号 `--++-`。"
            "所有兄弟分支均已分类为 interval-empty 或 residue-empty，"
            "末端空剩余和唯一命中确认没有隐藏第二路径。"
            "因此最新硬点是把这种分支决策模式提升为全局界，或登记 BranchDecision-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 branch decision ledger",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"branch_decision_group_count={result['branch_decision_group_count']}",
        f"all_rejected_branches_closed={fmt_bool(result['all_rejected_branches_closed'])}",
        f"selected_path_unique={fmt_bool(result['selected_path_unique'])}",
        f"global_branch_decision_pattern_bound_proved={fmt_bool(result['global_branch_decision_pattern_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 决策摘要",
        "",
        "| peel coefficients | selected peel sign | selected original sign | rejected statuses | closed |",
        "| --- | --- | --- | --- | --- |",
        f"| `{result['peel_coefficients']}` | `{result['selected_peel_sign_word']}` | "
        f"`{result['selected_original_sign_word']}` | `{result['rejected_statuses']}` | "
        f"{fmt_bool(result['branch_decision_ledger_closed'])} |",
        "",
        "## 2. 分支账本",
        "",
        "| step | coeff | selected | prefix | selected hits | rejected statuses |",
        "| ---: | ---: | --- | --- | ---: | --- |",
    ]
    for row in result["decision_rows"]:
        lines.append(
            f"| {row['step']} | {row['coefficient']} | `{row['selected_sign']}` | "
            f"`{row['prefix_after_step']}` | {row['selected_hit_count']} | "
            f"`{row['rejected_statuses']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 被拒分支细节",
            "",
            "| step | coeff | rejected sign | status | interval | rest abs | gap | interval candidates | hits |",
            "| ---: | ---: | --- | --- | --- | ---: | --- | ---: | ---: |",
        ]
    )
    for row in result["decision_rows"]:
        for branch_row in row["branches"]:
            if branch_row["sign"] == row["selected_sign"]:
                continue
            gap = "" if branch_row["interval_gap"] is None else branch_row["interval_gap"]
            lines.append(
                f"| {row['step']} | {row['coefficient']} | `{branch_row['sign']}` | "
                f"`{branch_row['status']}` | "
                f"`[{branch_row['rest_interval_start']},{branch_row['rest_interval_stop']})` | "
                f"{branch_row['rest_abs_sum']} | {gap} | "
                f"{branch_row['interval_candidate_count']} | {branch_row['hit_count']} |"
            )
    lines.extend(
        [
            "",
            "## 4. 自足小引理",
            "",
            "每个剥离节点只需验收两个事实之一：",
            "",
            "```text",
            "interval-empty:  [L-epsilon*A,H-epsilon*A) 与 [-R,R] 不交；",
            "residue-empty:   区间候选存在，但没有候选落入平移后的目标同余类。",
            "```",
            "",
            "若所有非选中兄弟分支满足上述二者之一，而选中路径末端只有一个空剩余命中，"
            "则该 formal unit 的 signed-sum 纤维是单点。",
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的所有非选中分支均被区间空或同余空排除，选中路径唯一。",
            "- 未闭合：把该分支决策模式提升为全局 bound，或排斥 BranchDecision-PDEC。",
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
                "branch_decision_ledger_closed": result["branch_decision_ledger_closed"],
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
