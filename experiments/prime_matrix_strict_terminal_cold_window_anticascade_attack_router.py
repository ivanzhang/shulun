#!/usr/bin/env python3
"""生成 strict 终端冷窗口反级联攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_cold_window_anticascade_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json
  docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.md"

TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
SIBLING_CHARGING = "CanonicalColdWindowSiblingChargingOrHotReturnLedger"
EFFECTIVE_PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
COLD_THRESHOLD_INVARIANCE = "ColdCoreThresholdDyadicOrderInvarianceBindingLedger"
SMALL_PRIME_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
FANIN = "MultiSourceKernelFanInSAEOrPDECExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-effective-pruning-latest-sync-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json",
    "prime-matrix-strict-multisource-fanin-small-quotient-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
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
        "experiments/prime_matrix_strict_terminal_cold_window_anticascade_attack_router.py": sha256(
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


def insufficiency_witness_rows() -> list[dict[str, Any]]:
    """给出现有局部冷条件不足以推出全局反级联的逻辑见证。"""
    rows: list[dict[str, Any]] = []
    for sibling_count in [2, 4, 8, 16]:
        c_core = 1
        local_cold_capacity = sibling_count * c_core
        rows.append(
            {
                "sibling_windows": sibling_count,
                "per_window_count": 1,
                "C_core": c_core,
                "all_windows_cold": True,
                "total_cold_charge": local_cold_capacity,
                "parent_bound_without_charging": "unbounded in sibling_count",
                "meaning": "局部 N_H(I)<=C_core 不会自动给出兄弟窗口求和界。",
            }
        )
    return rows


def required_ledger_rows() -> list[dict[str, str]]:
    """列出反级联闭合需要的精确账本。"""
    return [
        {
            "input": "canonical sibling family",
            "statement": "all children of a fixed prefix U are grouped by the same H_U and normalized product-window scale",
            "status": "available qualitatively",
        },
        {
            "input": "charging inequality",
            "statement": "sum_child C_core(child) <= C_parent_budget + named hot/fixed/PDEC returns",
            "status": "missing quantitative ledger",
        },
        {
            "input": "overlap discipline",
            "statement": "a terminal core charged to multiple child windows must create a fixed-history or ColumnCRT return",
            "status": "registered but not proved as global bound",
        },
        {
            "input": "same-parameter numeric table",
            "statement": "C_core and T_PDEC must be evaluated under the same Lambda/PDEC ledger",
            "status": "open numeric companion",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "EffectivePruningFrontierImported",
            result["effective_pruning_latest_sync_closed"],
            result["effective_pruning_latest_sync_closed"],
            "有效剪枝前沿已压缩到终端冷窗口反级联。",
            EFFECTIVE_PRUNING,
        ),
        row(
            "CanonicalThresholdAndWindowImported",
            result["canonical_threshold_and_window_imported"],
            result["canonical_threshold_and_window_imported"],
            "product-window 端点和 C_core 注册键已规范化。",
            COLD_THRESHOLD_INVARIANCE,
        ),
        row(
            "OldCascadeModesRemoved",
            result["old_cascade_modes_removed"],
            result["old_cascade_modes_removed"],
            "单源小素数幂和多源 fan-in 已不再是独立反级联阻塞。",
            f"{SMALL_PRIME_TABLE} AND {FANIN}",
        ),
        row(
            "LocalColdPredicateInsufficient",
            True,
            True,
            "局部 N_H(I)<=C_core 不能推出兄弟冷窗口求和界。",
            SIBLING_CHARGING,
        ),
        row(
            "SiblingChargingLedgerIsolated",
            True,
            True,
            "必须补兄弟窗口收费或重叠回流账本，才能关闭反级联。",
            SIBLING_CHARGING,
        ),
        row(
            "TerminalColdWindowAntiCascadeProved",
            False,
            False,
            "缺少 sum_child C_core(child) 的同参数求和控制。",
            SIBLING_CHARGING,
        ),
        row(
            "EffectiveColdHistoryPruningProved",
            False,
            False,
            "反级联、热核心和固定历史排斥仍未完成。",
            f"{SIBLING_CHARGING} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "ColdSupplyNumericEnvelopeProved",
            False,
            False,
            "还需 C_core/T_PDEC 同参数数值表接回最终供需余量。",
            f"{COLD_CORE_TABLE} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{SIBLING_CHARGING} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造终端冷窗口反级联攻坚证书。"""
    effective = load_json("prime-matrix-strict-effective-pruning-latest-sync-router.json")
    threshold = load_json("prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json")
    single_prime = load_json("prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json")
    fanin = load_json("prime-matrix-strict-multisource-fanin-small-quotient-router.json")

    effective_sync = effective.get("effective_pruning_latest_sync_closed") is True
    threshold_imported = threshold.get("cold_core_threshold_dyadic_order_invariance_proved") is True
    small_closed = single_prime.get("small_prime_power_cascade_table_proved") is True
    fanin_removed = fanin.get("multisource_fanin_independent_hardpoint_removed") is True
    old_modes_removed = small_closed and fanin_removed

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_terminal_cold_window_anticascade_attack_router",
        "status": "terminal_cold_window_anticascade_reduced_to_sibling_charging_ledger_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "effective_pruning_latest_sync_closed": effective_sync,
        "canonical_threshold_and_window_imported": threshold_imported,
        "old_cascade_modes_removed": old_modes_removed,
        "local_cold_predicate_insufficient_for_global_anticascade": True,
        "canonical_cold_window_sibling_charging_isolated": True,
        "terminal_cold_window_anticascade_proved": False,
        "effective_cold_history_pruning_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TERMINAL_ANTICASCADE,
        "hardpoint_after_router": (
            f"{SIBLING_CHARGING} AND {HOT_CORE} AND {FIXED_HISTORY} "
            f"AND {COLD_CORE_TABLE} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": SIBLING_CHARGING,
        "parallel_attack_targets": [
            HOT_CORE,
            FIXED_HISTORY,
            COLD_CORE_TABLE,
            PDEC_TABLE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "insufficiency_witness_rows": insufficiency_witness_rows(),
        "required_ledger_rows": required_ledger_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`TerminalColdWindowCompatibilityAntiCascadeLemma` 的最窄缺口已定位："
            "现有材料已经规范化端点和 C_core，也关闭了单源小素数幂与多源 fan-in，"
            "但局部冷条件 `N_H(I)<=C_core` 本身不能推出兄弟窗口或相邻前缀的全局求和界。"
            "若有许多兄弟窗口各自只含 1 个核心且 `C_core>=1`，每个窗口都冷，"
            "总冷收费仍可随兄弟数增长。要完成反级联，必须新增 "
            "`CanonicalColdWindowSiblingChargingOrHotReturnLedger`："
            "证明兄弟冷窗口的 C_core 总收费可被父级预算控制，或者重叠/过密必回流热核心、"
            "固定历史或 PDEC/ColumnCRT。本步给出的是精确剩余原子，不声称反级联或行/列命题已闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 终端冷窗口反级联攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"effective_pruning_latest_sync_closed={fmt_bool(result['effective_pruning_latest_sync_closed'])}",
        f"canonical_threshold_and_window_imported={fmt_bool(result['canonical_threshold_and_window_imported'])}",
        f"old_cascade_modes_removed={fmt_bool(result['old_cascade_modes_removed'])}",
        f"local_cold_predicate_insufficient_for_global_anticascade={fmt_bool(result['local_cold_predicate_insufficient_for_global_anticascade'])}",
        f"canonical_cold_window_sibling_charging_isolated={fmt_bool(result['canonical_cold_window_sibling_charging_isolated'])}",
        f"terminal_cold_window_anticascade_proved={fmt_bool(result['terminal_cold_window_anticascade_proved'])}",
        f"effective_cold_history_pruning_proved={fmt_bool(result['effective_cold_history_pruning_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 局部冷条件不足见证",
        "",
        "| siblings | per-window count | C_core | all cold | total cold charge | parent bound without charging |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for item in result["insufficiency_witness_rows"]:
        lines.append(
            "| "
            f"{item['sibling_windows']} | "
            f"{item['per_window_count']} | "
            f"{item['C_core']} | "
            f"`{fmt_bool(item['all_windows_cold'])}` | "
            f"{item['total_cold_charge']} | "
            f"`{table_cell(item['parent_bound_without_charging'])}` |"
        )

    lines.extend(
        [
            "",
            "## 必需账本",
            "",
            "| input | statement | status |",
            "|---|---|---|",
        ]
    )
    for item in result["required_ledger_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['input'])}` | "
            f"{table_cell(item['statement'])} | "
            f"`{table_cell(item['status'])}` |"
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
    for item in result["decision_rows"]:
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
