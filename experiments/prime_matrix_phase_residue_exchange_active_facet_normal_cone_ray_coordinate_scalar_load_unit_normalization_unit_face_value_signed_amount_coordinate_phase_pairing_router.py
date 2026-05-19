#!/usr/bin/env python3
"""生成 phase-residue exchange phase-pairing 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.md
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
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.json"
)

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValue"
    "SignedAmountCoordinateCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValue"
    "SignedAmountCoordinatePhasePairingCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangePhasePairingLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangePhasePairingLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangePhasePairingLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangePhasePairingLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangePhasePairingLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangePhasePairingLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangePhasePairingLedger"

SIGNED_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateImportedForPhasePairingLedger"
UNIT_GAP = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingUnitGapLedger"
POSITIVE_PHASE = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingPositiveEndpointLedger"
NEGATIVE_PHASE = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingNegativeEndpointLedger"
SIGNED_PAIRING = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingSignedMassValueLedger"
AMOUNT_MATCH = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingEqualsAmountLedger"
HALF_L1_MATCH = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingEqualsHalfL1Ledger"
PAYMENT_MATCH = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingEqualsPaymentValueLedger"
OFFSET_CANCEL = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingConstantOffsetCancelsLedger"
NO_PHASE_RESCALE = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingNoPhaseRescaleLedger"
NO_SIGN_MISMATCH = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingNoSignMismatchLedger"
SUPPORT_LOCK = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingTwoEndpointSupportLockedLedger"
PAIRING_PAYMENT = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingPDECCapReducedToCalibratedPairingLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingCollisionOrZeroExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingOrientationLedger"
NO_SIGNED_MASS_BLACKBOX = "StableLadderEndpointOrbitPhaseResidueNoAnonymousSignedAmountAfterPhasePairingLedger"
PHASE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangePhasePairingPacketLedger"
NO_ANON = "NoAnonymousPhasePairingAfterSignedAmountCoordinateLedger"


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
    """登记本脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def next_target(previous: dict[str, Any]) -> str:
    """把 signed-amount-coordinate 硬点替换为 phase-pairing 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        SIGNED_IMPORT,
        UNIT_GAP,
        POSITIVE_PHASE,
        NEGATIVE_PHASE,
        SIGNED_PAIRING,
        AMOUNT_MATCH,
        HALF_L1_MATCH,
        PAYMENT_MATCH,
        OFFSET_CANCEL,
        NO_PHASE_RESCALE,
        NO_SIGN_MISMATCH,
        SUPPORT_LOCK,
        PAIRING_PAYMENT,
        COLLISION_EXIT,
        ORIENTATION,
        NO_SIGNED_MASS_BLACKBOX,
        PHASE_PACKET,
        NO_ANON,
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


def phase_pairing_records() -> list[dict[str, str]]:
    """给出 phase-pairing 字段。"""
    return [
        {
            "field": "unit_phase_gap",
            "meaning": "由 <delta_{r0}-delta_{r*},phi>=1 得到 phi(r0)-phi(r*)=1。",
        },
        {
            "field": "positive_endpoint_phase",
            "meaning": "正端点贡献为 A phi(r0)。",
        },
        {
            "field": "negative_endpoint_phase",
            "meaning": "负端点贡献为 A phi(r*)。",
        },
        {
            "field": "signed_pairing_value",
            "meaning": "<W,phi>=A(phi(r0)-phi(r*))=A。",
        },
        {
            "field": "amount_capacity_match",
            "meaning": "phase pairing、amount、payment value 与 ||W||_1/2 都等于 A。",
        },
        {
            "field": "constant_offset_cancels",
            "meaning": "W 的净质量为 0，因此 phi 加常数不改变配对。",
        },
        {
            "field": "no_phase_rescale",
            "meaning": "单位相位差固定为 1，不存在额外相位重标定。",
        },
        {
            "field": "no_sign_mismatch",
            "meaning": "正端点 r0 与负端点 r* 的方向由 C_Pi 固定。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 phase-pairing 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    rows = [
        row(
            "PhaseResidueExchangeSignedAmountCoordinateImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange signed-amount-coordinate circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row("MultiplicityCapCarriedForwardAfterExchangePhasePairing", True, False, "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。", MULTIPLICITY_CAP),
        row("EndpointSingletonAtomSAECarriedForwardAfterExchangePhasePairing", True, False, "同点退化或零负载时仍回流 singleton atom/SAE。", SINGLETON),
        row("EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangePhasePairing", True, False, "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。", FULL_MEAN),
        row("EndpointOrbitBridgeCancellationCarriedForwardAfterExchangePhasePairing", True, False, "反号债或镜像互付继续由 bridge-cancellation 出口承接。", BRIDGE),
        row("EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangePhasePairing", True, False, "同号跨尺度堆高继续由 amplitude-depth 出口承接。", AMPLITUDE_DEPTH),
        row("EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangePhasePairing", True, False, "边界迁移继续由 variation-boundary flux 出口承接。", BOUNDARY),
        row("PhaseResidueExchangeSignedAmountCoordinateImportedForPhasePairing", True, True, "导入 W=A(delta_{r0}-delta_{r*})、||W||_1/2=A 与 price-one amount=A。", SIGNED_IMPORT),
        row("PhaseResidueExchangePhasePairingUnitGap", True, True, "单位相位差为 phi(r0)-phi(r*)=1。", UNIT_GAP),
        row("PhaseResidueExchangePhasePairingPositiveEndpoint", True, True, "正端点相位贡献为 A phi(r0)。", POSITIVE_PHASE),
        row("PhaseResidueExchangePhasePairingNegativeEndpoint", True, True, "负端点相位贡献为 A phi(r*)。", NEGATIVE_PHASE),
        row("PhaseResidueExchangePhasePairingSignedMassValue", True, True, "有符号质量的相位配对为 <W,phi>=A(phi(r0)-phi(r*))=A。", SIGNED_PAIRING),
        row("PhaseResidueExchangePhasePairingEqualsAmount", True, True, "相位配对值等于唯一 amount 坐标 A。", AMOUNT_MATCH),
        row("PhaseResidueExchangePhasePairingEqualsHalfL1", True, True, "相位配对值等于 ||W||_1/2。", HALF_L1_MATCH),
        row("PhaseResidueExchangePhasePairingEqualsPaymentValue", True, True, "相位配对值等于 payment_value=A。", PAYMENT_MATCH),
        row("PhaseResidueExchangePhasePairingConstantOffsetCancels", True, True, "W 的净质量为 0，phi 的常数偏移在配对中抵消。", OFFSET_CANCEL),
        row("PhaseResidueExchangePhasePairingNoPhaseRescale", True, True, "单位相位差已经固定为 1，不存在隐藏相位重标定。", NO_PHASE_RESCALE),
        row("PhaseResidueExchangePhasePairingNoSignMismatch", True, True, "正负端点与 C_Pi 的方向一致，不存在符号错配出口。", NO_SIGN_MISMATCH),
        row("PhaseResidueExchangePhasePairingTwoEndpointSupportLocked", True, True, "相位配对只读取 r0 与 r* 两个端点。", SUPPORT_LOCK),
        row("PhaseResidueExchangePhasePairingPDECCapReducedToCalibratedPairing", True, True, "若已有出口不支付，PDEC/cap 的待支付对象是校准相位配对 A。", PAIRING_PAYMENT),
        row("PhaseResidueExchangePhasePairingCollisionOrZeroExit", True, True, "若 r0=r* 或 A=0，则相位配对退化并回流 singleton/degenerate 出口。", COLLISION_EXIT),
        row("PhaseResidueExchangePhasePairingOrientation", True, True, "相位差按 r* -> r0 的既定方向读取。", ORIENTATION),
        row("PhaseResidueNoAnonymousSignedAmountAfterPhasePairing", True, True, "signed amount coordinate 被校准相位配对替代，不再有匿名相位读数。", NO_SIGNED_MASS_BLACKBOX),
        row("PhaseResidueExchangePhasePairingPacket", True, False, "若已有出口不支付，剩余就是 phase-pairing circuit PDEC/cap。", PHASE_PACKET),
        row("NoAnonymousPhasePairingAfterSignedAmountCoordinate", True, True, "相位、容量、变差三个读数都固定为同一 A。", NO_ANON),
        row("SparseScaleLadderSAECarriedForwardAfterExchangePhasePairing", True, False, "sparse scale-ladder SAE 继续前传；本步不证明全局求和。", SPARSE),
        row("EndpointOrbitPhaseResidueExchangePhasePairingStillOpen", False, False, "仍未排斥 singleton、full-cycle mean、multiplicity cap、phase-pairing、bridge、amplitude、boundary 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合；最新硬点为 phase-pairing circuit 或并行出口。", new_target),
    ]
    return rows


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    plain = (
        "phase-residue exchange signed-amount-coordinate 已把非退化剩余写成 "
        "W=A(delta_{r0}-delta_{r*})、||W||_1/2=A。本步把相位读数也锁定："
        "phi(r0)-phi(r*)=1 且 <W,phi>=A(phi(r0)-phi(r*))=A。于是 amount、"
        "payment value、half-L1 与 phase pairing 都是同一个 A；常数相位偏移、"
        "相位重标定和正负端点符号错配不再是可用出口。若 r0=r* 或 A=0 则回流 "
        "singleton/degenerate 出口，否则只能表现为 phase-pairing circuit PDEC/cap "
        "或已有出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_router",
        "status": "phase_residue_exchange_signed_amount_coordinate_reduced_to_phase_pairing_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_signed_amount_coordinate_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_phase_pairing_unit_gap_closed": True,
        "phase_residue_exchange_phase_pairing_positive_endpoint_closed": True,
        "phase_residue_exchange_phase_pairing_negative_endpoint_closed": True,
        "phase_residue_exchange_phase_pairing_signed_mass_value_closed": True,
        "phase_residue_exchange_phase_pairing_equals_amount_closed": True,
        "phase_residue_exchange_phase_pairing_equals_half_l1_closed": True,
        "phase_residue_exchange_phase_pairing_equals_payment_value_closed": True,
        "phase_residue_exchange_phase_pairing_constant_offset_cancels_closed": True,
        "phase_residue_exchange_phase_pairing_no_phase_rescale_closed": True,
        "phase_residue_exchange_phase_pairing_no_sign_mismatch_closed": True,
        "phase_residue_exchange_phase_pairing_pdec_cap_reduced_to_calibrated_pairing_closed": True,
        "phase_residue_no_anonymous_signed_amount_after_phase_pairing_closed": True,
        "anonymous_phase_pairing_removed_after_signed_amount_coordinate": True,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_pdec_cap_proved": False,
        "linear_witness_existence_proved": False,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_carried_forward": True,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_carried_forward": True,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "phase_pairing_records": phase_pairing_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix phase-residue exchange phase-pairing 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_signed_amount_coordinate_imported={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_imported'])}",
        f"phase_residue_exchange_phase_pairing_unit_gap_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_unit_gap_closed'])}",
        f"phase_residue_exchange_phase_pairing_signed_mass_value_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_signed_mass_value_closed'])}",
        f"phase_residue_exchange_phase_pairing_equals_amount_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_equals_amount_closed'])}",
        f"phase_residue_exchange_phase_pairing_equals_half_l1_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_equals_half_l1_closed'])}",
        f"phase_residue_exchange_phase_pairing_equals_payment_value_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_equals_payment_value_closed'])}",
        f"phase_residue_exchange_phase_pairing_no_phase_rescale_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_no_phase_rescale_closed'])}",
        f"phase_residue_exchange_phase_pairing_no_sign_mismatch_closed={fmt_bool(cert['phase_residue_exchange_phase_pairing_no_sign_mismatch_closed'])}",
        "linear_witness_existence_proved=false",
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_pdec_cap_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. signed-amount-coordinate 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "A>0",
        "positive_endpoint_atom=A delta_{r0}",
        "negative_endpoint_atom=A delta_{r*}",
        "signed_mass=W=A(delta_{r0}-delta_{r*})=A C_Pi",
        "positive_mass=A",
        "negative_mass=A",
        "net_mass=0",
        "||W||_1=2A",
        "||W||_1/2=A",
        "support={r0,r*}",
        "amount_slot_split=0",
        "orientation_flip=0",
        "anonymous_amount_pool=0",
        "```",
        "",
        "## 2. phase-pairing 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["phase_pairing_records"]:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "非退化时 phase-pairing 证书为：",
        "",
        "```text",
        "phi(r0)-phi(r*)=1",
        "positive_phase_contribution=A phi(r0)",
        "negative_phase_contribution=A phi(r*)",
        "<W,phi>=A(phi(r0)-phi(r*))=A",
        "phase_pairing_value=A",
        "amount=A",
        "payment_value=A",
        "||W||_1/2=A",
        "constant_offset_cancelled=true",
        "phase_rescale=0",
        "sign_mismatch=0",
        "phase_pairing_support={r0,r*}",
        "```",
        "",
        "若 `r0=r*` 或 `A=0`，则相位配对退化并回流 singleton/degenerate 出口。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["previous_direct_attack_target"],
        "  -> " + reduced_target(cert["next_direct_attack_target"]).replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines += [
        "",
        "## 5. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 6. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 phase-residue exchange active-facet normal-cone ray-coordinate scalar-load unit-normalization unit-face-value signed-amount-coordinate phase-pairing circuit PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 本证书没有证明线性相位/容量见证本身存在。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 7. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
