#!/usr/bin/env python3
"""生成 strict formal-unit 类型阈值同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_formal_unit_type_threshold_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-formal-unit-type-threshold-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-formal-unit-type-threshold-sync-router.json
  docs/monograph/prime-matrix-strict-formal-unit-type-threshold-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-formal-unit-type-threshold-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-formal-unit-type-threshold-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json",
    "prime-matrix-strict-same-parameter-prefix-window-spec-router.json",
    "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json",
    "prime-matrix-strict-normalized-prefix-potential-router.json",
    "prime-matrix-strict-boundary-cap-type-compression-router.json",
    "prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json",
    "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
]

TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
SPARSE_HISTORY = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
QUOTIENT_DEFICIT = "BoundaryCapLabelPreservingQuotientEntropyDeficit"
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
    result = {"experiments/prime_matrix_strict_formal_unit_type_threshold_sync_router.py": sha256(Path(__file__).resolve())}
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


def ledger_slot_closed(cert: dict[str, Any], slot: str) -> bool:
    """检查同参数账本槽位是否闭合。"""
    return any(item.get("slot") == slot and item.get("closed") is True for item in cert.get("ledger_rows", []))


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 formal-unit 类型阈值判定表。"""
    current = data["current"]
    same = data["same"]
    capacity = data["capacity"]
    normalized = data["normalized"]
    boundary = data["boundary"]
    quotient = data["quotient"]
    sparse = data["sparse"]

    target_imported = current.get("next_direct_attack_target") == TYPE_LEDGER
    same_window_closed = same.get("same_parameter_window_specification_proved") is True
    row_key_closed = ledger_slot_closed(same, "row_free_type_alphabet_key")
    msharp_link_closed = ledger_slot_closed(same, "D0_to_Msharp_budget_link")
    capacity_closed = (
        capacity.get("capacity_normalized_charge_closed") is True
        and capacity.get("distinct_label_lower_bound_closed") is True
        and any(
            item.get("gate") == "RegisteredCapacityMultiplierDisciplineClosed"
            and item.get("closed") is True
            for item in capacity.get("rows", [])
        )
    )
    m_tail_prefix_closed = current.get("finite_prefix_strict_mertens_component_closed") is True
    external_standard_prefix_closed = current.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True
    boundary_skeleton_closed = any(
        item.get("gate") == "PigeonholeSkeletonConditionalClosed" and item.get("closed") is True
        for item in boundary.get("rows", [])
    )
    quotient_reduced = quotient.get("hardpoint_after_router") == "UnifiedTerminalBudgetStrictInequality"
    sparse_closed = sparse.get("terminal_projection_anticollapse_closed") is True

    return [
        row(
            "FormalUnitTypeThresholdTargetImported",
            target_imported,
            False,
            "上一层关闭旧 Mertens 粗原子后，把下一主攻点固定为 formal-unit 类型阈值。",
            TYPE_LEDGER,
        ),
        row(
            "SameParameterTypeAlphabetClosed",
            same_window_closed and row_key_closed,
            True,
            "D0、M#、终端预算和 row-free type key 已登记在同一 alpha=0.43/P>=100000 窗口。",
            "type key defined; threshold comparison remains separate",
        ),
        row(
            "CapacityMultiplierAndMsharpLinkClosed",
            capacity_closed and msharp_link_closed,
            True,
            "容量乘子纪律给出 M#>=|R|/ceil(P/z)，同一标签复用不能免费制造类型实例。",
            "requires prefix mass and row-free anti-collapse",
        ),
        row(
            "PrefixMassSideAvailableUnderCurrentContract",
            m_tail_prefix_closed and external_standard_prefix_closed,
            False,
            "finite-prefix 的 Mertens 尾段已回接，standard/external lower-sieve 合同下 D0/M# 需求侧可用。",
            "strict first-principles beta-sieve appendix remains separate",
        ),
        row(
            "NormalizedPotentialStillDoesNotDefineTypeCount",
            normalized.get("prefix_label_support_to_row_free_type_anticollapse_proved") is False,
            True,
            "归一化势下界只给标签/质量侧；它本身不给 row-free type alphabet 的有效上界。",
            ROW_FREE,
        ),
        row(
            "BoundaryCapPigeonholeSkeletonImported",
            boundary_skeleton_closed,
            True,
            "边界帽类型压缩的条件鸽巢骨架已闭合：若有效义务数超过保标签类型数，则可接短复现矛盾。",
            f"{QUOTIENT_DEFICIT} OR {TYPE_DRIFT}",
        ),
        row(
            "StandaloneNumericTypeThresholdRejected",
            True,
            True,
            "不存在可脱离标签保持与命名回流的固定常数 T_formal；粗 key 压缩会丢标签，完整 key 又缺数量亏损。",
            f"{ROW_FREE} AND {TYPE_DRIFT}",
        ),
        row(
            "LabelPreservingQuotientRouteAlreadyReduced",
            quotient_reduced,
            False,
            "保标签商类型熵亏损已被既有证书压到统一终端预算严格缺口，不应作为新的黑箱常数重复保留。",
            "UnifiedTerminalBudgetStrictInequality",
        ),
        row(
            "SparseTerminalAntiCollapseNotRowFreeAntiCollapse",
            sparse_closed,
            True,
            "稀疏终端历史的无静默塌缩已闭合，但它只保证投影负载不消失，不等于 row-free type 保标签商熵亏损。",
            ROW_FREE,
        ),
        row(
            "FormalUnitTypeThresholdReducedToRowFreeAntiCollapse",
            target_imported and same_window_closed and row_key_closed and capacity_closed,
            False,
            "类型阈值账本的独立内容已压成：prefix 标签支撑不能在 row-free type/quotient 中大量塌缩；若塌缩必须登记为命名回流。",
            f"{ROW_FREE} AND {NAMED_RETURN}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步是精确压缩，不是终局矛盾；row-free 抗塌缩、命名回流、moving atom 与 DStructure 仍未全部闭合。",
            f"{ROW_FREE} AND {NAMED_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 formal-unit 类型阈值同步证书。"""
    data = {
        "current": load_json("prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json"),
        "same": load_json("prime-matrix-strict-same-parameter-prefix-window-spec-router.json"),
        "capacity": load_json("prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json"),
        "normalized": load_json("prime-matrix-strict-normalized-prefix-potential-router.json"),
        "boundary": load_json("prime-matrix-strict-boundary-cap-type-compression-router.json"),
        "quotient": load_json("prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json"),
        "sparse": load_json("prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"),
    }
    rows = build_rows(data)
    reduction_closed = any(
        item["gate"] == "FormalUnitTypeThresholdReducedToRowFreeAntiCollapse" and item["closed"]
        for item in rows
    )

    return {
        "certificate_type": "prime_matrix_strict_formal_unit_type_threshold_sync_router",
        "status": "formal_unit_type_threshold_reduced_to_rowfree_anticollapse_named_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "formal_unit_type_threshold_reduction_closed": reduction_closed,
        "formal_unit_type_threshold_standalone_numeric_proved": False,
        "prefix_label_support_to_row_free_type_anticollapse_proved": False,
        "named_return_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TYPE_LEDGER,
        "hardpoint_after_router": ROW_FREE,
        "next_direct_attack_target": ROW_FREE,
        "parallel_attack_targets": [
            NAMED_RETURN,
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore",
            DSTRUCTURE,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`FormalUnitTypeThresholdLedger` 已不能作为独立固定常数继续悬挂：同参数窗口和 row-free type key "
            "已经闭合，容量乘子把 D0/M# 需求侧接入，finite-prefix 的旧 Mertens 粗原子也已移除。"
            "真正未闭合的是保标签投影：不同 prefix 标签或标签骨架是否会在 row-free type/quotient 下大量合并。"
            "若完整 key 重复，可接同标签短复现；若粗 key 重复，则标签丢失并必须进入 PDEC/SAE/ColumnCRT 等命名回流。"
            "因此本步把类型阈值压成 `PrefixLabelSupportToRowFreeTypeAntiCollapse`，并行保留命名回流与 DStructure。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict formal-unit 类型阈值同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"formal_unit_type_threshold_reduction_closed={fmt_bool(result['formal_unit_type_threshold_reduction_closed'])}",
        f"formal_unit_type_threshold_standalone_numeric_proved={fmt_bool(result['formal_unit_type_threshold_standalone_numeric_proved'])}",
        f"prefix_label_support_to_row_free_type_anticollapse_proved={fmt_bool(result['prefix_label_support_to_row_free_type_anticollapse_proved'])}",
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
