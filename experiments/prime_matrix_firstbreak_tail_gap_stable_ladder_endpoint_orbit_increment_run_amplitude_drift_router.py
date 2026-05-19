#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit increment-run amplitude/drift 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_increment_run_amplitude_drift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAE"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitIncrementRunSurplusImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterIncrementRunAmplitudeDriftLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterIncrementRunAmplitudeDriftLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterIncrementRunAmplitudeDriftLedger"
RUN_COORD = "StableLadderEndpointOrbitIncrementRunSameSignCoordinateLedger"
RUN_MASS = "StableLadderEndpointOrbitIncrementRunMassLowerBoundLedger"
AMPLITUDE_SPLIT = "StableLadderEndpointOrbitIncrementRunAmplitudeThresholdDichotomyLedger"
EDGE_SPIKE = "StableLadderEndpointOrbitIncrementEdgeSpikePacketLedger"
LONG_DRIFT = "StableLadderEndpointOrbitLongBoundedIncrementDriftPacketLedger"
NO_ANON = "NoAnonymousIncrementRunSurplusExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterIncrementRunAmplitudeDriftLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAE"
    "OrEndpointOrbitLongBoundedIncrementDriftPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {BOUNDARY} "
    f"AND {RUN_COORD} AND {RUN_MASS} AND {AMPLITUDE_SPLIT} "
    f"AND {EDGE_SPIKE} AND {LONG_DRIFT} AND {NO_ANON} "
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
    """把旧活动基中的 increment-run 硬点替换成 amplitude/drift 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 increment-run amplitude/drift 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitIncrementRunSurplusImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、increment-run surplus、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterIncrementRunAmplitudeDrift",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterIncrementRunAmplitudeDrift",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterIncrementRunAmplitudeDrift",
            True,
            False,
            "上一层高切换 boundary-flux 出口继续前传；本步专攻低切换 run 支路。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitIncrementRunSameSignCoordinate",
            True,
            True,
            "把 run 内增量写成 Z_j=sigma Y_j>0，并保留连续 run 坐标。",
            RUN_COORD,
        ),
        row(
            "StableLadderEndpointOrbitIncrementRunMassLowerBound",
            True,
            True,
            "由上一层 pigeonhole 得到 sum_{j in R}Z_j>=H，其中 H=G/B。",
            RUN_MASS,
        ),
        row(
            "StableLadderEndpointOrbitIncrementRunAmplitudeThresholdDichotomy",
            True,
            True,
            "对任意幅度阈值 Lambda，若 max_R Z_j>=Lambda 则为 edge spike；否则 |R|>=H/Lambda 且所有增量受 Lambda 控制。",
            AMPLITUDE_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitIncrementEdgeSpikePacket",
            True,
            False,
            "大幅单边增量登记为 increment edge-spike atom；本步不证明其 SAE。",
            EDGE_SPIKE,
        ),
        row(
            "StableLadderEndpointOrbitLongBoundedIncrementDriftPacket",
            True,
            False,
            "无大幅边时得到长的有界增量单调漂移 run；本步不排斥该 PDEC/cap。",
            LONG_DRIFT,
        ),
        row(
            "NoAnonymousIncrementRunSurplusExit",
            True,
            True,
            "剩余不再是匿名 increment-run surplus，而是 edge-spike atom 或 long bounded-increment drift。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterIncrementRunAmplitudeDrift",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitIncrementRunAmplitudeDriftStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、edge spike SAE、long bounded drift、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、edge spike、long bounded drift、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 increment-run amplitude/drift 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "increment-run surplus 给出一个连续同符号 run R，使 Z_j=sigma Y_j>0 且 "
        "sum_{j in R}Z_j>=H。固定任意幅度阈值 Lambda。若某条边满足 Z_j>=Lambda，"
        "则剩余集中到单边大增量 edge-spike atom；否则所有边增量都小于 Lambda，"
        "因此 run 长度至少 H/Lambda，并形成长的有界增量单调漂移支路。"
        "上一层的 variation-boundary flux 出口继续前传。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_increment_run_amplitude_drift_router",
        "status": "endpoint_orbit_increment_run_reduced_to_edge_spike_or_long_bounded_drift_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_increment_run_surplus_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_increment_run_same_sign_coordinate_closed": True,
        "endpoint_orbit_increment_run_mass_lower_bound_closed": True,
        "endpoint_orbit_increment_run_amplitude_threshold_dichotomy_closed": True,
        "endpoint_orbit_increment_edge_spike_packet_registered": True,
        "endpoint_orbit_long_bounded_increment_drift_packet_registered": True,
        "anonymous_increment_run_surplus_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_increment_edge_spike_sae_proved": False,
        "endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "increment_run_amplitude_drift_formulas": {
            "imported_run": "R consecutive, Z_j=sigma*Y_j>0, sum_{j in R}Z_j>=H",
            "mass_from_previous": "H=G/B",
            "edge_spike_branch": "if max_{j in R}Z_j>=Lambda then IncrementEdgeSpikeSAE",
            "long_drift_branch": "if max_{j in R}Z_j<Lambda then |R|>=H/Lambda and R is a bounded-increment monotone drift",
            "boundary_flux_carried": "EndpointOrbitVariationBoundaryFluxPDECCap remains open from the high-run branch",
            "new_exit": "EndpointOrbitIncrementEdgeSpikeSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit increment-run amplitude/drift 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_increment_run_surplus_imported={fmt_bool(cert['endpoint_orbit_increment_run_surplus_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_increment_run_same_sign_coordinate_closed={fmt_bool(cert['endpoint_orbit_increment_run_same_sign_coordinate_closed'])}",
        f"endpoint_orbit_increment_run_mass_lower_bound_closed={fmt_bool(cert['endpoint_orbit_increment_run_mass_lower_bound_closed'])}",
        f"endpoint_orbit_increment_run_amplitude_threshold_dichotomy_closed={fmt_bool(cert['endpoint_orbit_increment_run_amplitude_threshold_dichotomy_closed'])}",
        f"endpoint_orbit_increment_edge_spike_packet_registered={fmt_bool(cert['endpoint_orbit_increment_edge_spike_packet_registered'])}",
        f"endpoint_orbit_long_bounded_increment_drift_packet_registered={fmt_bool(cert['endpoint_orbit_long_bounded_increment_drift_packet_registered'])}",
        f"anonymous_increment_run_surplus_removed={fmt_bool(cert['anonymous_increment_run_surplus_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_increment_edge_spike_sae_proved={fmt_bool(cert['endpoint_orbit_increment_edge_spike_sae_proved'])}",
        f"endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. increment-run surplus 包",
        "",
        "上一层低边界支路给出连续 run `R` 与符号 `sigma`。令：",
        "",
        "```text",
        "Z_j=sigma*Y_j>0 for j in R.",
        "```",
        "",
        "并有质量下界：",
        "",
        "```text",
        "sum_{j in R}Z_j >= H,  H=G/B.",
        "```",
        "",
        "## 2. 幅度阈值二分",
        "",
        "固定任意幅度阈值 `Lambda>0`。若：",
        "",
        "```text",
        "max_{j in R}Z_j >= Lambda,",
        "```",
        "",
        "则得到单边大增量 `increment edge-spike` 原子。否则：",
        "",
        "```text",
        "0<Z_j<Lambda for all j in R,",
        "```",
        "",
        "于是由总质量下界得到：",
        "",
        "```text",
        "|R| >= H/Lambda.",
        "```",
        "",
        "这就是长的有界增量单调漂移支路。",
        "",
        "## 3. 高边界通量前传",
        "",
        "上一层的 `EndpointOrbitVariationBoundaryFluxPDECCap` 来自 run 数超过预算的支路；本步没有排斥它，只把低切换 run surplus 继续下钻。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从匿名 increment-run surplus 变成 increment edge-spike SAE 或 long bounded-increment drift PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom、variation-boundary flux 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitIncrementEdgeSpikeSAE。",
            "- 本证书没有证明 EndpointOrbitLongBoundedIncrementDriftPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把低切换 increment-run surplus 压成大边原子或长有界漂移二分。",
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
