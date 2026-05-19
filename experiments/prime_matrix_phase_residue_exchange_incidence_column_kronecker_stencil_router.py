#!/usr/bin/env python3
"""生成 phase-residue exchange incidence-column Kronecker stencil 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_incidence_column_kronecker_stencil_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.json

输出：
  data/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeTransportEdgeIncidenceColumnCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeIncidenceColumnKroneckerStencilCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeTransportEdgeIncidenceColumnImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeIncidenceColumnKroneckerStencilLedger"
COLUMN_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeIncidenceColumnImportedForKroneckerStencilLedger"
ROOT_DELTA = "StableLadderEndpointOrbitPhaseResidueExchangeRootKroneckerDeltaCoordinateLedger"
SOURCE_DELTA = "StableLadderEndpointOrbitPhaseResidueExchangeSourceKroneckerDeltaCoordinateLedger"
SIGNED_STENCIL = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerDeltaDifferenceStencilLedger"
STENCIL_SIGNS = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilSignedCoefficientLedger"
CRT_ENDPOINTS = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilEndpointCRTCoordinateLedger"
DISTINCT_OR_SINGLETON = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourceCoordinateDistinctOrSingletonExitLedger"
STENCIL_ZERO_SUM = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilZeroSumLedger"
COLUMN_EQUALS_STENCIL = "StableLadderEndpointOrbitPhaseResidueExchangeIncidenceColumnEqualsKroneckerStencilLedger"
FLUX_SCALING = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilFluxScalingLedger"
NO_MATRIX = "StableLadderEndpointOrbitPhaseResidueNoAnonymousBoundaryMatrixColumnAfterKroneckerStencilLedger"
STENCIL_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeIncidenceColumnKroneckerStencilPacketLedger"
NO_ANON = "NoAnonymousTransportEdgeIncidenceColumnAfterKroneckerStencilLedger"


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
    """把 incidence-column 硬点替换为 Kronecker stencil 硬点。"""
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
        COLUMN_IMPORT,
        ROOT_DELTA,
        SOURCE_DELTA,
        SIGNED_STENCIL,
        STENCIL_SIGNS,
        CRT_ENDPOINTS,
        DISTINCT_OR_SINGLETON,
        STENCIL_ZERO_SUM,
        COLUMN_EQUALS_STENCIL,
        FLUX_SCALING,
        NO_MATRIX,
        STENCIL_PACKET,
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


def stencil_records() -> list[dict[str, str]]:
    """给出 Kronecker endpoint stencil 的字段。"""
    return [
        {
            "field": "root_delta",
            "meaning": "root 端单位坐标 delta_{s0}。",
        },
        {
            "field": "source_delta",
            "meaning": "source 端单位坐标 delta_{s*}。",
        },
        {
            "field": "signed_stencil",
            "meaning": "端点模板 k=delta_{s0}-delta_{s*}。",
        },
        {
            "field": "coefficient_vector",
            "meaning": "root 系数 +1，source 系数 -1，其余坐标 0。",
        },
        {
            "field": "crt_endpoint_words",
            "meaning": "s0 与 s* 继承上游 primitive witness CRT coordinate atom 的端点 residue word。",
        },
        {
            "field": "distinctness_guard",
            "meaning": "s0!=s* 时为两点模板；s0=s* 时回流 singleton/zero stencil 出口。",
        },
        {
            "field": "scaled_stencil",
            "meaning": "A k=A(delta_{s0}-delta_{s*})=W。",
        },
        {
            "field": "no_matrix_abstraction",
            "meaning": "不再依赖匿名矩阵列；剩余只依赖两个命名端点单位坐标。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 incidence-column Kronecker stencil 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeTransportEdgeIncidenceColumnImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange transport-edge incidence-column circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeIncidenceColumnImportedForKroneckerStencil",
            True,
            True,
            "导入 b_e=[s0]-[s*]、B[:,e]=b_e、f_e=A、Bf=W。",
            COLUMN_IMPORT,
        ),
        row(
            "PhaseResidueExchangeRootKroneckerDeltaCoordinate",
            True,
            True,
            "定义 root 端单位坐标 delta_{s0}。",
            ROOT_DELTA,
        ),
        row(
            "PhaseResidueExchangeSourceKroneckerDeltaCoordinate",
            True,
            True,
            "定义 source 端单位坐标 delta_{s*}。",
            SOURCE_DELTA,
        ),
        row(
            "PhaseResidueExchangeKroneckerDeltaDifferenceStencil",
            True,
            True,
            "把 incidence column 写成 k=delta_{s0}-delta_{s*}。",
            SIGNED_STENCIL,
        ),
        row(
            "PhaseResidueExchangeKroneckerStencilSignedCoefficient",
            True,
            True,
            "模板系数为 root:+1、source:-1、其余坐标 0。",
            STENCIL_SIGNS,
        ),
        row(
            "PhaseResidueExchangeKroneckerStencilEndpointCRTCoordinate",
            True,
            True,
            "两个端点继承上游 primitive witness CRT coordinate atom 的 CRT residue word。",
            CRT_ENDPOINTS,
        ),
        row(
            "PhaseResidueExchangeRootSourceCoordinateDistinctOrSingletonExit",
            True,
            True,
            "若 s0=s* 则模板为零并回流 singleton/degenerate 出口；否则保留两点模板。",
            DISTINCT_OR_SINGLETON,
        ),
        row(
            "PhaseResidueExchangeKroneckerStencilZeroSum",
            True,
            True,
            "sum_v(delta_{s0}(v)-delta_{s*}(v))=0。",
            STENCIL_ZERO_SUM,
        ),
        row(
            "PhaseResidueExchangeIncidenceColumnEqualsKroneckerStencil",
            True,
            True,
            "incidence column b_e 与 Kronecker difference stencil 完全相同。",
            COLUMN_EQUALS_STENCIL,
        ),
        row(
            "PhaseResidueExchangeKroneckerStencilFluxScaling",
            True,
            True,
            "A(delta_{s0}-delta_{s*})=A([s0]-[s*])=W，且 A>=|Lambda(D)|/2。",
            FLUX_SCALING,
        ),
        row(
            "PhaseResidueNoAnonymousBoundaryMatrixColumnAfterKroneckerStencil",
            True,
            True,
            "矩阵列口径被删除；剩余只是一对命名端点单位坐标的符号差。",
            NO_MATRIX,
        ),
        row(
            "PhaseResidueExchangeIncidenceColumnKroneckerStencilPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange incidence-column Kronecker-stencil circuit PDEC/cap。",
            STENCIL_PACKET,
        ),
        row(
            "NoAnonymousTransportEdgeIncidenceColumnAfterKroneckerStencil",
            True,
            True,
            "transport-edge incidence column 被压成 Kronecker endpoint stencil。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeIncidenceColumnKroneckerStencil",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeIncidenceColumnKroneckerStencilStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、Kronecker-stencil、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange incidence-column Kronecker-stencil circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 incidence-column Kronecker stencil 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange transport-edge incidence column 已把剩余写成 b_e=[s0]-[s*]、f_e=A。"
        "本步删除矩阵列抽象，把 b_e 写成两个端点单位坐标的差：k=delta_{s0}-delta_{s*}。"
        "两个端点继承上游 primitive witness CRT coordinate atom 的 residue word，"
        "乘以通量后 A k=A(delta_{s0}-delta_{s*})=W。"
        "剩余反例不再是匿名 boundary-matrix column，而必须表现为 incidence-column Kronecker-stencil circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_incidence_column_kronecker_stencil_router",
        "status": "phase_residue_exchange_transport_edge_incidence_column_reduced_to_kronecker_stencil_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "incidence_column_kronecker_stencil_records": stencil_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_transport_edge_incidence_column_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_incidence_column_imported_for_kronecker_stencil": True,
        "phase_residue_exchange_root_kronecker_delta_coordinate_closed": True,
        "phase_residue_exchange_source_kronecker_delta_coordinate_closed": True,
        "phase_residue_exchange_kronecker_delta_difference_stencil_closed": True,
        "phase_residue_exchange_kronecker_stencil_signed_coefficient_closed": True,
        "phase_residue_exchange_kronecker_stencil_endpoint_crt_coordinate_closed": True,
        "phase_residue_exchange_root_source_coordinate_distinct_or_singleton_exit_closed": True,
        "phase_residue_exchange_kronecker_stencil_zero_sum_closed": True,
        "phase_residue_exchange_incidence_column_equals_kronecker_stencil_closed": True,
        "phase_residue_exchange_kronecker_stencil_flux_scaling_closed": True,
        "phase_residue_no_anonymous_boundary_matrix_column_after_kronecker_stencil_closed": True,
        "phase_residue_exchange_incidence_column_kronecker_stencil_packet_registered": True,
        "anonymous_transport_edge_incidence_column_removed_after_kronecker_stencil": True,
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
        "phase_residue_exchange_incidence_column_kronecker_stencil_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange incidence-column Kronecker stencil 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_transport_edge_incidence_column_imported={fmt_bool(cert['phase_residue_exchange_transport_edge_incidence_column_imported'])}",
        f"phase_residue_exchange_root_kronecker_delta_coordinate_closed={fmt_bool(cert['phase_residue_exchange_root_kronecker_delta_coordinate_closed'])}",
        f"phase_residue_exchange_source_kronecker_delta_coordinate_closed={fmt_bool(cert['phase_residue_exchange_source_kronecker_delta_coordinate_closed'])}",
        f"phase_residue_exchange_kronecker_delta_difference_stencil_closed={fmt_bool(cert['phase_residue_exchange_kronecker_delta_difference_stencil_closed'])}",
        f"phase_residue_exchange_kronecker_stencil_signed_coefficient_closed={fmt_bool(cert['phase_residue_exchange_kronecker_stencil_signed_coefficient_closed'])}",
        f"phase_residue_exchange_kronecker_stencil_endpoint_crt_coordinate_closed={fmt_bool(cert['phase_residue_exchange_kronecker_stencil_endpoint_crt_coordinate_closed'])}",
        f"phase_residue_exchange_incidence_column_equals_kronecker_stencil_closed={fmt_bool(cert['phase_residue_exchange_incidence_column_equals_kronecker_stencil_closed'])}",
        f"phase_residue_exchange_kronecker_stencil_flux_scaling_closed={fmt_bool(cert['phase_residue_exchange_kronecker_stencil_flux_scaling_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_incidence_column_kronecker_stencil_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_incidence_column_kronecker_stencil_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. incidence column 输入",
        "",
        "上一层给出单列边界矩阵坐标：",
        "",
        "```text",
        "b_e=[s0]-[s*]",
        "B[:,e]=b_e",
        "f_e=A",
        "B f = A b_e = W",
        "```",
        "",
        "本证书继续不证明 `Lambda` 的存在，只处理已导入 incidence column 的端点模板化。",
        "",
        "## 2. Kronecker endpoint stencil",
        "",
        "定义端点单位坐标：",
        "",
        "```text",
        "delta_{s0}(v)=1 if v=s0, else 0",
        "delta_{s*}(v)=1 if v=s*, else 0",
        "k=delta_{s0}-delta_{s*}",
        "```",
        "",
        "于是：",
        "",
        "```text",
        "b_e=k",
        "A k=A(delta_{s0}-delta_{s*})=A([s0]-[s*])=W",
        "```",
        "",
        "## 3. CRT 端点字段",
        "",
        "两个端点不再是匿名矩阵坐标，而继承上游 primitive witness CRT coordinate atom：",
        "",
        "```text",
        "root_crt_word=crt(s0)",
        "source_crt_word=crt(s*)",
        "stencil=(+1 at root_crt_word) + (-1 at source_crt_word)",
        "```",
        "",
        "若 `s0=s*`，模板为零并回流 singleton/degenerate 出口；否则保留两点 signed stencil。",
        "",
        "## 4. incidence-column Kronecker stencil 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["incidence_column_kronecker_stencil_records"]:
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
            "- 本证书没有证明 phase-residue exchange incidence-column Kronecker-stencil circuit PDEC/cap。",
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
    print("phase_residue_exchange_incidence_column_kronecker_stencil_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
