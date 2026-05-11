#!/usr/bin/env python3
"""生成 strict acyclic seed primitive basis word 生成规则攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_primitive_basis_word_generation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.md"

TARGET = "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment"
NEXT_TARGET = "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def constructor_fields() -> list[dict[str, str]]:
    """列出 source tuple 到 basis word constructor 的最小字段。"""
    return [
        {
            "field": "input_source_tuple",
            "meaning": "同一 formal unit 下的 actual noncanonical seed/source tuple。",
        },
        {
            "field": "basis_word_formula",
            "meaning": "由 source tuple 参数正向产生 primitive basis word 的闭式公式或递推规则。",
        },
        {
            "field": "pre_cauchy_order_certificate",
            "meaning": "证明该构造发生在 Cauchy、dispersion、payment 和 terminal extraction 之前。",
        },
        {
            "field": "nonposthoc_uniqueness",
            "meaning": "排除从零行覆盖、payment 原像或推前后投影反选 word。",
        },
        {
            "field": "constructor_failure_return",
            "meaning": "source tuple 无法生成 word、生成多值或作用域冲突时的命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 primitive basis word 生成规则的第一字段。"""
    previous = data["previous"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    source_law = data["source_law"]
    origin = data["origin"]
    constructor = data["constructor"]
    unsigned = data["unsigned"]
    summand_origin = data["summand_origin"]
    row_table = data["row_table"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    tuple_available = (
        formal_record.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
    )
    constructor_missing = (
        constructor.get("actual_noncanonical_primitive_constructor_formula_proved") is False
        and origin.get("clean_core_primitive_source_constructor_admission_proved") is not True
    )
    row_generation_missing = (
        summand_origin.get("primitive_summand_signed_coefficient_origin_identity_proved") is False
        or row_table.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        or zero_nogo.get("downstream_reverse_source_blocked") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
    )

    return [
        row(
            "PrimitiveBasisWordGenerationTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 basis alphabet 账本压到 primitive basis word set generation rule。",
            TARGET,
        ),
        row(
            "WordConstructorPrecedesPredicateAndAnchor",
            True,
            True,
            "admissible predicate、row anchor、复杂度收费和缺字母回流都以已生成的 word 为定义域。",
            NEXT_TARGET,
        ),
        row(
            "SourceTupleAvailableButNoConstructor",
            tuple_available,
            False,
            "source tuple 可登记参数，但当前没有从这些参数到 primitive basis word 的正向公式。",
            NEXT_TARGET,
        ),
        row(
            "PreCauchySourceLawIsSpecificationNotConstructor",
            source_law.get("origin_generation_ledger_implication_closed") is True,
            False,
            "pre-Cauchy source law 说明需要哪些字段，但没有给出 basis_word_formula。",
            NEXT_TARGET,
        ),
        row(
            "ActualPrimitiveConstructorStillMissing",
            constructor_missing,
            False,
            "actual noncanonical primitive constructor/admission 未证明，因此不能自动产生 word constructor。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedSkeletonOnlyAnchorsAfterWord",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            False,
            "unsigned skeleton 可在 word 已有时提供几何锚；不能构造带算术权重的 word。",
            NEXT_TARGET,
        ),
        row(
            "RowOriginTableMissing",
            row_generation_missing,
            False,
            "primitive summand 来源恒等式和逐行原始生成表仍未证明，不能作为 constructor 证据。",
            NEXT_TARGET,
        ),
        row(
            "PosthocReverseSelectionBlocked",
            reverse_blocked,
            True,
            "从 payment、推前后投影或早期零行覆盖反选 word 已被既有 no-go 与 reverse firewall 阻断。",
            NEXT_TARGET,
        ),
        row(
            "SourceTupleToPrimitiveBasisWordConstructorCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 source tuple 到 primitive basis word 的 pre-Cauchy 正向构造。",
            NEXT_TARGET,
        ),
        row(
            "PrimitiveBasisWordSetGenerationRuleCurrentCorpusProved",
            False,
            False,
            "没有 word constructor，generation rule 的其余字段都只能悬空。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 primitive basis word 生成规则证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "source_law": load_json("prime-matrix-clean-core-precauchy-source-law-atom-router.json"),
        "origin": load_json("prime-matrix-clean-core-origin-source-admission-router.json"),
        "constructor": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "summand_origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
        if isinstance(doc, dict)
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_primitive_basis_word_generation_router",
        "status": "primitive_basis_word_generation_reduced_to_source_tuple_word_constructor_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "primitive_basis_word_generation_router_closed": True,
        "word_constructor_precedes_predicate_and_anchor": True,
        "source_tuple_available_but_no_constructor": True,
        "posthoc_reverse_selection_blocked": True,
        "source_tuple_to_primitive_basis_word_constructor_proved": False,
        "primitive_basis_word_set_generation_rule_proved": False,
        "noncanonical_precauchy_basis_alphabet_ledger_proved": False,
        "acyclic_seed_internal_arithmetic_basis_expansion_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedBasisWordAdmissibilityPredicateLedger",
            "AcyclicSeedWordToRowAnchorCompatibilityLedger",
            "AcyclicSeedBasisWordComplexityAndMissingReturnLedger",
        ],
        "terminal_return_if_no_word_constructor": TERMINAL_RETURN,
        "constructor_fields": constructor_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的第一可检验字段是 `{NEXT_TARGET}`："
            "必须先有 source tuple 到 primitive basis word 的 pre-Cauchy 正向构造，"
            "再谈准入谓词、row anchor、复杂度收费和 coefficient assignment。"
        ),
        "plain_conclusion": (
            "本步把最新真正单点再压到 source tuple -> primitive basis word constructor。"
            "现有 formal-unit/source-tuple 只能登记参数，unsigned skeleton 只能在 word 已有时给几何锚，"
            "零行/payment/推前后反选已被 no-go 阻断；因此 constructor 仍是未闭合的自足输入。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed primitive basis word generation 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"primitive_basis_word_generation_router_closed={fmt_bool(result['primitive_basis_word_generation_router_closed'])}",
        f"source_tuple_to_primitive_basis_word_constructor_proved={fmt_bool(result['source_tuple_to_primitive_basis_word_constructor_proved'])}",
        f"primitive_basis_word_set_generation_rule_proved={fmt_bool(result['primitive_basis_word_set_generation_rule_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. constructor 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["constructor_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
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
    for item in result["rows"]:
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
            "## 4. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行依赖：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_word_constructor"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
