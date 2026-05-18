#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit conductor-character 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_conductor_character_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap"
)

IMPORT = "StableLadderEndpointOrbitSignedFourierImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterConductorLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardLedger"
NONZERO = "StableLadderEndpointOrbitNonzeroFrequencyConductorLedger"
KERNEL = "StableLadderEndpointOrbitFrequencyKernelQuotientLedger"
COLLAPSE = "StableLadderEndpointOrbitKernelFiberCollapseLedger"
PRIMITIVE = "StableLadderEndpointOrbitPrimitiveConductorCharacterPacketLedger"
DERIVATIVE = "StableLadderEndpointOrbitDerivativeMultiplierAbsorbedLedger"
NO_ANON = "NoAnonymousEndpointOrbitSignedFourierExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterOrbitConductorLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {NONZERO} "
    f"AND {KERNEL} AND {COLLAPSE} AND {PRIMITIVE} AND {DERIVATIVE} "
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
    """把旧活动基中的 signed Fourier 硬点替换成 conductor-character 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit conductor-character 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitSignedFourierImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、signed Fourier cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterConductor",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForward",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其全局可求和。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitNonzeroFrequencyConductor",
            True,
            True,
            "对非零频率 h，令 d=gcd(h,r)、m=r/d>1、h0=h/d，则 gcd(h0,m)=1。",
            NONZERO,
        ),
        row(
            "StableLadderEndpointOrbitFrequencyKernelQuotient",
            True,
            True,
            "角色 e(-ht/r) 的 kernel 大小为 d，并因子化到导子商 C_m。",
            KERNEL,
        ),
        row(
            "StableLadderEndpointOrbitKernelFiberCollapse",
            True,
            True,
            "把 g_t 沿 kernel 纤维精确折叠为 G_s=sum_{u=0}^{d-1}g_{s+um}。",
            COLLAPSE,
        ),
        row(
            "StableLadderEndpointOrbitPrimitiveConductorCharacterPacket",
            True,
            False,
            "signed Fourier cap 被登记为 C_m 上的 primitive additive character packet；本步不排斥该 cap。",
            PRIMITIVE,
        ),
        row(
            "StableLadderEndpointOrbitDerivativeMultiplierAbsorbed",
            True,
            True,
            "derivative Fourier 下界可用 |omega^h-1|<=2 转为普通 signed Fourier 下界，常数损失已登记。",
            DERIVATIVE,
        ),
        row(
            "NoAnonymousEndpointOrbitSignedFourierExit",
            True,
            True,
            "匿名 signed Fourier 频率被压成唯一 conductor m 与 primitive 频率 h0。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterOrbitConductor",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPrimitiveConductorCharacterCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、primitive conductor character PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、primitive conductor character 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit conductor-character 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "endpoint orbit signed Fourier cap 的非零频率 h 可按 d=gcd(h,r) "
        "归约到导子 m=r/d 上的 primitive additive character。"
        "原轨道函数 g_t 沿 kernel 纤维精确折叠为 G_s，且 hat g(h)=sum_s G_s e(-h0*s/m)。"
        "derivative Fourier 分支只损失常数即可回到同一 Fourier 下界。"
        "因此剩余不再是匿名 signed Fourier 频率，而是 primitive conductor character/PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_conductor_character_router",
        "status": "endpoint_orbit_signed_fourier_reduced_to_primitive_conductor_character_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_signed_fourier_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_nonzero_frequency_conductor_closed": True,
        "endpoint_orbit_frequency_kernel_quotient_closed": True,
        "endpoint_orbit_kernel_fiber_collapse_closed": True,
        "endpoint_orbit_primitive_conductor_character_packet_registered": True,
        "endpoint_orbit_derivative_multiplier_absorbed": True,
        "anonymous_endpoint_orbit_signed_fourier_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_primitive_conductor_character_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "conductor_formulas": {
            "frequency": "1<=h<=r-1",
            "conductor": "d=gcd(h,r), m=r/d>1, h0=h/d, gcd(h0,m)=1",
            "character_factorization": "exp(-2*pi*i*h*t/r)=exp(-2*pi*i*h0*(t mod m)/m)",
            "kernel": "ker eta_h={0,m,2m,...,(d-1)m}, |ker|=d",
            "quotient": "C_r/ker eta_h ~= C_m",
            "collapsed_load": "G_s=sum_{u=0}^{d-1} g_{s+u*m}",
            "exact_identity": "hat g(h)=sum_{s mod m} G_s exp(-2*pi*i*h0*s/m)",
            "primitive_character": "s -> exp(-2*pi*i*h0*s/m) is primitive on C_m",
            "derivative_absorption": "|(omega_r^h-1)hat g(h)|>=M => |hat g(h)|>=M/2",
            "new_exit": "EndpointOrbitPrimitiveConductorCharacterPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit conductor-character 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_signed_fourier_imported={fmt_bool(cert['endpoint_orbit_signed_fourier_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_nonzero_frequency_conductor_closed={fmt_bool(cert['endpoint_orbit_nonzero_frequency_conductor_closed'])}",
        f"endpoint_orbit_frequency_kernel_quotient_closed={fmt_bool(cert['endpoint_orbit_frequency_kernel_quotient_closed'])}",
        f"endpoint_orbit_kernel_fiber_collapse_closed={fmt_bool(cert['endpoint_orbit_kernel_fiber_collapse_closed'])}",
        f"endpoint_orbit_primitive_conductor_character_packet_registered={fmt_bool(cert['endpoint_orbit_primitive_conductor_character_packet_registered'])}",
        f"endpoint_orbit_derivative_multiplier_absorbed={fmt_bool(cert['endpoint_orbit_derivative_multiplier_absorbed'])}",
        f"anonymous_endpoint_orbit_signed_fourier_removed={fmt_bool(cert['anonymous_endpoint_orbit_signed_fourier_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_primitive_conductor_character_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_primitive_conductor_character_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非零频率的导子",
        "",
        "上一层 signed Fourier 出口给出某个非零频率 `h`。令：",
        "",
        "```text",
        "1 <= h <= r-1,",
        "d=gcd(h,r),",
        "m=r/d>1,",
        "h0=h/d, gcd(h0,m)=1.",
        "```",
        "",
        "于是：",
        "",
        "```text",
        "exp(-2*pi*i*h*t/r)=exp(-2*pi*i*h0*(t mod m)/m).",
        "```",
        "",
        "## 2. kernel 纤维折叠",
        "",
        "该角色在 `C_r` 上的 kernel 为：",
        "",
        "```text",
        "ker eta_h={0,m,2m,...,(d-1)m},",
        "|ker eta_h|=d,",
        "C_r/ker eta_h ~= C_m.",
        "```",
        "",
        "把有符号负载沿 kernel 纤维折叠：",
        "",
        "```text",
        "G_s=sum_{u=0}^{d-1} g_{s+u*m},  s in Z/mZ.",
        "```",
        "",
        "则 Fourier 和精确变为 primitive conductor character packet：",
        "",
        "```text",
        "hat g(h)=sum_{s mod m} G_s exp(-2*pi*i*h0*s/m).",
        "```",
        "",
        "由于 `gcd(h0,m)=1`，该 additive character 在 `C_m` 上是 primitive。",
        "",
        "## 3. derivative Fourier 的常数吸收",
        "",
        "若上一层给出的是 derivative Fourier 下界，则：",
        "",
        "```text",
        "|(omega_r^h-1)hat g(h)| >= M.",
        "```",
        "",
        "因 `h!=0` 且 `|omega_r^h-1|<=2`，得到：",
        "",
        "```text",
        "|hat g(h)| >= M/2.",
        "```",
        "",
        "所以 long-arc Fourier 与 boundary derivative Fourier 都进入同一个 conductor-character 出口。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从匿名 signed Fourier cap 变成 primitive conductor character PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitPrimitiveConductorCharacterPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 signed Fourier 频率压成 primitive conductor character packet。",
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
