#!/usr/bin/env python3
"""生成 strict 稀疏终端历史 SAE 预算比较路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_sparse_terminal_history_sae_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sparse-terminal-history-sae-budget-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md",
    MONOGRAPH / "prime-matrix-strict-iterated-threshold-collapse-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
]

SPARSE_SAE_BUDGET = "SparseTerminalHistorySAEBudgetComparison"
FORCED_LOAD = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
MULTIPLICITY_CAP = "FormalUnitSparseHistoryMultiplicityCap"
ADAPTIVE_LAMBDA = "AdaptiveLambdaBalanceForIteratedCoreDensity"
FIXED_HISTORY_PDEC = "FixedTypeHistoryPDECExclusion"
BUDGET_GAP = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def lemmas() -> list[dict[str, str]]:
    """列出 SAE 预算比较引理。"""
    return [
        {
            "name": "nonpersistent_budget_formula",
            "formula": "If no history W is persistent, U_sparse <= sum_W (T_PDEC(W)-1) Cap(W).",
            "status": "closed",
            "meaning": "非持久稀疏历史的总供给上界已写成显式求和。",
        },
        {
            "name": "history_count_inserted",
            "formula": "sum_W may be bounded by sum_{r<=R} prod_{i<=r} A_{Lambda_i}, A_{Lambda_i}<=8Lambda_i^2.",
            "status": "closed",
            "meaning": "历史词数量上界已接入 SAE 预算。",
        },
        {
            "name": "single_history_capacity_slot",
            "formula": "Cap(W) is controlled by formal-unit multiplicity and the terminal core interval for h/D(W).",
            "status": "registered_input",
            "meaning": "单历史容量不再无名，交给 FormalUnitSparseHistoryMultiplicityCap。",
        },
        {
            "name": "forced_load_comparison",
            "formula": "If L_forced > U_sparse, then nonpersistent SAE supply cannot pay the early-zero-row obligation.",
            "status": "closed_criterion",
            "meaning": "供给小于需求时直接形成反例链矛盾。",
        },
        {
            "name": "pdec_or_budget_gap",
            "formula": "Every sparse terminal packet is either persistent PDEC or must satisfy L_forced <= U_sparse.",
            "status": "closed_dichotomy",
            "meaning": "稀疏终端不再是开放黑箱，只剩 PDEC 排斥或预算缺口。",
        },
        {
            "name": "budget_gap_input",
            "formula": "Prove L_forced > sum_W (T_PDEC(W)-1) Cap(W) after choosing Lambda schedule.",
            "status": "open_input",
            "meaning": "最新最窄硬点是需求下界与非持久供给上界的显式比较。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的稀疏终端历史 SAE 分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "NonpersistentSAEBudgetFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "若无持久历史 PDEC，总供给由历史求和上界控制。",
            "remaining": MULTIPLICITY_CAP,
        },
        {
            "gate": "ForcedLoadComparisonCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "`L_forced>U_sparse` 时得到供给-需求矛盾。",
            "remaining": FORCED_LOAD,
        },
        {
            "gate": "SparseTerminalPDECOrBudgetGapClosed",
            "closed": True,
            "proved": True,
            "meaning": "稀疏终端历史只剩持久 PDEC 或非持久预算比较。",
            "remaining": f"{FIXED_HISTORY_PDEC} OR {BUDGET_GAP}",
        },
        {
            "gate": "SparseHistoryDemandExceedsBudgetProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明早期零行强制负载严格超过非持久历史供给预算。",
            "remaining": f"{FORCED_LOAD} AND {MULTIPLICITY_CAP} AND {ADAPTIVE_LAMBDA}",
        },
        {
            "gate": "SparseTerminalHistorySAEBudgetProved",
            "closed": False,
            "proved": False,
            "meaning": "预算公式闭合，但关键不等式和固定历史 PDEC 排斥尚未完成。",
            "remaining": f"{BUDGET_GAP} AND {FIXED_HISTORY_PDEC}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_sparse_terminal_history_sae_budget_router",
        "status": "sparse_terminal_history_sae_budget_formula_closed_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "nonpersistent_sae_budget_formula_closed": True,
        "history_count_inserted": True,
        "forced_load_comparison_criterion_closed": True,
        "sparse_terminal_pdec_or_budget_gap_closed": True,
        "sparse_history_demand_exceeds_budget_proved": False,
        "forced_load_lower_bound_proved": False,
        "formal_unit_sparse_history_multiplicity_cap_proved": False,
        "fixed_type_history_pdec_excluded": False,
        "sparse_terminal_history_sae_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BUDGET_GAP,
        "parallel_targets": [FORCED_LOAD, MULTIPLICITY_CAP, ADAPTIVE_LAMBDA, FIXED_HISTORY_PDEC],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "稀疏终端 SAE 预算公式已经闭合。若没有任何历史词 W 持久复现进入 PDEC，"
            "则总稀疏供给满足 U_sparse <= sum_W (T_PDEC(W)-1) Cap(W)。"
            "历史词数量由有限深度和有限字母表控制；单历史容量交给 formal-unit 重数上界。"
            "因此稀疏终端分支只剩一个明确供需不等式：证明早期零行强制负载 "
            "L_forced 严格超过非持久历史供给预算，或排斥持久历史 PDEC。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 稀疏终端历史 SAE 预算比较路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"nonpersistent_sae_budget_formula_closed={fmt_bool(result['nonpersistent_sae_budget_formula_closed'])}",
        f"history_count_inserted={fmt_bool(result['history_count_inserted'])}",
        f"forced_load_comparison_criterion_closed={fmt_bool(result['forced_load_comparison_criterion_closed'])}",
        f"sparse_terminal_pdec_or_budget_gap_closed={fmt_bool(result['sparse_terminal_pdec_or_budget_gap_closed'])}",
        f"sparse_history_demand_exceeds_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_budget_proved'])}",
        f"forced_load_lower_bound_proved={fmt_bool(result['forced_load_lower_bound_proved'])}",
        f"formal_unit_sparse_history_multiplicity_cap_proved={fmt_bool(result['formal_unit_sparse_history_multiplicity_cap_proved'])}",
        f"fixed_type_history_pdec_excluded={fmt_bool(result['fixed_type_history_pdec_excluded'])}",
        f"sparse_terminal_history_sae_budget_proved={fmt_bool(result['sparse_terminal_history_sae_budget_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非持久 SAE 供给",
        "",
        "若所有历史词 `W` 都未达到 PDEC 持久阈值，则",
        "",
        "```text",
        "U_sparse <= sum_W (T_PDEC(W)-1) Cap(W).",
        "```",
        "",
        "历史词集合满足",
        "",
        "```text",
        "#W <= sum_{r<=R} prod_{i<=r} A_{Lambda_i},",
        "A_{Lambda_i} <= 8 Lambda_i^2.",
        "```",
        "",
        "所以当前缺口不是“稀疏终端是什么”，而是供给预算是否小于早期零行强制负载。",
        "",
        "## 2. 供需矛盾口",
        "",
        "若能证明",
        "",
        "```text",
        "L_forced > sum_W (T_PDEC(W)-1) Cap(W),",
        "```",
        "",
        "则非持久 SAE 分支无法支付早期零行反例链的终端义务；若同一历史持久化，则进入 PDEC/ColumnCRT。",
        "",
        "## 3. 引理表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["lemmas"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一步最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行输入：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步闭合 SAE 预算公式和供需判据；未证明需求大于供给，也未排斥固定历史 PDEC。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
