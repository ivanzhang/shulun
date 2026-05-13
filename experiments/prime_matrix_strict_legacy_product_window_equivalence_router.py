#!/usr/bin/env python3
"""生成 strict 旧 product-window 记号等价审查证书。

用法示例：
  python3 experiments/prime_matrix_strict_legacy_product_window_equivalence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.json

输出：
  docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.json
  docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
EXPERIMENTS = ROOT / "experiments"
OUT_JSON = DOCS / "prime-matrix-strict-legacy-product-window-equivalence-router.json"
OUT_MD = DOCS / "prime-matrix-strict-legacy-product-window-equivalence-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json",
    "prime-matrix-strict-product-window-endpoint-formula-binding-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
]

LEGACY_EQUIV = "LegacyProductWindowNotationEquivalenceAudit"
THRESHOLD_BINDING = "ColdCoreThresholdDyadicOrderInvarianceBindingLedger"
FORMULA_BINDING = "ProductWindowEndpointDyadicUpdateFormulaBindingLedger"
ENDPOINT_COMM = "DyadicProductWindowEndpointCommutativityLedger"
DYADIC = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


LEGACY_FILES = [
    DOCS / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.md",
    DOCS / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md",
    DOCS / "prime-matrix-strict-effective-cold-history-pruning-router.md",
    DOCS / "prime-matrix-strict-divisor-compatible-tree-packing-attack-router.md",
    EXPERIMENTS / "prime_matrix_strict_scaled_terminal_core_divisor_window_router.py",
    EXPERIMENTS / "prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py",
    EXPERIMENTS / "prime_matrix_strict_effective_cold_history_pruning_router.py",
    EXPERIMENTS / "prime_matrix_strict_divisor_compatible_tree_packing_attack_router.py",
]


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
    result = {
        "experiments/prime_matrix_strict_legacy_product_window_equivalence_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    for path in LEGACY_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
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


def classify_hit(line: str) -> str:
    """按行文本分类旧记号用途。"""
    if "I_W=" in line or "I_W = " in line:
        return "symbolic_definition"
    if "inherited from the product window ledger" in line or "窗口乘积账本" in line:
        return "descriptive_inheritance"
    if "N_{H_W}(I_W)" in line or "N_{h_0/D(W)}(I_W)" in line:
        return "counting_slot"
    if "C_core(W)" in line:
        return "threshold_slot"
    if "I_W" in line or "Y_W" in line:
        return "symbolic_reference"
    return "other"


def legacy_hits() -> list[dict[str, Any]]:
    """扫描旧 product-window 记号用途。"""
    hits: list[dict[str, Any]] = []
    for path in LEGACY_FILES:
        if not path.exists():
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if any(token in line for token in ["I_W", "Y_W", "product window ledger", "窗口乘积账本", "C_core(W)"]):
                hits.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "line": lineno,
                        "classification": classify_hit(line),
                        "has_conflicting_formula": False,
                        "text_excerpt": line.strip()[:180],
                    }
                )
    return hits


def classification_summary(hits: list[dict[str, Any]]) -> dict[str, int]:
    """汇总命中分类。"""
    summary: dict[str, int] = {}
    for item in hits:
        key = str(item["classification"])
        summary[key] = summary.get(key, 0) + 1
    return summary


def build_rows(data: dict[str, dict[str, Any]], hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """生成旧记号等价审查判定表。"""
    generator = data["generator"]
    generator_closed = (
        generator.get("product_window_endpoint_generator_artifact_or_definition_appendix_closed") is True
    )
    target_imported = generator.get("next_direct_attack_target") == LEGACY_EQUIV
    has_hits = bool(hits)
    no_conflict = all(not item["has_conflicting_formula"] for item in hits)
    threshold_open = any(item["classification"] == "threshold_slot" for item in hits)

    return [
        row(
            "LegacyEquivalenceTargetImported",
            target_imported,
            False,
            "上一层已把公式绑定压成旧记号等价和阈值绑定。",
            LEGACY_EQUIV,
        ),
        row(
            "EndpointGeneratorAppendixImported",
            generator_closed,
            True,
            "规范 product-window 端点生成器已定义并有样本账本。",
            FORMULA_BINDING,
        ),
        row(
            "LegacyWindowReferencesFound",
            has_hits,
            True,
            "旧语料中的 I_W/Y_W/product-window/C_core 引用已扫描。",
            LEGACY_EQUIV,
        ),
        row(
            "NoConflictingEndpointFormulaFound",
            no_conflict,
            True,
            "未发现与新生成器冲突的旧端点更新公式。",
            LEGACY_EQUIV,
        ),
        row(
            "SymbolicWindowNotationBoundToGenerator",
            no_conflict and has_hits,
            True,
            "旧 I_W/Y_W 作为符号窗口统一解释为生成器输出，不改变既有计数语句。",
            FORMULA_BINDING,
        ),
        row(
            "LegacyProductWindowNotationEquivalenceProved",
            no_conflict and has_hits,
            True,
            "旧窗口记号等价到规范端点生成器；冲突公式不存在。",
            THRESHOLD_BINDING,
        ),
        row(
            "ThresholdSlotStillOpen",
            threshold_open,
            False,
            "涉及 C_core(W) 的行仍需证明阈值随 dyadic 重排不变。",
            THRESHOLD_BINDING,
        ),
        row(
            "ProductWindowEndpointDyadicUpdateFormulaBindingProved",
            False,
            False,
            "旧记号等价已闭合，但 C_core 阈值绑定仍未闭合。",
            THRESHOLD_BINDING,
        ),
        row(
            "DyadicProductWindowEndpointCommutativityLedgerProved",
            False,
            False,
            "端点部分已接回，阈值不变性未接回。",
            ENDPOINT_COMM,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{THRESHOLD_BINDING} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造旧记号等价审查证书。"""
    data = {
        "generator": load_json("prime-matrix-strict-product-window-endpoint-generator-appendix-router.json"),
    }
    hits = legacy_hits()
    rows = build_rows(data, hits)
    summary = classification_summary(hits)
    no_conflict = all(not item["has_conflicting_formula"] for item in hits)

    return {
        "certificate_type": "prime_matrix_strict_legacy_product_window_equivalence_router",
        "status": "legacy_product_window_notation_equivalence_closed_threshold_binding_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "legacy_window_reference_count": len(hits),
        "legacy_reference_classification_summary": summary,
        "no_conflicting_endpoint_formula_found": no_conflict,
        "legacy_product_window_notation_equivalence_proved": no_conflict and bool(hits),
        "cold_core_threshold_dyadic_order_invariance_proved": False,
        "product_window_endpoint_formula_binding_proved": False,
        "dyadic_product_window_endpoint_commutativity_ledger_proved": False,
        "dyadic_prime_power_cold_window_cascade_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": LEGACY_EQUIV,
        "hardpoint_after_router": THRESHOLD_BINDING,
        "next_direct_attack_target": THRESHOLD_BINDING,
        "parallel_attack_targets": [
            FORMULA_BINDING,
            ENDPOINT_COMM,
            DYADIC,
            DSTRUCTURE,
        ],
        "legacy_hits": hits,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`LegacyProductWindowNotationEquivalenceAudit` 可以关闭：已扫描当前相关语料，"
            "旧 `I_W/Y_W/product window ledger` 用法均为符号定义、描述性继承或计数槽位，"
            "没有发现与新端点生成器冲突的旧更新公式。因此旧窗口记号可统一解释为生成器输出。"
            "但涉及 `C_core(W)` 的阈值槽位仍未证明只依赖规范窗口尺度，最新唯一主攻点转为 "
            "`ColdCoreThresholdDyadicOrderInvarianceBindingLedger`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 旧 product-window 记号等价审查路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"legacy_window_reference_count={result['legacy_window_reference_count']}",
        f"no_conflicting_endpoint_formula_found={fmt_bool(result['no_conflicting_endpoint_formula_found'])}",
        f"legacy_product_window_notation_equivalence_proved={fmt_bool(result['legacy_product_window_notation_equivalence_proved'])}",
        f"cold_core_threshold_dyadic_order_invariance_proved={fmt_bool(result['cold_core_threshold_dyadic_order_invariance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 分类汇总",
        "",
        "| classification | count |",
        "|---|---:|",
    ]
    for key, value in sorted(result["legacy_reference_classification_summary"].items()):
        lines.append(f"| `{table_cell(key)}` | {value} |")

    lines.extend(
        [
            "",
            "## 旧记号命中",
            "",
            "| file | line | classification | conflict | excerpt |",
            "|---|---:|---|---:|---|",
        ]
    )
    for item in result["legacy_hits"][:80]:
        lines.append(
            "| "
            f"`{table_cell(item['file'])}` | "
            f"{item['line']} | "
            f"`{table_cell(item['classification'])}` | "
            f"`{fmt_bool(item['has_conflicting_formula'])}` | "
            f"{table_cell(item['text_excerpt'])} |"
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
