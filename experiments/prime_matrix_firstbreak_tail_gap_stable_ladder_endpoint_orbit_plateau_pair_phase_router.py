#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit plateau-pair phase 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_pair_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitOppositeSignPlateauRampPairImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauPairPhaseLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauPairPhaseLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauPairPhaseLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauPairPhaseLedger"
PAIR_MODEL = "StableLadderEndpointOrbitOppositeSignPlateauPairModelLedger"
GAP_DECOMP = "StableLadderEndpointOrbitPlateauPairCyclicGapDecompositionLedger"
GAP_SPLIT = "StableLadderEndpointOrbitPlateauPairGapBudgetDichotomyLedger"
NEAR_CONTACT = "StableLadderEndpointOrbitNearContactOppositeSignBoundaryPacketLedger"
SEPARATED = "StableLadderEndpointOrbitPhaseSeparatedBipolarPlateauPairPacketLedger"
NO_ANON = "NoAnonymousOppositeSignPlateauRampPairExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPlateauPairPhaseLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {AMPLITUDE_DEPTH} "
    f"AND {BOUNDARY} AND {PAIR_MODEL} AND {GAP_DECOMP} AND {GAP_SPLIT} "
    f"AND {NEAR_CONTACT} AND {SEPARATED} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 opposite-sign pair 硬点替换成 phase 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 plateau-pair phase 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitOppositeSignPlateauRampPairImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、opposite-sign plateau pair、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauPairPhase",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauPairPhase",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauPairPhase",
            True,
            False,
            "amplitude-depth PDEC/cap 继续前传；本步不排斥该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauPairPhase",
            True,
            False,
            "variation-boundary flux PDEC/cap 继续前传；近邻正负 plateau 接触也并入该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitOppositeSignPlateauPairModel",
            True,
            True,
            "把镜像对写成两个不交连续弧 P,Q，sigma Y 在 P 为正，-sigma Y 在 Q 为正。",
            PAIR_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitPlateauPairCyclicGapDecomposition",
            True,
            True,
            "两个不交弧在周期轨道上决定两个互补 gap g1,g2，记录相位间隔而非匿名配对。",
            GAP_DECOMP,
        ),
        row(
            "StableLadderEndpointOrbitPlateauPairGapBudgetDichotomy",
            True,
            True,
            "给定 gap 预算 E：若 min(g1,g2)<=E，则是近接正负边界；否则两侧 gap 均大于 E。",
            GAP_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitNearContactOppositeSignBoundaryPacket",
            True,
            False,
            "近接支路登记为正负 plateau 短桥边界通量包；本步不排斥该 PDEC/cap。",
            NEAR_CONTACT,
        ),
        row(
            "StableLadderEndpointOrbitPhaseSeparatedBipolarPlateauPairPacket",
            True,
            False,
            "远离支路登记为相位分离的双极 plateau pair；本步不排斥该 PDEC/cap。",
            SEPARATED,
        ),
        row(
            "NoAnonymousOppositeSignPlateauRampPairExit",
            True,
            True,
            "opposite-sign plateau pair 不再匿名保留；它是近接边界包或相位分离双极包。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPlateauPairPhase",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPlateauPairPhaseStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、phase-separated bipolar pair、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、phase-separated bipolar pair、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 plateau-pair phase 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "opposite-sign plateau-ramp pair 给出两个不交连续弧 P,Q：sigma*Y 在 P 上为正，"
        "-sigma*Y 在 Q 上为正。两个弧在周期轨道上决定两个 gap。给定 gap 预算 E，"
        "若较短 gap 不超过 E，则正负 plateau 通过短桥近接，登记为 boundary-flux 包；"
        "否则两个 gap 都超过 E，登记为相位分离的 bipolar plateau pair。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_pair_phase_router",
        "status": "endpoint_orbit_opposite_sign_plateau_pair_reduced_to_boundary_or_phase_separated_bipolar_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_opposite_sign_plateau_ramp_pair_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_opposite_sign_plateau_pair_model_closed": True,
        "endpoint_orbit_plateau_pair_cyclic_gap_decomposition_closed": True,
        "endpoint_orbit_plateau_pair_gap_budget_dichotomy_closed": True,
        "endpoint_orbit_near_contact_opposite_sign_boundary_packet_registered": True,
        "endpoint_orbit_phase_separated_bipolar_plateau_pair_packet_registered": True,
        "anonymous_opposite_sign_plateau_ramp_pair_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_phase_separated_bipolar_plateau_pair_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "plateau_pair_phase_formulas": {
            "positive_arc": "P consecutive, sigma*Y_j>0, positive plateau-ramp load",
            "negative_arc": "Q consecutive, -sigma*Y_j>0, negative return plateau load",
            "cyclic_gaps": "two disjoint arcs determine two gaps g1,g2 on the cycle",
            "gap_budget": "choose E>=0",
            "near_contact_branch": "if min(g1,g2)<=E then NearContactOppositeSignBoundaryPacket",
            "phase_separated_branch": "if min(g1,g2)>E then PhaseSeparatedBipolarPlateauPairPDECCap",
            "new_exit": "PhaseSeparatedBipolarPlateauPairPDECCapOrAmplitudeDepthPDECCapOrVariationBoundaryFluxPDECCap",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder endpoint orbit plateau-pair phase 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_opposite_sign_plateau_ramp_pair_imported={fmt_bool(cert['endpoint_orbit_opposite_sign_plateau_ramp_pair_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_opposite_sign_plateau_pair_model_closed={fmt_bool(cert['endpoint_orbit_opposite_sign_plateau_pair_model_closed'])}",
        f"endpoint_orbit_plateau_pair_cyclic_gap_decomposition_closed={fmt_bool(cert['endpoint_orbit_plateau_pair_cyclic_gap_decomposition_closed'])}",
        f"endpoint_orbit_plateau_pair_gap_budget_dichotomy_closed={fmt_bool(cert['endpoint_orbit_plateau_pair_gap_budget_dichotomy_closed'])}",
        f"endpoint_orbit_near_contact_opposite_sign_boundary_packet_registered={fmt_bool(cert['endpoint_orbit_near_contact_opposite_sign_boundary_packet_registered'])}",
        f"endpoint_orbit_phase_separated_bipolar_plateau_pair_packet_registered={fmt_bool(cert['endpoint_orbit_phase_separated_bipolar_plateau_pair_packet_registered'])}",
        f"anonymous_opposite_sign_plateau_ramp_pair_removed={fmt_bool(cert['anonymous_opposite_sign_plateau_ramp_pair_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_phase_separated_bipolar_plateau_pair_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_phase_separated_bipolar_plateau_pair_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正负 plateau 对",
        "",
        "镜像支路给出两个不交连续弧：",
        "",
        "```text",
        "P: sigma*Y_j>0,",
        "Q: -sigma*Y_j>0.",
        "```",
        "",
        "因此它不是匿名反向质量，而是同一周期轨道上的一个正负双极结构。",
        "",
        "## 2. gap 预算二分",
        "",
        "两个不交弧在周期上决定两个 gap `g1,g2`。给定预算 `E`：",
        "",
        "```text",
        "if min(g1,g2)<=E: near-contact opposite-sign boundary packet;",
        "if min(g1,g2)>E: phase-separated bipolar plateau pair.",
        "```",
        "",
        "近接分支并入 variation-boundary flux；远离分支保留为真正相位分离的双极 plateau pair。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 opposite-sign plateau pair，而是 phase-separated bipolar plateau pair，外加 amplitude-depth、boundary flux、singleton、full-cycle mean 与 sparse SAE。",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
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
            "- 本证书没有证明 endpoint singleton atom/SAE。",
            "- 本证书没有证明 EndpointOrbitFullCycleMeanAtomSAE。",
            "- 本证书没有证明 EndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 opposite-sign plateau pair 压成近接边界或相位分离双极包。",
            f"- `{NEW_TARGET}` 仍未闭合。",
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
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
