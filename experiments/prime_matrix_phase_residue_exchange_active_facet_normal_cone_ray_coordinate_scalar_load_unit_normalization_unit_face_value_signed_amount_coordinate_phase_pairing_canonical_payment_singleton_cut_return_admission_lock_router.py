#!/usr/bin/env python3
"""生成 canonical-payment-singleton-cut-return-admission-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_cut_return_admission_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.md
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
    "phase-pairing-canonical-payment-singleton-cut-return-admission-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.json"
)
SINGLETON_CUT_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-unit-payment-singleton-cut-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
SINGLETON_HALL = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap"
NO_RETURN_ATOM = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonNoReturnHallAtomPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonCutReturnAdmissionLockImportedLedger"
ACTUAL_ADMISSION_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectAdmissionTrichotomyImportedForSingletonReturnLedger"
SINGLETON_CUT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonCutRouterImportedForReturnAdmissionLedger"
SINGLETON_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonCutBalanceImportedForReturnAdmissionLedger"
SAME_KEY_EMPTY = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonSameKeyCapacityEmptyImportedLedger"
RETURN_PARTITION = "StableLadderEndpointOrbitPhaseResidueExchangeSingletonReturnAdmissionPartitionLedger"
SAME_KEY_NO_NEW = "StableLadderEndpointOrbitPhaseResidueExchangeSingletonSameKeyReturnNoNewCapacityLedger"
CROSS_KEY_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeSingletonCrossKeyReturnWhitelistGateLedger"
LEGAL_RETURN_BOUNDARY = "StableLadderEndpointOrbitPhaseResidueExchangeSingletonLegalReturnNamedBoundaryLedger"
NO_RETURN_REGISTER = "StableLadderEndpointOrbitPhaseResidueExchangeSingletonNoReturnHallAtomRegistrationLedger"
NO_BROAD = "NoIndependentBroadCanonicalSingletonHallCutAfterReturnAdmissionLockLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterSingletonReturnAdmissionLedger"
BOUNDARY_FORWARD = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterSingletonReturnAdmissionLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterSingletonReturnAdmissionLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingletonReturnAdmissionLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingletonReturnAdmissionLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterSingletonReturnAdmissionLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterSingletonReturnAdmissionLedger"
VARIATION = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterSingletonReturnAdmissionLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterSingletonReturnAdmissionLedger"


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
    """登记本脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, SINGLETON_CUT_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def next_target(previous: dict[str, Any]) -> str:
    """把宽泛 singleton Hall cut 出口替换为 no-return atom。"""
    target = previous.get("next_direct_attack_target", "")
    if SINGLETON_HALL in target:
        return target.replace(SINGLETON_HALL, NO_RETURN_ATOM)
    return f"{NO_RETURN_ATOM}Or{WHITELIST_LEAK}Or{BOUNDARY_EQUALITY}"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        ACTUAL_ADMISSION_IMPORT,
        SINGLETON_CUT_IMPORT,
        SINGLETON_BALANCE,
        SAME_KEY_EMPTY,
        RETURN_PARTITION,
        SAME_KEY_NO_NEW,
        CROSS_KEY_GATE,
        LEGAL_RETURN_BOUNDARY,
        NO_RETURN_REGISTER,
        NO_BROAD,
        WHITELIST_FORWARD,
        BOUNDARY_FORWARD,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        VARIATION,
        SPARSE,
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


