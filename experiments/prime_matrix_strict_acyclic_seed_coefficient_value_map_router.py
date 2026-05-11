#!/usr/bin/env python3
"""生成 strict acyclic seed coefficient value map 公式攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_coefficient_value_map_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.md"

TARGET = "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"
NEXT_TARGET = "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
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


def origin_identity_fields() -> list[dict[str, str]]:
    """列出 basis word signed coefficient 来源恒等式字段。"""
    return [
        {
            "field": "origin_source_tuple",
            "meaning": "产生该 basis word/signed coefficient 的同 formal-unit pre-Cauchy source tuple。",
        },
        {
            "field": "signed_coefficient_expression",
            "meaning": "signed coefficient 的正向表达式，含筛权、符号、branch/local factor。",
        },
        {
            "field": "origin_to_basis_word_identity",
            "meaning": "证明来源表达式生成的对象正是该 primitive basis word。",
        },
        {
            "field": "prepushforward_equality",
            "meaning": "证明在 Phi/payment/Cauchy 推前之前已等于目标 alpha/delta 贡献。",
        },
        {
            "field": "return_tag",
            "meaning": "来源缺失、零因子、符号冲突或后验依赖时的命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 value map 公式的真正破坏输入。"""
    previous = data["previous"]
    expression = data["expression"]
    origin = data["origin"]
    row_table = data["row_table"]
    weight_formula = data["weight_formula"]
    value_table = data["value_table"]
    basis_source = data["basis_source"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    expression_route_open = (
        expression.get("primitive_summand_signed_coefficient_origin_identity_proved") is False
        or origin.get("primitive_summand_signed_coefficient_origin_identity_proved") is False
    )
    row_table_open = row_table.get("row_level_clean_core_origin_generation_table_proved") is False
    pointwise_open = (
        weight_formula.get("primitive_summand_signed_weight_expression_proved") is False
        or value_table.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
    )
    basis_source_open = basis_source.get("acyclic_seed_precauchy_basis_weight_source_formula_proved") is False
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "CoefficientValueMapTargetActive",
            target_active,
            False,
            "上一层已把 coefficient assignment 压到 basis word -> signed coefficient value map formula。",
            TARGET,
        ),
        row(
            "ValueMapMustBeOriginIdentity",
            True,
            True,
            "value map 不能只是赋值符号；必须说明 signed coefficient 从哪个 pre-Cauchy 来源恒等式生成。",
            NEXT_TARGET,
        ),
        row(
            "PrimitiveSummandOriginRouteStillOpen",
            expression_route_open,
            False,
            "primitive summand signed expression 已被压到来源恒等式，但来源恒等式仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "RowLevelOriginGenerationTableStillOpen",
            row_table_open,
            False,
            "逐行原始生成表仍未证明，不能给出 value map 的来源行。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseSignedWeightRoutesStillOpen",
            pointwise_open,
            False,
            "逐点 signed value table 和 signed weight expression 仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "BasisSourceStillOpen",
            basis_source_open,
            False,
            "basis weight source formula 仍未证明；value map 缺其算术来源。",
            NEXT_TARGET,
        ),
        row(
            "ReverseOriginRecoveryBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖反推 signed coefficient 来源。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordSignedCoefficientOriginIdentityCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出每个 basis word 的 signed coefficient pre-Cauchy 来源恒等式。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordToSignedCoefficientValueMapFormulaCurrentCorpusProved",
            False,
            False,
            "没有来源恒等式，value map formula 仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 coefficient value map 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "expression": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "weight_formula": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "value_table": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "basis_source": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_coefficient_value_map_router",
        "status": "coefficient_value_map_reduced_to_basis_word_origin_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "coefficient_value_map_router_closed": True,
        "value_map_must_be_origin_identity": True,
        "basis_word_signed_coefficient_origin_identity_proved": False,
        "basis_word_to_signed_coefficient_value_map_formula_proved": False,
        "acyclic_seed_coefficient_assignment_on_basis_alphabet_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
            "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
            "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
        ],
        "terminal_return_if_no_origin_identity": TERMINAL_RETURN,
        "origin_identity_fields": origin_identity_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 继续压到 `{NEXT_TARGET}`："
            "signed coefficient 的 value map 必须是 pre-Cauchy 来源恒等式，而不是后验赋值表。"
        ),
        "plain_conclusion": (
            "本步把 basis word -> signed coefficient value map 压到来源恒等式。"
            "换言之，必须正向说明每个 basis word 的 signed coefficient 从哪个同 formal-unit pre-Cauchy source tuple 生成，"
            "并在推前之前等于 alpha/delta 贡献；当前材料没有这条恒等式。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed coefficient value map 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"coefficient_value_map_router_closed={fmt_bool(result['coefficient_value_map_router_closed'])}",
        f"value_map_must_be_origin_identity={fmt_bool(result['value_map_must_be_origin_identity'])}",
        f"basis_word_signed_coefficient_origin_identity_proved={fmt_bool(result['basis_word_signed_coefficient_origin_identity_proved'])}",
        f"basis_word_to_signed_coefficient_value_map_formula_proved={fmt_bool(result['basis_word_to_signed_coefficient_value_map_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 来源恒等式字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["origin_identity_fields"]:
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
            result["terminal_return_if_no_origin_identity"],
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
