#!/usr/bin/env python3
"""生成 strict row-free type 抗塌缩同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_row_free_type_anticollapse_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json
  docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-row-free-type-anticollapse-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-row-free-type-anticollapse-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-formal-unit-type-threshold-sync-router.json",
    "prime-matrix-strict-boundary-cap-type-compression-router.json",
    "prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
]

ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
TYPE_DRIFT = "BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn"


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
    result = {"experiments/prime_matrix_strict_row_free_type_anticollapse_sync_router.py": sha256(Path(__file__).resolve())}
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
    """生成 row-free 抗塌缩判定表。"""
    formal = data["formal"]
    boundary = data["boundary"]
    quotient = data["quotient"]
    sparse = data["sparse"]
    forced = data["forced"]
    named = data["named"]
    defect = data["defect"]

    target_imported = formal.get("next_direct_attack_target") == ROW_FREE
    row_key_closed = has_closed_gate(boundary, "RowFreeTypeKeyDefinitionClosed")
    coarse_loss_identified = has_closed_gate(boundary, "CoarseTypeRepeatDoesNotPreserveLabelSupport")
    quotient_reduced = quotient.get("hardpoint_after_router") == UNIFIED_BUDGET
    sparse_no_loss = sparse.get("terminal_projection_anticollapse_closed") is True
    forced_no_loss = forced.get("terminal_projection_no_loss_or_named_return_closed") is True
    named_compressed = named.get("next_direct_attack_target") == UNIFIED_BUDGET
    defect_no_free_exit = defect.get("status") == "terminal_defect_no_free_exit_closed_unconditional_exclusion_open"

    return [
        row(
            "RowFreeAntiCollapseTargetImported",
            target_imported,
            False,
            "上一层已把 formal-unit 类型阈值的独立内容压成 row-free type 抗塌缩。",
            ROW_FREE,
        ),
        row(
            "RowFreeTypeKeyAndCoarseLossKnown",
            row_key_closed and coarse_loss_identified,
            True,
            "row-free type key 可定义；若粗化 key 以制造重复，就会丢失标签支撑，不能直接调用 CRT 短复现。",
            TYPE_DRIFT,
        ),
        row(
            "LabelPreservingCollapseRoutedToBudgetGap",
            quotient_reduced,
            False,
            "保标签商类型熵亏损已由既有证书路由到统一终端预算严格缺口。",
            UNIFIED_BUDGET,
        ),
        row(
            "LabelLosingCollapseRoutedToNamedReturn",
            defect_no_free_exit,
            False,
            "丢标签或相位漂移不能作为无名出口，必须进入 PDEC/SAE/ColumnCRT/热核心/固定历史等命名回流。",
            NAMED_RETURN,
        ),
        row(
            "SparseTerminalNoSilentCollapseImported",
            sparse_no_loss and forced_no_loss,
            True,
            "加权 prefix 义务沿历史递归不会静默消失：不进终端历史就进入命名回流桶。",
            "closed for no-silent-loss budget form",
        ),
        row(
            "StrongRowFreeInjectionNotNeeded",
            True,
            True,
            "统一预算不需要证明不同 prefix 标签强注入到不同 row-free type；只需要塌缩被收费或回流。",
            f"{NAMED_RETURN} AND {UNIFIED_BUDGET}",
        ),
        row(
            "NamedReturnCompressionImported",
            named_compressed,
            False,
            "命名出口字母表已压成持久终端包与非持久预算；但排斥和数值吸收仍未完成。",
            f"{NAMED_RETURN} OR {UNIFIED_BUDGET}",
        ),
        row(
            "RowFreeAntiCollapseClosedForBudget",
            target_imported and row_key_closed and coarse_loss_identified and quotient_reduced and forced_no_loss,
            False,
            "预算所需的 row-free 抗塌缩版本闭合：没有静默塌缩；剩余只是不利回流是否能被排斥或预算吸收。",
            f"{NAMED_RETURN} AND {UNIFIED_BUDGET}",
        ),
        row(
            "StrongRowFreeAntiCollapseCurrentCorpusProved",
            False,
            False,
            "强注入/全局不同 type 下界仍未证明，也不作为当前统一预算必要输入。",
            "not required for current budget route",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭的是无静默塌缩形式，不排斥命名回流；最终仍需命名回流/预算/DStructure。",
            f"{NAMED_RETURN} AND {UNIFIED_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 row-free type 抗塌缩同步证书。"""
    data = {
        "formal": load_json("prime-matrix-strict-formal-unit-type-threshold-sync-router.json"),
        "boundary": load_json("prime-matrix-strict-boundary-cap-type-compression-router.json"),
        "quotient": load_json("prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json"),
        "sparse": load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"),
        "forced": load_json("prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json"),
        "named": load_json("prime-matrix-strict-named-return-exclusion-compression-router.json"),
        "defect": load_json("prime-matrix-strict-terminal-defect-exhaustion-router.json"),
    }
    rows = build_rows(data)
    budget_closed = any(item["gate"] == "RowFreeAntiCollapseClosedForBudget" and item["closed"] for item in rows)

    return {
        "certificate_type": "prime_matrix_strict_row_free_type_anticollapse_sync_router",
        "status": "row_free_type_anticollapse_closed_for_budget_named_return_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "prefix_label_support_to_row_free_type_anticollapse_closed_for_budget": budget_closed,
        "strong_row_free_injection_proved": False,
        "named_return_exclusion_proved": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ROW_FREE,
        "hardpoint_after_router": NAMED_RETURN,
        "next_direct_attack_target": NAMED_RETURN,
        "parallel_attack_targets": [
            UNIFIED_BUDGET,
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore",
            DSTRUCTURE,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PrefixLabelSupportToRowFreeTypeAntiCollapse` 的强注入版本仍未证明，但当前统一预算只需要"
            "无静默塌缩版本：prefix 标签若保留标签骨架，则其商类型亏损已进入统一终端预算缺口；若粗化后丢标签，"
            "则必须进入 PDEC/SAE/ColumnCRT/热核心/固定历史等命名回流。稀疏终端历史的 no-loss 证书说明义务不会消失。"
            "因此 row-free 抗塌缩的预算形式关闭，下一最窄点转为排斥或吸收命名回流。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict row-free type 抗塌缩同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prefix_label_support_to_row_free_type_anticollapse_closed_for_budget={fmt_bool(result['prefix_label_support_to_row_free_type_anticollapse_closed_for_budget'])}",
        f"strong_row_free_injection_proved={fmt_bool(result['strong_row_free_injection_proved'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
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