def return_records() -> list[dict[str, str]]:
    """列出单点 cut 的 return/admission 分解。"""
    return [
        {
            "case": "same_key_capacity_edge",
            "route": "旧 singleton-cut 证书给出同 key capacity edge 为空；若出现同 key 重复，只是 duplicate，不增加容量。",
        },
        {
            "case": "bad_actual_object_edge",
            "route": "actual-object admission trichotomy 已把缺对象、换槽、重对象边排除为独立 capacity。",
        },
        {
            "case": "cross_key_return",
            "route": "跨 key return 必须命名并通过 whitelist；否则就是 CanonicalCrossKeyReturnWhitelistLeak。",
        },
        {
            "case": "named_boundary_return",
            "route": "合法命名 return 只能落入已开放的 boundary equality/endpoint return 边界。",
        },
        {
            "case": "no_legal_return",
            "route": "无同 key 容量、无坏对象边、无合法命名 return 时，宽泛 singleton cut 缩为 NoReturnHallAtom。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    singleton_cut: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 singleton-cut-return-admission-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    singleton_present = SINGLETON_HALL in old_target
    admission_ready = previous.get("phase_residue_exchange_no_independent_actual_object_admission_defect_closed") is True
    cut_ready = all(
        singleton_cut.get(key) is True
        for key in [
            "phase_residue_exchange_singleton_cut_demand_one_closed",
            "phase_residue_exchange_singleton_cut_capacity_zero_closed",
            "phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed",
            "phase_residue_exchange_cross_key_collision_trichotomy_closed",
        ]
    )
    imported = singleton_present and admission_ready and cut_ready
    return [
        row("PhaseResidueExchangeCanonicalPaymentSingletonCutReturnAdmissionLockImported", singleton_present, False, "导入当前 broad singleton Hall cut 出口。", old_target),
        row("PhaseResidueExchangeActualObjectAdmissionTrichotomyImportedForSingletonReturn", admission_ready, True, "导入对象 admission 三分支，坏对象边不再形成独立 capacity。", ACTUAL_ADMISSION_IMPORT),
        row("PhaseResidueExchangeCanonicalSingletonCutRouterImportedForReturnAdmission", cut_ready, True, "导入旧 singleton-cut 证书的 demand/capacity/cross-key 三分法。", SINGLETON_CUT_IMPORT),
        row("PhaseResidueExchangeCanonicalSingletonCutBalanceImportedForReturnAdmission", bool(singleton_cut.get("phase_residue_exchange_singleton_cut_balance_closed")), True, "单点 cut 余额仍为 I_A(k)-I_C(k)=1。", SINGLETON_BALANCE),
        row("PhaseResidueExchangeCanonicalSingletonSameKeyCapacityEmptyImported", bool(singleton_cut.get("phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed")), True, "同 key capacity edge 为空。", SAME_KEY_EMPTY),
        row("PhaseResidueExchangeSingletonReturnAdmissionPartition", True, True, "所有补偿尝试分为同 key、坏对象、跨 key、命名边界、无 return。", RETURN_PARTITION),
        row("PhaseResidueExchangeSingletonSameKeyReturnNoNewCapacity", True, True, "同 key 重复不增加 capacity；同 key 真 capacity 已由 cut capacity zero 排除。", SAME_KEY_NO_NEW),
        row("PhaseResidueExchangeSingletonCrossKeyReturnWhitelistGate", True, False, "跨 key return 若未进入白名单，直接成为 whitelist leak。", CROSS_KEY_GATE),
        row("PhaseResidueExchangeSingletonLegalReturnNamedBoundary", True, False, "合法命名 return 必须落入 boundary/endpoint 开放边界。", LEGAL_RETURN_BOUNDARY),
        row("PhaseResidueExchangeSingletonNoReturnHallAtomRegistration", imported, False, "无合法 return 时登记更窄的 no-return Hall atom。", NO_RETURN_REGISTER),
        row("NoIndependentBroadCanonicalSingletonHallCutAfterReturnAdmissionLock", imported, True, "宽泛 singleton Hall cut 不再作为独立出口，只剩 no-return atom 或已命名 return 出口。", NO_BROAD),
        row("CanonicalCrossKeyWhitelistLeakCarriedForwardAfterSingletonReturnAdmission", True, False, "cross-key whitelist leak 继续开放。", WHITELIST_FORWARD),
        row("BoundaryEqualityAtomCarriedForwardAfterSingletonReturnAdmission", True, False, "boundary equality atom 继续开放。", BOUNDARY_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterSingletonReturnAdmission", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointOrbitSingletonReturnAdmissionLockStillOpen", False, False, "仍未排斥 no-return Hall atom、whitelist leak、boundary equality 或 endpoint 并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    singleton_cut = load_json(SINGLETON_CUT_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, singleton_cut, new_target)
    imported = any(item["gate"] == "NoIndependentBroadCanonicalSingletonHallCutAfterReturnAdmissionLock" and item["closed"] for item in rows)
    plain = (
        "actual-object admission 已排除坏对象边，旧 singleton-cut 证书给出同 key 容量为空且余额为 1。"
        "因此 broad singleton Hall cut 的所有补偿尝试只能分为：同 key 重复不增容、跨 key 未白名单泄漏、"
        "命名 boundary/endpoint return，或完全无合法 return。"
        "本步把 broad singleton cut 改写为更窄的 no-return Hall atom，同时保留 whitelist、boundary 与 endpoint 出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_cut_return_admission_lock_router",
        "status": "phase_residue_exchange_broad_singleton_hall_cut_reduced_to_no_return_atom_or_named_return_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "singleton_cut_certificate": str(SINGLETON_CUT_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_singleton_hall_cut_defect_imported": SINGLETON_HALL in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_actual_object_admission_trichotomy_imported": previous.get("phase_residue_exchange_no_independent_actual_object_admission_defect_closed") is True,
        "phase_residue_exchange_singleton_cut_router_imported": singleton_cut.get("phase_residue_exchange_no_anonymous_payment_conservation_defect_closed") is True,
        "phase_residue_exchange_singleton_cut_balance_imported": singleton_cut.get("phase_residue_exchange_singleton_cut_balance_closed") is True,
        "phase_residue_exchange_same_key_capacity_empty_imported": singleton_cut.get("phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed") is True,
        "phase_residue_exchange_singleton_return_admission_partition_closed": True,
        "phase_residue_exchange_same_key_return_no_new_capacity_closed": True,
        "phase_residue_exchange_cross_key_return_whitelist_gate_closed": True,
        "phase_residue_exchange_legal_return_named_boundary_registered": True,
        "phase_residue_exchange_singleton_no_return_hall_atom_registered": imported,
        "phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed": imported,
        "phase_residue_exchange_canonical_singleton_no_return_hall_atom_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [SINGLETON_HALL],
        "new_exits": [NO_RETURN_ATOM, WHITELIST_LEAK, BOUNDARY_EQUALITY],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "return_records": return_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-singleton-cut-return-admission-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_singleton_hall_cut_defect_imported={fmt_bool(cert['phase_residue_exchange_singleton_hall_cut_defect_imported'])}",
        f"phase_residue_exchange_actual_object_admission_trichotomy_imported={fmt_bool(cert['phase_residue_exchange_actual_object_admission_trichotomy_imported'])}",
        f"phase_residue_exchange_singleton_cut_router_imported={fmt_bool(cert['phase_residue_exchange_singleton_cut_router_imported'])}",
        f"phase_residue_exchange_singleton_cut_balance_imported={fmt_bool(cert['phase_residue_exchange_singleton_cut_balance_imported'])}",
        f"phase_residue_exchange_same_key_capacity_empty_imported={fmt_bool(cert['phase_residue_exchange_same_key_capacity_empty_imported'])}",
        f"phase_residue_exchange_singleton_return_admission_partition_closed={fmt_bool(cert['phase_residue_exchange_singleton_return_admission_partition_closed'])}",
        f"phase_residue_exchange_same_key_return_no_new_capacity_closed={fmt_bool(cert['phase_residue_exchange_same_key_return_no_new_capacity_closed'])}",
        f"phase_residue_exchange_cross_key_return_whitelist_gate_closed={fmt_bool(cert['phase_residue_exchange_cross_key_return_whitelist_gate_closed'])}",
        f"phase_residue_exchange_legal_return_named_boundary_registered={fmt_bool(cert['phase_residue_exchange_legal_return_named_boundary_registered'])}",
        f"phase_residue_exchange_singleton_no_return_hall_atom_registered={fmt_bool(cert['phase_residue_exchange_singleton_no_return_hall_atom_registered'])}",
        f"phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed={fmt_bool(cert['phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed'])}",
        f"phase_residue_exchange_canonical_singleton_no_return_hall_atom_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_singleton_no_return_hall_atom_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. return/admission 分解",
        "",
        "| case | route |",
        "| --- | --- |",
    ]
    for record in cert["return_records"]:
        lines.append(f"| `{cell(record['case'])}` | {cell(record['route'])} |")
    lines.extend(
        [
            "",
            "## 2. 新硬点",
            "",
            "```text",
            cert["previous_direct_attack_target"],
            "  -> " + reduced_target(cert["next_direct_attack_target"]),
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
            "- 本证书只把 broad singleton Hall cut 改写为更窄的 no-return Hall atom 或已命名 return 出口。",
            "- 本证书没有证明 no-return Hall atom 不存在。",
            "- 本证书没有证明 cross-key whitelist leak、boundary equality atom 或 endpoint 并行出口。",
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
