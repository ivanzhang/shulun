#!/usr/bin/env python3
"""生成 phase-residue exchange scalar-load unit-normalization 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeScalarLoadUnitNormalizationLedger"
SCALAR_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadImportedForUnitNormalizationLedger"
UNIT_GENERATOR = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitGeneratorLedger"
UNIT_PAIRING = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitPairingLoadLedger"
UNIT_VARIATION = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitVariationLoadLedger"
UNIT_RATIO = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitSaturationRatioLedger"
SCALE_FACTOR = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadScaleFactorLedger"
DIV_FACTORIZATION = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadDivFactorizationLedger"
TOTAL_WEIGHT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadTotalWeightLedger"
NO_SCALE_FREEDOM = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadNoResidualScaleFreedomLedger"
UNIT_PAYMENT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadPDECCapReducedToUnitNormalizationLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitNormalizationCollisionOrZeroExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitNormalizationOrientationLedger"
NO_SCALAR_BLACKBOX = "StableLadderEndpointOrbitPhaseResidueNoAnonymousScalarLoadAfterUnitNormalizationLedger"
UNIT_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeScalarLoadUnitNormalizationPacketLedger"
NO_ANON = "NoAnonymousScalarLoadScaleAfterUnitNormalizationLedger"


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
    """把 scalar-load 硬点替换为 unit-normalization 硬点。"""
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
        SCALAR_IMPORT,
        UNIT_GENERATOR,
        UNIT_PAIRING,
        UNIT_VARIATION,
        UNIT_RATIO,
        SCALE_FACTOR,
        DIV_FACTORIZATION,
        TOTAL_WEIGHT,
        NO_SCALE_FREEDOM,
        UNIT_PAYMENT,
        COLLISION_EXIT,
        ORIENTATION,
        NO_SCALAR_BLACKBOX,
        UNIT_PACKET,
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


def unit_normalization_records() -> list[dict[str, str]]:
    """给出 unit-normalization 字段。"""
    return [
        {
            "field": "unit_generator",
            "meaning": "单位形状为 n_e=[r0]-[r*]，只保留二点有向支撑。",
        },
        {
            "field": "unit_pairing_load",
            "meaning": "<n_e,phi>=phi(r0)-phi(r*)=1。",
        },
        {
            "field": "unit_variation_load",
            "meaning": "||n_e||_1/2=1。",
        },
        {
            "field": "unit_saturation_ratio",
            "meaning": "unit_pairing_load/unit_variation_load=1。",
        },
        {
            "field": "scale_factor",
            "meaning": "唯一尺度因子仍是 A>0。",
        },
        {
            "field": "div_factorization",
            "meaning": "div=A*unit_div=A*n_e。",
        },
        {
            "field": "total_weight",
            "meaning": "全部待支付容量重量为 A，且 A C_Pi=W。",
        },
        {
            "field": "no_residual_scale_freedom",
            "meaning": "形状单位化后没有额外尺度规范、权重拆分或隐藏归一化参数。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 unit-normalization 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeScalarLoadImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange scalar-load circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "同点退化或零负载时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "整周期均值异常继续由 full-cycle mean atom/SAE 出口承接。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeScalarLoadImportedForUnitNormalization",
            True,
            True,
            "导入 scalar_load=A=lambda>0、pairing_load=A、variation_load=A、rank_one_generator=n_e。",
            SCALAR_IMPORT,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitGenerator",
            True,
            True,
            "把非退化二点支撑规范化为 unit_div=n_e=[r0]-[r*]。",
            UNIT_GENERATOR,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitPairingLoad",
            True,
            True,
            "活跃面给出 <unit_div,phi>=phi(r0)-phi(r*)=1。",
            UNIT_PAIRING,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitVariationLoad",
            True,
            True,
            "二点单位流满足 ||unit_div||_1/2=1。",
            UNIT_VARIATION,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitSaturationRatio",
            True,
            True,
            "单位配对负载与单位 variation 负载比例仍为 1。",
            UNIT_RATIO,
        ),
        row(
            "PhaseResidueExchangeScalarLoadScaleFactor",
            True,
            True,
            "唯一未支付强度是正尺度 A，且与上一层 scalar_load 相同。",
            SCALE_FACTOR,
        ),
        row(
            "PhaseResidueExchangeScalarLoadDivFactorization",
            True,
            True,
            "div=A*unit_div=A*n_e，没有第二个权重分解。",
            DIV_FACTORIZATION,
        ),
        row(
            "PhaseResidueExchangeScalarLoadTotalWeight",
            True,
            True,
            "总支付重量为 A，并保持 A C_Pi=W。",
            TOTAL_WEIGHT,
        ),
        row(
            "PhaseResidueExchangeScalarLoadNoResidualScaleFreedom",
            True,
            True,
            "单位化后无剩余尺度规范、分摊自由度或隐藏归一化参数。",
            NO_SCALE_FREEDOM,
        ),
        row(
            "PhaseResidueExchangeScalarLoadPDECCapReducedToUnitNormalization",
            True,
            True,
            "若已有出口不支付，PDEC/cap 的待支付对象是单位形状上的总权重 A。",
            UNIT_PAYMENT,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitNormalizationCollisionOrZeroExit",
            True,
            True,
            "若 r0=r* 或 A=0，单位形状或正尺度退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitNormalizationOrientation",
            True,
            True,
            "单位形状沿 source -> root 的既定方向，A 只作正权重。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousScalarLoadAfterUnitNormalization",
            True,
            True,
            "scalar-load 口径被分解为单位形状和总权重，不再有匿名尺度黑箱。",
            NO_SCALAR_BLACKBOX,
        ),
        row(
            "PhaseResidueExchangeScalarLoadUnitNormalizationPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange scalar-load unit-normalization circuit PDEC/cap。",
            UNIT_PACKET,
        ),
        row(
            "NoAnonymousScalarLoadScaleAfterUnitNormalization",
            True,
            True,
            "正标量 A 只作为单位二点证书上的总权重出现。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeScalarLoadUnitNormalization",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeScalarLoadUnitNormalizationStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、unit-normalized scalar-load、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange scalar-load unit-normalization circuit 或并行出口。",
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
        "phase-residue exchange scalar-load 已把非退化剩余压成单一正标量负载 A，"
        "并给出 pairing_load=A、variation_load=A、rank_one_generator=n_e。"
        "本步把 A 的尺度与单位形状分离：unit_div=n_e=[r0]-[r*]，"
        "<unit_div,phi>=1，||unit_div||_1/2=1，div=A*unit_div，total_weight=A，"
        "且 A C_Pi=W。于是剩余不再能藏在 scalar-load 的尺度规范或权重拆分中；"
        "若 r0=r* 或 A=0 则回流 singleton/degenerate 出口，否则只能表现为 "
        "unit-normalized scalar-load circuit PDEC/cap 或已有出口。"
    )

    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_router",
        "status": "phase_residue_exchange_scalar_load_reduced_to_unit_normalization_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "phase_residue_exchange_scalar_load_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_scalar_load_unit_generator_closed": True,
        "phase_residue_exchange_scalar_load_unit_pairing_load_closed": True,
        "phase_residue_exchange_scalar_load_unit_variation_load_closed": True,
        "phase_residue_exchange_scalar_load_unit_saturation_ratio_closed": True,
        "phase_residue_exchange_scalar_load_scale_factor_closed": True,
        "phase_residue_exchange_scalar_load_div_factorization_closed": True,
        "phase_residue_exchange_scalar_load_total_weight_closed": True,
        "phase_residue_exchange_scalar_load_no_residual_scale_freedom_closed": True,
        "phase_residue_exchange_scalar_load_pdec_cap_reduced_to_unit_normalization_closed": True,
        "phase_residue_no_anonymous_scalar_load_after_unit_normalization_closed": True,
        "anonymous_scalar_load_scale_removed_after_unit_normalization": True,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_circuit_pdec_cap_proved": False,
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
        "unit_normalization_records": unit_normalization_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    rows = cert["gates"]
    records = cert["unit_normalization_records"]
    lines = [
        "# Prime Matrix phase-residue exchange scalar-load unit-normalization 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_scalar_load_imported={fmt_bool(cert['phase_residue_exchange_scalar_load_imported'])}",
        f"phase_residue_exchange_scalar_load_unit_generator_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_unit_generator_closed'])}",
        f"phase_residue_exchange_scalar_load_unit_pairing_load_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_unit_pairing_load_closed'])}",
        f"phase_residue_exchange_scalar_load_unit_variation_load_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_unit_variation_load_closed'])}",
        f"phase_residue_exchange_scalar_load_unit_saturation_ratio_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_unit_saturation_ratio_closed'])}",
        f"phase_residue_exchange_scalar_load_scale_factor_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_scale_factor_closed'])}",
        f"phase_residue_exchange_scalar_load_div_factorization_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_div_factorization_closed'])}",
        f"phase_residue_exchange_scalar_load_no_residual_scale_freedom_closed={fmt_bool(cert['phase_residue_exchange_scalar_load_no_residual_scale_freedom_closed'])}",
        "linear_witness_existence_proved=false",
        "phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_circuit_pdec_cap_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. scalar-load 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "scalar_load=A=lambda>0",
        "rank_one_generator=n_e=[r0]-[r*]",
        "pairing_load=<div,phi>=A",
        "variation_load=||div||_1/2=A",
        "unit_saturation_ratio=1",
        "residual_vector_geometry=0",
        "A C_Pi=W",
        "```",
        "",
        "## 2. unit-normalization 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in records:
        lines.append(f"| `{record['field']}` | {cell(record['meaning'])} |")
    lines += [
        "",
        "非退化时 unit-normalization 证书为：",
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
        "若 `r0=r*` 或 `A=0`，则单位形状或正尺度退化并回流 singleton/degenerate 出口。",
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
        "- 本证书没有证明 phase-residue exchange active-facet normal-cone ray-coordinate scalar-load unit-normalization circuit PDEC/cap。",
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
