#!/usr/bin/env python3
"""生成 deep-late collar 与 core-excess quotient 层分裂证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_deep_collar_layer_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-deep-collar-layer-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-late-collar-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-integer-margin-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.json",
]

DEEP_COLLAR = "DeepLateShortCollarOrCoreExcessNamedReturnPDEC"
MIRROR_COLLAR = "DeepLateCollarMirrorContainmentLedger"
CROSS_MARGIN = "CrossCollarPositiveMarginCriterionLedger"
CORE_LAYER = "CoreExcessQuotientLayerDecompositionLedger"
LAYER_CONCENTRATION = "CoreExcessLayerConcentrationOrNamedReturnPDEC"
NEW_TARGET = "SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC"

LATE_COORD = "LateSupportExcessCoordinateLedger"
REGULAR_DEFECT = "RegularTailTwoUnitEndpointDefectLedger"
CORE_EXCESS = "LateCoreExcessFunctionalLedger"
LATE_MARGIN = "LateCollarMarginExactFormulaLedger"
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

REDUCED_DEEP = f"{MIRROR_COLLAR} AND {CROSS_MARGIN} AND {CORE_LAYER} AND {LAYER_CONCENTRATION} AND {NEW_TARGET}"
REDUCED_LATE = f"{LATE_COORD} AND {REGULAR_DEFECT} AND {CORE_EXCESS} AND {LATE_MARGIN} AND {REDUCED_DEEP}"
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
    """构造 deep collar 分裂判定表。"""
    imported = previous.get("next_direct_attack_target") == DEEP_COLLAR
    return [
        row(
            "DeepCollarImported",
            imported,
            False,
            "上一层把 late-support 剩余压成 deep-late collar，或 X_core/R_named 吃掉 margin。",
            DEEP_COLLAR,
        ),
        row(
            "MirrorCollarEquivalenceClosed",
            True,
            True,
            "令 x0=y-L、H=P-y、D=2y-P。L<=D 当且仅当 x0>=H，即 B=[x0,y-1] 完全落在自镜像 collar [H,y-1]。",
            MIRROR_COLLAR,
        ),
        row(
            "CrossCollarPositiveMarginClosed",
            True,
            True,
            "若 L>D 且 X_core+R_named < L(L-D)+min(L,y-1)，则正 gap 已成立。",
            CROSS_MARGIN,
        ),
        row(
            "CoreLayerDecompositionClosed",
            True,
            True,
            "令 h=H+r，k(h)=ceil((P-1)/h)-2；X_core=sum_{h=H+1}^m min(L,h-H)k(h)，并按 k 的 quotient 层精确分解。",
            CORE_LAYER,
        ),
        row(
            "CoreOrNamedConsumptionClosed",
            True,
            False,
            "若 L>D 但正 gap 失败，则 X_core+R_named 必至少吃掉 M=L(L-D)+min(L,y-1) 的全部 margin。",
            LAYER_CONCENTRATION,
        ),
        row(
            "DeepCollarOrCoreLayerStillOpen",
            False,
            False,
            "剩余不是一般 late tail，而是自镜像 collar 内部相位问题，或 quotient core 层/命名 return 的显式 margin 消耗。",
            NEW_TARGET,
        ),
        row(
            "DeepCollarReduced",
            True,
            False,
            "DeepLateShortCollarOrCoreExcessNamedReturnPDEC 被压成 collar mirror containment、cross-collar margin、quotient-layer 分解和 core/named 消耗。",
            REDUCED_DEEP,
        ),
        row(
            "DeepCollarProved",
            False,
            False,
            "本步没有排斥自镜像 collar，也没有排斥 quotient core 层集中或 R_named 吃掉 margin。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥自镜像 collar 或 core-layer/named-return 质量，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 deep collar 分裂证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-late-collar-router.json")
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
        "deep-late 剩余被拆成几何 collar 与 core quotient 层。若 L<=D，则 x0=y-L>=P-y，"
        "零块完全落在自镜像 collar [P-y,y-1]；若 L>D，则只有 X_core 或 R_named 消耗掉 "
        "M=L(L-D)+min(L,y-1) 才能阻止正 gap。并且 X_core 按 h=H+r 的 quotient 层 "
        "k(h)=ceil((P-1)/h)-2 精确分解。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_deep_collar_layer_router",
        "status": "deep_late_reduced_to_self_mirror_collar_or_core_quotient_layer_consumption_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": DEEP_COLLAR,
        "hardpoint_after_router": REDUCED_DEEP,
        "deep_collar_imported": previous.get("next_direct_attack_target") == DEEP_COLLAR,
        "mirror_collar_equivalence_closed": True,
        "cross_collar_positive_margin_closed": True,
        "core_layer_decomposition_closed": True,
        "core_or_named_consumption_closed": True,
        "self_mirror_collar_excluded": False,
        "core_layer_concentration_excluded": False,
        "deep_late_closed": False,
        "row_column_unconditional_closed": False,
        "deep_collar_formulas": {
            "x0": "x0=y-L",
            "mirror_collar": "L<=D <=> x0>=H=P-y <=> B subset [H,y-1]",
            "cross_margin": "L>D and X_core+R_named < L(L-D)+min(L,y-1) => G>0",
            "h_coordinate": "h=H+r, H+1<=h<=m",
            "layer_weight": "k(h)=ceil((P-1)/h)-2",
            "core_layers": "I_k={h: ceil((P-1)/h)=k+2}",
            "core_decomposition": "X_core=sum_{k>=1} k sum_{h in I_k} min(L,h-H)",
            "failure_branch": "if L>D and G<=0 then X_core+R_named>=L(L-D)+min(L,y-1)",
        },
        "next_direct_attack_target": NEW_TARGET,
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
        "# Prime Matrix deep-late collar quotient-layer 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"deep_collar_imported={fmt_bool(cert['deep_collar_imported'])}",
        f"mirror_collar_equivalence_closed={fmt_bool(cert['mirror_collar_equivalence_closed'])}",
        f"cross_collar_positive_margin_closed={fmt_bool(cert['cross_collar_positive_margin_closed'])}",
        f"core_layer_decomposition_closed={fmt_bool(cert['core_layer_decomposition_closed'])}",
        f"core_or_named_consumption_closed={fmt_bool(cert['core_or_named_consumption_closed'])}",
        f"self_mirror_collar_excluded={fmt_bool(cert['self_mirror_collar_excluded'])}",
        f"core_layer_concentration_excluded={fmt_bool(cert['core_layer_concentration_excluded'])}",
        f"deep_late_closed={fmt_bool(cert['deep_late_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. deep-late collar 等价式",
        "",
        "令",
        "",
        "```text",
        "x0=y-L,  H=P-y,  D=2y-P.",
        "```",
        "",
        "则",
        "",
        "```text",
        "L<=D",
        "<=> y-L >= y-D",
        "<=> x0 >= P-y = H.",
        "```",
        "",
        "所以 deep-late short collar 等价于",
        "",
        "```text",
        "B=[x0,y-1] subset [H,y-1].",
        "```",
        "",
        "这把几何剩余从“late 支撑”缩成自镜像 collar 内部相位问题。",
        "",
        "## 2. 跨出 collar 时的正 margin 门",
        "",
        "若 `L>D`，则跨出 collar。记",
        "",
        "```text",
        "M = L(L-D)+min(L,y-1).",
        "```",
        "",
        "上一层精确式给出",
        "",
        "```text",
        "G_int = M-X_core.",
        "```",
        "",
        "因此",
        "",
        "```text",
        "X_core+R_named < M  =>  G>0.",
        "```",
        "",
        "若反例仍存在，则必须有",
        "",
        "```text",
        "X_core+R_named >= M.",
        "```",
        "",
        "## 3. core-excess quotient 层",
        "",
        "令",
        "",
        "```text",
        "h=H+r,  H+1<=h<=m,",
        "k(h)=ceil((P-1)/h)-2.",
        "```",
        "",
        "定义 quotient 层",
        "",
        "```text",
        "I_k={h: ceil((P-1)/h)=k+2}.",
        "```",
        "",
        "则",
        "",
        "```text",
        "X_core=sum_{k>=1} k sum_{h in I_k} min(L,h-H).",
        "```",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        f"{DEEP_COLLAR}",
        f"  -> {MIRROR_COLLAR}",
        f"  AND {CROSS_MARGIN}",
        f"  AND {CORE_LAYER}",
        f"  AND {LAYER_CONCENTRATION}",
        f"  AND {NEW_TARGET}",
        "```",
        "",
        "真正剩余是自镜像 collar 内部相位，或 quotient core 层/命名 return 对 margin 的显式消耗。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
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
            "## 7. 诚实边界",
            "",
            "- 本证书没有排斥自镜像 collar 内部相位问题。",
            "- 本证书没有排斥 quotient core 层集中或 `R_named` 吃掉 margin。",
            "- `SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
