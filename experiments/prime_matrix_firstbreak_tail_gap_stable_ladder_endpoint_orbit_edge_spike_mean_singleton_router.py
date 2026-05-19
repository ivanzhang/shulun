#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit edge-spike mean/singleton 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_edge_spike_mean_singleton_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAE"
    "OrEndpointOrbitLongBoundedIncrementDriftPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitIncrementEdgeSpikeImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEdgeSpikeMeanSingletonLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEdgeSpikeMeanSingletonLedger"
LONG_DRIFT = "StableLadderEndpointOrbitLongBoundedIncrementDriftCarriedForwardAfterEdgeSpikeMeanSingletonLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterEdgeSpikeMeanSingletonLedger"
CENTERED = "StableLadderEndpointOrbitEdgeSpikeCenteredLoadExpansionLedger"
HALF_SPLIT = "StableLadderEndpointOrbitEdgeSpikeHalfThresholdDichotomyLedger"
SINGLETON_ABSORB = "StableLadderEndpointOrbitEdgeSpikeSingletonAtomAbsorptionLedger"
MEAN_ABSORB = "StableLadderEndpointOrbitEdgeSpikeFullCycleMeanAtomAbsorptionLedger"
NO_ANON = "NoAnonymousIncrementEdgeSpikeExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEdgeSpikeMeanSingletonLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {LONG_DRIFT} "
    f"AND {BOUNDARY} AND {CENTERED} AND {HALF_SPLIT} "
    f"AND {SINGLETON_ABSORB} AND {MEAN_ABSORB} AND {NO_ANON} "
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
    """把旧活动基中的 edge-spike 硬点替换成 mean/singleton 吸收接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 edge-spike mean/singleton 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitIncrementEdgeSpikeImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、increment edge-spike、long bounded drift、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEdgeSpikeMeanSingleton",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；edge-spike 可被吸收到该出口，但本步不证明其 SAE。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEdgeSpikeMeanSingleton",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；edge-spike 可被吸收到该出口，但本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitLongBoundedIncrementDriftCarriedForwardAfterEdgeSpikeMeanSingleton",
            True,
            False,
            "long bounded-increment drift 出口继续前传；本步不排斥该 PDEC/cap。",
            LONG_DRIFT,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterEdgeSpikeMeanSingleton",
            True,
            False,
            "variation-boundary flux 出口继续前传；本步不排斥该 PDEC/cap。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitEdgeSpikeCenteredLoadExpansion",
            True,
            True,
            "edge-spike 写成 sigma*Y_j=sigma*(X_j-mu)>=Lambda，其中 X_j 是未中心化点负载，mu 是整周期均值。",
            CENTERED,
        ),
        row(
            "StableLadderEndpointOrbitEdgeSpikeHalfThresholdDichotomy",
            True,
            True,
            "若 a-b>=Lambda，则 a>=Lambda/2 或 -b>=Lambda/2；取 a=sigma X_j, b=sigma mu。",
            HALF_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitEdgeSpikeSingletonAtomAbsorption",
            True,
            True,
            "sigma X_j>=Lambda/2 时，edge-spike 已是一个 endpoint singleton atom 出口。",
            SINGLETON_ABSORB,
        ),
        row(
            "StableLadderEndpointOrbitEdgeSpikeFullCycleMeanAtomAbsorption",
            True,
            True,
            "-sigma mu>=Lambda/2 时，edge-spike 已是 full-cycle mean atom 出口。",
            MEAN_ABSORB,
        ),
        row(
            "NoAnonymousIncrementEdgeSpikeExit",
            True,
            True,
            "increment edge-spike 不再作为独立匿名出口；它被 singleton 或 full-cycle mean 吸收。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterEdgeSpikeMeanSingleton",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitEdgeSpikeMeanSingletonStillOpen",
            False,
            False,
            "仍未排斥 singleton SAE、full-cycle mean SAE、long bounded drift、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、long bounded drift、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 edge-spike mean/singleton 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "increment edge-spike 给出某条边 j 与符号 sigma，使 sigma*Y_j>=Lambda。"
        "上一层的 Y_j 是中心化点负载，即 Y_j=X_j-mu。于是 sigma X_j - sigma mu>=Lambda。"
        "半阈值二分给出：若 sigma X_j>=Lambda/2，则这是 endpoint singleton atom；"
        "否则必有 -sigma mu>=Lambda/2，即 full-cycle mean atom。"
        "因此 edge-spike 不再是独立出口，而被已命名的 singleton 或 full-cycle mean 出口吸收。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_edge_spike_mean_singleton_router",
        "status": "endpoint_orbit_increment_edge_spike_absorbed_by_singleton_or_full_mean_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_increment_edge_spike_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_long_bounded_increment_drift_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_edge_spike_centered_load_expansion_closed": True,
        "endpoint_orbit_edge_spike_half_threshold_dichotomy_closed": True,
        "endpoint_orbit_edge_spike_singleton_atom_absorption_closed": True,
        "endpoint_orbit_edge_spike_full_cycle_mean_atom_absorption_closed": True,
        "anonymous_increment_edge_spike_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "edge_spike_mean_singleton_formulas": {
            "imported_spike": "exists j,sigma: sigma*Y_j>=Lambda",
            "centered_load_expansion": "Y_j=X_j-mu",
            "expanded_spike": "sigma*X_j-sigma*mu>=Lambda",
            "singleton_branch": "if sigma*X_j>=Lambda/2 then EndpointSingletonAtomSAE",
            "mean_branch": "if sigma*X_j<Lambda/2 then -sigma*mu>=Lambda/2, hence FullCycleMeanAtomSAE",
            "carried_exits": "LongBoundedIncrementDriftPDECCap and VariationBoundaryFluxPDECCap remain open",
            "new_exit": "EndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit edge-spike mean/singleton 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_increment_edge_spike_imported={fmt_bool(cert['endpoint_orbit_increment_edge_spike_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_long_bounded_increment_drift_carried_forward={fmt_bool(cert['endpoint_orbit_long_bounded_increment_drift_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_edge_spike_centered_load_expansion_closed={fmt_bool(cert['endpoint_orbit_edge_spike_centered_load_expansion_closed'])}",
        f"endpoint_orbit_edge_spike_half_threshold_dichotomy_closed={fmt_bool(cert['endpoint_orbit_edge_spike_half_threshold_dichotomy_closed'])}",
        f"endpoint_orbit_edge_spike_singleton_atom_absorption_closed={fmt_bool(cert['endpoint_orbit_edge_spike_singleton_atom_absorption_closed'])}",
        f"endpoint_orbit_edge_spike_full_cycle_mean_atom_absorption_closed={fmt_bool(cert['endpoint_orbit_edge_spike_full_cycle_mean_atom_absorption_closed'])}",
        f"anonymous_increment_edge_spike_removed={fmt_bool(cert['anonymous_increment_edge_spike_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. edge-spike 包",
        "",
        "上一层 edge-spike 支路给出某条轨道边 `j` 与符号 `sigma`：",
        "",
        "```text",
        "sigma*Y_j >= Lambda.",
        "```",
        "",
        "这里 `Y_j` 是中心化点负载，来自：",
        "",
        "```text",
        "Y_j = X_j - mu.",
        "```",
        "",
        "## 2. 半阈值吸收",
        "",
        "代入得到：",
        "",
        "```text",
        "sigma*X_j - sigma*mu >= Lambda.",
        "```",
        "",
        "因此必有二分：",
        "",
        "```text",
        "sigma*X_j >= Lambda/2",
        "or",
        "-sigma*mu >= Lambda/2.",
        "```",
        "",
        "第一支是单点实际负载过大，即 endpoint singleton atom；第二支是整周期均值项过大，即 full-cycle mean atom。",
        "",
        "## 3. 前传出口",
        "",
        "`EndpointOrbitLongBoundedIncrementDriftPDECCap` 与 `EndpointOrbitVariationBoundaryFluxPDECCap` 不是本步对象，继续前传为未闭合出口。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再含独立 increment edge-spike 出口；它已并入 endpoint singleton atom/SAE 或 full-cycle mean atom/SAE。未闭合项集中为 singleton、full-cycle mean、long bounded drift、boundary flux 与 sparse scale-ladder SAE。",
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
            "- 本证书没有证明 EndpointOrbitLongBoundedIncrementDriftPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 increment edge-spike 吸收到 singleton 或 full-cycle mean 出口。",
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
