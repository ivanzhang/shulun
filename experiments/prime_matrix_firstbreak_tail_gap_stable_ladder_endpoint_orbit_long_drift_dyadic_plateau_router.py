#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit long-drift dyadic plateau 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_drift_dyadic_plateau_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitLongBoundedIncrementDriftImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterLongDriftDyadicPlateauLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLongDriftDyadicPlateauLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLongDriftDyadicPlateauLedger"
DRIFT_MODEL = "StableLadderEndpointOrbitLongDriftPositiveBoundedRunLedger"
DYADIC = "StableLadderEndpointOrbitLongDriftDyadicAmplitudePartitionLedger"
DEPTH_SPLIT = "StableLadderEndpointOrbitLongDriftAmplitudeDepthBudgetDichotomyLedger"
BAND_MASS = "StableLadderEndpointOrbitLongDriftHeavyDyadicBandLedger"
PLATEAU_RUN = "StableLadderEndpointOrbitDyadicBandPlateauRunPartitionLedger"
PLATEAU_SPLIT = "StableLadderEndpointOrbitDyadicPlateauRunBoundaryDichotomyLedger"
PLATEAU_PACKET = "StableLadderEndpointOrbitComparableAmplitudePlateauDriftPacketLedger"
DEPTH_PACKET = "StableLadderEndpointOrbitAmplitudeDepthPacketLedger"
NO_ANON = "NoAnonymousLongBoundedIncrementDriftExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterLongDriftDyadicPlateauLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BOUNDARY} "
    f"AND {DRIFT_MODEL} AND {DYADIC} AND {DEPTH_SPLIT} "
    f"AND {BAND_MASS} AND {PLATEAU_RUN} AND {PLATEAU_SPLIT} "
    f"AND {PLATEAU_PACKET} AND {DEPTH_PACKET} AND {NO_ANON} "
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
    """把旧活动基中的 long bounded drift 硬点替换成 dyadic plateau 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 long-drift dyadic plateau 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitLongBoundedIncrementDriftImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、long bounded drift、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterLongDriftDyadicPlateau",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLongDriftDyadicPlateau",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLongDriftDyadicPlateau",
            True,
            False,
            "既有 variation-boundary flux 出口继续前传；本步不排斥该 PDEC/cap。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitLongDriftPositiveBoundedRun",
            True,
            True,
            "long drift 写成连续 run R 上 0<Z_j<Lambda 且 sum_R Z_j>=H。",
            DRIFT_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitLongDriftDyadicAmplitudePartition",
            True,
            True,
            "把 R 内正增量按 dyadic 幅度层 A_l={2^{-(l+1)}Lambda<=Z_j<2^{-l}Lambda} 分解。",
            DYADIC,
        ),
        row(
            "StableLadderEndpointOrbitLongDriftAmplitudeDepthBudgetDichotomy",
            True,
            True,
            "若非空 dyadic 层数 d>D，则登记 amplitude-depth PDEC/cap；若 d<=D，则某层承载至少 H/D。",
            DEPTH_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitLongDriftHeavyDyadicBand",
            True,
            True,
            "受控深度支路中存在 dyadic band A_l 满足 sum_{A_l}Z_j>=H/D 且所有增量可比较。",
            BAND_MASS,
        ),
        row(
            "StableLadderEndpointOrbitDyadicBandPlateauRunPartition",
            True,
            True,
            "把重 dyadic band 在 R 中分解为极大连续 plateau runs。",
            PLATEAU_RUN,
        ),
        row(
            "StableLadderEndpointOrbitDyadicPlateauRunBoundaryDichotomy",
            True,
            True,
            "若 plateau run 数大于 B，则进入 boundary flux；否则某个 plateau run 承载至少 H/(D B)。",
            PLATEAU_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitComparableAmplitudePlateauDriftPacket",
            True,
            False,
            "低边界支路登记为可比较幅度 plateau drift；本步不排斥该 PDEC/cap。",
            PLATEAU_PACKET,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthPacket",
            True,
            False,
            "高 dyadic 深度支路登记为 amplitude-depth PDEC/cap；本步不排斥该 cap。",
            DEPTH_PACKET,
        ),
        row(
            "NoAnonymousLongBoundedIncrementDriftExit",
            True,
            True,
            "long bounded drift 不再匿名保留；剩余是 amplitude-depth、plateau drift 或 boundary flux。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterLongDriftDyadicPlateau",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitLongDriftDyadicPlateauStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、plateau drift、amplitude depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、plateau drift、amplitude depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 long-drift dyadic plateau 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "long bounded drift 给出连续 run R，使 0<Z_j<Lambda 且 sum_R Z_j>=H。"
        "按 dyadic 幅度层 A_l={2^{-(l+1)}Lambda<=Z_j<2^{-l}Lambda} 分解。"
        "若非空层数超过 D，则这是幅度深度异常；若不超过 D，则某层承载至少 H/D。"
        "再把该层在 R 中分解为连续 plateau runs。若 plateau 数超过 B，则进入边界通量；"
        "否则某个可比较幅度 plateau run 承载至少 H/(D B)。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_drift_dyadic_plateau_router",
        "status": "endpoint_orbit_long_bounded_drift_reduced_to_dyadic_plateau_or_depth_or_boundary_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_long_bounded_increment_drift_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_long_drift_positive_bounded_run_closed": True,
        "endpoint_orbit_long_drift_dyadic_amplitude_partition_closed": True,
        "endpoint_orbit_long_drift_amplitude_depth_budget_dichotomy_closed": True,
        "endpoint_orbit_long_drift_heavy_dyadic_band_closed": True,
        "endpoint_orbit_dyadic_band_plateau_run_partition_closed": True,
        "endpoint_orbit_dyadic_plateau_run_boundary_dichotomy_closed": True,
        "endpoint_orbit_comparable_amplitude_plateau_drift_packet_registered": True,
        "endpoint_orbit_amplitude_depth_packet_registered": True,
        "anonymous_long_bounded_increment_drift_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_comparable_amplitude_plateau_drift_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "long_drift_dyadic_plateau_formulas": {
            "imported_drift": "R consecutive, 0<Z_j<Lambda, sum_{j in R}Z_j>=H",
            "dyadic_bands": "A_l={j in R: 2^{-(l+1)}Lambda<=Z_j<2^{-l}Lambda}",
            "depth_branch": "if number_of_nonempty_bands>D then AmplitudeDepthPDECCap",
            "heavy_band": "if number_of_nonempty_bands<=D then exists l: sum_{j in A_l}Z_j>=H/D",
            "plateau_partition": "A_l decomposes into maximal consecutive plateau runs P_s",
            "boundary_branch": "if number_of_plateau_runs>B then VariationBoundaryFluxPDECCap",
            "plateau_branch": "if number_of_plateau_runs<=B then exists s: sum_{j in P_s}Z_j>=H/(D*B)",
            "new_exit": "ComparableAmplitudePlateauDriftPDECCapOrAmplitudeDepthPDECCapOrVariationBoundaryFluxPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit long-drift dyadic plateau 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_long_bounded_increment_drift_imported={fmt_bool(cert['endpoint_orbit_long_bounded_increment_drift_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_long_drift_positive_bounded_run_closed={fmt_bool(cert['endpoint_orbit_long_drift_positive_bounded_run_closed'])}",
        f"endpoint_orbit_long_drift_dyadic_amplitude_partition_closed={fmt_bool(cert['endpoint_orbit_long_drift_dyadic_amplitude_partition_closed'])}",
        f"endpoint_orbit_long_drift_amplitude_depth_budget_dichotomy_closed={fmt_bool(cert['endpoint_orbit_long_drift_amplitude_depth_budget_dichotomy_closed'])}",
        f"endpoint_orbit_long_drift_heavy_dyadic_band_closed={fmt_bool(cert['endpoint_orbit_long_drift_heavy_dyadic_band_closed'])}",
        f"endpoint_orbit_dyadic_band_plateau_run_partition_closed={fmt_bool(cert['endpoint_orbit_dyadic_band_plateau_run_partition_closed'])}",
        f"endpoint_orbit_dyadic_plateau_run_boundary_dichotomy_closed={fmt_bool(cert['endpoint_orbit_dyadic_plateau_run_boundary_dichotomy_closed'])}",
        f"endpoint_orbit_comparable_amplitude_plateau_drift_packet_registered={fmt_bool(cert['endpoint_orbit_comparable_amplitude_plateau_drift_packet_registered'])}",
        f"endpoint_orbit_amplitude_depth_packet_registered={fmt_bool(cert['endpoint_orbit_amplitude_depth_packet_registered'])}",
        f"anonymous_long_bounded_increment_drift_removed={fmt_bool(cert['anonymous_long_bounded_increment_drift_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_comparable_amplitude_plateau_drift_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_comparable_amplitude_plateau_drift_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. long bounded drift 包",
        "",
        "上一层给出连续 run `R`：",
        "",
        "```text",
        "0<Z_j<Lambda,  sum_{j in R}Z_j>=H.",
        "```",
        "",
        "## 2. dyadic 幅度层",
        "",
        "对 `l>=0` 定义：",
        "",
        "```text",
        "A_l={j in R: 2^{-(l+1)}Lambda <= Z_j < 2^{-l}Lambda}.",
        "```",
        "",
        "`R` 有限，因此非空 dyadic 层数有限。给定深度预算 `D`：若非空层数 `d>D`，登记为 amplitude-depth PDEC/cap；若 `d<=D`，则有某个重层：",
        "",
        "```text",
        "sum_{j in A_l}Z_j >= H/D.",
        "```",
        "",
        "## 3. plateau run 二分",
        "",
        "把该重 dyadic band 在 `R` 中分解为极大连续 plateau runs。给定 plateau 边界预算 `B`：若 run 数超过 `B`，进入 variation-boundary flux；否则某个 plateau run `P_s` 满足：",
        "",
        "```text",
        "sum_{j in P_s}Z_j >= H/(D*B).",
        "```",
        "",
        "且 `P_s` 内所有增量在同一个 dyadic band 中，幅度相差小于 2 倍。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 long bounded drift，而是 comparable-amplitude plateau drift、amplitude-depth 或 variation-boundary flux，外加 singleton、full-cycle mean 与 sparse SAE。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 endpoint singleton atom/SAE。",
            "- 本证书没有证明 EndpointOrbitFullCycleMeanAtomSAE。",
            "- 本证书没有证明 EndpointOrbitComparableAmplitudePlateauDriftPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 long bounded drift 压成 dyadic plateau、amplitude-depth 或 boundary-flux 三分。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
