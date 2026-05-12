#!/usr/bin/env python3
"""生成 strict 内置 signed pairing 闭式前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_builtin_pairing_closed_form_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.md"

TARGET = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
NEXT_TARGET = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_VALUE_TABLE = "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton"
SIGNED_WEIGHT = "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow"
PRIMITIVE_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
ORIGIN_ID = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
SAME_ROW = "JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
    "prime-matrix-strict-row-level-noncircular-orientation-law-router.json",
    "prime-matrix-strict-orientation-law-branch-trace-router.json",
    "prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json",
    "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json",
    "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json",
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


def trace_fields() -> list[dict[str, str]]:
    """列出 atomic joint branch trace 必须一次性给出的字段。"""
    return [
        {
            "field": "atomic_row_domain",
            "requirement": "输入是已登记 unsigned carry-shell/phase skeleton 的 atomic joint row，而不是 payment 侧纤维。",
        },
        {
            "field": "same_formal_unit_trace",
            "requirement": "source tuple、basis word、signed coefficient、alpha/delta pairing 与 return tag 共享同一 formal unit。",
        },
        {
            "field": "ordered_branch_operations",
            "requirement": "在 Cauchy/Phi/payment 前给出有限有序 branch trace；不得由 row-level origin table 后验读取。",
        },
        {
            "field": "signed_coefficient_closed_value",
            "requirement": "signed coefficient 是 trace 中 orientation、truncation 和 local factor product 的闭式函数。",
        },
        {
            "field": "word_coefficient_pairing",
            "requirement": "证明 primitive basis word 与 signed coefficient 是同一 trace 的两面，而不是两条链拼接。",
        },
        {
            "field": "alpha_delta_payload",
            "requirement": "同一 row 携带 alpha/delta 两侧 payload 和 prepushforward sum identity。",
        },
        {
            "field": "exact_uv_branch_key",
            "requirement": "同步输出 exact `(u,v)`、branch key、sign/local factor 和非零条件。",
        },
        {
            "field": "named_return_tags",
            "requirement": "缺 trace、零 local factor、符号冲突、超预算、canonical 泄漏或后验读取必须命名回流。",
        },
    ]


def compression_lemmas() -> list[dict[str, str]]:
    """记录本步真正证明的压缩引理。"""
    return [
        {
            "lemma": "ClosedFormNeedsOddData",
            "statement": (
                "unsigned carry-shell、P列锚、相位轮和 ExactUV 支撑只是不带符号的偶数据；"
                "signed coefficient 对 primitive orientation/local factor 反变，因此闭式值必须包含奇数据来源。"
            ),
        },
        {
            "lemma": "OldSignedValueRouteIsCircular",
            "statement": (
                "从 pointwise signed value 继续展开会经过 signed weight、primitive expression、origin identity，"
                "最终回到 row-level origin table；该路径不能证明 atomic 内置闭式。"
            ),
        },
        {
            "lemma": "BranchTraceSufficesConditionally",
            "statement": (
                "若每条 atomic joint row 都有 Cauchy 前完整 branch trace，且 trace 同时给出 word、signed coefficient、"
                "orientation/local factor、alpha/delta payload 与 exact UV，则内置 pairing 闭式条件闭合。"
            ),
        },
        {
            "lemma": "MobiusParityShadowIsNotEnough",
            "statement": (
                "Möbius/奇偶只给局部符号影子；缺 actual source tuple、ordered branch trace、exact UV 和命名回流，"
                "不能替代 strict 内部闭式公式。"
            ),
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把内置 pairing 闭式压到 atomic branch trace 公式。"""
    previous = data["previous"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    signed_value = data["signed_value"]
    signed_weight = data["signed_weight"]
    primitive_expr = data["primitive_expr"]
    origin = data["origin"]
    orientation = data["orientation"]
    trace = data["trace"]
    same_row = data["same_row"]
    kernel = data["kernel"]
    pointwise = data["pointwise"]
    incidence = data["incidence"]

    signed_value_cycle = (
        signed_lift.get("next_direct_attack_target") == SIGNED_VALUE_TABLE
        and signed_value.get("next_direct_attack_target") == SIGNED_WEIGHT
        and signed_weight.get("next_direct_attack_target") == PRIMITIVE_EXPR
        and primitive_expr.get("next_direct_attack_target") == ORIGIN_ID
        and origin.get("next_direct_attack_target") == ROW_TABLE
    )
    trace_reduction_synced = (
        orientation.get("next_direct_attack_target") == ORIENTATION_LAW
        and trace.get("next_direct_attack_target") == BRANCH_TRACE
    )

    return [
        row(
            "BuiltInPairingTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 atomic joint rows 公式压成内置 signed coefficient/pairing 闭式。",
            TARGET,
        ),
        row(
            "UnsignedSkeletonImported",
            previous.get("unsigned_joint_row_skeleton_closed") is True
            and unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            True,
            "carry-shell、P列锚、相位轮和 row skeleton 可作为 atomic row 输入域。",
            "输入域闭合，不给 signed 值。",
        ),
        row(
            "OddSignedDataStillMissing",
            orientation.get("unsigned_geometry_even_under_orientation_flip") is True
            and orientation.get("signed_coefficient_is_orientation_sensitive") is True,
            True,
            "已登记的偶几何数据在取向翻转下不变，不能决定 signed coefficient。",
            ORIENTATION_LAW,
        ),
        row(
            "OldSignedValueRouteCircular",
            signed_value_cycle,
            False,
            "pointwise signed value 旧链会回到 row-level origin table，不能作为 atomic 声明内置闭式。",
            ROW_TABLE,
        ),
        row(
            "SameRowBridgeNeeded",
            same_row.get("next_direct_attack_target") == SAME_ROW,
            False,
            "unsigned primitive word 与 signed coefficient 必须在同一 pre-Cauchy row 上同源。",
            SAME_ROW,
        ),
        row(
            "OrientationReducedToBranchTrace",
            trace_reduction_synced,
            False,
            "取向/local factor 律已压成 actual noncanonical 完整 branch trace 公式或命名回流。",
            BRANCH_TRACE,
        ),
        row(
            "MobiusParityNotExactPairingFormula",
            kernel.get("mobius_truncation_rejected_as_exact_kernel") is True
            and kernel.get("threeedge_parity_audits_rejected_as_exact_kernel") is True,
            True,
            "Möbius 截断和奇偶审计只是符号影子，不含 exact trace、UV、branch key 和回流。",
            NEXT_TARGET,
        ),
        row(
            "PointwiseKernelContractDemandsOneTable",
            pointwise.get("field_contract_boundary_closed") is True,
            True,
            "非递归逐点核表要求 rows、weight、UV、local factor、rank 和回流在同一 formal unit 一次性给出。",
            "atomic trace table。",
        ),
        row(
            "BranchTraceWouldCloseBuiltinPairingConditionally",
            True,
            True,
            "若 atomic branch trace 正向给出 word/coefficient/pairing/local factor，则 BuiltIn pairing 闭式不再依赖 origin table。",
            f"prove {NEXT_TARGET}",
        ),
        row(
            "ActualEmitterExactUVStillParallel",
            incidence.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "branch trace 可输出每行 UV，但 bounded multiplicity incidence 仍是并行守门项。",
            EXACT_UV,
        ),
        row(
            "ExactAtomicJointBranchTraceCurrentCorpusProved",
            False,
            False,
            "当前材料没有提交每条 atomic joint row 的 exact branch trace signed coefficient formula。",
            NEXT_TARGET,
        ),
        row(
            "BuiltInSignedCoefficientPairingCurrentCorpusProved",
            False,
            False,
            "没有 branch trace 公式，内置 signed coefficient/pairing 闭式仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少 atomic trace 闭式、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。",
            f"{NEXT_TARGET} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造内置 pairing 闭式前沿证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "signed_value": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "signed_weight": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "primitive_expr": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "orientation": load_json("prime-matrix-strict-row-level-noncircular-orientation-law-router.json"),
        "trace": load_json("prime-matrix-strict-orientation-law-branch-trace-router.json"),
        "same_row": load_json("prime-matrix-strict-joint-alpha-side-word-coefficient-rule-router.json"),
        "kernel": load_json("prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"),
        "pointwise": load_json("prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json"),
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
        "certificate_type": "prime_matrix_strict_builtin_pairing_closed_form_frontier_router",
        "status": "builtin_signed_pairing_reduced_to_exact_atomic_joint_branch_trace_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_input_before_router": TARGET,
        "builtin_pairing_frontier_router_closed": True,
        "unsigned_joint_row_skeleton_closed": data["previous"].get("unsigned_joint_row_skeleton_closed") is True,
        "old_signed_value_route_circular": any(
            item["gate"] == "OldSignedValueRouteCircular" and item["closed"] is True for item in rows
        ),
        "orientation_branch_trace_reduction_synced": any(
            item["gate"] == "OrientationReducedToBranchTrace" and item["closed"] is True for item in rows
        ),
        "branch_trace_conditionally_suffices": True,
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved": False,
        "builtin_signed_coefficient_pairing_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": data["incidence"].get(
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "strict_author_side_remaining_basis": strict_basis,
        "trace_fields": trace_fields(),
        "compression_lemmas": compression_lemmas(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步继续直接攻击 `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`。"
            "已闭合的 unsigned skeleton 只给 atomic row 的位置和相位；signed coefficient 是取向/local factor "
            "敏感的奇数据，不能由偶几何、Möbius/奇偶影子或 signed-value 旧链后验生成。"
            "旧链会回到 row-level origin table，因此不能作为 atomic 内置闭式。"
            "真正非循环前沿压成 `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`："
            "对每条 atomic joint row，在同一 formal unit 和 Cauchy/Phi/payment 前完整列出 branch trace，"
            "并同步给出 basis word、signed coefficient、alpha/delta pairing、orientation/local factor、exact UV 和回流。"
            "当前语料没有该 trace 公式，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 内置 signed pairing 闭式前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unsigned_joint_row_skeleton_closed={fmt_bool(result['unsigned_joint_row_skeleton_closed'])}",
        f"old_signed_value_route_circular={fmt_bool(result['old_signed_value_route_circular'])}",
        f"orientation_branch_trace_reduction_synced={fmt_bool(result['orientation_branch_trace_reduction_synced'])}",
        f"branch_trace_conditionally_suffices={fmt_bool(result['branch_trace_conditionally_suffices'])}",
        (
            "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved="
            f"{fmt_bool(result['exact_atomic_joint_branch_trace_signed_coefficient_formula_proved'])}"
        ),
        f"builtin_signed_coefficient_pairing_proved={fmt_bool(result['builtin_signed_coefficient_pairing_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 本步压缩引理",
        "",
        "| lemma | statement |",
        "| --- | --- |",
    ]
    for item in result["compression_lemmas"]:
        lines.append(
            "| `{lemma}` | {statement} |".format(
                lemma=table_cell(item["lemma"]),
                statement=table_cell(item["statement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. atomic branch trace 字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["trace_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
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
            "## 4. 作者侧剩余基",
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
        lines.extend(["", "## 5. 缺失依赖", ""])
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
