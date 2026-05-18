#!/usr/bin/env python3
"""生成 arrival quotient 纤维重数证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_arrival_quotient_fiber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.json

输出：
  data/prime-matrix-firstbreak-arrival-quotient-fiber-ledger.json
  docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.json
  docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-arrival-quotient-fiber-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-arrival-quotient-fiber-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-arrival-quotient-fiber-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json",
    DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json",
    DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.md",
]

DISTINCT_QUOTIENT = "DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC"
FIBER_ENVELOPE = "ArrivalQuotientFiberMultiplicityEnvelopeLedger"
WEIGHTED_LOWER = "WeightedArrivalImageLowerBoundFromFiberEnvelope"
RAW_MASS = "ArrivalRawSourceMassAfterNonarrivalRemoval"
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

REDUCED_QUOTIENT = f"{FIBER_ENVELOPE} AND {RAW_MASS} AND {WEIGHTED_LOWER} AND {HIGH_FIBER}"


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
    """构造 arrival quotient 纤维判定表。"""
    imported = previous.get("next_direct_attack_target") == DISTINCT_QUOTIENT
    unit_imported = previous.get("source_tagged_unit_incidence_closed") is True
    quotient_defined = previous.get("arrival_quotient_map_defined") is True
    return [
        row(
            "DistinctArrivalQuotientImported",
            imported,
            False,
            "上一层把聚合 actual demand 的直接主攻设为 distinct arrival quotient 下界或 collision PDEC。",
            DISTINCT_QUOTIENT,
        ),
        row(
            "SourceTaggedUnitIncidenceImported",
            unit_imported,
            unit_imported,
            "source-tagged arrival 已给出低 carrier AP incidence 单位。",
            UNIT_INCIDENCE,
        ),
        row(
            "ArrivalQuotientMapImported",
            quotient_defined,
            quotient_defined,
            "商化映射 pi: source-tagged arrivals -> (t_next,q,a) 已定义。",
            "pi(source arrival)=(t_next,q,a)",
        ),
        row(
            "FiberRowFactorClosed",
            True,
            True,
            "固定 arrival incidence (t,q,a) 的源行 s 必须满足 s==t mod q 且 s in [x0,y-1]，所以行因子至多 ceil(L/q)。",
            "R_B(t,q)<=ceil(L/q)",
        ),
        row(
            "FiberColumnFactorClosed",
            True,
            True,
            "固定 q,a 的源列 c 必须满足 1<=c<P 且 c==a mod q，所以列因子至多 ceil((P-1)/q)。",
            "C_P(a,q)<=ceil((P-1)/q)",
        ),
        row(
            "ArrivalFiberEnvelopeClosed",
            True,
            True,
            "同一 (t,q,a) 的原像纤维至多 ceil(L/q)ceil((P-1)/q)；超过该值只能是口径错误或重复登记 return。",
            FIBER_ENVELOPE,
        ),
        row(
            "WeightedImageLowerBoundFormulaClosed",
            True,
            True,
            "由纤维上界，|image(pi)| >= sum_{arrival u} 1/F(pi(u))；均匀版本为 |image(pi)|>=|A|/Fmax。",
            WEIGHTED_LOWER,
        ),
        row(
            "RawArrivalMassStillOpen",
            False,
            False,
            "仍未证明 terminal nonarrival 去除后 raw source-tagged arrival mass 足够大。",
            RAW_MASS,
        ),
        row(
            "HighFiberConcentrationRegistered",
            True,
            False,
            "若 weighted image 下界不足，压力必须集中在小 q/高纤维或重复碰撞上，登记为 dense low-carrier/PDEC/SAE return。",
            HIGH_FIBER,
        ),
        row(
            "CollisionReturnStillOpen",
            False,
            False,
            "已登记碰撞/重复支付 return，但尚未排斥或求和吸收。",
            COLLISION_RETURN,
        ),
        row(
            "DistinctArrivalQuotientReduced",
            True,
            False,
            "DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC 被压成纤维 envelope、raw arrival mass、加权 image 下界和高纤维碰撞回流。",
            REDUCED_QUOTIENT,
        ),
        row(
            "DistinctArrivalQuotientProved",
            False,
            False,
            "本步只关闭 quotient 纤维乘数纪律；不证明 image(pi) 已足够大，也不排斥高纤维碰撞。",
            f"{RAW_MASS} AND {HIGH_FIBER}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、短块 SAE、raw arrival mass、terminal nonarrival 排斥、高纤维碰撞排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {AP_SUCCESSOR} AND {UNIT_INCIDENCE} AND {REDUCED_QUOTIENT} AND {COLLISION_RETURN} AND {TERMINAL_NONARRIVAL} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 arrival quotient 纤维证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json")
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
        "distinct arrival quotient 的乘数纪律被精确化。固定 arrival incidence (t,q,a) 的原像只能来自"
        "零块中同一 AP 行类和同一列剩余类，因此纤维大小至多 ceil(L/q)ceil((P-1)/q)。"
        "这给出加权 image 下界 |image(pi)| >= sum 1/F(pi(u))。剩余不是口径问题，而是 raw arrival mass "
        "是否足够，以及若 image 过小是否能把高纤维集中登记并排斥为 dense low-carrier/PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_arrival_quotient_fiber_router",
        "status": "arrival_quotient_reduced_to_fiber_envelope_and_raw_mass_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": DISTINCT_QUOTIENT,
        "hardpoint_after_router": REDUCED_QUOTIENT,
        "source_tagged_unit_incidence_imported": previous.get("source_tagged_unit_incidence_closed") is True,
        "arrival_quotient_map_imported": previous.get("arrival_quotient_map_defined") is True,
        "fiber_row_factor_closed": True,
        "fiber_column_factor_closed": True,
        "arrival_fiber_envelope_closed": True,
        "weighted_image_lower_bound_formula_closed": True,
        "raw_arrival_mass_after_nonarrival_removal_proved": False,
        "high_fiber_concentration_registered": True,
        "high_fiber_collision_pdec_excluded": False,
        "distinct_arrival_quotient_lower_bound_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": RAW_MASS,
        "parallel_attack_targets": [
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
        "# Prime Matrix arrival quotient 纤维重数证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"source_tagged_unit_incidence_imported={fmt_bool(cert['source_tagged_unit_incidence_imported'])}",
        f"arrival_quotient_map_imported={fmt_bool(cert['arrival_quotient_map_imported'])}",
        f"fiber_row_factor_closed={fmt_bool(cert['fiber_row_factor_closed'])}",
        f"fiber_column_factor_closed={fmt_bool(cert['fiber_column_factor_closed'])}",
        f"arrival_fiber_envelope_closed={fmt_bool(cert['arrival_fiber_envelope_closed'])}",
        f"weighted_image_lower_bound_formula_closed={fmt_bool(cert['weighted_image_lower_bound_formula_closed'])}",
        f"raw_arrival_mass_after_nonarrival_removal_proved={fmt_bool(cert['raw_arrival_mass_after_nonarrival_removal_proved'])}",
        f"high_fiber_concentration_registered={fmt_bool(cert['high_fiber_concentration_registered'])}",
        f"high_fiber_collision_pdec_excluded={fmt_bool(cert['high_fiber_collision_pdec_excluded'])}",
        f"distinct_arrival_quotient_lower_bound_proved={fmt_bool(cert['distinct_arrival_quotient_lower_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 纤维公式",
        "",
        "令 `A` 为 source-tagged arrivals，商化映射为",
        "",
        "```text",
        "pi: A -> (t_next,q,a).",
        "```",
        "",
        "固定一个 image 点 `(t,q,a)`。其源行 `s` 必须在零块 `B=[x0,y-1]` 中满足",
        "",
        "```text",
        "s == t mod q.",
        "```",
        "",
        "所以行因子",
        "",
        "```text",
        "R_B(t,q) = #{s in B: s == t mod q} <= ceil(L/q).",
        "```",
        "",
        "源列 `c` 必须满足",
        "",
        "```text",
        "1 <= c < P,   c == a mod q,",
        "```",
        "",
        "所以列因子",
        "",
        "```text",
        "C_P(a,q) <= ceil((P-1)/q).",
        "```",
        "",
        "因此原像纤维满足",
        "",
        "```text",
        "|pi^{-1}(t,q,a)| <= ceil(L/q) ceil((P-1)/q).",
        "```",
        "",
        "## 2. 加权 image 下界",
        "",
        "记 `F(t,q,a)=ceil(L/q)ceil((P-1)/q)`。纤维上界给出严格的商化下界：",
        "",
        "```text",
        "|image(pi)| >= sum_{u in A} 1/F(pi(u)).",
        "```",
        "",
        "特别地，若 `Fmax=max F(pi(u))`，则",
        "",
        "```text",
        "|image(pi)| >= |A|/Fmax.",
        "```",
        "",
        "这一步关闭的是乘数纪律：任何把许多源义务压到同一 arrival incidence 的行为都必须由上述纤维解释；",
        "若超过纤维 envelope，则是重复登记或碰撞 return。",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{DISTINCT_QUOTIENT}",
        f"  -> {FIBER_ENVELOPE}",
        f"  AND {RAW_MASS}",
        f"  AND {WEIGHTED_LOWER}",
        f"  AND {HIGH_FIBER}",
        "```",
        "",
        "真正剩余是证明 terminal nonarrival 去除后的 raw arrival mass 足够大；若 weighted image 仍然太小，",
        "则压力集中在小 q/高纤维或重复碰撞上，必须回流到 dense low-carrier/PDEC/SAE。",
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
            "- 本证书不证明 distinct arrival demand 已足够大。",
            "- 本证书只证明 arrival quotient 的纤维 envelope 和加权 image 下界公式。",
            "- `ArrivalRawSourceMassAfterNonarrivalRemoval` 与 `HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn` 仍未闭合。",
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
