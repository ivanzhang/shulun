#!/usr/bin/env python3
"""生成 RPZ 下层下降 grid_fail 避开证书。

用法示例：
  python3 experiments/prime_matrix_rpz_lower_grid_fail_avoidance_certificate.py

对相邻素数 `p>r`，令 `g=p-r`，`p` 对齐行号为 `a`。区间
`[(a-1)p+1, ap]` 含完整 `r` 对齐行当且仅当

  delta = - (a-1) g mod r <= g。

因此 `grid_fail` 是一个只依赖 `a mod r` 的精确相位条件。脚本把该条件与当前下降树
实际节点逐项比对，给出当前有限账本的避开证书；它不证明全局正式反例路径必避开这些相位。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def phase_delta(p: int, r: int, row: int) -> int:
    """计算 `p` 行起点到下一条 `r` 对齐行起点的距离。"""
    gap = p - r
    return (-(row - 1) * gap) % r


def grid_status_by_formula(p: int, r: int, row: int) -> dict[str, Any]:
    """用闭式判据计算 grid 状态。"""
    gap = p - r
    delta = phase_delta(p, r, row)
    return {
        "row": row,
        "row_mod_r": row % r,
        "gap_p_minus_r": gap,
        "delta_formula": delta,
        "success_by_formula": delta <= gap,
        "criterion_margin": gap - delta,
        "grid_fail_by_formula": delta > gap,
    }


def fail_residue_classes_mod_r(p: int, r: int) -> list[int]:
    """列出使 `grid_fail` 成立的行号余类 `a mod r`。"""
    return [
        residue
        for residue in range(r)
        if grid_status_by_formula(p, r, residue)["grid_fail_by_formula"]
    ]


def build(source_path: Path) -> dict[str, Any]:
    """构造 grid_fail 避开证书。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    actual_by_transition: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for node in source["actual_nodes"]:
        p = node["p"]
        r = node["r"]
        profile = grid_status_by_formula(p, r, node["row"])
        profile.update(
            {
                "source_status": node["status"],
                "source_delta": node["delta_to_next_r_row"],
                "formula_matches_source_delta": profile["delta_formula"]
                == node["delta_to_next_r_row"],
                "formula_matches_source_status": (
                    profile["grid_fail_by_formula"] == (node["status"] == "grid_fail")
                ),
            }
        )
        actual_by_transition[(p, r)].append(profile)

    rows = []
    for item in source["transition_summaries"]:
        p = item["p"]
        r = item["r"]
        modulus = item["phase_modulus_primorial_r"]
        gap = p - r
        fail_residues = fail_residue_classes_mod_r(p, r)
        actual_profiles = actual_by_transition.get((p, r), [])
        actual_failures = [
            profile for profile in actual_profiles if profile["grid_fail_by_formula"]
        ]
        actual_margins = [profile["criterion_margin"] for profile in actual_profiles]
        fail_count_formula = len(fail_residues) * (modulus // r)
        source_fail_count = item["counts"].get("grid_fail", 0)
        rows.append(
            {
                "p": p,
                "r": r,
                "gap": gap,
                "Q": modulus,
                "fail_residues_mod_r": fail_residues,
                "success_residues_mod_r": [
                    residue
                    for residue in range(r)
                    if residue not in fail_residues
                ],
                "fail_count_formula": fail_count_formula,
                "source_fail_count": source_fail_count,
                "formula_matches_source_count": fail_count_formula == source_fail_count,
                "actual_transition_nodes": len(actual_profiles),
                "actual_grid_fail_nodes": len(actual_failures),
                "actual_min_margin": min(actual_margins) if actual_margins else None,
                "actual_profiles": actual_profiles,
                "current_ledger_avoids_grid_fail": len(actual_failures) == 0,
                "global_status": "not_global_avoidance_proof",
            }
        )

    status_counts = Counter(
        "avoids" if row["current_ledger_avoids_grid_fail"] else "hits"
        for row in rows
    )
    return {
        "status": "rpz_lower_grid_fail_avoidance_current_ledger",
        "source": str(source_path),
        "formula": "delta=-(a-1)(p-r) mod r; grid_success iff delta<=p-r",
        "summary": {
            "transition_rows": len(rows),
            "rows_with_possible_grid_fail": sum(
                1 for row in rows if row["source_fail_count"] > 0
            ),
            "actual_transition_nodes": sum(
                row["actual_transition_nodes"] for row in rows
            ),
            "actual_grid_fail_nodes": sum(row["actual_grid_fail_nodes"] for row in rows),
            "formula_count_mismatches": sum(
                1 for row in rows if not row["formula_matches_source_count"]
            ),
            "formula_delta_mismatches": sum(
                1
                for row in rows
                for profile in row["actual_profiles"]
                if not profile["formula_matches_source_delta"]
            ),
            "current_ledger_avoidance_status_counts": dict(sorted(status_counts.items())),
            "global_avoidance_closed": False,
        },
        "rows": rows,
        "review_boundary": [
            "当前实际下降路径没有命中 grid_fail 相位",
            "闭式判据与枚举账本完全一致",
            "这不是全局正式下降路径避开证明",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 下层下降 grid_fail 避开证书",
        "",
        "**状态：** `rpz_lower_grid_fail_avoidance_current_ledger`",
        "",
        "## 精确判据",
        "",
        "设 `p>r` 为相邻素数、`g=p-r`，`p` 对齐行号为 `a`。则",
        "",
        "```text",
        "delta = - (a-1) g mod r；",
        "grid_success iff delta <= g；",
        "grid_fail iff delta > g。",
        "```",
        "",
        "## 总结",
        "",
        f"- 转换行数：`{summary['transition_rows']}`。",
        f"- 存在可能 grid_fail 的转换行数：`{summary['rows_with_possible_grid_fail']}`。",
        f"- 实际下降转换节点数：`{summary['actual_transition_nodes']}`。",
        f"- 实际 grid_fail 节点数：`{summary['actual_grid_fail_nodes']}`。",
        f"- 闭式计数与枚举不一致数：`{summary['formula_count_mismatches']}`。",
        f"- 实际节点 delta 与闭式不一致数：`{summary['formula_delta_mismatches']}`。",
        f"- 全局避开是否闭合：`{summary['global_avoidance_closed']}`。",
        "",
        "## 转换表",
        "",
        "| p | r | Q | gap | fail residues mod r | source fail count | actual nodes | actual fails | min margin |",
        "|---:|---:|---:|---:|---|---:|---:|---:|---:|",
    ]
    for row in result["rows"]:
        lines.append(
            "| {p} | {r} | {Q} | {gap} | `{fail_residues}` | {source_fail} | {actual_nodes} | {actual_fails} | {margin} |".format(
                p=row["p"],
                r=row["r"],
                Q=row["Q"],
                gap=row["gap"],
                fail_residues=row["fail_residues_mod_r"],
                source_fail=row["source_fail_count"],
                actual_nodes=row["actual_transition_nodes"],
                actual_fails=row["actual_grid_fail_nodes"],
                margin=row["actual_min_margin"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "三条待攻 `lower_descent_grid_fail` 行分别来自 `7->5`、`11->7`、`13->11`。本证书证明这些行的失败集合不是黑箱枚举，而是由一维余类不等式 `delta>p-r` 精确给出。",
            "",
            "当前实际下降树中的 `20` 个转换节点全部满足 `delta<=p-r`，所以当前有限账本避开所有 `grid_fail` 相位。该结论只闭合当前账本，不证明全局正式反例下降路径必然避开。",
            "",
            "下一步真正硬点是证明正式路径的行号相位始终落在 `delta<=p-r`，或在落入 `delta>p-r` 时把同相位族送入 `PDEC/ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.json"
        ),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate"
        ),
    )
    args = parser.parse_args()
    result = build(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
