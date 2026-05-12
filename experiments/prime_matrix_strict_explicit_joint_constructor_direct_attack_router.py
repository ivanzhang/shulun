#!/usr/bin/env python3
"""生成 strict 显式 joint 构造器直接攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_explicit_joint_constructor_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.md"

TARGET = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
NEW_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
JOINT_ALPHA = "JointAlphaSidePrimitiveWordCoefficientRuleLedger"
JOINT_SAME_ROW = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json",
    "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json",
    "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
    "prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json",
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json",
    "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON 证书；缺失时保留空对象用于审计。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记直接读取的上游证书哈希。"""
    hashes: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            hashes[f"docs/monograph/{name}"] = sha256(path)
    return hashes


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def fixed_point_chain() -> list[dict[str, str]]:
    """列出显式 joint 构造器在当前语料中的自回流链。"""
    return [
        {"from": TARGET, "to": JOINT_ALPHA},
        {"from": JOINT_ALPHA, "to": JOINT_SAME_ROW},
        {"from": JOINT_SAME_ROW, "to": ROW_TABLE},
        {"from": ROW_TABLE, "to": SIGNED_EMITTER},
        {"from": SIGNED_EMITTER, "to": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"},
        {"from": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward", "to": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"},
        {"from": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows", "to": "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy"},
        {"from": "AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy", "to": "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger"},
        {"from": "AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger", "to": "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment"},
        {"from": "AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment", "to": "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility"},
        {"from": "AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility", "to": "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility"},
        {"from": "AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility", "to": "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters"},
        {"from": "AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters", "to": "AcyclicSeedSignedWeightCoordinateSlotLedger"},
        {"from": "AcyclicSeedSignedWeightCoordinateSlotLedger", "to": "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"},
        {"from": "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords", "to": "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"},
        {"from": "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger", "to": "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"},
        {"from": "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula", "to": "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"},
        {"from": "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward", "to": ROW_TABLE},
    ]


def required_formula_fields() -> list[dict[str, str]]:
    """显式新公式工件必须一次性给出的字段。"""
    return [
        {
            "field": "domain",
            "meaning": "actual noncanonical source tuple 的精确定义域，不能读取 canonical、terminal 或后验 payment 数据。",
        },
        {
            "field": "row_index_formula",
            "meaning": "同一 formal unit 内 alpha/delta primitive rows 的正向索引和排序公式。",
        },
        {
            "field": "basis_word_and_signed_coefficient",
            "meaning": "每一行同时输出 primitive basis word 与 signed coefficient，不能先分别生成再后验配对。",
        },
        {
            "field": "uv_branch_sign_local_factor",
            "meaning": "同一行同步输出 exact (u,v)、branch key、sign 与非零 local factor。",
        },
        {
            "field": "pre_cauchy_pairing_identity",
            "meaning": "在 Cauchy/dispersion/Phi 推前前证明 alpha/delta 两侧配成 actual emitter 系数。",
        },
        {
            "field": "failure_return_tags",
            "meaning": "缺行、零 local factor、跨来源、后验读取、超预算和 unmatched pair 必须落入已登记命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """直接攻坚显式 joint 构造器，判断是否出现非循环新公式。"""
    pair = data["pair"]
    table = data["table"]
    joint_decl = data["joint_decl"]
    joint_explicit = data["joint_explicit"]
    joint_alpha = data["joint_alpha"]
    same_row = data["same_row"]
    row_level = data["row_level"]
    signed_fixed = data["signed_fixed"]
    joint_fixed = data["joint_fixed"]
    leaf_sync = data["leaf_sync"]
    terminal = data["terminal"]

    target_active = (
        pair.get("first_productive_input_after_router") == TARGET
        or table.get("first_productive_input_after_router") == TARGET
        or joint_decl.get("next_direct_attack_target") == TARGET
    )
    reduced_to_alpha = joint_explicit.get("next_direct_attack_target") == JOINT_ALPHA
    alpha_to_same_row = joint_alpha.get("next_direct_attack_target") == JOINT_SAME_ROW
    same_row_to_table = same_row.get("next_direct_attack_target") == ROW_TABLE
    table_to_emitter = row_level.get("next_direct_attack_target") == SIGNED_EMITTER
    signed_source_fixed = signed_fixed.get("current_internal_route_is_signed_source_fixed_point") is True
    joint_fixed_detected = (
        joint_fixed.get("cycle_cut_joint_route_returns_to_row_level_fixed_point") is True
        or leaf_sync.get("joint_constructor_path_is_fixed_point_without_new_formula") is True
    )
    terminal_schema = terminal.get("terminal_return_well_founded_descent_schema_closed") is True

    return [
        row(
            "ExplicitJointConstructorTargetActive",
            target_active,
            False,
            "pair-energy 非循环对齐与逐点核表字段合同都把首个生产性工件钉为显式 joint alpha/delta 构造器。",
            TARGET,
        ),
        row(
            "JointDeclarationBoundaryImported",
            joint_decl.get("same_source_tuple_container_closed") is True,
            True,
            "同一 source tuple 容器与 joint payload 字段边界已闭合。",
            "字段边界不是构造公式。",
        ),
        row(
            "JointConstructorReducedToAlphaSide",
            reduced_to_alpha,
            False,
            "直接展开 TARGET 后，第一实际字段是 alpha-side primitive word/coefficient 规则。",
            JOINT_ALPHA,
        ),
        row(
            "AlphaSideReducedToSameRow",
            alpha_to_same_row,
            False,
            "alpha-side 规则的未闭合处是 unsigned word skeleton 与 signed coefficient 在同一 pre-Cauchy row 上同源。",
            JOINT_SAME_ROW,
        ),
        row(
            "SameRowReducedToRowLevelTable",
            same_row_to_table,
            False,
            "same-row 同源恒等式要求完整逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowLevelTableReducedToSignedEmitter",
            table_to_emitter,
            False,
            "逐行表必须由无环 source seed 自带 signed row emitter 产生。",
            SIGNED_EMITTER,
        ),
        row(
            "SignedSourceFixedPointImported",
            signed_source_fixed,
            True,
            "继续内部展开 signed row emitter 会回到 row-level/signed-source 来源固定点。",
            "不能用固定点自证显式构造器。",
        ),
        row(
            "JointConstructorCurrentRouteIsFixedPoint",
            joint_fixed_detected,
            True,
            "现有 joint-alpha 路线已经被同步为回到 signed-source 固定点。",
            NEW_FORMULA,
        ),
        row(
            "NewExplicitFormulaArtifactPresent",
            False,
            False,
            "当前语料没有提交新的 actual joint alpha/delta 正向公式工件。",
            NEW_FORMULA,
        ),
        row(
            "TerminalDescentAlternativeSchemaImported",
            terminal_schema,
            False,
            "若不提交新公式，唯一非循环替代是终端回流 well-founded 下降证书及其叶子防火墙。",
            TERMINAL_DESCENT,
        ),
        row(
            "ExplicitJointConstructorRuleCurrentCorpusProved",
            False,
            False,
            "当前直接攻坚未得到非循环构造公式，只得到固定点判定和精确剩余。",
            f"{NEW_FORMULA} OR {TERMINAL_DESCENT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "没有显式新公式、终端下降、ExactUV、RatePreservation 和 DStructure 独立门，不能升级为无条件闭合。",
            f"({NEW_FORMULA} OR {TERMINAL_DESCENT}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造本轮直接攻坚结果。"""
    data = {
        "pair": load_json("prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json"),
        "table": load_json("prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json"),
        "joint_decl": load_json("prime-matrix-strict-joint-declaration-constructor-sync-router.json"),
        "joint_explicit": load_json("prime-matrix-strict-joint-explicit-alpha-delta-rule-sync-router.json"),
        "joint_alpha": load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"),
        "same_row": load_json("prime-matrix-strict-joint-alpha-same-row-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "signed_fixed": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "joint_fixed": load_json("prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json"),
        "leaf_sync": load_json("prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json"),
        "terminal": load_json("prime-matrix-strict-acyclic-terminal-descent-firewall-router.json"),
    }
    rows = build_rows(data)
    strict_basis = f"({NEW_FORMULA} OR {TERMINAL_DESCENT}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_explicit_joint_constructor_direct_attack_router",
        "status": "explicit_joint_constructor_direct_attack_reduced_to_new_formula_or_terminal_descent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "explicit_joint_constructor_target_active": any(r["gate"] == "ExplicitJointConstructorTargetActive" and r["closed"] for r in rows),
        "joint_declaration_sync_imported": data["joint_decl"].get("joint_declaration_constructor_sync_router_closed") is True,
        "joint_rule_reduced_to_alpha_side": data["joint_explicit"].get("next_direct_attack_target") == JOINT_ALPHA,
        "joint_alpha_side_route_returns_to_signed_source_fixed_point": any(
            r["gate"] == "JointConstructorCurrentRouteIsFixedPoint" and r["closed"] for r in rows
        ),
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "explicit_joint_constructor_rule_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TARGET,
        "first_nonrecursive_formula_artifact_after_router": NEW_FORMULA,
        "noncycle_alternative_after_router": TERMINAL_DESCENT,
        "strict_active_basis_after_router": strict_basis,
        "fixed_point_chain": fixed_point_chain(),
        "required_new_formula_fields": required_formula_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本轮直接攻击 {TARGET}：若沿现有 joint declaration / alpha-side / same-row / row-level 表继续展开，"
            "路线回到 signed-source 来源固定点，不能形成非循环证明。当前语料没有新的 actual joint alpha/delta "
            f"正向公式工件；因此该硬点没有闭合。下一最小可生产输入是 {NEW_FORMULA}，"
            f"或者改走非循环替代 {TERMINAL_DESCENT}。二者之外仍必须保留 ExactUV、RatePreservation 与 DStructure 门。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict 显式 joint 构造器直接攻坚证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "joint_declaration_sync_imported",
        "joint_rule_reduced_to_alpha_side",
        "joint_alpha_side_route_returns_to_signed_source_fixed_point",
        "new_explicit_joint_constructor_formula_artifact_present",
        "explicit_joint_constructor_rule_proved",
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved",
        "rate_preservation_ledger_proved",
        "dstructure_independent_gate_closed",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 当前自回流链")
    lines.append("")
    lines.append("| from | to |")
    lines.append("| --- | --- |")
    for item in result["fixed_point_chain"]:
        lines.append(f"| {cell(item['from'])} | {cell(item['to'])} |")
    lines.append("")
    lines.append("## 2. 新公式工件最低字段")
    lines.append("")
    lines.append("| field | meaning |")
    lines.append("| --- | --- |")
    for item in result["required_new_formula_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.append("")
    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## 4. 当前严格活动基")
    lines.append("")
    lines.append("```text")
    lines.append(result["strict_active_basis_after_router"])
    lines.append("```")
    lines.append("")
    lines.append("审稿边界：本文件是对显式 joint 构造器的直接攻坚判定。它没有把固定点冒充为证明，也没有声称行/列命题已经无条件闭合。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"wrote={OUT_JSON.relative_to(ROOT)}")
    print(f"wrote={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
