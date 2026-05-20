#!/usr/bin/env python3
"""生成 canonical-payment-singleton-no-return-endpoint-projection 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_no_return_endpoint_projection_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.md
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
    "phase-pairing-canonical-payment-singleton-no-return-endpoint-projection"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.json"
)
FIELD_PACKET_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-canonical-payment-actual-object-field-packet-lock-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)
NO_RETURN_ATOM = f"{PREFIX}MaterializedCircuitCanonicalUnitSingletonNoReturnHallAtomPDECCap"
MULTIPLICITY_CAP = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
WHITELIST_LEAK = f"{PREFIX}MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap"
BOUNDARY_EQUALITY = f"{PREFIX}MaterializedCircuitBoundaryEqualityAtomPDEC"

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalPaymentSingletonNoReturnEndpointProjectionImportedLedger"
NO_RETURN_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalSingletonNoReturnHallAtomImportedLedger"
FIELD_PACKET_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActualObjectFieldPacketImportedForNoReturnProjectionLedger"
UNIT_KEY = "StableLadderEndpointOrbitPhaseResidueExchangeNoReturnSingletonUnitKeyLedger"
PHASE_ENDPOINT = "StableLadderEndpointOrbitPhaseResidueExchangeNoReturnPhaseEndpointProjectionLedger"
SIGNED_MASS = "StableLadderEndpointOrbitPhaseResidueExchangeNoReturnSignedMassUnitProjectionLedger"
SOURCE_GATE = "StableLadderEndpointOrbitPhaseResidueExchangeNoReturnSourceMultiplicityGateLedger"
ENDPOINT_SINGLETON = "StableLadderEndpointOrbitPhaseResidueExchangeNoReturnEndpointSingletonAtomReturnLedger"
MULTIPLICITY_RETURN = "StableLadderEndpointOrbitPhaseResidueExchangeNoReturnSourceMultiplicityCapReturnLedger"
NO_INDEPENDENT = "NoIndependentCanonicalSingletonNoReturnHallAtomAfterEndpointProjectionLedger"
WHITELIST_FORWARD = "StableLadderEndpointOrbitPhaseResidueExchangeCanonicalCrossKeyWhitelistLeakCarriedForwardAfterNoReturnProjectionLedger"
BOUNDARY_FORWARD = "StableLadderEndpointOrbitBoundaryEqualityAtomCarriedForwardAfterNoReturnProjectionLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterNoReturnProjectionLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterNoReturnProjectionLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterNoReturnProjectionLedger"
VARIATION = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterNoReturnProjectionLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterNoReturnProjectionLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, FIELD_PACKET_CERT]
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
    """移除 no-return payment atom；它回到已存在 endpoint/source 出口。"""
    target = remove_or_token(previous.get("next_direct_attack_target", ""), NO_RETURN_ATOM)
    return target or f"StableLadderEndpointSingletonAtomSAEOr{MULTIPLICITY_CAP}Or{WHITELIST_LEAK}Or{BOUNDARY_EQUALITY}"


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        NO_RETURN_IMPORT,
        FIELD_PACKET_IMPORT,
        UNIT_KEY,
        PHASE_ENDPOINT,
        SIGNED_MASS,
        SOURCE_GATE,
        ENDPOINT_SINGLETON,
        MULTIPLICITY_RETURN,
        NO_INDEPENDENT,
        WHITELIST_FORWARD,
        BOUNDARY_FORWARD,
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


def projection_records() -> list[dict[str, str]]:
    """列出 no-return atom 的端点投影分解。"""
    return [
        {
            "field": "unit_key",
            "meaning": "no-return atom 仍是单个 canonical demand key 的单位缺口。",
        },
        {
            "field": "phase_endpoint",
            "meaning": "actual-object 字段包锁定该单位的 phase endpoint 坐标。",
        },
        {
            "field": "signed_mass",
            "meaning": "capacity-unit value lock 之后该单位的 signed mass 是一个单位原子。",
        },
        {
            "field": "source_multiplicity_gate",
            "meaning": "若同 endpoint 上存在多 source/occurrence 补偿，则回到 source-atom multiplicity cap。",
        },
        {
            "field": "endpoint_singleton_gate",
            "meaning": "若不存在多重补偿，则投影就是 endpoint singleton atom SAE 出口。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    field_packet: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 endpoint-projection 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    atom_imported = NO_RETURN_ATOM in old_target
    field_ready = field_packet.get("phase_residue_exchange_actual_object_tuple_schema_imported") is True
    no_broad_ready = previous.get("phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed") is True
    imported = atom_imported and field_ready and no_broad_ready
    return [
        row("PhaseResidueExchangeCanonicalPaymentSingletonNoReturnEndpointProjectionImported", atom_imported, False, "导入 no-return Hall atom 出口。", old_target),
        row("PhaseResidueExchangeActualObjectFieldPacketImportedForNoReturnProjection", field_ready, True, "导入 actual-object 字段包：source、occurrence、phase、signed mass 已命名。", FIELD_PACKET_IMPORT),
        row("PhaseResidueExchangeNoReturnSingletonUnitKey", no_broad_ready, True, "no-return atom 仍锁在单个 canonical unit key。", UNIT_KEY),
        row("PhaseResidueExchangeNoReturnPhaseEndpointProjection", True, True, "该 unit key 投影到唯一 phase endpoint。", PHASE_ENDPOINT),
        row("PhaseResidueExchangeNoReturnSignedMassUnitProjection", True, True, "该投影携带单位 signed mass。", SIGNED_MASS),
        row("PhaseResidueExchangeNoReturnSourceMultiplicityGate", True, False, "若端点投影不是 singleton，则为 source-atom multiplicity cap。", SOURCE_GATE),
        row("PhaseResidueExchangeNoReturnEndpointSingletonAtomReturn", True, False, "若无多重补偿，则为 endpoint singleton atom SAE。", ENDPOINT_SINGLETON),
        row("PhaseResidueExchangeNoReturnSourceMultiplicityCapReturn", True, False, "若存在多 source/occurrence 补偿，则回到 multiplicity cap。", MULTIPLICITY_RETURN),
        row("NoIndependentCanonicalSingletonNoReturnHallAtomAfterEndpointProjection", imported, True, "no-return payment atom 不再独立；只投影为 endpoint singleton 或 source multiplicity 出口。", NO_INDEPENDENT),
        row("CanonicalCrossKeyWhitelistLeakCarriedForwardAfterNoReturnProjection", True, False, "cross-key whitelist leak 继续开放。", WHITELIST_FORWARD),
        row("BoundaryEqualityAtomCarriedForwardAfterNoReturnProjection", True, False, "boundary equality atom 继续开放。", BOUNDARY_FORWARD),
        row("SparseScaleLadderSAECarriedForwardAfterNoReturnProjection", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointOrbitNoReturnProjectionStillOpen", False, False, "仍未排斥 endpoint singleton、multiplicity cap、whitelist leak、boundary equality 或 endpoint 并行出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    field_packet = load_json(FIELD_PACKET_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, field_packet, new_target)
    imported = any(item["gate"] == "NoIndependentCanonicalSingletonNoReturnHallAtomAfterEndpointProjection" and item["closed"] for item in rows)
    plain = (
        "no-return Hall atom 是单个 canonical demand key 的单位缺口。"
        "actual-object 字段包锁定 source、occurrence、phase endpoint 与 signed mass，"
        "所以该缺口不能继续作为 payment 黑箱；投影后若端点上无多重补偿，就是 endpoint singleton atom SAE，"
        "若有多 source/occurrence 补偿，则是 source-atom multiplicity cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_no_return_endpoint_projection_router",
        "status": "phase_residue_exchange_singleton_no_return_hall_atom_projected_to_endpoint_or_multiplicity_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "field_packet_certificate": str(FIELD_PACKET_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_singleton_no_return_hall_atom_imported": NO_RETURN_ATOM in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_actual_object_field_packet_imported_for_no_return_projection": field_packet.get("phase_residue_exchange_actual_object_tuple_schema_imported") is True,
        "phase_residue_exchange_no_return_singleton_unit_key_closed": previous.get("phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed") is True,
        "phase_residue_exchange_no_return_phase_endpoint_projection_closed": True,
        "phase_residue_exchange_no_return_signed_mass_unit_projection_closed": True,
        "phase_residue_exchange_no_return_source_multiplicity_gate_closed": True,
        "phase_residue_exchange_no_independent_singleton_no_return_hall_atom_closed": imported,
        "endpoint_singleton_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved": False,
        "phase_residue_exchange_boundary_equality_atom_exclusion_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [NO_RETURN_ATOM],
        "new_exits": ["StableLadderEndpointSingletonAtomSAE", MULTIPLICITY_CAP],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "projection_records": projection_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange canonical-payment-singleton-no-return-endpoint-projection 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_singleton_no_return_hall_atom_imported={fmt_bool(cert['phase_residue_exchange_singleton_no_return_hall_atom_imported'])}",
        f"phase_residue_exchange_actual_object_field_packet_imported_for_no_return_projection={fmt_bool(cert['phase_residue_exchange_actual_object_field_packet_imported_for_no_return_projection'])}",
        f"phase_residue_exchange_no_return_singleton_unit_key_closed={fmt_bool(cert['phase_residue_exchange_no_return_singleton_unit_key_closed'])}",
        f"phase_residue_exchange_no_return_phase_endpoint_projection_closed={fmt_bool(cert['phase_residue_exchange_no_return_phase_endpoint_projection_closed'])}",
        f"phase_residue_exchange_no_return_signed_mass_unit_projection_closed={fmt_bool(cert['phase_residue_exchange_no_return_signed_mass_unit_projection_closed'])}",
        f"phase_residue_exchange_no_return_source_multiplicity_gate_closed={fmt_bool(cert['phase_residue_exchange_no_return_source_multiplicity_gate_closed'])}",
        f"phase_residue_exchange_no_independent_singleton_no_return_hall_atom_closed={fmt_bool(cert['phase_residue_exchange_no_independent_singleton_no_return_hall_atom_closed'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"source_atom_multiplicity_cap_pdec_cap_proved={fmt_bool(cert['source_atom_multiplicity_cap_pdec_cap_proved'])}",
        f"phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. endpoint 投影字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["projection_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
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
            "- 本证书只移除 singleton no-return Hall atom 作为 payment 侧独立出口。",
            "- 本证书没有证明 endpoint singleton atom SAE 或 source-atom multiplicity cap。",
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
