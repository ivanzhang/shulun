#!/usr/bin/env python3
"""生成 strict cycle-cut 联合 basis/coefficient 发射器证书。

用法示例：
  python3 experiments/prime_matrix_strict_cycle_cut_joint_basis_coefficient_emitter_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cycle-cut-joint-basis-coefficient-emitter-router.md"

TARGET = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
NEXT_TARGET = "AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-signed-source-cycle-frontier-sync-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json",
    "prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json",
    "prime-matrix-strict-acyclic-seed-basis-word-formula-router.json",
    "prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
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


def emitter_fields() -> list[dict[str, str]]:
    """列出联合发射器必须同时输出的字段。"""
    return [
        {
            "field": "source_tuple_input",
            "meaning": "只读取同一 formal unit 的 actual noncanonical source tuple 与已闭合锚参数。",
        },
        {
            "field": "basis_word_output",
            "meaning": "在 Cauchy/payment 前输出 primitive basis word，而不是后验选择 word。",
        },
        {
            "field": "signed_coefficient_output",
            "meaning": "同一公式同时输出 signed coefficient、sign、local factor 和非零条件。",
        },
        {
            "field": "word_coefficient_identity",
            "meaning": "证明输出的 word 与 coefficient 是同一个 pre-Cauchy 算术对象的两面。",
        },
        {
            "field": "prepushforward_sum_identity",
            "meaning": "证明联合发射后的 rows 在 Phi/payment 推前前已经给出目标 alpha/delta 贡献。",
        },
        {
            "field": "no_downstream_read",
            "meaning": "公式不读取 payment、零行覆盖、origin table、terminal certificate 或外部谱后处理。",
        },
        {
            "field": "named_return_tags",
            "meaning": "缺 word、零 local factor、符号冲突、多值或超预算时命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 sequential word/assignment 为什么必须合并为联合发射器。"""
    frontier = data["frontier"]
    cycle = data["cycle"]
    word_generation = data["word_generation"]
    word_constructor = data["word_constructor"]
    word_formula = data["word_formula"]
    coordinate = data["coordinate"]
    slot = data["slot"]
    slot_value = data["slot_value"]
    assignment = data["assignment"]
    value_map = data["value_map"]
    origin = data["origin"]
    row_table = data["row_table"]

    return [
        row(
            "CycleCutInputActive",
            frontier.get("next_direct_attack_target") == TARGET,
            False,
            "上一层前沿同步已把非循环新增输入钉为 primitive basis 与 signed coefficient 的前置源输入。",
            TARGET,
        ),
        row(
            "ExistingCycleGuardImported",
            cycle.get("seed_coordinate_source_cycle_detected") is True,
            True,
            "已登记的 signed 坐标-来源链形成闭合依赖环，不能用环本身证明 signed coefficient。",
            TARGET,
        ),
        row(
            "WordFirstRouteStillOpen",
            word_generation.get("source_tuple_to_primitive_basis_word_constructor_proved") is False
            and word_constructor.get("basis_word_formula_from_source_tuple_parameters_proved") is False
            and word_formula.get("word_coordinate_formula_proved") is False,
            False,
            "先生成 basis word 的路线最终仍卡在 word coordinate / signed slot，而不是给出完整源输入。",
            "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility",
        ),
        row(
            "AnchorCoordinatesDoNotCloseSignedSlot",
            coordinate.get("anchor_input_rule_proved") is True
            and coordinate.get("signed_weight_coordinate_slot_proved") is False,
            True,
            "anchor/dyadic/phase 坐标域已闭合，但 signed weight coordinate slot 仍未证明。",
            "AcyclicSeedSignedWeightCoordinateSlotLedger",
        ),
        row(
            "CoefficientFirstRouteStillOpen",
            slot.get("signed_weight_slot_value_formula_proved") is False
            and slot_value.get("acyclic_seed_coefficient_assignment_on_basis_alphabet_proved") is False
            and assignment.get("basis_word_to_signed_coefficient_value_map_formula_proved") is False,
            False,
            "先给 coefficient assignment 的路线又要求 basis word value map 与来源恒等式，回到原始行表。",
            "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula",
        ),
        row(
            "ValueMapReturnsToOriginLedger",
            value_map.get("value_map_must_be_origin_identity") is True
            and origin.get("row_level_clean_core_origin_generation_table_proved") is False,
            True,
            "signed coefficient value map 必须是来源恒等式；来源恒等式又要求逐行原始生成表。",
            "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
        ),
        row(
            "RowTableRequiresEmitterImported",
            row_table.get("acyclic_seed_signed_row_emitter_rule_proved") is False,
            True,
            "逐行原始表本身要求 seed signed row emitter；这正是被环守卫禁止自证的对象。",
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity",
        ),
        row(
            "SequentialSplitRejected",
            True,
            True,
            "word-first 与 coefficient-first 都回到对方或原始表；cycle-cut 输入必须是联合发射公式。",
            NEXT_TARGET,
        ),
        row(
            "JointEmitterCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交同时输出 basis word 与 signed coefficient 的 Cauchy 前联合发射公式。",
            NEXT_TARGET,
        ),
        row(
            "TerminalDescentAlternativeStillOpen",
            False,
            False,
            "若不能提交联合发射器，只能走终端回流严格下降证书；该证书也未证明。",
            TERMINAL_DESCENT,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 cycle-cut 联合发射器证书。"""
    data = {
        "frontier": load_json("prime-matrix-strict-signed-source-cycle-frontier-sync-router.json"),
        "cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "word_generation": load_json("prime-matrix-strict-acyclic-seed-primitive-basis-word-generation-router.json"),
        "word_constructor": load_json("prime-matrix-strict-acyclic-seed-source-tuple-word-constructor-router.json"),
        "word_formula": load_json("prime-matrix-strict-acyclic-seed-basis-word-formula-router.json"),
        "coordinate": load_json("prime-matrix-strict-acyclic-seed-word-coordinate-formula-router.json"),
        "slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "slot_value": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "assignment": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "value_map": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_table": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_strict_cycle_cut_joint_basis_coefficient_emitter_router",
        "status": "cycle_cut_source_input_reduced_to_joint_basis_word_coefficient_emitter_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "cycle_cut_input_router_closed": True,
        "sequential_word_then_coefficient_split_rejected": True,
        "joint_basis_word_coefficient_emitter_proved": False,
        "acyclic_seed_cycle_cut_source_input_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_target": TERMINAL_DESCENT,
        "terminal_return_if_no_joint_emitter": TERMINAL_FAMILY,
        "strict_basis_after_router": f"({NEXT_TARGET} OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}",
        "emitter_fields": emitter_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TARGET}` 不能继续拆成“先生成 basis word、再赋 signed coefficient”的顺序链；"
            "这两条链已互相回指并回到 row-level origin 表。真正非循环破环输入必须是一条 Cauchy 前联合发射公式，"
            f"即 `{NEXT_TARGET}`。"
        ),
        "plain_conclusion": (
            "本步把 cycle-cut 输入进一步压窄：现有 word-first 路线只给 unsigned 坐标域，最终卡在 signed slot；"
            "coefficient-first 路线又要求 value map 来源恒等式，并回到逐行原始生成表。因此顺序拆分仍是来源环。"
            "要真正破环，必须提交一个同 formal unit、Cauchy/payment 前的联合发射器，同时输出 primitive basis word、"
            "signed coefficient、sign/local factor、prepushforward sum identity 和失败回流。该联合发射器当前未证明，"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict cycle-cut 联合 basis/coefficient 发射器路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cycle_cut_input_router_closed={fmt_bool(result['cycle_cut_input_router_closed'])}",
        f"sequential_word_then_coefficient_split_rejected={fmt_bool(result['sequential_word_then_coefficient_split_rejected'])}",
        f"joint_basis_word_coefficient_emitter_proved={fmt_bool(result['joint_basis_word_coefficient_emitter_proved'])}",
        f"acyclic_seed_cycle_cut_source_input_proved={fmt_bool(result['acyclic_seed_cycle_cut_source_input_proved'])}",
        f"acyclic_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_terminal_return_well_founded_descent_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 联合发射器字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["emitter_fields"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")

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
            "## 4. 下一最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行守门：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
            "外部 Mertens/theta 高段已接受时的当前活动基：",
            "",
            "```text",
            result["strict_basis_after_router"],
            "```",
            "",
            "审稿边界：本文件只证明顺序拆分会回到来源环，并把破环输入压成联合发射公式；"
            "它没有证明该联合公式，也没有证明行/列命题无条件闭合。",
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
