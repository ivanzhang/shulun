#!/usr/bin/env python3
"""生成 strict 联合 word/coefficient 发射公式字段原子证书。

用法示例：
  python3 experiments/prime_matrix_strict_joint_emitter_formula_field_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-joint-emitter-formula-field-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.md"

TARGET = "AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy"
NEXT_TARGET = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
ROWS_TARGET = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
IDENTITY_TARGET = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
RETURN_TARGET = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json",
    "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
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
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def productive_fields() -> list[dict[str, str]]:
    """列出联合发射公式内部真正需要生成的字段。"""
    return [
        {
            "field": "precauchy_joint_declaration_line",
            "status": "first_open_atom",
            "meaning": "在 Cauchy、dispersion、payment、Phi 推前之前声明同一 source tuple 的 actual noncanonical 联合发射器。",
        },
        {
            "field": "joint_rows_formula",
            "status": "blocked_until_declaration",
            "meaning": "由 declaration line 正向列出 primitive basis word、branch key、u/v、sign、local factor 与 signed coefficient。",
        },
        {
            "field": "word_coefficient_identity",
            "status": "blocked_until_rows_formula",
            "meaning": "证明 word 与 coefficient 是同一 pre-Cauchy 算术对象的两面，而非两个后验拼接标签。",
        },
        {
            "field": "prepushforward_sum_identity",
            "status": "blocked_until_rows_formula",
            "meaning": "证明联合发射行在 Phi/payment 推前前已经给出目标 alpha/delta 贡献。",
        },
        {
            "field": "no_downstream_recovery_and_named_return",
            "status": "schema_pinned_exact_ledger_open",
            "meaning": "禁止从 payment/零行/终端证书反推；失败、零因子、多值、超预算、thin/rejected/cancelling 必须命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查联合发射公式的字段边界与第一原子。"""
    previous = data["previous"]
    formal = data["formal"]
    tuple_doc = data["tuple"]
    constructor = data["constructor"]
    coordinate = data["coordinate"]
    slot = data["slot"]
    slot_value = data["slot_value"]
    assignment = data["assignment"]
    value_map = data["value_map"]
    origin = data["origin"]
    source_table = data["source_table"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]
    taxonomy = data["taxonomy"]
    firewall = data["firewall"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    source_tuple_closed = (
        formal.get("formal_unit_source_record_schema_closed") is True
        and formal.get("concrete_formal_unit_source_record_closed") is True
        and tuple_doc.get("source_tuple_anchor_parameter_schema_closed") is True
        and tuple_doc.get("concrete_source_tuple_anchor_parameter_data_closed") is True
    )
    word_first_open = (
        constructor.get("source_tuple_to_primitive_basis_word_constructor_proved") is False
        and coordinate.get("word_coordinate_formula_proved") is False
        and slot.get("signed_weight_coordinate_slot_proved") is False
    )
    coefficient_first_open = (
        slot_value.get("acyclic_seed_coefficient_assignment_on_basis_alphabet_proved") is False
        and assignment.get("basis_word_to_signed_coefficient_value_map_formula_proved") is False
        and value_map.get("basis_word_signed_coefficient_origin_identity_proved") is False
        and origin.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    source_table_first_line_open = (
        source_table.get("pre_cauchy_constructor_declaration_line_proved") is False
        and source_table.get("primitive_summand_emitter_formula_rows_proved") is False
        and source_table.get("alpha_delta_coefficient_identity_before_pushforward_proved") is False
    )
    downstream_blocked = (
        source_loop.get("source_loop_cut_closed") is True
        and source_loop.get("circular_reverse_derivation_rejected") is True
        and reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("zero_row_seed_extraction_blocked") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )
    taxonomy_blocks_fake_sources = (
        taxonomy.get("identity_taxonomy_closed") is True
        or firewall.get("constructor_source_class_firewall_boundary_closed") is True
    )
    return_ledger_open = source_table.get("source_table_no_downstream_recovery_return_ledger_proved") is False

    return [
        row(
            "JointEmitterFormulaTargetActive",
            target_active,
            False,
            "上一层已把 cycle-cut 破环输入压成同一 formal unit 的联合 basis word/coefficient 发射公式。",
            TARGET,
        ),
        row(
            "SourceTupleInputAlreadyClosed",
            source_tuple_closed,
            True,
            "formal unit 与 source tuple 的字段、锚参数和哈希纪律已经存在，输入容器不是当前硬点。",
            "生产性联合发射公式仍未给出。",
        ),
        row(
            "WordFirstRouteStillCannotEmitJointFormula",
            word_first_open,
            False,
            "单独从 source tuple 先构造 basis word 仍卡在 word coordinate 和 signed slot，不能给出联合发射。",
            NEXT_TARGET,
        ),
        row(
            "CoefficientFirstRouteStillReturnsToOriginTable",
            coefficient_first_open,
            False,
            "单独从 signed slot/assignment 出发仍回到 value map、origin identity 和 row-level 原始表。",
            NEXT_TARGET,
        ),
        row(
            "ActualEmitterSourceTableFirstLineMatchesJointDeclaration",
            source_table_first_line_open,
            False,
            "actual emitter 源表已有字段律：没有 pre-Cauchy declaration line，rows、identity 和 return ledger 都不能合法开始。",
            NEXT_TARGET,
        ),
        row(
            "DownstreamRecoveryFirewallImported",
            downstream_blocked,
            True,
            "payment、Phi 投影、零行覆盖和来源环均不能反推 signed pre-Cauchy 联合发射器。",
            RETURN_TARGET,
        ),
        row(
            "FakeIndependentSourceTaxonomyImported",
            taxonomy_blocks_fake_sources,
            True,
            "独立恒等式分类和 source-class 防火墙已排除 canonical/generic/external/unregistered 伪来源混入 strict 自足线。",
            NEXT_TARGET,
        ),
        row(
            "NoDownstreamReturnLedgerExactFormStillOpen",
            return_ledger_open,
            False,
            "禁止后验读取的原则已闭合，但 exact return ledger 仍需逐类记录零因子、多值、超预算、thin/rejected/cancelling。",
            RETURN_TARGET,
        ),
        row(
            "JointEmitterProductiveFieldsPinned",
            True,
            True,
            "联合公式的生产性字段被压成 declaration line、rows formula、word/coefficient identity、prepushforward identity 和 return ledger。",
            f"{NEXT_TARGET} AND {ROWS_TARGET} AND {IDENTITY_TARGET} AND {RETURN_TARGET}",
        ),
        row(
            "PreCauchyJointDeclarationLineCurrentCorpusProved",
            False,
            False,
            "当前材料尚未在 Cauchy/payment 前声明 actual noncanonical source tuple 的联合 word/coefficient emitter。",
            NEXT_TARGET,
        ),
        row(
            "JointEmitterFormulaCurrentCorpusProved",
            False,
            False,
            "缺 declaration line 时，后续 rows、identity 和 return ledger 不能合取闭合。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造联合发射公式字段原子证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json"),
        "formal": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "constructor": load_json("prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json"),
        "coordinate": load_json("prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"),
        "slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "slot_value": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "assignment": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "value_map": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "origin": load_json("prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "taxonomy": load_json("prime-matrix-independent-precauchy-identity-taxonomy-router.json"),
        "firewall": load_json("prime-matrix-clean-core-constructor-source-class-firewall-router.json"),
    }
    rows = build_rows(data)
    productive_basis = f"{NEXT_TARGET} AND {ROWS_TARGET} AND {IDENTITY_TARGET} AND {RETURN_TARGET}"
    return {
        "certificate_type": "prime_matrix_strict_joint_emitter_formula_field_atom_router",
        "status": "joint_emitter_formula_reduced_to_precauchy_joint_declaration_line_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "joint_emitter_formula_field_atom_router_closed": True,
        "source_tuple_input_closed": data["formal"].get("formal_unit_source_record_schema_closed") is True
        and data["tuple"].get("source_tuple_anchor_parameter_schema_closed") is True,
        "downstream_recovery_firewall_imported": True,
        "joint_productive_field_decomposition_pinned": True,
        "pre_cauchy_joint_declaration_line_proved": False,
        "joint_emitter_rows_formula_proved": False,
        "joint_word_coefficient_identity_proved": False,
        "joint_emitter_prepushforward_sum_identity_proved": False,
        "joint_emitter_no_downstream_named_return_ledger_proved": False,
        "joint_basis_word_coefficient_emitter_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            ROWS_TARGET,
            IDENTITY_TARGET,
            RETURN_TARGET,
            TERMINAL_DESCENT,
        ],
        "productive_basis_after_router": productive_basis,
        "strict_basis_after_router": f"(({productive_basis}) OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}",
        "productive_fields": productive_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 内部不能再靠 word-first 或 coefficient-first 顺序拆分闭合。"
            "已有 source tuple 只是输入容器；真正第一生产性原子是 Cauchy/payment 前的联合 declaration line，"
            f"即 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把联合发射公式拆到字段级：source tuple 输入已经闭合，后验读取已被 source-loop/no-go 防火墙排除；"
            "但能同时生成 primitive basis word 与 signed coefficient 的生产性公式仍不存在。"
            "因此当前首缺口不是再找一个后验表，而是在 Cauchy/payment/Phi 推前之前提交同一 actual noncanonical source tuple 的联合 declaration line。"
            "没有这条第一行，rows formula、word/coefficient identity、prepushforward identity 与 return ledger 都不能闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 联合 word/coefficient 发射公式字段原子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"joint_emitter_formula_field_atom_router_closed={fmt_bool(result['joint_emitter_formula_field_atom_router_closed'])}",
        f"source_tuple_input_closed={fmt_bool(result['source_tuple_input_closed'])}",
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(result['pre_cauchy_joint_declaration_line_proved'])}",
        f"joint_basis_word_coefficient_emitter_proved={fmt_bool(result['joint_basis_word_coefficient_emitter_proved'])}",
        f"acyclic_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_terminal_return_well_founded_descent_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 生产性字段",
        "",
        "| field | status | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["productive_fields"]:
        lines.append(
            f"| `{table_cell(item['field'])}` | `{table_cell(item['status'])}` | {table_cell(item['meaning'])} |"
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
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 下一真正单点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "完整生产性字段基：",
            "",
            "```text",
            result["productive_basis_after_router"],
            "```",
            "",
            "保留终端下降并行门后的当前严格自足基：",
            "",
            "```text",
            result["strict_basis_after_router"],
            "```",
            "",
            "审稿边界：本文件只关闭字段定位和第一原子定位；它没有证明联合 declaration line，"
            "也没有证明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
