#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit standard-character 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_standard_character_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPrimitiveConductorCharacterImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterStandardCharacterLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStandardCharacterLedger"
UNIT_AUTO = "StableLadderEndpointOrbitConductorUnitAutomorphismLedger"
STANDARD_COORD = "StableLadderEndpointOrbitStandardPhaseCoordinateLedger"
PERMUTED_LOAD = "StableLadderEndpointOrbitAutomorphicLoadPermutationLedger"
FIRST_HARMONIC = "StableLadderEndpointOrbitFirstHarmonicIdentityLedger"
INVARIANTS = "StableLadderEndpointOrbitLoadNormsAndSupportPreservedLedger"
NO_ANON = "NoAnonymousPrimitiveConductorFrequencyExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterStandardCharacterLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {UNIT_AUTO} "
    f"AND {STANDARD_COORD} AND {PERMUTED_LOAD} AND {FIRST_HARMONIC} "
    f"AND {INVARIANTS} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 primitive conductor 硬点替换成标准 character 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit standard-character 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitPrimitiveConductorCharacterImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、primitive conductor character cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterStandardCharacter",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStandardCharacter",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其全局可求和。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitConductorUnitAutomorphism",
            True,
            True,
            "因 gcd(h0,m)=1，乘以 h0 是 C_m 的置换自同构，存在逆元 u=h0^{-1} mod m。",
            UNIT_AUTO,
        ),
        row(
            "StableLadderEndpointOrbitStandardPhaseCoordinate",
            True,
            True,
            "令 a=h0*s mod m，把 primitive character 坐标改写为标准相位 a。",
            STANDARD_COORD,
        ),
        row(
            "StableLadderEndpointOrbitAutomorphicLoadPermutation",
            True,
            True,
            "定义 S_a=G_{u*a mod m}；这是 G_s 的精确置换，不丢失支撑与权重。",
            PERMUTED_LOAD,
        ),
        row(
            "StableLadderEndpointOrbitFirstHarmonicIdentity",
            True,
            True,
            "sum_s G_s e(-h0*s/m)=sum_a S_a e(-a/m)，primitive 频率参数被删除。",
            FIRST_HARMONIC,
        ),
        row(
            "StableLadderEndpointOrbitLoadNormsAndSupportPreserved",
            True,
            True,
            "置换保持支撑大小、L1/L2 质量、均值与 Fourier 下界常数。",
            INVARIANTS,
        ),
        row(
            "NoAnonymousPrimitiveConductorFrequencyExit",
            True,
            True,
            "剩余不再含匿名 h0；只有导子 m 与标准 first-harmonic packet。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterStandardCharacter",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitStandardConductorFirstHarmonicCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、standard conductor first-harmonic PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、standard first-harmonic cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit standard-character 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "primitive conductor character packet 中的 primitive 频率 h0 只是导子群 C_m 的单位自同构。"
        "令 u=h0^{-1} mod m，并作变量替换 a=h0*s mod m。"
        "折叠负载 G_s 被精确置换为 S_a=G_{u*a mod m}，且 "
        "sum_s G_s e(-h0*s/m)=sum_a S_a e(-a/m)。"
        "因此剩余从 primitive conductor character cap 进一步规范化为标准 first-harmonic conductor packet。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_standard_character_router",
        "status": "endpoint_orbit_primitive_character_reduced_to_standard_first_harmonic_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_primitive_conductor_character_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_conductor_unit_automorphism_closed": True,
        "endpoint_orbit_standard_phase_coordinate_closed": True,
        "endpoint_orbit_automorphic_load_permutation_closed": True,
        "endpoint_orbit_first_harmonic_identity_closed": True,
        "endpoint_orbit_load_norms_and_support_preserved": True,
        "anonymous_primitive_conductor_frequency_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_standard_conductor_first_harmonic_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "standard_character_formulas": {
            "previous_packet": "m>1, gcd(h0,m)=1, sum_{s mod m} G_s exp(-2*pi*i*h0*s/m)",
            "unit_inverse": "u*h0 == 1 mod m",
            "standard_coordinate": "a=h0*s mod m",
            "permuted_load": "S_a=G_{u*a mod m}",
            "exact_identity": "sum_{s mod m} G_s exp(-2*pi*i*h0*s/m)=sum_{a mod m} S_a exp(-2*pi*i*a/m)",
            "support_preservation": "|supp S|=|supp G|",
            "mass_preservation": "sum_a |S_a|^p=sum_s |G_s|^p for p=1,2",
            "mean_preservation": "sum_a S_a=sum_s G_s",
            "lower_bound_preservation": "|sum_s G_s e(-h0*s/m)|>=M iff |sum_a S_a e(-a/m)|>=M",
            "new_exit": "EndpointOrbitStandardConductorFirstHarmonicPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit standard-character 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_primitive_conductor_character_imported={fmt_bool(cert['endpoint_orbit_primitive_conductor_character_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_conductor_unit_automorphism_closed={fmt_bool(cert['endpoint_orbit_conductor_unit_automorphism_closed'])}",
        f"endpoint_orbit_standard_phase_coordinate_closed={fmt_bool(cert['endpoint_orbit_standard_phase_coordinate_closed'])}",
        f"endpoint_orbit_automorphic_load_permutation_closed={fmt_bool(cert['endpoint_orbit_automorphic_load_permutation_closed'])}",
        f"endpoint_orbit_first_harmonic_identity_closed={fmt_bool(cert['endpoint_orbit_first_harmonic_identity_closed'])}",
        f"endpoint_orbit_load_norms_and_support_preserved={fmt_bool(cert['endpoint_orbit_load_norms_and_support_preserved'])}",
        f"anonymous_primitive_conductor_frequency_removed={fmt_bool(cert['anonymous_primitive_conductor_frequency_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_standard_conductor_first_harmonic_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_standard_conductor_first_harmonic_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. primitive 频率只是单位自同构",
        "",
        "上一层给出的 conductor packet 形如：",
        "",
        "```text",
        "m>1, gcd(h0,m)=1,",
        "sum_{s mod m} G_s exp(-2*pi*i*h0*s/m).",
        "```",
        "",
        "由于 `h0` 是 `Z/mZ` 的单位，存在逆元：",
        "",
        "```text",
        "u*h0 == 1 mod m.",
        "```",
        "",
        "## 2. 标准相位坐标",
        "",
        "令：",
        "",
        "```text",
        "a=h0*s mod m,",
        "S_a=G_{u*a mod m}.",
        "```",
        "",
        "这是 `C_m` 上的精确置换，所以：",
        "",
        "```text",
        "sum_{s mod m} G_s exp(-2*pi*i*h0*s/m)",
        "  = sum_{a mod m} S_a exp(-2*pi*i*a/m).",
        "```",
        "",
        "因此 primitive 频率 `h0` 被删除，剩余只依赖导子 `m` 上的标准 first harmonic。",
        "",
        "## 3. 不变量",
        "",
        "置换不会改变支撑、质量、均值或 Fourier 下界：",
        "",
        "```text",
        "|supp S|=|supp G|,",
        "sum_a |S_a|^p=sum_s |G_s|^p  (p=1,2),",
        "sum_a S_a=sum_s G_s,",
        "|sum_s G_s e(-h0*s/m)|>=M iff |sum_a S_a e(-a/m)|>=M.",
        "```",
        "",
        "full-cycle mean atom 仍按上一层作为独立出口保留；本步只规范化非零标准 character 分支。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 primitive conductor character cap 变成 standard conductor first-harmonic PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitStandardConductorFirstHarmonicPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 primitive conductor character packet 规范化成标准 first-harmonic packet。",
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
