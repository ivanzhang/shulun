#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit single-arc 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_arc_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap"
)

IMPORT = "StableLadderEndpointOrbitSingleLobeSignedSurplusImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingleArcLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingleArcLedger"
LAYER = "StableLadderEndpointOrbitSingleLobeLayerCakeIdentityLedger"
ARC_SUPPORT = "StableLadderEndpointOrbitLobeSuperlevelArcSupportLedger"
PIGEONHOLE = "StableLadderEndpointOrbitLayerCakeArcPigeonholeLedger"
PACKET = "StableLadderEndpointOrbitSingleArcSignedSurplusPacketLedger"
NO_ANON = "NoAnonymousSingleLobeWeightExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterSingleArcLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {LAYER} "
    f"AND {ARC_SUPPORT} AND {PIGEONHOLE} AND {PACKET} "
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
    """把旧活动基中的 single-lobe 硬点替换成 single-arc 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit single-arc 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitSingleLobeSignedSurplusImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、single-lobe signed surplus cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingleArc",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingleArc",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其全局可求和。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitSingleLobeLayerCakeIdentity",
            True,
            True,
            "对 0<=W<=1，逐点有 W_a=int_0^1 1_{W_a>=t} dt。",
            LAYER,
        ),
        row(
            "StableLadderEndpointOrbitLobeSuperlevelArcSupport",
            True,
            True,
            "单三角叶片的每个非空超水平集 {W_a>=t} 是同一轴向半圆内的一个循环弧。",
            ARC_SUPPORT,
        ),
        row(
            "StableLadderEndpointOrbitLayerCakeArcPigeonhole",
            True,
            True,
            "若 int_0^1 H(t)dt>=L，则存在 t 使 H(t)>=L，其中 H(t)=sum_{W_a>=t} eta*S_a。",
            PIGEONHOLE,
        ),
        row(
            "StableLadderEndpointOrbitSingleArcSignedSurplusPacket",
            True,
            False,
            "single-lobe cap 被登记为单弧 signed surplus 包；本步不排斥该 cap。",
            PACKET,
        ),
        row(
            "NoAnonymousSingleLobeWeightExit",
            True,
            True,
            "剩余不再含连续叶片权重 W；它被压成某个超水平单弧 A_t。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterSingleArc",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitSingleArcSignedSurplusCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、single-arc signed surplus PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、single-arc cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit single-arc 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "single-lobe signed surplus 给出 sum eta*S_a*W_a>=L，其中 0<=W<=1 且 W 支撑在一个半圆叶片上。"
        "用 layer-cake 恒等式 W_a=int_0^1 1_{W_a>=t}dt，可把加权和写成超水平集 signed mass 的积分。"
        "因此存在某个阈值 t，使单个超水平弧 A_t={a:W_a>=t} 满足 sum_{a in A_t} eta*S_a>=L。"
        "剩余从加权叶片 cap 进一步压成单弧 signed surplus PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_arc_router",
        "status": "endpoint_orbit_single_lobe_surplus_reduced_to_single_arc_signed_surplus_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_single_lobe_signed_surplus_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_single_lobe_layer_cake_identity_closed": True,
        "endpoint_orbit_lobe_superlevel_arc_support_closed": True,
        "endpoint_orbit_layer_cake_arc_pigeonhole_closed": True,
        "endpoint_orbit_single_arc_signed_surplus_packet_registered": True,
        "anonymous_single_lobe_weight_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_single_arc_signed_surplus_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "single_arc_formulas": {
            "previous_packet": "sum_a eta*S_a*W_a>=L, 0<=W_a<=1",
            "layer_cake": "W_a=int_0^1 1_{W_a>=t} dt",
            "integral_identity": "sum_a eta*S_a*W_a=int_0^1 H(t) dt",
            "level_mass": "H(t)=sum_{a: W_a>=t} eta*S_a",
            "pigeonhole": "exists t in [0,1]: H(t)>=L",
            "arc": "A_t={a mod m: W_a>=t}",
            "arc_support": "A_t is a cyclic arc inside one axis half-circle",
            "single_arc_surplus": "sum_{a in A_t} eta*S_a>=L",
            "new_exit": "EndpointOrbitSingleArcSignedSurplusPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit single-arc 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_single_lobe_signed_surplus_imported={fmt_bool(cert['endpoint_orbit_single_lobe_signed_surplus_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_single_lobe_layer_cake_identity_closed={fmt_bool(cert['endpoint_orbit_single_lobe_layer_cake_identity_closed'])}",
        f"endpoint_orbit_lobe_superlevel_arc_support_closed={fmt_bool(cert['endpoint_orbit_lobe_superlevel_arc_support_closed'])}",
        f"endpoint_orbit_layer_cake_arc_pigeonhole_closed={fmt_bool(cert['endpoint_orbit_layer_cake_arc_pigeonhole_closed'])}",
        f"endpoint_orbit_single_arc_signed_surplus_packet_registered={fmt_bool(cert['endpoint_orbit_single_arc_signed_surplus_packet_registered'])}",
        f"anonymous_single_lobe_weight_removed={fmt_bool(cert['anonymous_single_lobe_weight_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_single_arc_signed_surplus_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_single_arc_signed_surplus_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单叶片加权包",
        "",
        "上一层给出：",
        "",
        "```text",
        "sum_a eta*S_a*W_a >= L,",
        "0 <= W_a <= 1.",
        "```",
        "",
        "其中 `W` 是单个三角半圆叶片权重。",
        "",
        "## 2. layer-cake 恒等式",
        "",
        "逐点有：",
        "",
        "```text",
        "W_a = int_0^1 1_{W_a>=t} dt.",
        "```",
        "",
        "所以：",
        "",
        "```text",
        "sum_a eta*S_a*W_a = int_0^1 H(t) dt,",
        "H(t)=sum_{a: W_a>=t} eta*S_a.",
        "```",
        "",
        "若积分至少为 `L`，则存在阈值 `t` 使：",
        "",
        "```text",
        "H(t) >= L.",
        "```",
        "",
        "## 3. 超水平单弧",
        "",
        "对单个三角叶片，超水平集：",
        "",
        "```text",
        "A_t={a mod m: W_a>=t}",
        "```",
        "",
        "是一个位于同一轴向半圆内的循环弧。因此得到：",
        "",
        "```text",
        "sum_{a in A_t} eta*S_a >= L.",
        "```",
        "",
        "这就是新的 single-arc signed surplus packet。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 single-lobe signed surplus PDEC/cap 变成 single-arc signed surplus PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitSingleArcSignedSurplusPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 single-lobe signed surplus cap 压成单弧 signed surplus 包。",
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
