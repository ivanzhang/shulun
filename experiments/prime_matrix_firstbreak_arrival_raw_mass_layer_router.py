#!/usr/bin/env python3
"""生成 arrival raw mass 层平衡证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_arrival_raw_mass_layer_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.json

输出：
  data/prime-matrix-firstbreak-arrival-raw-mass-layer-ledger.json
  docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.json
  docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-arrival-raw-mass-layer-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-arrival-raw-mass-layer-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-arrival-raw-mass-layer-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-arrival-quotient-fiber-router.json",
    DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json",
    DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json",
]

RAW_MASS = "ArrivalRawSourceMassAfterNonarrivalRemoval"
BALANCE = "ArrivalNonarrivalSourceLayerBalanceLedger"
LOW_STEP_LEDGER = "LowStepStableHistoryAlwaysArrivesLedger"
RAW_LOWER = "RawArrivalMassLowerBoundFromLowStepHistory"
LOW_STEP_MASS = "LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC"
TAIL_ESCAPE = "LargeStepTailTerminalEscapePDECOrSAE"
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

REDUCED_RAW = f"{BALANCE} AND {LOW_STEP_LEDGER} AND {RAW_LOWER} AND {LOW_STEP_MASS}"
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


def build_rows(previous: dict[str, Any], stable: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 raw arrival mass 层平衡判定表。"""
    raw_imported = previous.get("next_direct_attack_target") == RAW_MASS
    dichotomy_imported = stable.get("arrival_nonarrival_dichotomy_closed") is True
    return [
        row(
            "RawMassImported",
            raw_imported,
            False,
            "上一层把 distinct arrival quotient 的直接主攻压到 terminal nonarrival 去除后的 raw source mass。",
            RAW_MASS,
        ),
        row(
            "APSuccessorDichotomyImported",
            dichotomy_imported,
            dichotomy_imported,
            "稳定 history 的 AP 后继二分已闭合：每个稳定源标签只能到达或成为 terminal nonarrival。",
            AP_SUCCESSOR,
        ),
        row(
            "SourceLayerUniverseDefined",
            True,
            True,
            "令 S 为 no-loss 与 history-switch 处理后仍留在稳定表中的 source-tagged history 记录。",
            "S=stable source-tagged history layer",
        ),
        row(
            "ArrivalNonarrivalBalanceClosed",
            True,
            True,
            "对 S 中每个记录，以最后零块命中 t_* 和 carrier q 定义后继 t_*+q；于是 S=A disjoint_union E。",
            BALANCE,
        ),
        row(
            "LowStepAlwaysArrivesClosed",
            True,
            True,
            "设 H=P-y。因 t_*<=y-1，若 q<=H，则 t_*+q<=P-1，所以该源标签必在 post-break 支撑内到达。",
            LOW_STEP_LEDGER,
        ),
        row(
            "TerminalEscapeTailCutoffClosed",
            True,
            True,
            "若 t_*+q>=P，则 q>=P-t_*>=H+1；terminal nonarrival 全部位于 q>H 的大步长尾部。",
            TAIL_ESCAPE,
        ),
        row(
            "RawArrivalLowerBoundFormulaClosed",
            True,
            True,
            "由低步长必到达，raw arrival mass 满足 |A|>=|S_{q<=H}|；扣除 nonarrival 不会损失低步长层。",
            RAW_LOWER,
        ),
        row(
            "LowStepMassStillOpen",
            False,
            False,
            "仍未证明稳定源层在 q<=H 上有足够质量；若没有，则质量集中到 q>H 大步长尾部。",
            LOW_STEP_MASS,
        ),
        row(
            "LargeStepTailEscapeRegistered",
            True,
            False,
            "若低步长质量不足以支撑 raw arrival 下界，则反例链必须解释为 q>H tail escape/PDEC/SAE。",
            TAIL_ESCAPE,
        ),
        row(
            "RawArrivalMassReduced",
            True,
            False,
            "ArrivalRawSourceMassAfterNonarrivalRemoval 被压成 source-layer 平衡、低步长必到达、raw 下界公式和低步长质量/大步长尾逃逸。",
            REDUCED_RAW,
        ),
        row(
            "RawArrivalMassProved",
            False,
            False,
            "本步只关闭 terminal nonarrival 去除的精确阈值与质量恒等式；不证明 q<=H 层已有足够质量。",
            LOW_STEP_MASS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需低步长稳定质量下界或大步长尾逃逸排斥、高纤维碰撞排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 raw arrival mass 层平衡证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-arrival-quotient-fiber-router.json")
    stable = load_json(DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json")
    rows = build_rows(previous, stable)
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
        "raw arrival mass 的 terminal nonarrival 去除被压成精确层平衡。设 H=P-y，"
        "稳定 history 源标签的最后零块命中为 t_*。若 q<=H，则 t_*+q<=P-1，"
        "所以该源必到达；若 terminal nonarrival 发生，则 q>=H+1。"
        "因此 |A|>=|S_{q<=H}|，剩余硬点不是去除口径，而是证明低步长稳定源质量足够；"
        "若不足，反例链必须集中在 q>H 的大步长尾逃逸并登记为 PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_arrival_raw_mass_layer_router",
        "status": "arrival_raw_mass_reduced_to_low_step_history_mass_or_large_step_tail_escape_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": RAW_MASS,
        "hardpoint_after_router": REDUCED_RAW,
        "raw_arrival_mass_imported": previous.get("next_direct_attack_target") == RAW_MASS,
        "ap_successor_dichotomy_imported": stable.get("arrival_nonarrival_dichotomy_closed") is True,
        "source_layer_universe_defined": True,
        "arrival_nonarrival_source_layer_balance_closed": True,
        "low_step_always_arrives_closed": True,
        "terminal_escape_tail_cutoff_closed": True,
        "raw_arrival_lower_bound_formula_closed": True,
        "low_step_stable_history_mass_lower_bound_proved": False,
        "large_step_tail_escape_registered": True,
        "large_step_tail_escape_excluded": False,
        "raw_arrival_mass_after_nonarrival_removal_proved": False,
        "row_column_unconditional_closed": False,
        "cutoff_identity": {
            "postbreak_width": "H=P-y",
            "low_step_arrival": "q<=H => t_*+q<=P-1",
            "terminal_escape_tail": "t_*+q>=P => q>=H+1",
            "raw_lower_bound": "|A|>=|S_{q<=H}|",
        },
        "next_direct_attack_target": LOW_STEP_MASS,
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
        "# Prime Matrix arrival raw mass 层平衡证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"raw_arrival_mass_imported={fmt_bool(cert['raw_arrival_mass_imported'])}",
        f"ap_successor_dichotomy_imported={fmt_bool(cert['ap_successor_dichotomy_imported'])}",
        f"source_layer_universe_defined={fmt_bool(cert['source_layer_universe_defined'])}",
        f"arrival_nonarrival_source_layer_balance_closed={fmt_bool(cert['arrival_nonarrival_source_layer_balance_closed'])}",
        f"low_step_always_arrives_closed={fmt_bool(cert['low_step_always_arrives_closed'])}",
        f"terminal_escape_tail_cutoff_closed={fmt_bool(cert['terminal_escape_tail_cutoff_closed'])}",
        f"raw_arrival_lower_bound_formula_closed={fmt_bool(cert['raw_arrival_lower_bound_formula_closed'])}",
        f"low_step_stable_history_mass_lower_bound_proved={fmt_bool(cert['low_step_stable_history_mass_lower_bound_proved'])}",
        f"large_step_tail_escape_registered={fmt_bool(cert['large_step_tail_escape_registered'])}",
        f"large_step_tail_escape_excluded={fmt_bool(cert['large_step_tail_escape_excluded'])}",
        f"raw_arrival_mass_after_nonarrival_removal_proved={fmt_bool(cert['raw_arrival_mass_after_nonarrival_removal_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 层平衡定义",
        "",
        "令 `S` 为 no-loss 与 history-switch 处理后仍留在稳定表中的 source-tagged history 记录。",
        "对 `u in S`，记其 carrier 为 `q(u)`，同 key 在零块 `B=[x0,y-1]` 中的最后命中行为 `t_*(u)`。",
        "稳定 AP 后继二分给出：",
        "",
        "```text",
        "t_next(u)=t_*(u)+q(u).",
        "A={u in S: t_next(u)<=P-1}",
        "E={u in S: t_next(u)>=P}",
        "S=A disjoint_union E.",
        "```",
        "",
        "这里 `A` 是 source-tagged arrivals，`E` 是 terminal nonarrival。",
        "",
        "## 2. 精确阈值 H=P-y",
        "",
        "设首破裂后支撑宽度为",
        "",
        "```text",
        "H=P-y.",
        "```",
        "",
        "由于每个最后零块命中都满足 `t_*(u)<=y-1`，若 `q(u)<=H`，则",
        "",
        "```text",
        "t_*(u)+q(u) <= y-1+H = P-1.",
        "```",
        "",
        "所以低步长层必定到达：",
        "",
        "```text",
        "S_{q<=H} subset A.",
        "```",
        "",
        "反过来，若发生 terminal nonarrival，则",
        "",
        "```text",
        "t_*(u)+q(u)>=P",
        "=> q(u)>=P-t_*(u)>=P-(y-1)=H+1.",
        "```",
        "",
        "因此 terminal nonarrival 全部位于大步长尾部：",
        "",
        "```text",
        "E subset S_{q>H}.",
        "```",
        "",
        "## 3. raw arrival 下界",
        "",
        "上述阈值给出非循环 raw mass 下界：",
        "",
        "```text",
        "|A| >= |S_{q<=H}|.",
        "```",
        "",
        "所以 `terminal nonarrival` 的去除不会吞掉任何 `q<=H` 的稳定源质量。真正剩余是证明",
        "`S_{q<=H}` 足够厚；若它不够厚，则稳定质量被迫集中在 `q>H` 的大步长尾部，必须作为",
        "`LargeStepTailTerminalEscapePDECOrSAE` 登记。",
        "",
        "## 4. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{RAW_MASS}",
        f"  -> {BALANCE}",
        f"  AND {LOW_STEP_LEDGER}",
        f"  AND {RAW_LOWER}",
        f"  AND {LOW_STEP_MASS}",
        "```",
        "",
        "本步把“nonarrival 去除后 raw mass 是否足够”的问题改写为低步长层质量问题。",
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
            "- 本证书不证明 raw arrival mass 已足够大。",
            "- 本证书只证明低步长稳定源必到达、terminal nonarrival 必在 q>H 大步长尾部。",
            "- `LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC` 仍未闭合。",
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
