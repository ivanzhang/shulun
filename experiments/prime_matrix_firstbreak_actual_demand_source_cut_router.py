#!/usr/bin/env python3
"""生成首破裂低 carrier actual demand 的源侧切口证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_actual_demand_source_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json

输出：
  data/prime-matrix-firstbreak-actual-demand-source-cut-ledger.json
  docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json
  docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-actual-demand-source-cut-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json",
    DOCS / "prime-matrix-firstbreak-low-carrier-residue-ap-router.json",
    DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json",
    DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json",
    DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json",
]

DEMAND = "ActualLowCarrierRowIncidenceDemandLowerBound"
UNIT_DEMAND = "FirstBreakUnitReleaseDemandLowerBound"
AMPLIFICATION = "FirstBreakReleaseMassAmplificationOrSingletonSAE"
PAYMENT_INJECTION = "LowCarrierActualPaymentInjectionWithoutEnvelopeReuse"
NO_RECYCLING = "NoAPEnvelopeRecyclingDemandGuard"
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

REDUCED_DEMAND = f"{AMPLIFICATION} AND {PAYMENT_INJECTION}"


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


def build_rows(previous: dict[str, Any], firstbreak: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 actual demand 源侧切口判定表。"""
    demand_imported = previous.get("next_direct_attack_target") == DEMAND
    release_imported = firstbreak.get("first_break_release_set_nonempty") is True
    return [
        row(
            "ActualDemandImported",
            demand_imported,
            False,
            "上一层 AP exact-envelope 证书把容量比较剩余压到 actual row-incidence demand 下界。",
            DEMAND,
        ),
        row(
            "FirstBreakReleaseSetImported",
            release_imported,
            release_imported,
            "early-to-square 分裂已证明：若 square-anchor 分支不接管，则首破裂行 y 有非空释放列集。",
            UNIT_DEMAND,
        ),
        row(
            "UnitReleaseDemandLowerBoundClosed",
            True,
            True,
            "释放列非空只给出 D_y>=1 的单位 actual demand；这是源侧事实，不使用 AP envelope。",
            UNIT_DEMAND,
        ),
        row(
            "UnitDemandNotGapSufficient",
            True,
            True,
            "单位需求不足以超过 AP envelope：单个 residue cell 已可提供至少一个发生位，因此不能由 D_y>=1 得到容量矛盾。",
            AMPLIFICATION,
        ),
        row(
            "NoEnvelopeRecyclingGuard",
            True,
            True,
            "actual demand 下界必须来自首破裂/零行源侧，不能从 AP table 接近饱和反推需求；否则论证循环。",
            NO_RECYCLING,
        ),
        row(
            "PaymentInjectionSeparated",
            True,
            False,
            "即使源侧释放质量被放大，还必须证明这些压力注入同一低 carrier AP table；若不能注入，则回流到高秩、moving carrier、PDEC 或 SAE。",
            PAYMENT_INJECTION,
        ),
        row(
            "ActualDemandReduced",
            True,
            False,
            "ActualLowCarrierRowIncidenceDemandLowerBound 被切成源侧释放质量放大和非循环支付注入两项。",
            REDUCED_DEMAND,
        ),
        row(
            "ActualDemandProved",
            False,
            False,
            "本步没有证明 Ω(H) 或超 envelope 的 actual demand；只排除了把单位释放误当成容量矛盾的路线。",
            REDUCED_DEMAND,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、释放质量放大、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {REDUCED_DEMAND} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 actual demand 源侧切口证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json")
    firstbreak = load_json(DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json")
    rows = build_rows(previous, firstbreak)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {REDUCED_DEMAND} AND {STRICT_GAP} AND {DENSE_TABLE} "
        f"AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "Actual demand 的源侧下界被切开：首破裂释放非空只给出单位需求 D_y>=1，"
        "不足以超过 AP exact-envelope；真正需要证明的是释放质量沿反例链放大到可与 H 比较，"
        "并且这些压力非循环地注入同一低 carrier AP table。若无法放大，则只能登记为 singleton/sparse SAE；"
        "若无法注入，则回流到高秩、moving carrier、PDEC 或 SAE 出口。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_actual_demand_source_cut_router",
        "status": "firstbreak_actual_demand_cut_to_source_amplification_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": DEMAND,
        "hardpoint_after_router": REDUCED_DEMAND,
        "firstbreak_release_set_imported": firstbreak.get("first_break_release_set_nonempty") is True,
        "unit_release_demand_lower_bound_closed": True,
        "unit_demand_not_gap_sufficient": True,
        "no_envelope_recycling_guard": True,
        "release_mass_amplification_proved": False,
        "low_carrier_payment_injection_proved": False,
        "actual_low_carrier_row_incidence_demand_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": AMPLIFICATION,
        "parallel_attack_targets": [PAYMENT_INJECTION, STRICT_GAP, DENSE_TABLE, SPARSE_CELL, LOW_SAE, HIGH_RANK, NONREPLAY_SAE, MOVING_CARRIER],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂 actual demand 源侧切口证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"firstbreak_release_set_imported={fmt_bool(cert['firstbreak_release_set_imported'])}",
        f"unit_release_demand_lower_bound_closed={fmt_bool(cert['unit_release_demand_lower_bound_closed'])}",
        f"unit_demand_not_gap_sufficient={fmt_bool(cert['unit_demand_not_gap_sufficient'])}",
        f"no_envelope_recycling_guard={fmt_bool(cert['no_envelope_recycling_guard'])}",
        f"release_mass_amplification_proved={fmt_bool(cert['release_mass_amplification_proved'])}",
        f"low_carrier_payment_injection_proved={fmt_bool(cert['low_carrier_payment_injection_proved'])}",
        f"actual_low_carrier_row_incidence_demand_proved={fmt_bool(cert['actual_low_carrier_row_incidence_demand_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 源侧切口",
        "",
        "上一层已经给出 AP exact-envelope；因此 actual demand 下界必须来自反例链的源侧，而不能从 AP table 的",
        "容量饱和反推。首破裂分裂只保证：若平方锚分支不接管，则存在首个非零行 `y`，且释放列集非空。",
        "",
        "```text",
        "R_y != empty  =>  D_y >= 1.",
        "```",
        "",
        "这是严格的 actual demand 下界，但它只是单位下界。",
        "",
        "## 2. 为什么单位需求不够",
        "",
        "AP exact-envelope 中，任意一个低 carrier residue cell `(q,a)` 在 `I_y` 中最多有 `ceil(H/q)` 个发生位。",
        "只要该 cell 与区间相交，envelope 已能容纳一个单位事件。因此",
        "",
        "```text",
        "D_y >= 1",
        "```",
        "",
        "不能推出",
        "",
        "```text",
        "D_y > U_T(I_y).",
        "```",
        "",
        "容量矛盾需要的是源侧释放质量放大，例如沿反例链强制产生可与 `H=P-y` 比较的一族行发生需求；若没有放大，",
        "该释放只能作为 singleton/sparse SAE 计费。",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{DEMAND}",
        f"  -> {AMPLIFICATION}",
        f"  AND {PAYMENT_INJECTION}",
        "```",
        "",
        "- `FirstBreakReleaseMassAmplificationOrSingletonSAE`：证明首破裂释放不是孤立单位事件，而会沿反例链放大；若不放大，则进入 singleton/sparse SAE。",
        "- `LowCarrierActualPaymentInjectionWithoutEnvelopeReuse`：证明放大的源侧压力确实注入同一低 carrier AP table，且证明不使用 AP envelope 饱和本身。",
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
            "- 本证书不证明 actual demand 下界已经足以超过 AP envelope。",
            "- 本证书只关闭单位释放下界与非循环需求来源纪律。",
            "- 最新主攻变为释放质量放大或 singleton/sparse SAE 排斥，以及低 carrier actual payment 注入。",
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
