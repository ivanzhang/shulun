#!/usr/bin/env python3
"""生成 phase-residue exchange centered root-source score dipole 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_centered_root_source_score_dipole_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.json

输出：
  data/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-centered-root-source-score-dipole"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeOrientedRootSourceWitnessGapCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeCenteredRootSourceScoreDipoleCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedRootSourceWitnessGapImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeCenteredRootSourceScoreDipoleLedger"
GAP_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedWitnessGapImportedForCenteredScoreDipoleLedger"
MIDPOINT = "StableLadderEndpointOrbitPhaseResidueExchangeWitnessScoreMidpointLedger"
CENTERING = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourceScoreCenteringLedger"
ROOT_HALF = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredRootHalfGapSurplusLedger"
SOURCE_HALF = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredSourceHalfGapDeficitLedger"
ZERO_MEAN = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredTwoPointScoreZeroMeanLedger"
HALF_BOUND = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredHalfGapLowerBoundLedger"
TRANSLATION_REMOVED = "StableLadderEndpointOrbitPhaseResidueNoAnonymousCommonScoreOffsetAfterCenteringLedger"
DIPOLE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredRootSourceScoreDipolePacketLedger"
NO_ANON = "NoAnonymousOrientedRootSourceWitnessGapAfterCenteredScoreDipoleLedger"


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
    """把 oriented witness gap 硬点替换为 centered score dipole 硬点。"""
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
        GAP_IMPORT,
        MIDPOINT,
        CENTERING,
        ROOT_HALF,
        SOURCE_HALF,
        ZERO_MEAN,
        HALF_BOUND,
        TRANSLATION_REMOVED,
        DIPOLE_PACKET,
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


def dipole_records() -> list[dict[str, str]]:
    """给出 centered root-source score dipole 的字段。"""
    return [
        {
            "field": "root_score",
            "meaning": "根端分数 R=sigma*Lambda([s0])。",
        },
        {
            "field": "source_score",
            "meaning": "源端分数 T=sigma*Lambda([s*])。",
        },
        {
            "field": "midpoint",
            "meaning": "共同中点 M=(R+T)/2，用于去掉公共分数偏移。",
        },
        {
            "field": "centered_root_surplus",
            "meaning": "根端中心化剩余 U=R-M=G/2。",
        },
        {
            "field": "centered_source_deficit",
            "meaning": "源端中心化亏缺 V=T-M=-G/2。",
        },
        {
            "field": "zero_mean_dipole",
            "meaning": "两点中心化分数满足 U+V=0 且 U-V=G。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 centered root-source score dipole 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeOrientedRootSourceWitnessGapImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange oriented root-source witness gap circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeOrientedWitnessGapImportedForCenteredScoreDipole",
            True,
            True,
            "导入 R、T、G=R-T 以及 G>=|Lambda(D)|。",
            GAP_IMPORT,
        ),
        row(
            "PhaseResidueExchangeWitnessScoreMidpoint",
            True,
            True,
            "定义共同中点 M=(R+T)/2。",
            MIDPOINT,
        ),
        row(
            "PhaseResidueExchangeRootSourceScoreCentering",
            True,
            True,
            "把两端分数改写成 R=M+G/2 与 T=M-G/2。",
            CENTERING,
        ),
        row(
            "PhaseResidueExchangeCenteredRootHalfGapSurplus",
            True,
            True,
            "根端中心化剩余 U=R-M=G/2。",
            ROOT_HALF,
        ),
        row(
            "PhaseResidueExchangeCenteredSourceHalfGapDeficit",
            True,
            True,
            "源端中心化亏缺 V=T-M=-G/2。",
            SOURCE_HALF,
        ),
        row(
            "PhaseResidueExchangeCenteredTwoPointScoreZeroMean",
            True,
            True,
            "两点中心化分数满足 U+V=0，公共偏移已消去。",
            ZERO_MEAN,
        ),
        row(
            "PhaseResidueExchangeCenteredHalfGapLowerBound",
            True,
            True,
            "由 G>=|Lambda(D)| 得 U=G/2>=|Lambda(D)|/2，且 -V 同界。",
            HALF_BOUND,
        ),
        row(
            "PhaseResidueNoAnonymousCommonScoreOffsetAfterCentering",
            True,
            True,
            "oriented gap 不再携带匿名公共分数偏移；只剩零均值两点偶极。",
            TRANSLATION_REMOVED,
        ),
        row(
            "PhaseResidueExchangeCenteredRootSourceScoreDipolePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange centered root-source score dipole circuit PDEC/cap。",
            DIPOLE_PACKET,
        ),
        row(
            "NoAnonymousOrientedRootSourceWitnessGapAfterCenteredScoreDipole",
            True,
            True,
            "oriented root-source witness gap 被压成中心化两点 score dipole。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeCenteredRootSourceScoreDipole",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeCenteredRootSourceScoreDipoleStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、centered score dipole、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange centered root-source score dipole circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 centered root-source score dipole 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange oriented root-source witness gap 已把单对见证写成 G=R-T。"
        "本步取共同中点 M=(R+T)/2，把两端分数中心化为 "
        "U=R-M=G/2 与 V=T-M=-G/2。"
        "于是 U+V=0，且 U>=|Lambda(D)|/2；若平均见证非零，则 U>0、V<0。"
        "剩余反例不再含匿名公共分数偏移，而必须表现为 centered root-source score dipole circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_centered_root_source_score_dipole_router",
        "status": "phase_residue_exchange_oriented_root_source_witness_gap_reduced_to_centered_root_source_score_dipole_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "centered_root_source_score_dipole_records": dipole_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_oriented_root_source_witness_gap_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_oriented_witness_gap_imported_for_centered_score_dipole": True,
        "phase_residue_exchange_witness_score_midpoint_closed": True,
        "phase_residue_exchange_root_source_score_centering_closed": True,
        "phase_residue_exchange_centered_root_half_gap_surplus_closed": True,
        "phase_residue_exchange_centered_source_half_gap_deficit_closed": True,
        "phase_residue_exchange_centered_two_point_score_zero_mean_closed": True,
        "phase_residue_exchange_centered_half_gap_lower_bound_closed": True,
        "phase_residue_no_anonymous_common_score_offset_after_centering_closed": True,
        "phase_residue_exchange_centered_root_source_score_dipole_packet_registered": True,
        "anonymous_oriented_root_source_witness_gap_removed_after_centering": True,
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
        "phase_residue_exchange_centered_root_source_score_dipole_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange centered root-source score dipole 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_oriented_root_source_witness_gap_imported={fmt_bool(cert['phase_residue_exchange_oriented_root_source_witness_gap_imported'])}",
        f"phase_residue_exchange_witness_score_midpoint_closed={fmt_bool(cert['phase_residue_exchange_witness_score_midpoint_closed'])}",
        f"phase_residue_exchange_root_source_score_centering_closed={fmt_bool(cert['phase_residue_exchange_root_source_score_centering_closed'])}",
        f"phase_residue_exchange_centered_two_point_score_zero_mean_closed={fmt_bool(cert['phase_residue_exchange_centered_two_point_score_zero_mean_closed'])}",
        f"phase_residue_exchange_centered_half_gap_lower_bound_closed={fmt_bool(cert['phase_residue_exchange_centered_half_gap_lower_bound_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_centered_root_source_score_dipole_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_centered_root_source_score_dipole_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. oriented gap 输入",
        "",
        "上一层给出两个端点分数和有向差值：",
        "",
        "```text",
        "R = sigma * Lambda([s0])",
        "T = sigma * Lambda([s*])",
        "G = R - T >= |Lambda(D)|",
        "```",
        "",
        "本证书继续不证明 `Lambda` 的存在，只处理已导入见证后的代数归约。",
        "",
        "## 2. 中点中心化",
        "",
        "定义共同中点：",
        "",
        "```text",
        "M = (R + T) / 2",
        "```",
        "",
        "于是两端分数可无损改写为：",
        "",
        "```text",
        "R = M + G/2",
        "T = M - G/2",
        "```",
        "",
        "## 3. 零均值两点偶极",
        "",
        "定义中心化两点分数：",
        "",
        "```text",
        "U = R - M = G/2",
        "V = T - M = -G/2",
        "```",
        "",
        "因此：",
        "",
        "```text",
        "U + V = 0",
        "U - V = G",
        "U >= |Lambda(D)|/2",
        "```",
        "",
        "若平均见证非零，则 `U>0` 且 `V<0`。公共分数偏移 `M` 不再是剩余硬点的一部分。",
        "",
        "## 4. centered root-source score dipole 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["centered_root_source_score_dipole_records"]:
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
            "- 本证书没有证明 phase-residue exchange centered root-source score dipole circuit PDEC/cap。",
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
    print("phase_residue_exchange_centered_root_source_score_dipole_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
