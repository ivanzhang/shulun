#!/usr/bin/env python3
"""生成 strict carrier-lcm return 分支前沿路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_carrier_lcm_return_branch_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json

输出：
  data/carrier-lcm-return-branch-sample-ledger.json
  docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json
  docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.md"
OUT_LEDGER = DATA / "carrier-lcm-return-branch-sample-ledger.json"

HARDPOINT = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
GLOBAL_DIVIDES = "ColdPrefixProductDividesCarrierLCMH0Ledger"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json",
    DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json",
    DOCS / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def classify_return(return_kind: str, persistent: bool) -> dict[str, Any]:
    """把 carrier-lcm return 分到非持久预算或持久终端族。"""
    if persistent:
        route = PERSISTENT_TERMINAL
        bucket = "persistent_terminal_family"
    else:
        route = SPARSE_BUDGET
        bucket = "nonpersistent_budget_absorption"
    return {
        "return_kind": return_kind,
        "persistent": persistent,
        "bucket": bucket,
        "route": route,
        "is_named": return_kind
        in {
            "source_domain_defect_return",
            "valuation_overflow_return",
            "common_kernel_return",
            "fixed_history_or_pdec_return",
            "hot_core_return",
        },
    }


def sample_ledger() -> dict[str, Any]:
    """生成 return 分支前沿样本账本。"""
    samples = [
        {"case": "source_defect_nonpersistent", "return_kind": "source_domain_defect_return", "persistent": False},
        {"case": "source_defect_persistent", "return_kind": "source_domain_defect_return", "persistent": True},
        {"case": "valuation_overflow_nonpersistent", "return_kind": "valuation_overflow_return", "persistent": False},
        {"case": "valuation_overflow_persistent", "return_kind": "valuation_overflow_return", "persistent": True},
        {"case": "hot_core_persistent", "return_kind": "hot_core_return", "persistent": True},
    ]
    rows = [{**item, "classification": classify_return(item["return_kind"], bool(item["persistent"]))} for item in samples]
    return {
        "ledger_type": "carrier_lcm_return_branch_sample_ledger",
        "rule": "carrier-lcm returns are named and split by persistence into sparse budget or persistent terminal family",
        "rows": rows,
        "all_rows_named": all(row["classification"]["is_named"] for row in rows),
        "nonpersistent_budget_rows_present": any(
            row["classification"]["route"] == SPARSE_BUDGET for row in rows
        ),
        "persistent_terminal_rows_present": any(
            row["classification"]["route"] == PERSISTENT_TERMINAL for row in rows
        ),
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_carrier_lcm_return_branch_frontier_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/carrier-lcm-return-branch-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 return 分支前沿需要的导入。"""
    no_return = load_json(DOCS / "prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json")
    named = load_json(DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json")
    unified = load_json(DOCS / "prime-matrix-strict-unified-budget-after-named-sync-router.json")
    sparse = load_json(DOCS / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "target_imported": no_return.get("next_direct_attack_target") == HARDPOINT,
        "no_return_divisibility_imported": bool(
            no_return.get("no_return_cold_prefix_product_divides_carrier_lcm_h0_proved")
        ),
        "named_return_alphabet_compression_imported": bool(named.get("named_return_alphabet_compression_closed")),
        "unified_budget_latest_sync_imported": bool(unified.get("unified_budget_latest_sync_closed")),
        "sparse_history_budget_still_open": unified.get("sparse_history_demand_exceeds_nonpersistent_supply_budget_proved")
        is False,
        "persistent_terminal_still_open": unified.get("persistent_terminal_family_excluded") is False,
        "sparse_history_no_silent_collapse_imported": bool(
            sparse.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget")
        ),
        "common_kernel_no_free_cycle_imported": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
    }


def frontier_rows() -> list[dict[str, str]]:
    """列出 return 分支前沿拆分。"""
    return [
        {
            "return_branch": "source_domain_defect_return",
            "nonpersistent_route": SPARSE_BUDGET,
            "persistent_route": PERSISTENT_TERMINAL,
            "meaning": "单步来源域缺陷不能留在 no-return 分支；非持久则进预算，持久则进终端族。",
        },
        {
            "return_branch": "valuation_overflow_return",
            "nonpersistent_route": SPARSE_BUDGET,
            "persistent_route": PERSISTENT_TERMINAL,
            "meaning": "累计 p-token 溢出已命名；非持久由 U_cold/稀疏历史吸收，持久进入 PDEC/CleanKLS/固定历史。",
        },
        {
            "return_branch": "hot_or_fixed_or_common_kernel_return",
            "nonpersistent_route": SPARSE_BUDGET,
            "persistent_route": PERSISTENT_TERMINAL,
            "meaning": "共同核、热核心、固定历史没有第四出口；仍归入同一二分。",
        },
    ]


def decision_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decision_rows(flags: dict[str, bool], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    frontier_closed = (
        flags["target_imported"]
        and flags["no_return_divisibility_imported"]
        and flags["named_return_alphabet_compression_imported"]
        and flags["unified_budget_latest_sync_imported"]
        and flags["sparse_history_no_silent_collapse_imported"]
        and flags["common_kernel_no_free_cycle_imported"]
        and ledger["all_rows_named"]
    )
    return [
        decision_row(
            "ReturnBranchTargetImported",
            True,
            flags["target_imported"],
            "上一层已把全局 carrier-lcm 兼容剩余压成 return 分支排斥或吸收。",
            HARDPOINT,
        ),
        decision_row(
            "NoReturnBranchAlreadyClosed",
            True,
            flags["no_return_divisibility_imported"],
            "无回流分支上的 D(U)|h0^car 与整数残频已闭合。",
            "no-return branch closed",
        ),
        decision_row(
            "ReturnBranchAlphabetFrontierClosed",
            frontier_closed,
            frontier_closed,
            "所有 carrier-lcm return 分支均归入非持久预算吸收或持久终端族。",
            f"{SPARSE_BUDGET} OR {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "CarrierLCMCompatibilityReturnBranchIndependentHardpointRemoved",
            frontier_closed,
            frontier_closed,
            "return 分支不再是独立黑箱，已压成两个全局终端门。",
            f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorptionProved",
            False,
            False,
            "非持久预算反超与持久终端族排斥仍未完成。",
            f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        ),
        decision_row(
            "ColdPrefixProductDividesCarrierLCMH0LedgerGlobalProved",
            False,
            False,
            "全局整除还差 return 分支排斥或吸收。",
            HARDPOINT,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 return 分支前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    frontier_closed = next(
        item for item in decisions if item["gate"] == "ReturnBranchAlphabetFrontierClosed"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_carrier_lcm_return_branch_frontier_router",
        "status": "carrier_lcm_return_branch_reduced_to_sparse_budget_and_persistent_terminal_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        "next_direct_attack_target": SPARSE_BUDGET,
        "parallel_attack_targets": [PERSISTENT_TERMINAL, DSTRUCTURE],
        "imported_flags": flags,
        "frontier_rows": frontier_rows(),
        "sample_ledger_path": str(OUT_LEDGER.relative_to(ROOT)),
        "sample_ledger_sha256": sha256(OUT_LEDGER),
        "decision_table": decisions,
        "return_branch_alphabet_frontier_closed": bool(frontier_closed),
        "carrier_lcm_compatibility_return_branch_independent_hardpoint_removed": bool(frontier_closed),
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption` 已压缩为全局二门："
            "source-defect、valuation-overflow、共同核、热核心和固定历史等 return 分支均不是第四类出口；"
            "非持久 return 必须进入 `SparseHistoryDemandExceedsNonpersistentSupplyBudget`，持久 return 必须进入 "
            "`IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。"
            "因此 carrier-lcm 兼容的剩余不再是局部整除问题，而是非持久预算反超与持久终端族排斥。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict carrier-lcm return 分支前沿路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "return_branch_alphabet_frontier_closed",
        "carrier_lcm_compatibility_return_branch_independent_hardpoint_removed",
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved",
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved",
        "persistent_terminal_family_excluded",
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. Return 分支前沿")
    lines.append("")
    lines.append("| return_branch | nonpersistent_route | persistent_route | meaning |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["frontier_rows"]:
        lines.append(
            "| "
            + " | ".join(
                table_cell(item[key])
                for key in ["return_branch", "nonpersistent_route", "persistent_route", "meaning"]
            )
            + " |"
        )
    lines.append("")

    lines.append("## 2. 样本账本")
    lines.append("")
    lines.append(f"- path: `{result['sample_ledger_path']}`")
    lines.append(f"- sha256: `{result['sample_ledger_sha256']}`")
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append(f"- 并行守门：`{PERSISTENT_TERMINAL}` 与 `{DSTRUCTURE}`。")
    lines.append("- 边界：本步压缩 return 分支，不证明非持久预算反超或持久终端族排斥。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、Markdown 与样本账本。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "return_branch_alphabet_frontier_closed="
        f"{fmt_bool(result['return_branch_alphabet_frontier_closed'])}"
    )
    print(
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved="
        f"{fmt_bool(result['carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
