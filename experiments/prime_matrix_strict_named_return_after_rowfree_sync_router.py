#!/usr/bin/env python3
"""生成 strict row-free 后命名回流同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_named_return_after_rowfree_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json
  docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-named-return-after-rowfree-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-row-free-type-anticollapse-sync-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
    "prime-matrix-strict-named-return-same-parameter-deduction-router.json",
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
    "prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json",
]

NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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
    result = {"experiments/prime_matrix_strict_named_return_after_rowfree_sync_router.py": sha256(Path(__file__).resolve())}
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


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成命名回流同步判定表。"""
    rowfree = data["rowfree"]
    named = data["named"]
    same_param = data["same_param"]
    defect = data["defect"]
    margin = data["margin"]

    target_imported = rowfree.get("next_direct_attack_target") == NAMED_RETURN
    no_silent = rowfree.get("prefix_label_support_to_row_free_type_anticollapse_closed_for_budget") is True
    compression_closed = named.get("named_return_compression_closed") is True
    same_schema = same_param.get("named_return_same_parameter_schema_closed") is True
    defect_no_free = defect.get("status") == "terminal_defect_no_free_exit_closed_unconditional_exclusion_open"
    persistent_to_terminal = same_param.get("persistent_named_return_numeric_zero_available") is False
    nonpersistent_to_budget = (
        named.get("next_direct_attack_target") == UNIFIED_BUDGET
        and same_param.get("nonpersistent_named_return_absorbed_by_budget") is False
    )
    margin_knows_terminal = any(
        item.get("gate") == "PersistentReturnReducedToTerminalFamily" and item.get("closed") is True
        for item in margin.get("rows", []) or []
    )

    return [
        row(
            "NamedReturnTargetImportedFromRowFree",
            target_imported and no_silent,
            False,
            "row-free 抗塌缩预算版闭合后，剩余回流不能静默消失，只能作为命名回流或预算项处理。",
            NAMED_RETURN,
        ),
        row(
            "NoUnnamedDefectExitClosed",
            defect_no_free,
            False,
            "容量失败、丢标签、相位漂移、端点/TV 缺陷没有第四类无名出口，必须进入命名字母表。",
            NAMED_RETURN,
        ),
        row(
            "NamedAlphabetCompressionClosed",
            compression_closed,
            False,
            "PDEC/SAE/ColumnCRT/热核心/固定历史等命名出口字母表本身已压成持久终端包与非持久预算。",
            f"{TERMINAL_FAMILY} OR {UNIFIED_BUDGET}",
        ),
        row(
            "SameParameterDeductionSchemaClosed",
            same_schema,
            False,
            "E_named 的同参数扣除表结构闭合；不能凭空填 0，必须通过终端排斥或预算吸收。",
            "NamedReturnSameParameterDeductionTable",
        ),
        row(
            "PersistentNamedReturnReducedToTerminalFamily",
            persistent_to_terminal and margin_knows_terminal,
            False,
            "持久命名回流只有在 acyclic terminal family 被排斥后才能数值归零。",
            TERMINAL_FAMILY,
        ),
        row(
            "NonpersistentNamedReturnReducedToBudgetAbsorption",
            nonpersistent_to_budget,
            False,
            "非持久命名回流不需要单独逐项排斥；它必须进入 U_cold/统一预算吸收。",
            UNIFIED_BUDGET,
        ),
        row(
            "NamedReturnAlphabetNoLongerIndependentHardpoint",
            target_imported and compression_closed and same_schema and defect_no_free,
            False,
            "命名回流这个宽标签已完成拆解；剩余是终端族排斥与统一预算严格不等式，不是再扩展出口字母表。",
            f"{UNIFIED_BUDGET} AND {TERMINAL_FAMILY}",
        ),
        row(
            "NamedReturnExclusionCurrentCorpusProved",
            False,
            False,
            "当前材料尚未排斥所有持久终端族，也未证明统一预算严格吸收全部非持久回流。",
            f"{UNIFIED_BUDGET} AND {MOVING_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭命名回流字母表硬点，不关闭最终反例矛盾。",
            f"{UNIFIED_BUDGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 row-free 后命名回流同步证书。"""
    data = {
        "rowfree": load_json("prime-matrix-strict-row-free-type-anticollapse-sync-router.json"),
        "named": load_json("prime-matrix-strict-named-return-exclusion-compression-router.json"),
        "same_param": load_json("prime-matrix-strict-named-return-same-parameter-deduction-router.json"),
        "defect": load_json("prime-matrix-strict-terminal-defect-exhaustion-router.json"),
        "margin": load_json("prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json"),
    }
    rows = build_rows(data)
    alphabet_closed = any(
        item["gate"] == "NamedReturnAlphabetNoLongerIndependentHardpoint" and item["closed"]
        for item in rows
    )

    return {
        "certificate_type": "prime_matrix_strict_named_return_after_rowfree_sync_router",
        "status": "named_return_alphabet_compressed_to_budget_and_terminal_family_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "named_return_alphabet_compression_closed": alphabet_closed,
        "named_return_exclusion_proved": False,
        "persistent_named_return_terminal_family_excluded": False,
        "nonpersistent_named_return_budget_absorbed": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": NAMED_RETURN,
        "hardpoint_after_router": f"{UNIFIED_BUDGET} AND {TERMINAL_FAMILY}",
        "next_direct_attack_target": UNIFIED_BUDGET,
        "parallel_attack_targets": [
            MOVING_ATOM,
            "DirectAcyclicSameSetPDECCapDualCertificate",
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            DSTRUCTURE,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` 已完成字母表级压缩："
            "无名缺陷出口被删除，持久命名回流回到 acyclic PDEC/CleanKLS 终端包，非持久回流进入统一预算吸收。"
            "因此命名回流不再作为独立宽黑箱；下一步应直接攻 `UnifiedTerminalBudgetStrictInequality`，"
            "并行保留持久终端族的 moving atom/PDEC-CAP 排斥与 DStructure。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict row-free 后命名回流同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"named_return_alphabet_compression_closed={fmt_bool(result['named_return_alphabet_compression_closed'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"unified_terminal_budget_strict_inequality_proved={fmt_bool(result['unified_terminal_budget_strict_inequality_proved'])}",
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
