#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit arc endpoint-potential 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_arc_endpoint_potential_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap"
)

IMPORT = "StableLadderEndpointOrbitSingleArcSignedSurplusImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterArcEndpointPotentialLedger"
SIGNED_LOAD = "StableLadderEndpointOrbitArcSignedLoadSequenceLedger"
MEAN_SPLIT = "StableLadderEndpointOrbitArcMeanContributionDichotomyLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterArcEndpointPotentialLedger"
CENTERED = "StableLadderEndpointOrbitCenteredArcSurplusLedger"
PREFIX = "StableLadderEndpointOrbitCenteredPrefixPotentialLedger"
GAP = "StableLadderEndpointOrbitArcEndpointPotentialGapLedger"
PACKET = "StableLadderEndpointOrbitArcEndpointPotentialPacketLedger"
NO_ANON = "NoAnonymousSingleArcInteriorSurplusExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterArcEndpointPotentialLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {SIGNED_LOAD} AND {MEAN_SPLIT} "
    f"AND {FULL_MEAN} AND {CENTERED} AND {PREFIX} AND {GAP} "
    f"AND {PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 single-arc 硬点替换成 endpoint-potential 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit arc endpoint-potential 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitSingleArcSignedSurplusImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、single-arc signed surplus cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterArcEndpointPotential",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitArcSignedLoadSequence",
            True,
            True,
            "在轨道 C_m 上固定 X_a=eta*S_a，并把单弧写成 A=[u,v)。",
            SIGNED_LOAD,
        ),
        row(
            "StableLadderEndpointOrbitArcMeanContributionDichotomy",
            True,
            True,
            "把弧和分解为 |A|*mu 与中心化弧差；均值项若承担半数负载则进入 full-cycle mean atom。",
            MEAN_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterArcEndpointPotential",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步只识别该出口，不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitCenteredArcSurplus",
            True,
            True,
            "若均值项未承担半数负载，则中心化载荷 Y_a=X_a-mu 在同一弧上仍有 >=L/2 的盈余。",
            CENTERED,
        ),
        row(
            "StableLadderEndpointOrbitCenteredPrefixPotential",
            True,
            True,
            "定义 F(0)=0, F(j+1)=F(j)+Y_j，且 F(m)=0；中心化弧和等于 F(v)-F(u)。",
            PREFIX,
        ),
        row(
            "StableLadderEndpointOrbitArcEndpointPotentialGap",
            True,
            True,
            "F(v)-F(u)>=L/2 强制两个弧端点之间存在 >=L/2 的势能差。",
            GAP,
        ),
        row(
            "StableLadderEndpointOrbitArcEndpointPotentialPacket",
            True,
            False,
            "single-arc cap 被登记为端点势能差包；本步不排斥该 cap。",
            PACKET,
        ),
        row(
            "NoAnonymousSingleArcInteriorSurplusExit",
            True,
            True,
            "剩余不再是匿名弧内部盈余，而是 full-cycle mean atom 或端点势能差 PDEC/cap。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterArcEndpointPotential",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitArcEndpointPotentialCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、arc endpoint-potential PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、endpoint-potential cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit arc endpoint-potential 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "single-arc signed surplus 给出 sum_{a in A} X_a>=L，其中 X_a=eta*S_a。"
        "令 mu=m^{-1}sum_{C_m}X_a, Y_a=X_a-mu。弧和等于 |A|mu 加中心化弧差。"
        "若均值贡献承担半数负载，则这是 full-cycle mean atom 出口；否则中心化弧差至少 L/2。"
        "中心化前缀势能 F 满足 sum_A Y=F(v)-F(u)，故剩余被压成两个弧端点之间的势能差 PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_arc_endpoint_potential_router",
        "status": "endpoint_orbit_single_arc_surplus_reduced_to_mean_or_endpoint_potential_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_single_arc_signed_surplus_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_arc_signed_load_sequence_closed": True,
        "endpoint_orbit_arc_mean_contribution_dichotomy_closed": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_centered_arc_surplus_closed": True,
        "endpoint_orbit_centered_prefix_potential_closed": True,
        "endpoint_orbit_arc_endpoint_potential_gap_closed": True,
        "endpoint_orbit_arc_endpoint_potential_packet_registered": True,
        "anonymous_single_arc_interior_surplus_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_arc_endpoint_potential_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "arc_endpoint_potential_formulas": {
            "previous_packet": "sum_{a in A} X_a>=L, X_a=eta*S_a",
            "mean": "mu=(1/m) sum_{a in C_m} X_a",
            "centered_load": "Y_a=X_a-mu, sum_{a in C_m}Y_a=0",
            "arc_decomposition": "sum_{a in A}X_a=|A|*mu+sum_{a in A}Y_a",
            "mean_outlet": "if |A|*mu>=L/2 then m*mu>=L/2 because |A|<=m",
            "centered_arc": "otherwise sum_{a in A}Y_a>=L/2",
            "prefix_potential": "F(0)=0, F(j+1)=F(j)+Y_j, F(m)=0",
            "endpoint_gap": "for A=[u,v), sum_{a in A}Y_a=F(v)-F(u)>=L/2",
            "new_exit": "EndpointOrbitArcEndpointPotentialPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit arc endpoint-potential 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_single_arc_signed_surplus_imported={fmt_bool(cert['endpoint_orbit_single_arc_signed_surplus_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_arc_signed_load_sequence_closed={fmt_bool(cert['endpoint_orbit_arc_signed_load_sequence_closed'])}",
        f"endpoint_orbit_arc_mean_contribution_dichotomy_closed={fmt_bool(cert['endpoint_orbit_arc_mean_contribution_dichotomy_closed'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_centered_arc_surplus_closed={fmt_bool(cert['endpoint_orbit_centered_arc_surplus_closed'])}",
        f"endpoint_orbit_centered_prefix_potential_closed={fmt_bool(cert['endpoint_orbit_centered_prefix_potential_closed'])}",
        f"endpoint_orbit_arc_endpoint_potential_gap_closed={fmt_bool(cert['endpoint_orbit_arc_endpoint_potential_gap_closed'])}",
        f"endpoint_orbit_arc_endpoint_potential_packet_registered={fmt_bool(cert['endpoint_orbit_arc_endpoint_potential_packet_registered'])}",
        f"anonymous_single_arc_interior_surplus_removed={fmt_bool(cert['anonymous_single_arc_interior_surplus_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_arc_endpoint_potential_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_arc_endpoint_potential_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单弧 signed surplus 包",
        "",
        "上一层给出：",
        "",
        "```text",
        "sum_{a in A} X_a >= L,",
        "X_a = eta*S_a,  A=[u,v) subset C_m.",
        "```",
        "",
        "## 2. 均值/中心化分解",
        "",
        "令：",
        "",
        "```text",
        "mu=(1/m) sum_{a in C_m} X_a,",
        "Y_a=X_a-mu.",
        "```",
        "",
        "于是：",
        "",
        "```text",
        "sum_{a in A} X_a = |A|*mu + sum_{a in A} Y_a.",
        "```",
        "",
        "若 `|A|*mu>=L/2`，因为 `|A|<=m`，得到 `m*mu>=L/2`，登记为 full-cycle mean atom 出口。否则：",
        "",
        "```text",
        "sum_{a in A} Y_a >= L/2.",
        "```",
        "",
        "## 3. 端点势能差",
        "",
        "定义中心化前缀势能：",
        "",
        "```text",
        "F(0)=0,",
        "F(j+1)=F(j)+Y_j,",
        "F(m)=0.",
        "```",
        "",
        "对弧 `A=[u,v)`，有：",
        "",
        "```text",
        "sum_{a in A}Y_a = F(v)-F(u).",
        "```",
        "",
        "因此若均值出口不承担负载，则两个弧端点强制满足：",
        "",
        "```text",
        "F(v)-F(u) >= L/2.",
        "```",
        "",
        "这就是新的 arc endpoint-potential packet。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 single-arc signed surplus PDEC/cap 变成 arc endpoint-potential PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitArcEndpointPotentialPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 single-arc signed surplus cap 压成 full-cycle mean atom 或端点势能差包。",
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
