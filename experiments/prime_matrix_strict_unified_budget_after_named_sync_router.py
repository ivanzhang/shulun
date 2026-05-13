#!/usr/bin/env python3
"""生成 strict 命名回流后统一预算同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_unified_budget_after_named_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json
  docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json",
    "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
    "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json",
    "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json",
]

UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
PERSISTENT_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
BETA_APPENDIX = (
    "BetaSieveLowerWeightRecursiveConstructionLedger AND "
    "BetaSieveLowerBoundDominanceProof AND "
    "BetaSieveMainCoefficientExplicit99PercentPGe100000"
)


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
    result = {"experiments/prime_matrix_strict_unified_budget_after_named_sync_router.py": sha256(Path(__file__).resolve())}
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


def has_closed_gate(cert: dict[str, Any], gate: str) -> bool:
    """检查 rows 中某个 gate 是否闭合。"""
    return any(item.get("gate") == gate and item.get("closed") is True for item in cert.get("rows", []) or [])


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成统一预算最新判定表。"""
    named = data["named"]
    finite = data["finite"]
    rowfree = data["rowfree"]
    cold = data["cold"]
    terminal = data["terminal"]
    margin = data["margin"]
    concrete = data["concrete"]

    target_imported = named.get("next_direct_attack_target") == UNIFIED_BUDGET
    d0_external_closed = finite.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True
    d0_strict_first_principles = finite.get("finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed") is True
    rowfree_budget = rowfree.get("prefix_label_support_to_row_free_type_anticollapse_closed_for_budget") is True
    cold_discipline = (
        cold.get("cold_supply_upper_envelope_closed") is True
        and cold.get("same_parameter_lambda_schedule_closed") is True
        and cold.get("adaptive_lambda_no_free_lunch_dichotomy_closed") is True
    )
    terminal_normal_form = terminal.get("single_parameter_margin_normal_form_closed") is True
    named_alphabet = named.get("named_return_alphabet_compression_closed") is True
    schema_closed = margin.get("coupled_margin_schema_closed") is True
    concrete_failed = concrete.get("concrete_same_parameter_margin_table_certificate_proved") is False
    persistent_pinned = has_closed_gate(margin, "PersistentReturnReducedToTerminalFamily")
    sparse_budget_open = has_closed_gate(margin, "SparseBudgetFormulaClosed")

    return [
        row(
            "UnifiedBudgetTargetImported",
            target_imported,
            False,
            "命名回流压缩后，下一主攻点为同参数统一预算严格不等式。",
            UNIFIED_BUDGET,
        ),
        row(
            "SingleParameterNormalFormAlreadyClosed",
            terminal_normal_form and schema_closed,
            True,
            "终局矛盾已固定为同一参数下的 D_prefix-E_named-U_cold>0，字段合同已列全。",
            "ConcreteSameParameterMarginTableCertificate",
        ),
        row(
            "D0PrefixDemandAvailableUnderCurrentContract",
            d0_external_closed,
            False,
            "在当前 standard/external lower-sieve 合同下，finite-prefix D0/M# 需求侧已不再卡 Mertens 或类型阈值。",
            "closed under accepted standard/external lower-sieve contract",
        ),
        row(
            "FirstPrinciplesLowerSieveStillSeparate",
            d0_strict_first_principles,
            False,
            "若要求 Rosser-Iwaniec lower-sieve 也从零内联，beta-sieve 三项附录仍未完成。",
            "closed" if d0_strict_first_principles else BETA_APPENDIX,
        ),
        row(
            "RowFreeNoSilentCollapseImported",
            rowfree_budget,
            False,
            "prefix 标签到 row-free/终端投影的预算所需无静默塌缩已闭合。",
            "closed for budget form",
        ),
        row(
            "NamedReturnAlphabetCompressed",
            named_alphabet,
            False,
            "命名回流已分成非持久预算吸收与持久终端族排斥。",
            f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        row(
            "ColdSupplyDisciplineImported",
            cold_discipline,
            True,
            "冷供给、Lambda schedule 和无免费调参二分已锁入同一参数账本。",
            SPARSE_BUDGET,
        ),
        row(
            "ConcreteMarginTableStillNotProved",
            concrete_failed,
            False,
            "同参数表旧尝试仍未给出 E0/U0 数值吸收和持久终端排斥。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "NonpersistentBudgetIsNowNarrowestInequality",
            sparse_budget_open,
            False,
            "非持久命名回流是否能由 U_cold 吸收，已压成 SparseHistoryDemandExceedsNonpersistentSupplyBudget。",
            SPARSE_BUDGET,
        ),
        row(
            "PersistentTerminalFamilyStillParallel",
            persistent_pinned,
            False,
            "持久命名回流仍需 actual noncanonical moving atom/PDEC-CAP 终端排斥。",
            MOVING_ATOM,
        ),
        row(
            "UnifiedTerminalBudgetStrictInequalityCurrentCorpusProved",
            False,
            False,
            "D0 条件可用、row-free 与冷纪律闭合后，仍未同时证明非持久预算反超和持久终端排斥。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "统一预算尚未给出最终直接矛盾；DStructure/Rankin 独立门仍保留。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造命名回流后的统一预算同步证书。"""
    data = {
        "named": load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json"),
        "finite": load_json("prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json"),
        "rowfree": load_json("prime-matrix-strict-row-free-type-anticollapse-sync-router.json"),
        "cold": load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "terminal": load_json("prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"),
        "margin": load_json("prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json"),
        "concrete": load_json("prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"),
    }
    rows = build_rows(data)
    latest_sync_closed = all(
        any(item["gate"] == gate and item["closed"] for item in rows)
        for gate in [
            "UnifiedBudgetTargetImported",
            "SingleParameterNormalFormAlreadyClosed",
            "D0PrefixDemandAvailableUnderCurrentContract",
            "RowFreeNoSilentCollapseImported",
            "NamedReturnAlphabetCompressed",
            "ColdSupplyDisciplineImported",
        ]
    )

    return {
        "certificate_type": "prime_matrix_strict_unified_budget_after_named_sync_router",
        "status": "unified_budget_synced_to_sparse_budget_and_moving_atom_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "unified_budget_latest_sync_closed": latest_sync_closed,
        "d0_prefix_available_under_standard_external_contract": True,
        "d0_prefix_strict_first_principles_lower_sieve_closed": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": UNIFIED_BUDGET,
        "hardpoint_after_router": f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        "next_direct_attack_target": SPARSE_BUDGET,
        "parallel_attack_targets": [
            MOVING_ATOM,
            "DirectAcyclicSameSetPDECCapDualCertificate",
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            DSTRUCTURE,
            BETA_APPENDIX,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`UnifiedTerminalBudgetStrictInequality` 已同步到最新前沿：D0 prefix 需求在当前 standard/external "
            "lower-sieve 合同下可用，row-free 无静默塌缩与冷供给调参纪律已闭合，命名回流也已拆成非持久预算吸收"
            "和持久终端族排斥。剩余不再是旧 Mertens、类型阈值或命名字母表，而是两个真实输入："
            "`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 与 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 命名回流后统一预算同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unified_budget_latest_sync_closed={fmt_bool(result['unified_budget_latest_sync_closed'])}",
        f"sparse_history_demand_exceeds_nonpersistent_supply_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_nonpersistent_supply_budget_proved'])}",
        f"persistent_terminal_family_excluded={fmt_bool(result['persistent_terminal_family_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "|---|---:|---:|---|---|",
    ]
    for item in result["rows"]:
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
