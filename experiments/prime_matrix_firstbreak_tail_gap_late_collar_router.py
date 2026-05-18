#!/usr/bin/env python3
"""生成 late-support tail gap collar 分裂证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_late_collar_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-late-collar-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-late-collar-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-late-collar-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-late-collar-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-integer-margin-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.json",
    DOCS / "prime-matrix-firstbreak-stable-tail-gap-router.json",
]

LATE_DENSE = "IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC"
LATE_COORD = "LateSupportExcessCoordinateLedger"
REGULAR_DEFECT = "RegularTailTwoUnitEndpointDefectLedger"
CORE_EXCESS = "LateCoreExcessFunctionalLedger"
LATE_MARGIN = "LateCollarMarginExactFormulaLedger"
LATE_COLLAR = "DeepLateShortCollarOrCoreExcessNamedReturnPDEC"

INTEGER_MARGIN = "NormalizedIntegerTailMarginFunctionalLedger"
PRIME_DOMINATION = "PrimeTailDominatedByIntegerTailEnvelopeLedger"
EARLY_HALF = "EarlyHalfSupportTailCannotSaturateLemma"
MARGIN_CRITERION = "IntegerMarginPositiveBranchCriterionLedger"
TAIL_INDEX = "TailIndexChangeOfVariablesLedger"
EXACT_TAIL = "ExactPrimeTailEnvelopeOneDimensionalLedger"
GAP_SEPARATION = "StableTailGapNamedReturnSeparationLedger"
ZERO_MASS = "ZeroBlockCoverObligationMassLedger"
STABLE_TOTAL = "StableSourceTotalAfterNamedReturnsLedger"
GAP_FORMULA = "ExplicitStableTailGapFunctionalLedger"
PARTITION = "StableHistoryLowTailMassPartitionLedger"
TAIL_WINDOW = "LargeStepTailTerminalWindowEnvelopeLedger"
LOW_FROM_TAIL = "LowStepStableMassLowerBoundFromTotalMinusTailEnvelope"
RAW_BALANCE = "ArrivalNonarrivalSourceLayerBalanceLedger"
LOW_STEP_ARRIVES = "LowStepStableHistoryAlwaysArrivesLedger"
RAW_LOWER = "RawArrivalMassLowerBoundFromLowStepHistory"
FIBER_ENVELOPE = "ArrivalQuotientFiberMultiplicityEnvelopeLedger"
WEIGHTED_LOWER = "WeightedArrivalImageLowerBoundFromFiberEnvelope"
HIGH_FIBER = "HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn"
COLLISION_RETURN = "ArrivalCollisionOrDuplicatePaymentReturnLedger"
UNIT_INCIDENCE = "SourceTaggedArrivalUnitIncidenceLedger"
AP_SUCCESSOR = "StableHistoryAPSuccessorDichotomyLedger"
TERMINAL_NONARRIVAL = "TerminalNonarrivalLargeStepEscapePDECOrSAE"
NO_LOSS = "ZeroBlockHistoryProjectionNoLossLedger"
STABLE_OR_SWITCH = "StableLowCarrierPaymentTableOrHistorySwitchPDEC"
SHORT_BLOCK = "ShortZeroBlockSingletonSAESummability"
PAYMENT_INJECTION = "LowCarrierActualPaymentInjectionWithoutEnvelopeReuse"
STRICT_GAP = "LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC"
DENSE_TABLE = "DenseLowCarrierResidueTablePDECExclusion"
SPARSE_CELL = "SparseLowCarrierResidueCellSAESummability"
LOW_SAE = "LowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "HighCarrierRankDeficitCapacityBoundOrSingletonSAE"
NONREPLAY_SAE = "NonreplaySparseFirstBreakSAESummability"
MOVING_CARRIER = "MovingCarrierPhaseSlipPDECExclusion"
SQUARE_INPUT = "NoZeroRowAtXEqualsP_PlusOneRowAfterSquare"
SIGNED_ROW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

REDUCED_LATE = f"{LATE_COORD} AND {REGULAR_DEFECT} AND {CORE_EXCESS} AND {LATE_MARGIN} AND {LATE_COLLAR}"
REDUCED_NORMALIZED = f"{INTEGER_MARGIN} AND {PRIME_DOMINATION} AND {EARLY_HALF} AND {MARGIN_CRITERION} AND {REDUCED_LATE}"
REDUCED_POSITIVE = f"{TAIL_INDEX} AND {EXACT_TAIL} AND {GAP_SEPARATION} AND {REDUCED_NORMALIZED}"
REDUCED_TAIL_GAP = f"{ZERO_MASS} AND {STABLE_TOTAL} AND {GAP_FORMULA} AND {REDUCED_POSITIVE}"
REDUCED_LOW_STEP = f"{PARTITION} AND {TAIL_WINDOW} AND {LOW_FROM_TAIL} AND {REDUCED_TAIL_GAP}"
REDUCED_RAW = f"{RAW_BALANCE} AND {LOW_STEP_ARRIVES} AND {RAW_LOWER} AND {REDUCED_LOW_STEP}"
REDUCED_QUOTIENT = f"{FIBER_ENVELOPE} AND {REDUCED_RAW} AND {WEIGHTED_LOWER} AND {HIGH_FIBER}"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 late collar 分裂判定表。"""
    imported = previous.get("next_direct_attack_target") == LATE_DENSE
    return [
        row(
            "LateDenseImported",
            imported,
            False,
            "上一层把剩余压成 late-support dense-tail 或 named-return 质量。",
            LATE_DENSE,
        ),
        row(
            "LateCoordinateClosed",
            True,
            True,
            "写 P=2m+1，H=P-y。late branch 为 y>m；令 D=2y-P，E=y-m-1=(D-1)/2。",
            LATE_COORD,
        ),
        row(
            "RegularTailEndpointDefectClosed",
            True,
            True,
            "当 r>E 且 r<y-1 时，ceil((P-1)/(H+r))=2；端点 r=y-1 给 q=P-1，ceil=1。",
            REGULAR_DEFECT,
        ),
        row(
            "LateCoreExcessFunctionalClosed",
            True,
            True,
            "所有超过二重的 tail 质量只在 1<=r<=E；定义 X_core=sum min(L,r)(ceil((P-1)/(H+r))-2)。",
            CORE_EXCESS,
        ),
        row(
            "LateMarginExactFormulaClosed",
            True,
            True,
            "C_all=L(2y-L-1)+X_core-min(L,y-1)，故 G_int=L(L-D)+min(L,y-1)-X_core。",
            LATE_MARGIN,
        ),
        row(
            "PositiveLateMarginCriterionClosed",
            True,
            True,
            "若 L(L-D)+min(L,y-1)>X_core+R_named，则 G>0。",
            LATE_MARGIN,
        ),
        row(
            "DeepLateCollarOrCoreExcessStillOpen",
            False,
            False,
            "若不能正 gap，则必须是 margin 非正的 deep-late short collar，或 X_core/R_named 吃掉该 margin。",
            LATE_COLLAR,
        ),
        row(
            "LateDenseReduced",
            True,
            False,
            "IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC 被压成 late 坐标、端点缺口、core-excess functional、精确 margin 与 deep-collar/core-excess PDEC。",
            REDUCED_LATE,
        ),
        row(
            "LateDenseProved",
            False,
            False,
            "本步没有排斥 deep-late short collar，也没有证明 X_core/R_named 不会吃掉 margin。",
            LATE_COLLAR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 deep-late collar、core-excess/named-return 质量，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 late collar 分裂证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-integer-margin-router.json")
    rows = build_rows(previous)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} "
        f"AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} "
        f"AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} "
        f"AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} "
        f"AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "late-support tail gap 被压成精确 collar 公式。写 P=2m+1、D=2y-P、E=(D-1)/2。"
        "超过二重的 tail 只来自短 core 1<=r<=E；regular tail 在 r=y-1 还有一个端点缺口。"
        "因此 G_int=L(L-D)+min(L,y-1)-X_core。若这个 margin 大于 R_named，则正 gap 已成立；"
        "否则反例必须进入 deep-late short collar，或由 core-excess/named-return 质量承担。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_late_collar_router",
        "status": "late_support_tail_gap_reduced_to_core_excess_or_deep_late_collar_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": LATE_DENSE,
        "hardpoint_after_router": REDUCED_LATE,
        "late_dense_imported": previous.get("next_direct_attack_target") == LATE_DENSE,
        "late_coordinate_closed": True,
        "regular_tail_endpoint_defect_closed": True,
        "late_core_excess_functional_closed": True,
        "late_margin_exact_formula_closed": True,
        "positive_late_margin_criterion_closed": True,
        "deep_late_collar_excluded": False,
        "core_excess_named_return_pdec_excluded": False,
        "late_dense_tail_named_return_proved": False,
        "row_column_unconditional_closed": False,
        "late_margin_formulas": {
            "P": "P=2m+1",
            "D": "D=2y-P",
            "E": "E=y-m-1=(D-1)/2",
            "X_core": "sum_{1<=r<=E} min(L,r)(ceil((P-1)/(P-y+r))-2)",
            "C_all": "L(2y-L-1)+X_core-min(L,y-1)",
            "G_int": "L(L-D)+min(L,y-1)-X_core",
            "positive_branch": "L(L-D)+min(L,y-1)>X_core+R_named => G>0",
            "failure_branch": "G<=0 => L(L-D)+min(L,y-1)<=X_core+R_named",
        },
        "next_direct_attack_target": LATE_COLLAR,
        "parallel_attack_targets": [
            HIGH_FIBER,
            COLLISION_RETURN,
            TERMINAL_NONARRIVAL,
            PAYMENT_INJECTION,
            STRICT_GAP,
            DENSE_TABLE,
            SPARSE_CELL,
            LOW_SAE,
            HIGH_RANK,
            NONREPLAY_SAE,
            MOVING_CARRIER,
        ],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix late-support tail gap collar 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"late_dense_imported={fmt_bool(cert['late_dense_imported'])}",
        f"late_coordinate_closed={fmt_bool(cert['late_coordinate_closed'])}",
        f"regular_tail_endpoint_defect_closed={fmt_bool(cert['regular_tail_endpoint_defect_closed'])}",
        f"late_core_excess_functional_closed={fmt_bool(cert['late_core_excess_functional_closed'])}",
        f"late_margin_exact_formula_closed={fmt_bool(cert['late_margin_exact_formula_closed'])}",
        f"positive_late_margin_criterion_closed={fmt_bool(cert['positive_late_margin_criterion_closed'])}",
        f"deep_late_collar_excluded={fmt_bool(cert['deep_late_collar_excluded'])}",
        f"core_excess_named_return_pdec_excluded={fmt_bool(cert['core_excess_named_return_pdec_excluded'])}",
        f"late_dense_tail_named_return_proved={fmt_bool(cert['late_dense_tail_named_return_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. late 坐标",
        "",
        "在 late branch 写",
        "",
        "```text",
        "P=2m+1,  H=P-y,  y>m,",
        "D=2y-P,  E=y-m-1=(D-1)/2.",
        "```",
        "",
        "当 `r>E` 且 `r<y-1` 时，`H+r>m` 且 `H+r<P-1`，因此",
        "",
        "```text",
        "ceil((P-1)/(H+r))=2.",
        "```",
        "",
        "端点 `r=y-1` 给出 `H+r=P-1`，所以",
        "",
        "```text",
        "ceil((P-1)/(H+r))=1.",
        "```",
        "",
        "## 2. core-excess functional",
        "",
        "超过二重的整数 tail 只可能来自短 core：",
        "",
        "```text",
        "1<=r<=E.",
        "```",
        "",
        "定义",
        "",
        "```text",
        "X_core=sum_{1<=r<=E} min(L,r)(ceil((P-1)/(P-y+r))-2).",
        "```",
        "",
        "于是全整数 tail 精确分解为",
        "",
        "```text",
        "C_all = L(2y-L-1)+X_core-min(L,y-1).",
        "```",
        "",
        "因此",
        "",
        "```text",
        "G_int = L(P-1)-C_all",
        "      = L(L-D)+min(L,y-1)-X_core.",
        "```",
        "",
        "若",
        "",
        "```text",
        "L(L-D)+min(L,y-1) > X_core+R_named,",
        "```",
        "",
        "则 `G=G_prime-R_named>0`。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        f"{LATE_DENSE}",
        f"  -> {LATE_COORD}",
        f"  AND {REGULAR_DEFECT}",
        f"  AND {CORE_EXCESS}",
        f"  AND {LATE_MARGIN}",
        f"  AND {LATE_COLLAR}",
        "```",
        "",
        "真正剩余是 deep-late short collar，或 `X_core/R_named` 吃掉 late margin。",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 新活动基",
            "",
            "inverse-alignment 回流分支更新为：",
            "",
            "```text",
            cert["reduced_inverse_alignment_branch"],
            "```",
            "",
            "合并 exact-UV/source-rank 前沿后的活动基：",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书没有排斥 deep-late short collar。",
            "- 本证书没有证明 `X_core` 或 `R_named` 不会吃掉 late margin。",
            "- `DeepLateShortCollarOrCoreExcessNamedReturnPDEC` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成 JSON、ledger 和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
