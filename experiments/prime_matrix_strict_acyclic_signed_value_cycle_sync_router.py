#!/usr/bin/env python3
"""生成 strict acyclic signed value 子循环同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_signed_value_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-signed-value-cycle-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-signed-value-cycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-signed-value-cycle-sync-router.md"

ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
PRIMITIVE_COEFF = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
BASIS_SOURCE = "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"
INTERNAL_EXPANSION = "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"
BASIS_ALPHABET = "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"
WORD_GENERATION = "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment"
WORD_CONSTRUCTOR = "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility"
BASIS_WORD_FORMULA = "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility"
WORD_COORDINATE = "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"
SIGNED_SLOT = "AcyclicSeedSignedWeightCoordinateSlotLedger"
SLOT_VALUE = "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"
COEFFICIENT_ASSIGNMENT = "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"
VALUE_MAP = "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"
ORIGIN_IDENTITY = "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"

NONCIRCULAR_GUARD = (
    "NoncircularPreCauchySignedCoefficientOriginInputIndependentOfRowLevelGenerationCycle"
)
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json",
    "prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json",
    "prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json",
    "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json",
    "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json",
    "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json",
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


def cycle_edges() -> list[dict[str, str]]:
    """登记本次下钻确认的 signed value 子循环。"""
    return [
        {"from": ROW_TABLE, "to": EMITTER},
        {"from": EMITTER, "to": PRIMITIVE_COEFF},
        {"from": PRIMITIVE_COEFF, "to": BASIS_SOURCE},
        {"from": BASIS_SOURCE, "to": INTERNAL_EXPANSION},
        {"from": INTERNAL_EXPANSION, "to": BASIS_ALPHABET},
        {"from": BASIS_ALPHABET, "to": WORD_GENERATION},
        {"from": WORD_GENERATION, "to": WORD_CONSTRUCTOR},
        {"from": WORD_CONSTRUCTOR, "to": BASIS_WORD_FORMULA},
        {"from": BASIS_WORD_FORMULA, "to": WORD_COORDINATE},
        {"from": WORD_COORDINATE, "to": SIGNED_SLOT},
        {"from": SIGNED_SLOT, "to": SLOT_VALUE},
        {"from": SLOT_VALUE, "to": COEFFICIENT_ASSIGNMENT},
        {"from": COEFFICIENT_ASSIGNMENT, "to": VALUE_MAP},
        {"from": VALUE_MAP, "to": ORIGIN_IDENTITY},
        {"from": ORIGIN_IDENTITY, "to": ROW_TABLE},
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 signed value 子循环是否给出非循环证明。"""
    row_table = data["row_table"]
    emitter = data["emitter"]
    primitive_coeff = data["primitive_coeff"]
    basis_source = data["basis_source"]
    internal = data["internal"]
    alphabet = data["alphabet"]
    word_generation = data["word_generation"]
    word_constructor = data["word_constructor"]
    basis_word_formula = data["basis_word_formula"]
    word_coordinate = data["word_coordinate"]
    signed_slot = data["signed_slot"]
    slot_value = data["slot_value"]
    coefficient_assignment = data["coefficient_assignment"]
    value_map = data["value_map"]
    origin_identity = data["origin_identity"]
    same_row = data["same_row"]
    source_loop = data["source_loop"]
    reverse = data["reverse"]
    zero_nogo = data["zero_nogo"]

    cycle_return_detected = (
        row_table.get("next_direct_attack_target") == EMITTER
        and emitter.get("next_direct_attack_target") == PRIMITIVE_COEFF
        and primitive_coeff.get("next_direct_attack_target") == BASIS_SOURCE
        and basis_source.get("next_direct_attack_target") == INTERNAL_EXPANSION
        and internal.get("next_direct_attack_target") == BASIS_ALPHABET
        and alphabet.get("next_direct_attack_target") == WORD_GENERATION
        and word_generation.get("next_direct_attack_target") == WORD_CONSTRUCTOR
        and word_constructor.get("next_direct_attack_target") == BASIS_WORD_FORMULA
        and basis_word_formula.get("next_direct_attack_target") == WORD_COORDINATE
        and word_coordinate.get("next_direct_attack_target") == SIGNED_SLOT
        and signed_slot.get("next_direct_attack_target") == SLOT_VALUE
        and slot_value.get("next_direct_attack_target") == COEFFICIENT_ASSIGNMENT
        and coefficient_assignment.get("next_direct_attack_target") == VALUE_MAP
        and value_map.get("next_direct_attack_target") == ORIGIN_IDENTITY
        and origin_identity.get("next_direct_attack_target") == ROW_TABLE
    )
    geometry_domain_closed = (
        word_coordinate.get("anchor_input_rule_proved") is True
        and word_coordinate.get("coordinate_domain_closed_after_anchor_input") is True
        and signed_slot.get("coordinate_domain_closed") is True
    )
    signed_value_open = (
        signed_slot.get("signed_weight_slot_value_formula_proved") is False
        and slot_value.get("acyclic_seed_coefficient_assignment_on_basis_alphabet_proved") is False
        and coefficient_assignment.get("basis_word_to_signed_coefficient_value_map_formula_proved")
        is False
    )
    origin_return_open = (
        value_map.get("basis_word_signed_coefficient_origin_identity_proved") is False
        and origin_identity.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    same_row_imported = (
        same_row.get("joint_alpha_same_row_origin_identity_router_closed") is True
        and same_row.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    reverse_blocked = (
        source_loop.get("circular_reverse_derivation_rejected") is True
        or reverse.get("reverse_provenance_functor_boundary_closed") is True
        or zero_nogo.get("downstream_reverse_source_blocked") is True
    )

    return [
        row(
            "AcyclicSignedValueSubcycleDetected",
            cycle_return_detected,
            True,
            "从逐行原始生成表下钻到 signed slot/value map 后，又经 basis word 来源恒等式返回同一逐行原始生成表。",
            ROW_TABLE,
        ),
        row(
            "GeometryCoordinateSubchainClosed",
            geometry_domain_closed,
            True,
            "anchor input、dyadic/phase 坐标输入域已闭合；当前缺口不是几何坐标。",
            SIGNED_SLOT,
        ),
        row(
            "SignedValueSubchainStillOpen",
            signed_value_open,
            False,
            "signed weight slot value、coefficient assignment、basis word value map 均未给出非循环赋值公式。",
            COEFFICIENT_ASSIGNMENT,
        ),
        row(
            "OriginIdentityReturnsToRowLevel",
            origin_return_open,
            False,
            "basis word signed coefficient 来源恒等式与 primitive summand 来源恒等式会合，仍需逐行原始生成表。",
            ROW_TABLE,
        ),
        row(
            "SameRowBridgeImportedButNotProof",
            same_row_imported,
            False,
            "same-row 桥接已说明 word/coefficient 必须同一行同源，但它也回收到逐行原始生成表。",
            ROW_TABLE,
        ),
        row(
            "ReverseAndZeroRowRecoveryStillBlocked",
            reverse_blocked,
            True,
            "不能用 payment 反推、早期零行覆盖或来源环自证 signed coefficient 来源。",
            NONCIRCULAR_GUARD,
        ),
        row(
            "ExistingSubcycleCountsAsProof",
            False,
            False,
            "该闭环只定位了最窄缺口，不能作为行/列命题无条件证明。",
            NONCIRCULAR_GUARD,
        ),
        row(
            "NoncircularRowLevelGenerationCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交独立于本闭环的逐行 clean-core 原始 signed coefficient 生成表。",
            ROW_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "严格自足线仍缺非循环 signed coefficient 来源输入；外部线仍需 DStructure/Rankin 独立验收。",
            f"({ROW_TABLE} WITH {NONCIRCULAR_GUARD}) AND {DSTRUCTURE_GATE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 signed value 子循环同步证书。"""
    data = {
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "emitter": load_json("prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"),
        "primitive_coeff": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "basis_source": load_json("prime-matrix-strict-acyclic-seed-basis-weight-source-formula-router.json"),
        "internal": load_json("prime-matrix-strict-acyclic-seed-internal-arithmetic-basis-expansion-router.json"),
        "alphabet": load_json("prime-matrix-strict-acyclic-seed-basis-alphabet-ledger-router.json"),
        "word_generation": load_json("prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json"),
        "word_constructor": load_json("prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json"),
        "basis_word_formula": load_json("prime-matrix-strict-acyclic-seed-basis-word-formula-router.json"),
        "word_coordinate": load_json("prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"),
        "signed_slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "slot_value": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "coefficient_assignment": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "value_map": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "origin_identity": load_json("prime-matrix-strict-acyclic-seed-basis-word-origin-identity-router.json"),
        "same_row": load_json("prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "reverse": load_json("prime-matrix-clean-core-reverse-provenance-functor-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    cycle_detected = rows[0]["closed"] is True
    geometry_closed = rows[1]["closed"] is True
    return {
        "certificate_type": "prime_matrix_strict_acyclic_signed_value_cycle_sync_router",
        "status": "acyclic_signed_value_cycle_synced_to_noncircular_row_level_generation_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "acyclic_signed_value_subcycle_detected": cycle_detected,
        "geometry_coordinate_subchain_closed": geometry_closed,
        "existing_subcycle_counts_as_proof": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "noncircular_pre_cauchy_signed_coefficient_origin_input_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "current_frontier": ROW_TABLE,
        "required_noncircular_guard": NONCIRCULAR_GUARD,
        "next_direct_attack_target": ROW_TABLE,
        "terminal_return_if_no_noncircular_input": TERMINAL_RETURN,
        "dstructure_rankin_gate": DSTRUCTURE_GATE,
        "cycle_edges": cycle_edges(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 acyclic signed value/slot/value-map 子链完整同步：几何坐标域已闭合，"
            "但 signed coefficient 赋值链从 row-level 表下钻后，经 signed slot、coefficient assignment、"
            "value map、basis word 来源恒等式又返回同一个 row-level 表。这个回流不是证明。"
            "下一步若继续严格自足，必须提交独立于本闭环的逐行 clean-core 原始 signed coefficient 生成表；"
            "否则该分支只能按命名纪律回流终端家族。"
        ),
        "frontier_statement": (
            f"当前前沿仍是 `{ROW_TABLE}`，但必须附加非循环守门 `{NONCIRCULAR_GUARD}`："
            "不得通过 signed slot/value map/source identity 再回到 row-level 表来证明自身。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic signed value 子循环同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_signed_value_subcycle_detected={fmt_bool(result['acyclic_signed_value_subcycle_detected'])}",
        f"geometry_coordinate_subchain_closed={fmt_bool(result['geometry_coordinate_subchain_closed'])}",
        f"existing_subcycle_counts_as_proof={fmt_bool(result['existing_subcycle_counts_as_proof'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        "noncircular_pre_cauchy_signed_coefficient_origin_input_proved="
        f"{fmt_bool(result['noncircular_pre_cauchy_signed_coefficient_origin_input_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 子循环链条",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["cycle_edges"]:
        lines.append(
            "| `{source}` | `{target}` |".format(
                source=table_cell(item["from"]),
                target=table_cell(item["to"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 当前前沿",
            "",
            result["frontier_statement"],
            "",
            "严格自足下一步：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "WITH",
            result["required_noncircular_guard"],
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_noncircular_input"],
            "```",
            "",
            "仍需独立验收门：",
            "",
            "```text",
            result["dstructure_rankin_gate"],
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
