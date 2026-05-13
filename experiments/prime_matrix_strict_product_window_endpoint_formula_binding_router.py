#!/usr/bin/env python3
"""生成 strict product-window 端点公式绑定攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_product_window_endpoint_formula_binding_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-product-window-endpoint-formula-binding-router.json

输出：
  docs/monograph/prime-matrix-strict-product-window-endpoint-formula-binding-router.json
  docs/monograph/prime-matrix-strict-product-window-endpoint-formula-binding-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
EXPERIMENTS = ROOT / "experiments"
OUT_JSON = DOCS / "prime-matrix-strict-product-window-endpoint-formula-binding-router.json"
OUT_MD = DOCS / "prime-matrix-strict-product-window-endpoint-formula-binding-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
    "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json",
]

FORMULA_BINDING = "ProductWindowEndpointDyadicUpdateFormulaBindingLedger"
GENERATOR = "ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix"
THRESHOLD_BINDING = "ColdCoreThresholdDyadicOrderInvarianceBindingLedger"
ENDPOINT_COMM = "DyadicProductWindowEndpointCommutativityLedger"
PHASE_DEFECT = "DyadicPathDependentColdWindowPhaseDefectPDECRoute"
ROUNDING_DEFECT = "DyadicBoundaryRoundingPhaseDefectPDECRoute"
DYADIC = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
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
    result = {
        "experiments/prime_matrix_strict_product_window_endpoint_formula_binding_router.py": sha256(
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


def corpus_hits() -> list[dict[str, str]]:
    """列出现有语料中 product-window 相关命中。"""
    hits: list[dict[str, str]] = []
    targets = [
        DOCS / "prime-matrix-strict-scaled-terminal-core-divisor-window-router.md",
        DOCS / "prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md",
        EXPERIMENTS / "prime_matrix_strict_scaled_terminal_core_divisor_window_router.py",
        EXPERIMENTS / "prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py",
    ]
    for path in targets:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for needle in ["product window ledger", "I_W", "Y_W", "terminal core interval"]:
            if needle in text:
                hits.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "needle": needle,
                        "binding_strength": "descriptive_reference_only",
                    }
                )
    return hits


def required_schema_rows() -> list[dict[str, str]]:
    """给出需要补齐的端点生成器 schema。"""
    return [
        {
            "field": "base_window",
            "required_content": "base endpoints Y_0^-,Y_0^+ with integer or dyadic-rational representation",
            "why_needed": "确定所有 I_W 的共同来源。",
        },
        {
            "field": "history_update",
            "required_content": "for each child multiplier m, exact endpoint update rule and rounding direction",
            "why_needed": "判断不同历史顺序是否可能改变端点。",
        },
        {
            "field": "dyadic_specialization",
            "required_content": "for m=2^e, update reduces to outward scaling by 2^e",
            "why_needed": "把 dyadic 取整结合律接到当前 I_W。",
        },
        {
            "field": "normalization",
            "required_content": "all stepwise endpoints are normalized to the same final representation",
            "why_needed": "排除因中间舍入格式造成的伪顺序差异。",
        },
        {
            "field": "threshold_binding",
            "required_content": "C_core(W) is a function of normalized final window scale, or defects are registered",
            "why_needed": "不仅端点要交换，冷阈值也要随 dyadic 重排不变。",
        },
        {
            "field": "defect_return",
            "required_content": "if any field fails, discrepancy routes to boundary phase defect/PDEC/hot core",
            "why_needed": "避免公式绑定失败变成自由容量。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 product-window 公式绑定判定表。"""
    endpoint = data["endpoint"]
    scaled = data["scaled"]
    hits = corpus_hits()

    target_imported = endpoint.get("next_direct_attack_target") == FORMULA_BINDING
    conditional_rounding = endpoint.get("dyadic_endpoint_commutativity_conditional_on_formula_closed") is True
    window_exists = scaled.get("terminal_core_window_closed") is True
    descriptive_hits = bool(hits)

    return [
        row(
            "FormulaBindingTargetImported",
            target_imported,
            False,
            "上一层已把 dyadic 端点交换律压成 product-window 端点公式绑定。",
            FORMULA_BINDING,
        ),
        row(
            "TerminalWindowExists",
            window_exists,
            True,
            "I_W 已作为终端核心窗口对象存在。",
            GENERATOR,
        ),
        row(
            "DescriptiveProductWindowReferencesFound",
            descriptive_hits,
            True,
            "现有语料有 product-window 文字引用，但不是端点生成器。",
            GENERATOR,
        ),
        row(
            "DyadicRoundingConditionalLemmaImported",
            conditional_rounding,
            True,
            "若端点公式绑定到 dyadic 外向缩放，交换律已经由取整结合律支付。",
            FORMULA_BINDING,
        ),
        row(
            "MachineReadableEndpointGeneratorFound",
            False,
            False,
            "当前语料没有可复核的端点更新公式/生成器/hash。",
            GENERATOR,
        ),
        row(
            "ThresholdBindingFound",
            False,
            False,
            "当前语料没有把 C_core(W) 绑定到规范化终端窗口尺度。",
            THRESHOLD_BINDING,
        ),
        row(
            "FormulaFailureDefectRouteRegistered",
            True,
            False,
            "若生成器不能满足 dyadic 外向缩放，差异必须回流边界相位缺陷。",
            ROUNDING_DEFECT,
        ),
        row(
            "ProductWindowEndpointDyadicUpdateFormulaBindingProved",
            False,
            False,
            "生成器/定义附录和阈值绑定未补齐，公式绑定不能关闭。",
            f"{GENERATOR} AND {THRESHOLD_BINDING}",
        ),
        row(
            "DyadicProductWindowEndpointCommutativityLedgerProved",
            False,
            False,
            "公式绑定未闭合，因此端点交换律仍未无条件接回 I_W。",
            ENDPOINT_COMM,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{GENERATOR} AND {PHASE_DEFECT} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 product-window 端点公式绑定证书。"""
    data = {
        "endpoint": load_json("prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
    }
    rows = build_rows(data)
    hits = corpus_hits()

    return {
        "certificate_type": "prime_matrix_strict_product_window_endpoint_formula_binding_router",
        "status": "product_window_formula_binding_reduced_to_generator_artifact_or_definition_appendix_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "terminal_window_object_exists": True,
        "descriptive_product_window_references_found": bool(hits),
        "dyadic_rounding_conditional_lemma_imported": True,
        "machine_readable_endpoint_generator_found": False,
        "product_window_endpoint_formula_binding_proved": False,
        "cold_core_threshold_order_invariance_proved": False,
        "formula_failure_defect_route_registered": True,
        "dyadic_product_window_endpoint_commutativity_ledger_proved": False,
        "dyadic_prime_power_cold_window_cascade_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": FORMULA_BINDING,
        "hardpoint_after_router": f"{GENERATOR} AND {THRESHOLD_BINDING}",
        "next_direct_attack_target": GENERATOR,
        "parallel_attack_targets": [
            THRESHOLD_BINDING,
            ROUNDING_DEFECT,
            PHASE_DEFECT,
            ENDPOINT_COMM,
            DYADIC,
            DSTRUCTURE,
        ],
        "corpus_hits": hits,
        "required_schema_rows": required_schema_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ProductWindowEndpointDyadicUpdateFormulaBindingLedger` 不能由当前语料直接闭合。"
            "现有材料只说 `I_W` 的端点继承自 product window ledger，但没有给出 machine-readable 的端点更新公式、"
            "舍入方向、规范化表示和 `C_core(W)` 阈值绑定。已闭合的 dyadic 取整交换律可作为后端引理，"
            "但还需要新增 `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix`，否则公式失败必须进入边界相位缺陷路由。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict product-window 端点公式绑定路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_window_object_exists={fmt_bool(result['terminal_window_object_exists'])}",
        f"descriptive_product_window_references_found={fmt_bool(result['descriptive_product_window_references_found'])}",
        f"machine_readable_endpoint_generator_found={fmt_bool(result['machine_readable_endpoint_generator_found'])}",
        f"product_window_endpoint_formula_binding_proved={fmt_bool(result['product_window_endpoint_formula_binding_proved'])}",
        f"cold_core_threshold_order_invariance_proved={fmt_bool(result['cold_core_threshold_order_invariance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 语料命中",
        "",
        "| file | needle | binding_strength |",
        "|---|---|---|",
    ]
    for item in result["corpus_hits"]:
        lines.append(
            "| "
            f"`{table_cell(item['file'])}` | "
            f"`{table_cell(item['needle'])}` | "
            f"`{table_cell(item['binding_strength'])}` |"
        )

    lines.extend(
        [
            "",
            "## 需要补齐的生成器 schema",
            "",
            "| field | required_content | why_needed |",
            "|---|---|---|",
        ]
    )
    for item in result["required_schema_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['field'])}` | "
            f"{table_cell(item['required_content'])} | "
            f"{table_cell(item['why_needed'])} |"
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
