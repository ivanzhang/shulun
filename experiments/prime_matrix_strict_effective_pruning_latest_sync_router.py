#!/usr/bin/env python3
"""生成 strict 有效冷历史剪枝最新同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_effective_pruning_latest_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-effective-pruning-latest-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-effective-pruning-latest-sync-router.json
  docs/monograph/prime-matrix-strict-effective-pruning-latest-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-effective-pruning-latest-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-effective-pruning-latest-sync-router.md"

EFFECTIVE_PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
TREE_PACKING = "DivisorCompatibleColdHistoryTreePackingBound"
PREFIX_BRANCHING = "ColdHistoryPrefixBranchingHotOrFixedReturnLemma"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
SMALL_PRIME_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
FANIN = "MultiSourceKernelFanInSAEOrPDECExclusion"
SPARSE_ABSORB = "SparseTerminalHistorySAEAbsorptionOrPDECExclusion"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json",
    "prime-matrix-strict-effective-cold-history-pruning-router.json",
    "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json",
    "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    "prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json",
    "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json",
    "prime-matrix-strict-multisource-fanin-small-quotient-router.json",
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
        "experiments/prime_matrix_strict_effective_pruning_latest_sync_router.py": sha256(
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


def frontier_rows() -> list[dict[str, str]]:
    """列出有效剪枝前沿压缩结果。"""
    return [
        {
            "old_blocker": "single-prime power cascade",
            "new_status": "closed by valuation canonicalization for p=2,3,5",
            "remaining": "none as independent blocker",
        },
        {
            "old_blocker": "multi-source kernel fan-in",
            "new_status": "reduced to bounded quotient SAE/PDEC and sparse terminal sync",
            "remaining": "not an independent fan-in blocker",
        },
        {
            "old_blocker": "formal sparse terminal history",
            "new_status": "synced to same-parameter cold supply numeric envelope",
            "remaining": "effective pruning and terminal anti-cascade",
        },
        {
            "old_blocker": "cold windows staying cold across adjacent prefixes",
            "new_status": "not yet controlled",
            "remaining": "TerminalColdWindowCompatibilityAntiCascadeLemma",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    latest_sync = result["effective_pruning_latest_sync_closed"]
    return [
        row(
            "EffectivePruningInterfaceImported",
            result["effective_pruning_interface_closed"],
            result["effective_pruning_interface_closed"],
            "有效剪枝已归约到除数兼容树、前缀分叉与回流出口。",
            EFFECTIVE_PRUNING,
        ),
        row(
            "SmallPrimePowerCascadeBlockerRemoved",
            result["small_prime_power_cascade_table_proved"],
            result["small_prime_power_cascade_table_proved"],
            "单源小素数幂级联表已关闭。",
            SMALL_PRIME_TABLE,
        ),
        row(
            "FanInIndependentBlockerRemoved",
            result["multisource_fanin_independent_hardpoint_removed"],
            result["multisource_fanin_independent_hardpoint_removed"],
            "多源 fan-in 已并入有界商型 SAE/PDEC，不再作为独立树分叉阻塞。",
            FANIN,
        ),
        row(
            "SparseTerminalSyncImported",
            result["sparse_terminal_history_independent_hardpoint_removed"],
            result["sparse_terminal_history_independent_hardpoint_removed"],
            "稀疏终端残留已接回同参数冷供给数值包。",
            SPARSE_ABSORB,
        ),
        row(
            "EffectivePruningLatestSyncClosed",
            latest_sync,
            latest_sync,
            "旧树打包阻塞已压缩到终端冷窗口反级联与热/固定出口。",
            EFFECTIVE_PRUNING,
        ),
        row(
            "TerminalColdWindowAntiCascadeProved",
            False,
            False,
            "尚未证明相邻/层叠冷窗口不能无限保持冷兼容。",
            TERMINAL_ANTICASCADE,
        ),
        row(
            "EffectiveColdHistoryPruningProved",
            False,
            False,
            "有效剪枝仍需终端冷窗口反级联、热核心和固定历史排斥。",
            f"{TERMINAL_ANTICASCADE} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "ColdSupplyNumericEnvelopeProved",
            False,
            False,
            "即便剪枝结构闭合，还需 C_core/T_PDEC 同参数数值表。",
            f"{COLD_CORE_TABLE} AND {PDEC_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{TERMINAL_ANTICASCADE} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造有效冷历史剪枝最新同步证书。"""
    sparse_sync = load_json("prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json")
    effective = load_json("prime-matrix-strict-effective-cold-history-pruning-router.json")
    single_prime = load_json("prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json")
    fanin = load_json("prime-matrix-strict-multisource-fanin-small-quotient-router.json")

    effective_interface = effective.get("effective_pruning_interface_closed") is True
    small_prime_closed = single_prime.get("small_prime_power_cascade_table_proved") is True
    fanin_removed = fanin.get("multisource_fanin_independent_hardpoint_removed") is True
    sparse_removed = sparse_sync.get("sparse_terminal_history_independent_hardpoint_removed") is True
    latest_sync = effective_interface and small_prime_closed and fanin_removed and sparse_removed

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_effective_pruning_latest_sync_router",
        "status": "effective_pruning_reduced_to_terminal_cold_window_anticascade_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "effective_pruning_interface_closed": effective_interface,
        "small_prime_power_cascade_table_proved": small_prime_closed,
        "multisource_fanin_independent_hardpoint_removed": fanin_removed,
        "sparse_terminal_history_independent_hardpoint_removed": sparse_removed,
        "effective_pruning_latest_sync_closed": latest_sync,
        "terminal_cold_window_anticascade_proved": False,
        "effective_cold_history_pruning_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": EFFECTIVE_PRUNING,
        "hardpoint_after_router": (
            f"{TERMINAL_ANTICASCADE} AND {HOT_CORE} AND {FIXED_HISTORY} "
            f"AND {COLD_CORE_TABLE} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": TERMINAL_ANTICASCADE,
        "parallel_attack_targets": [
            HOT_CORE,
            FIXED_HISTORY,
            COLD_CORE_TABLE,
            PDEC_TABLE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "frontier_rows": frontier_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`EffectiveColdHistoryPruningOrHotFixedReturnTheorem` 已同步到最新前沿："
            "单源小素数幂级联已由 valuation 规范化关闭，多源 fan-in 已归入有界小商 SAE/PDEC，"
            "稀疏终端残留也已接回同参数冷供给数值包。因此旧的树打包宽阻塞不再是当前最窄点。"
            "真正剩余压成 `TerminalColdWindowCompatibilityAntiCascadeLemma`：必须证明冷窗口不能在"
            "相邻前缀/层叠缩频中持续保持冷兼容而不触发热核心、固定历史或命名回流。"
            "本步只更新前沿，不声称有效剪枝或行/列命题已经闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 有效冷历史剪枝最新同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"effective_pruning_interface_closed={fmt_bool(result['effective_pruning_interface_closed'])}",
        f"small_prime_power_cascade_table_proved={fmt_bool(result['small_prime_power_cascade_table_proved'])}",
        f"multisource_fanin_independent_hardpoint_removed={fmt_bool(result['multisource_fanin_independent_hardpoint_removed'])}",
        f"sparse_terminal_history_independent_hardpoint_removed={fmt_bool(result['sparse_terminal_history_independent_hardpoint_removed'])}",
        f"effective_pruning_latest_sync_closed={fmt_bool(result['effective_pruning_latest_sync_closed'])}",
        f"terminal_cold_window_anticascade_proved={fmt_bool(result['terminal_cold_window_anticascade_proved'])}",
        f"effective_cold_history_pruning_proved={fmt_bool(result['effective_cold_history_pruning_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 前沿压缩",
        "",
        "| old blocker | new status | remaining |",
        "|---|---|---|",
    ]
    for item in result["frontier_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['old_blocker'])}` | "
            f"{table_cell(item['new_status'])} | "
            f"`{table_cell(item['remaining'])}` |"
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
