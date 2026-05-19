#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit single-lobe 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_lobe_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap"
)

IMPORT = "StableLadderEndpointOrbitAxisLobeWeightedSurplusImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingleLobeLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingleLobeLedger"
TWO_LOBE = "StableLadderEndpointOrbitTwoLobeSurplusDecompositionLedger"
HALF_DROP = "StableLadderEndpointOrbitHalfThresholdLossLedger"
SINGLE_CHOICE = "StableLadderEndpointOrbitSingleLobeSignChoiceLedger"
SUPPORT = "StableLadderEndpointOrbitSingleLobeHalfCircleSupportLedger"
PACKET = "StableLadderEndpointOrbitSingleLobeSignedSurplusPacketLedger"
NO_ANON = "NoAnonymousAxisLobeDifferenceExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterSingleLobeLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {TWO_LOBE} "
    f"AND {HALF_DROP} AND {SINGLE_CHOICE} AND {SUPPORT} AND {PACKET} "
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
    """把旧活动基中的 axis-lobe 硬点替换成 single-lobe 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit single-lobe 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitAxisLobeWeightedSurplusImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、axis-lobe weighted surplus cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingleLobe",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingleLobe",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其全局可求和。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitTwoLobeSurplusDecomposition",
            True,
            True,
            "把 axis-lobe surplus 写成 A-B，其中 A=sum S_a w_a、B=sum S_a v_a。",
            TWO_LOBE,
        ),
        row(
            "StableLadderEndpointOrbitHalfThresholdLoss",
            True,
            True,
            "若 A-B>=L，则 A>=L/2 或 -B>=L/2，至多损失常数 2。",
            HALF_DROP,
        ),
        row(
            "StableLadderEndpointOrbitSingleLobeSignChoice",
            True,
            True,
            "选择 W=w,eta=+1 或 W=v,eta=-1，使 sum eta*S_a*W_a>=L/2。",
            SINGLE_CHOICE,
        ),
        row(
            "StableLadderEndpointOrbitSingleLobeHalfCircleSupport",
            True,
            True,
            "所选 W 非负、由单个三角叶片给出，并支撑在一个轴向半圆上。",
            SUPPORT,
        ),
        row(
            "StableLadderEndpointOrbitSingleLobeSignedSurplusPacket",
            True,
            False,
            "axis-lobe cap 被登记为单叶片带符号盈余包；本步不排斥该 cap。",
            PACKET,
        ),
        row(
            "NoAnonymousAxisLobeDifferenceExit",
            True,
            True,
            "剩余不再是 w-v 的双叶片差异；它有单个叶片 W 和一个符号 eta。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterSingleLobe",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitSingleLobeSignedSurplusCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、single-lobe signed surplus PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、single-lobe cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit single-lobe 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "axis-lobe weighted surplus 给出两个相反半圆叶片的差 A-B>=L。"
        "若正叶片 A 本身未达到 L/2，则负叶片必须满足 -B>=L/2。"
        "因此可以选择一个半圆叶片 W 和一个符号 eta，使 sum eta*S_a*W_a>=L/2。"
        "剩余从双叶片差异进一步压成单叶片带符号盈余 PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_lobe_router",
        "status": "endpoint_orbit_axis_lobe_surplus_reduced_to_single_lobe_signed_surplus_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_axis_lobe_weighted_surplus_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_two_lobe_surplus_decomposition_closed": True,
        "endpoint_orbit_half_threshold_loss_closed": True,
        "endpoint_orbit_single_lobe_sign_choice_closed": True,
        "endpoint_orbit_single_lobe_half_circle_support_closed": True,
        "endpoint_orbit_single_lobe_signed_surplus_packet_registered": True,
        "anonymous_axis_lobe_difference_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_single_lobe_signed_surplus_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "single_lobe_formulas": {
            "previous_packet": "sum_a S_a*(w_a-v_a)>=L, w_a,v_a>=0",
            "positive_lobe_mass": "A=sum_a S_a*w_a",
            "negative_lobe_mass": "B=sum_a S_a*v_a",
            "two_lobe_surplus": "A-B>=L",
            "half_threshold": "A>=L/2 OR -B>=L/2",
            "single_choice_positive": "if A>=L/2: W=w, eta=+1",
            "single_choice_negative": "if A<L/2: W=v, eta=-1",
            "single_lobe_surplus": "sum_a eta*S_a*W_a>=L/2",
            "support": "W is supported on one axis half-circle and 0<=W_a<=1",
            "new_exit": "EndpointOrbitSingleLobeSignedSurplusPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit single-lobe 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_axis_lobe_weighted_surplus_imported={fmt_bool(cert['endpoint_orbit_axis_lobe_weighted_surplus_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_two_lobe_surplus_decomposition_closed={fmt_bool(cert['endpoint_orbit_two_lobe_surplus_decomposition_closed'])}",
        f"endpoint_orbit_half_threshold_loss_closed={fmt_bool(cert['endpoint_orbit_half_threshold_loss_closed'])}",
        f"endpoint_orbit_single_lobe_sign_choice_closed={fmt_bool(cert['endpoint_orbit_single_lobe_sign_choice_closed'])}",
        f"endpoint_orbit_single_lobe_half_circle_support_closed={fmt_bool(cert['endpoint_orbit_single_lobe_half_circle_support_closed'])}",
        f"endpoint_orbit_single_lobe_signed_surplus_packet_registered={fmt_bool(cert['endpoint_orbit_single_lobe_signed_surplus_packet_registered'])}",
        f"anonymous_axis_lobe_difference_removed={fmt_bool(cert['anonymous_axis_lobe_difference_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_single_lobe_signed_surplus_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_single_lobe_signed_surplus_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 双叶片差异",
        "",
        "上一层给出的 axis-lobe packet 为：",
        "",
        "```text",
        "sum_a S_a*(w_a-v_a) >= L,",
        "w_a>=0, v_a>=0.",
        "```",
        "",
        "记：",
        "",
        "```text",
        "A=sum_a S_a*w_a,",
        "B=sum_a S_a*v_a.",
        "```",
        "",
        "则：",
        "",
        "```text",
        "A-B >= L.",
        "```",
        "",
        "## 2. 单叶片二分",
        "",
        "若 `A>=L/2`，选择 `W=w` 与 `eta=+1`。否则 `A<L/2`，由 `A-B>=L` 得到 `-B>L/2`，选择 `W=v` 与 `eta=-1`。所以必有：",
        "",
        "```text",
        "sum_a eta*S_a*W_a >= L/2.",
        "```",
        "",
        "## 3. 支撑与常数",
        "",
        "所选 `W` 是单个三角叶片权重，满足：",
        "",
        "```text",
        "0 <= W_a <= 1,",
        "supp(W) is one axis half-circle.",
        "```",
        "",
        "因此双叶片差异只损失常数 `2`，被压成单叶片带符号盈余包。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 axis-lobe weighted surplus PDEC/cap 变成 single-lobe signed surplus PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitSingleLobeSignedSurplusPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 axis-lobe weighted surplus cap 压成单叶片带符号盈余包。",
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
