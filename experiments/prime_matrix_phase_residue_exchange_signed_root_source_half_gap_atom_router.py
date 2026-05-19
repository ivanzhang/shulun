#!/usr/bin/env python3
"""生成 phase-residue exchange signed root-source half-gap atom 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_signed_root_source_half_gap_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.json

输出：
  data/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeCenteredRootSourceScoreDipoleCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeSignedRootSourceHalfGapAtomCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredRootSourceScoreDipoleImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeSignedRootSourceHalfGapAtomLedger"
CENTERED_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCenteredScoreDipoleImportedForHalfGapAtomLedger"
HALF_AMPLITUDE = "StableLadderEndpointOrbitPhaseResidueExchangeHalfGapAmplitudeLedger"
HALF_LOWER_BOUND = "StableLadderEndpointOrbitPhaseResidueExchangeHalfGapAmplitudeLowerBoundLedger"
SIGNED_SUPPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRootPositiveSourceNegativeSupportLedger"
ATOM_FACTORIZATION = "StableLadderEndpointOrbitPhaseResidueExchangeSignedHalfGapAtomFactorizationLedger"
ZERO_MASS = "StableLadderEndpointOrbitPhaseResidueExchangeSignedHalfGapAtomZeroMassLedger"
TOTAL_VARIATION = "StableLadderEndpointOrbitPhaseResidueExchangeSignedHalfGapAtomTotalVariationLedger"
NO_UNEQUAL = "StableLadderEndpointOrbitPhaseResidueNoAnonymousUnequalEndpointScoreAfterHalfGapAtomLedger"
ATOM_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeSignedRootSourceHalfGapAtomPacketLedger"
NO_ANON = "NoAnonymousCenteredRootSourceScoreDipoleAfterHalfGapAtomLedger"


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
    """把 centered score dipole 硬点替换为 signed half-gap atom 硬点。"""
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
        CENTERED_IMPORT,
        HALF_AMPLITUDE,
        HALF_LOWER_BOUND,
        SIGNED_SUPPORT,
        ATOM_FACTORIZATION,
        ZERO_MASS,
        TOTAL_VARIATION,
        NO_UNEQUAL,
        ATOM_PACKET,
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


def atom_records() -> list[dict[str, str]]:
    """给出 signed root-source half-gap atom 的字段。"""
    return [
        {
            "field": "half_gap_amplitude",
            "meaning": "正幅度 A=G/2。",
        },
        {
            "field": "signed_support",
            "meaning": "固定两点支撑：root 端 +1，source 端 -1。",
        },
        {
            "field": "signed_atom",
            "meaning": "中心化分数向量 W=A([s0]-[s*])。",
        },
        {
            "field": "zero_mass",
            "meaning": "符号原子净质量为 0。",
        },
        {
            "field": "total_variation",
            "meaning": "总变差 |A|+|-A|=2A=G。",
        },
        {
            "field": "lower_bound",
            "meaning": "A>=|Lambda(D)|/2；非零见证时 A>0。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 signed root-source half-gap atom 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeCenteredRootSourceScoreDipoleImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange centered root-source score dipole circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeCenteredScoreDipoleImportedForHalfGapAtom",
            True,
            True,
            "导入 U=G/2、V=-G/2、U+V=0 以及 G>=|Lambda(D)|。",
            CENTERED_IMPORT,
        ),
        row(
            "PhaseResidueExchangeHalfGapAmplitude",
            True,
            True,
            "定义正幅度 A=G/2=U=-V。",
            HALF_AMPLITUDE,
        ),
        row(
            "PhaseResidueExchangeHalfGapAmplitudeLowerBound",
            True,
            True,
            "由 G>=|Lambda(D)| 得 A>=|Lambda(D)|/2；非零见证时 A>0。",
            HALF_LOWER_BOUND,
        ),
        row(
            "PhaseResidueExchangeRootPositiveSourceNegativeSupport",
            True,
            True,
            "中心化两点支撑的符号固定为 root 端 +1、source 端 -1。",
            SIGNED_SUPPORT,
        ),
        row(
            "PhaseResidueExchangeSignedHalfGapAtomFactorization",
            True,
            True,
            "中心化分数向量无损分解为 W=A([s0]-[s*])。",
            ATOM_FACTORIZATION,
        ),
        row(
            "PhaseResidueExchangeSignedHalfGapAtomZeroMass",
            True,
            True,
            "符号原子净质量为 0。",
            ZERO_MASS,
        ),
        row(
            "PhaseResidueExchangeSignedHalfGapAtomTotalVariation",
            True,
            True,
            "总变差为 2A=G。",
            TOTAL_VARIATION,
        ),
        row(
            "PhaseResidueNoAnonymousUnequalEndpointScoreAfterHalfGapAtom",
            True,
            True,
            "剩余不再包含不等幅端点分数；只有正幅度乘固定符号原子。",
            NO_UNEQUAL,
        ),
        row(
            "PhaseResidueExchangeSignedRootSourceHalfGapAtomPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange signed root-source half-gap atom circuit PDEC/cap。",
            ATOM_PACKET,
        ),
        row(
            "NoAnonymousCenteredRootSourceScoreDipoleAfterHalfGapAtom",
            True,
            True,
            "centered root-source score dipole 被压成 signed half-gap atom。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeSignedRootSourceHalfGapAtom",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeSignedRootSourceHalfGapAtomStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、signed half-gap atom、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange signed root-source half-gap atom circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 signed root-source half-gap atom 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange centered root-source score dipole 已把剩余写成 U=G/2、V=-G/2。"
        "本步定义正幅度 A=G/2，并把中心化分数向量无损分解为 W=A([s0]-[s*])。"
        "该符号原子净质量为 0，总变差为 2A=G，且 A>=|Lambda(D)|/2。"
        "剩余反例不再含不等幅端点分数，而必须表现为 signed root-source half-gap atom circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_signed_root_source_half_gap_atom_router",
        "status": "phase_residue_exchange_centered_root_source_score_dipole_reduced_to_signed_root_source_half_gap_atom_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "signed_root_source_half_gap_atom_records": atom_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_centered_root_source_score_dipole_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_centered_score_dipole_imported_for_half_gap_atom": True,
        "phase_residue_exchange_half_gap_amplitude_closed": True,
        "phase_residue_exchange_half_gap_amplitude_lower_bound_closed": True,
        "phase_residue_exchange_root_positive_source_negative_support_closed": True,
        "phase_residue_exchange_signed_half_gap_atom_factorization_closed": True,
        "phase_residue_exchange_signed_half_gap_atom_zero_mass_closed": True,
        "phase_residue_exchange_signed_half_gap_atom_total_variation_closed": True,
        "phase_residue_no_anonymous_unequal_endpoint_score_after_half_gap_atom_closed": True,
        "phase_residue_exchange_signed_root_source_half_gap_atom_packet_registered": True,
        "anonymous_centered_root_source_score_dipole_removed_after_half_gap_atom": True,
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
        "phase_residue_exchange_signed_root_source_half_gap_atom_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange signed root-source half-gap atom 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_centered_root_source_score_dipole_imported={fmt_bool(cert['phase_residue_exchange_centered_root_source_score_dipole_imported'])}",
        f"phase_residue_exchange_half_gap_amplitude_closed={fmt_bool(cert['phase_residue_exchange_half_gap_amplitude_closed'])}",
        f"phase_residue_exchange_half_gap_amplitude_lower_bound_closed={fmt_bool(cert['phase_residue_exchange_half_gap_amplitude_lower_bound_closed'])}",
        f"phase_residue_exchange_root_positive_source_negative_support_closed={fmt_bool(cert['phase_residue_exchange_root_positive_source_negative_support_closed'])}",
        f"phase_residue_exchange_signed_half_gap_atom_factorization_closed={fmt_bool(cert['phase_residue_exchange_signed_half_gap_atom_factorization_closed'])}",
        f"phase_residue_exchange_signed_half_gap_atom_zero_mass_closed={fmt_bool(cert['phase_residue_exchange_signed_half_gap_atom_zero_mass_closed'])}",
        f"phase_residue_exchange_signed_half_gap_atom_total_variation_closed={fmt_bool(cert['phase_residue_exchange_signed_half_gap_atom_total_variation_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_signed_root_source_half_gap_atom_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_signed_root_source_half_gap_atom_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. centered score dipole 输入",
        "",
        "上一层给出中心化两点分数：",
        "",
        "```text",
        "U = G/2",
        "V = -G/2",
        "U + V = 0",
        "G >= |Lambda(D)|",
        "```",
        "",
        "本证书继续不证明 `Lambda` 的存在，只处理已导入见证后的代数原子化。",
        "",
        "## 2. 半 gap 幅度",
        "",
        "定义正幅度：",
        "",
        "```text",
        "A = G / 2 = U = -V",
        "```",
        "",
        "于是：",
        "",
        "```text",
        "A >= |Lambda(D)| / 2",
        "```",
        "",
        "若平均见证非零，则 `A>0`。",
        "",
        "## 3. 固定符号原子",
        "",
        "中心化分数向量可写成：",
        "",
        "```text",
        "W = A([s0]-[s*])",
        "```",
        "",
        "其中 root 端符号为 `+1`，source 端符号为 `-1`。该原子满足：",
        "",
        "```text",
        "mass(W) = 0",
        "TV(W) = 2A = G",
        "```",
        "",
        "因此剩余不再含不等幅端点分数，只剩一个正幅度乘固定符号支撑。",
        "",
        "## 4. signed root-source half-gap atom 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["signed_root_source_half_gap_atom_records"]:
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
            "- 本证书没有证明 phase-residue exchange signed root-source half-gap atom circuit PDEC/cap。",
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
    print("phase_residue_exchange_signed_root_source_half_gap_atom_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
