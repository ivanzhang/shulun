#!/usr/bin/env python3
"""生成 strict 稀疏预算在正余量最新前沿下的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_sparse_budget_positive_margin_latest_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json
  docs/monograph/prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.md"

SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
EFFECTIVE_PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
BETA_APPENDIX = (
    "BetaSieveLowerWeightRecursiveConstructionLedger AND "
    "BetaSieveLowerBoundDominanceProof AND "
    "BetaSieveMainCoefficientExplicit99PercentPGe100000"
)

SOURCE_FILES = [
    "prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json",
    "prime-matrix-strict-sparse-budget-after-unified-sync-router.json",
    "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json",
    "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json",
    "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
    "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json",
    "prime-matrix-strict-named-return-terminal-saturation-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
        "experiments/prime_matrix_strict_sparse_budget_positive_margin_latest_sync_router.py": sha256(
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


def lane_rows() -> list[dict[str, str]]:
    """列出稀疏预算的当前分解通道。"""
    return [
        {
            "lane": "pure nonpersistent sparse lane",
            "reduction": f"{SPARSE_BUDGET} -> {STRICT_MARGIN} -> {COLD_NUMERIC}",
            "status": "structure_closed_numeric_open",
            "meaning": "需求项、非持久回流吸收、冷供给公式和 Lambda 纪律已锁同参数；剩余是冷供给数值包。",
        },
        {
            "lane": "cold numeric envelope",
            "reduction": f"{COLD_NUMERIC} -> {EFFECTIVE_PRUNING} AND {COLD_CORE_TABLE} AND {PDEC_TABLE}",
            "status": "open",
            "meaning": "粗 full-depth 历史包过大，必须用有效剪枝或同参数数值表缩小 U_np。",
        },
        {
            "lane": "hot/fixed escape",
            "reduction": f"{HOT_CORE} AND {FIXED_HISTORY}",
            "status": "parallel_open",
            "meaning": "热核心和固定历史不能记入非持久冷供给；它们仍需排斥或登记终端回流。",
        },
        {
            "lane": "persistent terminal family",
            "reduction": MOVING_ATOM,
            "status": "parallel_open",
            "meaning": "持久命名回流仍需 actual noncanonical moving atom / acyclic 终端族排斥。",
        },
    ]


def imported_flags(data: dict[str, dict[str, Any]]) -> dict[str, bool]:
    """读取同步所需上游标志。"""
    positive = data["positive"]
    sparse = data["sparse"]
    same = data["same"]
    cold = data["cold"]
    cold_after = data["cold_after"]
    carrier = data["carrier"]
    named = data["named"]
    return {
        "sparse_budget_target_imported_from_positive": positive.get("next_direct_attack_target") == SPARSE_BUDGET,
        "positive_margin_frontier_synced": positive.get(
            "positive_margin_after_finite_prefix_terminal_sync_closed"
        )
        is True,
        "sparse_budget_normal_form_closed": sparse.get(
            "same_parameter_sparse_demand_cold_supply_normal_form_closed"
        )
        is True,
        "same_parameter_sparse_margin_reduced_to_cold_numeric": same.get(
            "same_parameter_sparse_margin_internal_reduction_closed"
        )
        is True,
        "cold_numeric_reduced_to_effective_pruning": cold.get("crude_full_depth_history_envelope_rejected_as_sufficient")
        is True
        and cold.get("cold_supply_formula_sync_closed") is True,
        "cold_after_return_cycle_reduced_to_tables": cold_after.get(
            "cold_supply_same_parameter_numeric_envelope_proved"
        )
        is False
        and cold_after.get("next_direct_attack_target") == COLD_CORE_TABLE,
        "carrier_return_frontier_aligned": carrier.get("return_branch_alphabet_frontier_closed") is True,
        "named_terminal_saturation_imported": named.get("named_return_terminal_saturation_sync_closed") is True,
    }


def build_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    sync_closed = (
        flags["sparse_budget_target_imported_from_positive"]
        and flags["positive_margin_frontier_synced"]
        and flags["sparse_budget_normal_form_closed"]
        and flags["same_parameter_sparse_margin_reduced_to_cold_numeric"]
        and flags["cold_numeric_reduced_to_effective_pruning"]
        and flags["carrier_return_frontier_aligned"]
        and flags["named_terminal_saturation_imported"]
    )
    return [
        row(
            "SparseBudgetTargetImportedFromPositiveMargin",
            flags["sparse_budget_target_imported_from_positive"],
            False,
            "正余量最新同步后，当前最窄主攻点就是非持久稀疏预算反超。",
            SPARSE_BUDGET,
        ),
        row(
            "SparseBudgetNormalFormImported",
            flags["sparse_budget_normal_form_closed"],
            flags["sparse_budget_normal_form_closed"],
            "SparseHistoryDemand... 已等价压成同参数稀疏供需严格余量。",
            STRICT_MARGIN,
        ),
        row(
            "SameParameterSparseMarginReducedToColdNumeric",
            flags["same_parameter_sparse_margin_reduced_to_cold_numeric"],
            flags["same_parameter_sparse_margin_reduced_to_cold_numeric"],
            "纯非持久分支内部剩余已压成 ColdSupplySameParameterNumericEnvelope。",
            COLD_NUMERIC,
        ),
        row(
            "ColdNumericEnvelopeReducedToEffectivePruningAndTables",
            flags["cold_numeric_reduced_to_effective_pruning"],
            False,
            "粗历史数包已被证明过宽；必须证明有效冷历史剪枝或给出 C_core/T_PDEC 数值表。",
            f"{EFFECTIVE_PRUNING} AND {COLD_CORE_TABLE} AND {PDEC_TABLE}",
        ),
        row(
            "CarrierReturnFrontierAligned",
            flags["carrier_return_frontier_aligned"],
            flags["carrier_return_frontier_aligned"],
            "carrier-lcm return 分支已按非持久预算或持久终端二分登记，不能作为独立局部硬点。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "NamedTerminalSaturationImported",
            flags["named_terminal_saturation_imported"],
            flags["named_terminal_saturation_imported"],
            "命名回流终端饱和同步已导入，非持久/持久通道保持分离。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "SparseBudgetPositiveMarginLatestSyncClosed",
            sync_closed,
            sync_closed,
            "稀疏预算在正余量最新前沿下已同步到冷供给数值包与并行终端出口。",
            f"{EFFECTIVE_PRUNING} AND {COLD_CORE_TABLE} AND {PDEC_TABLE}",
        ),
        row(
            "EffectiveColdHistoryPruningProved",
            False,
            False,
            "尚未证明大多数形式冷历史因除数不兼容、LCM 高度、热核心或固定历史回流而退出冷供给。",
            EFFECTIVE_PRUNING,
        ),
        row(
            "ColdCoreAndPDECNumericTablesProved",
            False,
            False,
            "尚未给出同参数 C_core(W) 与 T_PDEC(W) 的可求和数值表。",
            f"{COLD_CORE_TABLE} AND {PDEC_TABLE}",
        ),
        row(
            "SparseHistoryDemandExceedsNonpersistentSupplyBudgetProved",
            False,
            False,
            "非持久预算反超仍未证明；只是独立黑箱已被删除。",
            f"{EFFECTIVE_PRUNING} AND {COLD_CORE_TABLE} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "持久终端族、DStructure/Rankin 和严格第一性 beta-sieve 附录仍未全部完成。",
            f"{MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造稀疏预算最新同步证书。"""
    data = {
        "positive": load_json("prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json"),
        "sparse": load_json("prime-matrix-strict-sparse-budget-after-unified-sync-router.json"),
        "same": load_json("prime-matrix-strict-same-parameter-sparse-margin-attack-router.json"),
        "cold": load_json("prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json"),
        "cold_after": load_json("prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json"),
        "carrier": load_json("prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json"),
        "named": load_json("prime-matrix-strict-named-return-terminal-saturation-sync-router.json"),
    }
    flags = imported_flags(data)
    rows = build_rows(flags)
    sync_closed = any(
        item["gate"] == "SparseBudgetPositiveMarginLatestSyncClosed" and item["proved"]
        for item in rows
    )
    return {
        "certificate_type": "prime_matrix_strict_sparse_budget_positive_margin_latest_sync_router",
        "status": "sparse_budget_latest_synced_to_cold_numeric_effective_pruning_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "sparse_budget_positive_margin_latest_sync_closed": sync_closed,
        "same_parameter_sparse_margin_reduced_to_cold_numeric": flags[
            "same_parameter_sparse_margin_reduced_to_cold_numeric"
        ],
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "effective_cold_history_pruning_proved": False,
        "cold_core_threshold_numeric_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SPARSE_BUDGET,
        "hardpoint_after_router": (
            f"{EFFECTIVE_PRUNING} AND {COLD_CORE_TABLE} AND {PDEC_TABLE} "
            f"AND {HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": EFFECTIVE_PRUNING,
        "parallel_attack_targets": [
            COLD_CORE_TABLE,
            PDEC_TABLE,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
            BETA_APPENDIX,
        ],
        "lane_rows": lane_rows(),
        "imported_flags": flags,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 已在最新正余量前沿下同步："
            "它不再是独立黑箱，而是经同参数稀疏供需严格余量压到 `ColdSupplySameParameterNumericEnvelope`。"
            "冷供给数值包已证明粗 full-depth 历史包不可用，下一真正最窄点是 "
            "`EffectiveColdHistoryPruningOrHotFixedReturnTheorem`，并行需要 `ColdCoreThresholdFunctionNumericTable` "
            "与 `SameParameterPDECThresholdNumericTable`。热核心、固定历史、moving atom、DStructure 和严格第一性 "
            "beta-sieve 附录仍保留。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 稀疏预算正余量最新同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sparse_budget_positive_margin_latest_sync_closed={fmt_bool(result['sparse_budget_positive_margin_latest_sync_closed'])}",
        f"same_parameter_sparse_margin_reduced_to_cold_numeric={fmt_bool(result['same_parameter_sparse_margin_reduced_to_cold_numeric'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"effective_cold_history_pruning_proved={fmt_bool(result['effective_cold_history_pruning_proved'])}",
        f"cold_core_threshold_numeric_table_proved={fmt_bool(result['cold_core_threshold_numeric_table_proved'])}",
        f"same_parameter_pdec_threshold_numeric_table_proved={fmt_bool(result['same_parameter_pdec_threshold_numeric_table_proved'])}",
        f"sparse_history_demand_exceeds_nonpersistent_supply_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_nonpersistent_supply_budget_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步后分解",
        "",
        "```text",
        result["hardpoint_before_router"],
        "  =>",
        result["hardpoint_after_router"],
        "```",
        "",
        "| lane | reduction | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["lane_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['lane'])}`",
                    table_cell(item["reduction"]),
                    f"`{table_cell(item['status'])}`",
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "sparse_budget_positive_margin_latest_sync_closed="
        f"{fmt_bool(result['sparse_budget_positive_margin_latest_sync_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved="
        f"{fmt_bool(result['sparse_history_demand_exceeds_nonpersistent_supply_budget_proved'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
