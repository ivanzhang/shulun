#!/usr/bin/env python3
"""生成 endpoint pivot duplicate same-slot multiplicity-cap import 证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_pivot_duplicate_same_slot_multiplicity_cap_import_router.py
  python3 -m json.tool docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.json

输出：
  data/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-ledger.json
  docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.json
  docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-"
    "slot-accounting-router.json"
)
SOURCE_ATOM_CERT = (
    DOCS
    / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-"
    "dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-"
    "slot-source-atom-router.json"
)
SOURCE_ATOM_MULTIPLICITY_CERT = (
    DOCS
    / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-"
    "dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-"
    "slot-source-atom-multiplicity-fiber-router.json"
)

DUPLICATE_SLOT_MULTIPLICITY = "EndpointOrbitAlternatingCyclePivotPrimeDuplicateSameSlotSourceMultiplicityCapPDEC"
SOURCE_MULTIPLICITY = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
DUPLICATE_SPARSE = "EndpointOrbitAlternatingCyclePivotPrimeDuplicatePaymentSparseSAESummability"
SAME_AP_LOCK = "EndpointOrbitAlternatingCyclePivotPrimeSameAPTablePaymentInjectionLock"
CROSS_TABLE_SWITCH = "EndpointOrbitAlternatingCyclePivotPrimeCrossTableSwitchPDECOrMovingPivot"
BOUNDED_SUPPORT = "EndpointOrbitAlternatingCyclePivotPrimeBoundedSourceSupportEndpointSingletonFullMeanOrSparseSAE"
LONG_TRANSFER = "EndpointOrbitAlternatingCyclePivotPrimeLongSourceSupportMassTransferToLowCarrierDemandOrPDEC"
ENDPOINT_STRICT_GAP = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierAPEnvelopeStrictGapOrDenseTablePDEC"
DENSE_TABLE = "EndpointOrbitAlternatingCyclePivotPrimeDenseLowCarrierResidueTablePDECExclusion"
SPARSE_CELL = "EndpointOrbitAlternatingCyclePivotPrimeSparseLowCarrierResidueCellSAESummability"
LOW_SAE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "EndpointOrbitAlternatingCyclePivotPrimeHighCarrierRankDeficitOrSingletonSAE"
NONREPLAY_SAE = "EndpointOrbitAlternatingCyclePivotPrimeNonreplaySparseSAESummability"
MOVING_PIVOT = "EndpointOrbitAlternatingCycleMovingPivotPrimePhaseSlipPDECExclusion"
SPARSE_SCALE = "SparseScaleLadderSAESummability"
ENDPOINT_SINGLETON = "StableLadderEndpointSingletonAtomSAE"
FULL_CYCLE_MEAN = "EndpointOrbitFullCycleMeanAtomSAE"

IMPORT = "StableLadderEndpointOrbitPivotPrimeDuplicateSameSlotMultiplicityImportedLedger"
SAME_SLOT_KEY = "StableLadderEndpointOrbitPivotPrimeDuplicateSameSlotKeyCarriesSourceAtomLedger"
EXTRA_UNIT = "StableLadderEndpointOrbitPivotPrimeDuplicateExtraUnitSameSourceAtomLedger"
EXISTING_CAP = "StableLadderEndpointOrbitPivotPrimeDuplicateMultiplicityImportedToExistingSourceAtomCapLedger"
NO_NEW_CAP = "StableLadderEndpointOrbitPivotPrimeDuplicateMultiplicityNoNewPaymentCapacityLedger"
NO_DUP_SLOT_MULT = "NoIndependentEndpointPivotPrimeDuplicateSameSlotMultiplicityAfterCapImportLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def source_hashes() -> dict[str, str]:
    """登记本脚本与上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, SOURCE_ATOM_CERT, SOURCE_ATOM_MULTIPLICITY_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 duplicate same-slot multiplicity 特例并入已有 source-atom multiplicity cap。"""
    target = previous.get("next_direct_attack_target", "")
    if DUPLICATE_SLOT_MULTIPLICITY in target:
        return target.replace(DUPLICATE_SLOT_MULTIPLICITY, SOURCE_MULTIPLICITY)
    return f"{target} AND {SOURCE_MULTIPLICITY}" if target else SOURCE_MULTIPLICITY


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        SAME_SLOT_KEY,
        EXTRA_UNIT,
        EXISTING_CAP,
        NO_NEW_CAP,
        NO_DUP_SLOT_MULT,
        new_target,
    ]
    return " AND ".join(ledgers)


def replace_latest_basis(previous: dict[str, Any], reduced: str) -> str:
    """更新长活动基。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    old = previous.get("next_direct_attack_target", "")
    if basis and old and old in basis:
        return basis.replace(old, reduced)
    return reduced


