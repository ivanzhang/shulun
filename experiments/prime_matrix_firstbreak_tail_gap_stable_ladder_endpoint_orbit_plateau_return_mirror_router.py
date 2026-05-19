#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit plateau-return mirror 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_return_mirror_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPlateauRampPotentialImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauReturnMirrorLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauReturnMirrorLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauReturnMirrorLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauReturnMirrorLedger"
POS_RAMP = "StableLadderEndpointOrbitPositivePlateauRampImportedModelLedger"
ZERO_SUM = "StableLadderEndpointOrbitFullCycleZeroSumReturnObligationLedger"
NEG_RETURN = "StableLadderEndpointOrbitNegativeReturnMassLowerBoundLedger"
RETURN_DYADIC = "StableLadderEndpointOrbitReturnMassDyadicAmplitudePartitionLedger"
RETURN_DEPTH = "StableLadderEndpointOrbitReturnAmplitudeDepthDichotomyLedger"
RETURN_BAND = "StableLadderEndpointOrbitHeavyReturnDyadicBandLedger"
RETURN_RUN = "StableLadderEndpointOrbitReturnPlateauRunPartitionLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitReturnRunBoundaryDichotomyLedger"
MIRROR_PAIR = "StableLadderEndpointOrbitOppositeSignPlateauRampPairPacketLedger"
NO_ANON = "NoAnonymousPlateauRampPotentialExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPlateauReturnMirrorLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {AMPLITUDE_DEPTH} "
    f"AND {BOUNDARY} AND {POS_RAMP} AND {ZERO_SUM} AND {NEG_RETURN} "
    f"AND {RETURN_DYADIC} AND {RETURN_DEPTH} AND {RETURN_BAND} "
    f"AND {RETURN_RUN} AND {RETURN_SPLIT} AND {MIRROR_PAIR} "
    f"AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 plateau-ramp potential 硬点替换成 return mirror 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 plateau-return mirror 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitPlateauRampPotentialImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、plateau-ramp potential、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauReturnMirror",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauReturnMirror",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauReturnMirror",
            True,
            False,
            "amplitude-depth PDEC/cap 从上一层继续前传；return mass 高深度也并入该出口。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauReturnMirror",
            True,
            False,
            "variation-boundary flux PDEC/cap 从上一层继续前传；return run 高切换也并入该出口。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitPositivePlateauRampImportedModel",
            True,
            True,
            "plateau-ramp 写成正向连续弧 P，Z_j=sigma Y_j>0 且 sum_P Z_j>=H0。",
            POS_RAMP,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleZeroSumReturnObligation",
            True,
            True,
            "中心化负载满足全周期和为零，因此补弧必须支付同等反向回落。",
            ZERO_SUM,
        ),
        row(
            "StableLadderEndpointOrbitNegativeReturnMassLowerBound",
            True,
            True,
            "补弧上的负向 return mass W_j=(-sigma Y_j)_+ 总和至少 H0。",
            NEG_RETURN,
        ),
        row(
            "StableLadderEndpointOrbitReturnMassDyadicAmplitudePartition",
            True,
            True,
            "把补弧 return mass 按 dyadic 幅度层分解。",
            RETURN_DYADIC,
        ),
        row(
            "StableLadderEndpointOrbitReturnAmplitudeDepthDichotomy",
            True,
            True,
            "若 return 非空幅度层数超过 D，则进入 amplitude-depth；否则存在重 return band 承载至少 H0/D。",
            RETURN_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitHeavyReturnDyadicBand",
            True,
            True,
            "受控深度支路中存在一个 return dyadic band 承载至少 H0/D。",
            RETURN_BAND,
        ),
        row(
            "StableLadderEndpointOrbitReturnPlateauRunPartition",
            True,
            True,
            "把重 return band 在补弧中分解为极大连续 return plateau runs。",
            RETURN_RUN,
        ),
        row(
            "StableLadderEndpointOrbitReturnRunBoundaryDichotomy",
            True,
            True,
            "若 return plateau run 数超过 B，则进入 boundary flux；否则存在重 return plateau run 承载至少 H0/(D B)。",
            RETURN_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitOppositeSignPlateauRampPairPacket",
            True,
            False,
            "低深度低边界支路登记为正 plateau-ramp 与负 return plateau 的镜像对；本步不排斥该 PDEC/cap。",
            MIRROR_PAIR,
        ),
        row(
            "NoAnonymousPlateauRampPotentialExit",
            True,
            True,
            "plateau-ramp potential 不再匿名保留；它必须有负向镜像 return，或进入 depth/boundary 出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPlateauReturnMirror",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPlateauReturnMirrorStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、opposite-sign plateau-ramp pair、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、opposite-sign plateau-ramp pair、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 plateau-return mirror 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "plateau-ramp potential 给出正向连续弧 P，使 Z_j=sigma*Y_j>0 且 sum_P Z_j>=H0。"
        "由于中心化负载在整周期上的总和为零，补弧必须有负向 return mass 至少 H0。"
        "把 W_j=(-sigma*Y_j)_+ 按 dyadic 幅度层和连续 run 分解：若层数过多则进入 amplitude-depth，"
        "若 run 数过多则进入 boundary flux；否则存在一个重负向 return plateau。"
        "因此匿名 ramp potential 被压成正 ramp 与负 return plateau 的镜像对。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_return_mirror_router",
        "status": "endpoint_orbit_plateau_ramp_reduced_to_return_mirror_or_depth_or_boundary_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_plateau_ramp_potential_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_positive_plateau_ramp_imported_model_closed": True,
        "endpoint_orbit_full_cycle_zero_sum_return_obligation_closed": True,
        "endpoint_orbit_negative_return_mass_lower_bound_closed": True,
        "endpoint_orbit_return_mass_dyadic_amplitude_partition_closed": True,
        "endpoint_orbit_return_amplitude_depth_dichotomy_closed": True,
        "endpoint_orbit_heavy_return_dyadic_band_closed": True,
        "endpoint_orbit_return_plateau_run_partition_closed": True,
        "endpoint_orbit_return_run_boundary_dichotomy_closed": True,
        "endpoint_orbit_opposite_sign_plateau_ramp_pair_packet_registered": True,
        "anonymous_plateau_ramp_potential_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_opposite_sign_plateau_ramp_pair_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "plateau_return_mirror_formulas": {
            "positive_ramp": "P consecutive, Z_j=sigma*Y_j>0, sum_{j in P}Z_j>=H0",
            "cycle_zero_sum": "sum_{cycle}sigma*Y_j=0",
            "return_mass": "W_j=(-sigma*Y_j)_+ on the complement, sum W_j>=H0",
            "return_dyadic_bands": "B_l={j: 2^{-(l+1)}A<=W_j<2^{-l}A} for a chosen top return scale A",
            "depth_branch": "if number_of_nonempty_return_bands>D then AmplitudeDepthPDECCap",
            "heavy_return_band": "otherwise exists l: sum_{j in B_l}W_j>=H0/D",
            "boundary_branch": "if number_of_return_plateau_runs>B then VariationBoundaryFluxPDECCap",
            "mirror_pair_branch": "otherwise exists negative return plateau Q with sum_Q W_j>=H0/(D*B)",
            "new_exit": "OppositeSignPlateauRampPairPDECCapOrAmplitudeDepthPDECCapOrVariationBoundaryFluxPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit plateau-return mirror 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_plateau_ramp_potential_imported={fmt_bool(cert['endpoint_orbit_plateau_ramp_potential_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_positive_plateau_ramp_imported_model_closed={fmt_bool(cert['endpoint_orbit_positive_plateau_ramp_imported_model_closed'])}",
        f"endpoint_orbit_full_cycle_zero_sum_return_obligation_closed={fmt_bool(cert['endpoint_orbit_full_cycle_zero_sum_return_obligation_closed'])}",
        f"endpoint_orbit_negative_return_mass_lower_bound_closed={fmt_bool(cert['endpoint_orbit_negative_return_mass_lower_bound_closed'])}",
        f"endpoint_orbit_return_mass_dyadic_amplitude_partition_closed={fmt_bool(cert['endpoint_orbit_return_mass_dyadic_amplitude_partition_closed'])}",
        f"endpoint_orbit_return_amplitude_depth_dichotomy_closed={fmt_bool(cert['endpoint_orbit_return_amplitude_depth_dichotomy_closed'])}",
        f"endpoint_orbit_heavy_return_dyadic_band_closed={fmt_bool(cert['endpoint_orbit_heavy_return_dyadic_band_closed'])}",
        f"endpoint_orbit_return_plateau_run_partition_closed={fmt_bool(cert['endpoint_orbit_return_plateau_run_partition_closed'])}",
        f"endpoint_orbit_return_run_boundary_dichotomy_closed={fmt_bool(cert['endpoint_orbit_return_run_boundary_dichotomy_closed'])}",
        f"endpoint_orbit_opposite_sign_plateau_ramp_pair_packet_registered={fmt_bool(cert['endpoint_orbit_opposite_sign_plateau_ramp_pair_packet_registered'])}",
        f"anonymous_plateau_ramp_potential_removed={fmt_bool(cert['anonymous_plateau_ramp_potential_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_opposite_sign_plateau_ramp_pair_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_opposite_sign_plateau_ramp_pair_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正向 ramp 与整周期回落义务",
        "",
        "上一层给出正向连续 plateau-ramp：",
        "",
        "```text",
        "P consecutive,  Z_j=sigma*Y_j>0,  sum_{j in P}Z_j>=H0.",
        "```",
        "",
        "由于 `Y` 是中心化轨道负载，整周期满足：",
        "",
        "```text",
        "sum_cycle sigma*Y_j=0.",
        "```",
        "",
        "因此补弧上的负向 return mass",
        "",
        "```text",
        "W_j=(-sigma*Y_j)_+",
        "```",
        "",
        "必须满足 `sum W_j>=H0`。",
        "",
        "## 2. return mass 分解",
        "",
        "把 `W_j` 按 dyadic 幅度层分解。给定深度预算 `D`：若非空 return 层数超过 `D`，则进入 amplitude-depth PDEC/cap；否则有某个重 return band 承载至少 `H0/D`。",
        "",
        "再把该重层在补弧中分解为极大连续 return plateau runs。给定边界预算 `B`：若 run 数超过 `B`，则进入 variation-boundary flux；否则存在一个负向 return plateau `Q` 满足：",
        "",
        "```text",
        "sum_{j in Q} W_j >= H0/(D*B).",
        "```",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 plateau-ramp potential，而是正 ramp 与负 return plateau 的镜像对，外加 amplitude-depth、boundary flux、singleton、full-cycle mean 与 sparse SAE。",
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
            "- 本证书没有证明 EndpointOrbitOppositeSignPlateauRampPairPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 plateau-ramp potential 压成负向 return mirror、amplitude-depth 或 boundary-flux 三分。",
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
