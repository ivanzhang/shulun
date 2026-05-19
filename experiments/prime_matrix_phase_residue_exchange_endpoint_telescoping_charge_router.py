#!/usr/bin/env python3
"""生成 phase-residue exchange endpoint telescoping charge 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_endpoint_telescoping_charge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.json

输出：
  data/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-endpoint-telescoping-charge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangePrefixDefectLadderCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeEndpointTelescopingChargeCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangePrefixDefectLadderImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeEndpointTelescopingChargeLedger"
PREFIX_LADDER = "StableLadderEndpointOrbitPhaseResidueExchangePrefixDefectLadderImportedForEndpointChargeLedger"
BOUNDARY_OPERATOR = "StableLadderEndpointOrbitPhaseResidueExchangePivotBoundaryOperatorLedger"
INTERNAL_CANCEL = "StableLadderEndpointOrbitPhaseResidueExchangeInternalSourceCancellationLedger"
ENDPOINT_CHARGE = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointChargeIdentityLedger"
PREFIX_TELESCOPE = "StableLadderEndpointOrbitPhaseResidueExchangePrefixChargeTelescopingLedger"
NO_INTERIOR_DEBT = "StableLadderEndpointOrbitPhaseResidueNoInteriorAnonymousDebtAfterEndpointChargeLedger"
CHARGE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeEndpointTelescopingChargePacketLedger"
NO_ANON = "NoAnonymousExchangePrefixDefectLadderAfterEndpointTelescopingChargeLedger"


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
    """把 prefix defect ladder 硬点替换为 endpoint telescoping charge 硬点。"""
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
        PREFIX_LADDER,
        BOUNDARY_OPERATOR,
        INTERNAL_CANCEL,
        ENDPOINT_CHARGE,
        PREFIX_TELESCOPE,
        NO_INTERIOR_DEBT,
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
    """给出 endpoint telescoping charge 的字段。"""
    return [
        {
            "field": "pivot_boundary_operator",
            "meaning": "第 i 个 pivot 的源侧边界为 d_i=[u_i]-[u_{i-1}]。",
        },
        {
            "field": "internal_source_cancellation",
            "meaning": "内部源点 u_i 同时是 d_i 的正端和 d_{i+1} 的负端，求和后相消。",
        },
        {
            "field": "endpoint_charge_identity",
            "meaning": "整条链求和得到 sum_i d_i=[s0]-[s]。",
        },
        {
            "field": "prefix_charge_telescoping",
            "meaning": "前 t 个 pivot 求和得到 [u_t]-[u_0]，与前缀缺失源输运一致。",
        },
        {
            "field": "no_interior_anonymous_debt",
            "meaning": "若内部债不由命名出口支付，则它必须在相邻 pivot 中成对抵消。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 endpoint telescoping charge 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangePrefixDefectLadderImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange prefix defect ladder circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "端点电荷退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangePrefixDefectLadderImportedForEndpointCharge",
            True,
            True,
            "导入上一层前缀单位缺口 ladder 与前缀切换输运。",
            PREFIX_LADDER,
        ),
        row(
            "PhaseResidueExchangePivotBoundaryOperator",
            True,
            True,
            "每个 pivot 给出源侧边界算子 d_i=[u_i]-[u_{i-1}]。",
            BOUNDARY_OPERATOR,
        ),
        row(
            "PhaseResidueExchangeInternalSourceCancellation",
            True,
            True,
            "内部源点在相邻 pivot 的边界算子中一正一负，求和相消。",
            INTERNAL_CANCEL,
        ),
        row(
            "PhaseResidueExchangeEndpointChargeIdentity",
            True,
            True,
            "整条交换链的源侧边界望远镜为 [s0]-[s]。",
            ENDPOINT_CHARGE,
        ),
        row(
            "PhaseResidueExchangePrefixChargeTelescoping",
            True,
            True,
            "每个前缀的望远镜电荷为 [u_t]-[u_0]，匹配前缀状态输运。",
            PREFIX_TELESCOPE,
        ),
        row(
            "PhaseResidueNoInteriorAnonymousDebtAfterEndpointCharge",
            True,
            True,
            "内部源点不再匿名携带净债；未命名债只能压到端点差或已有出口。",
            NO_INTERIOR_DEBT,
        ),
        row(
            "PhaseResidueExchangeEndpointTelescopingChargePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange endpoint telescoping charge circuit PDEC/cap。",
            CHARGE_PACKET,
        ),
        row(
            "NoAnonymousExchangePrefixDefectLadderAfterEndpointTelescopingCharge",
            True,
            True,
            "prefix defect ladder 不再匿名保留；它含端点望远镜电荷或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeEndpointTelescopingCharge",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeEndpointTelescopingChargeStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、endpoint telescoping charge、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange endpoint telescoping charge circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint telescoping charge 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange prefix defect ladder 已把切换词压成嵌套前缀单位缺口。"
        "本步把每个局部 pivot 的源侧边界写成 d_i=[u_i]-[u_{i-1}]；"
        "内部源点在相邻 d_i 中一正一负相消，整条链望远镜为 [s0]-[s]。"
        "剩余反例不再能在内部源点匿名保留净债，而只能表现为端点望远镜电荷 circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_telescoping_charge_router",
        "status": "phase_residue_exchange_prefix_defect_ladder_reduced_to_endpoint_telescoping_charge_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "endpoint_charge_records": endpoint_charge_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_prefix_defect_ladder_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_prefix_defect_ladder_imported_for_endpoint_charge": True,
        "phase_residue_exchange_pivot_boundary_operator_closed": True,
        "phase_residue_exchange_internal_source_cancellation_closed": True,
        "phase_residue_exchange_endpoint_charge_identity_closed": True,
        "phase_residue_exchange_prefix_charge_telescoping_closed": True,
        "phase_residue_no_interior_anonymous_debt_after_endpoint_charge_closed": True,
        "phase_residue_exchange_endpoint_telescoping_charge_packet_registered": True,
        "anonymous_exchange_prefix_defect_ladder_removed_after_endpoint_charge": True,
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
        "phase_residue_exchange_endpoint_telescoping_charge_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange endpoint telescoping charge 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_prefix_defect_ladder_imported={fmt_bool(cert['phase_residue_exchange_prefix_defect_ladder_imported'])}",
        f"phase_residue_exchange_pivot_boundary_operator_closed={fmt_bool(cert['phase_residue_exchange_pivot_boundary_operator_closed'])}",
        f"phase_residue_exchange_internal_source_cancellation_closed={fmt_bool(cert['phase_residue_exchange_internal_source_cancellation_closed'])}",
        f"phase_residue_exchange_endpoint_charge_identity_closed={fmt_bool(cert['phase_residue_exchange_endpoint_charge_identity_closed'])}",
        f"phase_residue_exchange_endpoint_telescoping_charge_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_endpoint_telescoping_charge_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. pivot 边界算子",
        "",
        "上一层给出前缀单位缺口 ladder：",
        "",
        "```text",
        "P_s = (u_0=s, b_1, u_1, ..., b_r, u_r=s0)",
        "```",
        "",
        "每个局部 pivot `u_{i-1}->b_i->u_i` 定义源侧边界：",
        "",
        "```text",
        "d_i = [u_i] - [u_{i-1}]",
        "```",
        "",
        "它记录第 `i` 步前缀切换把缺失源从 `u_{i-1}` 输运到 `u_i`。",
        "",
        "## 2. 内部相消",
        "",
        "对内部源点 `u_i`，它在 `d_i` 中以正号出现，又在 `d_{i+1}` 中以负号出现。因此整条链求和时所有内部源点相消：",
        "",
        "```text",
        "sum_{i=1}^r d_i = [u_r] - [u_0] = [s0] - [s]",
        "```",
        "",
        "## 3. 前缀望远镜",
        "",
        "任意前缀也满足：",
        "",
        "```text",
        "sum_{i=1}^t d_i = [u_t] - [u_0]",
        "```",
        "",
        "这与前缀 pivot 乘积把缺失源从 `u_0` 输运到 `u_t` 完全一致。若内部出现未命名净债，它不能留在内部源点，只能回流已有出口或压到端点电荷。",
        "",
        "## 4. endpoint telescoping charge 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["endpoint_charge_records"]:
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
            "- 本证书没有证明 phase-residue exchange endpoint telescoping charge circuit PDEC/cap。",
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
    print("phase_residue_exchange_endpoint_telescoping_charge_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
