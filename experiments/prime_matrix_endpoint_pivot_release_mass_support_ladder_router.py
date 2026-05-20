#!/usr/bin/env python3
"""生成 endpoint pivot release-mass 的支撑阶梯证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_pivot_release_mass_support_ladder_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.json"
)
CYCLE_SKELETON_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.json"
)
EDGE_SPIKE_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json"

ENDPOINT_AMPLIFICATION = "EndpointOrbitAlternatingCyclePivotPrimeReleaseMassAmplificationOrEndpointSingletonSAE"
BOUNDED_SUPPORT = "EndpointOrbitAlternatingCyclePivotPrimeBoundedSourceSupportEndpointSingletonFullMeanOrSparseSAE"
LONG_TRANSFER = "EndpointOrbitAlternatingCyclePivotPrimeLongSourceSupportMassTransferToLowCarrierDemandOrPDEC"
ENDPOINT_PAYMENT_INJECTION = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierActualPaymentInjectionWithoutEnvelopeReuse"
ENDPOINT_STRICT_GAP = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierAPEnvelopeStrictGapOrDenseTablePDEC"
DENSE_TABLE = "EndpointOrbitAlternatingCyclePivotPrimeDenseLowCarrierResidueTablePDECExclusion"
SPARSE_CELL = "EndpointOrbitAlternatingCyclePivotPrimeSparseLowCarrierResidueCellSAESummability"
LOW_SAE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "EndpointOrbitAlternatingCyclePivotPrimeHighCarrierRankDeficitOrSingletonSAE"
NONREPLAY_SAE = "EndpointOrbitAlternatingCyclePivotPrimeNonreplaySparseSAESummability"
MOVING_PIVOT = "EndpointOrbitAlternatingCycleMovingPivotPrimePhaseSlipPDECExclusion"
SOURCE_MULTIPLICITY = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
SPARSE_SCALE = "SparseScaleLadderSAESummability"
ENDPOINT_SINGLETON = "StableLadderEndpointSingletonAtomSAE"
FULL_CYCLE_MEAN = "EndpointOrbitFullCycleMeanAtomSAE"

REDUCED_AMPLIFICATION = f"{BOUNDED_SUPPORT} AND {LONG_TRANSFER}"

IMPORT = "StableLadderEndpointOrbitPivotPrimeReleaseMassImportedForSupportLadderLedger"
UNIT_NOT_ENOUGH = "StableLadderEndpointOrbitPivotPrimeUnitReleaseNotAmplificationLedger"
FINITE_SUPPORT = "StableLadderEndpointOrbitPivotPrimeReleaseSourceFiniteSupportLedger"
SUPPORT_MASS = "StableLadderEndpointOrbitPivotPrimeSourceSupportMassLedger"
THRESHOLD = "StableLadderEndpointOrbitPivotPrimeSourceSupportThresholdDichotomyLedger"
BOUNDED_LEDGER = "StableLadderEndpointOrbitPivotPrimeBoundedSourceSupportRouteLedger"
LONG_LEDGER = "StableLadderEndpointOrbitPivotPrimeLongSourceSupportTransferRouteLedger"
NO_AMPLIFICATION = "NoIndependentEndpointPivotPrimeReleaseMassAmplificationAfterSupportLadderLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, CYCLE_SKELETON_CERT, EDGE_SPIKE_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 release-mass amplification 硬点替换为支撑阶梯二出口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_AMPLIFICATION})"
    if ENDPOINT_AMPLIFICATION in target:
        return target.replace(ENDPOINT_AMPLIFICATION, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        UNIT_NOT_ENOUGH,
        FINITE_SUPPORT,
        SUPPORT_MASS,
        THRESHOLD,
        BOUNDED_LEDGER,
        LONG_LEDGER,
        NO_AMPLIFICATION,
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


def build_rows(
    previous: dict[str, Any],
    cycle_skeleton: dict[str, Any],
    edge_spike: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 endpoint release-mass 支撑阶梯判定表。"""
    imported = ENDPOINT_AMPLIFICATION in previous.get("next_direct_attack_target", "")
    unit_not_enough = previous.get("endpoint_unit_demand_not_gap_sufficient") is True
    finite_support = cycle_skeleton.get("endpoint_signed_depth_flux_finite_support_skeleton_closed") is True
    unit_atoms = cycle_skeleton.get("endpoint_signed_depth_flux_unit_atom_expansion_closed") is True
    singleton_absorption = edge_spike.get("endpoint_orbit_edge_spike_singleton_atom_absorption_closed") is True
    full_mean_absorption = edge_spike.get("endpoint_orbit_edge_spike_full_cycle_mean_atom_absorption_closed") is True
    return [
        row("EndpointReleaseMassImportedForSupportLadder", imported, False, "导入 endpoint actual-demand source-cut 后的 release-mass amplification 硬点。", ENDPOINT_AMPLIFICATION),
        row("EndpointUnitReleaseNotAmplificationClosed", imported and unit_not_enough, True, "单个 source-tagged endpoint incidence 只是单位需求，不能作为 AP envelope gap。", UNIT_NOT_ENOUGH),
        row("EndpointReleaseSourceFiniteSupportClosed", imported and finite_support and unit_atoms, True, "signed-depth/flux skeleton 已把 endpoint 源侧质量展成有限支撑单位原子。", FINITE_SUPPORT),
        row("EndpointSourceSupportMassLedgerClosed", imported and finite_support and unit_atoms, True, "释放质量只能来自源侧单位支撑基数 M；不存在匿名连续质量池。", SUPPORT_MASS),
        row("EndpointSourceSupportThresholdDichotomyClosed", imported, True, "对任意阈值 A，M<A 是短支撑，M>=A 是长支撑。", THRESHOLD),
        row("EndpointBoundedSupportRouteRegistered", imported and singleton_absorption and full_mean_absorption, False, "短支撑不能给出可比 AP demand；必须进入 endpoint singleton、full-cycle mean、source-multiplicity 或 sparse SAE。", BOUNDED_SUPPORT),
        row("EndpointLongSupportTransferRouteRegistered", imported, False, "长支撑才可能产生放大；仍需证明它非循环转移为 low-carrier AP demand，否则是 PDEC/SAE。", LONG_TRANSFER),
        row("NoIndependentEndpointReleaseMassAmplificationAfterSupportLadder", imported, True, "release-mass amplification 不再作为匿名单出口保留。", NO_AMPLIFICATION),
        row("EndpointReleaseMassAmplificationReduced", imported, False, "本步只完成支撑阶梯降维；短支撑 SAE 与长支撑转移仍未排斥。", REDUCED_AMPLIFICATION),
        row("EndpointReleaseMassAmplificationProved", False, False, "未证明 endpoint release mass 已经放大到超过 AP envelope。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    cycle_skeleton = load_json(CYCLE_SKELETON_CERT)
    edge_spike = load_json(EDGE_SPIKE_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, cycle_skeleton, edge_spike, new_target)
    imported = any(item["gate"] == "EndpointReleaseMassImportedForSupportLadder" and item["closed"] for item in rows)
    reduced_closed = any(
        item["gate"] == "NoIndependentEndpointReleaseMassAmplificationAfterSupportLadder" and item["closed"]
        for item in rows
    )
    plain = (
        "endpoint release-mass amplification 已被压成有限支撑阶梯：单位源点不构成 AP envelope gap；"
        "释放质量只能来自 signed-depth/flux skeleton 的 source-tagged unit support。"
        "若支撑短，则必须进入 endpoint singleton、full-cycle mean、source-multiplicity 或 sparse SAE；"
        "若支撑长，才需要证明它非循环转移为低 carrier AP demand，否则转移失败是 PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_release_mass_support_ladder_router",
        "status": "endpoint_pivot_release_mass_reduced_to_support_ladder_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "cycle_skeleton_certificate": str(CYCLE_SKELETON_CERT.relative_to(ROOT)),
        "edge_spike_singleton_certificate": str(EDGE_SPIKE_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_release_mass_amplification_imported": imported,
        "endpoint_unit_release_not_amplification_closed": imported,
        "endpoint_release_source_finite_support_closed": imported,
        "endpoint_source_support_mass_ledger_closed": imported,
        "endpoint_source_support_threshold_dichotomy_closed": imported,
        "endpoint_release_mass_reduced_to_support_ladder": reduced_closed,
        "endpoint_bounded_source_support_sae_proved": False,
        "endpoint_long_source_support_mass_transfer_proved": False,
        "endpoint_release_mass_amplification_proved": False,
        "endpoint_low_carrier_payment_injection_proved": False,
        "endpoint_pivot_ap_envelope_strict_gap_proved": False,
        "endpoint_pivot_dense_low_carrier_residue_table_pdec_proved": False,
        "endpoint_pivot_sparse_low_carrier_residue_cell_sae_proved": False,
        "endpoint_pivot_low_carrier_nonpersistent_sparse_sae_proved": False,
        "endpoint_pivot_high_carrier_rank_deficit_proved": False,
        "endpoint_pivot_nonreplay_sparse_sae_proved": False,
        "endpoint_pivot_moving_prime_phase_slip_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ENDPOINT_AMPLIFICATION,
        "hardpoint_after_router": REDUCED_AMPLIFICATION,
        "old_exits": [ENDPOINT_AMPLIFICATION],
        "new_exits": [BOUNDED_SUPPORT, LONG_TRANSFER],
        "parallel_open_exits": [
            ENDPOINT_PAYMENT_INJECTION,
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
            SOURCE_MULTIPLICITY,
        ],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot release-mass support-ladder 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_release_mass_amplification_imported={fmt_bool(cert['endpoint_release_mass_amplification_imported'])}",
        f"endpoint_unit_release_not_amplification_closed={fmt_bool(cert['endpoint_unit_release_not_amplification_closed'])}",
        f"endpoint_release_source_finite_support_closed={fmt_bool(cert['endpoint_release_source_finite_support_closed'])}",
        f"endpoint_source_support_mass_ledger_closed={fmt_bool(cert['endpoint_source_support_mass_ledger_closed'])}",
        f"endpoint_source_support_threshold_dichotomy_closed={fmt_bool(cert['endpoint_source_support_threshold_dichotomy_closed'])}",
        f"endpoint_release_mass_reduced_to_support_ladder={fmt_bool(cert['endpoint_release_mass_reduced_to_support_ladder'])}",
        f"endpoint_long_source_support_mass_transfer_proved={fmt_bool(cert['endpoint_long_source_support_mass_transfer_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 支撑阶梯",
        "",
        "endpoint actual demand 的单位源点不能直接给 AP envelope gap。释放质量只能来自 signed-depth/flux skeleton 的有限 source-tagged unit support；记其基数为 `M`。",
        "",
        "对任意阈值 `A`，只有两支：",
        "",
        "```text",
        "M < A   => bounded source support / endpoint singleton-full-mean-sparse branch,",
        "M >= A  => long source support mass-transfer or PDEC branch.",
        "```",
        "",
        "## 2. 出口更新",
        "",
        "```text",
        cert["hardpoint_before_router"],
        f"  -> {BOUNDED_SUPPORT}",
        f"  AND {LONG_TRANSFER}",
        "```",
        "",
        "短支撑不能形成可比容量压力；长支撑仍需证明能非循环转移到同一低 carrier AP table。转移失败不是免费误差，而是 dense-table、sparse-cell、高秩、moving-pivot 或 endpoint 并行出口。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "- 本证书不证明 release mass 已放大到超过 AP envelope。",
            "- 本证书只把放大源压到有限 source support 的长短二分。",
            "- bounded support SAE 和 long support mass transfer 仍未完成。",
            "- payment injection、strict gap、dense-table、sparse-cell、高秩、moving-pivot 与 endpoint 并行出口仍未排斥。",
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
