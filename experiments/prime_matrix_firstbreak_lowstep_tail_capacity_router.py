#!/usr/bin/env python3
"""生成 low-step 稳定质量与 large-step tail 容量证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_lowstep_tail_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json

输出：
  data/prime-matrix-firstbreak-lowstep-tail-capacity-ledger.json
  docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json
  docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-lowstep-tail-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-lowstep-tail-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-lowstep-tail-capacity-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-arrival-raw-mass-layer-router.json",
    DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json",
    DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json",
    DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json",
    DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
]

LOW_STEP_MASS = "LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC"
PARTITION = "StableHistoryLowTailMassPartitionLedger"
TAIL_WINDOW = "LargeStepTailTerminalWindowEnvelopeLedger"
LOW_FROM_TAIL = "LowStepStableMassLowerBoundFromTotalMinusTailEnvelope"
TAIL_GAP = "StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC"
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

REDUCED_LOW_STEP = f"{PARTITION} AND {TAIL_WINDOW} AND {LOW_FROM_TAIL} AND {TAIL_GAP}"
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


def build_rows(previous: dict[str, Any], lcm_rank: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 low-step/tail 容量判定表。"""
    imported = previous.get("next_direct_attack_target") == LOW_STEP_MASS
    raw_balance_imported = previous.get("arrival_nonarrival_source_layer_balance_closed") is True
    lcm_rank_imported = lcm_rank.get("small_lcm_rank_pressure_closed") is True
    return [
        row(
            "LowStepMassImported",
            imported,
            False,
            "上一层把 raw arrival mass 的剩余压成低步长稳定源质量，或 q>H 大步长尾逃逸。",
            LOW_STEP_MASS,
        ),
        row(
            "RawLayerBalanceImported",
            raw_balance_imported,
            raw_balance_imported,
            "稳定源层已按 q<=H 到达层和 q>H terminal tail 层分割。",
            RAW_BALANCE,
        ),
        row(
            "LowTailPartitionClosed",
            True,
            True,
            "S=S_{q<=H} disjoint_union S_{q>H}，且 |S_{q<=H}|=|S|-|S_{q>H}|。",
            PARTITION,
        ),
        row(
            "TerminalTailRowWindowClosed",
            True,
            True,
            "对 q>H 的 terminal nonarrival，最后零块命中 t_* 必在 B∩[P-q,y-1]，该窗口长度至多 min(L,q-H)。",
            TAIL_WINDOW,
        ),
        row(
            "TailColumnMultiplicityClosed",
            True,
            True,
            "固定 q 和 terminal 行 t 后，源列必须满足 c==-tP mod q；1<=c<P 中至多 ceil((P-1)/q) 个。",
            TAIL_WINDOW,
        ),
        row(
            "LargeStepTailEnvelopeClosed",
            True,
            True,
            "因此非重复 tail source records 满足 |S_{q>H}|<=sum_{H<q<P} |B∩[P-q,y-1]| ceil((P-1)/q)。",
            TAIL_WINDOW,
        ),
        row(
            "LowStepMassFromTotalMinusTailClosed",
            True,
            True,
            "在无 tail 重复/饱和 defect 时，|S_{q<=H}|>=|S|-C_tail。",
            LOW_FROM_TAIL,
        ),
        row(
            "LargeStepTailNoSmallLCMReplayImported",
            lcm_rank_imported,
            lcm_rank_imported,
            "若 q>H，则任何包含该 q 的固定 carrier 复现 LCM 已超过 H；它不能隐藏在 small-LCM replay 中。",
            "q>H => lcm>=q>H",
        ),
        row(
            "TailSaturationReturnRegistered",
            True,
            False,
            "若低步长质量仍不足，则必须证明 |S|-C_tail 不够，或把 tail envelope 近饱和/重复登记为 PDEC/SAE。",
            TAIL_GAP,
        ),
        row(
            "LowStepMassReduced",
            True,
            False,
            "LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC 被压成低/尾分割、tail window envelope、总量减尾容量下界和 tail saturation gap。",
            REDUCED_LOW_STEP,
        ),
        row(
            "LowStepMassProved",
            False,
            False,
            "本步没有证明 |S|-C_tail 已超过所需需求；只关闭 q>H tail 的显式容量 envelope。",
            TAIL_GAP,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需稳定源总量减 tail envelope 的正间隙，或 tail 近饱和 PDEC/SAE 排斥，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 low-step/tail 容量证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-arrival-raw-mass-layer-router.json")
    lcm_rank = load_json(DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json")
    rows = build_rows(previous, lcm_rank)
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
        "低步长稳定质量硬点被压到显式 tail envelope。设 H=P-y，B=[x0,y-1]，"
        "S 为稳定 source-tagged history 层。q<=H 的层必到达；q>H 的 terminal tail 若最后命中为 t_*，"
        "则 t_* 必在 B∩[P-q,y-1]，窗口长度至多 min(L,q-H)。固定 q,t_* 后源列 c 至多有 ceil((P-1)/q) 个。"
        "因此 |S_{q>H}| 有显式 C_tail 上界，进而 |S_{q<=H}|>=|S|-C_tail。"
        "剩余硬点变为证明该差额足够，或证明 tail envelope 近饱和/重复就是 PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_lowstep_tail_capacity_router",
        "status": "lowstep_mass_reduced_to_total_minus_large_step_tail_envelope_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": LOW_STEP_MASS,
        "hardpoint_after_router": REDUCED_LOW_STEP,
        "lowstep_mass_imported": previous.get("next_direct_attack_target") == LOW_STEP_MASS,
        "raw_layer_balance_imported": previous.get("arrival_nonarrival_source_layer_balance_closed") is True,
        "stable_low_tail_partition_closed": True,
        "terminal_tail_row_window_closed": True,
        "tail_column_multiplicity_closed": True,
        "large_step_tail_envelope_closed": True,
        "lowstep_mass_from_total_minus_tail_closed": True,
        "large_step_tail_no_small_lcm_replay_imported": lcm_rank.get("small_lcm_rank_pressure_closed") is True,
        "stable_total_minus_tail_envelope_gap_proved": False,
        "large_step_tail_saturation_pdec_excluded": False,
        "lowstep_stable_history_mass_lower_bound_proved": False,
        "row_column_unconditional_closed": False,
        "tail_envelope_formula": {
            "postbreak_width": "H=P-y",
            "zero_block": "B=[x0,y-1], L=y-x0",
            "terminal_tail_rows_for_q": "T_q=B∩[P-q,y-1]",
            "row_window_bound": "|T_q|<=min(L,q-H)",
            "column_bound": "C_q(t)<=ceil((P-1)/q)",
            "tail_capacity": "C_tail=sum_{H<q<P} |T_q| ceil((P-1)/q)",
            "lowstep_lower_bound": "|S_{q<=H}|>=|S|-C_tail",
        },
        "next_direct_attack_target": TAIL_GAP,
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
        "# Prime Matrix low-step/tail 容量证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"lowstep_mass_imported={fmt_bool(cert['lowstep_mass_imported'])}",
        f"raw_layer_balance_imported={fmt_bool(cert['raw_layer_balance_imported'])}",
        f"stable_low_tail_partition_closed={fmt_bool(cert['stable_low_tail_partition_closed'])}",
        f"terminal_tail_row_window_closed={fmt_bool(cert['terminal_tail_row_window_closed'])}",
        f"tail_column_multiplicity_closed={fmt_bool(cert['tail_column_multiplicity_closed'])}",
        f"large_step_tail_envelope_closed={fmt_bool(cert['large_step_tail_envelope_closed'])}",
        f"lowstep_mass_from_total_minus_tail_closed={fmt_bool(cert['lowstep_mass_from_total_minus_tail_closed'])}",
        f"large_step_tail_no_small_lcm_replay_imported={fmt_bool(cert['large_step_tail_no_small_lcm_replay_imported'])}",
        f"stable_total_minus_tail_envelope_gap_proved={fmt_bool(cert['stable_total_minus_tail_envelope_gap_proved'])}",
        f"large_step_tail_saturation_pdec_excluded={fmt_bool(cert['large_step_tail_saturation_pdec_excluded'])}",
        f"lowstep_stable_history_mass_lower_bound_proved={fmt_bool(cert['lowstep_stable_history_mass_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 低步长/尾部恒等式",
        "",
        "设 `H=P-y`，零块 `B=[x0,y-1]`，`L=y-x0`。稳定源层满足",
        "",
        "```text",
        "S = S_{q<=H} disjoint_union S_{q>H}.",
        "|S_{q<=H}| = |S| - |S_{q>H}|.",
        "```",
        "",
        "上一层已证明 `q<=H` 的稳定源必到达，因此关键是控制 `q>H` 的 terminal tail。",
        "",
        "## 2. q>H 的 terminal row window",
        "",
        "若 `u in S_{q>H}` 是 terminal nonarrival，最后零块命中行为 `t_*`，则",
        "",
        "```text",
        "t_*+q >= P,    t_* in B.",
        "```",
        "",
        "所以",
        "",
        "```text",
        "t_* in T_q := B ∩ [P-q, y-1].",
        "|T_q| <= min(L, q-H).",
        "```",
        "",
        "固定 `q` 和 terminal 行 `t` 后，源列必须满足",
        "",
        "```text",
        "c == -tP mod q,    1 <= c < P,",
        "```",
        "",
        "所以列数至多",
        "",
        "```text",
        "ceil((P-1)/q).",
        "```",
        "",
        "## 3. tail envelope 与低步长下界",
        "",
        "因此非重复 tail source records 满足",
        "",
        "```text",
        "C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q)",
        "       <= sum_{H<q<P} min(L,q-H) ceil((P-1)/q),",
        "|S_{q>H}| <= C_tail.",
        "```",
        "",
        "从而得到",
        "",
        "```text",
        "|S_{q<=H}| >= |S| - C_tail.",
        "```",
        "",
        "若出现超过该 envelope 的重复使用，或必须把 tail envelope 压到近饱和才能逃避低步长质量，",
        "则它是命名的 `LargeStepTail` 容量饱和/PDEC/SAE 回流。",
        "",
        "## 4. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{LOW_STEP_MASS}",
        f"  -> {PARTITION}",
        f"  AND {TAIL_WINDOW}",
        f"  AND {LOW_FROM_TAIL}",
        f"  AND {TAIL_GAP}",
        "```",
        "",
        "本步把低步长质量问题压成一个显式差额问题：证明 `|S|-C_tail` 足够，",
        "或证明 tail 近饱和/重复就是 PDEC/SAE。",
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
            "- 本证书不证明低步长稳定源质量已经足够。",
            "- 本证书只关闭 q>H terminal tail 的 row-window/column-multiplicity envelope。",
            "- `StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC` 仍未闭合。",
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
