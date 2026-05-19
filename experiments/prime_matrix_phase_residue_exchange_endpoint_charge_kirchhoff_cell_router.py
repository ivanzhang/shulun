#!/usr/bin/env python3
"""生成 phase-residue exchange endpoint charge Kirchhoff cell 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_endpoint_charge_kirchhoff_cell_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.json

输出：
  data/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangePrimitiveAtomEndpointChargeCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangePrimitiveAtomEndpointChargeImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeEndpointChargeKirchhoffCellLedger"
ENDPOINT_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeImportedForKirchhoffCellLedger"
LOCAL_CELL = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeLocalKirchhoffCellLedger"
ROOT_DIV = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeRootPositiveDivergenceLedger"
SOURCE_DIV = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeSourceNegativeDivergenceLedger"
KIRCHHOFF_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeKirchhoffBalanceLedger"
POS_NEG_DIV = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargePositiveNegativeDivergenceEqualityLedger"
BOUNDARY_VARIATION = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeBoundaryVariationLedger"
CELL_EQUALS_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellEqualsEndpointChargePacketLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeKirchhoffCellOrientationLedger"
NO_ENDPOINT = "StableLadderEndpointOrbitPhaseResidueNoAnonymousEndpointChargeAfterKirchhoffCellLedger"
KIRCHHOFF_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeKirchhoffCellPacketLedger"
NO_ANON = "NoAnonymousEndpointChargePacketAfterKirchhoffCellLedger"


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
    """把 endpoint charge 硬点替换为 Kirchhoff cell 硬点。"""
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
        ENDPOINT_IMPORT,
        LOCAL_CELL,
        ROOT_DIV,
        SOURCE_DIV,
        KIRCHHOFF_BALANCE,
        POS_NEG_DIV,
        BOUNDARY_VARIATION,
        CELL_EQUALS_PACKET,
        COLLISION_EXIT,
        ORIENTATION,
        NO_ENDPOINT,
        KIRCHHOFF_PACKET,
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


def kirchhoff_cell_records() -> list[dict[str, str]]:
    """给出局部 Kirchhoff cell 的字段。"""
    return [
        {
            "field": "local_kirchhoff_cell",
            "meaning": "局部 CRT word 单元 K={r0,r*}，非退化时含两个端点。",
        },
        {
            "field": "divergence_at_root",
            "meaning": "root word r0 的散度为 div(r0)=+A。",
        },
        {
            "field": "divergence_at_source",
            "meaning": "source word r* 的散度为 div(r*)=-A。",
        },
        {
            "field": "kirchhoff_balance",
            "meaning": "单元总散度 sum_K div=+A-A=0。",
        },
        {
            "field": "positive_negative_divergence",
            "meaning": "正散度质量与负散度质量绝对值相等，均为 A。",
        },
        {
            "field": "total_boundary_variation",
            "meaning": "单元边界总变差 |+A|+|-A|=2A。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r*，同点散度消去并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 endpoint charge Kirchhoff cell 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangePrimitiveAtomEndpointChargeImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange primitive atom endpoint charge circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "同点正负散度消去或退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeImportedForKirchhoffCell",
            True,
            True,
            "导入 root_charge=(r0,+A)、source_charge=(r*,-A)、net_charge=0、absolute_flux=2A。",
            ENDPOINT_IMPORT,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeLocalKirchhoffCell",
            True,
            True,
            "端点电荷被登记为局部 CRT word cell K={r0,r*}。",
            LOCAL_CELL,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeRootPositiveDivergence",
            True,
            True,
            "root word r0 的散度为 +A。",
            ROOT_DIV,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeSourceNegativeDivergence",
            True,
            True,
            "source word r* 的散度为 -A。",
            SOURCE_DIV,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeKirchhoffBalance",
            True,
            True,
            "局部单元满足 Kirchhoff 守恒：sum_K div=0。",
            KIRCHHOFF_BALANCE,
        ),
        row(
            "PhaseResidueExchangeEndpointChargePositiveNegativeDivergenceEquality",
            True,
            True,
            "正散度与负散度绝对质量相等，均为 A。",
            POS_NEG_DIV,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeBoundaryVariation",
            True,
            True,
            "局部边界总变差为 |+A|+|-A|=2A。",
            BOUNDARY_VARIATION,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellEqualsEndpointChargePacket",
            True,
            True,
            "Kirchhoff cell 与上一层 endpoint charge packet 表示同一向量 W。",
            CELL_EQUALS_PACKET,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r*，同点散度 +A-A=0 并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeKirchhoffCellOrientation",
            True,
            True,
            "方向仍记录为 source -> root；不退回匿名无向边。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousEndpointChargeAfterKirchhoffCell",
            True,
            True,
            "endpoint charge 口径被删除；剩余是命名局部 Kirchhoff cell。",
            NO_ENDPOINT,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeKirchhoffCellPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange endpoint charge Kirchhoff cell circuit PDEC/cap。",
            KIRCHHOFF_PACKET,
        ),
        row(
            "NoAnonymousEndpointChargePacketAfterKirchhoffCell",
            True,
            True,
            "root/source endpoint charge packet 被压成二点局部散度守恒单元。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeEndpointChargeKirchhoffCell",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeEndpointChargeKirchhoffCellStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、Kirchhoff cell、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange endpoint charge Kirchhoff cell circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint charge Kirchhoff cell 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange primitive atom endpoint charge 已把剩余写成 "
        "root_charge=(r0,+A)、source_charge=(r*,-A)、ordered_charge_pair=((r0,+A),(r*,-A))、"
        "net_charge=0、positive_mass=negative_mass=A、absolute_flux=2A、A C_Pi=W。"
        "本步删除 endpoint charge 作为黑箱的口径，把非退化对象登记为二点局部 Kirchhoff cell："
        "K={r0,r*}，div(r0)=+A，div(r*)=-A，sum_K div=0，正负散度质量均为 A，"
        "边界总变差为 2A，并保留 source -> root 方向。若 r0=r*，同点散度消去并回流 "
        "singleton/degenerate 出口。剩余反例不再是匿名 endpoint charge packet，而必须表现为 "
        "endpoint charge Kirchhoff cell circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_charge_kirchhoff_cell_router",
        "status": "phase_residue_exchange_endpoint_charge_reduced_to_kirchhoff_cell_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "endpoint_charge_kirchhoff_cell_records": kirchhoff_cell_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_primitive_atom_endpoint_charge_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_endpoint_charge_imported_for_kirchhoff_cell": True,
        "phase_residue_exchange_endpoint_charge_local_kirchhoff_cell_closed": True,
        "phase_residue_exchange_endpoint_charge_root_positive_divergence_closed": True,
        "phase_residue_exchange_endpoint_charge_source_negative_divergence_closed": True,
        "phase_residue_exchange_endpoint_charge_kirchhoff_balance_closed": True,
        "phase_residue_exchange_endpoint_charge_positive_negative_divergence_equality_closed": True,
        "phase_residue_exchange_endpoint_charge_boundary_variation_closed": True,
        "phase_residue_exchange_kirchhoff_cell_equals_endpoint_charge_packet_closed": True,
        "phase_residue_exchange_kirchhoff_cell_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_kirchhoff_cell_orientation_closed": True,
        "phase_residue_no_anonymous_endpoint_charge_after_kirchhoff_cell_closed": True,
        "phase_residue_exchange_endpoint_charge_kirchhoff_cell_packet_registered": True,
        "anonymous_endpoint_charge_packet_removed_after_kirchhoff_cell": True,
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
        "phase_residue_exchange_endpoint_charge_kirchhoff_cell_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange endpoint charge Kirchhoff cell 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_primitive_atom_endpoint_charge_imported={fmt_bool(cert['phase_residue_exchange_primitive_atom_endpoint_charge_imported'])}",
        f"phase_residue_exchange_endpoint_charge_local_kirchhoff_cell_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_local_kirchhoff_cell_closed'])}",
        f"phase_residue_exchange_endpoint_charge_root_positive_divergence_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_root_positive_divergence_closed'])}",
        f"phase_residue_exchange_endpoint_charge_source_negative_divergence_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_source_negative_divergence_closed'])}",
        f"phase_residue_exchange_endpoint_charge_kirchhoff_balance_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_kirchhoff_balance_closed'])}",
        f"phase_residue_exchange_endpoint_charge_positive_negative_divergence_equality_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_positive_negative_divergence_equality_closed'])}",
        f"phase_residue_exchange_endpoint_charge_boundary_variation_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_boundary_variation_closed'])}",
        f"phase_residue_exchange_kirchhoff_cell_collision_or_singleton_exit_closed={fmt_bool(cert['phase_residue_exchange_kirchhoff_cell_collision_or_singleton_exit_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_endpoint_charge_kirchhoff_cell_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_endpoint_charge_kirchhoff_cell_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. endpoint charge 输入",
        "",
        "上一层给出：",
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
        "## 2. Kirchhoff cell 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["endpoint_charge_kirchhoff_cell_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时局部 Kirchhoff cell 为：",
            "",
            "```text",
            "K={r0,r*}",
            "div(r0)=+A",
            "div(r*)=-A",
            "sum_{r in K} div(r)=0",
            "positive_divergence=A",
            "negative_divergence=A",
            "total_boundary_variation=2A",
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
            "- 本证书没有证明 phase-residue exchange endpoint charge Kirchhoff cell circuit PDEC/cap。",
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
    print("phase_residue_exchange_endpoint_charge_kirchhoff_cell_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
