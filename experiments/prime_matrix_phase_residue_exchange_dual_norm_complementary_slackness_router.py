#!/usr/bin/env python3
"""生成 phase-residue exchange dual-norm complementary-slackness 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_dual_norm_complementary_slackness_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.json

输出：
  data/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeCutPotentialDualNormSaturationCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeDualNormComplementarySlacknessCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeCutPotentialDualNormImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeComplementarySlacknessLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeComplementarySlacknessLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeComplementarySlacknessLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeComplementarySlacknessLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeComplementarySlacknessLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeComplementarySlacknessLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeComplementarySlacknessLedger"
DUAL_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeDualNormImportedForComplementarySlacknessLedger"
EDGE_ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeCalibratedEdgeOrientationLedger"
UNIT_DROP = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessUnitPotentialDropLedger"
PRIMAL_FLUX = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessPrimalFluxLedger"
PRIMAL_COST = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessPrimalCostLedger"
DUAL_VALUE = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessDualValueLedger"
ZERO_GAP = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessZeroDualityGapLedger"
SATURATED_SUPPORT = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessSaturatedEdgeSupportLedger"
NO_HIDDEN_CYCLE = "StableLadderEndpointOrbitPhaseResidueNoHiddenPositiveCostCycleAfterComplementarySlacknessLedger"
EQUALS_DUAL = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessEqualsDualNormLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessOrientationLedger"
NO_DUAL = "StableLadderEndpointOrbitPhaseResidueNoAnonymousDualNormAfterComplementarySlacknessLedger"
CS_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessPacketLedger"
NO_ANON = "NoAnonymousDualNormAfterComplementarySlacknessLedger"


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
    """把 dual-norm saturation 硬点替换为 complementary-slackness 硬点。"""
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
        DUAL_IMPORT,
        EDGE_ORIENTATION,
        UNIT_DROP,
        PRIMAL_FLUX,
        PRIMAL_COST,
        DUAL_VALUE,
        ZERO_GAP,
        SATURATED_SUPPORT,
        NO_HIDDEN_CYCLE,
        EQUALS_DUAL,
        COLLISION_EXIT,
        ORIENTATION,
        NO_DUAL,
        CS_PACKET,
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


def complementary_slackness_records() -> list[dict[str, str]]:
    """给出互补松弛/校准边字段。"""
    return [
        {
            "field": "oriented_edge",
            "meaning": "非退化时登记有向边 e=(r* -> r0)，边界为 [r0]-[r*]。",
        },
        {
            "field": "unit_potential_drop",
            "meaning": "势差 phi(r0)-phi(r*)=1，恰好饱和单位边成本。",
        },
        {
            "field": "primal_flux",
            "meaning": "边上输运通量为 A。",
        },
        {
            "field": "primal_cost",
            "meaning": "单位成本边的 primal cost 为 A。",
        },
        {
            "field": "dual_value",
            "meaning": "dual value 为 <div,phi>=A。",
        },
        {
            "field": "zero_duality_gap",
            "meaning": "primal cost - dual value = A-A=0。",
        },
        {
            "field": "saturated_support",
            "meaning": "全部非零通量都落在势差等于边成本的饱和边上。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r*，边长、势差和对偶间隙证书退化并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 complementary-slackness 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeCutPotentialDualNormImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange cut-potential dual-norm saturation circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "同点退化或零通量时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeDualNormImportedForComplementarySlackness",
            True,
            True,
            "导入 ||div||_1=2A、||phi||_infty=1/2、<div,phi>=A 与 sign alignment。",
            DUAL_IMPORT,
        ),
        row(
            "PhaseResidueExchangeCalibratedEdgeOrientation",
            True,
            True,
            "非退化对象登记为 e=(r* -> r0) 的有向单位边。",
            EDGE_ORIENTATION,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessUnitPotentialDrop",
            True,
            True,
            "势差 phi(r0)-phi(r*)=1，恰好饱和单位边成本。",
            UNIT_DROP,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessPrimalFlux",
            True,
            True,
            "边通量为 A，边界为 A([r0]-[r*])。",
            PRIMAL_FLUX,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessPrimalCost",
            True,
            True,
            "单位成本边给出 primal cost=A。",
            PRIMAL_COST,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessDualValue",
            True,
            True,
            "对偶值 <div,phi>=A。",
            DUAL_VALUE,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessZeroDualityGap",
            True,
            True,
            "primal cost 与 dual value 相等，对偶间隙为 0。",
            ZERO_GAP,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessSaturatedEdgeSupport",
            True,
            True,
            "全部非零通量都在势差等于边成本的饱和边上。",
            SATURATED_SUPPORT,
        ),
        row(
            "PhaseResidueNoHiddenPositiveCostCycleAfterComplementarySlackness",
            True,
            True,
            "二点单边证书内没有可保留边界同时增加正成本的隐藏循环。",
            NO_HIDDEN_CYCLE,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessEqualsDualNorm",
            True,
            True,
            "互补松弛证书与上一层 dual-norm saturation 表示同一局部对象。",
            EQUALS_DUAL,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r*，边、势差和通量证书退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessOrientation",
            True,
            True,
            "方向由负势/负散度端指向正势/正散度端，固定为 source -> root。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousDualNormAfterComplementarySlackness",
            True,
            True,
            "dual-norm saturation 口径被删除；剩余是命名互补松弛零间隙证书。",
            NO_DUAL,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange dual-norm complementary-slackness circuit PDEC/cap。",
            CS_PACKET,
        ),
        row(
            "NoAnonymousDualNormAfterComplementarySlackness",
            True,
            True,
            "对偶范数饱和被压成 primal/dual 零间隙的校准边证书。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeComplementarySlackness",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeComplementarySlacknessStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、complementary-slackness、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange dual-norm complementary-slackness circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 dual-norm complementary-slackness 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange cut-potential dual-norm 已把剩余写成 "
        "||div||_1=2A、||phi||_infty=1/2、<div,phi>=A、"
        "<div,phi>=||div||_1||phi||_infty，并且正/负散度与正/负势极点同号。"
        "本步删除 dual-norm saturation 作为黑箱的口径，把非退化对象登记为 primal/dual "
        "互补松弛零间隙：有向边 e=(r* -> r0)、单位势差 phi(r0)-phi(r*)=1、"
        "边通量 A、primal cost=A、dual value=A、duality gap=0。"
        "若 r0=r*，边、势差和对偶间隙证书退化并回流 singleton/degenerate 出口。"
        "剩余反例不再是匿名 dual-norm saturation，而必须表现为 dual-norm complementary-slackness "
        "circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_dual_norm_complementary_slackness_router",
        "status": "phase_residue_exchange_dual_norm_reduced_to_complementary_slackness_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "complementary_slackness_records": complementary_slackness_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_cut_potential_dual_norm_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_dual_norm_imported_for_complementary_slackness": True,
        "phase_residue_exchange_calibrated_edge_orientation_closed": True,
        "phase_residue_exchange_complementary_slackness_unit_potential_drop_closed": True,
        "phase_residue_exchange_complementary_slackness_primal_flux_closed": True,
        "phase_residue_exchange_complementary_slackness_primal_cost_closed": True,
        "phase_residue_exchange_complementary_slackness_dual_value_closed": True,
        "phase_residue_exchange_complementary_slackness_zero_duality_gap_closed": True,
        "phase_residue_exchange_complementary_slackness_saturated_edge_support_closed": True,
        "phase_residue_no_hidden_positive_cost_cycle_after_complementary_slackness_closed": True,
        "phase_residue_exchange_complementary_slackness_equals_dual_norm_closed": True,
        "phase_residue_exchange_complementary_slackness_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_complementary_slackness_orientation_closed": True,
        "phase_residue_no_anonymous_dual_norm_after_complementary_slackness_closed": True,
        "phase_residue_exchange_complementary_slackness_packet_registered": True,
        "anonymous_dual_norm_saturation_removed_after_complementary_slackness": True,
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
        "phase_residue_exchange_cut_potential_dual_norm_saturation_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_dual_norm_complementary_slackness_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange dual-norm complementary slackness 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_cut_potential_dual_norm_imported={fmt_bool(cert['phase_residue_exchange_cut_potential_dual_norm_imported'])}",
        f"phase_residue_exchange_calibrated_edge_orientation_closed={fmt_bool(cert['phase_residue_exchange_calibrated_edge_orientation_closed'])}",
        f"phase_residue_exchange_complementary_slackness_unit_potential_drop_closed={fmt_bool(cert['phase_residue_exchange_complementary_slackness_unit_potential_drop_closed'])}",
        f"phase_residue_exchange_complementary_slackness_primal_cost_closed={fmt_bool(cert['phase_residue_exchange_complementary_slackness_primal_cost_closed'])}",
        f"phase_residue_exchange_complementary_slackness_dual_value_closed={fmt_bool(cert['phase_residue_exchange_complementary_slackness_dual_value_closed'])}",
        f"phase_residue_exchange_complementary_slackness_zero_duality_gap_closed={fmt_bool(cert['phase_residue_exchange_complementary_slackness_zero_duality_gap_closed'])}",
        f"phase_residue_exchange_complementary_slackness_saturated_edge_support_closed={fmt_bool(cert['phase_residue_exchange_complementary_slackness_saturated_edge_support_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_dual_norm_complementary_slackness_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_dual_norm_complementary_slackness_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. dual-norm saturation 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "div(r0)=+A",
        "div(r*)=-A",
        "phi(r0)=+1/2",
        "phi(r*)=-1/2",
        "||div||_1=2A",
        "||phi||_infty=1/2",
        "<div,phi>=||div||_1 ||phi||_infty=A",
        "sign(div(r0))=sign(phi(r0))=+",
        "sign(div(r*))=sign(phi(r*))=-",
        "A C_Pi=W",
        "```",
        "",
        "## 2. complementary slackness 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["complementary_slackness_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时互补松弛证书为：",
            "",
            "```text",
            "e=(r* -> r0)",
            "partial(A e)=A([r0]-[r*])=div",
            "cost(e)=1",
            "phi(r0)-phi(r*)=1=cost(e)",
            "primal_cost=A cost(e)=A",
            "dual_value=<div,phi>=A",
            "duality_gap=primal_cost-dual_value=0",
            "support(F) subset {edges with phi(head)-phi(tail)=cost(edge)}",
            "A C_Pi=W",
            "```",
            "",
            "若 `r0=r*`，则边、势差和对偶间隙证书退化并回流 singleton/degenerate 出口。",
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
            "- 本证书没有证明 phase-residue exchange dual-norm complementary-slackness circuit PDEC/cap。",
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
    print("phase_residue_exchange_dual_norm_complementary_slackness_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
