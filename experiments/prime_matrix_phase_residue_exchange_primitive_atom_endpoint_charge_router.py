#!/usr/bin/env python3
"""生成 phase-residue exchange primitive atom endpoint charge 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_primitive_atom_endpoint_charge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.json

输出：
  data/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeSignedCRTPairPrimitiveAtomCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangePrimitiveAtomEndpointChargeCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangePrimitiveAtomEndpointChargeLedger"
ATOM_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangePrimitiveAtomImportedForEndpointChargeLedger"
ROOT_CHARGE = "StableLadderEndpointOrbitPhaseResidueExchangeRootPositiveEndpointChargeLedger"
SOURCE_CHARGE = "StableLadderEndpointOrbitPhaseResidueExchangeSourceNegativeEndpointChargeLedger"
CHARGE_PAIR = "StableLadderEndpointOrbitPhaseResidueExchangeOrderedEndpointChargePairLedger"
CHARGE_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeBalanceLedger"
POS_NEG_MASS = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointPositiveNegativeMassEqualityLedger"
ABS_FLUX = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointAbsoluteFluxLedger"
PACKET_EQUALS_ATOM = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeEqualsPrimitiveAtomLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeOrientationLedger"
NO_ATOM = "StableLadderEndpointOrbitPhaseResidueNoAnonymousPrimitiveAtomAfterEndpointChargeLedger"
CHARGE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangePrimitiveAtomEndpointChargePacketLedger"
NO_ANON = "NoAnonymousSignedCRTPairPrimitiveAtomAfterEndpointChargeLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def source_hashes() -> dict[str, str]:
    """登记本脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def next_target(previous: dict[str, Any]) -> str:
    """把 primitive atom 硬点替换为 endpoint charge 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        ATOM_IMPORT,
        ROOT_CHARGE,
        SOURCE_CHARGE,
        CHARGE_PAIR,
        CHARGE_BALANCE,
        POS_NEG_MASS,
        ABS_FLUX,
        PACKET_EQUALS_ATOM,
        COLLISION_EXIT,
        ORIENTATION,
        NO_ATOM,
        CHARGE_PACKET,
        NO_ANON,
        SPARSE,
        new_target,
    ]
    return " AND ".join(ledgers)


def replace_latest_basis(previous: dict[str, Any], reduced: str) -> str:
    """更新长活动基。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    old = previous.get("next_direct_attack_target", "")
    if basis and old and old in basis:
        return basis.replace(old, reduced)
    return reduced


