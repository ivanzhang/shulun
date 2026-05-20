#!/usr/bin/env python3
"""生成 endpoint pivot actual demand 的源侧切口证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_pivot_actual_demand_source_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.md
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
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-"
    "fixed-residue-ap-table-router.json"
)
FIRSTBREAK_SOURCE_CUT_CERT = DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json"
ENDPOINT_DYNAMIC_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.json"
)

ENDPOINT_DEMAND = "EndpointOrbitAlternatingCyclePivotPrimeActualLowCarrierRowIncidenceDemandLowerBound"
ENDPOINT_AMPLIFICATION = "EndpointOrbitAlternatingCyclePivotPrimeReleaseMassAmplificationOrEndpointSingletonSAE"
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

REDUCED_DEMAND = f"{ENDPOINT_AMPLIFICATION} AND {ENDPOINT_PAYMENT_INJECTION}"

IMPORT = "StableLadderEndpointOrbitPivotPrimeActualDemandImportedForSourceCutLedger"
UNIT = "StableLadderEndpointOrbitPivotPrimeUnitIncidenceDemandLedger"
UNIT_NOT_ENOUGH = "StableLadderEndpointOrbitPivotPrimeUnitDemandNotEnvelopeGapLedger"
NO_RECYCLING = "StableLadderEndpointOrbitPivotPrimeNoAPEnvelopeRecyclingDemandGuardLedger"
AMPLIFICATION_LEDGER = "StableLadderEndpointOrbitPivotPrimeReleaseMassAmplificationRouteLedger"
PAYMENT_LEDGER = "StableLadderEndpointOrbitPivotPrimeLowCarrierPaymentInjectionRouteLedger"
NO_DEMAND = "NoIndependentEndpointPivotPrimeActualDemandAfterSourceCutLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, FIRSTBREAK_SOURCE_CUT_CERT, ENDPOINT_DYNAMIC_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 endpoint actual demand 硬点替换为源侧放大与支付注入接口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_DEMAND})"
    if ENDPOINT_DEMAND in target:
        return target.replace(ENDPOINT_DEMAND, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        UNIT,
        UNIT_NOT_ENOUGH,
        NO_RECYCLING,
        AMPLIFICATION_LEDGER,
        PAYMENT_LEDGER,
        NO_DEMAND,
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
    firstbreak_source_cut: dict[str, Any],
    endpoint_dynamic: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 endpoint actual-demand 源侧切口判定表。"""
    imported = ENDPOINT_DEMAND in previous.get("next_direct_attack_target", "")
    template_guard = firstbreak_source_cut.get("no_envelope_recycling_guard") is True
    dynamic_imported = endpoint_dynamic.get("endpoint_orbit_signed_depth_flux_packet_registered") is True
    return [
        row("EndpointActualDemandImportedForSourceCut", imported, False, "导入 AP-envelope 层剩余的 endpoint actual low-carrier row-incidence demand。", ENDPOINT_DEMAND),
        row("EndpointUnitIncidenceDemandClosed", imported, True, "若 endpoint fixed-residue actual-demand 分支为真，则至少有一个源侧标记的 endpoint row/cell incidence 单位。", UNIT),
        row("EndpointDynamicPacketSourceImported", dynamic_imported, dynamic_imported, "endpoint dynamic signed-depth flux packet 提供源侧带符号单位的命名载体，避免把匿名 envelope 计数当成 demand。", IMPORT),
        row("EndpointUnitDemandNotGapSufficient", imported, True, "单位 incidence 不足以打穿 AP envelope；单个低 carrier cell 的 envelope 已可容纳一个命中。", UNIT_NOT_ENOUGH),
        row("EndpointNoAPEnvelopeRecyclingGuard", imported and template_guard, True, "actual demand 必须来自 endpoint 源侧单位和反例链传播，不能从 AP envelope 接近饱和反推，避免循环论证。", NO_RECYCLING),
        row("EndpointReleaseMassAmplificationRouteRegistered", imported, False, "若要超过 exact envelope，源侧单位必须沿 endpoint orbit 放大；若不能放大，则进入 endpoint singleton/full-cycle mean/source-multiplicity 或 sparse SAE。", ENDPOINT_AMPLIFICATION),
        row("EndpointLowCarrierPaymentInjectionRouteRegistered", imported, False, "放大后的源侧压力还必须非循环地注入同一低 carrier AP table；失败则回流到 dense-table PDEC、sparse-cell SAE、高秩或 moving-pivot。", ENDPOINT_PAYMENT_INJECTION),
        row("NoIndependentEndpointActualDemandAfterSourceCut", imported, True, "endpoint actual demand 不再作为匿名单出口保留。", NO_DEMAND),
        row("EndpointActualDemandReduced", imported, False, "本步只给出源侧切口；释放质量放大和低 carrier 支付注入仍未证明。", REDUCED_DEMAND),
        row("EndpointActualDemandProved", False, False, "未证明 endpoint actual demand 超过 AP envelope。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    firstbreak_source_cut = load_json(FIRSTBREAK_SOURCE_CUT_CERT)
    endpoint_dynamic = load_json(ENDPOINT_DYNAMIC_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, firstbreak_source_cut, endpoint_dynamic, new_target)
    imported = any(item["gate"] == "EndpointActualDemandImportedForSourceCut" and item["closed"] for item in rows)
    reduced_closed = any(item["gate"] == "NoIndependentEndpointActualDemandAfterSourceCut" and item["closed"] for item in rows)
    plain = (
        "endpoint actual demand 下界已被切到源侧：活跃 fixed-residue demand 至少给出一个"
        " source-tagged endpoint incidence，但单位需求不足以超过 AP exact-envelope。"
        "真正剩余是证明源侧释放质量沿 endpoint orbit 放大，且非循环地注入同一低 carrier AP table；"
        "否则分别进入 endpoint singleton/full-cycle/source-multiplicity/sparse SAE 或 dense-table/sparse-cell/高秩/moving-pivot 出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_actual_demand_source_cut_router",
        "status": "endpoint_pivot_actual_demand_reduced_to_source_amplification_and_payment_injection_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "firstbreak_source_cut_template_certificate": str(FIRSTBREAK_SOURCE_CUT_CERT.relative_to(ROOT)),
        "endpoint_dynamic_packet_certificate": str(ENDPOINT_DYNAMIC_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_actual_demand_imported": imported,
        "endpoint_unit_incidence_demand_closed": imported,
        "endpoint_unit_demand_not_gap_sufficient": imported,
        "endpoint_no_ap_envelope_recycling_guard": imported,
        "endpoint_actual_demand_reduced_to_source_cut": reduced_closed,
        "endpoint_release_mass_amplification_proved": False,
        "endpoint_low_carrier_payment_injection_proved": False,
        "endpoint_actual_low_carrier_row_incidence_demand_proved": False,
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
        "hardpoint_before_router": ENDPOINT_DEMAND,
        "hardpoint_after_router": REDUCED_DEMAND,
        "old_exits": [ENDPOINT_DEMAND],
        "new_exits": [ENDPOINT_AMPLIFICATION, ENDPOINT_PAYMENT_INJECTION],
        "parallel_open_exits": [
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
        "# Prime Matrix endpoint pivot actual-demand source-cut 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_actual_demand_imported={fmt_bool(cert['endpoint_actual_demand_imported'])}",
        f"endpoint_unit_incidence_demand_closed={fmt_bool(cert['endpoint_unit_incidence_demand_closed'])}",
        f"endpoint_unit_demand_not_gap_sufficient={fmt_bool(cert['endpoint_unit_demand_not_gap_sufficient'])}",
        f"endpoint_no_ap_envelope_recycling_guard={fmt_bool(cert['endpoint_no_ap_envelope_recycling_guard'])}",
        f"endpoint_actual_demand_reduced_to_source_cut={fmt_bool(cert['endpoint_actual_demand_reduced_to_source_cut'])}",
        f"endpoint_release_mass_amplification_proved={fmt_bool(cert['endpoint_release_mass_amplification_proved'])}",
        f"endpoint_low_carrier_payment_injection_proved={fmt_bool(cert['endpoint_low_carrier_payment_injection_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 源侧切口",
        "",
        "上一层已经关闭 endpoint AP exact-envelope。actual demand 因此必须来自 endpoint 源侧单位，而不能从 envelope 饱和反推。",
        "",
        "活跃 fixed-residue demand 至少给出一个 source-tagged endpoint row/cell incidence；但这只是单位下界。单个低 carrier AP cell 的 envelope 已可容纳一个命中，所以单位下界不足以产生容量矛盾。",
        "",
        "## 2. 出口更新",
        "",
        "```text",
        cert["hardpoint_before_router"],
        f"  -> {ENDPOINT_AMPLIFICATION}",
        f"  AND {ENDPOINT_PAYMENT_INJECTION}",
        "```",
        "",
        "- 源侧释放质量放大：必须证明 endpoint 源侧单位沿 orbit 形成足够大的 actual demand；失败时进入 endpoint singleton、full-cycle mean、source-multiplicity 或 sparse SAE。",
        "- 低 carrier 支付注入：放大后的压力必须非循环地注入同一低 carrier AP table；失败时进入 dense-table PDEC、sparse-cell SAE、高秩或 moving-pivot。",
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
            "- 本证书不证明 endpoint actual demand 超过 AP envelope。",
            "- 本证书只排除把单位 incidence 或 envelope 饱和当作 demand gap 的循环路线。",
            "- release-mass amplification 与 low-carrier payment injection 仍未完成。",
            "- endpoint strict gap、dense-table、sparse-cell、高秩、moving-pivot 与并行 endpoint 出口仍未排斥。",
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
