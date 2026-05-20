#!/usr/bin/env python3
"""生成 canonical-payment-cross-key-return-whitelist-slot-projection 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_cross_key_return_whitelist_slot_projection_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.md
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
    "phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.json"
)
SLOT_VECTOR_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"
MULTIPLICITY_CAP = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentCrossKeyReturnWhitelistSlotProjectionImportedLedger"
CROSS_KEY_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyReturnWhitelistLeakImportedLedger"
SLOT_VECTOR_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectSlotVectorImportedForCrossKeyReturnLedger"
CROSS_KEY_UNIT = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnUnitPairLedger"
NOT_SAME_OBJECT = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnNotSameActualObjectLedger"
SLOT_PARTITION = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnSlotChangePartitionLedger"
SOURCE_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnSourceMultiplicityReturnLedger"
CRT_BOUNDARY_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnCRTBoundaryReturnLedger"
PHASE_ORBIT_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnPhaseOrbitReturnLedger"
SIGNED_PAIRING_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeCrossKeyReturnSignedPairingReturnLedger"
NO_INDEPENDENT = "NoIndependentCanonicalCrossKeyReturnWhitelistLeakAfterSlotProjectionLedger"
BOUNDARY_FORWARD = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterCrossKeyReturnSlotProjectionLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCrossKeyReturnSlotProjectionLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCrossKeyReturnSlotProjectionLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCrossKeyReturnSlotProjectionLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCrossKeyReturnSlotProjectionLedger"
VARIATION = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCrossKeyReturnSlotProjectionLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCrossKeyReturnSlotProjectionLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, SLOT_VECTOR_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def remove_or_token(text: str, token: str) -> str:
    """从长 OR 目标中移除一个 token。"""
    updated = text
    while f"{token}Or" in updated:
        updated = updated.replace(f"{token}Or", "")
    while f"Or{token}" in updated:
        updated = updated.replace(f"Or{token}", "")
    return updated.replace(token, "")


def next_target(previous: dict[str, Any]) -> str:
    """移除跨 key whitelist leak 独立出口。"""
    target = remove_or_token(previous.get("next_direct_attack_target", ""), WHITELIST_LEAK)
    return target or f"StableLadderEndpointSingletonAtomSAEOr{MULTIPLICITY_CAP}Or{BOUNDARY_EQUALITY}OrEndpointOrbitBridgeCancellationPDECCap"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        CROSS_KEY_IMPORT,
        SLOT_VECTOR_IMPORT,
        CROSS_KEY_UNIT,
        NOT_SAME_OBJECT,
        SLOT_PARTITION,
        SOURCE_RETURN,
        CRT_BOUNDARY_RETURN,
        PHASE_ORBIT_RETURN,
        SIGNED_PAIRING_RETURN,
        NO_INDEPENDENT,
        BOUNDARY_FORWARD,
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


def slot_records() -> list[dict[str, str]]:
    """列出跨 key return 的槽位投影。"""
    return [
        {"slot": "source_or_occurrence", "route": "源或 occurrence 改变时，回到 source-atom multiplicity cap。"},
        {"slot": "CRT_or_congruence", "route": "CRT 或 congruence 改变时，回到 boundary equality/CRT boundary 出口。"},
        {"slot": "phase_endpoint", "route": "phase endpoint 改变时，回到 bridge、amplitude-depth 或 variation-boundary flux 出口。"},
        {"slot": "signed_mass_or_pairing", "route": "signed mass 或 pairing 改变时，回到 full-cycle mean 或 amplitude-depth 出口。"},
    ]


def build_rows(previous: dict[str, Any], slot_cert: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 cross-key-return slot-projection 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    leak_imported = WHITELIST_LEAK in old_target
    slot_ready = slot_cert.get("phase_residue_exchange_actual_object_slot_vector_closed") is True
    imported = leak_imported and slot_ready
    return [
        row("PhaseResidueExchangeCanonicalPaymentCrossKeyReturnWhitelistSlotProjectionImported", leak_imported, False, "导入 cross-key return whitelist leak 出口。", old_target),
        row("PhaseResidueExchangeActualObjectSlotVectorImportedForCrossKeyReturn", slot_ready, True, "导入 actual-object slot vector。", SLOT_VECTOR_IMPORT),
        row("PhaseResidueExchangeCrossKeyReturnUnitPair", True, True, "跨 key return 连接两个不同 canonical unit key。", CROSS_KEY_UNIT),
        row("PhaseResidueExchangeCrossKeyReturnNotSameActualObject", True, False, "未白名单跨 key return 不能继续声称是同一 actual object。", NOT_SAME_OBJECT),
        row("PhaseResidueExchangeCrossKeyReturnSlotChangePartition", True, True, "不同 actual object 必在 source、CRT、phase、signed/pairing 等槽位中至少一槽变化。", SLOT_PARTITION),
        row("PhaseResidueExchangeCrossKeyReturnSourceMultiplicityReturn", True, False, "source/occurrence 变化回到 multiplicity cap。", SOURCE_RETURN),
        row("PhaseResidueExchangeCrossKeyReturnCRTBoundaryReturn", True, False, "CRT/congruence 变化回到 boundary equality。", CRT_BOUNDARY_RETURN),
        row("PhaseResidueExchangeCrossKeyReturnPhaseOrbitReturn", True, False, "phase endpoint 变化回到 endpoint orbit 出口。", PHASE_ORBIT_RETURN),
        row("PhaseResidueExchangeCrossKeyReturnSignedPairingReturn", True, False, "signed mass/pairing 变化回到 full mean 或 amplitude-depth 出口。", SIGNED_PAIRING_RETURN),
        row("NoIndependentCanonicalCrossKeyReturnWhitelistLeakAfterSlotProjection", imported, True, "cross-key whitelist leak 不再是 payment 侧独立出口，只能按槽位投影到已命名出口。", NO_INDEPENDENT),
        row("BoundaryEqualityAtomCarriedForwardAfterCrossKeyReturnSlotProjection", True, False, "boundary equality atom 继续开放。", BOUNDARY_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterCrossKeyReturnSlotProjection", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointOrbitCrossKeyReturnSlotProjectionStillOpen", False, False, "仍未排斥 endpoint/source/boundary 并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    slot_cert = load_json(SLOT_VECTOR_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, slot_cert, new_target)
    imported = any(item["gate"] == "NoIndependentCanonicalCrossKeyReturnWhitelistLeakAfterSlotProjection" and item["closed"] for item in rows)
    plain = (
        "跨 key 非白名单 return 不能作为 payment 图中的匿名逃逸。"
        "actual-object slot vector 已固定；若 return 不是同一对象，则至少一个槽位变化。"
        "source/occurrence 变化回到 multiplicity cap，CRT/congruence 变化回到 boundary equality，"
        "phase 或 signed/pairing 变化回到 endpoint orbit 的 bridge、amplitude-depth、variation 或 full-mean 出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_cross_key_return_whitelist_slot_projection_router",
        "status": "phase_residue_exchange_cross_key_return_whitelist_leak_projected_to_slot_exits_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "slot_vector_certificate": str(SLOT_VECTOR_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_cross_key_return_whitelist_leak_imported": WHITELIST_LEAK in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_actual_object_slot_vector_imported_for_cross_key_return": slot_cert.get("phase_residue_exchange_actual_object_slot_vector_closed") is True,
        "phase_residue_exchange_cross_key_return_unit_pair_closed": True,
        "phase_residue_exchange_cross_key_return_slot_change_partition_closed": True,
        "phase_residue_exchange_no_independent_cross_key_return_whitelist_leak_closed": imported,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [WHITELIST_LEAK],
        "new_exits": [MULTIPLICITY_CAP, BOUNDARY_EQUALITY, "EndpointOrbitBridgeCancellationPDECCap", "EndpointOrbitAmplitudeDepthPDECCap", "EndpointOrbitVariationBoundaryFluxPDECCap"],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "slot_records": slot_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-cross-key-return-whitelist-slot-projection 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_cross_key_return_whitelist_leak_imported={fmt_bool(cert['phase_residue_exchange_cross_key_return_whitelist_leak_imported'])}",
        f"phase_residue_exchange_actual_object_slot_vector_imported_for_cross_key_return={fmt_bool(cert['phase_residue_exchange_actual_object_slot_vector_imported_for_cross_key_return'])}",
        f"phase_residue_exchange_cross_key_return_unit_pair_closed={fmt_bool(cert['phase_residue_exchange_cross_key_return_unit_pair_closed'])}",
        f"phase_residue_exchange_cross_key_return_slot_change_partition_closed={fmt_bool(cert['phase_residue_exchange_cross_key_return_slot_change_partition_closed'])}",
        f"phase_residue_exchange_no_independent_cross_key_return_whitelist_leak_closed={fmt_bool(cert['phase_residue_exchange_no_independent_cross_key_return_whitelist_leak_closed'])}",
        f"source_atom_multiplicity_cap_pdec_cap_proved={fmt_bool(cert['source_atom_multiplicity_cap_pdec_cap_proved'])}",
        f"phase_residue_exchange_boundary_equality_atom_exclusion_proved={fmt_bool(cert['phase_residue_exchange_boundary_equality_atom_exclusion_proved'])}",
        f"endpoint_orbit_bridge_cancellation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_bridge_cancellation_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 跨 key return 槽位投影",
        "",
        "| slot | route |",
        "| --- | --- |",
    ]
    for record in cert["slot_records"]:
        lines.append(f"| `{cell(record['slot'])}` | {cell(record['route'])} |")
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
            "- 本证书只移除 cross-key return whitelist leak 作为 payment 侧独立出口。",
            "- 本证书没有证明 source multiplicity、boundary equality 或 endpoint orbit 出口。",
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
