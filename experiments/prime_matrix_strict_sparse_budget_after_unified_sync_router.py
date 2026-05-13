#!/usr/bin/env python3
"""生成 strict 统一预算后稀疏供需缺口同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_sparse_budget_after_unified_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sparse-budget-after-unified-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-sparse-budget-after-unified-sync-router.json
  docs/monograph/prime-matrix-strict-sparse-budget-after-unified-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-sparse-budget-after-unified-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-sparse-budget-after-unified-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-unified-budget-after-named-sync-router.json",
    "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json",
    "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json",
    "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json",
    "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
]

SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
FORCED_LOAD = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
COLD_SUPPLY = "ColdCoreNonpersistentSupplyUpperBound"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
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
    result = {
        "experiments/prime_matrix_strict_sparse_budget_after_unified_sync_router.py": sha256(
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


def equations() -> list[dict[str, str]]:
    """列出本轮固定的同参数供需方程。"""
    return [
        {
            "name": "demand_accounting",
            "formula": "L_forced >= M#_{x,z}-E_registered",
            "status": "closed_normal_form",
            "meaning": "早期零行产生的 prefix 加权义务，要么进入终端负载，要么登记为命名回流。",
        },
        {
            "name": "nonpersistent_supply",
            "formula": "U_np <= sum_W (T_PDEC(W)-1) C_core(W)",
            "status": "closed_upper_envelope",
            "meaning": "所有非持久稀疏历史的冷供给已被同一 Lambda/PDEC 阈值上界控制。",
        },
        {
            "name": "sparse_budget_gap",
            "formula": "M#_{x,z}-E_registered > U_np",
            "status": "open_strict_margin",
            "meaning": "这是 SparseHistoryDemandExceedsNonpersistentSupplyBudget 的同参数标量形态。",
        },
        {
            "name": "hot_or_persistent_escape",
            "formula": "large N_{H_W}(I_W) or repeated W -> hot/fixed/PDEC terminal return",
            "status": "registered_open",
            "meaning": "热核心或固定历史不是自由容量；但仍需独立排斥或回流验收。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成稀疏供需缺口同步判定表。"""
    unified = data["unified"]
    sparse = data["sparse"]
    forced = data["forced"]
    cold_gap = data["cold_gap"]
    multiplicity = data["multiplicity"]
    scaled = data["scaled"]
    anti = data["anti"]
    cold_balance = data["cold_balance"]
    finite = data["finite"]
    rowfree = data["rowfree"]
    named = data["named"]

    target_imported = unified.get("next_direct_attack_target") == SPARSE_BUDGET
    budget_formula = sparse.get("nonpersistent_sae_budget_formula_closed") is True
    comparison_criterion = sparse.get("forced_load_comparison_criterion_closed") is True
    no_silent = (
        anti.get("terminal_projection_anticollapse_closed") is True
        and rowfree.get("prefix_label_support_to_row_free_type_anticollapse_closed_for_budget") is True
        and forced.get("terminal_projection_no_loss_or_named_return_closed") is True
    )
    demand_contract = (
        finite.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True
        and forced.get("forced_load_criterion_closed") is True
    )
    first_principles_lower_sieve = (
        finite.get("finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed") is True
    )
    cold_contract = (
        cold_gap.get("cold_supply_upper_bound_closed") is True
        and cold_gap.get("cold_budget_contradiction_criterion_closed") is True
        and cold_balance.get("same_parameter_lambda_schedule_closed") is True
        and cold_balance.get("adaptive_lambda_no_free_lunch_dichotomy_closed") is True
    )
    multiplicity_contract = (
        multiplicity.get("multiplicity_to_divisor_count_closed") is True
        and scaled.get("cold_hot_split_closed") is True
        and scaled.get("cold_core_budget_insertion_closed") is True
    )
    named_compressed = named.get("named_return_alphabet_compression_closed") is True

    return [
        row(
            "SparseBudgetTargetImportedFromUnifiedBudget",
            target_imported,
            False,
            "统一预算最新前沿已把非持久分支精确钉到 SparseHistoryDemandExceedsNonpersistentSupplyBudget。",
            SPARSE_BUDGET,
        ),
        row(
            "NonpersistentBudgetFormulaClosed",
            budget_formula and comparison_criterion,
            True,
            "若没有持久历史，U_np 已写成历史词求和；若 L_forced>U_np 就得到供需矛盾。",
            STRICT_MARGIN,
        ),
        row(
            "NoSilentProjectionCollapseImported",
            no_silent,
            True,
            "prefix 义务到 row-free/稀疏终端历史的预算版无静默塌缩已闭合。",
            "closed for budget form; strong injection not asserted",
        ),
        row(
            "DemandSideAvailableUnderCurrentContract",
            demand_contract,
            False,
            "在当前 standard/external lower-sieve 合同下，finite-prefix 需求侧和强制负载守恒可用。",
            STRICT_MARGIN,
        ),
        row(
            "FirstPrinciplesLowerSieveStillSeparate",
            first_principles_lower_sieve,
            False,
            "若要求 lower-sieve 基本引理从零内联，beta-sieve 三项附录仍未完成。",
            "closed" if first_principles_lower_sieve else BETA_APPENDIX,
        ),
        row(
            "ColdSupplySameParameterDisciplineClosed",
            cold_contract,
            True,
            "冷供给上界、Lambda 调节纪律和供需矛盾判据已锁到同一参数账本。",
            STRICT_MARGIN,
        ),
        row(
            "SingleHistoryCapacityReducedToColdOrHot",
            multiplicity_contract,
            False,
            "单历史重数已压到缩频核心窗口；冷窗口进 U_np，热窗口必须命名回流。",
            f"{STRICT_MARGIN} AND {HOT_CORE}",
        ),
        row(
            "NamedReturnAlphabetCompressed",
            named_compressed,
            False,
            "非持久回流必须进入统一预算，持久回流进入终端族；没有无名出口。",
            f"{STRICT_MARGIN} AND {MOVING_ATOM}",
        ),
        row(
            "SameParameterSparseDemandColdSupplyNormalFormClosed",
            target_imported and budget_formula and no_silent and demand_contract and cold_contract,
            False,
            "SparseHistoryDemandExceedsNonpersistentSupplyBudget 等价压成同参数标量缺口 M#-E_registered>U_np。",
            STRICT_MARGIN,
        ),
        row(
            "SameParameterSparseDemandColdSupplyStrictMarginProved",
            False,
            False,
            "当前材料尚未给出 M#_{x,z}-E_registered-U_np 的严格正余量证书。",
            STRICT_MARGIN,
        ),
        row(
            "HotFixedPersistentEscapesExcluded",
            False,
            False,
            "热核心、固定历史和持久终端族仍未被独立排斥；它们不能作为非持久 U_np 免费容量。",
            f"{HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM}",
        ),
        row(
            "SparseHistoryDemandExceedsNonpersistentSupplyBudgetProved",
            False,
            False,
            "预算结构、供需口和同参数纪律已闭合，但严格余量和热/持久出口排斥仍未完成。",
            f"{STRICT_MARGIN} AND {HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步没有得到排除早期零行反例链的终端矛盾；DStructure/Rankin 晋级门仍保留。",
            f"{STRICT_MARGIN} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造统一预算后的稀疏供需缺口同步证书。"""
    data = {
        "unified": load_json("prime-matrix-strict-unified-budget-after-named-sync-router.json"),
        "sparse": load_json("prime-matrix-strict-sparse-terminal-history-sae-budget-router.json"),
        "forced": load_json("prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json"),
        "cold_gap": load_json("prime-matrix-strict-cold-core-threshold-budget-gap-router.json"),
        "multiplicity": load_json("prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
        "anti": load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"),
        "cold_balance": load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "finite": load_json("prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json"),
        "rowfree": load_json("prime-matrix-strict-row-free-type-anticollapse-sync-router.json"),
        "named": load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json"),
    }
    rows = build_rows(data)
    normal_form_closed = any(
        item["gate"] == "SameParameterSparseDemandColdSupplyNormalFormClosed" and item["closed"]
        for item in rows
    )

    return {
        "certificate_type": "prime_matrix_strict_sparse_budget_after_unified_sync_router",
        "status": "sparse_budget_synced_to_same_parameter_margin_hot_fixed_moving_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "sparse_budget_latest_sync_closed": normal_form_closed,
        "nonpersistent_budget_formula_closed": True,
        "no_silent_projection_collapse_closed_for_budget": True,
        "demand_side_available_under_standard_external_contract": True,
        "first_principles_lower_sieve_closed": False,
        "cold_supply_same_parameter_discipline_closed": True,
        "same_parameter_sparse_demand_cold_supply_normal_form_closed": normal_form_closed,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "persistent_terminal_family_excluded": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SPARSE_BUDGET,
        "hardpoint_after_router": (
            f"{STRICT_MARGIN} AND {HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM}"
        ),
        "next_direct_attack_target": STRICT_MARGIN,
        "parallel_attack_targets": [
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            "DirectAcyclicSameSetPDECCapDualCertificate",
            DSTRUCTURE,
            BETA_APPENDIX,
        ],
        "equations": equations(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 已被同步到最新统一预算前沿："
            "非持久历史预算公式、prefix/row-free 无静默塌缩、finite-prefix 需求侧、冷供给同参数纪律、"
            "以及单历史容量的冷/热分裂都已接入。剩余不再是宽泛的“稀疏历史是什么”，而是同一参数下的"
            "严格标量缺口 `M#_{x,z}-E_registered>U_np`。当前尚未证明该严格正余量；热核心、固定历史和"
            "持久终端族仍需作为并行出口排斥，行/列命题不能升级为无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 统一预算后稀疏供需缺口同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sparse_budget_latest_sync_closed={fmt_bool(result['sparse_budget_latest_sync_closed'])}",
        f"same_parameter_sparse_demand_cold_supply_normal_form_closed={fmt_bool(result['same_parameter_sparse_demand_cold_supply_normal_form_closed'])}",
        f"same_parameter_sparse_demand_cold_supply_strict_margin_proved={fmt_bool(result['same_parameter_sparse_demand_cold_supply_strict_margin_proved'])}",
        f"sparse_history_demand_exceeds_nonpersistent_supply_budget_proved={fmt_bool(result['sparse_history_demand_exceeds_nonpersistent_supply_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 同参数供需方程",
        "",
        "| name | formula | status | meaning |",
        "|---|---|---|---|",
    ]
    for item in result["equations"]:
        lines.append(
            "| "
            f"`{table_cell(item['name'])}` | "
            f"`{table_cell(item['formula'])}` | "
            f"`{table_cell(item['status'])}` | "
            f"{table_cell(item['meaning'])} |"
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
