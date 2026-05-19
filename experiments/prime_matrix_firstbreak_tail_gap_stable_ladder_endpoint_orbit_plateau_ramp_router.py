#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit plateau-ramp 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_ramp_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitComparableAmplitudePlateauDriftImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauRampLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauRampLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauRampLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauRampLedger"
PLATEAU_MODEL = "StableLadderEndpointOrbitComparablePlateauSameSignLoadLedger"
LENGTH_SPLIT = "StableLadderEndpointOrbitPlateauLengthBudgetDichotomyLedger"
SHORT_ABSORB = "StableLadderEndpointOrbitShortPlateauEdgeSpikeAbsorptionLedger"
RAMP_PACKET = "StableLadderEndpointOrbitLongPlateauMonotoneRampPacketLedger"
NO_ANON = "NoAnonymousComparableAmplitudePlateauDriftExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPlateauRampLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCap"
    "OrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {AMPLITUDE_DEPTH} "
    f"AND {BOUNDARY} AND {PLATEAU_MODEL} AND {LENGTH_SPLIT} "
    f"AND {SHORT_ABSORB} AND {RAMP_PACKET} AND {NO_ANON} "
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
    """把旧活动基中的 plateau drift 硬点替换成 ramp 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 plateau-ramp 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitComparableAmplitudePlateauDriftImported",
            imported,
            False,
            "上一层剩余含 singleton、full-cycle mean、comparable-amplitude plateau drift、amplitude depth、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauRamp",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；短 plateau 的大单边原子也并入此命名出口。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauRamp",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；短 plateau edge-spike 的均值半阈值也并入此出口。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauRamp",
            True,
            False,
            "amplitude-depth PDEC/cap 从上一层继续前传；本步专攻受控深度下的 plateau 支路。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauRamp",
            True,
            False,
            "variation-boundary flux PDEC/cap 从上一层继续前传；本步专攻低边界 plateau 支路。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitComparablePlateauSameSignLoad",
            True,
            True,
            "plateau 支路写成连续 P_s、同号负载 Z_j=sigma Y_j>0、a<=Z_j<2a 且 sum_{P_s}Z_j>=H0。",
            PLATEAU_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitPlateauLengthBudgetDichotomy",
            True,
            True,
            "给定长度预算 L0：若 |P_s|<=L0，则 max Z_j>=H0/L0；否则 P_s 是长度超过 L0 的可比较单调 ramp。",
            LENGTH_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitShortPlateauEdgeSpikeAbsorption",
            True,
            True,
            "短 plateau 给出的 max Z_j>=H0/L0 是 edge-spike；由中心化展开半阈值吸收到 singleton 或 full-cycle mean。",
            SHORT_ABSORB,
        ),
        row(
            "StableLadderEndpointOrbitLongPlateauMonotoneRampPacket",
            True,
            False,
            "长 plateau 给出 prefix potential 在同一连续弧上的单调爬升，登记为 plateau-ramp potential PDEC/cap。",
            RAMP_PACKET,
        ),
        row(
            "NoAnonymousComparableAmplitudePlateauDriftExit",
            True,
            True,
            "comparable-amplitude plateau drift 不再匿名保留；短支路被吸收，长支路成为 plateau-ramp potential。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPlateauRamp",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPlateauRampStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、plateau-ramp potential、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、plateau-ramp potential、amplitude-depth、boundary flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 plateau-ramp 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "comparable-amplitude plateau drift 给出连续 plateau P_s、符号 sigma、"
        "以及 a>0，使 Z_j=sigma Y_j 满足 a<=Z_j<2a 且 sum_{P_s}Z_j>=H0。"
        "给定长度预算 L0：若 |P_s|<=L0，则某条边满足 Z_j>=H0/L0，"
        "由 edge-spike 的中心化半阈值吸收到 singleton 或 full-cycle mean；"
        "若 |P_s|>L0，则 prefix potential 在一段长连续弧上单调爬升至少 H0，"
        "并登记为 plateau-ramp potential PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_ramp_router",
        "status": "endpoint_orbit_comparable_plateau_reduced_to_edge_absorption_or_monotone_ramp_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_comparable_amplitude_plateau_drift_imported": imported,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "endpoint_orbit_comparable_plateau_same_sign_load_closed": True,
        "endpoint_orbit_plateau_length_budget_dichotomy_closed": True,
        "endpoint_orbit_short_plateau_edge_spike_absorption_closed": True,
        "endpoint_orbit_long_plateau_monotone_ramp_packet_registered": True,
        "anonymous_comparable_amplitude_plateau_drift_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_plateau_ramp_potential_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "plateau_ramp_formulas": {
            "imported_plateau": "P_s consecutive, Z_j=sigma*Y_j>0, a<=Z_j<2a, sum_{j in P_s}Z_j>=H0",
            "length_budget": "choose L0>=1",
            "short_branch": "if |P_s|<=L0 then max_{P_s}Z_j>=H0/L0 and the edge-spike is absorbed by singleton/full-cycle mean outlets",
            "long_branch": "if |P_s|>L0 then the prefix potential S(t)=sum_{i<=t}sigma*Y_i rises monotonically by at least H0 across P_s",
            "new_exit": "EndpointOrbitPlateauRampPotentialPDECCapOrAmplitudeDepthPDECCapOrVariationBoundaryFluxPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit plateau-ramp 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_comparable_amplitude_plateau_drift_imported={fmt_bool(cert['endpoint_orbit_comparable_amplitude_plateau_drift_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_amplitude_depth_carried_forward={fmt_bool(cert['endpoint_orbit_amplitude_depth_carried_forward'])}",
        f"endpoint_orbit_variation_boundary_flux_carried_forward={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_carried_forward'])}",
        f"endpoint_orbit_comparable_plateau_same_sign_load_closed={fmt_bool(cert['endpoint_orbit_comparable_plateau_same_sign_load_closed'])}",
        f"endpoint_orbit_plateau_length_budget_dichotomy_closed={fmt_bool(cert['endpoint_orbit_plateau_length_budget_dichotomy_closed'])}",
        f"endpoint_orbit_short_plateau_edge_spike_absorption_closed={fmt_bool(cert['endpoint_orbit_short_plateau_edge_spike_absorption_closed'])}",
        f"endpoint_orbit_long_plateau_monotone_ramp_packet_registered={fmt_bool(cert['endpoint_orbit_long_plateau_monotone_ramp_packet_registered'])}",
        f"anonymous_comparable_amplitude_plateau_drift_removed={fmt_bool(cert['anonymous_comparable_amplitude_plateau_drift_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_plateau_ramp_potential_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_plateau_ramp_potential_pdec_cap_proved'])}",
        f"endpoint_orbit_amplitude_depth_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_amplitude_depth_pdec_cap_proved'])}",
        f"endpoint_orbit_variation_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_variation_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. plateau 模型",
        "",
        "上一层可比较幅度 plateau 支路给出连续弧 `P_s`：",
        "",
        "```text",
        "Z_j=sigma*Y_j>0,  a<=Z_j<2a,  sum_{j in P_s}Z_j>=H0.",
        "```",
        "",
        "这保留了真实链的相位方向：不是只知道总质量大，而是知道质量集中在同一连续弧、同一符号、同一 dyadic 幅度层。",
        "",
        "## 2. 长度预算二分",
        "",
        "给定长度预算 `L0>=1`。若 `|P_s|<=L0`，则：",
        "",
        "```text",
        "max_{j in P_s} Z_j >= H0/L0.",
        "```",
        "",
        "这是一条 edge-spike。沿用已归档的中心化展开 `Y_j=X_j-mu` 与半阈值二分，短 plateau 被吸收到 endpoint singleton atom 或 full-cycle mean atom。",
        "",
        "若 `|P_s|>L0`，则 prefix potential",
        "",
        "```text",
        "S(t)=sum_{i<=t} sigma*Y_i",
        "```",
        "",
        "在 `P_s` 上逐步单调爬升，并且跨越总高度至少 `H0`。这不是匿名 plateau drift，而是长弧单调 ramp potential 包。",
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余不再是匿名 comparable-amplitude plateau drift，而是 plateau-ramp potential，外加 amplitude-depth、boundary flux、singleton、full-cycle mean 与 sparse SAE。",
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
            "- 本证书没有证明 EndpointOrbitPlateauRampPotentialPDECCap。",
            "- 本证书没有证明 EndpointOrbitAmplitudeDepthPDECCap。",
            "- 本证书没有证明 EndpointOrbitVariationBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 comparable-amplitude plateau drift 压成短原子吸收或长单调 ramp potential。",
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
