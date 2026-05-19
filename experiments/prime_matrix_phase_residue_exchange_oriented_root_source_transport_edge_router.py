#!/usr/bin/env python3
"""生成 phase-residue exchange oriented root-source transport edge 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_oriented_root_source_transport_edge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.json

输出：
  data/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeSignedRootSourceHalfGapAtomCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeOrientedRootSourceTransportEdgeCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedRootSourceHalfGapAtomImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeOrientedRootSourceTransportEdgeLedger"
ATOM_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedHalfGapAtomImportedForTransportEdgeLedger"
EDGE_ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeOrientationLedger"
EDGE_FLUX = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeFluxLedger"
EDGE_BOUNDARY = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeBoundaryIdentityLedger"
EDGE_DIVERGENCE = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeDivergenceLedger"
EDGE_CONSERVATION = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeMassConservationLedger"
EDGE_FLUX_BOUND = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeFluxLowerBoundLedger"
NO_SIGNED_ATOM = "StableLadderEndpointOrbitPhaseResidueNoAnonymousSignedAtomAfterTransportEdgeLedger"
EDGE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedRootSourceTransportEdgePacketLedger"
NO_ANON = "NoAnonymousSignedRootSourceHalfGapAtomAfterTransportEdgeLedger"


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
    """把 signed half-gap atom 硬点替换为 oriented transport edge 硬点。"""
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
        ATOM_IMPORT,
        EDGE_ORIENTATION,
        EDGE_FLUX,
        EDGE_BOUNDARY,
        EDGE_DIVERGENCE,
        EDGE_CONSERVATION,
        EDGE_FLUX_BOUND,
        NO_SIGNED_ATOM,
        EDGE_PACKET,
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


def edge_records() -> list[dict[str, str]]:
    """给出 oriented root-source transport edge 的字段。"""
    return [
        {
            "field": "tail",
            "meaning": "输运边尾点为 source 端 s*。",
        },
        {
            "field": "head",
            "meaning": "输运边头点为 root 端 s0。",
        },
        {
            "field": "flux",
            "meaning": "正通量 F=A=G/2。",
        },
        {
            "field": "boundary",
            "meaning": "边界算子给出 partial(F e_{s*->s0})=A([s0]-[s*])。",
        },
        {
            "field": "divergence",
            "meaning": "root 端入流 +A，source 端出流 -A。",
        },
        {
            "field": "conservation",
            "meaning": "总散度为 0，通量下界 A>=|Lambda(D)|/2。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 oriented root-source transport edge 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeSignedRootSourceHalfGapAtomImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange signed root-source half-gap atom circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeSignedHalfGapAtomImportedForTransportEdge",
            True,
            True,
            "导入 W=A([s0]-[s*])、A>=|Lambda(D)|/2、mass(W)=0。",
            ATOM_IMPORT,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeOrientation",
            True,
            True,
            "把符号支撑定向为 source s* 到 root s0 的单边。",
            EDGE_ORIENTATION,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeFlux",
            True,
            True,
            "登记正通量 F=A=G/2。",
            EDGE_FLUX,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeBoundaryIdentity",
            True,
            True,
            "边界恒等式 partial(F e_{s*->s0})=A([s0]-[s*])=W。",
            EDGE_BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeDivergence",
            True,
            True,
            "root 端散度为 +A，source 端散度为 -A。",
            EDGE_DIVERGENCE,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeMassConservation",
            True,
            True,
            "两端散度相加为 0；输运边保持净质量守恒。",
            EDGE_CONSERVATION,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeFluxLowerBound",
            True,
            True,
            "通量继承 A>=|Lambda(D)|/2；非零见证时 F>0。",
            EDGE_FLUX_BOUND,
        ),
        row(
            "PhaseResidueNoAnonymousSignedAtomAfterTransportEdge",
            True,
            True,
            "剩余不再是匿名 signed atom，而是一条命名 source-to-root transport edge。",
            NO_SIGNED_ATOM,
        ),
        row(
            "PhaseResidueExchangeOrientedRootSourceTransportEdgePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange oriented root-source transport edge circuit PDEC/cap。",
            EDGE_PACKET,
        ),
        row(
            "NoAnonymousSignedRootSourceHalfGapAtomAfterTransportEdge",
            True,
            True,
            "signed root-source half-gap atom 被压成有向输运边。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeOrientedRootSourceTransportEdge",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeOrientedRootSourceTransportEdgeStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、transport edge、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange oriented root-source transport edge circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 oriented root-source transport edge 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange signed root-source half-gap atom 已把剩余写成 W=A([s0]-[s*])。"
        "本步把该符号原子解释为一条 source s* 指向 root s0 的有向输运边，通量 F=A。"
        "边界恒等式 partial(F e_{s*->s0})=A([s0]-[s*])=W，root 端散度 +A、source 端散度 -A。"
        "剩余反例不再是匿名 signed atom，而必须表现为 oriented root-source transport edge circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_oriented_root_source_transport_edge_router",
        "status": "phase_residue_exchange_signed_root_source_half_gap_atom_reduced_to_oriented_root_source_transport_edge_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "oriented_root_source_transport_edge_records": edge_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_signed_root_source_half_gap_atom_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_signed_half_gap_atom_imported_for_transport_edge": True,
        "phase_residue_exchange_transport_edge_orientation_closed": True,
        "phase_residue_exchange_transport_edge_flux_closed": True,
        "phase_residue_exchange_transport_edge_boundary_identity_closed": True,
        "phase_residue_exchange_transport_edge_divergence_closed": True,
        "phase_residue_exchange_transport_edge_mass_conservation_closed": True,
        "phase_residue_exchange_transport_edge_flux_lower_bound_closed": True,
        "phase_residue_no_anonymous_signed_atom_after_transport_edge_closed": True,
        "phase_residue_exchange_oriented_root_source_transport_edge_packet_registered": True,
        "anonymous_signed_root_source_half_gap_atom_removed_after_transport_edge": True,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "linear_witness_existence_proved": False,
        "phase_residue_exchange_oriented_root_source_transport_edge_circuit_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "source_hashes": source_hashes(),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange oriented root-source transport edge 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_signed_root_source_half_gap_atom_imported={fmt_bool(cert['phase_residue_exchange_signed_root_source_half_gap_atom_imported'])}",
        f"phase_residue_exchange_transport_edge_orientation_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_orientation_closed'])}",
        f"phase_residue_exchange_transport_edge_flux_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_flux_closed'])}",
        f"phase_residue_exchange_transport_edge_boundary_identity_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_boundary_identity_closed'])}",
        f"phase_residue_exchange_transport_edge_divergence_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_divergence_closed'])}",
        f"phase_residue_exchange_transport_edge_mass_conservation_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_mass_conservation_closed'])}",
        f"phase_residue_exchange_transport_edge_flux_lower_bound_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_flux_lower_bound_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_oriented_root_source_transport_edge_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_oriented_root_source_transport_edge_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed half-gap atom 输入",
        "",
        "上一层给出符号原子：",
        "",
        "```text",
        "W = A([s0]-[s*])",
        "A >= |Lambda(D)|/2",
        "mass(W)=0",
        "```",
        "",
        "本证书继续不证明 `Lambda` 的存在，只处理已导入见证后的边界算子重写。",
        "",
        "## 2. 有向输运边",
        "",
        "定义一条从 source 到 root 的边：",
        "",
        "```text",
        "e = s* -> s0",
        "F = A",
        "```",
        "",
        "边界算子给出：",
        "",
        "```text",
        "partial(F e) = A([s0]-[s*]) = W",
        "```",
        "",
        "## 3. 守恒读数",
        "",
        "该边在两个端点上的散度为：",
        "",
        "```text",
        "div(s0) = +A",
        "div(s*) = -A",
        "div(s0)+div(s*) = 0",
        "F >= |Lambda(D)|/2",
        "```",
        "",
        "因此剩余不再是匿名 signed atom，而是一条命名 source-to-root transport edge。",
        "",
        "## 4. oriented root-source transport edge 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["oriented_root_source_transport_edge_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 5. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
            "```",
            "",
            "## 6. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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

    lines.extend(
        [
            "",
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange oriented root-source transport edge circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 9. 依赖哈希",
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
    """生成 JSON、ledger 和 Markdown 三件套。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("phase_residue_exchange_oriented_root_source_transport_edge_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
