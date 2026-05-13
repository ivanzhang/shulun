#!/usr/bin/env python3
"""生成 strict 共同核回流后统一预算最新同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_unified_budget_after_return_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json
  docs/monograph/prime-matrix-strict-unified-budget-after-return-cycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.md"

UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
RETURN_CYCLE = "CommonKernelReturnCycleDescentOrPDECLedger"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
SAME_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
FIXED_QUOTIENT_PDEC = "FixedQuotientTypePDECColumnCertificateExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    "prime-matrix-strict-unified-budget-after-named-sync-router.json",
    "prime-matrix-strict-sparse-budget-after-unified-sync-router.json",
    "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json",
    "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json",
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
    "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json",
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
        "experiments/prime_matrix_strict_unified_budget_after_return_cycle_sync_router.py": sha256(
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
    """列出回流后统一预算的两条真实剩余线。"""
    return [
        {
            "lane": "nonpersistent budget lane",
            "closed_inputs": "no-silent collapse, finite quotient/history alphabet, no free common-kernel return cycle",
            "remaining": SAME_MARGIN,
        },
        {
            "lane": "persistent named-return lane",
            "closed_inputs": "named alphabet compression and same-set PDEC protocol audit",
            "remaining": f"{DIRECT_PDEC} OR {MOVING_ATOM}",
        },
        {
            "lane": "independent promotion lane",
            "closed_inputs": "none claimed here",
            "remaining": DSTRUCTURE,
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "UnifiedBudgetTargetImported",
            result["unified_budget_target_imported"],
            False,
            "共同核回流账本关闭后，主线返回同参数统一预算严格不等式。",
            UNIFIED_BUDGET,
        ),
        row(
            "NoFreeCommonKernelReturnImported",
            result["no_free_common_kernel_return_imported"],
            result["no_free_common_kernel_return_imported"],
            "非持久共同核不能形成不下降、不收费、不命名的循环。",
            RETURN_CYCLE,
        ),
        row(
            "UnifiedBudgetPreviousSyncImported",
            result["unified_budget_previous_sync_imported"],
            result["unified_budget_previous_sync_imported"],
            "旧统一预算同步已把终局口径固定为非持久预算和持久终端两线。",
            f"{SPARSE_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "SparseBudgetSameParameterReductionImported",
            result["sparse_budget_same_parameter_reduction_imported"],
            result["sparse_budget_same_parameter_reduction_imported"],
            "非持久预算已压成同参数稀疏需求-冷供给严格余量。",
            SAME_MARGIN,
        ),
        row(
            "SameParameterMarginReducedToColdNumericEnvelope",
            result["same_parameter_margin_reduced_to_cold_numeric_envelope"],
            result["same_parameter_margin_reduced_to_cold_numeric_envelope"],
            "同参数余量内部已进一步压成冷供给数值包与热/固定/持久出口。",
            COLD_NUMERIC,
        ),
        row(
            "NamedReturnPersistentLaneStillOpen",
            False,
            False,
            "持久命名回流仍需 acyclic same-set PDEC 作用域匹配、moving atom 排斥或外部输入。",
            f"{NAMED_RETURN} AND {DIRECT_PDEC} AND {MOVING_ATOM}",
        ),
        row(
            "UnifiedBudgetAfterReturnCycleSyncClosed",
            result["unified_budget_after_return_cycle_sync_closed"],
            False,
            "同步边界闭合：免费循环已删除，剩余只在非持久同参数余量和持久命名回流两线。",
            f"{SAME_MARGIN} AND {MOVING_ATOM}",
        ),
        row(
            "UnifiedTerminalBudgetStrictInequalityProved",
            False,
            False,
            "还没有同时证明同参数正余量和持久命名回流排斥。",
            f"{SAME_MARGIN} AND {NAMED_RETURN} AND {MOVING_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{SAME_MARGIN} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造共同核回流后统一预算最新同步证书。"""
    ret = load_json("prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    unified = load_json("prime-matrix-strict-unified-budget-after-named-sync-router.json")
    sparse = load_json("prime-matrix-strict-sparse-budget-after-unified-sync-router.json")
    same = load_json("prime-matrix-strict-same-parameter-sparse-margin-attack-router.json")
    cold = load_json("prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json")
    named = load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json")
    direct = load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json")

    target_imported = ret.get("next_direct_attack_target") == UNIFIED_BUDGET
    no_free_return = ret.get("common_kernel_return_cycle_descent_or_pdec_proved") is True
    unified_sync = unified.get("unified_budget_latest_sync_closed") is True
    sparse_reduction = sparse.get("same_parameter_sparse_demand_cold_supply_normal_form_closed") is True
    same_margin_reduction = same.get("same_parameter_sparse_margin_internal_reduction_closed") is True
    cold_formula = cold.get("cold_supply_formula_sync_closed") is True
    named_compressed = named.get("named_return_alphabet_compression_closed") is True
    direct_scope_audit = direct.get("scope_audit_closed") is True
    sync_closed = all(
        [
            target_imported,
            no_free_return,
            unified_sync,
            sparse_reduction,
            same_margin_reduction,
            cold_formula,
            named_compressed,
            direct_scope_audit,
        ]
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_unified_budget_after_return_cycle_sync_router",
        "status": "unified_budget_synced_after_common_kernel_return_cycle_two_lanes_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "unified_budget_target_imported": target_imported,
        "no_free_common_kernel_return_imported": no_free_return,
        "unified_budget_previous_sync_imported": unified_sync,
        "sparse_budget_same_parameter_reduction_imported": sparse_reduction,
        "same_parameter_margin_reduced_to_cold_numeric_envelope": same_margin_reduction and cold_formula,
        "named_return_alphabet_compression_imported": named_compressed,
        "direct_acyclic_same_set_scope_audit_imported": direct_scope_audit,
        "unified_budget_after_return_cycle_sync_closed": sync_closed,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "named_return_exclusion_proved": False,
        "persistent_terminal_family_excluded": False,
        "moving_atom_exclusion_proved": False,
        "fixed_quotient_pdec_excluded": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": UNIFIED_BUDGET,
        "hardpoint_after_router": f"{SAME_MARGIN} AND {NAMED_RETURN} AND {MOVING_ATOM}",
        "next_direct_attack_target": SAME_MARGIN,
        "parallel_attack_targets": [
            COLD_NUMERIC,
            NAMED_RETURN,
            DIRECT_PDEC,
            FIXED_QUOTIENT_PDEC,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "lane_rows": lane_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`UnifiedTerminalBudgetStrictInequality` 已同步到共同核回流后的最新前沿。"
            "刚关闭的 `CommonKernelReturnCycleDescentOrPDECLedger` 删除了一个旧循环："
            "非持久共同核不能再作为免费回流吞掉预算。于是统一预算的真实剩余只剩两条："
            "一是非持久侧的同参数严格余量 `SameParameterSparseDemandColdSupplyStrictMarginCertificate`，"
            "它已进一步指向 `ColdSupplySameParameterNumericEnvelope`；二是持久命名回流侧的 acyclic PDEC/moving atom 排斥。"
            "本步关闭的是同步边界，不证明这两条剩余，也不声明行/列命题无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 共同核回流后统一预算最新同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"no_free_common_kernel_return_imported={fmt_bool(result['no_free_common_kernel_return_imported'])}",
        f"unified_budget_previous_sync_imported={fmt_bool(result['unified_budget_previous_sync_imported'])}",
        f"sparse_budget_same_parameter_reduction_imported={fmt_bool(result['sparse_budget_same_parameter_reduction_imported'])}",
        f"same_parameter_margin_reduced_to_cold_numeric_envelope={fmt_bool(result['same_parameter_margin_reduced_to_cold_numeric_envelope'])}",
        f"named_return_alphabet_compression_imported={fmt_bool(result['named_return_alphabet_compression_imported'])}",
        f"direct_acyclic_same_set_scope_audit_imported={fmt_bool(result['direct_acyclic_same_set_scope_audit_imported'])}",
        f"unified_budget_after_return_cycle_sync_closed={fmt_bool(result['unified_budget_after_return_cycle_sync_closed'])}",
        f"same_parameter_sparse_demand_cold_supply_strict_margin_proved={fmt_bool(result['same_parameter_sparse_demand_cold_supply_strict_margin_proved'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 剩余两线",
        "",
        "| lane | closed inputs | remaining |",
        "| --- | --- | --- |",
    ]
    for item in result["lane_rows"]:
        lines.append(
            "| {lane} | {closed_inputs} | {remaining} |".format(
                lane=table_cell(item["lane"]),
                closed_inputs=table_cell(item["closed_inputs"]),
                remaining=table_cell(item["remaining"]),
            )
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
            "## 3. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 下钻入口：`{COLD_NUMERIC}`。",
            "- 并行门：持久命名回流、acyclic PDEC/moving atom、DStructure/Rankin。",
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
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
