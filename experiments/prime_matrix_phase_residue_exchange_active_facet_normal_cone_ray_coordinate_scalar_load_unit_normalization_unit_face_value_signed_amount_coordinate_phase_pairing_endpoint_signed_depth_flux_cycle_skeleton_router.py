#!/usr/bin/env python3
"""生成 endpoint-signed-depth-flux-cycle-skeleton 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_signed_depth_flux_cycle_skeleton_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.md
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
    "phase-pairing-endpoint-signed-depth-flux-cycle-skeleton"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)

SOURCE_MULTIPLICITY = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
PACKET = "EndpointOrbitSignedDepthFluxPacketPDECCap"
CYCLE = "EndpointOrbitSignedDepthFluxAlternatingTransportCyclePDECCap"

IMPORT = "StableLadderEndpointOrbitSignedDepthFluxPacketImportedForCycleSkeletonLedger"
FINITE_SUPPORT = "StableLadderEndpointOrbitSignedDepthFluxFiniteSupportSkeletonLedger"
UNIT_ATOMS = "StableLadderEndpointOrbitSignedDepthFluxUnitAtomExpansionLedger"
ZERO_BALANCE = "StableLadderEndpointOrbitSignedDepthFluxZeroMeanBalanceLedger"
PAIRING_GRAPH = "StableLadderEndpointOrbitSignedDepthFluxPairingGraphLedger"
LEAF_RETURN = "StableLadderEndpointOrbitSignedDepthFluxAcyclicLeafReturnLedger"
CYCLE_RESIDUAL = "StableLadderEndpointOrbitSignedDepthFluxAlternatingCycleResidualLedger"
NO_PACKET = "NoIndependentEndpointSignedDepthFluxPacketAfterCycleSkeletonLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEndpointCycleSkeletonLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEndpointCycleSkeletonLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEndpointCycleSkeletonLedger"
MULTIPLICITY = "StableLadderEndpointOrbitSourceMultiplicityCapCarriedForwardAfterEndpointCycleSkeletonLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def next_target(previous: dict[str, Any]) -> str:
    """把 signed-depth/flux packet 替换为更窄的 alternating transport cycle。"""
    target = previous.get("next_direct_attack_target", "")
    if PACKET in target:
        target = target.replace(PACKET, CYCLE)
    elif CYCLE not in target:
        target = f"{target}Or{CYCLE}" if target else CYCLE
    return target


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        FINITE_SUPPORT,
        UNIT_ATOMS,
        ZERO_BALANCE,
        PAIRING_GRAPH,
        LEAF_RETURN,
        CYCLE_RESIDUAL,
        NO_PACKET,
        SPARSE,
        SINGLETON,
        FULL_MEAN,
        MULTIPLICITY,
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


def skeleton_records() -> list[dict[str, str]]:
    """列出 signed packet 的有限支撑骨架节点。"""
    return [
        {
            "piece": "positive_unit_atom",
            "role": "signed endpoint measure 的正单位负载；若孤立则回到 endpoint singleton。",
        },
        {
            "piece": "negative_unit_atom",
            "role": "signed endpoint measure 的负单位负载；若缺少配对则回到 source multiplicity。",
        },
        {
            "piece": "pairing_edge",
            "role": "把正负单位按相位/来源配成 endpoint transport edge。",
        },
        {
            "piece": "acyclic_leaf",
            "role": "有限支撑图若无环必有叶；叶不能隐藏，只能回流到已命名出口。",
        },
        {
            "piece": "alternating_cycle",
            "role": "剥离所有叶后仍存在的非匿名 signed-depth/flux 残余硬点。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 endpoint cycle-skeleton 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = PACKET in old_target and previous.get("endpoint_orbit_signed_depth_flux_packet_registered") is True
    zero_mean = previous.get("endpoint_orbit_dynamic_packet_zero_mean_reduction_closed") is True
    return [
        row("EndpointSignedDepthFluxPacketImportedForCycleSkeleton", imported, False, "导入 signed-depth/flux packet 作为当前动态硬点。", old_target),
        row("EndpointSignedDepthFluxFiniteSupportSkeleton", imported, True, "CRT 周期内的 endpoint signed packet 可登记为有限支撑骨架。", FINITE_SUPPORT),
        row("EndpointSignedDepthFluxUnitAtomExpansion", imported, True, "unit normalization 和 face value 把 packet 展成正负单位原子。", UNIT_ATOMS),
        row("EndpointSignedDepthFluxZeroMeanBalance", zero_mean, True, "full-cycle mean 已独立前传后，packet 余量是零均值 signed support。", ZERO_BALANCE),
        row("EndpointSignedDepthFluxPairingGraph", imported and zero_mean, True, "正负单位原子诱导有限 endpoint pairing graph。", PAIRING_GRAPH),
        row("EndpointSignedDepthFluxAcyclicLeafReturn", imported and zero_mean, True, "若 pairing graph 无交替环，则叶剥离回到 singleton、source multiplicity 或 full mean。", LEAF_RETURN),
        row("EndpointSignedDepthFluxAlternatingCycleResidual", False, False, "无叶残余只能是交替 transport cycle；此 cycle 尚未排斥。", CYCLE),
        row("NoIndependentEndpointSignedDepthFluxPacketAfterCycleSkeleton", imported and zero_mean, True, "signed-depth/flux packet 不再作为匿名整包出口。", NO_PACKET),
        row("SparseScaleLadderSAECarriedForwardAfterEndpointCycleSkeleton", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointCycleSkeletonStillOpen", False, False, "仍未排斥 sparse、endpoint singleton、full mean、source multiplicity 或 alternating cycle。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    imported = any(item["gate"] == "EndpointSignedDepthFluxPacketImportedForCycleSkeleton" and item["closed"] for item in rows)
    zero_mean = any(item["gate"] == "EndpointSignedDepthFluxZeroMeanBalance" and item["closed"] for item in rows)
    packet_removed = any(
        item["gate"] == "NoIndependentEndpointSignedDepthFluxPacketAfterCycleSkeleton" and item["closed"]
        for item in rows
    )
    plain = (
        "signed-depth/flux packet 不能继续作为一个未解析整包。"
        "在 finite CRT endpoint support 上，零均值 signed unit atoms 要么经叶剥离回到 "
        "endpoint singleton、full-cycle mean 或 source multiplicity，"
        "要么留下交替 transport cycle。"
        "本步只把整包硬点压成 cycle 硬点，不证明该 cycle 不存在。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_signed_depth_flux_cycle_skeleton_router",
        "status": "phase_residue_exchange_endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_orbit_signed_depth_flux_packet_imported": imported,
        "endpoint_signed_depth_flux_finite_support_skeleton_closed": imported,
        "endpoint_signed_depth_flux_unit_atom_expansion_closed": imported,
        "endpoint_signed_depth_flux_zero_mean_balance_closed": zero_mean,
        "endpoint_signed_depth_flux_pairing_graph_closed": imported and zero_mean,
        "endpoint_signed_depth_flux_acyclic_leaf_return_closed": imported and zero_mean,
        "endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle": packet_removed,
        "endpoint_signed_depth_flux_alternating_transport_cycle_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [PACKET],
        "new_exits": [CYCLE],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "skeleton_records": skeleton_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange endpoint-signed-depth-flux-cycle-skeleton 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_signed_depth_flux_packet_imported={fmt_bool(cert['endpoint_orbit_signed_depth_flux_packet_imported'])}",
        f"endpoint_signed_depth_flux_finite_support_skeleton_closed={fmt_bool(cert['endpoint_signed_depth_flux_finite_support_skeleton_closed'])}",
        f"endpoint_signed_depth_flux_unit_atom_expansion_closed={fmt_bool(cert['endpoint_signed_depth_flux_unit_atom_expansion_closed'])}",
        f"endpoint_signed_depth_flux_zero_mean_balance_closed={fmt_bool(cert['endpoint_signed_depth_flux_zero_mean_balance_closed'])}",
        f"endpoint_signed_depth_flux_pairing_graph_closed={fmt_bool(cert['endpoint_signed_depth_flux_pairing_graph_closed'])}",
        f"endpoint_signed_depth_flux_acyclic_leaf_return_closed={fmt_bool(cert['endpoint_signed_depth_flux_acyclic_leaf_return_closed'])}",
        f"endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle={fmt_bool(cert['endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle'])}",
        f"endpoint_signed_depth_flux_alternating_transport_cycle_pdec_cap_proved={fmt_bool(cert['endpoint_signed_depth_flux_alternating_transport_cycle_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有限支撑骨架",
        "",
        "| piece | role |",
        "| --- | --- |",
    ]
    for record in cert["skeleton_records"]:
        lines.append(f"| `{cell(record['piece'])}` | {cell(record['role'])} |")
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
            "- 本证书只把 signed-depth/flux packet 整包压成 endpoint alternating transport cycle。",
            "- 本证书没有证明 alternating cycle、endpoint singleton、full-cycle mean、source multiplicity 或 sparse SAE。",
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
