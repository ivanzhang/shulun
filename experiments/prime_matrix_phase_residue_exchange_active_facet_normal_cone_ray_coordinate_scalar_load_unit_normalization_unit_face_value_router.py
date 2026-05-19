#!/usr/bin/env python3
"""生成 phase-residue exchange unit-normalization unit-face-value 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitNormalizationImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeUnitFaceValueLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeUnitFaceValueLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeUnitFaceValueLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeUnitFaceValueLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeUnitFaceValueLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeUnitFaceValueLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeUnitFaceValueLedger"
UNIT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitNormalizationImportedForUnitFaceValueLedger"
UNIT_SHAPE = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueUnitShapeLedger"
PAIRING_FACE = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValuePairingLedger"
VARIATION_FACE = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueVariationLedger"
FACE_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueOneLedger"
SIGNED_DICTIONARY = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueSignedDictionaryLedger"
TOTAL_AMOUNT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueTotalAmountLedger"
PAYMENT_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValuePaymentValueLedger"
NO_MULTIPLIER = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueNoCapacityMultiplierLedger"
NO_DENOMINATION_SPLIT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueNoDenominationSplitLedger"
FACE_PAYMENT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValuePDECCapReducedToPriceOnePaymentLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueCollisionOrZeroExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValueOrientationLedger"
NO_UNIT_FACE_BLACKBOX = "StableLadderEndpointOrbitPhaseResidueNoAnonymousUnitNormalizationAfterUnitFaceValueLedger"
FACE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeUnitFaceValuePacketLedger"
NO_ANON = "NoAnonymousCapacityFaceValueAfterUnitFaceValueLedger"


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
    """把 unit-normalization 硬点替换为 unit-face-value 硬点。"""
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
        UNIT_IMPORT,
        UNIT_SHAPE,
        PAIRING_FACE,
        VARIATION_FACE,
        FACE_VALUE,
        SIGNED_DICTIONARY,
        TOTAL_AMOUNT,
        PAYMENT_VALUE,
        NO_MULTIPLIER,
        NO_DENOMINATION_SPLIT,
        FACE_PAYMENT,
        COLLISION_EXIT,
        ORIENTATION,
        NO_UNIT_FACE_BLACKBOX,
        FACE_PACKET,
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


def unit_face_value_records() -> list[dict[str, str]]:
    """给出 unit-face-value 字段。"""
    return [
        {
            "field": "unit_shape",
            "meaning": "单位证书仍是 u_e=n_e=[r0]-[r*]。",
        },
        {
            "field": "pairing_face_value",
            "meaning": "<u_e,phi>=1，因此配对面额为 1。",
        },
        {
            "field": "variation_face_value",
            "meaning": "||u_e||_1/2=1，因此变差面额也为 1。",
        },
        {
            "field": "capacity_face_value",
            "meaning": "容量支付面额 face_value=1，不再带隐藏乘子。",
        },
        {
            "field": "signed_dictionary",
            "meaning": "C_Pi(r0)=+1、C_Pi(r*)=-1，其余为 0。",
        },
        {
            "field": "total_amount",
            "meaning": "唯一支付数量为 amount=A>0。",
        },
        {
            "field": "payment_value",
            "meaning": "payment_value=amount*face_value=A。",
        },
        {
            "field": "no_capacity_multiplier",
            "meaning": "不存在第二个容量乘子、面额换算或单位重标定。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 unit-face-value 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeScalarLoadUnitNormalizationImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange scalar-load unit-normalization circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "同点退化或零负载时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeUnitNormalizationImportedForUnitFaceValue",
            True,
            True,
            "导入 unit_div=n_e、<unit_div,phi>=1、||unit_div||_1/2=1、total_weight=A。",
            UNIT_IMPORT,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueUnitShape",
            True,
            True,
            "单位形状仍是 u_e=n_e=[r0]-[r*]，支撑没有扩张。",
            UNIT_SHAPE,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValuePairing",
            True,
            True,
            "配对读数给出单位面额：<u_e,phi>=1。",
            PAIRING_FACE,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueVariation",
            True,
            True,
            "变差读数给出同一单位面额：||u_e||_1/2=1。",
            VARIATION_FACE,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueOne",
            True,
            True,
            "容量支付面额固定为 face_value=1。",
            FACE_VALUE,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueSignedDictionary",
            True,
            True,
            "单位证书的 signed dictionary 为 C_Pi(r0)=+1、C_Pi(r*)=-1、其余 0。",
            SIGNED_DICTIONARY,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueTotalAmount",
            True,
            True,
            "唯一支付数量为 amount=A>0。",
            TOTAL_AMOUNT,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValuePaymentValue",
            True,
            True,
            "总支付值为 amount*face_value=A，并保持 W=A C_Pi。",
            PAYMENT_VALUE,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueNoCapacityMultiplier",
            True,
            True,
            "不存在额外容量乘子或单位重标定。",
            NO_MULTIPLIER,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueNoDenominationSplit",
            True,
            True,
            "不存在多面额拆分；反例只能使用同一 price-one 单位证书。",
            NO_DENOMINATION_SPLIT,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValuePDECCapReducedToPriceOnePayment",
            True,
            True,
            "若已有出口不支付，PDEC/cap 的待支付对象是 price-one 单位证书上的数量 A。",
            FACE_PAYMENT,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueCollisionOrZeroExit",
            True,
            True,
            "若 r0=r* 或 A=0，面额证书退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValueOrientation",
            True,
            True,
            "单位面额沿 source -> root 的既定方向支付。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousUnitNormalizationAfterUnitFaceValue",
            True,
            True,
            "unit-normalization 口径被面额为 1 的支付证书替代，不再有匿名容量面额。",
            NO_UNIT_FACE_BLACKBOX,
        ),
        row(
            "PhaseResidueExchangeUnitFaceValuePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange unit-face-value circuit PDEC/cap。",
            FACE_PACKET,
        ),
        row(
            "NoAnonymousCapacityFaceValueAfterUnitFaceValue",
            True,
            True,
            "容量面额固定为 1，A 只表示 price-one 单位证书的总数量。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeUnitFaceValue",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeUnitFaceValueStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、unit-face-value、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange unit-face-value circuit 或并行出口。",
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
        "phase-residue exchange unit-normalization 已把非退化剩余写成 "
        "unit_div=n_e=[r0]-[r*]、<unit_div,phi>=1、||unit_div||_1/2=1、"
        "div=A*unit_div、total_weight=A、A C_Pi=W。本步把这个单位证书的容量面额"
        "显式固定为 face_value=1：配对面额、变差面额和 signed dictionary 面额一致，"
        "payment_value=A*1=A。于是剩余不再能藏在容量乘子、面额换算或多面额拆分中；"
        "若 r0=r* 或 A=0 则回流 singleton/degenerate 出口，否则只能表现为 "
        "unit-face-value circuit PDEC/cap 或已有出口。"
    )

    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_router",
        "status": "phase_residue_exchange_unit_normalization_reduced_to_unit_face_value_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_scalar_load_unit_normalization_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_unit_face_value_unit_shape_closed": True,
        "phase_residue_exchange_unit_face_value_pairing_closed": True,
        "phase_residue_exchange_unit_face_value_variation_closed": True,
        "phase_residue_exchange_unit_face_value_one_closed": True,
        "phase_residue_exchange_unit_face_value_signed_dictionary_closed": True,
        "phase_residue_exchange_unit_face_value_total_amount_closed": True,
        "phase_residue_exchange_unit_face_value_payment_value_closed": True,
        "phase_residue_exchange_unit_face_value_no_capacity_multiplier_closed": True,
        "phase_residue_exchange_unit_face_value_no_denomination_split_closed": True,
        "phase_residue_exchange_unit_face_value_pdec_cap_reduced_to_price_one_payment_closed": True,
        "phase_residue_no_anonymous_unit_normalization_after_unit_face_value_closed": True,
        "anonymous_capacity_face_value_removed_after_unit_face_value": True,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_circuit_pdec_cap_proved": False,
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
        "unit_face_value_records": unit_face_value_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    rows = cert["gates"]
    records = cert["unit_face_value_records"]
    lines = [
        "# Prime Matrix phase-residue exchange unit-face-value 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_scalar_load_unit_normalization_imported={fmt_bool(cert['phase_residue_exchange_scalar_load_unit_normalization_imported'])}",
        f"phase_residue_exchange_unit_face_value_unit_shape_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_unit_shape_closed'])}",
        f"phase_residue_exchange_unit_face_value_pairing_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_pairing_closed'])}",
        f"phase_residue_exchange_unit_face_value_variation_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_variation_closed'])}",
        f"phase_residue_exchange_unit_face_value_one_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_one_closed'])}",
        f"phase_residue_exchange_unit_face_value_total_amount_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_total_amount_closed'])}",
        f"phase_residue_exchange_unit_face_value_payment_value_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_payment_value_closed'])}",
        f"phase_residue_exchange_unit_face_value_no_capacity_multiplier_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_no_capacity_multiplier_closed'])}",
        f"phase_residue_exchange_unit_face_value_no_denomination_split_closed={fmt_bool(cert['phase_residue_exchange_unit_face_value_no_denomination_split_closed'])}",
        "linear_witness_existence_proved=false",
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_circuit_pdec_cap_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. unit-normalization 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "unit_div=n_e=[r0]-[r*]",
        "<unit_div,phi>=1",
        "||unit_div||_1/2=1",
        "unit_saturation_ratio=1",
        "scale_factor=A>0",
        "div=A*unit_div=A*n_e",
        "total_weight=A",
        "A C_Pi=W",
        "residual_scale_freedom=0",
        "```",
        "",
        "## 2. unit-face-value 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in records:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "非退化时 unit-face-value 证书为：",
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
        "若 `r0=r*` 或 `A=0`，则单位面额证书退化并回流 singleton/degenerate 出口。",
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
        "- 本证书没有证明 phase-residue exchange active-facet normal-cone ray-coordinate scalar-load unit-normalization unit-face-value circuit PDEC/cap。",
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
