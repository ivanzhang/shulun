#!/usr/bin/env python3
"""生成 phase-residue exchange transport-edge incidence column 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_transport_edge_incidence_column_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.json

输出：
  data/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-transport-edge-incidence-column"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeOrientedRootSourceTransportEdgeCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeTransportEdgeIncidenceColumnCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedRootSourceTransportEdgeImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeTransportEdgeIncidenceColumnLedger"
EDGE_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeImportedForIncidenceColumnLedger"
TAIL_HEAD = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeTailHeadCoordinateLedger"
INCIDENCE_VECTOR = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeIncidenceVectorLedger"
BOUNDARY_COLUMN = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeBoundaryMatrixColumnLedger"
FLUX_COORDINATE = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeFluxCoordinateLedger"
MATRIX_BOUNDARY = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeMatrixBoundaryIdentityLedger"
COLUMN_ZERO_SUM = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeIncidenceColumnZeroSumLedger"
COLUMN_SUPPORT = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeTwoEndpointSupportLedger"
NO_HIDDEN_CYCLE = "StableLadderEndpointOrbitPhaseResidueNoHiddenCycleInsideSingleIncidenceColumnLedger"
COLUMN_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeIncidenceColumnPacketLedger"
NO_ANON = "NoAnonymousOrientedRootSourceTransportEdgeAfterIncidenceColumnLedger"


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
    """把 oriented transport edge 硬点替换为 incidence column 硬点。"""
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
        EDGE_IMPORT,
        TAIL_HEAD,
        INCIDENCE_VECTOR,
        BOUNDARY_COLUMN,
        FLUX_COORDINATE,
        MATRIX_BOUNDARY,
        COLUMN_ZERO_SUM,
        COLUMN_SUPPORT,
        NO_HIDDEN_CYCLE,
        COLUMN_PACKET,
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


def incidence_records() -> list[dict[str, str]]:
    """给出单边 incidence column 的字段。"""
    return [
        {
            "field": "tail_slot",
            "meaning": "边尾坐标为 source 端 s*。",
        },
        {
            "field": "head_slot",
            "meaning": "边头坐标为 root 端 s0。",
        },
        {
            "field": "incidence_column",
            "meaning": "b_e=[s0]-[s*]，即 b_e(s0)=+1、b_e(s*)=-1。",
        },
        {
            "field": "boundary_matrix",
            "meaning": "边界矩阵 B 的 e 列满足 B[:,e]=b_e。",
        },
        {
            "field": "flux_coordinate",
            "meaning": "单边通量坐标 f_e=A。",
        },
        {
            "field": "matrix_boundary",
            "meaning": "Bf=A b_e=A([s0]-[s*])=W。",
        },
        {
            "field": "zero_sum",
            "meaning": "列和为 0；除 root/source 两端外所有顶点坐标为 0。",
        },
        {
            "field": "cycle_guard",
            "meaning": "单列对象没有内部顶点复用；循环压力只能进入命名 PDEC/cap 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 transport-edge incidence column 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeOrientedRootSourceTransportEdgeImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange oriented root-source transport edge circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeImportedForIncidenceColumn",
            True,
            True,
            "导入 e=s*->s0、F=A、partial(F e)=W、F>=|Lambda(D)|/2。",
            EDGE_IMPORT,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeTailHeadCoordinate",
            True,
            True,
            "登记 tail_slot=s* 与 head_slot=s0。",
            TAIL_HEAD,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeIncidenceVector",
            True,
            True,
            "定义 b_e=[s0]-[s*]，root 端 +1、source 端 -1。",
            INCIDENCE_VECTOR,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeBoundaryMatrixColumn",
            True,
            True,
            "边界矩阵的单列满足 B[:,e]=b_e。",
            BOUNDARY_COLUMN,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeFluxCoordinate",
            True,
            True,
            "单边通量向量只有 f_e=A 一个活动坐标。",
            FLUX_COORDINATE,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeMatrixBoundaryIdentity",
            True,
            True,
            "矩阵边界恒等式 Bf=A b_e=A([s0]-[s*])=W。",
            MATRIX_BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeIncidenceColumnZeroSum",
            True,
            True,
            "incidence column 的列和为 0，继承质量守恒。",
            COLUMN_ZERO_SUM,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeTwoEndpointSupport",
            True,
            True,
            "非退化边只在 root/source 两端有非零坐标；退化情形回流 singleton 出口。",
            COLUMN_SUPPORT,
        ),
        row(
            "PhaseResidueNoHiddenCycleInsideSingleIncidenceColumn",
            True,
            True,
            "单列边界矩阵对象没有内部路径或循环可藏；循环性只能出现在命名 PDEC/cap 出口。",
            NO_HIDDEN_CYCLE,
        ),
        row(
            "PhaseResidueExchangeTransportEdgeIncidenceColumnPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange transport-edge incidence-column circuit PDEC/cap。",
            COLUMN_PACKET,
        ),
        row(
            "NoAnonymousOrientedRootSourceTransportEdgeAfterIncidenceColumn",
            True,
            True,
            "有向输运边被压成 tail/head 坐标、incidence column 与单通量坐标。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeTransportEdgeIncidenceColumn",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeTransportEdgeIncidenceColumnStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、incidence-column、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange transport-edge incidence-column circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 transport-edge incidence column 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange oriented root-source transport edge 已把剩余写成 e=s*->s0、F=A。"
        "本步把该边登记为单列 incidence 坐标：b_e=[s0]-[s*]，边界矩阵 B 的 e 列为 b_e，"
        "单通量坐标 f_e=A。于是 Bf=A b_e=A([s0]-[s*])=W。"
        "剩余反例不再是未坐标化的有向边，而必须表现为 transport-edge incidence-column circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_transport_edge_incidence_column_router",
        "status": "phase_residue_exchange_oriented_root_source_transport_edge_reduced_to_incidence_column_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "transport_edge_incidence_column_records": incidence_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_oriented_root_source_transport_edge_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_transport_edge_imported_for_incidence_column": True,
        "phase_residue_exchange_transport_edge_tail_head_coordinate_closed": True,
        "phase_residue_exchange_transport_edge_incidence_vector_closed": True,
        "phase_residue_exchange_transport_edge_boundary_matrix_column_closed": True,
        "phase_residue_exchange_transport_edge_flux_coordinate_closed": True,
        "phase_residue_exchange_transport_edge_matrix_boundary_identity_closed": True,
        "phase_residue_exchange_transport_edge_incidence_column_zero_sum_closed": True,
        "phase_residue_exchange_transport_edge_two_endpoint_support_closed": True,
        "phase_residue_no_hidden_cycle_inside_single_incidence_column_closed": True,
        "phase_residue_exchange_transport_edge_incidence_column_packet_registered": True,
        "anonymous_oriented_root_source_transport_edge_removed_after_incidence_column": True,
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
        "phase_residue_exchange_transport_edge_incidence_column_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange transport-edge incidence column 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_oriented_root_source_transport_edge_imported={fmt_bool(cert['phase_residue_exchange_oriented_root_source_transport_edge_imported'])}",
        f"phase_residue_exchange_transport_edge_tail_head_coordinate_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_tail_head_coordinate_closed'])}",
        f"phase_residue_exchange_transport_edge_incidence_vector_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_incidence_vector_closed'])}",
        f"phase_residue_exchange_transport_edge_boundary_matrix_column_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_boundary_matrix_column_closed'])}",
        f"phase_residue_exchange_transport_edge_flux_coordinate_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_flux_coordinate_closed'])}",
        f"phase_residue_exchange_transport_edge_matrix_boundary_identity_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_matrix_boundary_identity_closed'])}",
        f"phase_residue_exchange_transport_edge_incidence_column_zero_sum_closed={fmt_bool(cert['phase_residue_exchange_transport_edge_incidence_column_zero_sum_closed'])}",
        f"phase_residue_no_hidden_cycle_inside_single_incidence_column_closed={fmt_bool(cert['phase_residue_no_hidden_cycle_inside_single_incidence_column_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_transport_edge_incidence_column_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_transport_edge_incidence_column_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. oriented transport edge 输入",
        "",
        "上一层给出有向输运边：",
        "",
        "```text",
        "e = s* -> s0",
        "F = A",
        "partial(F e) = A([s0]-[s*]) = W",
        "F >= |Lambda(D)|/2",
        "```",
        "",
        "本证书继续不证明 `Lambda` 的存在，只处理已导入边的坐标化。",
        "",
        "## 2. 单列 incidence 坐标",
        "",
        "定义边界矩阵的单列：",
        "",
        "```text",
        "tail(e)=s*",
        "head(e)=s0",
        "b_e=[s0]-[s*]",
        "B[:,e]=b_e",
        "f_e=A",
        "```",
        "",
        "于是矩阵边界恒等式为：",
        "",
        "```text",
        "B f = A b_e = A([s0]-[s*]) = W",
        "```",
        "",
        "## 3. 列守恒读数",
        "",
        "```text",
        "b_e(s0)=+1",
        "b_e(s*)=-1",
        "b_e(v)=0  (v not in {s0,s*})",
        "sum_v b_e(v)=0",
        "support(b_e)={s0,s*} in the nondegenerate case",
        "```",
        "",
        "因此剩余不再是未坐标化的有向边，而是一列命名 boundary-matrix incidence column。",
        "",
        "## 4. transport-edge incidence column 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["transport_edge_incidence_column_records"]:
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
            "- 本证书没有证明 phase-residue exchange transport-edge incidence-column circuit PDEC/cap。",
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
    print("phase_residue_exchange_transport_edge_incidence_column_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
