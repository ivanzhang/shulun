#!/usr/bin/env python3
"""生成 strict acyclic seed basis word signed coefficient 来源恒等式证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_basis_word_origin_identity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.md"

TARGET = "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"
NEXT_TARGET = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
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


def row_table_fields() -> list[dict[str, str]]:
    """列出逐行原始生成表字段。"""
    return [
        {
            "field": "basis_word_id",
            "meaning": "由已闭合几何坐标产生的 primitive basis word 编号。",
        },
        {
            "field": "origin_source_tuple",
            "meaning": "同 formal-unit pre-Cauchy 来源 tuple。",
        },
        {
            "field": "signed_coefficient",
            "meaning": "该 basis word/primitive summand 的 signed coefficient 正向公式。",
        },
        {
            "field": "branch_key_uv_sign_local_factor",
            "meaning": "branch key、u/v map、sign、local factor 和非零条件。",
        },
        {
            "field": "prepushforward_sum_identity",
            "meaning": "推前前求和等于目标 alpha/delta 系数贡献。",
        },
        {
            "field": "return_tag",
            "meaning": "缺来源、零因子、超预算、后验依赖或作用域冲突时的回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把 basis word 来源恒等式接回逐行原始生成表。"""
    previous = data["previous"]
    primitive_origin = data["primitive_origin"]
    row_table = data["row_table"]
    emitter = data["emitter"]
    formal_record = data["formal_record"]
    source_tuple = data["source_tuple"]
    anchor_input = data["anchor_input"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    containers_closed = (
        formal_record.get("formal_unit_source_record_schema_closed") is True
        and source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
        and anchor_input.get("anchor_input_rule_proved") is True
    )
    same_as_primitive_origin = (
        primitive_origin.get("primitive_summand_origin_identity_router_closed") is True
        or primitive_origin.get("origin_identity_is_row_level_origin_generation") is True
    )
    row_table_open = row_table.get("row_level_clean_core_origin_generation_table_proved") is False
    emitter_open = emitter.get("acyclic_seed_signed_row_emitter_rule_proved") is False
    loop_cut = (
        source_loop.get("source_loop_cut_closed") is True
        or source_loop.get("circular_reverse_derivation_rejected") is True
        or reverse.get("reverse_provenance_functor_boundary_closed") is True
    )
    zero_blocked = (
        zero_nogo.get("geometry_source_extraction_blocked") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "BasisWordOriginIdentityTargetActive",
            target_active,
            False,
            "上一层已把 basis word value map 压到 signed coefficient 来源恒等式。",
            TARGET,
        ),
        row(
            "ContainersAndGeometricWordsAvailable",
            containers_closed,
            True,
            "formal-unit/source-tuple 和几何 basis word 输入已闭合。",
            "但它们不产生 signed coefficient。",
        ),
        row(
            "BasisWordOriginEqualsRowLevelGeneration",
            same_as_primitive_origin,
            True,
            "basis word 来源恒等式与 primitive summand 来源恒等式是同一需求：逐行原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "RowLevelGenerationTableStillOpen",
            row_table_open,
            False,
            "当前材料没有逐 basis word/primitive summand 的 signed coefficient 原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "AcyclicSignedEmitterStillOpen",
            emitter_open,
            False,
            "无环 seed signed row emitter 仍缺 primitive row signed coefficient law。",
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity",
        ),
        row(
            "SourceLoopAndReverseRecoveryBlocked",
            loop_cut and zero_blocked,
            True,
            "不能用来源循环、payment 反推或早期零行 unsigned cover 生成来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "RowLevelCleanCoreOriginalCoefficientGenerationTableCurrentCorpusProved",
            False,
            False,
            "当前材料尚未提交 actual noncanonical primitive summands 的逐行原始生成表。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordSignedCoefficientOriginIdentityCurrentCorpusProved",
            False,
            False,
            "没有逐行原始生成表，basis word signed coefficient 来源恒等式仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 basis word origin identity 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "primitive_origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "emitter": load_json("prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "anchor_input": load_json("prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_basis_word_origin_identity_router",
        "status": "basis_word_origin_identity_reduced_to_row_level_generation_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "basis_word_origin_identity_router_closed": True,
        "basis_word_origin_equals_row_level_generation": True,
        "row_level_clean_core_origin_generation_table_proved": False,
        "basis_word_signed_coefficient_origin_identity_proved": False,
        "basis_word_to_signed_coefficient_value_map_formula_proved": False,
        "acyclic_seed_coefficient_assignment_on_basis_alphabet_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity",
            "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
            "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
        ],
        "terminal_return_if_no_row_generation_table": TERMINAL_RETURN,
        "row_table_fields": row_table_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 与既有 primitive summand 来源恒等式会合；"
            f"真正共同剩余是 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把 basis word signed coefficient 来源恒等式接回统一原始生成表。"
            "几何 word 和 source tuple 已经命名，但 signed coefficient 的来源必须由逐行 clean-core 原始生成表给出；"
            "当前材料仍没有该表。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed basis word origin identity 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"basis_word_origin_identity_router_closed={fmt_bool(result['basis_word_origin_identity_router_closed'])}",
        f"basis_word_origin_equals_row_level_generation={fmt_bool(result['basis_word_origin_equals_row_level_generation'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"basis_word_signed_coefficient_origin_identity_proved={fmt_bool(result['basis_word_signed_coefficient_origin_identity_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 原始生成表字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["row_table_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 前沿压缩",
            "",
            result["frontier_reduction"],
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
            result["terminal_return_if_no_row_generation_table"],
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