def endpoint_charge_records() -> list[dict[str, str]]:
    """给出 endpoint charge packet 的字段。"""
    return [
        {
            "field": "root_positive_charge",
            "meaning": "root CRT word r0 携带正端点电荷 +A。",
        },
        {
            "field": "source_negative_charge",
            "meaning": "source CRT word r* 携带负端点电荷 -A。",
        },
        {
            "field": "ordered_charge_pair",
            "meaning": "有序端点电荷对 ((r0,+A),(r*,-A)) 保留 source -> root 方向。",
        },
        {
            "field": "net_charge",
            "meaning": "净电荷 +A-A=0。",
        },
        {
            "field": "positive_negative_mass",
            "meaning": "正质量与负质量绝对值相等，均为 A。",
        },
        {
            "field": "absolute_flux",
            "meaning": "端点绝对通量 |+A|+|-A|=2A。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r*，同点正负电荷消去并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 primitive atom endpoint charge 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange signed CRT pair primitive atom circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "同点正负消去或退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangePrimitiveAtomImportedForEndpointCharge",
            True,
            True,
            "导入 support={r0,r*}、coefficient(r0)=+1、coefficient(r*)=-1、flux_weights=(+A,-A)。",
            ATOM_IMPORT,
        ),
        row(
            "PhaseResidueExchangeRootPositiveEndpointCharge",
            True,
            True,
            "root word r0 被登记为正端点电荷 +A。",
            ROOT_CHARGE,
        ),
        row(
            "PhaseResidueExchangeSourceNegativeEndpointCharge",
            True,
            True,
            "source word r* 被登记为负端点电荷 -A。",
            SOURCE_CHARGE,
        ),
        row(
            "PhaseResidueExchangeOrderedEndpointChargePair",
            True,
            True,
            "端点电荷包为有序对 ((r0,+A),(r*,-A))。",
            CHARGE_PAIR,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeBalance",
            True,
            True,
            "净电荷 +A-A=0，继承 primitive atom 的零质量。",
            CHARGE_BALANCE,
        ),
        row(
            "PhaseResidueExchangeEndpointPositiveNegativeMassEquality",
            True,
            True,
            "正端点质量与负端点质量绝对值相等，均为 A。",
            POS_NEG_MASS,
        ),
        row(
            "PhaseResidueExchangeEndpointAbsoluteFlux",
            True,
            True,
            "端点绝对通量 |+A|+|-A|=2A。",
            ABS_FLUX,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeEqualsPrimitiveAtom",
            True,
            True,
            "endpoint charge packet 与上一层 primitive atom 表示同一向量 W。",
            PACKET_EQUALS_ATOM,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r*，同点 +A 与 -A 消去并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeOrientation",
            True,
            True,
            "方向保留为 source -> root；不降成无向电荷集合。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousPrimitiveAtomAfterEndpointCharge",
            True,
            True,
            "primitive atom 口径被删除；剩余是命名 root/source endpoint charge packet。",
            NO_ATOM,
        ),
        row(
            "PhaseResidueExchangePrimitiveAtomEndpointChargePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange primitive atom endpoint charge circuit PDEC/cap。",
            CHARGE_PACKET,
        ),
        row(
            "NoAnonymousSignedCRTPairPrimitiveAtomAfterEndpointCharge",
            True,
            True,
            "signed CRT pair primitive atom 被压成正负端点电荷守恒包。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangePrimitiveAtomEndpointCharge",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangePrimitiveAtomEndpointChargeStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、endpoint charge、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange primitive atom endpoint charge circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 primitive atom endpoint charge 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange signed CRT pair primitive atom 已把剩余写成 support={r0,r*}、"
        "coefficient(r0)=+1、coefficient(r*)=-1、flux_weights=(+A,-A)、A C_Pi=W。"
        "本步删除 primitive atom 作为黑箱的口径，把非退化对象登记为 root/source 两个端点电荷："
        "root 端 (r0,+A)、source 端 (r*,-A)，净电荷为 0，正负质量均为 A，绝对通量为 2A，"
        "并保留 source -> root 方向。若 r0=r*，同点正负电荷消去并回流 singleton/degenerate 出口。"
        "剩余反例不再是匿名 primitive atom，而必须表现为 primitive atom endpoint charge circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_primitive_atom_endpoint_charge_router",
        "status": "phase_residue_exchange_primitive_atom_reduced_to_endpoint_charge_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "primitive_atom_endpoint_charge_records": endpoint_charge_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_signed_crt_pair_primitive_atom_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_primitive_atom_imported_for_endpoint_charge": True,
        "phase_residue_exchange_root_positive_endpoint_charge_closed": True,
        "phase_residue_exchange_source_negative_endpoint_charge_closed": True,
        "phase_residue_exchange_ordered_endpoint_charge_pair_closed": True,
        "phase_residue_exchange_endpoint_charge_balance_closed": True,
        "phase_residue_exchange_endpoint_positive_negative_mass_equality_closed": True,
        "phase_residue_exchange_endpoint_absolute_flux_closed": True,
        "phase_residue_exchange_endpoint_charge_equals_primitive_atom_closed": True,
        "phase_residue_exchange_endpoint_charge_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_endpoint_charge_orientation_closed": True,
        "phase_residue_no_anonymous_primitive_atom_after_endpoint_charge_closed": True,
        "phase_residue_exchange_primitive_atom_endpoint_charge_packet_registered": True,
        "anonymous_signed_crt_pair_primitive_atom_removed_after_endpoint_charge": True,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "linear_witness_existence_proved": False,
        "phase_residue_exchange_primitive_atom_endpoint_charge_circuit_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "source_hashes": source_hashes(),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange primitive atom endpoint charge 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_signed_crt_pair_primitive_atom_imported={fmt_bool(cert['phase_residue_exchange_signed_crt_pair_primitive_atom_imported'])}",
        f"phase_residue_exchange_root_positive_endpoint_charge_closed={fmt_bool(cert['phase_residue_exchange_root_positive_endpoint_charge_closed'])}",
        f"phase_residue_exchange_source_negative_endpoint_charge_closed={fmt_bool(cert['phase_residue_exchange_source_negative_endpoint_charge_closed'])}",
        f"phase_residue_exchange_ordered_endpoint_charge_pair_closed={fmt_bool(cert['phase_residue_exchange_ordered_endpoint_charge_pair_closed'])}",
        f"phase_residue_exchange_endpoint_charge_balance_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_balance_closed'])}",
        f"phase_residue_exchange_endpoint_positive_negative_mass_equality_closed={fmt_bool(cert['phase_residue_exchange_endpoint_positive_negative_mass_equality_closed'])}",
        f"phase_residue_exchange_endpoint_absolute_flux_closed={fmt_bool(cert['phase_residue_exchange_endpoint_absolute_flux_closed'])}",
        f"phase_residue_exchange_endpoint_charge_collision_or_singleton_exit_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_collision_or_singleton_exit_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_primitive_atom_endpoint_charge_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_primitive_atom_endpoint_charge_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. primitive atom 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "support={r0,r*}",
        "coefficient(r0)=+1",
        "coefficient(r*)=-1",
        "flux_weights=(+A,-A)",
        "A C_Pi=W",
        "```",
        "",
        "## 2. endpoint charge 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["primitive_atom_endpoint_charge_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时 endpoint charge packet 为：",
            "",
            "```text",
            "root_charge=(r0,+A)",
            "source_charge=(r*,-A)",
            "ordered_charge_pair=((r0,+A),(r*,-A))",
            "net_charge=+A-A=0",
            "positive_mass=A",
            "negative_mass=A",
            "absolute_flux=2A",
            "A C_Pi=W",
            "```",
            "",
            "若 `r0=r*`，则同点 `+A-A=0` 并回流 singleton/degenerate 出口。",
            "",
            "## 3. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
            "```",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
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
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange primitive atom endpoint charge circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
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
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、ledger 和 Markdown 三件套。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("phase_residue_exchange_primitive_atom_endpoint_charge_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
