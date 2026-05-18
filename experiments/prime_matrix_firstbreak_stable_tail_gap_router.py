#!/usr/bin/env python3
"""生成稳定总源质量减 tail envelope 的 gap 证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_stable_tail_gap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json

输出：
  data/prime-matrix-firstbreak-stable-tail-gap-ledger.json
  docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json
  docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-stable-tail-gap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-stable-tail-gap-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-stable-tail-gap-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-lowstep-tail-capacity-router.json",
    DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json",
]

TAIL_GAP = "StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC"
ZERO_MASS = "ZeroBlockCoverObligationMassLedger"
STABLE_TOTAL = "StableSourceTotalAfterNamedReturnsLedger"
GAP_FORMULA = "ExplicitStableTailGapFunctionalLedger"
POSITIVE_GAP = "PositiveStableTailGapOrNamedReturnMassPDEC"
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

REDUCED_TAIL_GAP = f"{ZERO_MASS} AND {STABLE_TOTAL} AND {GAP_FORMULA} AND {POSITIVE_GAP}"
REDUCED_LOW_STEP = f"{PARTITION} AND {TAIL_WINDOW} AND {LOW_FROM_TAIL} AND {REDUCED_TAIL_GAP}"
REDUCED_RAW = f"{RAW_BALANCE} AND {LOW_STEP_ARRIVES} AND {RAW_LOWER} AND {REDUCED_LOW_STEP}"
REDUCED_QUOTIENT = f"{FIBER_ENVELOPE} AND {REDUCED_RAW} AND {WEIGHTED_LOWER} AND {HIGH_FIBER}"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def file_contains(path: Path, needle: str) -> bool:
    """检查文本证据标记。"""
    if not path.exists():
        return False
    return needle in path.read_text(encoding="utf-8")


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


def build_rows(previous: dict[str, Any], long_zero: dict[str, Any], no_loss_closed: bool) -> list[dict[str, Any]]:
    """构造 stable tail gap 判定表。"""
    imported = previous.get("next_direct_attack_target") == TAIL_GAP
    zero_mass_imported = long_zero.get("zero_block_cover_obligation_mass_imported") is True
    tail_env_imported = previous.get("large_step_tail_envelope_closed") is True
    return [
        row(
            "TailGapImported",
            imported,
            False,
            "上一层把低步长稳定质量压成 |S|-C_tail 的显式差额，或 tail saturation PDEC。",
            TAIL_GAP,
        ),
        row(
            "ZeroBlockObligationMassImported",
            zero_mass_imported,
            zero_mass_imported,
            "长零块覆盖义务域 O_B={(t,c):x0<=t<y,1<=c<P} 的大小为 L(P-1)。",
            ZERO_MASS,
        ),
        row(
            "NoLossAccountingImported",
            no_loss_closed,
            no_loss_closed,
            "no-loss 账本给出 O_B=StableSourceRecords disjoint_union NamedReturnRecords，无义务丢失。",
            NO_LOSS,
        ),
        row(
            "StableTotalAfterNamedReturnsClosed",
            True,
            True,
            "记 R_named 为 history switch、duplicate、tail saturation 等命名 return 质量，则稳定源总量满足 |S|>=L(P-1)-R_named。",
            STABLE_TOTAL,
        ),
        row(
            "TailEnvelopeImported",
            tail_env_imported,
            tail_env_imported,
            "上一层已闭合 C_tail=sum_{H<q<P}|B∩[P-q,y-1]|ceil((P-1)/q)。",
            TAIL_WINDOW,
        ),
        row(
            "ExplicitTailGapFunctionalClosed",
            True,
            True,
            "组合得到 |S_{q<=H}| >= L(P-1)-R_named-C_tail。",
            GAP_FORMULA,
        ),
        row(
            "PositiveGapStillOpen",
            False,
            False,
            "仍未证明该显式 gap 超过所需 raw arrival demand；若失败，必须由 R_named 或 tail saturation 承担。",
            POSITIVE_GAP,
        ),
        row(
            "TailGapReduced",
            True,
            False,
            "StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC 被压成零块总义务、稳定源总量、显式 gap functional 和正 gap/命名 return。",
            REDUCED_TAIL_GAP,
        ),
        row(
            "TailGapProved",
            False,
            False,
            "本步没有证明 gap 为正或足够大，只把剩余写成显式不等式与命名 return 质量。",
            POSITIVE_GAP,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需正 gap 或命名 return/PDEC 排斥，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 stable tail gap 证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-lowstep-tail-capacity-router.json")
    long_zero = load_json(DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json")
    no_loss_closed = file_contains(
        DOCS / "prime-matrix-no-loss-return-accounting-router.md",
        "no_loss_return_accounting_closed=true",
    )
    rows = build_rows(previous, long_zero, no_loss_closed)
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
        "stable tail gap 被写成显式 functional。零块覆盖义务总量为 L(P-1)，no-loss 说明这些义务"
        "要么成为稳定源记录，要么成为命名 return。若 R_named 记所有 history switch、duplicate、tail saturation "
        "等命名 return 质量，且 C_tail 为上一层 q>H tail envelope，则 |S_{q<=H}|>=L(P-1)-R_named-C_tail。"
        "剩余硬点变为证明该 gap 足够大，或证明 R_named/tail saturation 已经是 PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_stable_tail_gap_router",
        "status": "stable_tail_gap_reduced_to_explicit_functional_and_named_return_mass_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": TAIL_GAP,
        "hardpoint_after_router": REDUCED_TAIL_GAP,
        "tail_gap_imported": previous.get("next_direct_attack_target") == TAIL_GAP,
        "zero_block_obligation_mass_imported": long_zero.get("zero_block_cover_obligation_mass_imported") is True,
        "no_loss_accounting_imported": no_loss_closed,
        "stable_total_after_named_returns_closed": True,
        "tail_envelope_imported": previous.get("large_step_tail_envelope_closed") is True,
        "explicit_tail_gap_functional_closed": True,
        "positive_stable_tail_gap_proved": False,
        "named_return_mass_pdec_excluded": False,
        "stable_total_minus_tail_envelope_gap_proved": False,
        "row_column_unconditional_closed": False,
        "gap_formula": {
            "zero_block_obligation_mass": "|O_B|=L(P-1)",
            "stable_total_lower_bound": "|S|>=L(P-1)-R_named",
            "tail_capacity": "C_tail=sum_{H<q<P}|B∩[P-q,y-1]|ceil((P-1)/q)",
            "lowstep_lower_bound": "|S_{q<=H}|>=L(P-1)-R_named-C_tail",
        },
        "next_direct_attack_target": POSITIVE_GAP,
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
        "# Prime Matrix stable tail gap 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"tail_gap_imported={fmt_bool(cert['tail_gap_imported'])}",
        f"zero_block_obligation_mass_imported={fmt_bool(cert['zero_block_obligation_mass_imported'])}",
        f"no_loss_accounting_imported={fmt_bool(cert['no_loss_accounting_imported'])}",
        f"stable_total_after_named_returns_closed={fmt_bool(cert['stable_total_after_named_returns_closed'])}",
        f"tail_envelope_imported={fmt_bool(cert['tail_envelope_imported'])}",
        f"explicit_tail_gap_functional_closed={fmt_bool(cert['explicit_tail_gap_functional_closed'])}",
        f"positive_stable_tail_gap_proved={fmt_bool(cert['positive_stable_tail_gap_proved'])}",
        f"named_return_mass_pdec_excluded={fmt_bool(cert['named_return_mass_pdec_excluded'])}",
        f"stable_total_minus_tail_envelope_gap_proved={fmt_bool(cert['stable_total_minus_tail_envelope_gap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总源质量",
        "",
        "零块覆盖义务域为",
        "",
        "```text",
        "O_B={(t,c): x0<=t<y, 1<=c<P},",
        "|O_B|=L(P-1).",
        "```",
        "",
        "no-loss 账本给出",
        "",
        "```text",
        "O_B = StableSourceRecords disjoint_union NamedReturnRecords.",
        "```",
        "",
        "记命名 return 质量为 `R_named`，则",
        "",
        "```text",
        "|S| >= L(P-1)-R_named.",
        "```",
        "",
        "## 2. gap functional",
        "",
        "上一层已经闭合 tail envelope：",
        "",
        "```text",
        "C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q).",
        "```",
        "",
        "因此低步长稳定质量满足显式下界：",
        "",
        "```text",
        "|S_{q<=H}| >= L(P-1)-R_named-C_tail.",
        "```",
        "",
        "如果该下界不足，不能无名消失；必须由 `R_named`、tail saturation、history switch、duplicate/collision",
        "或 PDEC/SAE 账本承载。",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{TAIL_GAP}",
        f"  -> {ZERO_MASS}",
        f"  AND {STABLE_TOTAL}",
        f"  AND {GAP_FORMULA}",
        f"  AND {POSITIVE_GAP}",
        "```",
        "",
        "真正剩余是证明 `L(P-1)-R_named-C_tail` 足够大；若失败，则必须证明相应命名 return 质量已经形成 PDEC/SAE。",
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
            "- 本证书不证明 tail gap 已经足够大。",
            "- 本证书只把低步长稳定质量下界写成 `L(P-1)-R_named-C_tail`。",
            "- `PositiveStableTailGapOrNamedReturnMassPDEC` 仍未闭合。",
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
