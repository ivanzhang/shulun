#!/usr/bin/env python3
"""生成 tail gap 全整数 margin 分裂证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_integer_margin_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-integer-margin-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-integer-margin-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-integer-margin-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-integer-margin-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.json",
    DOCS / "prime-matrix-firstbreak-stable-tail-gap-router.json",
    DOCS / "prime-matrix-firstbreak-lowstep-tail-capacity-router.json",
]

NORMALIZED_HARDPOINT = "NormalizedTailGapPositiveOrDenseTailReturnPDEC"
INTEGER_MARGIN = "NormalizedIntegerTailMarginFunctionalLedger"
PRIME_DOMINATION = "PrimeTailDominatedByIntegerTailEnvelopeLedger"
EARLY_HALF = "EarlyHalfSupportTailCannotSaturateLemma"
MARGIN_CRITERION = "IntegerMarginPositiveBranchCriterionLedger"
LATE_DENSE = "IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC"

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

REDUCED_NORMALIZED = (
    f"{INTEGER_MARGIN} AND {PRIME_DOMINATION} AND {EARLY_HALF} "
    f"AND {MARGIN_CRITERION} AND {LATE_DENSE}"
)
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
    """构造整数 margin 分裂判定表。"""
    imported = previous.get("next_direct_attack_target") == NORMALIZED_HARDPOINT
    normalized = previous.get("tail_index_change_of_variables_closed") is True
    return [
        row(
            "NormalizedTailGapImported",
            imported,
            False,
            "上一层把正 gap 硬点压成 q=H+r 的一维 prime-tail functional。",
            NORMALIZED_HARDPOINT,
        ),
        row(
            "OneDimensionalTailImported",
            normalized,
            normalized,
            "已得到 C_tail=sum_{prime q=H+r<P} min(L,r)ceil((P-1)/(H+r))。",
            EXACT_TAIL,
        ),
        row(
            "IntegerMarginFunctionalClosed",
            True,
            True,
            "定义 G_int=L(P-1)-C_all，其中 C_all=sum_{1<=r<y}min(L,r)ceil((P-1)/(P-y+r))。",
            INTEGER_MARGIN,
        ),
        row(
            "PrimeTailDominatedByIntegerTailClosed",
            True,
            True,
            "因 prime tail 是 integer tail 的子和，C_tail<=C_all，故 G'=L(P-1)-C_tail>=G_int。",
            PRIME_DOMINATION,
        ),
        row(
            "PositiveBranchCriterionClosed",
            True,
            True,
            "若 G_int>R_named，则 G=L(P-1)-C_tail-R_named>0。",
            MARGIN_CRITERION,
        ),
        row(
            "EarlyHalfPureTailCannotSaturateClosed",
            True,
            True,
            "若 P 为奇素数且 y<=floor(P/2)，则 ceil((P-1)/(P-y+r))<=2，故 G_int>=L(P-2y+L)>0。",
            EARLY_HALF,
        ),
        row(
            "LateSupportOrNamedReturnStillOpen",
            False,
            False,
            "仍未排斥 y>floor(P/2) 的 late-support dense-tail，或 R_named 吃掉整数 margin 的命名 return 质量。",
            LATE_DENSE,
        ),
        row(
            "NormalizedTailGapReduced",
            True,
            False,
            "NormalizedTailGapPositiveOrDenseTailReturnPDEC 被压成整数 margin、prime/integer 支配、前半支撑 tail 不饱和，以及 late-support/named-return PDEC。",
            REDUCED_NORMALIZED,
        ),
        row(
            "NormalizedPositiveGapProved",
            False,
            False,
            "本步没有证明全局 G>0；只关闭前半支撑的 pure-tail 饱和解释，并把失败口径集中到 late support 或 R_named。",
            LATE_DENSE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥 late-support dense-tail/named-return 质量，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造整数 margin 分裂证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.json")
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
        "归一化 tail gap 被继续压成全整数 margin。由于 prime tail 是 integer tail 的子和，"
        "只要 G_int=L(P-1)-C_all 超过命名 return 质量 R_named，就得到正 gap。"
        "特别地，当首破裂 y 仍在前半支撑 y<=floor(P/2) 时，所有 tail carrier 都满足 "
        "ceil((P-1)/(P-y+r))<=2，从而 G_int>=L(P-2y+L)>0；因此 pure tail 本身不能吃满零块义务。"
        "剩余硬点集中到 late-support dense-tail 或 R_named 过大。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_integer_margin_router",
        "status": "normalized_tail_gap_reduced_to_integer_margin_or_late_support_dense_tail_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": NORMALIZED_HARDPOINT,
        "hardpoint_after_router": REDUCED_NORMALIZED,
        "normalized_tail_gap_imported": previous.get("next_direct_attack_target") == NORMALIZED_HARDPOINT,
        "one_dimensional_tail_imported": previous.get("tail_index_change_of_variables_closed") is True,
        "integer_margin_functional_closed": True,
        "prime_tail_dominated_by_integer_tail_closed": True,
        "positive_branch_criterion_closed": True,
        "early_half_support_tail_cannot_saturate_closed": True,
        "integer_margin_positive_globally_proved": False,
        "late_support_dense_tail_named_return_pdec_excluded": False,
        "normalized_positive_gap_proved": False,
        "row_column_unconditional_closed": False,
        "integer_margin_formulas": {
            "C_all": "sum_{1<=r<y} min(L,r) ceil((P-1)/(P-y+r))",
            "G_int": "L(P-1)-C_all",
            "prime_domination": "C_tail<=C_all and G_prime>=G_int",
            "positive_branch": "G_int>R_named => G>0",
            "early_half_bound": "y<=floor(P/2) => C_all<=L(2y-L-1) and G_int>=L(P-2y+L)>0",
        },
        "next_direct_attack_target": LATE_DENSE,
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
        "# Prime Matrix tail gap 全整数 margin 分裂证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"normalized_tail_gap_imported={fmt_bool(cert['normalized_tail_gap_imported'])}",
        f"one_dimensional_tail_imported={fmt_bool(cert['one_dimensional_tail_imported'])}",
        f"integer_margin_functional_closed={fmt_bool(cert['integer_margin_functional_closed'])}",
        f"prime_tail_dominated_by_integer_tail_closed={fmt_bool(cert['prime_tail_dominated_by_integer_tail_closed'])}",
        f"positive_branch_criterion_closed={fmt_bool(cert['positive_branch_criterion_closed'])}",
        f"early_half_support_tail_cannot_saturate_closed={fmt_bool(cert['early_half_support_tail_cannot_saturate_closed'])}",
        f"integer_margin_positive_globally_proved={fmt_bool(cert['integer_margin_positive_globally_proved'])}",
        f"late_support_dense_tail_named_return_pdec_excluded={fmt_bool(cert['late_support_dense_tail_named_return_pdec_excluded'])}",
        f"normalized_positive_gap_proved={fmt_bool(cert['normalized_positive_gap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全整数 margin",
        "",
        "由上一层",
        "",
        "```text",
        "C_tail = sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r)),",
        "H=P-y.",
        "```",
        "",
        "去掉素数限制，定义",
        "",
        "```text",
        "C_all = sum_{1<=r<y} min(L,r) ceil((P-1)/(P-y+r)),",
        "G_int = L(P-1)-C_all.",
        "```",
        "",
        "于是",
        "",
        "```text",
        "C_tail <= C_all,",
        "G_prime=L(P-1)-C_tail >= G_int.",
        "```",
        "",
        "因此若",
        "",
        "```text",
        "G_int > R_named,",
        "```",
        "",
        "则 `G=G_prime-R_named>0`。",
        "",
        "## 2. 前半支撑不能由 pure tail 饱和",
        "",
        "若 `P` 为奇素数且",
        "",
        "```text",
        "y <= floor(P/2),",
        "```",
        "",
        "则对所有 `1<=r<y`，有",
        "",
        "```text",
        "P-y+r > (P-1)/2,",
        "ceil((P-1)/(P-y+r)) <= 2.",
        "```",
        "",
        "又 `1<=L<=y`，所以",
        "",
        "```text",
        "C_all <= 2 sum_{1<=r<y} min(L,r)",
        "      = L(2y-L-1),",
        "G_int >= L(P-2y+L) > 0.",
        "```",
        "",
        "这说明在前半支撑中，tail envelope 即使按全整数上界也不能吃满 `L(P-1)`。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        f"{NORMALIZED_HARDPOINT}",
        f"  -> {INTEGER_MARGIN}",
        f"  AND {PRIME_DOMINATION}",
        f"  AND {EARLY_HALF}",
        f"  AND {MARGIN_CRITERION}",
        f"  AND {LATE_DENSE}",
        "```",
        "",
        "真正剩余是 late-support dense-tail，或 `R_named` 吃掉整数 margin 的命名 return 质量。",
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
            "- 本证书没有证明全局 `G>0`。",
            "- 本证书只证明 prime tail 被 integer tail 支配，并关闭前半支撑 pure-tail 饱和解释。",
            "- `IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC` 仍未闭合。",
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
