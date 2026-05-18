#!/usr/bin/env python3
"""生成 stable tail gap 的一维归一化证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_normalization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-normalization-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-normalization-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-normalization-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-stable-tail-gap-router.json",
    DOCS / "prime-matrix-firstbreak-lowstep-tail-capacity-router.json",
    DOCS / "prime-matrix-firstbreak-arrival-raw-mass-layer-router.json",
    DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json",
]

POSITIVE_GAP = "PositiveStableTailGapOrNamedReturnMassPDEC"
TAIL_INDEX = "TailIndexChangeOfVariablesLedger"
EXACT_TAIL = "ExactPrimeTailEnvelopeOneDimensionalLedger"
INTEGER_TAIL = "AllIntegerTailEnvelopeDominatesPrimeTailLedger"
GAP_SEPARATION = "StableTailGapNamedReturnSeparationLedger"
TAIL_POSITIVE = "NormalizedTailGapPositiveOrDenseTailReturnPDEC"
ZERO_MASS = "ZeroBlockCoverObligationMassLedger"
STABLE_TOTAL = "StableSourceTotalAfterNamedReturnsLedger"
GAP_FORMULA = "ExplicitStableTailGapFunctionalLedger"
PARTITION = "StableHistoryLowTailMassPartitionLedger"
TAIL_WINDOW = "LargeStepTailTerminalWindowEnvelopeLedger"
LOW_FROM_TAIL = "LowStepStableMassLowerBoundFromTotalMinusTailEnvelope"
TAIL_ESCAPE = "LargeStepTailTerminalEscapePDECOrSAE"
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
HISTORY_SWITCH = "HistorySwitchPDECOrColumnCRTExclusion"
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

REDUCED_POSITIVE_GAP = f"{TAIL_INDEX} AND {EXACT_TAIL} AND {GAP_SEPARATION} AND {TAIL_POSITIVE}"
REDUCED_TAIL_GAP = f"{ZERO_MASS} AND {STABLE_TOTAL} AND {GAP_FORMULA} AND {REDUCED_POSITIVE_GAP}"
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
    """构造 tail gap 归一化判定表。"""
    imported = previous.get("next_direct_attack_target") == POSITIVE_GAP
    gap_imported = previous.get("explicit_tail_gap_functional_closed") is True
    return [
        row(
            "PositiveGapImported",
            imported,
            False,
            "上一层把 stable tail gap 的直接主攻设为正 gap 或命名 return/PDEC。",
            POSITIVE_GAP,
        ),
        row(
            "ExplicitGapFunctionalImported",
            gap_imported,
            gap_imported,
            "已得到 |S_{q<=H}|>=L(P-1)-R_named-C_tail。",
            GAP_FORMULA,
        ),
        row(
            "TailIndexChangeOfVariablesClosed",
            True,
            True,
            "令 q=H+r。因 H=P-y，行窗口 B∩[P-q,y-1]=B∩[y-r,y-1]，长度精确为 min(L,r)。",
            TAIL_INDEX,
        ),
        row(
            "ExactPrimeTailEnvelopeClosed",
            True,
            True,
            "因此 C_tail=sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r))。",
            EXACT_TAIL,
        ),
        row(
            "AllIntegerDominatingEnvelopeClosed",
            True,
            True,
            "去掉 q 为素数的限制得到安全上界 C_tail<=C_all=sum_{1<=r<P-H} min(L,r) ceil((P-1)/(H+r))。",
            INTEGER_TAIL,
        ),
        row(
            "NamedReturnSeparationClosed",
            True,
            True,
            "gap 可分为 G_prime=L(P-1)-C_tail 与 G=G_prime-R_named；命名 return 质量只进入最后扣除项。",
            GAP_SEPARATION,
        ),
        row(
            "NormalizedPositiveGapStillOpen",
            False,
            False,
            "仍未证明归一化 gap 足够大；若不足，则必须由 prime tail 过密、tail 饱和或 R_named 过大承担。",
            TAIL_POSITIVE,
        ),
        row(
            "PositiveGapReduced",
            True,
            False,
            "PositiveStableTailGapOrNamedReturnMassPDEC 被压成 tail-index 归一化、精确 prime tail envelope、gap 分离和归一化正 gap/稠密 return。",
            REDUCED_POSITIVE_GAP,
        ),
        row(
            "PositiveGapProved",
            False,
            False,
            "本步没有证明正 gap；只把 C_tail 化成一维 r-sum，并把失败形态登记为 dense tail/named return PDEC。",
            TAIL_POSITIVE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需归一化正 gap 或 dense tail/named return 排斥，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 tail gap 归一化证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-stable-tail-gap-router.json")
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
        "positive stable tail gap 被归一化成一维 tail-index 和式。令 q=H+r，H=P-y。"
        "则 P-q=y-r，故 terminal row window B∩[P-q,y-1] 变为 B∩[y-r,y-1]，长度精确为 min(L,r)。"
        "因此 C_tail=sum_{prime q=H+r<P} min(L,r)ceil((P-1)/(H+r))。"
        "剩余硬点不再是窗口几何，而是证明该一维 prime-tail functional 留出正 gap；"
        "若没有，失败只能登记为 dense tail、tail saturation 或 named-return mass PDEC。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_normalization_router",
        "status": "positive_tail_gap_reduced_to_one_dimensional_tail_index_functional_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": POSITIVE_GAP,
        "hardpoint_after_router": REDUCED_POSITIVE_GAP,
        "positive_gap_imported": previous.get("next_direct_attack_target") == POSITIVE_GAP,
        "explicit_gap_functional_imported": previous.get("explicit_tail_gap_functional_closed") is True,
        "tail_index_change_of_variables_closed": True,
        "exact_prime_tail_envelope_closed": True,
        "all_integer_dominating_envelope_closed": True,
        "named_return_separation_closed": True,
        "normalized_positive_gap_proved": False,
        "dense_tail_return_pdec_excluded": False,
        "positive_stable_tail_gap_proved": False,
        "row_column_unconditional_closed": False,
        "normalized_formulas": {
            "H": "H=P-y",
            "q_change": "q=H+r",
            "row_window": "|B∩[P-q,y-1]|=min(L,r)",
            "prime_tail": "C_tail=sum_{prime q=H+r<P} min(L,r)ceil((P-1)/(H+r))",
            "integer_tail": "C_all=sum_{1<=r<P-H} min(L,r)ceil((P-1)/(H+r))",
            "gap": "G=L(P-1)-R_named-C_tail",
        },
        "next_direct_attack_target": TAIL_POSITIVE,
        "parallel_attack_targets": [
            TAIL_ESCAPE,
            HIGH_FIBER,
            COLLISION_RETURN,
            TERMINAL_NONARRIVAL,
            HISTORY_SWITCH,
            SHORT_BLOCK,
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
        "# Prime Matrix tail gap 归一化证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"positive_gap_imported={fmt_bool(cert['positive_gap_imported'])}",
        f"explicit_gap_functional_imported={fmt_bool(cert['explicit_gap_functional_imported'])}",
        f"tail_index_change_of_variables_closed={fmt_bool(cert['tail_index_change_of_variables_closed'])}",
        f"exact_prime_tail_envelope_closed={fmt_bool(cert['exact_prime_tail_envelope_closed'])}",
        f"all_integer_dominating_envelope_closed={fmt_bool(cert['all_integer_dominating_envelope_closed'])}",
        f"named_return_separation_closed={fmt_bool(cert['named_return_separation_closed'])}",
        f"normalized_positive_gap_proved={fmt_bool(cert['normalized_positive_gap_proved'])}",
        f"dense_tail_return_pdec_excluded={fmt_bool(cert['dense_tail_return_pdec_excluded'])}",
        f"positive_stable_tail_gap_proved={fmt_bool(cert['positive_stable_tail_gap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. q=H+r 归一化",
        "",
        "设 `H=P-y`。对 tail carrier 写",
        "",
        "```text",
        "q=H+r,  1<=r<P-H.",
        "```",
        "",
        "则",
        "",
        "```text",
        "P-q = P-H-r = y-r.",
        "```",
        "",
        "因此 terminal row window 精确为",
        "",
        "```text",
        "B ∩ [P-q,y-1] = B ∩ [y-r,y-1],",
        "|B ∩ [P-q,y-1]| = min(L,r).",
        "```",
        "",
        "## 2. 一维 tail functional",
        "",
        "于是 prime tail envelope 化成",
        "",
        "```text",
        "C_tail = sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r)).",
        "```",
        "",
        "去掉素数限制给出安全上界",
        "",
        "```text",
        "C_tail <= C_all = sum_{1<=r<P-H} min(L,r) ceil((P-1)/(H+r)).",
        "```",
        "",
        "gap 分离为",
        "",
        "```text",
        "G_prime = L(P-1)-C_tail,",
        "G = G_prime-R_named.",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{POSITIVE_GAP}",
        f"  -> {TAIL_INDEX}",
        f"  AND {EXACT_TAIL}",
        f"  AND {GAP_SEPARATION}",
        f"  AND {TAIL_POSITIVE}",
        "```",
        "",
        "真正剩余是证明归一化 prime-tail functional 留出正 gap；若失败，必须证明 dense tail、tail saturation",
        "或 named-return mass 已经构成 PDEC/SAE。",
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
            "- 本证书不证明归一化 gap 为正。",
            "- 本证书只把 `C_tail` 化成一维 `r=q-H` 的 exact prime-tail functional。",
            "- `NormalizedTailGapPositiveOrDenseTailReturnPDEC` 仍未闭合。",
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
