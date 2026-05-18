#!/usr/bin/env python3
"""生成 arrival candidate 到 actual demand 的单位注入/商化证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_arrival_candidate_actual_demand_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json

输出：
  data/prime-matrix-firstbreak-arrival-candidate-actual-demand-ledger.json
  docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json
  docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-arrival-candidate-actual-demand-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-arrival-candidate-actual-demand-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json",
    DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json",
    DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "prime-matrix-strict-forced-obligation-lower-bound-router.md",
    DOCS / "prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.md",
]

ARRIVAL_INJECTION = "ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse"
UNIT_INCIDENCE = "SourceTaggedArrivalUnitIncidenceLedger"
QUOTIENT_LOWER = "DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC"
COLLISION_RETURN = "ArrivalCollisionOrDuplicatePaymentReturnLedger"
NO_RECYCLING = "NoAPEnvelopeRecyclingDemandGuard"
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

REDUCED_ARRIVAL = f"{UNIT_INCIDENCE} AND {QUOTIENT_LOWER} AND {COLLISION_RETURN}"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def file_contains(path: Path, needle: str) -> bool:
    """检查文本文件中是否含有指定证据标记。"""
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


def build_rows(previous: dict[str, Any], source_cut: dict[str, Any], no_loss_imported: bool) -> list[dict[str, Any]]:
    """构造 arrival candidate actual demand 判定表。"""
    arrival_imported = previous.get("next_direct_attack_target") == ARRIVAL_INJECTION
    candidate_imported = previous.get("arrival_candidate_registered") is True
    no_recycling = source_cut.get("no_envelope_recycling_guard") is True
    return [
        row(
            "ArrivalCandidateInjectionImported",
            arrival_imported,
            False,
            "上一层把稳定 history 的到达分支直接主攻设为 arrival candidate 到 actual demand 的非循环注入。",
            ARRIVAL_INJECTION,
        ),
        row(
            "ArrivalCandidateImported",
            candidate_imported,
            candidate_imported,
            "AP 后继二分已登记：当 t_next=t_*+q 落入 [y,P-1] 时形成 post-break arrival candidate。",
            AP_SUCCESSOR,
        ),
        row(
            "NoEnvelopeRecyclingGuardImported",
            no_recycling,
            no_recycling,
            "actual demand 下界必须来自源侧到达标记，不能从 AP envelope 接近饱和反推。",
            NO_RECYCLING,
        ),
        row(
            "SourceTaggedUnitIncidenceClosed",
            True,
            True,
            "源侧 arrival candidate 继承零块 history tag，并满足 t_next==-aP^{-1} mod q；因此它给出一个低 carrier AP row-incidence 单位。",
            UNIT_INCIDENCE,
        ),
        row(
            "RawCandidateNotAggregateDemandGuard",
            True,
            True,
            "raw arrival candidate 数不能直接当成 demand 下界；actual demand 只计去重后的 post-break row/cell incidence。",
            QUOTIENT_LOWER,
        ),
        row(
            "ArrivalQuotientMapDefined",
            True,
            True,
            "定义商化映射 pi: source-tagged arrivals -> (t_next,q,a)。actual demand 至少是 image(pi) 的 distinct incidence 数。",
            QUOTIENT_LOWER,
        ),
        row(
            "NoLossCollisionReturnImported",
            no_loss_imported,
            no_loss_imported,
            "若多个源义务映到同一 (t,q,a)，重复不能删除；只能商化、加权或登记 duplicate/collision return。",
            COLLISION_RETURN,
        ),
        row(
            "ArrivalCollisionReturnRegistered",
            True,
            False,
            "大规模碰撞、重复支付或换源吸收必须进入 PDEC/ColumnCRT/SAE/duplicate return，而不是免费容量。",
            COLLISION_RETURN,
        ),
        row(
            "DistinctArrivalQuotientLowerBoundOpen",
            False,
            False,
            "仍未证明去重后的 image(pi) 足够大，可以和 AP envelope gap 比较；这是新的聚合硬点。",
            QUOTIENT_LOWER,
        ),
        row(
            "ArrivalCandidateInjectionReduced",
            True,
            False,
            "ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse 被压成单位 source-tagged incidence、distinct quotient 下界和碰撞 return 三项。",
            REDUCED_ARRIVAL,
        ),
        row(
            "ArrivalCandidateInjectionProved",
            False,
            False,
            "本步只闭合单位注入，不证明聚合 actual demand 下界，也不排斥碰撞终端。",
            f"{QUOTIENT_LOWER} AND {COLLISION_RETURN}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、短块 SAE、distinct arrival quotient 下界、terminal nonarrival 排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {REDUCED_ARRIVAL} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 arrival candidate actual demand 证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json")
    source_cut = load_json(DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json")
    no_loss_imported = file_contains(
        DOCS / "prime-matrix-no-loss-return-accounting-router.md",
        "no_loss_return_accounting_closed=true",
    )
    rows = build_rows(previous, source_cut, no_loss_imported)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} "
        f"AND {AP_SUCCESSOR} AND {REDUCED_ARRIVAL} AND {TERMINAL_NONARRIVAL} "
        f"AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} "
        f"AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "arrival candidate 到 actual demand 的接口被拆开：源侧标记的到达候选确实给出一个低 carrier "
        "AP row-incidence 单位，且不使用 envelope 饱和反推；但 raw 到达候选不能直接当作聚合需求。"
        "必须对 source-tagged arrivals 按 (t_next,q,a) 商化，证明 distinct image 足够大；"
        "若大量源义务碰撞到少数 incidence，则该碰撞必须登记为 PDEC/ColumnCRT/SAE/duplicate return。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_arrival_candidate_actual_demand_router",
        "status": "arrival_candidate_actual_demand_reduced_to_unit_incidence_and_quotient_lower_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": ARRIVAL_INJECTION,
        "hardpoint_after_router": REDUCED_ARRIVAL,
        "arrival_candidate_imported": previous.get("arrival_candidate_registered") is True,
        "no_envelope_recycling_guard_imported": source_cut.get("no_envelope_recycling_guard") is True,
        "source_tagged_unit_incidence_closed": True,
        "arrival_quotient_map_defined": True,
        "no_loss_collision_return_imported": no_loss_imported,
        "arrival_collision_return_registered": True,
        "distinct_arrival_quotient_lower_bound_proved": False,
        "arrival_collision_return_excluded": False,
        "arrival_candidate_actual_demand_injection_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": QUOTIENT_LOWER,
        "parallel_attack_targets": [
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
        "# Prime Matrix arrival candidate 到 actual demand 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"arrival_candidate_imported={fmt_bool(cert['arrival_candidate_imported'])}",
        f"no_envelope_recycling_guard_imported={fmt_bool(cert['no_envelope_recycling_guard_imported'])}",
        f"source_tagged_unit_incidence_closed={fmt_bool(cert['source_tagged_unit_incidence_closed'])}",
        f"arrival_quotient_map_defined={fmt_bool(cert['arrival_quotient_map_defined'])}",
        f"no_loss_collision_return_imported={fmt_bool(cert['no_loss_collision_return_imported'])}",
        f"arrival_collision_return_registered={fmt_bool(cert['arrival_collision_return_registered'])}",
        f"distinct_arrival_quotient_lower_bound_proved={fmt_bool(cert['distinct_arrival_quotient_lower_bound_proved'])}",
        f"arrival_collision_return_excluded={fmt_bool(cert['arrival_collision_return_excluded'])}",
        f"arrival_candidate_actual_demand_injection_proved={fmt_bool(cert['arrival_candidate_actual_demand_injection_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单位注入",
        "",
        "arrival candidate 不是从 AP 表容量反推出来的。它带有零块源侧 history tag，并满足",
        "",
        "```text",
        "t_next == -a P^{-1} mod q,   y <= t_next <= P-1.",
        "```",
        "",
        "因此它给出一个低 carrier AP row-incidence 单位：",
        "",
        "```text",
        "(source tag, t_next, q, a) -> incidence(t_next,q,a).",
        "```",
        "",
        "这一步是非循环的，因为它只使用源侧到达标记和同余等式，不使用 AP envelope 是否接近饱和。",
        "",
        "## 2. 为什么 raw candidate 不能直接计数",
        "",
        "actual demand 下界不能数 raw source-tagged arrivals。必须先商化：",
        "",
        "```text",
        "pi: source-tagged arrivals -> (t_next,q,a).",
        "```",
        "",
        "真正可与 AP envelope 比较的是 distinct incidence 数 `|image(pi)|`。如果多个源义务映到同一",
        "`(t_next,q,a)`，这些重合不能被删除，也不能当作多个独立 demand；它们必须进入 quotient、weighted return、",
        "duplicate/collision PDEC、ColumnCRT 或 SAE。",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{ARRIVAL_INJECTION}",
        f"  -> {UNIT_INCIDENCE}",
        f"  AND {QUOTIENT_LOWER}",
        f"  AND {COLLISION_RETURN}",
        "```",
        "",
        "当前真正剩余是证明去重后的 arrival image 足够大；若 image 过小，则必须把塌缩解释为命名碰撞/重复支付终端。",
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
            "- 本证书不证明聚合 actual demand 下界。",
            "- 本证书只证明 source-tagged arrival 的单位 incidence 注入，并建立去重口径。",
            "- `DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC` 与 `ArrivalCollisionOrDuplicatePaymentReturnLedger` 仍未闭合。",
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
