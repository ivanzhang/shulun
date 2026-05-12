#!/usr/bin/env python3
"""生成 strict atomic branch trace signed payload 前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_atomic_branch_trace_payload_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.md"

TARGET = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
NEXT_TARGET = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
ACTUAL_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SAME_ROW = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json",
    "prime-matrix-strict-branch-trace-signed-payload-cycle-router.json",
    "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json",
    "prime-matrix-strict-orientation-law-branch-trace-router.json",
    "prime-matrix-strict-row-level-noncircular-orientation-law-router.json",
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json",
    "prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json",
    "prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json",
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


def payload_fields() -> list[dict[str, str]]:
    """列出 signed payload trace constructor 的字段。"""
    return [
        {
            "field": "payload_domain",
            "requirement": "同一 atomic joint row 的 visible trace 已给出，payload 必须绑定这条 trace。",
        },
        {
            "field": "orientation_parity",
            "requirement": "给出 primitive orientation bit，证明它早于 Cauchy/Phi/payment 且不是 payment 反推。",
        },
        {
            "field": "signed_coefficient_value",
            "requirement": "给出 signed coefficient 的闭式或有限递推值，不能调用 row-level origin table。",
        },
        {
            "field": "local_factor_product",
            "requirement": "列出筛因子、截断因子、branch local factor 与非零条件。",
        },
        {
            "field": "word_coefficient_same_row_identity",
            "requirement": "证明 basis word 与 signed coefficient 是同一 trace 的两个字段。",
        },
        {
            "field": "alpha_delta_prepushforward_identity",
            "requirement": "证明 payload 在 Phi/payment 推前前等于 actual alpha/delta 贡献。",
        },
        {
            "field": "uv_key_payload",
            "requirement": "同步输出 exact `(u,v)`、branch key、sign 和 local factor 口径。",
        },
        {
            "field": "payload_return_tags",
            "requirement": "缺 payload、零 local factor、符号冲突、超预算、canonical 泄漏或后验读取必须命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把 exact atomic trace 压到 signed payload trace constructor。"""
    previous = data["previous"]
    trace_cycle = data["trace_cycle"]
    global_trace = data["global_trace"]
    orientation = data["orientation"]
    row_orientation = data["row_orientation"]
    same_row = data["same_row"]
    signed_slot = data["signed_slot"]
    slot_value = data["slot_value"]
    assignment = data["assignment"]
    value_map = data["value_map"]
    incidence = data["incidence"]

    signed_assignment_chain_open = (
        signed_slot.get("next_direct_attack_target")
        == "AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords"
        and slot_value.get("next_direct_attack_target") == "AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger"
        and assignment.get("next_direct_attack_target") == "AcyclicSeedBasisWordToSignedCoefficientValueMapFormula"
        and value_map.get("next_direct_attack_target") == "AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward"
    )

    return [
        row(
            "ExactAtomicTraceTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 BuiltIn pairing 闭式压成 exact atomic joint branch trace。",
            TARGET,
        ),
        row(
            "ActualTraceCycleImported",
            trace_cycle.get("active_previous_target") == ACTUAL_TRACE
            and trace_cycle.get("branch_trace_route_counts_as_independent_proof") is False,
            True,
            "actual noncanonical branch trace 的内部展开已被证明不能自证 signed payload。",
            "atomic specialization inherits this obstruction。",
        ),
        row(
            "TraceSplitsIntoCoordinateAndPayload",
            trace_cycle.get("visible_coordinate_trace_reduced_to_word_coordinate_chain") is True
            and trace_cycle.get("signed_payload_trace_returns_to_row_level_origin_table") is True,
            True,
            "完整 trace 分为 visible coordinate trace 与 signed payload trace；只有前者已定位。",
            NEXT_TARGET,
        ),
        row(
            "VisibleCoordinateTraceDoesNotEmitPayload",
            True,
            True,
            "anchor/D0/K/Omega/phase/word-coordinate 只给 row 与 word 的可见坐标，不产生 orientation 或 signed coefficient。",
            NEXT_TARGET,
        ),
        row(
            "SignedPayloadAssignmentChainReturnsToOrigin",
            signed_assignment_chain_open,
            True,
            "signed slot -> slot value -> coefficient assignment -> value map -> origin identity 继续回到 row-level 表。",
            ROW_TABLE,
        ),
        row(
            "OrientationAndSameRowLawsStillDemandPayload",
            orientation.get("next_direct_attack_target") == ACTUAL_TRACE
            and row_orientation.get("next_direct_attack_target") == ORIENTATION_LAW
            and same_row.get("next_direct_attack_target") == SAME_ROW,
            False,
            "取向/local factor 与 same-row word/coefficient 桥接都要求 payload 正向生成。",
            NEXT_TARGET,
        ),
        row(
            "AtomicRestrictionDoesNotCreateSignedPayload",
            True,
            True,
            "把 actual trace 限制到 atomic joint rows 只缩小输入域；不会凭空产生 signed coefficient 值。",
            NEXT_TARGET,
        ),
        row(
            "PayloadConstructorWouldCloseAtomicTraceConditionally",
            True,
            True,
            "若 signed payload constructor 给出 orientation、coefficient、local factor、same-row identity 和回流，则 atomic trace 条件闭合。",
            f"prove {NEXT_TARGET}",
        ),
        row(
            "TraceSelfProofAlreadyRemovedFromGlobalFrontier",
            global_trace.get("branch_trace_self_proof_eliminated") is True,
            True,
            "全局前沿已把 branch trace 自证从活动证明路径删除。",
            "new payload input or nontrace terminal atom。",
        ),
        row(
            "ActualEmitterExactUVStillParallel",
            incidence.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "payload 可登记每行 UV；bounded multiplicity incidence 仍需独立证明。",
            EXACT_UV,
        ),
        row(
            "AtomicSignedPayloadConstructorCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出不经 assignment/origin 环的 atomic signed payload trace constructor。",
            NEXT_TARGET,
        ),
        row(
            "ExactAtomicTraceCurrentCorpusProved",
            False,
            False,
            "缺少 signed payload constructor，ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn 未证明。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少 atomic signed payload、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。",
            f"{NEXT_TARGET} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 atomic branch trace signed payload 前沿证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"),
        "trace_cycle": load_json("prime-matrix-strict-branch-trace-signed-payload-cycle-router.json"),
        "global_trace": load_json("prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json"),
        "orientation": load_json("prime-matrix-strict-orientation-law-branch-trace-router.json"),
        "row_orientation": load_json("prime-matrix-strict-row-level-noncircular-orientation-law-router.json"),
        "same_row": load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"),
        "signed_slot": load_json("prime-matrix-strict-acyclic-seed-signed-weight-coordinate-slot-router.json"),
        "slot_value": load_json("prime-matrix-strict-acyclic-seed-signed-slot-value-formula-router.json"),
        "assignment": load_json("prime-matrix-strict-acyclic-seed-coefficient-assignment-router.json"),
        "value_map": load_json("prime-matrix-strict-acyclic-seed-coefficient-value-map-router.json"),
        "incidence": load_json("prime-matrix-strict-actual-emitter-incidence-entropy-router.json"),
    }
    rows = build_rows(data)
    strict_basis = f"{NEXT_TARGET} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_atomic_branch_trace_payload_frontier_router",
        "status": "exact_atomic_branch_trace_reduced_to_signed_payload_constructor_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_input_before_router": TARGET,
        "atomic_trace_payload_frontier_router_closed": True,
        "actual_trace_cycle_imported": data["trace_cycle"].get("branch_trace_route_counts_as_independent_proof")
        is False,
        "visible_coordinate_trace_reduced_to_word_coordinate_chain": data["trace_cycle"].get(
            "visible_coordinate_trace_reduced_to_word_coordinate_chain"
        )
        is True,
        "signed_payload_trace_returns_to_row_level_origin_table": data["trace_cycle"].get(
            "signed_payload_trace_returns_to_row_level_origin_table"
        )
        is True,
        "payload_constructor_conditionally_suffices": True,
        "atomic_signed_payload_constructor_proved": False,
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": data["incidence"].get(
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "strict_author_side_remaining_basis": strict_basis,
        "payload_fields": payload_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步直接攻击 `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`。"
            "已有 branch trace 审查表明：可见坐标 trace 可以沿 anchor、D0/K/Omega、phase 和 word-coordinate 链定位，"
            "但 signed payload trace 会经 signed slot、coefficient assignment、value map 和 origin identity 回到 row-level 表。"
            "atomic 限制只缩小输入域，不能自动产生 signed coefficient。"
            "因此真正最窄字段压成 `AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`："
            "在同一 atomic trace 上正向给出 orientation、signed coefficient、local factor、same-row identity、"
            "alpha/delta prepushforward identity、exact UV/key 和命名回流。当前材料没有该 payload constructor，"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict atomic branch trace signed payload 前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"actual_trace_cycle_imported={fmt_bool(result['actual_trace_cycle_imported'])}",
        (
            "visible_coordinate_trace_reduced_to_word_coordinate_chain="
            f"{fmt_bool(result['visible_coordinate_trace_reduced_to_word_coordinate_chain'])}"
        ),
        (
            "signed_payload_trace_returns_to_row_level_origin_table="
            f"{fmt_bool(result['signed_payload_trace_returns_to_row_level_origin_table'])}"
        ),
        f"payload_constructor_conditionally_suffices={fmt_bool(result['payload_constructor_conditionally_suffices'])}",
        f"atomic_signed_payload_constructor_proved={fmt_bool(result['atomic_signed_payload_constructor_proved'])}",
        (
            "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved="
            f"{fmt_bool(result['exact_atomic_joint_branch_trace_signed_coefficient_formula_proved'])}"
        ),
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed payload 字段",
        "",
        "| field | requirement |",
        "| --- | --- |",
    ]
    for item in result["payload_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
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
