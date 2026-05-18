#!/usr/bin/env python3
"""生成首破裂低 carrier 固定 residue 的 AP 骨架证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_low_carrier_residue_ap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.json

输出：
  data/prime-matrix-firstbreak-low-carrier-residue-ap-ledger.json
  docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.json
  docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-low-carrier-residue-ap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-low-carrier-residue-ap-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-low-carrier-residue-ap-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json",
    DOCS / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json",
    DOCS / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json",
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.md",
    DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json",
]

LOW_CARRIER = "LowCarrierFixedResidueColumnCRTPDECExclusion"
AP_CAPACITY = "LowCarrierResidueAPEnvelopeCapacityComparison"
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

REDUCED_LOW_CARRIER = f"{AP_CAPACITY} AND {DENSE_TABLE} AND {SPARSE_CELL}"


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


def build_rows(previous: dict[str, Any], lowmod: dict[str, Any], phase_schema: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 AP 骨架判定表。"""
    low_carrier_imported = LOW_CARRIER in previous.get("hardpoint_after_router", "")
    lowmod_route_imported = lowmod.get("pdec_columncrt_route_registered") is True
    phase_schema_imported = phase_schema.get("early_zero_phase_defect_schema_admission_closed") is True
    return [
        row(
            "LowCarrierFixedResidueImported",
            low_carrier_imported,
            False,
            "上一层把 small-LCM 的首个出口压到低 carrier 固定 residue 的 ColumnCRT/PDEC 排斥。",
            LOW_CARRIER,
        ),
        row(
            "ResidueToRowAPFormulaClosed",
            True,
            True,
            "固定 q 与列 residue a 时，覆盖条件 c≡a mod q 等价于行 t≡-a P^{-1} mod q。",
            "none for formula",
        ),
        row(
            "SingleResidueAPEnvelopeClosed",
            True,
            True,
            "在 I_y={y,...,P-1}、H=P-y 中，同一 (q,a) residue cell 的行命中数至多 ceil(H/q)。",
            "cell_load <= ceil(H/q)",
        ),
        row(
            "LowCarrierResidueTableFiniteClosed",
            True,
            True,
            "固定阈值 B 后，q<=B 的低 carrier residue cells 总数至多 sum_{q<=B} q，是低维有限表。",
            "finite low-carrier residue table",
        ),
        row(
            "LowEffectiveModColumnCRTImport",
            lowmod_route_imported,
            lowmod_route_imported,
            "仓库已有低有效模路由：共同因子/低商模异常若持久，必须登记为 PDEC/ColumnCRT。",
            DENSE_TABLE,
        ),
        row(
            "PersistentResidueTableIsPDEC",
            True,
            phase_schema_imported,
            "若某些低 carrier residue cells 持续超出 AP envelope 或承担正密度压力，它们构成同 formal unit 的低维 residue table PDEC。",
            DENSE_TABLE,
        ),
        row(
            "NonpersistentResidueCellsAreSparseSAE",
            True,
            phase_schema_imported,
            "若低 carrier residue cells 不持久复现，则它们不能形成支付链，只能进入 sparse SAE/LocalSurvivor。",
            SPARSE_CELL,
        ),
        row(
            "APEnvelopeCapacityComparisonOpen",
            False,
            False,
            "尚未证明反例链所需低 carrier 压力必超过 AP envelope，或证明低于 envelope 时仍不足以支付零行。",
            AP_CAPACITY,
        ),
        row(
            "LowCarrierFixedResidueReduced",
            True,
            False,
            "抽象低 carrier fixed-residue 出口被压成 AP envelope 容量比较、稠密 residue table PDEC、稀疏 cell SAE 三项。",
            REDUCED_LOW_CARRIER,
        ),
        row(
            "LowCarrierFixedResidueExcluded",
            False,
            False,
            "本步只给出 AP 骨架和命名分流，尚未排斥三项终端。",
            REDUCED_LOW_CARRIER,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、低 carrier 三项、其余 first-break 出口与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {REDUCED_LOW_CARRIER} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造低 carrier AP 骨架证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json")
    lowmod = load_json(DOCS / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json")
    phase_schema = load_json(DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json")
    rows = build_rows(previous, lowmod, phase_schema)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {REDUCED_LOW_CARRIER} "
        f"AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "低 carrier 固定 residue 分支已被压成行向 AP 骨架："
        "对固定 q 和列 residue a，覆盖相位强制行 t 落在唯一同余类 t≡-aP^{-1} mod q；"
        "因此在 H=P-y 的剩余行宽内，每个 residue cell 至多命中 ceil(H/q) 行。"
        "持续超出或正密度承担压力只能成为低维 residue table PDEC/ColumnCRT；"
        "非持久 cell 进入 sparse SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_low_carrier_residue_ap_router",
        "status": "firstbreak_low_carrier_fixed_residue_reduced_to_ap_table_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": LOW_CARRIER,
        "hardpoint_after_router": REDUCED_LOW_CARRIER,
        "residue_to_row_ap_formula_closed": True,
        "single_residue_ap_envelope_closed": True,
        "low_carrier_residue_table_finite_closed": True,
        "persistent_residue_table_pdec_registered": True,
        "nonpersistent_residue_cells_sae_registered": True,
        "ap_envelope_capacity_comparison_proved": False,
        "low_carrier_fixed_residue_excluded": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": AP_CAPACITY,
        "parallel_attack_targets": [DENSE_TABLE, SPARSE_CELL, LOW_SAE, HIGH_RANK, NONREPLAY_SAE, MOVING_CARRIER],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂低 carrier fixed-residue AP 骨架证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"residue_to_row_ap_formula_closed={fmt_bool(cert['residue_to_row_ap_formula_closed'])}",
        f"single_residue_ap_envelope_closed={fmt_bool(cert['single_residue_ap_envelope_closed'])}",
        f"low_carrier_residue_table_finite_closed={fmt_bool(cert['low_carrier_residue_table_finite_closed'])}",
        f"ap_envelope_capacity_comparison_proved={fmt_bool(cert['ap_envelope_capacity_comparison_proved'])}",
        f"low_carrier_fixed_residue_excluded={fmt_bool(cert['low_carrier_fixed_residue_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. AP 骨架引理",
        "",
        "首破裂后行区间记为 `I_y={y,...,P-1}`，长度 `H=P-y`。对低 carrier 素数 `q<P` 和固定列 residue `a mod q`，覆盖条件为",
        "",
        "```text",
        "tP+c == 0 mod q,   c == a mod q.",
        "```",
        "",
        "因此",
        "",
        "```text",
        "tP == -a mod q.",
        "```",
        "",
        "由于 `(P,q)=1`，得到唯一行同余类",
        "",
        "```text",
        "t == -a P^{-1} mod q.",
        "```",
        "",
        "所以同一 `(q,a)` residue cell 在 `I_y` 中最多命中",
        "",
        "```text",
        "ceil(H/q)",
        "```",
        "",
        "个行位置。固定阈值 `B` 后，所有 `q<=B` 的低 carrier cell 数至多 `sum_{q<=B} q`，于是低 carrier fixed-residue 压力是一个低维 AP table 问题。",
        "",
        "## 2. 三分出口",
        "",
        "低 carrier fixed-residue 出口更新为：",
        "",
        "```text",
        f"{LOW_CARRIER}",
        f"  -> {AP_CAPACITY}",
        f"  AND {DENSE_TABLE}",
        f"  AND {SPARSE_CELL}",
        "```",
        "",
        "- AP envelope 容量比较：证明反例所需低 carrier 压力超过 AP table 可供给，或证明未超过时仍不足以支付零行。",
        "- 稠密 residue table PDEC：若某些低维 cell 持久承担正密度压力或超出 envelope，则进入同 formal unit 的 ColumnCRT/PDEC。",
        "- 稀疏 cell SAE：若 cell 不持久，只能作为 sparse SAE/LocalSurvivor 计费。",
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
            "- 本证书不证明低 carrier fixed-residue 分支不存在。",
            "- 本证书只把该分支压成 AP table 容量比较、稠密 residue table PDEC 与稀疏 cell SAE。",
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
