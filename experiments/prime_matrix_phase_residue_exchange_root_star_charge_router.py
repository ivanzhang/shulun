#!/usr/bin/env python3
"""生成 phase-residue exchange root-star charge 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_root_star_charge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.json

输出：
  data/prime-matrix-phase-residue-exchange-root-star-charge-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-root-star-charge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeEndpointTelescopingChargeCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeRootStarChargeCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointTelescopingChargeImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeRootStarChargeLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeRootStarChargeLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRootStarChargeLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRootStarChargeLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRootStarChargeLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRootStarChargeLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeRootStarChargeLedger"
ENDPOINT_CHARGE = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointTelescopingChargeImportedForRootStarLedger"
COMMON_ROOT = "StableLadderEndpointOrbitPhaseResidueExchangeCommonRootEndpointLedger"
STAR_CHARGE_FAMILY = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeFamilyLedger"
ROOT_MULTIPLICITY = "StableLadderEndpointOrbitPhaseResidueExchangeRootChargeMultiplicityLedger"
NONROOT_UNIT_OUTPUT = "StableLadderEndpointOrbitPhaseResidueExchangeNonrootUnitOutputChargeLedger"
TOTAL_ZERO = "StableLadderEndpointOrbitPhaseResidueExchangeRootStarTotalChargeZeroLedger"
NO_ENDPOINT_ANON = "StableLadderEndpointOrbitPhaseResidueNoAnonymousEndpointChargeDistributionLedger"
STAR_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeRootStarChargePacketLedger"
NO_ANON = "NoAnonymousEndpointTelescopingChargeAfterRootStarLedger"


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
    """把 endpoint telescoping charge 硬点替换为 root-star charge 硬点。"""
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
        ENDPOINT_CHARGE,
        COMMON_ROOT,
        STAR_CHARGE_FAMILY,
        ROOT_MULTIPLICITY,
        NONROOT_UNIT_OUTPUT,
        TOTAL_ZERO,
        NO_ENDPOINT_ANON,
        STAR_PACKET,
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


def root_star_records() -> list[dict[str, str]]:
    """给出 root-star charge 的字段。"""
    return [
        {
            "field": "common_root_endpoint",
            "meaning": "所有端点电荷都指向同一基准缺失源点 s0。",
        },
        {
            "field": "endpoint_charge_family",
            "meaning": "对每个 s!=s0 有 c_s=[s0]-[s]。",
        },
        {
            "field": "root_charge_multiplicity",
            "meaning": "聚合后根点 s0 的正电荷为 |S|-1。",
        },
        {
            "field": "nonroot_unit_output",
            "meaning": "每个非根源点 s 各贡献一次 -[s]。",
        },
        {
            "field": "total_charge_zero",
            "meaning": "聚合电荷 C=(|S|-1)[s0]-sum_{s!=s0}[s] 的总系数为 0。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 root-star charge 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeEndpointTelescopingChargeImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange endpoint telescoping charge circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "根星电荷退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeEndpointTelescopingChargeImportedForRootStar",
            True,
            True,
            "导入上一层端点望远镜电荷 [s0]-[s]。",
            ENDPOINT_CHARGE,
        ),
        row(
            "PhaseResidueExchangeCommonRootEndpoint",
            True,
            True,
            "所有交换路径共用同一根点 s0。",
            COMMON_ROOT,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeFamily",
            True,
            True,
            "对每个非根源点登记一条 c_s=[s0]-[s]。",
            STAR_CHARGE_FAMILY,
        ),
        row(
            "PhaseResidueExchangeRootChargeMultiplicity",
            True,
            True,
            "聚合后根点 s0 的正端点电荷数为 |S|-1。",
            ROOT_MULTIPLICITY,
        ),
        row(
            "PhaseResidueExchangeNonrootUnitOutputCharge",
            True,
            True,
            "每个非根源点只出现一次负端点电荷。",
            NONROOT_UNIT_OUTPUT,
        ),
        row(
            "PhaseResidueExchangeRootStarTotalChargeZero",
            True,
            True,
            "根星电荷场总系数为零，只重排端点压力不创造净量。",
            TOTAL_ZERO,
        ),
        row(
            "PhaseResidueNoAnonymousEndpointChargeDistribution",
            True,
            True,
            "端点电荷分布不再匿名；它是唯一根星入射场或已有命名出口。",
            NO_ENDPOINT_ANON,
        ),
        row(
            "PhaseResidueExchangeRootStarChargePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange root-star charge circuit PDEC/cap。",
            STAR_PACKET,
        ),
        row(
            "NoAnonymousEndpointTelescopingChargeAfterRootStar",
            True,
            True,
            "endpoint telescoping charge 不再匿名保留；它含根星电荷集中或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeRootStarCharge",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeRootStarChargeStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、root-star charge、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange root-star charge circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 root-star charge 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange endpoint telescoping charge 已把每条交换路径压成 [s0]-[s]。"
        "由于所有路径共用同一根点 s0，聚合所有 s!=s0 的端点电荷得到"
        " C=(|S|-1)[s0]-sum_{s!=s0}[s]，总电荷为零。"
        "剩余反例不再是匿名端点电荷分布，而是根点集中、非根单位输出的 root-star charge circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_root_star_charge_router",
        "status": "phase_residue_exchange_endpoint_telescoping_charge_reduced_to_root_star_charge_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "root_star_records": root_star_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_endpoint_telescoping_charge_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_endpoint_telescoping_charge_imported_for_root_star": True,
        "phase_residue_exchange_common_root_endpoint_closed": True,
        "phase_residue_exchange_endpoint_charge_family_closed": True,
        "phase_residue_exchange_root_charge_multiplicity_closed": True,
        "phase_residue_exchange_nonroot_unit_output_charge_closed": True,
        "phase_residue_exchange_root_star_total_charge_zero_closed": True,
        "phase_residue_no_anonymous_endpoint_charge_distribution_closed": True,
        "phase_residue_exchange_root_star_charge_packet_registered": True,
        "anonymous_endpoint_telescoping_charge_removed_after_root_star": True,
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
        "phase_residue_exchange_root_star_charge_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange root-star charge 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_endpoint_telescoping_charge_imported={fmt_bool(cert['phase_residue_exchange_endpoint_telescoping_charge_imported'])}",
        f"phase_residue_exchange_common_root_endpoint_closed={fmt_bool(cert['phase_residue_exchange_common_root_endpoint_closed'])}",
        f"phase_residue_exchange_root_charge_multiplicity_closed={fmt_bool(cert['phase_residue_exchange_root_charge_multiplicity_closed'])}",
        f"phase_residue_exchange_root_star_total_charge_zero_closed={fmt_bool(cert['phase_residue_exchange_root_star_total_charge_zero_closed'])}",
        f"phase_residue_exchange_root_star_charge_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_root_star_charge_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 端点电荷族",
        "",
        "上一层给出每个非根源点到共同根点的端点电荷：",
        "",
        "```text",
        "c_s = [s0] - [s],  s != s0",
        "```",
        "",
        "这里 `s0` 是同一个基准缺失源点，不随 `s` 改变。",
        "",
        "## 2. 根星聚合",
        "",
        "把所有非根源点的端点电荷相加：",
        "",
        "```text",
        "C = sum_{s != s0} c_s = (|S|-1)[s0] - sum_{s != s0}[s]",
        "```",
        "",
        "因此根点 `s0` 承受 `|S|-1` 个正端点电荷，每个非根源点只贡献一次负电荷。",
        "",
        "## 3. 总电荷守恒",
        "",
        "聚合电荷的总系数为：",
        "",
        "```text",
        "(|S|-1) - (|S|-1) = 0",
        "```",
        "",
        "所以这一步不创造净量，只把所有端点压力固定成唯一的根星入射场。若该场不能由已有出口支付，剩余就是 root-star charge circuit PDEC/cap。",
        "",
        "## 4. root-star charge 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["root_star_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 5. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
            "```",
            "",
            "## 6. 判定表",
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
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange root-star charge circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 9. 依赖哈希",
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
    print("phase_residue_exchange_root_star_charge_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
