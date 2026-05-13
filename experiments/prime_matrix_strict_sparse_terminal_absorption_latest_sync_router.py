#!/usr/bin/env python3
"""生成 strict 稀疏终端历史吸收最新同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_sparse_terminal_absorption_latest_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json
  docs/monograph/prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.md"

SPARSE_ABSORB = "SparseTerminalHistorySAEAbsorptionOrPDECExclusion"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
SAME_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
EFFECTIVE_PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
TREE_PACKING = "DivisorCompatibleColdHistoryTreePackingBound"
PREFIX_BRANCHING = "ColdHistoryPrefixBranchingHotOrFixedReturnLemma"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-multisource-fanin-small-quotient-router.json",
    "prime-matrix-strict-sparse-terminal-history-router.json",
    "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json",
    "prime-matrix-strict-sparse-budget-after-unified-sync-router.json",
    "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json",
    "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json",
    "prime-matrix-strict-effective-cold-history-pruning-router.json",
    "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_sparse_terminal_absorption_latest_sync_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def sync_chain_rows() -> list[dict[str, str]]:
    """列出稀疏终端历史吸收的最新同步链。"""
    return [
        {
            "stage": "finite encoding",
            "result": "history words W have finite depth and finite quotient alphabet",
            "next": "PDEC/SAE dichotomy",
        },
        {
            "stage": "fanin update",
            "result": "multi-source fan-in reduces to q<2Lambda bounded quotients",
            "next": "bounded quotient SAE/PDEC",
        },
        {
            "stage": "nonpersistent budget",
            "result": "U_np<=sum_W (T_PDEC(W)-1) C_core(W)",
            "next": "same-parameter margin",
        },
        {
            "stage": "same-parameter margin",
            "result": "M#_{x,z}-E_registered>U_np is the exact strict target",
            "next": "cold supply numeric envelope",
        },
        {
            "stage": "numeric envelope",
            "result": "crude full-depth history count is too wide",
            "next": "effective cold-history pruning",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    independent_removed = result["sparse_terminal_history_independent_hardpoint_removed"]
    return [
        row(
            "FanInBoundedQuotientReductionImported",
            result["multisource_fanin_independent_hardpoint_removed"],
            result["multisource_fanin_independent_hardpoint_removed"],
            "多源 fan-in 已归入有界小商 SAE/PDEC，不再是独立无限出口。",
            SPARSE_ABSORB,
        ),
        row(
            "SparseFiniteEncodingImported",
            result["sparse_terminal_history_finite_encoding_closed"],
            result["sparse_terminal_history_finite_encoding_closed"],
            "稀疏终端历史有有限词编码和 PDEC/SAE 二分。",
            SPARSE_ABSORB,
        ),
        row(
            "NonpersistentBudgetFormulaImported",
            result["nonpersistent_sae_budget_formula_closed"],
            result["nonpersistent_sae_budget_formula_closed"],
            "非持久稀疏历史供给公式已闭合。",
            SPARSE_BUDGET,
        ),
        row(
            "SparseBudgetSyncedToSameParameterMargin",
            result["same_parameter_sparse_demand_cold_supply_normal_form_closed"],
            False,
            "稀疏预算目标已等价到同参数标量缺口。",
            SAME_MARGIN,
        ),
        row(
            "SparseTerminalIndependentHardpointRemoved",
            independent_removed,
            independent_removed,
            "稀疏终端历史吸收问题已同步到冷供给数值包，不再作为单独硬点。",
            COLD_NUMERIC,
        ),
        row(
            "SparseTerminalHistoryAbsorbed",
            False,
            False,
            "尚未证明同参数严格余量，也未排斥热/固定/持久出口。",
            f"{COLD_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "EffectiveColdHistoryPruningCurrentTarget",
            False,
            False,
            "粗历史包过宽，必须证明有效剪枝或热/固定回流。",
            EFFECTIVE_PRUNING,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{EFFECTIVE_PRUNING} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造稀疏终端历史吸收最新同步证书。"""
    fanin = load_json("prime-matrix-strict-multisource-fanin-small-quotient-router.json")
    sparse = load_json("prime-matrix-strict-sparse-terminal-history-router.json")
    budget = load_json("prime-matrix-strict-sparse-terminal-history-sae-budget-router.json")
    sparse_sync = load_json("prime-matrix-strict-sparse-budget-after-unified-sync-router.json")
    same_margin = load_json("prime-matrix-strict-same-parameter-sparse-margin-attack-router.json")
    cold_numeric = load_json("prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json")

    fanin_removed = fanin.get("multisource_fanin_independent_hardpoint_removed") is True
    finite_encoding = sparse.get("history_word_encoding_closed") is True
    nonpersistent_formula = budget.get("nonpersistent_sae_budget_formula_closed") is True
    same_parameter = sparse_sync.get("same_parameter_sparse_demand_cold_supply_normal_form_closed") is True
    margin_reduction = same_margin.get("same_parameter_sparse_margin_internal_reduction_closed") is True
    crude_rejected = cold_numeric.get("crude_full_depth_history_envelope_rejected_as_sufficient") is True
    independent_removed = (
        fanin_removed and finite_encoding and nonpersistent_formula and same_parameter and margin_reduction
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_sparse_terminal_absorption_latest_sync_router",
        "status": "sparse_terminal_absorption_synced_to_effective_pruning_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "multisource_fanin_independent_hardpoint_removed": fanin_removed,
        "sparse_terminal_history_finite_encoding_closed": finite_encoding,
        "nonpersistent_sae_budget_formula_closed": nonpersistent_formula,
        "same_parameter_sparse_demand_cold_supply_normal_form_closed": same_parameter,
        "same_parameter_sparse_margin_internal_reduction_closed": margin_reduction,
        "crude_full_depth_history_envelope_rejected_as_sufficient": crude_rejected,
        "sparse_terminal_history_independent_hardpoint_removed": independent_removed,
        "sparse_terminal_history_absorbed": False,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "effective_cold_history_pruning_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SPARSE_ABSORB,
        "hardpoint_after_router": (
            f"{EFFECTIVE_PRUNING} AND {TREE_PACKING} AND {PREFIX_BRANCHING} "
            f"AND {KERNEL_BUDGET} AND {TERMINAL_ANTICASCADE}"
        ),
        "next_direct_attack_target": EFFECTIVE_PRUNING,
        "parallel_attack_targets": [
            TREE_PACKING,
            PREFIX_BRANCHING,
            KERNEL_BUDGET,
            TERMINAL_ANTICASCADE,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "sync_chain_rows": sync_chain_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SparseTerminalHistorySAEAbsorptionOrPDECExclusion` 已同步到最新前沿："
            "稀疏历史有有限词编码，非持久分支有 SAE 求和公式；刚关闭的多源 fan-in 小商归约"
            "把覆盖超图移入有界商型 SAE/PDEC，不再留下独立无界出口。于是稀疏终端历史本身"
            "不再是活动硬点，真正剩余是同参数冷供给数值包；而粗 full-depth 历史数已被证明过宽，"
            "所以最新主攻点回到 `EffectiveColdHistoryPruningOrHotFixedReturnTheorem`。"
            "本步不声称稀疏终端历史已被吸收，也不声称行/列命题无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 稀疏终端历史吸收最新同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"multisource_fanin_independent_hardpoint_removed={fmt_bool(result['multisource_fanin_independent_hardpoint_removed'])}",
        f"sparse_terminal_history_finite_encoding_closed={fmt_bool(result['sparse_terminal_history_finite_encoding_closed'])}",
        f"nonpersistent_sae_budget_formula_closed={fmt_bool(result['nonpersistent_sae_budget_formula_closed'])}",
        f"same_parameter_sparse_demand_cold_supply_normal_form_closed={fmt_bool(result['same_parameter_sparse_demand_cold_supply_normal_form_closed'])}",
        f"sparse_terminal_history_independent_hardpoint_removed={fmt_bool(result['sparse_terminal_history_independent_hardpoint_removed'])}",
        f"sparse_terminal_history_absorbed={fmt_bool(result['sparse_terminal_history_absorbed'])}",
        f"effective_cold_history_pruning_proved={fmt_bool(result['effective_cold_history_pruning_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 同步链",
        "",
        "| stage | result | next |",
        "|---|---|---|",
    ]
    for item in result["sync_chain_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['stage'])}` | "
            f"{table_cell(item['result'])} | "
            f"`{table_cell(item['next'])}` |"
        )

    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['gate'])}` | "
            f"`{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | "
            f"{table_cell(item['meaning'])} | "
            f"`{table_cell(item['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")

    lines.extend(
        [
            "",
            "## 证据哈希",
            "",
            "| file | sha256 |",
            "|---|---|",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
