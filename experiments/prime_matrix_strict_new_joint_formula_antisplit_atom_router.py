#!/usr/bin/env python3
"""生成 strict 新 joint 公式反分裂原子证书。

用法示例：
  python3 experiments/prime_matrix_strict_new_joint_formula_antisplit_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-new-joint-formula-antisplit-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-new-joint-formula-antisplit-atom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-new-joint-formula-antisplit-atom-router.md"

NEW_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
ANTISPLIT = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
ALPHA_MAP = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SIGNED_LIFT = "AlphaFormulaSignedCoefficientLiftLedger"
SIGNED_VALUE = "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
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


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能当成证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def antisplit_fields() -> list[dict[str, str]]:
    """反分裂新公式必须一次性给出的字段。"""
    return [
        {
            "field": "single_row_source_tuple",
            "requirement": "同一 actual noncanonical source tuple 在同一 formal unit 内直接生成 joint primitive row。",
        },
        {
            "field": "basis_word_and_signed_coefficient_together",
            "requirement": "同一公式同时输出 basis word 与 signed coefficient；不得先走 alpha-side word 再后验补 coefficient。",
        },
        {
            "field": "alpha_delta_pairing_payload",
            "requirement": "同一行直接携带 alpha/delta 两侧 pairing 数据，而不是由 row-level 表或 signed-source 固定点回推。",
        },
        {
            "field": "uv_key_sign_local_factor",
            "requirement": "同步输出 exact `(u,v)`、branch key、sign/local factor 和非零条件。",
        },
        {
            "field": "prepushforward_identity",
            "requirement": "在 Cauchy、Phi、payment 推前前证明该行贡献等于 actual emitter 系数。",
        },
        {
            "field": "no_split_certificate",
            "requirement": "证明该构造不因分裂为 alpha-side/row-level/signed-source 路径而回到已登记固定点。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步旧分裂路线，并钉出反分裂原子。"""
    terminal = data["terminal"]
    formula_line = data["formula_line"]
    explicit_rule = data["explicit_rule"]
    alpha_side = data["alpha_side"]
    alpha_map = data["alpha_map"]
    alpha_row = data["alpha_row"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    signed_value = data["signed_value"]
    signed_weight = data["signed_weight"]
    primitive_expr = data["primitive_expr"]
    origin = data["origin"]
    row_level = data["row_level"]
    seed_cycle = data["seed_cycle"]
    incidence = data["incidence"]

    return [
        row(
            "NewFormulaTerminalObligationActive",
            terminal.get("next_direct_attack_target") == NEW_FORMULA,
            terminal.get("new_explicit_joint_constructor_formula_artifact_present") is True,
            "上一层已把 strict 内部非循环点压成新显式 joint 公式工件。",
            NEW_FORMULA,
        ),
        row(
            "OldFormulaLineSplitsToExplicitAlphaDelta",
            formula_line.get("next_direct_attack_target")
            == "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter",
            formula_line.get("actual_noncanonical_primitive_constructor_formula_line_proved") is True,
            "旧 actual constructor formula line 先拆成显式 alpha/delta primitive rule。",
            "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter",
        ),
        row(
            "ExplicitAlphaDeltaSplitsToAlphaSide",
            explicit_rule.get("next_direct_attack_target")
            == "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger",
            explicit_rule.get("explicit_alpha_delta_primitive_constructor_rule_proved") is True,
            "显式 alpha/delta 规则又先要求 alpha-side primitive rule；delta/pairing 还没有对象。",
            "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger",
        ),
        row(
            "AlphaSideSplitsToDeterministicRowMap",
            alpha_side.get("next_direct_attack_target") == ALPHA_MAP,
            alpha_side.get("actual_noncanonical_alpha_side_primitive_rule_proved") is True,
            "alpha-side 规则压到确定性 alpha row 发射映射。",
            ALPHA_MAP,
        ),
        row(
            "DeterministicRowMapSplitsToAnchorPhase",
            alpha_map.get("next_direct_attack_target") == ALPHA_ROW,
            alpha_map.get("deterministic_alpha_primitive_row_emission_map_proved") is True,
            "确定性发射映射的首缺口是把 A/D0/K/Omega/phase_rule 变成 alpha row。",
            ALPHA_ROW,
        ),
        row(
            "AnchorPhaseHasOnlyUnsignedSkeleton",
            alpha_row.get("next_direct_attack_target") == SIGNED_LIFT
            and unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            alpha_row.get("alpha_row_anchor_phase_emission_formula_proved") is True,
            "carry-shell、P列锚、相位轮等只给 unsigned skeleton；signed coefficient 仍开放。",
            SIGNED_LIFT,
        ),
        row(
            "SignedLiftSplitsToPointwiseValueTable",
            signed_lift.get("next_direct_attack_target") == SIGNED_VALUE,
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is True,
            "signed lift 等价于逐 skeleton row 的 signed alpha value table。",
            SIGNED_VALUE,
        ),
        row(
            "SignedValueRouteReturnsToOriginTable",
            signed_value.get("next_direct_attack_target")
            == "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow"
            and signed_weight.get("next_direct_attack_target")
            == "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
            and primitive_expr.get("next_direct_attack_target")
            == "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
            and origin.get("next_direct_attack_target") == ROW_TABLE,
            False,
            "signed value 继续展开会回到 primitive origin identity 与 row-level 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowLevelReturnsToSeedCoordinateCycle",
            row_level.get("next_direct_attack_target")
            == "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
            and seed_cycle.get("seed_coordinate_source_cycle_detected") is True,
            False,
            "row-level/signed-emitter 路线回到 signed 坐标-来源依赖环。",
            "cannot count as new formula。",
        ),
        row(
            "ExactUVDoesNotSupplyFormula",
            incidence.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV incidence 是并行守门项；它不生产 basis word/coefficient joint formula。",
            EXACT_UV,
        ),
        row(
            "AntiSplitFormulaCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交不经 alpha-side/row-level/signed-source 分裂路径的 joint primitive row 公式。",
            ANTISPLIT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "反分裂 joint 公式、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 均未合取闭合。",
            f"{ANTISPLIT} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造新 joint 公式反分裂原子证书。"""
    data = {
        "terminal": load_json("prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"),
        "formula_line": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "alpha_side": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "alpha_map": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "alpha_row": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "signed_value": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "signed_weight": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "primitive_expr": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "row_level": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "seed_cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "incidence": load_json("prime-matrix-strict-actual-emitter-incidence-entropy-router.json"),
    }
    rows = build_rows(data)
    split_route_synced = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "OldFormulaLineSplitsToExplicitAlphaDelta",
            "ExplicitAlphaDeltaSplitsToAlphaSide",
            "AlphaSideSplitsToDeterministicRowMap",
            "DeterministicRowMapSplitsToAnchorPhase",
            "AnchorPhaseHasOnlyUnsignedSkeleton",
            "SignedLiftSplitsToPointwiseValueTable",
            "SignedValueRouteReturnsToOriginTable",
            "RowLevelReturnsToSeedCoordinateCycle",
        }
    )
    strict_basis = f"{ANTISPLIT} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_new_joint_formula_antisplit_atom_router",
        "status": "new_joint_formula_reduced_to_antisplit_joint_row_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "new_formula_target_active": data["terminal"].get("next_direct_attack_target") == NEW_FORMULA,
        "old_split_formula_route_synced": split_route_synced,
        "old_split_formula_route_is_nonproof_cycle": True,
        "antisplit_joint_formula_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": data["incidence"].get(
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ANTISPLIT,
        "strict_author_side_remaining_basis": strict_basis,
        "antisplit_fields": antisplit_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步直接攻 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 的内部形态。"
            "若新公式沿旧路线先拆成 explicit alpha/delta、alpha-side、deterministic row map、anchor-phase、"
            "signed lift、signed value、origin table，则会回到 row-level/signed-source 坐标来源环，不能算新公式。"
            "因此真正最窄原子不是再展开旧 alpha-side 链，而是一个反分裂公式："
            "`NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection`，它必须在同一行同时输出"
            "basis word、signed coefficient、alpha/delta pairing、exact `(u,v)`、key、sign/local factor，且证明不经"
            "已登记固定点。当前语料没有该工件，命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 新 joint 公式反分裂原子",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"new_formula_target_active={fmt_bool(result['new_formula_target_active'])}",
        f"old_split_formula_route_synced={fmt_bool(result['old_split_formula_route_synced'])}",
        f"old_split_formula_route_is_nonproof_cycle={fmt_bool(result['old_split_formula_route_is_nonproof_cycle'])}",
        f"antisplit_joint_formula_proved={fmt_bool(result['antisplit_joint_formula_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分裂路线同步",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 2. 反分裂字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["antisplit_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 作者侧剩余基",
            "",
            "```text",
            result["strict_author_side_remaining_basis"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 4. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