def cap_import_records() -> list[dict[str, str]]:
    """列出 duplicate same-slot 到 source-atom cap 的字段投影。"""
    return [
        {"field": "same_ap_table_key", "meaning": "上一层锁定的同一 endpoint packet、q、residue、AP class 与窗口。"},
        {"field": "source_support_atom", "meaning": "payment key 中已经固定的源侧 atom 字段。"},
        {"field": "extra_source_unit", "meaning": "同一 slot 上第二个及以后的 source-support 单位。"},
        {"field": "multiplicity_count", "meaning": "同一 source atom 对同一 slot 的额外出现重数。"},
        {"field": "existing_cap_outlet", "meaning": "已有 SourceAtomMultiplicityCapPDECCap，负责该类持久重数异常。"},
    ]


def build_rows(
    previous: dict[str, Any],
    source_atom: dict[str, Any],
    source_atom_multiplicity: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 duplicate same-slot multiplicity cap-import 判定表。"""
    imported = DUPLICATE_SLOT_MULTIPLICITY in previous.get("next_direct_attack_target", "")
    same_slot_key = previous.get("endpoint_duplicate_same_canonical_slot_key_closed") is True
    no_new_capacity = previous.get("endpoint_duplicate_count_not_new_capacity_closed") is True
    source_atom_imported = SOURCE_MULTIPLICITY in source_atom.get("next_direct_attack_target", "")
    cap_carried = SOURCE_MULTIPLICITY in source_atom_multiplicity.get("next_direct_attack_target", "")
    return [
        row("EndpointDuplicateSameSlotMultiplicityImported", imported, False, "导入 duplicate same-slot source multiplicity cap/PDEC 硬点。", DUPLICATE_SLOT_MULTIPLICITY),
        row("EndpointDuplicateSameSlotKeyCarriesSourceAtom", imported and same_slot_key, True, "same canonical slot key 已包含 source-support atom 字段；同槽重复不能换源。", SAME_SLOT_KEY),
        row("EndpointDuplicateExtraUnitSameSourceAtom", imported and same_slot_key, True, "第二个及以后的同槽 source unit 是同一 source atom 的重数出现。", EXTRA_UNIT),
        row("EndpointDuplicateMultiplicityNoNewPaymentCapacity", imported and no_new_capacity, True, "这些额外单位不能产生新 AP-table capacity，只能作为重数异常计费。", NO_NEW_CAP),
        row("ExistingSourceAtomMultiplicityCapImported", source_atom_imported or cap_carried, False, "已有 source-atom multiplicity-cap PDEC/cap 正是该持久重数异常的通用出口。", SOURCE_MULTIPLICITY),
        row("NoIndependentDuplicateSameSlotMultiplicityAfterCapImport", imported, True, "duplicate same-slot multiplicity 不再作为独立 endpoint 专属出口保留。", NO_DUP_SLOT_MULT),
        row("EndpointDuplicateSameSlotMultiplicityReduced", imported, False, "本步只把 duplicate 专属 cap 并入既有 source-atom multiplicity cap；该 cap 本身仍未排斥。", SOURCE_MULTIPLICITY),
        row("SourceAtomMultiplicityCapProved", False, False, "未证明 source-atom multiplicity cap/PDEC 不存在。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    source_atom = load_json(SOURCE_ATOM_CERT)
    source_atom_multiplicity = load_json(SOURCE_ATOM_MULTIPLICITY_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, source_atom, source_atom_multiplicity, new_target)
    imported = any(item["gate"] == "EndpointDuplicateSameSlotMultiplicityImported" and item["closed"] for item in rows)
    reduced_closed = any(
        item["gate"] == "NoIndependentDuplicateSameSlotMultiplicityAfterCapImport" and item["closed"]
        for item in rows
    )
    cap_imported = any(item["gate"] == "ExistingSourceAtomMultiplicityCapImported" for item in rows)
    plain = (
        "duplicate same-slot source multiplicity 已并入既有 source-atom multiplicity cap："
        "same canonical slot key 已固定 source-support atom；同槽额外 source unit 不能增加支付容量，"
        "只能作为该 source atom 的持久重数异常，回到既有 SourceAtomMultiplicityCapPDECCap。"
        "本步不排斥该 cap，也不证明 duplicate sparse SAE。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_duplicate_same_slot_multiplicity_cap_import_router",
        "status": "endpoint_pivot_duplicate_same_slot_multiplicity_imported_to_existing_source_atom_cap_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_atom_certificate": str(SOURCE_ATOM_CERT.relative_to(ROOT)),
        "source_atom_multiplicity_certificate": str(SOURCE_ATOM_MULTIPLICITY_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_duplicate_same_slot_multiplicity_imported": imported,
        "endpoint_duplicate_same_slot_key_carries_source_atom": previous.get("endpoint_duplicate_same_canonical_slot_key_closed") is True,
        "endpoint_duplicate_extra_unit_same_source_atom_closed": imported,
        "endpoint_duplicate_multiplicity_no_new_payment_capacity": previous.get("endpoint_duplicate_count_not_new_capacity_closed") is True,
        "existing_source_atom_multiplicity_cap_imported": cap_imported,
        "endpoint_duplicate_same_slot_multiplicity_reduced_to_existing_cap": reduced_closed,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_duplicate_payment_sparse_sae_summability_proved": False,
        "endpoint_same_ap_table_payment_injection_lock_proved": False,
        "endpoint_cross_table_switch_pdec_or_moving_pivot_proved": False,
        "endpoint_bounded_source_support_sae_proved": False,
        "endpoint_long_source_support_mass_transfer_proved": False,
        "endpoint_pivot_ap_envelope_strict_gap_proved": False,
        "endpoint_pivot_dense_low_carrier_residue_table_pdec_proved": False,
        "endpoint_pivot_sparse_low_carrier_residue_cell_sae_proved": False,
        "endpoint_pivot_low_carrier_nonpersistent_sparse_sae_proved": False,
        "endpoint_pivot_high_carrier_rank_deficit_proved": False,
        "endpoint_pivot_nonreplay_sparse_sae_proved": False,
        "endpoint_pivot_moving_prime_phase_slip_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": DUPLICATE_SLOT_MULTIPLICITY,
        "hardpoint_after_router": SOURCE_MULTIPLICITY,
        "old_exits": [DUPLICATE_SLOT_MULTIPLICITY],
        "new_exits": [SOURCE_MULTIPLICITY],
        "parallel_open_exits": [
            DUPLICATE_SPARSE,
            SAME_AP_LOCK,
            CROSS_TABLE_SWITCH,
            BOUNDED_SUPPORT,
            LONG_TRANSFER,
            ENDPOINT_STRICT_GAP,
            DENSE_TABLE,
            SPARSE_CELL,
            LOW_SAE,
            HIGH_RANK,
            NONREPLAY_SAE,
            MOVING_PIVOT,
            SPARSE_SCALE,
            ENDPOINT_SINGLETON,
            FULL_CYCLE_MEAN,
        ],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "cap_import_records": cap_import_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot duplicate same-slot multiplicity-cap import 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_duplicate_same_slot_multiplicity_imported={fmt_bool(cert['endpoint_duplicate_same_slot_multiplicity_imported'])}",
        f"endpoint_duplicate_same_slot_key_carries_source_atom={fmt_bool(cert['endpoint_duplicate_same_slot_key_carries_source_atom'])}",
        f"endpoint_duplicate_extra_unit_same_source_atom_closed={fmt_bool(cert['endpoint_duplicate_extra_unit_same_source_atom_closed'])}",
        f"endpoint_duplicate_multiplicity_no_new_payment_capacity={fmt_bool(cert['endpoint_duplicate_multiplicity_no_new_payment_capacity'])}",
        f"existing_source_atom_multiplicity_cap_imported={fmt_bool(cert['existing_source_atom_multiplicity_cap_imported'])}",
        f"endpoint_duplicate_same_slot_multiplicity_reduced_to_existing_cap={fmt_bool(cert['endpoint_duplicate_same_slot_multiplicity_reduced_to_existing_cap'])}",
        f"source_atom_multiplicity_cap_pdec_cap_proved={fmt_bool(cert['source_atom_multiplicity_cap_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 字段投影",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["cap_import_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "duplicate same-slot multiplicity 的投影为：",
            "",
            "```text",
            "same canonical slot key includes source_support_atom",
            "extra source units on the same slot => multiplicity of that source atom",
            "persistent extra multiplicity => existing SourceAtomMultiplicityCapPDECCap",
            "```",
            "",
            "## 2. 出口更新",
            "",
            "```text",
            cert["hardpoint_before_router"],
            f"  -> {SOURCE_MULTIPLICITY}",
            "```",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书不证明 source-atom multiplicity cap/PDEC。",
            "- 本证书不证明 duplicate-payment sparse SAE 求和。",
            "- 本证书只移除 duplicate 专属 same-slot multiplicity cap 作为独立出口。",
            "- same AP table injection、cross-table switch、bounded/long support、strict gap、dense/sparse table、高秩、nonreplay、moving-pivot 与 endpoint 并行出口仍未排斥。",
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
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown。"""
    cert = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_md(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
