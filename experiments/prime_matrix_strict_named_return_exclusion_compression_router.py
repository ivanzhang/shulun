#!/usr/bin/env python3
"""生成 strict 命名回流排斥压缩证书。

用法示例：
  python3 experiments/prime_matrix_strict_named_return_exclusion_compression_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-named-return-exclusion-compression-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-terminal-defect-exhaustion-router.md",
    MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.md",
    MONOGRAPH / "prime-matrix-named-exit-absorption-contract.md",
    MONOGRAPH / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.md",
    MONOGRAPH / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-router.md",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.md",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.md",
    MONOGRAPH / "claim-status-table.md",
]

NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
PERSISTENT = "PersistentNamedReturnGlobalTerminalExclusion"
NONPERSISTENT = "NonpersistentNamedReturnUnifiedBudgetContradiction"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
UNIFIED_GAP = "UnifiedTerminalBudgetStrictInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def compression_rows() -> list[dict[str, str]]:
    """列出命名回流压缩规则。"""
    return [
        {
            "return_type": "PDEC / ColumnCRT",
            "persistence": "persistent finite signature or fixed displacement",
            "compression": GLOBAL_TERMINAL,
            "meaning": "持久相位/列位移缺陷不再作为单独终端，而是进入全局 PDEC-CAP 或 clean KLS/DLS 终端包。",
        },
        {
            "return_type": "SAE / isolated endpoint",
            "persistence": "nonpersistent sparse packet",
            "compression": UNIFIED_GAP,
            "meaning": "孤立或不持久坏窗只能消耗有限 SAE 供给；是否矛盾由统一预算严格不等式判定。",
        },
        {
            "return_type": "HotCore",
            "persistence": "terminal core divisor window over threshold",
            "compression": f"{GLOBAL_TERMINAL} OR {UNIFIED_GAP}",
            "meaning": "热核心若持久就是 PDEC/ColumnCRT，若不持久则进入冷/热预算，不允许作为自由容量保留。",
        },
        {
            "return_type": "FixedHistory",
            "persistence": "same sparse history word above threshold",
            "compression": GLOBAL_TERMINAL,
            "meaning": "固定历史持久复现就是有限签名 PDEC/ColumnCRT；未持久则已在 sparse SAE 预算中计数。",
        },
        {
            "return_type": "Rankin / finite core",
            "persistence": "promotion or finite ledger return",
            "compression": DSTRUCTURE,
            "meaning": "最终 DStructure/Rankin 晋级门仍是独立验收，不由本命名回流压缩自动关闭。",
        },
    ]


def theorem_rows() -> list[dict[str, Any]]:
    """给出本轮定理边界。"""
    return [
        {
            "name": "NamedReturnCompressionTheorem",
            "proved": True,
            "statement": (
                f"{NAMED_RETURN} 不是新的单体数学估计；它等价压缩为持久命名回流的 "
                f"{PERSISTENT} 与非持久命名回流的 {NONPERSISTENT}。"
            ),
            "role": "删除命名出口字母表自身作为硬点的歧义。",
        },
        {
            "name": "PersistentReturnReduction",
            "proved": True,
            "statement": (
                f"持久 PDEC/ColumnCRT/FixedHistory/HotCore 回流必须进入 {GLOBAL_TERMINAL} "
                "或 DStructure/Rankin 晋级门。"
            ),
            "role": "把持久缺陷接回既有全局终端家族，而不是生成新分支。",
        },
        {
            "name": "NonpersistentReturnReduction",
            "proved": True,
            "statement": (
                f"非持久 SAE/sparse/hot-core 供给必须进入 {UNIFIED_GAP} 的供需比较。"
            ),
            "role": "把孤立缺陷转成可攻的终端预算不等式。",
        },
        {
            "name": "NamedReturnExclusionUnconditional",
            "proved": False,
            "statement": (
                f"完整排斥命名回流仍需证明 {GLOBAL_TERMINAL} 与 {UNIFIED_GAP}，"
                f"并处理 {DSTRUCTURE}。"
            ),
            "role": "这是仍未闭合的全局排斥边界。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍只在假设早期零行反例链内压缩命名回流，不使用真实缺席样本。",
            "remaining": "无。",
        },
        {
            "gate": "NoLossNamedReturnAlphabetImported",
            "closed": True,
            "proved": True,
            "meaning": "no-loss 账本保证所有失败对象都保留为命名 return 记录，不能消失。",
            "remaining": "终端排斥仍未证明。",
        },
        {
            "gate": "NamedReturnCompressionClosed",
            "closed": True,
            "proved": True,
            "meaning": "命名回流字母表已压成持久全局终端包与非持久统一预算二分。",
            "remaining": f"{GLOBAL_TERMINAL} AND {UNIFIED_GAP}",
        },
        {
            "gate": "PersistentNamedReturnExcluded",
            "closed": False,
            "proved": False,
            "meaning": "持久 PDEC/ColumnCRT/FixedHistory 仍需全局 PDEC-CAP 或内部 CleanKLS/DLS 证明。",
            "remaining": GLOBAL_TERMINAL,
        },
        {
            "gate": "NonpersistentNamedReturnExcluded",
            "closed": False,
            "proved": False,
            "meaning": "非持久 sparse/SAE/hot-core 仍需统一终端预算严格反超。",
            "remaining": UNIFIED_GAP,
        },
        {
            "gate": "NamedReturnExclusionProved",
            "closed": False,
            "proved": False,
            "meaning": "命名回流已不再是模糊目标，但其两个压缩后的真输入尚未全部完成。",
            "remaining": f"{GLOBAL_TERMINAL} AND {UNIFIED_GAP} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造命名回流压缩证书。"""
    return {
        "certificate_type": "prime_matrix_strict_named_return_exclusion_compression_router",
        "status": "named_return_exclusion_compressed_persistent_or_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "named_return_compression_closed": True,
        "persistent_named_return_reduced_to_global_terminal": True,
        "nonpersistent_named_return_reduced_to_unified_budget": True,
        "hot_core_fixed_history_absorbed": True,
        "persistent_named_return_excluded": False,
        "nonpersistent_named_return_excluded": False,
        "named_return_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": UNIFIED_GAP,
        "parallel_attack_target": GLOBAL_TERMINAL,
        "referee_gate": DSTRUCTURE,
        "compression_rows": compression_rows(),
        "theorem_rows": theorem_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "命名回流排斥已被压缩：命名出口字母表本身不再是数学硬点。"
            "持久回流接回全局 PDEC-CAP/内部 CleanKLS 终端包；非持久回流接入统一终端预算严格不等式。"
            "因此下一步最适合直接攻有不等式形态的 UnifiedTerminalBudgetStrictInequality。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 命名回流排斥压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"named_return_compression_closed={fmt_bool(result['named_return_compression_closed'])}",
        f"persistent_named_return_reduced_to_global_terminal={fmt_bool(result['persistent_named_return_reduced_to_global_terminal'])}",
        f"nonpersistent_named_return_reduced_to_unified_budget={fmt_bool(result['nonpersistent_named_return_reduced_to_unified_budget'])}",
        f"hot_core_fixed_history_absorbed={fmt_bool(result['hot_core_fixed_history_absorbed'])}",
        f"persistent_named_return_excluded={fmt_bool(result['persistent_named_return_excluded'])}",
        f"nonpersistent_named_return_excluded={fmt_bool(result['nonpersistent_named_return_excluded'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩表",
        "",
        "| return_type | persistence | compression | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["compression_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['return_type'])}`",
                    table_cell(row["persistence"]),
                    table_cell(row["compression"]),
                    table_cell(row["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 定理边界",
            "",
            "| name | proved | statement | role |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["statement"]),
                    table_cell(row["role"]),
                ]
            )
            + " |"
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
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
            "独立晋级门：",
            "",
            "```text",
            result["referee_gate"],
            "```",
            "",
            "审稿边界：本文件只删除命名回流字母表的歧义；"
            "它没有证明全局 PDEC/CleanKLS，也没有证明统一预算严格不等式。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"status={result['status']}")


if __name__ == "__main__":
    main()
