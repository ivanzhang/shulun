#!/usr/bin/env python3
"""生成 strict 同参数核心阈值求和优势路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_parameter_core_threshold_summation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-parameter-core-threshold-summation-router.json

输出：
  docs/monograph/prime-matrix-strict-same-parameter-core-threshold-summation-router.json
  docs/monograph/prime-matrix-strict-same-parameter-core-threshold-summation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-same-parameter-core-threshold-summation-router.json"
OUT_MD = DOCS / "prime-matrix-strict-same-parameter-core-threshold-summation-router.md"

CORE_SUM = "SameParameterCoreThresholdSummationDominanceTable"
CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
SUPPORT_TABLE = "CoreHistoryWeightedSupportMeasureTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
LOAD_LOWER = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
FINITE_RUNNER = "FiniteColdHistorySummationRunnerOrAnalyticEnvelope"
PREFIX_BRANCHING = "ColdHistoryPrefixBranchingHotOrFixedReturnLemma"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
COLD_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
WIDTH_LCM = "SiblingCollarWidthLCMKernelCompressionLedger"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-cold-core-threshold-function-table-router.json",
    "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
    "prime-matrix-strict-effective-cold-history-pruning-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
    "prime-matrix-strict-unified-terminal-budget-equation-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    "prime-matrix-wsh-fo-pdec-threshold-ledger.json",
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
        "experiments/prime_matrix_strict_same_parameter_core_threshold_summation_router.py": sha256(
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


def summation_formula_rows() -> list[dict[str, str]]:
    """列出求和优势的精确对象。"""
    return [
        {
            "name": "actual_cold_history_domain",
            "formula": "C_cold(h_0)={W: D(W)|h_0, H_W=h_0/D(W), W remains nonpersistent cold}",
            "status": "closed_domain_open_size",
            "meaning": "求和只能在实际存活冷历史族上做，不能对全部形式历史求和。",
        },
        {
            "name": "nonpersistent_supply_bound",
            "formula": "U_np <= sum_{W in C_cold(h_0)} (T_PDEC(W)-1) C_core(W)",
            "status": "imported_closed_bound",
            "meaning": "非持久冷供给上界已经闭合；当前缺的是右侧是否足够小。",
        },
        {
            "name": "length_envelope",
            "formula": "N_{H_W}(I_W) <= |I_W|",
            "status": "closed_pointwise_cap",
            "meaning": "点态长度 cap 可作上界组件，但不能控制历史数量或 T_PDEC 权重。",
        },
        {
            "name": "weighted_support_measure",
            "formula": "Sigma_core(h_0)=sum_{W in C_cold(h_0)} (T_PDEC(W)-1) C_core(W)",
            "status": "open_numeric_measure",
            "meaning": "这是本层必须生成的同参数加权支撑测度表。",
        },
        {
            "name": "dominance_target",
            "formula": "Sigma_core(h_0) < L_forced(P,z,D)-E_named",
            "status": "open_strict_dominance",
            "meaning": "若成立，则早期零行反例链的非持久冷供给不足，形成终端矛盾。",
        },
    ]


def obstruction_rows() -> list[dict[str, Any]]:
    """说明为什么点态 C_core cap 不能直接推出求和优势。"""
    return [
        {
            "model": "free_support_count",
            "assumption": "only C_core(W)<=1 and T_PDEC(W)-1<=1",
            "consequence": "sum_W(T_PDEC(W)-1)C_core(W)=#C_cold(h_0)",
            "obstruction": "若没有 #C_cold(h_0) 支撑界，右侧可任意大。",
            "needed_input": SUPPORT_TABLE,
        },
        {
            "model": "large_persistence_threshold",
            "assumption": "#C_cold(h_0) bounded but T_PDEC(W) unbounded",
            "consequence": "同一支撑可被持久阈值权重放大。",
            "obstruction": "必须用同一参数账本固定 T_PDEC，不能事后调参。",
            "needed_input": PDEC_TABLE,
        },
        {
            "model": "weak_forced_load",
            "assumption": "cold supply bounded but L_forced lower bound missing",
            "consequence": "无法推出 L_forced>U_np。",
            "obstruction": "反例链需求端必须给出同参数强制负载下界。",
            "needed_input": LOAD_LOWER,
        },
    ]


def failure_matrix_rows() -> list[dict[str, str]]:
    """把求和优势失败的源头接回统一矛盾场。"""
    return [
        {
            "failure": "too many cold histories under one prefix",
            "rigidity_route": "same-prefix LCM anchor and incremental multiplier split",
            "named_exit": f"{PREFIX_BRANCHING} / {KERNEL_BUDGET} / {LOW_KERNEL}",
        },
        {
            "failure": "collar or short-window support expands too much",
            "rigidity_route": "sibling collar width LCM compression",
            "named_exit": f"{WIDTH_LCM} / {HOT_CORE} / {FIXED_HISTORY}",
        },
        {
            "failure": "terminal cold windows stay crowded without becoming hot",
            "rigidity_route": "cold-hot split plus terminal anti-cascade",
            "named_exit": f"{COLD_ANTICASCADE} / {HOT_CORE}",
        },
        {
            "failure": "same history repeats beyond nonpersistent allowance",
            "rigidity_route": "multiplicity threshold converts persistence into named return",
            "named_exit": f"{PDEC_TABLE} / {FIXED_HISTORY}",
        },
        {
            "failure": "supply is bounded but still not below demand",
            "rigidity_route": "unified terminal budget gap",
            "named_exit": LOAD_LOWER,
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CoreSummationTargetImported",
            result["core_summation_target_imported"],
            result["core_summation_target_imported"],
            "上一层已把 C_core 定义表后的主攻点指向同参数求和优势。",
            CORE_SUM,
        ),
        row(
            "SameParameterColdSupplyFormulaImported",
            result["same_parameter_cold_supply_formula_imported"],
            result["same_parameter_cold_supply_formula_imported"],
            "非持久冷供给公式和同参数账本已从回流后数值包继承。",
            CORE_SUM,
        ),
        row(
            "ActualColdHistoryDomainImported",
            result["actual_cold_history_domain_imported"],
            result["actual_cold_history_domain_imported"],
            "有效剪枝接口给出实际冷历史族 C_cold(h_0)，并禁止对全部形式历史求和。",
            SUPPORT_TABLE,
        ),
        row(
            "PointwiseCapNotEnoughCertified",
            result["pointwise_cap_not_enough_certified"],
            result["pointwise_cap_not_enough_certified"],
            "仅有 C_core 点态 cap 无法控制历史支撑数、T_PDEC 权重和需求端负载。",
            f"{SUPPORT_TABLE} AND {PDEC_TABLE} AND {LOAD_LOWER}",
        ),
        row(
            "WeightedSupportReductionClosed",
            result["weighted_support_reduction_closed"],
            result["weighted_support_reduction_closed"],
            "求和优势被精确压成同参数加权支撑测度表加需求端严格比较。",
            f"{SUPPORT_TABLE} AND {FINITE_RUNNER} AND {LOAD_LOWER}",
        ),
        row(
            "SameParameterPDECThresholdNumericTableProved",
            False,
            False,
            "有限 FO-PDEC ledger 只是投影阈值账本，不是全局同参数 T_PDEC 表。",
            PDEC_TABLE,
        ),
        row(
            "CoreHistoryWeightedSupportMeasureTableProved",
            False,
            False,
            "尚未证明实际冷历史族的加权支撑测度足够小。",
            SUPPORT_TABLE,
        ),
        row(
            "CoreThresholdSummationDominanceProved",
            False,
            False,
            "缺支撑测度、T_PDEC 表和需求端严格下界的闭合比较。",
            f"{SUPPORT_TABLE} AND {PDEC_TABLE} AND {LOAD_LOWER}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{SUPPORT_TABLE} AND {PDEC_TABLE} AND {LOAD_LOWER} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同参数核心阈值求和优势证书。"""
    core = load_json("prime-matrix-strict-cold-core-threshold-function-table-router.json")
    cold = load_json("prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json")
    pruning = load_json("prime-matrix-strict-effective-cold-history-pruning-router.json")
    prefix = load_json("prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    budget = load_json("prime-matrix-strict-cold-core-threshold-budget-gap-router.json")
    unified = load_json("prime-matrix-strict-unified-terminal-budget-equation-router.json")
    anticollapse = load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    pdec_ledger = load_json("prime-matrix-wsh-fo-pdec-threshold-ledger.json")

    target = core.get("next_direct_attack_target") == CORE_SUM
    formula = cold.get("effective_pruning_closed_for_nonpersistent_budget") is True
    actual_domain = (
        pruning.get("effective_pruning_interface_closed") is True
        and pruning.get("divisor_compatibility_interface_closed") is True
    )
    prefix_routes = prefix.get("prefix_branching_structural_dichotomy_closed") is True
    budget_criterion = budget.get("cold_budget_contradiction_criterion_closed") is True
    unified_equation = unified.get("algebraic_composition_closed") is True
    no_silent_collapse = (
        anticollapse.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget") is True
    )
    finite_pdec_only = pdec_ledger.get("status") == "finite_fo_pdec_fourier_threshold_ledger_not_global_proof"
    pointwise_obstruction = (
        core.get("cold_core_function_table_schema_closed") is True
        and core.get("trivial_interval_length_cap_closed") is True
    )
    support_reduction = all(
        [
            target,
            formula,
            actual_domain,
            prefix_routes,
            budget_criterion,
            unified_equation,
            no_silent_collapse,
            pointwise_obstruction,
        ]
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_same_parameter_core_threshold_summation_router",
        "status": "core_threshold_summation_reduced_to_weighted_support_measure_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "core_summation_target_imported": target,
        "same_parameter_cold_supply_formula_imported": formula,
        "actual_cold_history_domain_imported": actual_domain,
        "prefix_branching_routes_imported": prefix_routes,
        "cold_budget_contradiction_criterion_imported": budget_criterion,
        "unified_terminal_budget_equation_imported": unified_equation,
        "prefix_label_anticollapse_imported": no_silent_collapse,
        "finite_fo_pdec_ledger_is_not_global_table": finite_pdec_only,
        "pointwise_cap_not_enough_certified": pointwise_obstruction,
        "weighted_support_reduction_closed": support_reduction,
        "core_history_weighted_support_measure_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "sparse_terminal_forced_load_lower_bound_proved": False,
        "finite_cold_history_summation_runner_or_analytic_envelope_proved": False,
        "core_threshold_summation_dominance_proved": False,
        "cold_core_threshold_numeric_table_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": CORE_SUM,
        "hardpoint_after_router": f"{SUPPORT_TABLE} AND {PDEC_TABLE} AND {LOAD_LOWER}",
        "next_direct_attack_target": SUPPORT_TABLE,
        "parallel_attack_targets": [
            PDEC_TABLE,
            LOAD_LOWER,
            FINITE_RUNNER,
            PREFIX_BRANCHING,
            COLD_ANTICASCADE,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "summation_formula_rows": summation_formula_rows(),
        "obstruction_rows": obstruction_rows(),
        "failure_matrix_rows": failure_matrix_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SameParameterCoreThresholdSummationDominanceTable` 不能由上一层的点态 `C_core` 定义表直接闭合。"
            "本步把它压成严格的同参数三原子：第一，实际冷历史族的加权支撑测度 "
            "`CoreHistoryWeightedSupportMeasureTable`；第二，同一账本下的 `SameParameterPDECThresholdNumericTable`；"
            "第三，需求端 `SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`。"
            "点态长度 cap 只能控制单个窗口，不能控制冷历史数量、持久阈值权重或需求端下界；"
            "若求和优势失败，失败源必须回流到前缀分叉/LCM 共同核、终端热核心、固定历史/PDEC 或统一终端预算缺口。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 同参数核心阈值求和优势路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"core_summation_target_imported={fmt_bool(result['core_summation_target_imported'])}",
        f"same_parameter_cold_supply_formula_imported={fmt_bool(result['same_parameter_cold_supply_formula_imported'])}",
        f"actual_cold_history_domain_imported={fmt_bool(result['actual_cold_history_domain_imported'])}",
        f"pointwise_cap_not_enough_certified={fmt_bool(result['pointwise_cap_not_enough_certified'])}",
        f"weighted_support_reduction_closed={fmt_bool(result['weighted_support_reduction_closed'])}",
        f"core_history_weighted_support_measure_table_proved={fmt_bool(result['core_history_weighted_support_measure_table_proved'])}",
        f"same_parameter_pdec_threshold_numeric_table_proved={fmt_bool(result['same_parameter_pdec_threshold_numeric_table_proved'])}",
        f"sparse_terminal_forced_load_lower_bound_proved={fmt_bool(result['sparse_terminal_forced_load_lower_bound_proved'])}",
        f"core_threshold_summation_dominance_proved={fmt_bool(result['core_threshold_summation_dominance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 求和对象",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["summation_formula_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['name'])}`",
                    table_cell(item["formula"]),
                    f"`{table_cell(item['status'])}`",
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 点态 cap 的不足",
            "",
            "| model | assumption | consequence | obstruction | needed input |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["obstruction_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['model'])}`",
                    table_cell(item["assumption"]),
                    table_cell(item["consequence"]),
                    table_cell(item["obstruction"]),
                    table_cell(item["needed_input"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 失败源回流矩阵",
            "",
            "| failure | rigidity route | named exit |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["failure_matrix_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(item["failure"]),
                    table_cell(item["rigidity_route"]),
                    table_cell(item["named_exit"]),
                ]
            )
            + " |"
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
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行：`{PDEC_TABLE}`、`{LOAD_LOWER}`、`{FINITE_RUNNER}`。",
            "- 边界：本步关闭的是求和优势的结构化降解与失败源登记，不提交最终数值反超。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """入口函数。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"weighted_support_reduction_closed={fmt_bool(result['weighted_support_reduction_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
