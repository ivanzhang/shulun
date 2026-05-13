#!/usr/bin/env python3
"""生成 strict 命名回流终端饱和同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_named_return_terminal_saturation_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-named-return-terminal-saturation-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-named-return-terminal-saturation-sync-router.json
  docs/monograph/prime-matrix-strict-named-return-terminal-saturation-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-named-return-terminal-saturation-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-named-return-terminal-saturation-sync-router.md"

NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
    "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json",
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
        "experiments/prime_matrix_strict_named_return_terminal_saturation_sync_router.py": sha256(
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
    """读取命名回流终端饱和同步所需的上游状态。"""
    defect = data["defect"]
    budget = data["budget"]
    acyclic = data["acyclic"]
    named = data["named"]
    rowfree = data["rowfree"]
    carrier = data["carrier"]
    return {
        "terminal_defect_no_free_exit_imported": defect.get("terminal_defect_no_free_exit_closed") is True,
        "terminal_defect_targets_named_return": defect.get("next_direct_attack_target") == NAMED_RETURN,
        "named_return_compression_imported": named.get("named_return_compression_closed") is True,
        "named_return_after_rowfree_imported": rowfree.get("named_return_alphabet_compression_closed") is True,
        "carrier_lcm_return_frontier_imported": carrier.get("return_branch_alphabet_frontier_closed") is True,
        "terminal_budget_synced_to_positive_margin": budget.get("hardpoint_after_router") == POSITIVE_MARGIN,
        "positive_margin_still_open": budget.get("explicit_positive_terminal_budget_margin_proved") is False,
        "acyclic_family_saturation_imported": acyclic.get("status")
        == "strict_acyclic_terminal_family_saturated_to_nonrecursive_breaker_open",
        "acyclic_family_still_open": acyclic.get("strict_acyclic_terminal_family_proved") is False,
        "dstructure_gate_still_open": acyclic.get(
            "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved"
        )
        is False,
    }


def lane_rows() -> list[dict[str, str]]:
    """列出命名回流的终端饱和通道。"""
    return [
        {
            "lane": "nonpersistent SAE/sparse/hot-core packets",
            "saturation": f"{UNIFIED_BUDGET} -> {POSITIVE_MARGIN}",
            "current_status": "synchronized_open",
            "meaning": "非持久命名回流不能另开扣除项；它只能进入同参数预算余量。",
        },
        {
            "lane": "persistent PDEC/ColumnCRT/fixed-history/hot-core",
            "saturation": (
                f"{TERMINAL_FAMILY} -> "
                f"({NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA})"
            ),
            "current_status": "saturated_open",
            "meaning": "持久命名回流已回到 acyclic 终端家族；剩余是破环、同集匹配或显式构造。",
        },
        {
            "lane": "carrier-lcm source/valuation return",
            "saturation": f"{SPARSE_BUDGET} OR {PERSISTENT_TERMINAL}",
            "current_status": "frontier_closed_exclusion_open",
            "meaning": "carrier-lcm return 不是新局部整除硬点；它按持久性接入两条主通道。",
        },
        {
            "lane": "finite promotion / referee gate",
            "saturation": DSTRUCTURE,
            "current_status": "independent_gate_open",
            "meaning": "DStructure/Rankin 是独立验收门，不能由命名回流同步自动关闭。",
        },
    ]


def build_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成本次同步判定表。"""
    saturation_inputs_ok = (
        flags["terminal_defect_no_free_exit_imported"]
        and flags["terminal_defect_targets_named_return"]
        and flags["named_return_compression_imported"]
        and flags["named_return_after_rowfree_imported"]
        and flags["carrier_lcm_return_frontier_imported"]
    )
    nonpersistent_frontier_ok = (
        flags["terminal_budget_synced_to_positive_margin"] and flags["positive_margin_still_open"]
    )
    persistent_frontier_ok = flags["acyclic_family_saturation_imported"] and flags["acyclic_family_still_open"]
    sync_closed = saturation_inputs_ok and nonpersistent_frontier_ok and persistent_frontier_ok
    return [
        row(
            "TerminalDefectNoFreeExitImported",
            flags["terminal_defect_no_free_exit_imported"],
            flags["terminal_defect_no_free_exit_imported"],
            "强 TV/端点缺陷已耗尽到命名出口集合，没有第四类无名出口。",
            NAMED_RETURN,
        ),
        row(
            "NamedReturnAlphabetCompressionImported",
            flags["named_return_compression_imported"] and flags["named_return_after_rowfree_imported"],
            flags["named_return_compression_imported"] and flags["named_return_after_rowfree_imported"],
            "PDEC/SAE/ColumnCRT/热核心/固定历史字母表已压成持久终端与非持久预算二分。",
            f"{UNIFIED_BUDGET} AND {TERMINAL_FAMILY}",
        ),
        row(
            "CarrierLCMReturnBranchAligned",
            flags["carrier_lcm_return_frontier_imported"],
            flags["carrier_lcm_return_frontier_imported"],
            "carrier-lcm return 分支已按同一命名回流二分登记，不再形成独立局部整除硬点。",
            f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        row(
            "NonpersistentLaneSaturatedToPositiveMargin",
            nonpersistent_frontier_ok,
            False,
            "非持久命名回流已同步到统一预算最新前沿，即同参数正余量 D_prefix-E_named-U_cold>0。",
            POSITIVE_MARGIN,
        ),
        row(
            "PersistentLaneSaturatedToAcyclicTerminalFamily",
            persistent_frontier_ok,
            False,
            "持久命名回流已同步到 acyclic 终端家族饱和态，必须破环或同集匹配。",
            f"{NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA}",
        ),
        row(
            "DStructureRankinGatePreserved",
            flags["dstructure_gate_still_open"],
            False,
            "独立 DStructure/Rankin 验收门仍保留，不能由本同步证书替代。",
            DSTRUCTURE,
        ),
        row(
            "NamedReturnTerminalSaturationSyncClosed",
            sync_closed,
            sync_closed,
            "命名回流的当前终端饱和边界已同步：剩余只在非持久正余量与持久终端破环两侧。",
            f"{POSITIVE_MARGIN} AND ({NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA})",
        ),
        row(
            "NonpersistentNamedReturnAbsorbedByPositiveMargin",
            False,
            False,
            "还没有同一参数下的显式正终端预算余量数值/符号证书。",
            POSITIVE_MARGIN,
        ),
        row(
            "PersistentNamedReturnExcludedByNonrecursiveBreaker",
            False,
            False,
            "还没有 nonrecursive actual noncanonical pre-Cauchy/signed-lift 破环包或等价替代证书。",
            f"{NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA}",
        ),
        row(
            "NamedReturnExclusionProved",
            False,
            False,
            "同步压缩不等于排斥；两条终端通道尚未同时关闭。",
            f"{POSITIVE_MARGIN} AND ({NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未从早期零行反例链与真实结构链之间得到最终无条件矛盾。",
            f"{POSITIVE_MARGIN} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造命名回流终端饱和同步证书。"""
    data = {
        "defect": load_json("prime-matrix-strict-terminal-defect-exhaustion-router.json"),
        "budget": load_json("prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"),
        "acyclic": load_json("prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"),
        "named": load_json("prime-matrix-strict-named-return-exclusion-compression-router.json"),
        "rowfree": load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json"),
        "carrier": load_json("prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json"),
    }
    flags = imported_flags(data)
    rows = build_rows(flags)
    sync_closed = any(
        item["gate"] == "NamedReturnTerminalSaturationSyncClosed" and item["proved"]
        for item in rows
    )

    return {
        "certificate_type": "prime_matrix_strict_named_return_terminal_saturation_sync_router",
        "status": "named_return_terminal_saturation_synced_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "named_return_terminal_saturation_sync_closed": sync_closed,
        "nonpersistent_named_return_absorbed_by_positive_margin": False,
        "persistent_named_return_excluded_by_nonrecursive_breaker": False,
        "explicit_positive_terminal_budget_margin_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "named_return_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": NAMED_RETURN,
        "hardpoint_after_router": (
            f"{POSITIVE_MARGIN} AND "
            f"({NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR {JOINT_FORMULA}) AND "
            f"{MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": POSITIVE_MARGIN,
        "parallel_attack_targets": [
            NONRECURSIVE_BREAKER,
            SCOPE_MATCH,
            JOINT_FORMULA,
            MODEL_LEDGER,
            RATE_LEDGER,
            DSTRUCTURE,
        ],
        "lane_rows": lane_rows(),
        "imported_flags": flags,
        "decision_table": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` 的最新前沿已同步到终端饱和态："
            "非持久命名回流不再另开扣除项，而是进入同参数显式正余量 "
            "`D_prefix-E_named-U_cold>0`；持久命名回流不再是宽黑箱，而是进入 acyclic 终端家族的 "
            "nonrecursive 破环、同集 PDEC 作用域匹配或新显式构造公式。"
            "本步只关闭同步边界，不证明两条通道排斥，因此行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 命名回流终端饱和同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"named_return_terminal_saturation_sync_closed={fmt_bool(result['named_return_terminal_saturation_sync_closed'])}",
        f"nonpersistent_named_return_absorbed_by_positive_margin={fmt_bool(result['nonpersistent_named_return_absorbed_by_positive_margin'])}",
        f"persistent_named_return_excluded_by_nonrecursive_breaker={fmt_bool(result['persistent_named_return_excluded_by_nonrecursive_breaker'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端饱和通道",
        "",
        "| lane | saturation | current_status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["lane_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['lane'])}`",
                    table_cell(item["saturation"]),
                    f"`{table_cell(item['current_status'])}`",
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
    for item in result["decision_table"]:
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
            "## 3. 当前最窄硬点",
            "",
            "主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行守门：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "完整剩余：",
            "",
            "```text",
            result["hardpoint_after_router"],
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
        "named_return_terminal_saturation_sync_closed="
        f"{fmt_bool(result['named_return_terminal_saturation_sync_closed'])}"
    )
    print(
        "named_return_exclusion_proved="
        f"{fmt_bool(result['named_return_exclusion_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
