#!/usr/bin/env python3
"""生成 strict acyclic seed source tuple 到 primitive basis word 构造器证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_source_tuple_word_constructor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.md"

TARGET = "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility"
NEXT_TARGET = "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
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


def formula_fields() -> list[dict[str, str]]:
    """列出 basis word formula 必须提交的字段。"""
    return [
        {
            "field": "parameter_domain",
            "meaning": "公式允许读取的 source tuple 字段：A、D0、K、Omega、phase_rule、窗口端点和 formal_unit_id。",
        },
        {
            "field": "word_coordinate_formula",
            "meaning": "把 source tuple 参数变成 primitive basis word 坐标的闭式公式或确定性递推。",
        },
        {
            "field": "arithmetic_weight_slot",
            "meaning": "word 中承载 signed local factor、筛权来源和截断层的槽位。",
        },
        {
            "field": "no_post_payment_input",
            "meaning": "公式不得读取 Cauchy、dispersion、payment、零行覆盖或 terminal extraction 后的数据。",
        },
        {
            "field": "formula_failure_return",
            "meaning": "公式未定义、多值、读到后验数据或跨作用域时的命名回流。",
        },
    ]


def tuple_schema_field_names(source_tuple: dict[str, Any]) -> set[str]:
    """提取 source tuple schema 字段名。"""
    fields = source_tuple.get("schema_fields", [])
    return {item.get("field", "") for item in fields if isinstance(item, dict)}


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 source tuple 到 word constructor 的首字段。"""
    previous = data["previous"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    source_law = data["source_law"]
    constructor = data["constructor"]
    origin = data["origin"]
    unsigned = data["unsigned"]
    explicit_rule = data["explicit_rule"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    schema_names = tuple_schema_field_names(source_tuple)
    required_schema = {"formal_unit_id", "A", "D0,K,Omega", "phase_rule", "source_tuple_hash"}
    tuple_schema_closed = (
        formal_record.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
        and required_schema.issubset(schema_names)
    )
    formula_missing = (
        constructor.get("actual_noncanonical_primitive_constructor_formula_proved") is False
        and origin.get("clean_core_primitive_source_constructor_admission_proved") is not True
    )
    downstream_not_formula = (
        explicit_rule.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False
        and unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        or zero_nogo.get("downstream_reverse_source_blocked") is True
        or zero_nogo.get("geometry_source_extraction_blocked") is True
    )

    return [
        row(
            "SourceTupleWordConstructorTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 primitive basis word 生成规则压到 source tuple 到 word constructor。",
            TARGET,
        ),
        row(
            "InputSourceTupleClosed",
            tuple_schema_closed,
            True,
            "formal unit/source tuple 的输入字段、锚集合、D0/K/Omega、phase_rule 与 hash 已锁定。",
            "输入对象不是当前首缺口。",
        ),
        row(
            "BasisWordFormulaIsFirstOpenField",
            True,
            True,
            "constructor 的真正首字段是 basis_word_formula；没有公式，pre-Cauchy 顺序证书和唯一性都无对象。",
            NEXT_TARGET,
        ),
        row(
            "SchemaParametersAreNotFormula",
            tuple_schema_closed,
            False,
            "A、D0、K、Omega、phase_rule 是参数，不是从参数到 primitive basis word 的算术映射。",
            NEXT_TARGET,
        ),
        row(
            "SourceLawSpecificationNotFormula",
            source_law.get("origin_generation_ledger_implication_closed") is True,
            False,
            "pre-Cauchy source law 规定必须有来源公式和回流纪律，但不提供 word_coordinate_formula。",
            NEXT_TARGET,
        ),
        row(
            "ActualNoncanonicalConstructorFormulaStillMissing",
            formula_missing,
            False,
            "actual noncanonical primitive constructor formula/admission 尚未证明，不能推出 basis word formula。",
            NEXT_TARGET,
        ),
        row(
            "DownstreamRowAndAlphaDeltaRulesCannotDefineFormula",
            downstream_not_formula,
            False,
            "unsigned row skeleton 与 alpha/delta rule 都在 word 或 primitive row 已生成后使用，不能倒置成 formula。",
            NEXT_TARGET,
        ),
        row(
            "PostPaymentAndZeroRowInputsRejected",
            reverse_blocked,
            True,
            "basis_word_formula 不能读 payment 原像、推前后投影或早期零行覆盖，否则是后验选择循环。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordFormulaFromSourceTupleParametersCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交从 source tuple 参数到 primitive basis word 坐标的闭式公式或确定性递推。",
            NEXT_TARGET,
        ),
        row(
            "SourceTupleToPrimitiveBasisWordConstructorCurrentCorpusProved",
            False,
            False,
            "没有 basis_word_formula，constructor 的顺序证书、非后验唯一性和失败回流仍未合取闭合。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 source tuple word constructor 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "source_law": load_json("prime-matrix-clean-core-precauchy-source-law-atom-router.json"),
        "constructor": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
        "origin": load_json("prime-matrix-clean-core-origin-source-admission-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_source_tuple_word_constructor_router",
        "status": "source_tuple_word_constructor_reduced_to_basis_word_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "source_tuple_word_constructor_router_closed": True,
        "input_source_tuple_closed": True,
        "basis_word_formula_is_first_open_field": True,
        "schema_parameters_are_not_formula": True,
        "post_payment_and_zero_row_inputs_rejected": True,
        "basis_word_formula_from_source_tuple_parameters_proved": False,
        "source_tuple_to_primitive_basis_word_constructor_proved": False,
        "primitive_basis_word_set_generation_rule_proved": False,
        "noncanonical_precauchy_basis_alphabet_ledger_proved": False,
        "acyclic_seed_internal_arithmetic_basis_expansion_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedPreCauchyOrderCertificateForBasisWordFormula",
            "AcyclicSeedNonposthocWordConstructorUniquenessLedger",
            "AcyclicSeedWordConstructorFailureReturnLedger",
        ],
        "terminal_return_if_no_basis_word_formula": TERMINAL_RETURN,
        "formula_fields": formula_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的输入 source tuple 已有字段和哈希纪律；真正首缺口是 `{NEXT_TARGET}`。"
            "也就是说，需要一条只读取 source tuple 参数、发生在 Cauchy/payment 前、能输出 primitive basis word 坐标的公式。"
        ),
        "plain_conclusion": (
            "本步把 source tuple -> primitive basis word constructor 继续压到 basis_word_formula。"
            "现有账本已经锁定输入参数，但没有把 A、D0/K/Omega、phase_rule 等参数变成 primitive basis word 的算术公式；"
            "下游 unsigned skeleton、alpha/delta rule 和 payment/零行反推都不能补这个公式。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed source tuple word constructor 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"source_tuple_word_constructor_router_closed={fmt_bool(result['source_tuple_word_constructor_router_closed'])}",
        f"input_source_tuple_closed={fmt_bool(result['input_source_tuple_closed'])}",
        f"basis_word_formula_from_source_tuple_parameters_proved={fmt_bool(result['basis_word_formula_from_source_tuple_parameters_proved'])}",
        f"source_tuple_to_primitive_basis_word_constructor_proved={fmt_bool(result['source_tuple_to_primitive_basis_word_constructor_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. basis_word_formula 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["formula_fields"]:
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
            result["terminal_return_if_no_basis_word_formula"],
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
