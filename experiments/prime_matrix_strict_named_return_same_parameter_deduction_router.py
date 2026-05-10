#!/usr/bin/env python3
"""生成 strict 命名回流同参数扣除表路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_named_return_same_parameter_deduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-named-return-same-parameter-deduction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-named-return-same-parameter-deduction-router.json"
OUT_MD = DOCS / "prime-matrix-strict-named-return-same-parameter-deduction-router.md"

CONCRETE = DOCS / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"
FLOOR_CHARGE = DOCS / "prime-matrix-strict-rosser-floor-terminal-charge-router.json"
NAMED_COMPRESSION = DOCS / "prime-matrix-strict-named-return-exclusion-compression-router.json"
SPARSE_BUDGET = DOCS / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json"
COLD_BALANCE = DOCS / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"
TERMINAL_FAMILY = DOCS / "prime-matrix-strict-acyclic-terminal-family-attack-router.json"
COUPLED_LEDGER = DOCS / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json"

SOURCE_FILES = [
    CONCRETE,
    FLOOR_CHARGE,
    NAMED_COMPRESSION,
    SPARSE_BUDGET,
    COLD_BALANCE,
    TERMINAL_FAMILY,
    COUPLED_LEDGER,
]

NAMED_TABLE = "NamedReturnSameParameterDeductionTable"
STRICT_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
DIRECT_CLEAN = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
SAE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def component(
    name: str,
    same_parameter_rule: str,
    current_value: str,
    numeric_available: bool,
    remaining: str,
) -> dict[str, Any]:
    """构造 E_named 分量表行。"""
    return {
        "component": name,
        "same_parameter_rule": same_parameter_rule,
        "current_value": current_value,
        "numeric_available": numeric_available,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造命名回流同参数扣除表证书。"""
    concrete = load_json(CONCRETE)
    floor_charge = load_json(FLOOR_CHARGE)
    named = load_json(NAMED_COMPRESSION)
    sparse = load_json(SPARSE_BUDGET)
    cold = load_json(COLD_BALANCE)
    terminal = load_json(TERMINAL_FAMILY)
    coupled = load_json(COUPLED_LEDGER)

    guard = (
        floor_charge.get("counterexample_assumption_only") is True
        and floor_charge.get("empirical_absence_not_used") is True
        and floor_charge.get("row_column_unconditional_closed") is False
    )
    parameter_id = floor_charge.get("parameter_id") or concrete.get("candidate_parameter_row", {}).get("parameter_id")
    charge_imported = floor_charge.get("sawtooth_failure_no_free_d0_loss_closed") is True
    compression_imported = named.get("named_return_compression_closed") is True
    persistent_reduced = named.get("persistent_named_return_reduced_to_global_terminal") is True
    nonpersistent_reduced = named.get("nonpersistent_named_return_reduced_to_unified_budget") is True
    sparse_formula = sparse.get("nonpersistent_sae_budget_formula_closed") is True
    cold_discipline = cold.get("single_parameter_margin_ledger_closed") is True
    terminal_split = terminal.get("strict_acyclic_terminal_family_boundary_refined") is True

    # 中文注释：同参数扣除表的 schema 可闭合；数值 E0 仍需排斥持久终端并证明非持久预算反超。
    schema_closed = all(
        [
            guard,
            charge_imported,
            compression_imported,
            persistent_reduced,
            nonpersistent_reduced,
            sparse_formula,
            cold_discipline,
            terminal_split,
        ]
    )

    persistent_terminal_excluded = terminal.get("strict_terminal_family_proved") is True
    nonpersistent_budget_beaten = sparse.get("sparse_history_demand_exceeds_budget_proved") is True
    cold_numeric = concrete.get("u0_cold_supply_bound_available") is True
    e0_available = persistent_terminal_excluded and nonpersistent_budget_beaten
    direct = (
        e0_available
        and concrete.get("d0_prefix_lower_bound_available") is True
        and cold_numeric
        and concrete.get("dstructure_rankin_independently_accepted") is True
    )

    component_rows = [
        component(
            "E_persistent",
            "persistent PDEC/ColumnCRT/FixedHistory/HotCore must be excluded in the same terminal scope",
            "0 only after strict terminal family is proved; otherwise branch returns",
            persistent_terminal_excluded,
            f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}",
        ),
        component(
            "E_nonpersistent",
            "nonpersistent SAE/sparse/hot-core is not a separate E0 term after it is counted in U_cold",
            "absorbed by U_cold only after sparse budget gap is proved",
            nonpersistent_budget_beaten,
            f"{SAE_BUDGET} AND {COLD_NUMERIC}",
        ),
        component(
            "E_floor_charge",
            "sawtooth/near-square failure uses the same formal-unit terminal alphabet",
            "inherits E_persistent or E_nonpersistent according to persistence",
            False,
            f"{STRICT_TERMINAL} OR {SAE_BUDGET}",
        ),
        component(
            "E_finite_boundary",
            "finite prefix undecided is not an E0 deduction; it blocks D0 directly",
            "not counted in E_named",
            concrete.get("finite_boundary_prefix_certificate_proved") is True,
            FINITE_PREFIX,
        ),
    ]

    hardpoint_before = floor_charge.get("hardpoint_after_router", "")
    hardpoint_after = (
        f"{FINITE_PREFIX} AND "
        f"({STRICT_TERMINAL} OR {NAMED_TABLE}) AND "
        f"{COLD_NUMERIC} AND {SAE_BUDGET} AND {DSTRUCTURE}"
    )

    decision_rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "仍只在早期零行反例链内整理命名回流扣除，不使用真实缺席样本。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "TerminalChargeImported",
            charge_imported,
            True,
            "Rosser floor/sawtooth 失败态已被强制登记为命名终端收费。",
            NAMED_TABLE,
        ),
        row(
            "NamedReturnAlphabetCompressed",
            compression_imported,
            True,
            "命名回流字母表已压成持久全局终端与非持久统一预算二分。",
            f"{STRICT_TERMINAL} AND {SAE_BUDGET}",
        ),
        row(
            "SameParameterDeductionSchemaClosed",
            schema_closed,
            False,
            "同一 parameter_id 下的 E_named 只能由持久终端排斥和非持久预算吸收两类规则生成。",
            "schema closed; numeric fields open.",
        ),
        row(
            "PersistentNamedReturnNumericZero",
            persistent_terminal_excluded,
            persistent_terminal_excluded,
            "只有 strict 终端家族排斥后，持久命名回流才能在 E0 表中记为 0。",
            f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}",
        ),
        row(
            "NonpersistentNamedReturnAbsorbedByBudget",
            nonpersistent_budget_beaten,
            nonpersistent_budget_beaten,
            "只有非持久 SAE/cold budget 被证明反超，非持久回流才可由 U_cold 吸收。",
            f"{SAE_BUDGET} AND {COLD_NUMERIC}",
        ),
        row(
            "NamedReturnSameParameterDeductionTableProved",
            e0_available,
            e0_available,
            "同参数扣除表 schema 已闭合，但数值表仍未生成。",
            f"({CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}) AND {SAE_BUDGET}",
        ),
        row(
            "DirectTerminalContradictionReached",
            direct,
            direct,
            "仍未形成 D0-E0-U0>0 与 DStructure/Rankin 同时闭合的终端矛盾。",
            hardpoint_after,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_named_return_same_parameter_deduction_router",
        "status": "named_return_same_parameter_schema_closed_numeric_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parameter_id": parameter_id,
        "terminal_charge_imported": charge_imported,
        "named_return_compression_imported": compression_imported,
        "persistent_return_reduced_to_terminal_family": persistent_reduced,
        "nonpersistent_return_reduced_to_budget": nonpersistent_reduced,
        "sparse_budget_formula_imported": sparse_formula,
        "same_parameter_cold_discipline_imported": cold_discipline,
        "strict_terminal_family_split_imported": terminal_split,
        "named_return_same_parameter_schema_closed": schema_closed,
        "persistent_named_return_numeric_zero_available": persistent_terminal_excluded,
        "nonpersistent_named_return_absorbed_by_budget": nonpersistent_budget_beaten,
        "named_return_same_parameter_deduction_table_proved": e0_available,
        "e0_named_return_deduction_available": e0_available,
        "direct_unconditional_contradiction_found": direct,
        "row_column_unconditional_closed": direct,
        "hardpoint_before_router": hardpoint_before,
        "hardpoint_after_router": hardpoint_after,
        "next_direct_attack_target": DIRECT_PDEC,
        "parallel_attack_targets": [
            CANONICAL_LOCK,
            DIRECT_CLEAN,
            SAE_BUDGET,
            COLD_NUMERIC,
            FINITE_PREFIX,
            DSTRUCTURE,
        ],
        "component_rows": component_rows,
        "decision_rows": decision_rows,
        "source_hashes": source_hashes(),
        "coupled_status_snapshot": {
            "coupled_margin_schema_closed": coupled.get("coupled_margin_schema_closed"),
            "named_return_numeric_bound_present": coupled.get("named_return_numeric_bound_present"),
            "cold_supply_numeric_bound_present": coupled.get("cold_supply_numeric_bound_present"),
            "finite_boundary_hash_present": coupled.get("finite_boundary_hash_present"),
        },
        "plain_conclusion": (
            "`NamedReturnSameParameterDeductionTable` 已被直接展开。它不是一个可凭空填写的常数表；"
            "在同一 parameter_id 下，持久命名回流只有在 strict acyclic terminal family 被排斥后才能记为 0，"
            "非持久命名回流只有在 SparseHistoryDemandExceedsNonpersistentSupplyBudget 与冷供给同参数上界闭合后才可由 U_cold 吸收。"
            "因此本步关闭的是 E_named 的表结构和收费纪律，不是数值表。下一最窄数学主攻点转为同一坏窗集合上的 "
            "DirectAcyclicSameSetPDECCapDualCertificate；并行保留 canonical-lock、direct clean KLS、SAE budget、finite prefix 和 DStructure/Rankin。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 命名回流同参数扣除表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"parameter_id={result['parameter_id']}",
        f"named_return_same_parameter_schema_closed={fmt_bool(result['named_return_same_parameter_schema_closed'])}",
        (
            "persistent_named_return_numeric_zero_available="
            f"{fmt_bool(result['persistent_named_return_numeric_zero_available'])}"
        ),
        (
            "nonpersistent_named_return_absorbed_by_budget="
            f"{fmt_bool(result['nonpersistent_named_return_absorbed_by_budget'])}"
        ),
        (
            "named_return_same_parameter_deduction_table_proved="
            f"{fmt_bool(result['named_return_same_parameter_deduction_table_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. E_named 分量表",
        "",
        "| component | same_parameter_rule | current_value | numeric_available | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["component_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['component'])}`",
                    table_cell(item["same_parameter_rule"]),
                    table_cell(item["current_value"]),
                    f"`{fmt_bool(item['numeric_available'])}`",
                    table_cell(item["remaining"]),
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
            "## 3. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本文件只关闭同参数 E_named 的结构表；它没有证明持久终端排斥、非持久预算反超或行/列命题无条件闭合。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
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
