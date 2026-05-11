#!/usr/bin/env python3
"""生成 strict acyclic seed signed slot value formula 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_signed_slot_value_formula_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.md"

TARGET = "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"
NEXT_TARGET = "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
    "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
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


def value_formula_components() -> list[dict[str, str]]:
    """列出 slot value formula 的内部组成。"""
    return [
        {
            "component": "coefficient_assignment",
            "role": "每个 basis word 到 signed coefficient 的赋值公式，是第一开口。",
        },
        {
            "component": "sign_local_factor_rule",
            "role": "由 coefficient assignment 诱导符号、local factor 和非零条件。",
        },
        {
            "component": "return_rule",
            "role": "零值、符号冲突、local factor 缺失或超预算的命名回流。",
        },
        {
            "component": "prepushforward_sum_identity",
            "role": "证明赋值后的 primitive words 在推前前给出目标 alpha/delta 系数。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 signed slot value formula 的第一字段。"""
    slot = data["slot"]
    internal = data["internal"]
    alphabet = data["alphabet"]
    basis_source = data["basis_source"]
    coefficient = data["coefficient"]
    value_table = data["value_table"]
    weight_formula = data["weight_formula"]
    summand_expression = data["summand_expression"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    slot_target_active = slot.get("next_direct_attack_target") == TARGET
    basis_word_domain_partly_available = slot.get("coordinate_domain_closed") is True
    alphabet_assignment_open = (
        internal.get("basis_coefficient_assignment_ledger_proved") is False
        or alphabet.get("noncanonical_precauchy_basis_alphabet_ledger_proved") is False
    )
    coefficient_source_open = (
        basis_source.get("acyclic_seed_precauchy_basis_weight_source_formula_proved") is False
        or coefficient.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False
    )
    pointwise_value_open = (
        value_table.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
        or weight_formula.get("pointwise_nonrecursive_signed_alpha_weight_formula_proved") is False
        or summand_expression.get("primitive_summand_signed_weight_expression_proved") is False
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "SignedSlotValueFormulaTargetActive",
            slot_target_active,
            False,
            "上一层已把 signed weight coordinate slot 压到 primitive basis word 上的 slot value formula。",
            TARGET,
        ),
        row(
            "PrimitiveWordDomainAvailableButUnsigned",
            basis_word_domain_partly_available,
            True,
            "primitive word 的几何输入域已闭合，但该域仍是 unsigned 坐标域。",
            NEXT_TARGET,
        ),
        row(
            "CoefficientAssignmentIsFirstOpenField",
            True,
            True,
            "slot value formula 的第一字段是 basis word 到 signed coefficient 的赋值；没有它，符号和 local factor 都无定义。",
            NEXT_TARGET,
        ),
        row(
            "AlphabetAndAssignmentStillOpen",
            alphabet_assignment_open,
            False,
            "noncanonical basis alphabet 与 coefficient assignment 尚未共同闭合。",
            NEXT_TARGET,
        ),
        row(
            "BasisSourceAndCoefficientLawStillOpen",
            coefficient_source_open,
            False,
            "basis weight source formula 与 primitive row signed coefficient law 仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseSignedValueFormulaStillOpen",
            pointwise_value_open,
            False,
            "逐点 signed alpha 值表、非递归 signed weight 公式和 primitive summand signed expression 仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "ReverseCoefficientRecoveryBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖反推 coefficient assignment。",
            NEXT_TARGET,
        ),
        row(
            "CoefficientAssignmentOnBasisAlphabetCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交从 actual noncanonical basis word 到 signed coefficient 的赋值公式。",
            NEXT_TARGET,
        ),
        row(
            "SignedSlotValueFormulaCurrentCorpusProved",
            False,
            False,
            "没有 coefficient assignment，slot value formula 仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 signed slot value formula 证书。"""
    data = {
        "slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "internal": load_json("prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"),
        "alphabet": load_json("prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"),
        "basis_source": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
        "coefficient": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "value_table": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "weight_formula": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "summand_expression": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_signed_slot_value_formula_router",
        "status": "signed_slot_value_formula_reduced_to_coefficient_assignment_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "signed_slot_value_formula_router_closed": True,
        "coefficient_assignment_is_first_open_field": True,
        "acyclic_seed_coefficient_assignment_on_basis_alphabet_proved": False,
        "signed_weight_slot_value_formula_proved": False,
        "signed_weight_coordinate_slot_proved": False,
        "word_coordinate_formula_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
            "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger",
            "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
        ],
        "terminal_return_if_no_coefficient_assignment": TERMINAL_RETURN,
        "value_formula_components": value_formula_components(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的第一不可替代字段是 `{NEXT_TARGET}`："
            "必须先给出每个 basis word 到 signed coefficient 的赋值，才能定义 sign/local factor 和推前前求和。"
        ),
        "plain_conclusion": (
            "本步把 signed slot value formula 压到 coefficient assignment。"
            "几何 primitive word 域已经可用，但该域没有 signed 赋值；"
            "现有 basis source、basis alphabet、逐点 signed value table 都仍未闭合，且 payment/零行反推被阻断。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed signed slot value formula 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_slot_value_formula_router_closed={fmt_bool(result['signed_slot_value_formula_router_closed'])}",
        f"coefficient_assignment_is_first_open_field={fmt_bool(result['coefficient_assignment_is_first_open_field'])}",
        f"acyclic_seed_coefficient_assignment_on_basis_alphabet_proved={fmt_bool(result['acyclic_seed_coefficient_assignment_on_basis_alphabet_proved'])}",
        f"signed_weight_slot_value_formula_proved={fmt_bool(result['signed_weight_slot_value_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. value formula 组成",
        "",
        "| component | role |",
        "| --- | --- |",
    ]
    for item in result["value_formula_components"]:
        lines.append(
            "| `{component}` | {role} |".format(
                component=table_cell(item["component"]),
                role=table_cell(item["role"]),
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
            result["terminal_return_if_no_coefficient_assignment"],
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
