#!/usr/bin/env python3
"""生成 strict 正余量在 finite-prefix 与命名终端同步后的前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_positive_margin_after_finite_prefix_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json
  docs/monograph/prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.md"

POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
BETA_APPENDIX = (
    "BetaSieveLowerWeightRecursiveConstructionLedger AND "
    "BetaSieveLowerBoundDominanceProof AND "
    "BetaSieveMainCoefficientExplicit99PercentPGe100000"
)

SOURCE_FILES = [
    "prime-matrix-strict-named-return-terminal-saturation-sync-router.json",
    "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json",
    "prime-matrix-strict-unified-budget-after-named-sync-router.json",
    "prime-matrix-strict-forced-load-latest-frontier-sync-router.json",
    "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json",
    "prime-matrix-strict-same-parameter-prefix-window-spec-router.json",
    "prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json",
    "prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json",
    "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json",
    "prime-matrix-strict-formal-unit-type-threshold-sync-router.json",
    "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
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
        "experiments/prime_matrix_strict_positive_margin_after_finite_prefix_terminal_sync_router.py": sha256(
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


def imported_flags(data: dict[str, dict[str, Any]]) -> dict[str, bool]:
    """读取正余量同步所需的上游闭合状态。"""
    finite_tail = data["finite_tail"]
    range_manifest = data["range_manifest"]
    same_window = data["same_window"]
    runner = data["runner"]
    analytic_tail = data["analytic_tail"]
    type_sync = data["type_sync"]
    rowfree = data["rowfree"]
    named_terminal = data["named_terminal"]
    unified = data["unified"]
    terminal_budget = data["terminal_budget"]
    forced = data["forced"]

    finite_contract_closed = (
        finite_tail.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True
        and range_manifest.get("range_and_parameter_manifest_closed") is True
        and same_window.get("same_parameter_window_specification_proved") is True
        and runner.get("reproducible_prefix_rough_count_runner_hash_ledger_proved") is True
        and analytic_tail.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True
    )
    return {
        "positive_margin_active": terminal_budget.get("next_direct_attack_target") == POSITIVE_MARGIN,
        "forced_load_frontier_synced": forced.get("b3_analytic_budget_latest_synced") is True,
        "finite_prefix_available_under_current_contract": finite_contract_closed,
        "finite_prefix_strict_first_principles_lower_sieve_closed": finite_tail.get(
            "finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed"
        )
        is True,
        "formal_type_reduced_to_rowfree": type_sync.get("formal_unit_type_threshold_reduction_closed") is True,
        "rowfree_budget_anticollapse_closed": rowfree.get(
            "prefix_label_support_to_row_free_type_anticollapse_closed_for_budget"
        )
        is True,
        "named_terminal_saturation_imported": named_terminal.get(
            "named_return_terminal_saturation_sync_closed"
        )
        is True,
        "unified_budget_after_named_synced": unified.get("unified_budget_latest_sync_closed") is True,
        "nonpersistent_budget_open": unified.get(
            "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved"
        )
        is False,
        "persistent_terminal_open": (
            named_terminal.get("persistent_named_return_excluded_by_nonrecursive_breaker") is False
            and unified.get("persistent_terminal_family_excluded") is False
        ),
    }


def frontier_rows() -> list[dict[str, str]]:
    """列出同步后的正余量分解。"""
    return [
        {
            "component": "D_prefix finite-prefix demand",
            "latest_status": "available_under_current_standard_external_contract",
            "role": "给正余量左端提供同参数需求项。",
            "remaining": BETA_APPENDIX,
        },
        {
            "component": "row-free/type projection",
            "latest_status": "budget_anticollapse_closed",
            "role": "防止 prefix 标签质量在预算投影中静默消失。",
            "remaining": "strict strong injection not needed; named-return exits remain.",
        },
        {
            "component": "nonpersistent named returns",
            "latest_status": "open",
            "role": "必须由稀疏历史需求反超非持久冷供给来吸收。",
            "remaining": SPARSE_BUDGET,
        },
        {
            "component": "persistent named returns",
            "latest_status": "open",
            "role": "必须排斥 actual noncanonical moving atom / acyclic 终端族。",
            "remaining": f"{MOVING_ATOM} OR {NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA}",
        },
        {
            "component": "finite promotion",
            "latest_status": "independent_gate_open",
            "role": "DStructure/Rankin 仍是独立验收门。",
            "remaining": DSTRUCTURE,
        },
    ]


def build_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    current_sync_closed = (
        flags["positive_margin_active"]
        and flags["forced_load_frontier_synced"]
        and flags["finite_prefix_available_under_current_contract"]
        and flags["formal_type_reduced_to_rowfree"]
        and flags["rowfree_budget_anticollapse_closed"]
        and flags["named_terminal_saturation_imported"]
        and flags["unified_budget_after_named_synced"]
    )
    return [
        row(
            "PositiveMarginTargetImported",
            flags["positive_margin_active"],
            False,
            "最新终端预算前沿仍把主目标固定为同参数正余量。",
            POSITIVE_MARGIN,
        ),
        row(
            "ForcedLoadAndB3FrontierSynchronized",
            flags["forced_load_frontier_synced"],
            flags["forced_load_frontier_synced"],
            "强制负载守恒、稀疏历史预算抗塌缩与 B3 解析预算已经同步，不再把旧 B3-TV 当活动最窄点。",
            "finite prefix / named terminal frontier",
        ),
        row(
            "FinitePrefixDemandAvailableUnderCurrentContract",
            flags["finite_prefix_available_under_current_contract"],
            False,
            "range manifest、同参数窗口、runner/hash、解析尾桥和 Mertens 尾段已接成当前 standard/external D0 合同。",
            "closed under current contract" if flags["finite_prefix_available_under_current_contract"] else FINITE_PREFIX,
        ),
        row(
            "FirstPrinciplesBetaSieveAppendixStillOpen",
            flags["finite_prefix_strict_first_principles_lower_sieve_closed"],
            False,
            "若要求 lower-sieve 基本引理全部从零内联，仍需 beta-sieve 三项附录；该强化不阻塞当前合同路线。",
            "closed" if flags["finite_prefix_strict_first_principles_lower_sieve_closed"] else BETA_APPENDIX,
        ),
        row(
            "FormalTypeReducedAndRowFreeBudgetClosed",
            flags["formal_type_reduced_to_rowfree"] and flags["rowfree_budget_anticollapse_closed"],
            False,
            "formal-unit 类型阈值已压成 row-free 抗塌缩；预算所需版本已闭合，剩余并入命名回流。",
            "named returns and terminal atoms",
        ),
        row(
            "NamedReturnTerminalSaturationImported",
            flags["named_terminal_saturation_imported"],
            flags["named_terminal_saturation_imported"],
            "命名回流已同步到非持久正余量通道与持久 acyclic 终端通道。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "UnifiedBudgetAfterNamedImported",
            flags["unified_budget_after_named_synced"],
            flags["unified_budget_after_named_synced"],
            "统一预算已压到非持久稀疏预算与持久 moving atom 两条真实输入。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "NonpersistentSparseBudgetStillOpen",
            False,
            False,
            "还没有证明稀疏历史需求严格反超非持久冷供给。",
            SPARSE_BUDGET,
        ),
        row(
            "PersistentTerminalFamilyStillOpen",
            False,
            False,
            "还没有排斥 actual noncanonical moving atom 或等价的 acyclic 终端破环包。",
            f"{MOVING_ATOM} OR {NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA}",
        ),
        row(
            "PositiveMarginAfterFinitePrefixTerminalSyncClosed",
            current_sync_closed,
            current_sync_closed,
            "正余量的当前前沿已完成同步：旧 finite-prefix/B3/type 粗阻塞不再是活动最窄点。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
        row(
            "ExplicitPositiveTerminalBudgetMarginProved",
            False,
            False,
            "非持久预算反超、持久终端排斥和 DStructure 尚未同时完成。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链与真实结构链之间的无条件终端矛盾。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造正余量最新同步证书。"""
    data = {
        "named_terminal": load_json("prime-matrix-strict-named-return-terminal-saturation-sync-router.json"),
        "positive": load_json("prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json"),
        "unified": load_json("prime-matrix-strict-unified-budget-after-named-sync-router.json"),
        "forced": load_json("prime-matrix-strict-forced-load-latest-frontier-sync-router.json"),
        "range_manifest": load_json("prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json"),
        "same_window": load_json("prime-matrix-strict-same-parameter-prefix-window-spec-router.json"),
        "runner": load_json("prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json"),
        "analytic_tail": load_json("prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json"),
        "finite_tail": load_json("prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json"),
        "type_sync": load_json("prime-matrix-strict-formal-unit-type-threshold-sync-router.json"),
        "rowfree": load_json("prime-matrix-strict-row-free-type-anticollapse-sync-router.json"),
        "terminal_budget": load_json("prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"),
    }
    flags = imported_flags(data)
    rows = build_rows(flags)
    sync_closed = any(
        item["gate"] == "PositiveMarginAfterFinitePrefixTerminalSyncClosed" and item["proved"]
        for item in rows
    )

    return {
        "certificate_type": "prime_matrix_strict_positive_margin_after_finite_prefix_terminal_sync_router",
        "status": "positive_margin_frontier_synced_to_sparse_budget_and_moving_atom_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "positive_margin_after_finite_prefix_terminal_sync_closed": sync_closed,
        "finite_prefix_available_under_current_contract": flags["finite_prefix_available_under_current_contract"],
        "finite_prefix_strict_first_principles_lower_sieve_closed": flags[
            "finite_prefix_strict_first_principles_lower_sieve_closed"
        ],
        "rowfree_budget_anticollapse_closed": flags["rowfree_budget_anticollapse_closed"],
        "named_return_terminal_saturation_imported": flags["named_terminal_saturation_imported"],
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "explicit_positive_terminal_budget_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": POSITIVE_MARGIN,
        "hardpoint_after_router": f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        "next_direct_attack_target": SPARSE_BUDGET,
        "parallel_attack_targets": [
            MOVING_ATOM,
            NONRECURSIVE_BREAKER,
            SCOPE_MATCH,
            JOINT_FORMULA,
            HOT_CORE,
            FIXED_HISTORY,
            DSTRUCTURE,
            BETA_APPENDIX,
        ],
        "frontier_rows": frontier_rows(),
        "imported_flags": flags,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ExplicitPositiveTerminalBudgetMarginInequality` 的最新前沿已同步：finite-prefix D0 在当前 "
            "standard/external 合同下由 range manifest、同参数窗口、runner/hash、解析尾桥和 Mertens 同步支撑；"
            "formal-unit 类型阈值已压到 row-free 抗塌缩且预算版已闭合；命名回流已同步到非持久预算与持久终端通道。"
            "因此当前真正最窄主攻点不再是 B3-TV、runner 或类型阈值，而是 "
            "`SparseHistoryDemandExceedsNonpersistentSupplyBudget`；并行保留 actual noncanonical moving atom、"
            "热/固定历史、DStructure/Rankin 与严格第一性 beta-sieve 附录。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 正余量 finite-prefix/命名终端同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"positive_margin_after_finite_prefix_terminal_sync_closed={fmt_bool(result['positive_margin_after_finite_prefix_terminal_sync_closed'])}",
        f"finite_prefix_available_under_current_contract={fmt_bool(result['finite_prefix_available_under_current_contract'])}",
        f"finite_prefix_strict_first_principles_lower_sieve_closed={fmt_bool(result['finite_prefix_strict_first_principles_lower_sieve_closed'])}",
        f"rowfree_budget_anticollapse_closed={fmt_bool(result['rowfree_budget_anticollapse_closed'])}",
        f"named_return_terminal_saturation_imported={fmt_bool(result['named_return_terminal_saturation_imported'])}",
        f"sparse_history_demand_exceeds_nonpersistent_supply_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_nonpersistent_supply_budget_proved'])}",
        f"persistent_terminal_family_excluded={fmt_bool(result['persistent_terminal_family_excluded'])}",
        f"explicit_positive_terminal_budget_margin_proved={fmt_bool(result['explicit_positive_terminal_budget_margin_proved'])}",
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
        "| component | latest_status | role | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["frontier_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['component'])}`",
                    f"`{table_cell(item['latest_status'])}`",
                    table_cell(item["role"]),
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
        "positive_margin_after_finite_prefix_terminal_sync_closed="
        f"{fmt_bool(result['positive_margin_after_finite_prefix_terminal_sync_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(
        "explicit_positive_terminal_budget_margin_proved="
        f"{fmt_bool(result['explicit_positive_terminal_budget_margin_proved'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
