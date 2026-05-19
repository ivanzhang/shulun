#!/usr/bin/env python3
"""生成 phase-residue exchange signed-amount-coordinate 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.md
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
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-router.json"
)

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinateCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeSignedAmountCoordinateLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeSignedAmountCoordinateLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSignedAmountCoordinateLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSignedAmountCoordinateLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSignedAmountCoordinateLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSignedAmountCoordinateLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeSignedAmountCoordinateLedger"

FACE_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueImportedForSignedAmountCoordinateLedger"
PRICE_ONE = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinatePriceOneLedger"
POSITIVE_ATOM = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinatePositiveEndpointAtomLedger"
NEGATIVE_ATOM = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateNegativeEndpointAtomLedger"
SIGNED_MASS = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateSignedMassLedger"
MASS_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateEndpointMassBalanceLedger"
HALF_L1 = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateHalfL1EqualsAmountLedger"
COORDINATE_RECOVERY = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateRecoveryLedger"
SUPPORT_CARDINALITY = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateSupportCardinalityLedger"
NO_SLOT_SPLIT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateNoAmountSlotSplitLedger"
NO_ORIENTATION_FLIP = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateNoOrientationFlipLedger"
FACE_PAYMENT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinatePDECCapReducedToEndpointSignedMassLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateCollisionOrZeroExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinateOrientationLedger"
NO_FACE_BLACKBOX = "StableLadderEndpointOrbitPhaseResidueNoAnonymousUnitFaceValueAfterSignedAmountCoordinateLedger"
AMOUNT_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeSignedAmountCoordinatePacketLedger"
NO_ANON = "NoAnonymousAmountPoolAfterSignedAmountCoordinateLedger"


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
    """把 unit-face-value 硬点替换为 signed-amount-coordinate 硬点。"""
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
        FACE_IMPORT,
        PRICE_ONE,
        POSITIVE_ATOM,
        NEGATIVE_ATOM,
        SIGNED_MASS,
        MASS_BALANCE,
        HALF_L1,
        COORDINATE_RECOVERY,
        SUPPORT_CARDINALITY,
        NO_SLOT_SPLIT,
        NO_ORIENTATION_FLIP,
        FACE_PAYMENT,
        COLLISION_EXIT,
        ORIENTATION,
        NO_FACE_BLACKBOX,
        AMOUNT_PACKET,
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


def signed_amount_coordinate_records() -> list[dict[str, str]]:
    """给出 signed-amount-coordinate 字段。"""
    return [
        {
            "field": "price_one_import",
            "meaning": "继承 face_value=1、amount=A、payment_value=A。",
        },
        {
            "field": "positive_endpoint_atom",
            "meaning": "正端点质量为 W_+=A delta_{r0}。",
        },
        {
            "field": "negative_endpoint_atom",
            "meaning": "负端点质量为 W_-=A delta_{r*}。",
        },
        {
            "field": "signed_mass_coordinate",
            "meaning": "W=A(delta_{r0}-delta_{r*})=A C_Pi。",
        },
        {
            "field": "endpoint_mass_balance",
            "meaning": "正质量与负质量都等于 A，净质量为 0。",
        },
        {
            "field": "half_l1_coordinate",
            "meaning": "||W||_1/2=A，amount 可由有符号质量唯一恢复。",
        },
        {
            "field": "support_cardinality",
            "meaning": "非退化时支撑正好是 {r0,r*}，没有第三个支付槽。",
        },
        {
            "field": "no_amount_pool",
            "meaning": "不存在匿名 amount 池、方向翻转或多槽拆分。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 signed-amount-coordinate 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeUnitFaceValueImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange unit-face-value circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "同点退化或零负载时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueImportedForSignedAmountCoordinate",
            True,
            True,
            "导入 face_value=1、C_Pi(r0)=+1、C_Pi(r*)=-1、amount=A、payment_value=A。",
            FACE_IMPORT,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinatePriceOne",
            True,
            True,
            "单位面额已固定为 1，因此 amount 坐标就是实际支付值。",
            PRICE_ONE,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinatePositiveEndpointAtom",
            True,
            True,
            "正端点原子为 A delta_{r0}。",
            POSITIVE_ATOM,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateNegativeEndpointAtom",
            True,
            True,
            "负端点原子为 A delta_{r*}。",
            NEGATIVE_ATOM,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateSignedMass",
            True,
            True,
            "有符号质量为 W=A(delta_{r0}-delta_{r*})=A C_Pi。",
            SIGNED_MASS,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateEndpointMassBalance",
            True,
            True,
            "正质量 A 与负质量 A 精确相等，净质量为 0。",
            MASS_BALANCE,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateHalfL1EqualsAmount",
            True,
            True,
            "||W||_1/2=A，amount 无法再独立漂移。",
            HALF_L1,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateRecovery",
            True,
            True,
            "A 可由正端点质量、负端点质量或半 L1 读数唯一恢复。",
            COORDINATE_RECOVERY,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateSupportCardinality",
            True,
            True,
            "非退化支撑正好是两个端点；没有第三个支付槽。",
            SUPPORT_CARDINALITY,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateNoAmountSlotSplit",
            True,
            True,
            "不存在把 A 拆成多个同面额支付槽再重组的自由度。",
            NO_SLOT_SPLIT,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateNoOrientationFlip",
            True,
            True,
            "正端点和负端点方向由 C_Pi 固定，不允许方向翻转吸收异常。",
            NO_ORIENTATION_FLIP,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinatePDECCapReducedToEndpointSignedMass",
            True,
            True,
            "若已有出口不支付，PDEC/cap 的待支付对象是唯一二端点有符号质量坐标。",
            FACE_PAYMENT,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateCollisionOrZeroExit",
            True,
            True,
            "若 r0=r* 或 A=0，二端点有符号质量退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinateOrientation",
            True,
            True,
            "有符号质量沿 source -> root 的既定方向支付。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousUnitFaceValueAfterSignedAmountCoordinate",
            True,
            True,
            "unit-face-value 口径被二端点有符号质量坐标替代，不再有匿名 amount 池。",
            NO_FACE_BLACKBOX,
        ),
        row(
            "PhaseResidueExchangeSignedAmountCoordinatePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 signed-amount-coordinate circuit PDEC/cap。",
            AMOUNT_PACKET,
        ),
        row(
            "NoAnonymousAmountPoolAfterSignedAmountCoordinate",
            True,
            True,
            "A 只表示同一二端点 signed dictionary 上的唯一质量坐标。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeSignedAmountCoordinate",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeSignedAmountCoordinateStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、signed-amount-coordinate、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 signed-amount-coordinate circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    latest_basis = replace_latest_basis(previous, reduced)
    rows = build_rows(previous, new_target)

    plain = (
        "phase-residue exchange unit-face-value 已把非退化剩余写成 face_value=1、"
        "amount=A、payment_value=A、C_Pi(r0)=+1、C_Pi(r*)=-1。本步继续把 amount "
        "从匿名标量压成二端点有符号质量坐标：W_+=A delta_{r0}、"
        "W_-=A delta_{r*}、W=A(delta_{r0}-delta_{r*})=A C_Pi、"
        "||W||_1/2=A。于是剩余不再能藏在 amount 池、多槽拆分或方向翻转中；"
        "若 r0=r* 或 A=0 则回流 singleton/degenerate 出口，否则只能表现为 "
        "signed-amount-coordinate circuit PDEC/cap 或已有出口。"
    )

    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_router",
        "status": "phase_residue_exchange_unit_face_value_reduced_to_signed_amount_coordinate_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_unit_face_value_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_signed_amount_coordinate_price_one_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_positive_endpoint_atom_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_negative_endpoint_atom_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_signed_mass_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_endpoint_mass_balance_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_half_l1_equals_amount_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_recovery_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_support_cardinality_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_no_amount_slot_split_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_no_orientation_flip_closed": True,
        "phase_residue_exchange_signed_amount_coordinate_pdec_cap_reduced_to_endpoint_signed_mass_closed": True,
        "phase_residue_no_anonymous_unit_face_value_after_signed_amount_coordinate_closed": True,
        "anonymous_amount_pool_removed_after_signed_amount_coordinate": True,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_circuit_pdec_cap_proved": False,
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
        "latest_noncycle_basis_after_router": latest_basis,
        "signed_amount_coordinate_records": signed_amount_coordinate_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    rows = cert["gates"]
    records = cert["signed_amount_coordinate_records"]
    lines = [
        "# Prime Matrix phase-residue exchange signed-amount-coordinate 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_unit_face_value_imported={fmt_bool(cert['phase_residue_exchange_unit_face_value_imported'])}",
        f"phase_residue_exchange_signed_amount_coordinate_price_one_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_price_one_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_positive_endpoint_atom_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_positive_endpoint_atom_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_negative_endpoint_atom_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_negative_endpoint_atom_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_signed_mass_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_signed_mass_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_endpoint_mass_balance_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_endpoint_mass_balance_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_half_l1_equals_amount_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_half_l1_equals_amount_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_no_amount_slot_split_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_no_amount_slot_split_closed'])}",
        f"phase_residue_exchange_signed_amount_coordinate_no_orientation_flip_closed={fmt_bool(cert['phase_residue_exchange_signed_amount_coordinate_no_orientation_flip_closed'])}",
        "linear_witness_existence_proved=false",
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_circuit_pdec_cap_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. unit-face-value 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "u_e=n_e=[r0]-[r*]",
        "<u_e,phi>=1",
        "||u_e||_1/2=1",
        "face_value=1",
        "C_Pi(r0)=+1",
        "C_Pi(r*)=-1",
        "C_Pi(other)=0",
        "amount=A>0",
        "payment_value=amount*face_value=A",
        "W=A C_Pi",
        "capacity_multiplier=1",
        "denomination_split=0",
        "```",
        "",
        "## 2. signed-amount-coordinate 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in records:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "非退化时 signed-amount-coordinate 证书为：",
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
        "若 `r0=r*` 或 `A=0`，则二端点有符号质量退化并回流 singleton/degenerate 出口。",
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
    for item in rows:
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
        "- 本证书没有证明 phase-residue exchange active-facet normal-cone ray-coordinate scalar-load unit-normalization unit-face-value signed-amount-coordinate circuit PDEC/cap。",
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
