#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit axis-lobe 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_axis_lobe_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap"
)

IMPORT = "StableLadderEndpointOrbitStandardFirstHarmonicImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterAxisLobeLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterAxisLobeLedger"
AMPLITUDE = "StableLadderEndpointOrbitComplexFirstHarmonicAmplitudeLedger"
AXIS = "StableLadderEndpointOrbitAxisProjectionDichotomyLedger"
SIGN = "StableLadderEndpointOrbitAxisSignChoiceLedger"
LOBE = "StableLadderEndpointOrbitTrigonometricLobeWeightLedger"
SURPLUS = "StableLadderEndpointOrbitAxisLobeWeightedSurplusPacketLedger"
NO_ANON = "NoAnonymousStandardFirstHarmonicExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterAxisLobeLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {AMPLITUDE} "
    f"AND {AXIS} AND {SIGN} AND {LOBE} AND {SURPLUS} "
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
    """把旧活动基中的 standard first-harmonic 硬点替换成 axis-lobe 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit axis-lobe 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitStandardFirstHarmonicImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、standard first-harmonic cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterAxisLobe",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterAxisLobe",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其全局可求和。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitComplexFirstHarmonicAmplitude",
            True,
            True,
            "标准 first harmonic 写成 F=sum_a S_a exp(-2*pi*i*a/m)，并保留 |F| 下界。",
            AMPLITUDE,
        ),
        row(
            "StableLadderEndpointOrbitAxisProjectionDichotomy",
            True,
            True,
            "由 |F|^2=(Re F)^2+(Im F)^2，至少一个坐标投影有 |.|>=|F|/sqrt(2)。",
            AXIS,
        ),
        row(
            "StableLadderEndpointOrbitAxisSignChoice",
            True,
            True,
            "选 j in {0,1} 和 eps in {+1,-1}，使 sum_a S_a eps*phi_j(a) 达到正下界。",
            SIGN,
        ),
        row(
            "StableLadderEndpointOrbitTrigonometricLobeWeight",
            True,
            True,
            "把 eps*phi_j 分解为正负半圆叶片权重 w-v，其中 w,v>=0 且支撑为轴向半圆。",
            LOBE,
        ),
        row(
            "StableLadderEndpointOrbitAxisLobeWeightedSurplusPacket",
            True,
            False,
            "standard first-harmonic cap 被登记为显式 axis-lobe 加权盈余包；本步不排斥该 cap。",
            SURPLUS,
        ),
        row(
            "NoAnonymousStandardFirstHarmonicExit",
            True,
            True,
            "剩余不再是复数 Fourier 下界；它被压成某个轴、符号和半圆叶片权重包。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterAxisLobe",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitAxisLobeWeightedSurplusCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、axis-lobe weighted surplus PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、axis-lobe cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit axis-lobe 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "standard conductor first-harmonic cap 给出 F=sum_a S_a e(-a/m) 的复数下界。"
        "把 F 分解为实部和虚部后，至少一个坐标投影保留 |F|/sqrt(2) 的下界。"
        "再选择符号并把对应三角函数分解为正负半圆叶片权重，得到显式 axis-lobe 加权盈余包。"
        "因此剩余不再是匿名复数 first-harmonic cap，而是有轴向、符号和半圆权重的实变量 PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_axis_lobe_router",
        "status": "endpoint_orbit_standard_first_harmonic_reduced_to_axis_lobe_weighted_surplus_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_standard_first_harmonic_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_complex_first_harmonic_amplitude_closed": True,
        "endpoint_orbit_axis_projection_dichotomy_closed": True,
        "endpoint_orbit_axis_sign_choice_closed": True,
        "endpoint_orbit_trigonometric_lobe_weight_closed": True,
        "endpoint_orbit_axis_lobe_weighted_surplus_packet_registered": True,
        "anonymous_standard_first_harmonic_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_axis_lobe_weighted_surplus_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "axis_lobe_formulas": {
            "previous_packet": "F=sum_{a mod m} S_a exp(-2*pi*i*a/m), |F|>=M",
            "real_imaginary": "Re F=sum_a S_a cos(2*pi*a/m), Im F=-sum_a S_a sin(2*pi*a/m)",
            "axis_projection": "max(|Re F|,|Im F|)>=M/sqrt(2)",
            "axis_functions": "phi_0(a)=cos(2*pi*a/m), phi_1(a)=-sin(2*pi*a/m)",
            "sign_choice": "exists j in {0,1}, eps in {+1,-1}: sum_a S_a eps*phi_j(a)>=M/sqrt(2)",
            "lobe_weights": "w_a=max(eps*phi_j(a),0), v_a=max(-eps*phi_j(a),0)",
            "weighted_surplus": "sum_a S_a*(w_a-v_a)>=M/sqrt(2)",
            "lobe_support": "supp(w) and supp(v) are opposite axis half-circles on C_m",
            "new_exit": "EndpointOrbitAxisLobeWeightedSurplusPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit axis-lobe 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_standard_first_harmonic_imported={fmt_bool(cert['endpoint_orbit_standard_first_harmonic_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_complex_first_harmonic_amplitude_closed={fmt_bool(cert['endpoint_orbit_complex_first_harmonic_amplitude_closed'])}",
        f"endpoint_orbit_axis_projection_dichotomy_closed={fmt_bool(cert['endpoint_orbit_axis_projection_dichotomy_closed'])}",
        f"endpoint_orbit_axis_sign_choice_closed={fmt_bool(cert['endpoint_orbit_axis_sign_choice_closed'])}",
        f"endpoint_orbit_trigonometric_lobe_weight_closed={fmt_bool(cert['endpoint_orbit_trigonometric_lobe_weight_closed'])}",
        f"endpoint_orbit_axis_lobe_weighted_surplus_packet_registered={fmt_bool(cert['endpoint_orbit_axis_lobe_weighted_surplus_packet_registered'])}",
        f"anonymous_standard_first_harmonic_removed={fmt_bool(cert['anonymous_standard_first_harmonic_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_axis_lobe_weighted_surplus_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_axis_lobe_weighted_surplus_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 复数 first harmonic",
        "",
        "上一层给出的标准 conductor packet 为：",
        "",
        "```text",
        "F=sum_{a mod m} S_a exp(-2*pi*i*a/m),",
        "|F|>=M.",
        "```",
        "",
        "其坐标投影是：",
        "",
        "```text",
        "Re F=sum_a S_a cos(2*pi*a/m),",
        "Im F=-sum_a S_a sin(2*pi*a/m).",
        "```",
        "",
        "## 2. 轴向投影二分",
        "",
        "由 `|F|^2=(Re F)^2+(Im F)^2`，必有：",
        "",
        "```text",
        "max(|Re F|, |Im F|) >= M/sqrt(2).",
        "```",
        "",
        "令：",
        "",
        "```text",
        "phi_0(a)=cos(2*pi*a/m),",
        "phi_1(a)=-sin(2*pi*a/m).",
        "```",
        "",
        "于是存在 `j in {0,1}` 与 `eps in {+1,-1}`，使：",
        "",
        "```text",
        "sum_a S_a eps*phi_j(a) >= M/sqrt(2).",
        "```",
        "",
        "## 3. 半圆叶片权重",
        "",
        "把所选三角函数拆成正负叶片：",
        "",
        "```text",
        "w_a=max(eps*phi_j(a),0),",
        "v_a=max(-eps*phi_j(a),0).",
        "```",
        "",
        "则 `w` 与 `v` 支撑在相反的轴向半圆上，并且：",
        "",
        "```text",
        "sum_a S_a*(w_a-v_a) >= M/sqrt(2).",
        "```",
        "",
        "这就是新的显式 axis-lobe weighted surplus packet。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 standard conductor first-harmonic cap 变成 axis-lobe weighted surplus PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitAxisLobeWeightedSurplusPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 standard first-harmonic cap 压成轴向半圆叶片加权盈余包。",
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
