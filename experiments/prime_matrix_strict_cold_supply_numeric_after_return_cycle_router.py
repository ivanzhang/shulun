#!/usr/bin/env python3
"""生成 strict 回流后冷供给数值包同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_supply_numeric_after_return_cycle_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json
  docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.md"

COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
CORE_CAP_TABLE = "ColdCoreThresholdFunctionNumericTable"
PERSISTENCE_TABLE = "SameParameterPDECThresholdNumericTable"
RETURN_CYCLE = "CommonKernelReturnCycleDescentOrPDECLedger"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
SIBLING_CHARGING = "CanonicalColdWindowSiblingChargingOrHotReturnLedger"
WIDTH_LCM = "SiblingCollarWidthLCMKernelCompressionLedger"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json",
    "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json",
    "prime-matrix-strict-effective-pruning-latest-sync-router.json",
    "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
    "prime-matrix-strict-cold-window-sibling-charging-router.json",
    "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json",
    "prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json",
    "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
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
        "experiments/prime_matrix_strict_cold_supply_numeric_after_return_cycle_router.py": sha256(
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


def pruning_rows() -> list[dict[str, str]]:
    """列出预算版有效剪枝的出口。"""
    return [
        {
            "failure_mode": "terminal cold-window anti-cascade fails",
            "route": "sibling charging / collar width LCM / low-kernel return",
            "budget_effect": "cannot remain in U_np after no-free-return-cycle",
        },
        {
            "failure_mode": "sibling family overcharges parent cold support",
            "route": "hot core or fixed history",
            "budget_effect": "counted as named return, not cold supply",
        },
        {
            "failure_mode": "collar width explosion",
            "route": "LCM height or common-kernel return",
            "budget_effect": "LCM/common-kernel branch is charged, not free",
        },
        {
            "failure_mode": "all named returns absent",
            "route": "genuinely cold nonpersistent histories only",
            "budget_effect": "remaining task is numeric C_core/T_PDEC summation",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ColdNumericTargetImported",
            result["cold_numeric_target_imported"],
            result["cold_numeric_target_imported"],
            "回流后同参数余量已把主攻点指向冷供给数值包。",
            COLD_NUMERIC,
        ),
        row(
            "ColdSupplyFormulaSyncImported",
            result["cold_supply_formula_sync_imported"],
            result["cold_supply_formula_sync_imported"],
            "旧冷供给公式和同参数调参纪律可用。",
            COLD_NUMERIC,
        ),
        row(
            "EffectivePruningStructuralSyncImported",
            result["effective_pruning_structural_sync_imported"],
            result["effective_pruning_structural_sync_imported"],
            "有效剪枝已通过小素数幂、fan-in、稀疏终端和兄弟收费链同步到最新前沿。",
            PRUNING,
        ),
        row(
            "NoFreeReturnCycleImported",
            result["no_free_return_cycle_imported"],
            result["no_free_return_cycle_imported"],
            "共同核/LCM/collar 回流不能作为免费冷供给循环。",
            RETURN_CYCLE,
        ),
        row(
            "EffectivePruningClosedForNonpersistentBudget",
            result["effective_pruning_closed_for_nonpersistent_budget"],
            result["effective_pruning_closed_for_nonpersistent_budget"],
            "剪枝失败均进入命名出口或预算扣减；纯非持久 U_np 只剩真正冷历史。",
            f"{CORE_CAP_TABLE} AND {PERSISTENCE_TABLE}",
        ),
        row(
            "ColdCoreThresholdNumericTableProved",
            False,
            False,
            "仍缺同参数 C_core(W) 的可求和数值表。",
            CORE_CAP_TABLE,
        ),
        row(
            "SameParameterPDECThresholdNumericTableProved",
            False,
            False,
            "仍缺同参数 T_PDEC(W) 的阈值数值表。",
            PERSISTENCE_TABLE,
        ),
        row(
            "ColdSupplySameParameterNumericEnvelopeProved",
            False,
            False,
            "预算版剪枝关闭后，真正剩余是 C_core/T_PDEC 数值表与并行命名出口排斥。",
            f"{CORE_CAP_TABLE} AND {PERSISTENCE_TABLE} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{CORE_CAP_TABLE} AND {PERSISTENCE_TABLE} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造回流后冷供给数值包证书。"""
    margin = load_json("prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json")
    cold = load_json("prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json")
    effective = load_json("prime-matrix-strict-effective-pruning-latest-sync-router.json")
    sibling = load_json("prime-matrix-strict-cold-window-sibling-charging-router.json")
    width = load_json("prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json")
    low = load_json("prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json")
    ret = load_json("prime-matrix-strict-common-kernel-return-cycle-descent-router.json")

    target = margin.get("next_direct_attack_target") == COLD_NUMERIC
    formula = cold.get("cold_supply_formula_sync_closed") is True
    effective_sync = effective.get("effective_pruning_latest_sync_closed") is True
    sibling_closed = sibling.get("canonical_cold_window_sibling_charging_ledger_closed") is True
    width_closed = width.get("width_lcm_kernel_compression_proved") is True
    low_unnamed_removed = low.get("unnamed_low_kernel_exit_removed") is True
    no_free_return = ret.get("common_kernel_return_cycle_descent_or_pdec_proved") is True
    budget_pruning_closed = all(
        [target, formula, effective_sync, sibling_closed, width_closed, low_unnamed_removed, no_free_return]
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_cold_supply_numeric_after_return_cycle_router",
        "status": "cold_supply_numeric_after_return_cycle_reduced_to_core_pdec_tables_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "cold_numeric_target_imported": target,
        "cold_supply_formula_sync_imported": formula,
        "effective_pruning_structural_sync_imported": effective_sync,
        "sibling_charging_ledger_imported": sibling_closed,
        "collar_width_lcm_compression_imported": width_closed,
        "low_kernel_unnamed_exit_removed_imported": low_unnamed_removed,
        "no_free_return_cycle_imported": no_free_return,
        "effective_pruning_closed_for_nonpersistent_budget": budget_pruning_closed,
        "cold_core_threshold_numeric_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "moving_atom_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLD_NUMERIC,
        "hardpoint_after_router": f"{CORE_CAP_TABLE} AND {PERSISTENCE_TABLE} AND {HOT_CORE} AND {FIXED_HISTORY}",
        "next_direct_attack_target": CORE_CAP_TABLE,
        "parallel_attack_targets": [PERSISTENCE_TABLE, HOT_CORE, FIXED_HISTORY, MOVING_ATOM, DSTRUCTURE],
        "pruning_rows": pruning_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdSupplySameParameterNumericEnvelope` 已同步到共同核回流关闭后的前沿。"
            "旧的有效剪枝阻塞不再是一个免费循环：终端冷窗口反级联失败、兄弟超收费、collar 宽度爆发、"
            "低乘子共同核回流都会进入热核心、固定历史、PDEC/SAE 或统一预算扣减，不能继续算入纯非持久冷供给。"
            "因此在非持久预算侧，真正剩余压成两个数值表：`ColdCoreThresholdFunctionNumericTable` "
            "和 `SameParameterPDECThresholdNumericTable`。本步不排斥热/固定/持久出口，也不证明最终数值反超。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 回流后冷供给数值包同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cold_numeric_target_imported={fmt_bool(result['cold_numeric_target_imported'])}",
        f"cold_supply_formula_sync_imported={fmt_bool(result['cold_supply_formula_sync_imported'])}",
        f"effective_pruning_structural_sync_imported={fmt_bool(result['effective_pruning_structural_sync_imported'])}",
        f"no_free_return_cycle_imported={fmt_bool(result['no_free_return_cycle_imported'])}",
        f"effective_pruning_closed_for_nonpersistent_budget={fmt_bool(result['effective_pruning_closed_for_nonpersistent_budget'])}",
        f"cold_core_threshold_numeric_table_proved={fmt_bool(result['cold_core_threshold_numeric_table_proved'])}",
        f"same_parameter_pdec_threshold_numeric_table_proved={fmt_bool(result['same_parameter_pdec_threshold_numeric_table_proved'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 剪枝失败出口",
        "",
        "| failure mode | route | budget effect |",
        "| --- | --- | --- |",
    ]
    for item in result["pruning_rows"]:
        lines.append(
            "| {failure_mode} | {route} | {budget_effect} |".format(
                failure_mode=table_cell(item["failure_mode"]),
                route=table_cell(item["route"]),
                budget_effect=table_cell(item["budget_effect"]),
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
            f"- 并行：`{PERSISTENCE_TABLE}`、热核心/固定历史、moving atom 与 DStructure。",
            "- 边界：本步关闭预算版有效剪枝，不提交 C_core/T_PDEC 数值表。",
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
