#!/usr/bin/env python3
"""生成 finite-prefix / named-return 耦合正余量账本证书。

用法示例：
  python3 experiments/prime_matrix_strict_finite_prefix_named_return_coupled_margin_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-positive-terminal-budget-margin-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.json",
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
    MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json",
    MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json",
]

COUPLED = "FinitePrefixNamedReturnCoupledPositiveMarginLedger"
CONCRETE_TABLE = "ConcreteSameParameterMarginTableCertificate"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
PERSISTENT = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
NONPERSISTENT = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本路由依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def schema_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """列出耦合账本必须含有的字段。"""
    return [
        {
            "field": "parameter_id",
            "present": result["concrete_parameter_table_present"],
            "meaning": "同一组 z,D,Lambda,T_PDEC；禁止需求和供给分开调参。",
            "needed_for": "same-parameter discipline",
        },
        {
            "field": "D0_prefix_lower_bound",
            "present": result["prefix_numeric_lower_bound_present"],
            "meaning": "由 B3 外部前沿和有限 prefix 证书给出的 D_prefix 统一显式下界。",
            "needed_for": FINITE_PREFIX,
        },
        {
            "field": "E0_named_return_deduction",
            "present": result["named_return_numeric_bound_present"],
            "meaning": "命名回流扣除项；持久回流需进入 PDEC/CleanKLS，非持久回流进统一预算。",
            "needed_for": NAMED_RETURN,
        },
        {
            "field": "U0_cold_supply_bound",
            "present": result["cold_supply_numeric_bound_present"],
            "meaning": "非持久冷/稀疏历史供给的同参数显式上界。",
            "needed_for": NONPERSISTENT,
        },
        {
            "field": "margin_delta",
            "present": result["coupled_positive_margin_proved"],
            "meaning": "严格差值 D0-E0-U0>0，或失败时登记具体回流。",
            "needed_for": COUPLED,
        },
        {
            "field": "finite_boundary_hash",
            "present": result["finite_boundary_hash_present"],
            "meaning": "所有有限 P 边界的可复核证书 hash。",
            "needed_for": FINITE_PREFIX,
        },
    ]


def outcome_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """列出耦合账本的终端二分。"""
    return [
        {
            "case": "positive margin",
            "criterion": "D0(P,z)-E0(P,z)-U0(P,z)>0",
            "closed_as_logic": True,
            "proved_for_current_corpus": result["coupled_positive_margin_proved"],
            "consequence": "非持久冷/SAE 供给无法支付反例链义务，得到终端供需矛盾。",
        },
        {
            "case": "nonpositive margin with persistent return",
            "criterion": "E0_named contains persistent PDEC/ColumnCRT/FixedHistory/HotCore",
            "closed_as_logic": True,
            "proved_for_current_corpus": result["persistent_named_return_excluded"],
            "consequence": "必须回流到 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 或 DStructure/Rankin。",
        },
        {
            "case": "nonpositive margin with nonpersistent overload",
            "criterion": "U0_cold too large or sparse history supply absorbs demand",
            "closed_as_logic": True,
            "proved_for_current_corpus": result["sparse_history_demand_exceeds_budget_proved"],
            "consequence": "必须证明 SparseHistoryDemandExceedsNonpersistentSupplyBudget，或暴露 Lambda/阈值失败源。",
        },
        {
            "case": "finite boundary undecided",
            "criterion": "finite prefix certificate missing",
            "closed_as_logic": False,
            "proved_for_current_corpus": not result["finite_boundary_prefix_open"],
            "consequence": "不能把渐近 B3 余量推广成全局定理。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链内做终端供需比较，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "CoupledMarginSchemaClosed",
            "closed": True,
            "proved": True,
            "meaning": "最后正余量账本的必需字段已完全列出。",
            "remaining": CONCRETE_TABLE,
        },
        {
            "gate": "B3ExternalLaneImported",
            "closed": result["b3_external_lane_imported"],
            "proved": False,
            "meaning": "外部 B3/Mertens 版可供给 D0 的解析尾段。",
            "remaining": "finite boundary and same-parameter table",
        },
        {
            "gate": "ConcreteSameParameterTablePresent",
            "closed": result["concrete_parameter_table_present"],
            "proved": result["concrete_parameter_table_present"],
            "meaning": "当前还没有把 D0、E0、U0 写入同一可比较表。",
            "remaining": CONCRETE_TABLE,
        },
        {
            "gate": "FiniteBoundaryPrefixCertificatePresent",
            "closed": not result["finite_boundary_prefix_open"],
            "proved": not result["finite_boundary_prefix_open"],
            "meaning": "有限 P 边界仍未物化。",
            "remaining": FINITE_PREFIX,
        },
        {
            "gate": "NamedReturnNumericallyRegistered",
            "closed": result["named_return_numeric_bound_present"],
            "proved": result["named_return_numeric_bound_present"],
            "meaning": "E_named 仍没有同参数上界或排斥证书。",
            "remaining": f"{PERSISTENT} AND {NAMED_RETURN}",
        },
        {
            "gate": "ColdSupplyNumericDominanceRegistered",
            "closed": result["cold_supply_numeric_bound_present"] and result["sparse_history_demand_exceeds_budget_proved"],
            "proved": result["cold_supply_numeric_bound_present"] and result["sparse_history_demand_exceeds_budget_proved"],
            "meaning": "U_cold 有公式，但尚未和 D0-E0 做严格数值反超。",
            "remaining": NONPERSISTENT,
        },
        {
            "gate": "DirectTerminalContradictionReached",
            "closed": result["direct_unconditional_contradiction_found"],
            "proved": result["direct_unconditional_contradiction_found"],
            "meaning": "耦合账本尚未给出正余量或强制回流矛盾。",
            "remaining": f"{CONCRETE_TABLE} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造耦合正余量账本证书。"""
    positive = load_json(MONOGRAPH / "prime-matrix-strict-positive-terminal-budget-margin-attack-router.json")
    prefix = load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json")
    cold = load_json(MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.json")
    sparse = load_json(MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json")
    named = load_json(MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json")

    finite_prefix_open = prefix.get("finite_boundary_prefix_rough_count_certificate_proved") is not True
    b3_external_lane = positive.get("b3_external_front_no_longer_primary_blocker") is True
    persistent_excluded = named.get("persistent_named_return_excluded") is True
    nonpersistent_excluded = named.get("nonpersistent_named_return_excluded") is True
    sparse_demand_exceeds = sparse.get("sparse_history_demand_exceeds_budget_proved") is True
    cold_numeric_present = cold.get("cold_supply_upper_bound_closed") is True and cold.get("history_sum_envelope_closed") is True

    # 这些字段是正余量证明所需的具体数值表；当前证书只有公式和布尔状态，未给出同参数数值行。
    concrete_table_present = False
    prefix_numeric_present = prefix.get("uniform_prefix_rough_count_lower_bound_proved") is True and not finite_prefix_open
    named_numeric_present = named.get("named_return_exclusion_proved") is True
    finite_hash_present = False
    coupled_positive = (
        concrete_table_present
        and prefix_numeric_present
        and named_numeric_present
        and cold_numeric_present
        and sparse_demand_exceeds
        and persistent_excluded
        and nonpersistent_excluded
    )
    direct_contradiction = coupled_positive and positive.get("dstructure_rankin_independently_accepted") is True

    result = {
        "certificate_type": "prime_matrix_strict_finite_prefix_named_return_coupled_margin_ledger_router",
        "status": "coupled_margin_schema_closed_numeric_certificate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "b3_external_lane_imported": b3_external_lane,
        "coupled_margin_schema_closed": True,
        "concrete_parameter_table_present": concrete_table_present,
        "prefix_numeric_lower_bound_present": prefix_numeric_present,
        "finite_boundary_prefix_open": finite_prefix_open,
        "finite_boundary_hash_present": finite_hash_present,
        "named_return_numeric_bound_present": named_numeric_present,
        "persistent_named_return_excluded": persistent_excluded,
        "nonpersistent_named_return_excluded": nonpersistent_excluded,
        "cold_supply_numeric_bound_present": cold_numeric_present,
        "sparse_history_demand_exceeds_budget_proved": sparse_demand_exceeds,
        "hot_core_excluded": cold.get("terminal_core_hot_divisor_window_excluded") is True,
        "fixed_history_pdec_excluded": cold.get("fixed_type_history_pdec_excluded") is True,
        "coupled_positive_margin_proved": coupled_positive,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": direct_contradiction,
        "hardpoint_before_router": COUPLED,
        "hardpoint_after_router": (
            f"{CONCRETE_TABLE} AND {FINITE_PREFIX} AND {NAMED_RETURN} AND {NONPERSISTENT} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": CONCRETE_TABLE,
        "parallel_attack_targets": [
            FINITE_PREFIX,
            NAMED_RETURN,
            PERSISTENT,
            NONPERSISTENT,
            HOT_CORE,
            FIXED_HISTORY,
            DSTRUCTURE,
        ],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`FinitePrefixNamedReturnCoupledPositiveMarginLedger` 的逻辑形态已闭合：最后只需要同一参数表中"
            "的 D0、E0、U0 三项和严格差值。现有材料只有代数公式、外部 B3 条件前沿、冷供给上界公式和命名回流"
            "压缩二分；尚没有 concrete same-parameter margin table，也没有有限 prefix hash、E_named 同参数扣除表、"
            "或 SparseHistoryDemandExceedsNonpersistentSupplyBudget 的数值反超。因此当前仍不能推出终端直接矛盾。"
        ),
    }
    result["schema_rows"] = schema_rows(result)
    result["outcome_rows"] = outcome_rows(result)
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict finite-prefix / named-return 耦合正余量账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"b3_external_lane_imported={fmt_bool(result['b3_external_lane_imported'])}",
        f"coupled_margin_schema_closed={fmt_bool(result['coupled_margin_schema_closed'])}",
        f"concrete_parameter_table_present={fmt_bool(result['concrete_parameter_table_present'])}",
        f"prefix_numeric_lower_bound_present={fmt_bool(result['prefix_numeric_lower_bound_present'])}",
        f"finite_boundary_prefix_open={fmt_bool(result['finite_boundary_prefix_open'])}",
        f"finite_boundary_hash_present={fmt_bool(result['finite_boundary_hash_present'])}",
        f"named_return_numeric_bound_present={fmt_bool(result['named_return_numeric_bound_present'])}",
        f"cold_supply_numeric_bound_present={fmt_bool(result['cold_supply_numeric_bound_present'])}",
        f"sparse_history_demand_exceeds_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_budget_proved'])}",
        f"persistent_named_return_excluded={fmt_bool(result['persistent_named_return_excluded'])}",
        f"nonpersistent_named_return_excluded={fmt_bool(result['nonpersistent_named_return_excluded'])}",
        f"coupled_positive_margin_proved={fmt_bool(result['coupled_positive_margin_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 必需字段",
        "",
        "| field | present | meaning | needed_for |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["schema_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['field'])}`",
                    f"`{fmt_bool(row['present'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["needed_for"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 终端二分",
            "",
            "| case | criterion | closed_as_logic | proved_for_current_corpus | consequence |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["outcome_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['case'])}`",
                    table_cell(row["criterion"]),
                    f"`{fmt_bool(row['closed_as_logic'])}`",
                    f"`{fmt_bool(row['proved_for_current_corpus'])}`",
                    table_cell(row["consequence"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一最窄点",
            "",
            "```text",
            result["hardpoint_after_router"],
            "```",
            "",
            "下一步应直接生成 `ConcreteSameParameterMarginTableCertificate`：同一 `parameter_id` 下列出 `D0_prefix_lower_bound`、"
            "`E0_named_return_deduction`、`U0_cold_supply_bound`、`margin_delta` 和 `finite_boundary_hash`。若 `margin_delta>0`，"
            "进入终端供需矛盾；若不为正，失败行必须登记为持久 PDEC/CleanKLS、非持久 SAE 超供给、热核心或固定历史 PDEC。",
            "",
            "审稿边界：本文件闭合耦合账本 schema，不闭合数值正余量。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
