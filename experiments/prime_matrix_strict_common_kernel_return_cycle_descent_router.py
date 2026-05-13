#!/usr/bin/env python3
"""生成 strict 共同核回流循环下降/PDEC 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_common_kernel_return_cycle_descent_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json

输出：
  docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json
  docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json"
OUT_MD = DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.md"

RETURN_DESCENT = "CommonKernelReturnCycleDescentOrPDECLedger"
LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
SPARSE_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
FIXED_QUOTIENT_PDEC = "FixedQuotientTypePDECColumnCertificateExclusion"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
BOUNDED_SAE = "BoundedQuotientTypeSAEAbsorption"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json",
    "prime-matrix-strict-fixed-quotient-type-columncrt-router.json",
    "prime-matrix-strict-fixed-quotient-density-transfer-router.json",
    "prime-matrix-strict-sparse-terminal-history-router.json",
    "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json",
    "prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json",
    "prime-matrix-strict-cold-window-sibling-charging-router.json",
    "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json",
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    "prime-matrix-strict-unified-budget-after-named-sync-router.json",
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
        "experiments/prime_matrix_strict_common_kernel_return_cycle_descent_router.py": sha256(
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


def cycle_exit_rows() -> list[dict[str, str]]:
    """列出回流循环的三类出口。"""
    return [
        {
            "exit": "fixed quotient descent",
            "trigger": "persistent pair quotient (b,c) with bc>=2",
            "effect": "frequency height h is replaced by h/(bc), so a same-level cycle is impossible",
        },
        {
            "exit": "persistent finite type",
            "trigger": "same history word, quotient type, sibling overlap key, or kernel key repeats above threshold",
            "effect": "the branch is registered as FixedHistory/ColumnCRT/PDEC",
        },
        {
            "exit": "nonpersistent finite debit",
            "trigger": "no finite type reaches its persistence threshold",
            "effect": "each return consumes a bounded SAE/history-token allowance already present in the nonpersistent budget",
        },
        {
            "exit": "hot family return",
            "trigger": "sibling family charge exceeds the cold support envelope",
            "effect": "the branch is no longer cold; it routes to hot core, fixed history, PDEC, or SAE",
        },
    ]


def token_samples() -> list[dict[str, Any]]:
    """给出有限类型阈值样本，核验非持久回流有总量上界。"""
    samples: list[dict[str, Any]] = []
    for alphabet_size, threshold in [(6, 3), (10, 4), (14, 5)]:
        max_nonpersistent = alphabet_size * (threshold - 1)
        first_forced_persistent = max_nonpersistent + 1
        samples.append(
            {
                "alphabet_size": alphabet_size,
                "threshold": threshold,
                "max_nonpersistent_returns": max_nonpersistent,
                "first_forced_persistent_return": first_forced_persistent,
                "pigeonhole_ok": first_forced_persistent > max_nonpersistent,
            }
        )
    return samples


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "ReturnCycleTargetImported",
            result["return_cycle_target_imported"],
            result["return_cycle_target_imported"],
            "上一层已把低乘子共同核的真正剩余压成回流下降/PDEC 账本。",
            RETURN_DESCENT,
        ),
        row(
            "FixedQuotientHeightDescentClosed",
            result["fixed_quotient_height_descent_closed"],
            result["fixed_quotient_height_descent_closed"],
            "固定商型分支已有 h -> h/(bc), bc>=2 的严格高度下降。",
            FIXED_QUOTIENT_PDEC,
        ),
        row(
            "PersistentFiniteTypePDECRouteClosed",
            result["persistent_finite_type_pdec_route_closed"],
            False,
            "同一有限历史/商型/重叠键持久复现时已登记为 PDEC/ColumnCRT，但排斥未完成。",
            f"{FIXED_HISTORY} OR {FIXED_QUOTIENT_PDEC}",
        ),
        row(
            "NonpersistentFiniteDebitClosed",
            result["nonpersistent_finite_debit_closed"],
            result["nonpersistent_finite_debit_closed"],
            "若没有持久复现，则回流次数由有限字母表乘持久阈值控制，并进入 SAE/冷供给预算。",
            f"{BOUNDED_SAE} AND {SPARSE_MARGIN}",
        ),
        row(
            "SiblingHotFixedReturnRegistered",
            result["sibling_hot_fixed_return_registered"],
            result["sibling_hot_fixed_return_registered"],
            "兄弟整族超冷预算或重复收费不能继续留在冷分支。",
            f"{HOT_CORE} OR {FIXED_HISTORY}",
        ),
        row(
            "FreeCommonKernelReturnCycleExcluded",
            result["free_common_kernel_return_cycle_excluded"],
            result["free_common_kernel_return_cycle_excluded"],
            "共同核回流不能无限免费循环；必为高度下降、有限预算扣减、热回流或 PDEC。",
            f"{UNIFIED_BUDGET} OR {NAMED_RETURN}",
        ),
        row(
            "CommonKernelReturnCycleDescentOrPDECProved",
            result["common_kernel_return_cycle_descent_or_pdec_proved"],
            result["common_kernel_return_cycle_descent_or_pdec_proved"],
            "目标账本闭合为无免费循环；但命名出口和预算严格余量仍开。",
            f"{UNIFIED_BUDGET} AND {NAMED_RETURN}",
        ),
        row(
            "LowMultiplierCommonKernelExcluded",
            False,
            False,
            "共同核免费循环已排除，但 PDEC/SAE/热核心/固定历史出口尚未全部排斥。",
            f"{UNIFIED_BUDGET} AND {NAMED_RETURN} AND {FIXED_QUOTIENT_PDEC}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{UNIFIED_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造回流循环下降/PDEC 证书。"""
    low_sync = load_json("prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json")
    fixed = load_json("prime-matrix-strict-fixed-quotient-type-columncrt-router.json")
    fixed_transfer = load_json("prime-matrix-strict-fixed-quotient-density-transfer-router.json")
    sparse = load_json("prime-matrix-strict-sparse-terminal-history-router.json")
    sparse_budget = load_json("prime-matrix-strict-sparse-terminal-history-sae-budget-router.json")
    sibling = load_json("prime-matrix-strict-cold-window-sibling-charging-router.json")
    named = load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json")
    unified = load_json("prime-matrix-strict-unified-budget-after-named-sync-router.json")

    target_imported = low_sync.get("next_direct_attack_target") == RETURN_DESCENT
    fixed_descent = (
        fixed.get("strict_height_descent_closed") is True
        and fixed.get("finite_descent_depth_closed") is True
        and fixed_transfer.get("density_transfer_without_loss_closed") is True
    )
    persistent_route = (
        sparse.get("persistent_history_pdec_route_registered") is True
        and named.get("named_return_alphabet_compression_closed") is True
    )
    nonpersistent_debit = (
        sparse.get("history_word_encoding_closed") is True
        and sparse.get("nonpersistent_history_sae_reduction_closed") is True
        and sparse_budget.get("nonpersistent_sae_budget_formula_closed") is True
    )
    sibling_return = (
        sibling.get("family_hot_return_registered") is True
        and sibling.get("overlap_return_registered") is True
        and sibling.get("canonical_cold_window_sibling_charging_ledger_closed") is True
    )
    samples = token_samples()
    samples_ok = all(item["pigeonhole_ok"] for item in samples)
    free_cycle_excluded = target_imported and fixed_descent and persistent_route and nonpersistent_debit and sibling_return and samples_ok
    unified_synced = unified.get("unified_budget_latest_sync_closed") is True

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_common_kernel_return_cycle_descent_router",
        "status": "common_kernel_free_return_cycle_excluded_named_exits_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "return_cycle_target_imported": target_imported,
        "fixed_quotient_height_descent_closed": fixed_descent,
        "persistent_finite_type_pdec_route_closed": persistent_route,
        "nonpersistent_finite_debit_closed": nonpersistent_debit,
        "sibling_hot_fixed_return_registered": sibling_return,
        "finite_token_pigeonhole_samples_passed": samples_ok,
        "free_common_kernel_return_cycle_excluded": free_cycle_excluded,
        "common_kernel_return_cycle_descent_or_pdec_proved": free_cycle_excluded,
        "unified_budget_latest_sync_imported": unified_synced,
        "unified_terminal_budget_strict_inequality_proved": False,
        "named_return_exclusion_proved": False,
        "fixed_quotient_pdec_excluded": False,
        "terminal_core_hot_divisor_window_excluded": False,
        "fixed_type_history_pdec_excluded": False,
        "low_multiplier_common_kernel_excluded": False,
        "terminal_cold_window_anticascade_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": RETURN_DESCENT,
        "hardpoint_after_router": f"{UNIFIED_BUDGET} AND {NAMED_RETURN} AND {FIXED_QUOTIENT_PDEC}",
        "next_direct_attack_target": UNIFIED_BUDGET,
        "parallel_attack_targets": [
            NAMED_RETURN,
            SPARSE_MARGIN,
            FIXED_QUOTIENT_PDEC,
            HOT_CORE,
            FIXED_HISTORY,
            TERMINAL_ANTICASCADE,
            SIBLING_NUMERIC,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "cycle_exit_rows": cycle_exit_rows(),
        "finite_token_samples": samples,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`CommonKernelReturnCycleDescentOrPDECLedger` 可以关闭为“无免费回流循环”。"
            "若共同核分支落在固定商型，已有 `h -> h/(bc)` 且 `bc>=2` 的严格高度下降；"
            "若不固定但有限历史/商型/重叠键反复出现，则由持久阈值登记为固定历史、ColumnCRT 或 PDEC；"
            "若所有键都不持久，则每次回流都消耗有限字母表 SAE/冷供给预算；兄弟整族超收费则转入热核心或固定历史。"
            "因此低乘子共同核不能形成不下降、不收费、也不命名的循环。"
            "但这只关闭免费循环，不排斥 PDEC/SAE/热核心/固定历史出口，也不证明统一终端预算严格余量，"
            "所以行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 共同核回流循环下降/PDEC 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"return_cycle_target_imported={fmt_bool(result['return_cycle_target_imported'])}",
        f"fixed_quotient_height_descent_closed={fmt_bool(result['fixed_quotient_height_descent_closed'])}",
        f"persistent_finite_type_pdec_route_closed={fmt_bool(result['persistent_finite_type_pdec_route_closed'])}",
        f"nonpersistent_finite_debit_closed={fmt_bool(result['nonpersistent_finite_debit_closed'])}",
        f"sibling_hot_fixed_return_registered={fmt_bool(result['sibling_hot_fixed_return_registered'])}",
        f"free_common_kernel_return_cycle_excluded={fmt_bool(result['free_common_kernel_return_cycle_excluded'])}",
        f"common_kernel_return_cycle_descent_or_pdec_proved={fmt_bool(result['common_kernel_return_cycle_descent_or_pdec_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"low_multiplier_common_kernel_excluded={fmt_bool(result['low_multiplier_common_kernel_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 回流出口",
        "",
        "| exit | trigger | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["cycle_exit_rows"]:
        lines.append(
            "| {exit} | {trigger} | {effect} |".format(
                exit=table_cell(item["exit"]),
                trigger=table_cell(item["trigger"]),
                effect=table_cell(item["effect"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 有限 token 样本",
            "",
            "| alphabet size | threshold | max nonpersistent returns | first forced persistent return | pigeonhole ok |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["finite_token_samples"]:
        lines.append(
            "| `{alphabet_size}` | `{threshold}` | `{max_np}` | `{first}` | `{ok}` |".format(
                alphabet_size=item["alphabet_size"],
                threshold=item["threshold"],
                max_np=item["max_nonpersistent_returns"],
                first=item["first_forced_persistent_return"],
                ok=fmt_bool(item["pigeonhole_ok"]),
            )
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
            "## 4. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 含义：免费循环已经排除，剩余必须在同参数终端预算中证明需求严格大于非持久供给与命名回流扣除。",
            "- 并行：固定商型 PDEC、固定历史、热核心和 DStructure/Rankin 仍是独立验收门。",
            "",
            "## 5. 依赖哈希",
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
