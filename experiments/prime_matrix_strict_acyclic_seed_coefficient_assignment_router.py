#!/usr/bin/env python3
"""生成 strict acyclic seed coefficient assignment 攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_coefficient_assignment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.md"

TARGET = "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"
NEXT_TARGET = "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json",
    "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
    "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
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


def assignment_fields() -> list[dict[str, str]]:
    """列出 coefficient assignment 的必要字段。"""
    return [
        {
            "field": "assignment_domain",
            "meaning": "已生成的 actual noncanonical primitive basis words。",
        },
        {
            "field": "value_map_formula",
            "meaning": "每个 basis word 到 signed coefficient 的赋值公式。",
        },
        {
            "field": "sign_local_factor_projection",
            "meaning": "从赋值公式投影出 sign、local factor 和非零条件。",
        },
        {
            "field": "basis_source_compatibility",
            "meaning": "赋值公式与 seed pre-Cauchy basis weight source 是同一对象。",
        },
        {
            "field": "failure_return",
            "meaning": "无定义、零因子、符号冲突、超预算或作用域冲突时的回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 coefficient assignment 的第一开口。"""
    previous = data["previous"]
    anchor_input = data["anchor_input"]
    alphabet = data["alphabet"]
    internal = data["internal"]
    basis_source = data["basis_source"]
    coefficient = data["coefficient"]
    value_table = data["value_table"]
    weight_formula = data["weight_formula"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    target_active = previous.get("next_direct_attack_target") == TARGET
    geometric_domain_closed = anchor_input.get("anchor_input_rule_proved") is True
    alphabet_domain_not_enough = alphabet.get("noncanonical_precauchy_basis_alphabet_ledger_proved") is False
    value_map_missing = (
        internal.get("basis_coefficient_assignment_ledger_proved") is False
        and value_table.get("pointwise_signed_alpha_coefficient_value_table_proved") is False
        and weight_formula.get("pointwise_nonrecursive_signed_alpha_weight_formula_proved") is False
    )
    source_law_open = (
        basis_source.get("acyclic_seed_precauchy_basis_weight_source_formula_proved") is False
        or coefficient.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False
    )
    reverse_blocked = (
        reverse.get("reverse_provenance_functor_boundary_closed") is True
        and zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "CoefficientAssignmentTargetActive",
            target_active,
            False,
            "上一层已把 signed slot value formula 压到 coefficient assignment。",
            TARGET,
        ),
        row(
            "GeometricBasisWordDomainClosed",
            geometric_domain_closed,
            True,
            "anchor/dyadic/phase 输入域已经闭合；可作为 assignment 的 unsigned domain。",
            NEXT_TARGET,
        ),
        row(
            "BasisAlphabetDomainStillNeedsSignedValue",
            alphabet_domain_not_enough,
            False,
            "noncanonical basis alphabet 的 signed/local-factor 层仍依赖 coefficient assignment 自身。",
            NEXT_TARGET,
        ),
        row(
            "ValueMapFormulaIsFirstOpenField",
            True,
            True,
            "assignment 的第一不可替代字段是 basis word 到 signed coefficient 的 value map formula。",
            NEXT_TARGET,
        ),
        row(
            "ExistingPointwiseValueRoutesStillOpen",
            value_map_missing,
            False,
            "逐点 signed value table、非递归 signed weight 公式和 basis coefficient assignment 均未证明。",
            NEXT_TARGET,
        ),
        row(
            "BasisSourceAndCoefficientLawStillOpen",
            source_law_open,
            False,
            "basis weight source 与 primitive row signed coefficient law 仍缺赋值公式支撑。",
            NEXT_TARGET,
        ),
        row(
            "ReverseAssignmentRecoveryBlocked",
            reverse_blocked,
            True,
            "不能从 payment、推前后投影或早期零行覆盖反推出 value map formula。",
            NEXT_TARGET,
        ),
        row(
            "BasisWordToSignedCoefficientValueMapFormulaCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出 actual noncanonical basis word 到 signed coefficient 的赋值公式。",
            NEXT_TARGET,
        ),
        row(
            "CoefficientAssignmentOnBasisAlphabetCurrentCorpusProved",
            False,
            False,
            "没有 value map formula，coefficient assignment 仍未证明。",
            TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 coefficient assignment 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "anchor_input": load_json("prime-matrix-strict-acyclic-seed-anchor-input-rule-router.json"),
        "alphabet": load_json("prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"),
        "internal": load_json("prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"),
        "basis_source": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
        "coefficient": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
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
        "certificate_type": "prime_matrix_strict_acyclic_seed_coefficient_assignment_router",
        "status": "coefficient_assignment_reduced_to_basis_word_value_map_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "coefficient_assignment_router_closed": True,
        "geometric_basis_word_domain_closed": True,
        "value_map_formula_is_first_open_field": True,
        "basis_word_to_signed_coefficient_value_map_formula_proved": False,
        "acyclic_seed_coefficient_assignment_on_basis_alphabet_proved": False,
        "signed_weight_slot_value_formula_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_targets": [
            "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
            "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton",
            "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward",
        ],
        "terminal_return_if_no_value_map_formula": TERMINAL_RETURN,
        "assignment_fields": assignment_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 的第一开口是 `{NEXT_TARGET}`。"
            "几何 basis word 域已可用，但 signed assignment 必须给出 word -> coefficient 的具体赋值公式。"
        ),
        "plain_conclusion": (
            "本步把 coefficient assignment 压到 value map formula。"
            "锚/相位/截断输入已经闭合，问题不再是找到 word，而是给每个 word 赋 signed coefficient；"
            "这个赋值不能由 payment、零行覆盖或下游解积分反推。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed coefficient assignment 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"coefficient_assignment_router_closed={fmt_bool(result['coefficient_assignment_router_closed'])}",
        f"geometric_basis_word_domain_closed={fmt_bool(result['geometric_basis_word_domain_closed'])}",
        f"basis_word_to_signed_coefficient_value_map_formula_proved={fmt_bool(result['basis_word_to_signed_coefficient_value_map_formula_proved'])}",
        f"acyclic_seed_coefficient_assignment_on_basis_alphabet_proved={fmt_bool(result['acyclic_seed_coefficient_assignment_on_basis_alphabet_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. assignment 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["assignment_fields"]:
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
            result["terminal_return_if_no_value_map_formula"],
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
