#!/usr/bin/env python3
"""生成 phase-residue exchange cut-potential dual-norm saturation 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_cut_potential_dual_norm_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.json

输出：
  data/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-cut-potential-dual-norm"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCutPotentialCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeCutPotentialDualNormSaturationCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCutPotentialImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeCutPotentialDualNormLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeCutPotentialDualNormLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCutPotentialDualNormLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCutPotentialDualNormLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCutPotentialDualNormLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCutPotentialDualNormLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeCutPotentialDualNormLedger"
CUT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialImportedForDualNormLedger"
DIV_L1 = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialDivergenceL1NormLedger"
POT_LINF = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialLInfinityNormLedger"
HOLDER_BOUND = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialHolderDualBoundLedger"
PAIRING_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialPairingValueLedger"
DUAL_SAT = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialDualNormSaturationLedger"
POLAR_SIGN = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialPolarSignAlignmentLedger"
EXTREMAL_SUPPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialExtremalSupportLedger"
EQUALS_CUT = "StableLadderEndpointOrbitPhaseResidueExchangeDualNormEqualsCutPotentialLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeDualNormCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeDualNormOrientationLedger"
NO_CUT = "StableLadderEndpointOrbitPhaseResidueNoAnonymousCutPotentialAfterDualNormLedger"
DUAL_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialDualNormPacketLedger"
NO_ANON = "NoAnonymousCutPotentialAfterDualNormLedger"


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
    """把 cut-potential 硬点替换为 dual-norm saturation 硬点。"""
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
        CUT_IMPORT,
        DIV_L1,
        POT_LINF,
        HOLDER_BOUND,
        PAIRING_VALUE,
        DUAL_SAT,
        POLAR_SIGN,
        EXTREMAL_SUPPORT,
        EQUALS_CUT,
        COLLISION_EXIT,
        ORIENTATION,
        NO_CUT,
        DUAL_PACKET,
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


def dual_norm_records() -> list[dict[str, str]]:
    """给出对偶范数饱和字段。"""
    return [
        {
            "field": "divergence_l1_norm",
            "meaning": "二点散度满足 ||div||_1=|+A|+|-A|=2A。",
        },
        {
            "field": "potential_l_infinity_norm",
            "meaning": "规范化势函数满足 ||phi||_infty=1/2。",
        },
        {
            "field": "holder_dual_bound",
            "meaning": "Hölder 对偶界给出 <div,phi> <= ||div||_1 ||phi||_infty=A。",
        },
        {
            "field": "pairing_value",
            "meaning": "直接配对值为 <div,phi>=A。",
        },
        {
            "field": "dual_norm_saturation",
            "meaning": "配对达到 L1-Linfty 对偶界等号。",
        },
        {
            "field": "polar_sign_alignment",
            "meaning": "div 与 phi 在两个端点同号极化：正端匹配正势，负端匹配负势。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r*，L1 质量与势差退化并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 cut-potential dual-norm saturation 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeKirchhoffCellCutPotentialImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange endpoint charge Kirchhoff cell cut-potential circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "同点退化或对偶质量为零时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeCutPotentialImportedForDualNorm",
            True,
            True,
            "导入 phi(r0)=+1/2、phi(r*)=-1/2、<div,phi>=A。",
            CUT_IMPORT,
        ),
        row(
            "PhaseResidueExchangeCutPotentialDivergenceL1Norm",
            True,
            True,
            "散度 L1 范数为 |+A|+|-A|=2A。",
            DIV_L1,
        ),
        row(
            "PhaseResidueExchangeCutPotentialLInfinityNorm",
            True,
            True,
            "势函数 L_infty 范数为 1/2。",
            POT_LINF,
        ),
        row(
            "PhaseResidueExchangeCutPotentialHolderDualBound",
            True,
            True,
            "L1-Linfty Hölder 对偶界给出 <div,phi> <= A。",
            HOLDER_BOUND,
        ),
        row(
            "PhaseResidueExchangeCutPotentialPairingValue",
            True,
            True,
            "直接计算配对值为 <div,phi>=A。",
            PAIRING_VALUE,
        ),
        row(
            "PhaseResidueExchangeCutPotentialDualNormSaturation",
            True,
            True,
            "配对等于对偶界，形成 dual-norm saturation 证书。",
            DUAL_SAT,
        ),
        row(
            "PhaseResidueExchangeCutPotentialPolarSignAlignment",
            True,
            True,
            "正散度在正势极点，负散度在负势极点，Hölder 等号条件闭合。",
            POLAR_SIGN,
        ),
        row(
            "PhaseResidueExchangeCutPotentialExtremalSupport",
            True,
            True,
            "全部散度质量都落在 |phi|=||phi||_infty 的端点上。",
            EXTREMAL_SUPPORT,
        ),
        row(
            "PhaseResidueExchangeDualNormEqualsCutPotential",
            True,
            True,
            "dual-norm saturation 证书与上一层 cut-potential 表示同一局部对象。",
            EQUALS_CUT,
        ),
        row(
            "PhaseResidueExchangeDualNormCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r*，对偶范数证书退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeDualNormOrientation",
            True,
            True,
            "方向仍由正散度/正势端指向负散度/负势端的极化差固定为 source -> root。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousCutPotentialAfterDualNorm",
            True,
            True,
            "cut-potential 口径被删除；剩余是命名对偶范数等号饱和证书。",
            NO_CUT,
        ),
        row(
            "PhaseResidueExchangeCutPotentialDualNormPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange cut-potential dual-norm saturation circuit PDEC/cap。",
            DUAL_PACKET,
        ),
        row(
            "NoAnonymousCutPotentialAfterDualNorm",
            True,
            True,
            "规范化 cut-potential 被压成 L1-Linfty 对偶等号饱和包。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeCutPotentialDualNorm",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeCutPotentialDualNormStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、dual-norm saturation、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange cut-potential dual-norm saturation circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 cut-potential dual-norm saturation 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange Kirchhoff cell cut-potential 已把剩余写成 "
        "phi(r0)=+1/2、phi(r*)=-1/2、phi(r0)+phi(r*)=0、phi(r0)-phi(r*)=1、"
        "<div,phi>=A、A C_Pi=W。"
        "本步删除 cut-potential 作为黑箱的口径，把非退化对象登记为 L1-Linfty 对偶范数等号饱和："
        "||div||_1=2A、||phi||_infty=1/2、||div||_1||phi||_infty=A、<div,phi>=A。"
        "因此 Hölder 对偶界被精确饱和，正散度落在正势极点，负散度落在负势极点。"
        "若 r0=r*，散度质量与势差退化并回流 singleton/degenerate 出口。"
        "剩余反例不再是匿名 cut-potential，而必须表现为 cut-potential dual-norm saturation "
        "circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_cut_potential_dual_norm_router",
        "status": "phase_residue_exchange_cut_potential_reduced_to_dual_norm_saturation_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "cut_potential_dual_norm_records": dual_norm_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_kirchhoff_cell_cut_potential_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_cut_potential_imported_for_dual_norm": True,
        "phase_residue_exchange_cut_potential_divergence_l1_norm_closed": True,
        "phase_residue_exchange_cut_potential_l_infinity_norm_closed": True,
        "phase_residue_exchange_cut_potential_holder_dual_bound_closed": True,
        "phase_residue_exchange_cut_potential_pairing_value_closed": True,
        "phase_residue_exchange_cut_potential_dual_norm_saturation_closed": True,
        "phase_residue_exchange_cut_potential_polar_sign_alignment_closed": True,
        "phase_residue_exchange_cut_potential_extremal_support_closed": True,
        "phase_residue_exchange_dual_norm_equals_cut_potential_closed": True,
        "phase_residue_exchange_dual_norm_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_dual_norm_orientation_closed": True,
        "phase_residue_no_anonymous_cut_potential_after_dual_norm_closed": True,
        "phase_residue_exchange_cut_potential_dual_norm_packet_registered": True,
        "anonymous_cut_potential_removed_after_dual_norm": True,
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
        "phase_residue_exchange_endpoint_charge_kirchhoff_cell_cut_potential_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_cut_potential_dual_norm_saturation_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange cut-potential dual-norm saturation 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_kirchhoff_cell_cut_potential_imported={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_cut_potential_imported'])}",
        f"phase_residue_exchange_cut_potential_divergence_l1_norm_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_divergence_l1_norm_closed'])}",
        f"phase_residue_exchange_cut_potential_l_infinity_norm_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_l_infinity_norm_closed'])}",
        f"phase_residue_exchange_cut_potential_holder_dual_bound_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_holder_dual_bound_closed'])}",
        f"phase_residue_exchange_cut_potential_pairing_value_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_pairing_value_closed'])}",
        f"phase_residue_exchange_cut_potential_dual_norm_saturation_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_dual_norm_saturation_closed'])}",
        f"phase_residue_exchange_cut_potential_polar_sign_alignment_closed={fmt_bool(cert['phase_residue_exchange_cut_potential_polar_sign_alignment_closed'])}",
        f"phase_residue_exchange_dual_norm_collision_or_singleton_exit_closed={fmt_bool(cert['phase_residue_exchange_dual_norm_collision_or_singleton_exit_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_cut_potential_dual_norm_saturation_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_cut_potential_dual_norm_saturation_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. cut-potential 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "phi(r0)=+1/2",
        "phi(r*)=-1/2",
        "phi(r0)+phi(r*)=0",
        "phi(r0)-phi(r*)=1",
        "<div,phi>=A",
        "A C_Pi=W",
        "```",
        "",
        "## 2. dual-norm saturation 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["cut_potential_dual_norm_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时对偶范数证书为：",
            "",
            "```text",
            "||div||_1=|+A|+|-A|=2A",
            "||phi||_infty=1/2",
            "||div||_1 ||phi||_infty=A",
            "<div,phi>=(+A)(+1/2)+(-A)(-1/2)=A",
            "<div,phi>=||div||_1 ||phi||_infty",
            "sign(div(r0))=sign(phi(r0))=+",
            "sign(div(r*))=sign(phi(r*))=-",
            "A C_Pi=W",
            "```",
            "",
            "若 `r0=r*`，则势差与对偶质量退化并回流 singleton/degenerate 出口。",
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
            "- 本证书没有证明 phase-residue exchange cut-potential dual-norm saturation circuit PDEC/cap。",
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
    print("phase_residue_exchange_cut_potential_dual_norm_saturation_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
