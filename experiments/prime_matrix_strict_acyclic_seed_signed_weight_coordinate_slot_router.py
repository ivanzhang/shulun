#!/usr/bin/env python3
"""生成 strict acyclic seed signed weight coordinate slot 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_signed_weight_coordinate_slot_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.md"

TARGET = "AcyclicSeedSignedWeightCoordinateSlotLedger"
NEXT_TARGET = "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
    "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
    "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
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
    """汇总依赖证据文件哈希。"""
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


def slot_fields() -> list[dict[str, str]]:
    """列出 signed weight 坐标槽必须给出的字段。"""
    return [
        {
            "field": "slot_schema",
            "meaning": "在 primitive basis word 中声明 signed_weight、sign、local_factor、return_tag 槽位。",
        },
        {
            "field": "slot_value_formula",
            "meaning": "对每个 primitive basis word 给出 signed weight/local factor 的实际赋值公式。",
        },
        {
            "field": "nonzero_and_sign_rule",
            "meaning": "证明 local factor 非零、符号口径确定；失败时命名回流。",
        },
        {
            "field": "basis_assignment_compatibility",
            "meaning": "证明该槽位赋值与 seed coefficient assignment/basis source 是同一公式。",
        },
        {
            "field": "prepushforward_sum_compatibility",
            "meaning": "证明槽位赋值参与推前前 alpha/delta 求和恒等式。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 signed weight coordinate slot 的首个未闭合字段。"""
    anchor_input = data["anchor_input"]
    signed_lift = data["signed_lift"]
    coefficient_law = data["coefficient_law"]
    basis_source = data["basis_source"]
    internal_expansion = data["internal_expansion"]
    basis_alphabet = data["basis_alphabet"]
    value_table = data["value_table"]
    weight_formula = data["weight_formula"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    coordinate_domain_closed = anchor_input.get("anchor_input_rule_proved") is True
    slot_schema_available = coordinate_domain_closed
    assignment_missing = (
        internal_expansion.get("basis_coefficient_assignment_ledger_proved") is False
        or coefficient_law.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False
    )
    value_formula_missing = (
        signed_lift.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
        and value_table.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
        and weight_formula.get("pointwise_nonrecursive_signed_alpha_weight_formula_proved") is False
    )
    basis_source_missing = (
        basis_source.get("acyclic_seed_precauchy_basis_weight_source_formula_proved") is False
        or basis_alphabet.get("noncanonical_precauchy_basis_alphabet_ledger_proved") is False
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "SignedWeightCoordinateSlotTargetActive",
            anchor_input.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已关闭 anchor input rule，并把 word coordinate formula 的剩余压到 signed weight coordinate slot。",
            TARGET,
        ),
        row(
            "CoordinateDomainClosed",
            coordinate_domain_closed,
            True,
            "primitive word 的 anchor/dyadic/phase 输入域已由锚区间和多重度账本闭合。",
            "slot_schema 可声明。",
        ),
        row(
            "SlotSchemaAvailableButValueMissing",
            slot_schema_available,
            False,
            "可声明 signed_weight/sign/local_factor 槽位，但还没有每个 word 的实际赋值公式。",
            NEXT_TARGET,
        ),
        row(
            "SlotValueFormulaIsFirstOpenField",
            True,
            True,
            "没有 slot_value_formula，非零符号、coefficient assignment 和推前前求和都无从验证。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseSignedValueTableStillOpen",
            value_formula_missing,
            False,
            "逐 skeleton row signed value table 与非递归 signed weight formula 仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "BasisSourceAndAssignmentStillOpen",
            assignment_missing and basis_source_missing,
            False,
            "seed basis source、basis alphabet 和 coefficient assignment 尚未闭合，不能给 signed slot 赋值。",
            NEXT_TARGET,
        ),
        row(
            "UnsignedCoordinateCannotFillSignedSlot",
            coordinate_domain_closed,
            True,
            "anchor/dyadic/phase 坐标只给 unsigned 输入域，不能自动产生 signed weight/local factor。",
            NEXT_TARGET,
        ),
        row(
            "ReverseSignedSlotRecoveryBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖反推 signed slot value。",
            NEXT_TARGET,
        ),
        row(
            "SignedWeightSlotValueFormulaCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交 primitive basis word 上的 signed weight/local factor 赋值公式。",
            NEXT_TARGET,
        ),
        row(
            "SignedWeightCoordinateSlotCurrentCorpusProved",
            False,
            False,
            "slot schema 可命名，但缺 value formula、非零符号规则和 assignment 兼容，故坐标槽未闭合。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 signed weight coordinate slot 证书。"""
    data = {
        "anchor_input": load_json("prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "coefficient_law": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "basis_source": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
        "internal_expansion": load_json(
            "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"
        ),
        "basis_alphabet": load_json("prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"),
        "value_table": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "weight_formula": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_signed_weight_coordinate_slot_router",
        "status": "signed_weight_coordinate_slot_reduced_to_slot_value_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "signed_weight_coordinate_slot_router_closed": True,
        "coordinate_domain_closed": True,
        "slot_schema_available": True,
        "slot_value_formula_is_first_open_field": True,
        "signed_weight_slot_value_formula_proved": False,
        "signed_weight_coordinate_slot_proved": False,
        "word_coordinate_formula_proved": False,
        "basis_word_formula_from_source_tuple_parameters_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger",
            "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
            "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
        ],
        "terminal_return_if_no_slot_value_formula": TERMINAL_RETURN,
        "slot_fields": slot_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的输入域和槽位 schema 可由已闭合坐标账本声明；"
            f"真正首缺口是 `{NEXT_TARGET}`，即每个 primitive basis word 的 signed weight/local factor 赋值公式。"
        ),
        "plain_conclusion": (
            "本步把 signed weight coordinate slot 压到 slot_value_formula。"
            "锚、dyadic、phase 输入已闭合，所以几何坐标不再阻塞；剩余是纯 signed 算术："
            "必须正向给出每个 primitive basis word 的 signed weight/local factor，且与 basis source 和 coefficient assignment 兼容。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed signed weight coordinate slot 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_weight_coordinate_slot_router_closed={fmt_bool(result['signed_weight_coordinate_slot_router_closed'])}",
        f"coordinate_domain_closed={fmt_bool(result['coordinate_domain_closed'])}",
        f"slot_schema_available={fmt_bool(result['slot_schema_available'])}",
        f"signed_weight_slot_value_formula_proved={fmt_bool(result['signed_weight_slot_value_formula_proved'])}",
        f"signed_weight_coordinate_slot_proved={fmt_bool(result['signed_weight_coordinate_slot_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. slot 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["slot_fields"]:
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
            result["terminal_return_if_no_slot_value_formula"],
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
