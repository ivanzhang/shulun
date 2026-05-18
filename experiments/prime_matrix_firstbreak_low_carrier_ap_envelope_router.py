#!/usr/bin/env python3
"""生成首破裂低 carrier AP table 精确 envelope 证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_low_carrier_ap_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json

输出：
  data/prime-matrix-firstbreak-low-carrier-ap-envelope-ledger.json
  docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json
  docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-low-carrier-ap-envelope-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-low-carrier-residue-ap-router.json",
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.md",
    DOCS / "prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md",
    DOCS / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json",
    DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json",
]

AP_CAPACITY = "LowCarrierResidueAPEnvelopeCapacityComparison"
EXACT_ENV = "LowCarrierAPExactEnvelopeLedger"
DEMAND = "ActualLowCarrierRowIncidenceDemandLowerBound"
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

REDUCED_AP_CAPACITY = f"{DEMAND} AND {STRICT_GAP}"


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


def build_rows(previous: dict[str, Any], phase_schema: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 AP envelope 判定表。"""
    ap_capacity_imported = previous.get("next_direct_attack_target") == AP_CAPACITY
    phase_schema_imported = phase_schema.get("early_zero_phase_defect_schema_admission_closed") is True
    return [
        row(
            "APEnvelopeCapacityImported",
            ap_capacity_imported,
            False,
            "上一层把低 carrier fixed-residue 出口压到 AP envelope 容量比较。",
            AP_CAPACITY,
        ),
        row(
            "CellCountFormulaClosed",
            True,
            True,
            "对任意 table T，U_T(I)=sum_{(q,a) in T} #{t in I:t≡-aP^{-1} mod q}。",
            EXACT_ENV,
        ),
        row(
            "SingleCellSharpBoundClosed",
            True,
            True,
            "单个 (q,a) cell 的行发生数不超过 floor((H+q-1)/q)=ceil(H/q)。",
            "N_{q,a}(I)<=ceil(H/q)",
        ),
        row(
            "AllResiduesExactMassClosed",
            True,
            True,
            "固定 q 时，所有 a mod q 的 cell 在 I_y 中的发生数精确求和为 H；每一行只选择一个 residue。",
            "sum_a N_{q,a}(I)=H",
        ),
        row(
            "SelectedTableEnvelopeClosed",
            True,
            True,
            "任意选定低 carrier table T 的 envelope 为 U_T<=sum_{(q,a) in T} ceil(H/q)，且 U_T<=H*|Q(T)|。",
            EXACT_ENV,
        ),
        row(
            "FormalEnvelopeNotActualDemandGuard",
            True,
            True,
            "AP envelope 只是可供给上界；要形成矛盾还必须证明反例链强制的 actual row-incidence demand 超过该上界。",
            DEMAND,
        ),
        row(
            "DenseTablePDECRouteRegistered",
            True,
            phase_schema_imported,
            "若 table T 为了接近 envelope 必须在许多低 carrier residue 上持久占位，则它是同 formal unit 的稠密 residue table PDEC。",
            DENSE_TABLE,
        ),
        row(
            "SparseTableSAERouteRegistered",
            True,
            phase_schema_imported,
            "若 T 稀疏或不持久，AP envelope 发生只进入 sparse cell SAE/LocalSurvivor，不形成稳定反例支付链。",
            SPARSE_CELL,
        ),
        row(
            "APCapacityComparisonReduced",
            True,
            False,
            "容量比较被拆成 exact envelope ledger、actual demand 下界、以及 envelope strict gap 或 dense-table PDEC。",
            REDUCED_AP_CAPACITY,
        ),
        row(
            "APCapacityComparisonProved",
            False,
            False,
            "本步不证明 actual demand 下界，也不排斥 dense table PDEC；只关闭 envelope 公式。",
            REDUCED_AP_CAPACITY,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、AP demand/gap、PDEC/SAE 终端与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {REDUCED_AP_CAPACITY} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造低 carrier AP envelope 证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-low-carrier-residue-ap-router.json")
    phase_schema = load_json(DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json")
    rows = build_rows(previous, phase_schema)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {REDUCED_AP_CAPACITY} AND {DENSE_TABLE} AND {SPARSE_CELL} "
        f"AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "低 carrier AP envelope 已被精确化：任意 residue table T 的行发生量为 "
        "U_T(I)=sum_{(q,a) in T} N_{q,a}(I)，其中 N_{q,a}(I)<=ceil(H/q)；"
        "更尖锐地，固定 q 时 sum_a N_{q,a}(I)=H。"
        "因此容量比较的形式上界已闭合，真正剩余是证明反例链的 actual row-incidence demand "
        "超过该 envelope，或把接近 envelope 的稠密低维 table 登记并排斥为 PDEC。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_low_carrier_ap_envelope_router",
        "status": "firstbreak_low_carrier_ap_exact_envelope_closed_demand_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": AP_CAPACITY,
        "hardpoint_after_router": REDUCED_AP_CAPACITY,
        "cell_count_formula_closed": True,
        "single_cell_sharp_bound_closed": True,
        "all_residues_exact_mass_closed": True,
        "selected_table_envelope_closed": True,
        "formal_envelope_not_actual_demand_guard": True,
        "ap_capacity_comparison_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": DEMAND,
        "parallel_attack_targets": [STRICT_GAP, DENSE_TABLE, SPARSE_CELL, LOW_SAE, HIGH_RANK, NONREPLAY_SAE, MOVING_CARRIER],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂低 carrier AP exact-envelope 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"cell_count_formula_closed={fmt_bool(cert['cell_count_formula_closed'])}",
        f"single_cell_sharp_bound_closed={fmt_bool(cert['single_cell_sharp_bound_closed'])}",
        f"all_residues_exact_mass_closed={fmt_bool(cert['all_residues_exact_mass_closed'])}",
        f"selected_table_envelope_closed={fmt_bool(cert['selected_table_envelope_closed'])}",
        f"ap_capacity_comparison_proved={fmt_bool(cert['ap_capacity_comparison_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Exact envelope",
        "",
        "首破裂后行区间 `I_y` 长度为 `H=P-y`。对低 carrier residue table",
        "",
        "```text",
        "T subset {(q,a): q<=B, a mod q},",
        "```",
        "",
        "定义行发生量",
        "",
        "```text",
        "U_T(I_y)=sum_{(q,a) in T} #{t in I_y: t == -a P^{-1} mod q}.",
        "```",
        "",
        "单个 cell 满足",
        "",
        "```text",
        "#{t in I_y: t == -a P^{-1} mod q} <= ceil(H/q).",
        "```",
        "",
        "更尖锐的是，固定 `q` 时所有 residue cell 精确分割行区间：",
        "",
        "```text",
        "sum_{a mod q} #{t in I_y: t == -a P^{-1} mod q} = H.",
        "```",
        "",
        "因为每个行 `t` 对模 `q` 只选择一个 residue `a=-tP mod q`。所以任意 table 的安全 envelope 为",
        "",
        "```text",
        "U_T(I_y) <= sum_{(q,a) in T} ceil(H/q),",
        "U_T(I_y) <= H * |{q: exists a with (q,a) in T}|.",
        "```",
        "",
        "## 2. 剩余真实容量接口",
        "",
        "AP envelope 只是形式可供给上界。要把它升级为矛盾，还需要同一 formal unit 下的 actual 需求下界：",
        "",
        "```text",
        "ActualLowCarrierRowIncidenceDemandLowerBound",
        "```",
        "",
        "并证明该需求超过 exact envelope；若某个低维 table 接近 envelope，则它必须是稠密 residue table PDEC，而不是普通误差。",
        "",
        "因此本硬点更新为：",
        "",
        "```text",
        f"{AP_CAPACITY}",
        f"  -> {DEMAND}",
        f"  AND {STRICT_GAP}",
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 新活动基",
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
            "## 5. 诚实边界",
            "",
            "- 本证书不证明低 carrier AP 分支不存在。",
            "- 本证书只关闭 AP table 的 exact envelope 公式。",
            "- actual demand 下界、strict gap 和 dense-table PDEC 排斥仍未完成。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
