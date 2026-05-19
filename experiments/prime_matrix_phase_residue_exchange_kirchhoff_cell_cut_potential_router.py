#!/usr/bin/env python3
"""生成 phase-residue exchange Kirchhoff cell cut-potential 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_kirchhoff_cell_cut_potential_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.json

输出：
  data/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCutPotentialCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeKirchhoffCellImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeKirchhoffCellCutPotentialLedger"
CELL_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellImportedForCutPotentialLedger"
SUPPORT = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialSupportLedger"
VALUES = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialValuesLedger"
ZERO_MEAN = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialZeroMeanLedger"
OSCILLATION = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialUnitOscillationLedger"
PAIRING = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialDivergencePairingLedger"
NORMALIZATION = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialNormalizationLedger"
EQUALS_CELL = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialEqualsKirchhoffCellLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialOrientationLedger"
NO_CELL = "StableLadderEndpointOrbitPhaseResidueNoAnonymousKirchhoffCellAfterCutPotentialLedger"
CUT_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialPacketLedger"
NO_ANON = "NoAnonymousKirchhoffCellAfterCutPotentialLedger"


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
    """把 Kirchhoff cell 硬点替换为 cut-potential 硬点。"""
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
        CELL_IMPORT,
        SUPPORT,
        VALUES,
        ZERO_MEAN,
        OSCILLATION,
        PAIRING,
        NORMALIZATION,
        EQUALS_CELL,
        COLLISION_EXIT,
        ORIENTATION,
        NO_CELL,
        CUT_PACKET,
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


def cut_potential_records() -> list[dict[str, str]]:
    """给出规范化 cut-potential 的字段。"""
    return [
        {
            "field": "cut_potential_support",
            "meaning": "势函数只支撑在非退化二点单元 K={r0,r*} 上。",
        },
        {
            "field": "root_potential",
            "meaning": "root word r0 的规范化势值为 phi(r0)=+1/2。",
        },
        {
            "field": "source_potential",
            "meaning": "source word r* 的规范化势值为 phi(r*)=-1/2。",
        },
        {
            "field": "zero_mean",
            "meaning": "二点均值为 0，即 phi(r0)+phi(r*)=0。",
        },
        {
            "field": "unit_oscillation",
            "meaning": "从 source 到 root 的势差为 phi(r0)-phi(r*)=1。",
        },
        {
            "field": "divergence_pairing",
            "meaning": "Kirchhoff 散度与势函数的配对为 <div,phi>=A。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r*，势差退化为 0 并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 Kirchhoff cell cut-potential 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeEndpointChargeKirchhoffCellImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange endpoint charge Kirchhoff cell circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "同点退化或势差为零时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellImportedForCutPotential",
            True,
            True,
            "导入 K={r0,r*}、div(r0)=+A、div(r*)=-A、sum_K div=0。",
            CELL_IMPORT,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialSupport",
            True,
            True,
            "规范化 cut-potential 只支撑在二点 cell K 上。",
            SUPPORT,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialValues",
            True,
            True,
            "势值固定为 phi(r0)=+1/2、phi(r*)=-1/2。",
            VALUES,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialZeroMean",
            True,
            True,
            "二点势函数满足 phi(r0)+phi(r*)=0。",
            ZERO_MEAN,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialUnitOscillation",
            True,
            True,
            "source -> root 势差被规范化为 1。",
            OSCILLATION,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialDivergencePairing",
            True,
            True,
            "散度与 cut-potential 的配对为 A，给出正配对证书。",
            PAIRING,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialNormalization",
            True,
            True,
            "势函数具有零均值、单位振荡和 L_infty 半幅 1/2 的规范化。",
            NORMALIZATION,
        ),
        row(
            "PhaseResidueExchangeCutPotentialEqualsKirchhoffCell",
            True,
            True,
            "cut-potential 证书与上一层 Kirchhoff cell 表示同一局部散度单元。",
            EQUALS_CELL,
        ),
        row(
            "PhaseResidueExchangeCutPotentialCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r*，势差与散度配对退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeCutPotentialOrientation",
            True,
            True,
            "方向仍记录为 source -> root，由势差 phi(root)-phi(source)>0 固定。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousKirchhoffCellAfterCutPotential",
            True,
            True,
            "Kirchhoff cell 口径被删除；剩余是命名 cut-potential 配对证书。",
            NO_CELL,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange endpoint charge Kirchhoff cell cut-potential circuit PDEC/cap。",
            CUT_PACKET,
        ),
        row(
            "NoAnonymousKirchhoffCellAfterCutPotential",
            True,
            True,
            "二点 Kirchhoff cell 被压成规范化势函数及其正散度配对。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeKirchhoffCellCutPotential",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、cut-potential、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange endpoint charge Kirchhoff cell cut-potential circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 Kirchhoff cell cut-potential 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange endpoint charge Kirchhoff cell 已把剩余写成 "
        "K={r0,r*}、div(r0)=+A、div(r*)=-A、sum_K div=0、positive_divergence=negative_divergence=A、"
        "total_boundary_variation=2A、A C_Pi=W。"
        "本步删除 Kirchhoff cell 作为黑箱的口径，把非退化对象登记为规范化 cut-potential："
        "phi(r0)=+1/2、phi(r*)=-1/2、phi(r0)+phi(r*)=0、phi(r0)-phi(r*)=1，"
        "并给出正配对 <div,phi>=A。若 r0=r*，势差退化并回流 singleton/degenerate 出口。"
        "剩余反例不再是匿名二点 Kirchhoff cell，而必须表现为 endpoint charge Kirchhoff cell "
        "cut-potential circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_kirchhoff_cell_cut_potential_router",
        "status": "phase_residue_exchange_kirchhoff_cell_reduced_to_cut_potential_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "kirchhoff_cell_cut_potential_records": cut_potential_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_endpoint_charge_kirchhoff_cell_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_kirchhoff_cell_imported_for_cut_potential": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_support_closed": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_values_closed": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_zero_mean_closed": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_unit_oscillation_closed": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_divergence_pairing_closed": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_normalization_closed": True,
        "phase_residue_exchange_cut_potential_equals_kirchhoff_cell_closed": True,
        "phase_residue_exchange_cut_potential_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_cut_potential_orientation_closed": True,
        "phase_residue_no_anonymous_kirchhoff_cell_after_cut_potential_closed": True,
        "phase_residue_exchange_kirchhoff_cell_cut_potential_packet_registered": True,
        "anonymous_kirchhoff_cell_removed_after_cut_potential": True,
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
        "phase_residue_exchange_endpoint_charge_kirchhoff_cell_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_endpoint_charge_kirchhoff_cell_cut_potential_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange Kirchhoff cell cut-potential 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_endpoint_charge_kirchhoff_cell_imported={fmt_bool(cert['phase_residue_exchange_endpoint_charge_kirchhoff_cell_imported'])}",
        f"phase_residue_exchange_kirchhoff_cell_cut_potential_support_closed={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_cut_potential_support_closed'])}",
        f"phase_residue_exchange_kirchhoff_cell_cut_potential_values_closed={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_cut_potential_values_closed'])}",
        f"phase_residue_exchange_kirchhoff_cell_cut_potential_zero_mean_closed={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_cut_potential_zero_mean_closed'])}",
        f"phase_residue_exchange_kirchhoff_cell_cut_potential_unit_oscillation_closed={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_cut_potential_unit_oscillation_closed'])}",
        f"phase_residue_exchange_kirchhoff_cell_cut_potential_divergence_pairing_closed={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_cut_potential_divergence_pairing_closed'])}",
        f"phase_residue_exchange_cut_potential_collision_or_singleton_exit_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_collision_or_singleton_exit_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_endpoint_charge_kirchhoff_cell_cut_potential_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_endpoint_charge_kirchhoff_cell_cut_potential_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Kirchhoff cell 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "K={r0,r*}",
        "div(r0)=+A",
        "div(r*)=-A",
        "sum_K div=0",
        "positive_divergence=A",
        "negative_divergence=A",
        "total_boundary_variation=2A",
        "A C_Pi=W",
        "```",
        "",
        "## 2. cut-potential 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["kirchhoff_cell_cut_potential_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时规范化 cut-potential 为：",
            "",
            "```text",
            "phi(r0)=+1/2",
            "phi(r*)=-1/2",
            "phi(r0)+phi(r*)=0",
            "phi(r0)-phi(r*)=1",
            "<div,phi>=(+A)(+1/2)+(-A)(-1/2)=A",
            "A C_Pi=W",
            "```",
            "",
            "若 `r0=r*`，则势差退化为 `0` 并回流 singleton/degenerate 出口。",
            "",
            "## 3. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
            "```",
            "",
            "## 4. 判定表",
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
            "## 5. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange endpoint charge Kirchhoff cell cut-potential circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 7. 依赖哈希",
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
    print("phase_residue_exchange_endpoint_charge_kirchhoff_cell_cut_potential_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
