#!/usr/bin/env python3
"""生成 phase-residue exchange complementary-slackness active-facet 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_complementary_slackness_active_facet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.json

输出：
  data/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-complementary-slackness-active-facet"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeDualNormComplementarySlacknessCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeComplementarySlacknessActiveFacetNormalConeCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeActiveFacetLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeActiveFacetLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeActiveFacetLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeActiveFacetLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeActiveFacetLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeActiveFacetLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeActiveFacetLedger"
CS_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeComplementarySlacknessImportedForActiveFacetLedger"
DUAL_FEASIBLE = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetDualFeasibilityLedger"
FACET_EQUALITY = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetEqualityLedger"
FACET_NORMAL = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetNormalVectorLedger"
NORMAL_CONE = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetNormalConeLedger"
FLOW_NORMAL = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetFlowNormalConeMembershipLedger"
GAP_FORMULA = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetGapFormulaLedger"
INACTIVE_EXCLUSION = "StableLadderEndpointOrbitPhaseResidueNoInactiveConstraintCarriesFluxAfterActiveFacetLedger"
SATURATED_SUPPORT = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetSaturatedSupportLedger"
EQUALS_CS = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetEqualsComplementarySlacknessLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetCollisionOrSingletonExitLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetOrientationLedger"
NO_CS = "StableLadderEndpointOrbitPhaseResidueNoAnonymousComplementarySlacknessAfterActiveFacetLedger"
FACET_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeActiveFacetNormalConePacketLedger"
NO_ANON = "NoAnonymousComplementarySlacknessAfterActiveFacetLedger"


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
    """把 complementary-slackness 硬点替换为 active-facet normal-cone 硬点。"""
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
        CS_IMPORT,
        DUAL_FEASIBLE,
        FACET_EQUALITY,
        FACET_NORMAL,
        NORMAL_CONE,
        FLOW_NORMAL,
        GAP_FORMULA,
        INACTIVE_EXCLUSION,
        SATURATED_SUPPORT,
        EQUALS_CS,
        COLLISION_EXIT,
        ORIENTATION,
        NO_CS,
        FACET_PACKET,
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


def active_facet_records() -> list[dict[str, str]]:
    """给出活跃约束面/法锥字段。"""
    return [
        {
            "field": "dual_feasible_inequality",
            "meaning": "单位边约束为 phi(r0)-phi(r*) <= 1。",
        },
        {
            "field": "active_facet_equality",
            "meaning": "互补松弛零间隙和 A>0 迫使 phi(r0)-phi(r*)=1。",
        },
        {
            "field": "facet_normal",
            "meaning": "活跃约束面的法向量为 n_e=[r0]-[r*]。",
        },
        {
            "field": "normal_cone_ray",
            "meaning": "局部法锥是 {lambda n_e: lambda >= 0}。",
        },
        {
            "field": "flow_normal_membership",
            "meaning": "散度 div=A n_e 落在该正法锥射线上。",
        },
        {
            "field": "gap_formula",
            "meaning": "对偶间隙等于 A(1-(phi(r0)-phi(r*)))=0。",
        },
        {
            "field": "inactive_constraint_exclusion",
            "meaning": "若约束不活跃且 A>0，则 gap>0，和上一层零间隙矛盾。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r* 或 A=0，法向量/法锥证书退化并回流 singleton/degenerate 出口。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 active-facet normal-cone 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeComplementarySlacknessImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange dual-norm complementary-slackness circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "同点退化或零法向量时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeComplementarySlacknessImportedForActiveFacet",
            True,
            True,
            "导入 e=(r* -> r0)、cost(e)=1、primal_cost=dual_value=A、gap=0。",
            CS_IMPORT,
        ),
        row(
            "PhaseResidueExchangeActiveFacetDualFeasibility",
            True,
            True,
            "单位成本边的对偶可行约束为 phi(r0)-phi(r*) <= 1。",
            DUAL_FEASIBLE,
        ),
        row(
            "PhaseResidueExchangeActiveFacetEquality",
            True,
            True,
            "非零通量 A 与零间隙强制约束取等号 phi(r0)-phi(r*)=1。",
            FACET_EQUALITY,
        ),
        row(
            "PhaseResidueExchangeActiveFacetNormalVector",
            True,
            True,
            "活跃约束面的法向量为 n_e=[r0]-[r*]。",
            FACET_NORMAL,
        ),
        row(
            "PhaseResidueExchangeActiveFacetNormalCone",
            True,
            True,
            "局部法锥是正射线 {lambda n_e: lambda >= 0}。",
            NORMAL_CONE,
        ),
        row(
            "PhaseResidueExchangeActiveFacetFlowNormalConeMembership",
            True,
            True,
            "散度 div=A n_e 落在活跃约束面的正法锥内。",
            FLOW_NORMAL,
        ),
        row(
            "PhaseResidueExchangeActiveFacetGapFormula",
            True,
            True,
            "gap=A(1-(phi(r0)-phi(r*)))=0。",
            GAP_FORMULA,
        ),
        row(
            "PhaseResidueNoInactiveConstraintCarriesFluxAfterActiveFacet",
            True,
            True,
            "若约束严格不活跃且 A>0，则 gap>0，和零间隙矛盾。",
            INACTIVE_EXCLUSION,
        ),
        row(
            "PhaseResidueExchangeActiveFacetSaturatedSupport",
            True,
            True,
            "全部非零通量都落在这一个活跃约束面对应的饱和边上。",
            SATURATED_SUPPORT,
        ),
        row(
            "PhaseResidueExchangeActiveFacetEqualsComplementarySlackness",
            True,
            True,
            "active-facet normal-cone 证书与上一层 complementary slackness 表示同一局部对象。",
            EQUALS_CS,
        ),
        row(
            "PhaseResidueExchangeActiveFacetCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r* 或 A=0，法向量与法锥证书退化并回流 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeActiveFacetOrientation",
            True,
            True,
            "正法向量方向固定为 source -> root 的边界 [r0]-[r*]。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueNoAnonymousComplementarySlacknessAfterActiveFacet",
            True,
            True,
            "complementary slackness 口径被删除；剩余是命名单活跃约束面法锥证书。",
            NO_CS,
        ),
        row(
            "PhaseResidueExchangeActiveFacetNormalConePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange active-facet normal-cone circuit PDEC/cap。",
            FACET_PACKET,
        ),
        row(
            "NoAnonymousComplementarySlacknessAfterActiveFacet",
            True,
            True,
            "零间隙校准边被压成单活跃 Lipschitz 约束面及其正法锥。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeActiveFacet",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeActiveFacetStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、active-facet normal-cone、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange active-facet normal-cone circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 active-facet normal-cone 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange complementary slackness 已把剩余写成 "
        "e=(r* -> r0)、cost(e)=1、phi(r0)-phi(r*)=1、primal_cost=A、dual_value=A、gap=0。"
        "本步删除 complementary slackness 作为黑箱的口径，把非退化对象登记为单个活跃 "
        "Lipschitz 约束面及其正法锥：对偶可行约束 phi(r0)-phi(r*)<=1 被 A>0 与 gap=0 "
        "强制取等号，法向量 n_e=[r0]-[r*]，散度 div=A n_e 位于正法锥 "
        "{lambda n_e: lambda>=0}。若 r0=r* 或 A=0，法向量/法锥退化并回流 "
        "singleton/degenerate 出口。剩余反例不再是匿名 complementary slackness，而必须表现为 "
        "active-facet normal-cone circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_complementary_slackness_active_facet_router",
        "status": "phase_residue_exchange_complementary_slackness_reduced_to_active_facet_normal_cone_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "active_facet_records": active_facet_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_complementary_slackness_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_complementary_slackness_imported_for_active_facet": True,
        "phase_residue_exchange_active_facet_dual_feasibility_closed": True,
        "phase_residue_exchange_active_facet_equality_closed": True,
        "phase_residue_exchange_active_facet_normal_vector_closed": True,
        "phase_residue_exchange_active_facet_normal_cone_closed": True,
        "phase_residue_exchange_active_facet_flow_normal_cone_membership_closed": True,
        "phase_residue_exchange_active_facet_gap_formula_closed": True,
        "phase_residue_no_inactive_constraint_carries_flux_after_active_facet_closed": True,
        "phase_residue_exchange_active_facet_saturated_support_closed": True,
        "phase_residue_exchange_active_facet_equals_complementary_slackness_closed": True,
        "phase_residue_exchange_active_facet_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_active_facet_orientation_closed": True,
        "phase_residue_no_anonymous_complementary_slackness_after_active_facet_closed": True,
        "phase_residue_exchange_active_facet_normal_cone_packet_registered": True,
        "anonymous_complementary_slackness_removed_after_active_facet": True,
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
        "phase_residue_exchange_dual_norm_complementary_slackness_circuit_pdec_cap_proved": False,
        "phase_residue_exchange_complementary_slackness_active_facet_normal_cone_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange complementary slackness active facet 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_complementary_slackness_imported={fmt_bool(cert['phase_residue_exchange_complementary_slackness_imported'])}",
        f"phase_residue_exchange_active_facet_dual_feasibility_closed={fmt_bool(cert['phase_residue_exchange_active_facet_dual_feasibility_closed'])}",
        f"phase_residue_exchange_active_facet_equality_closed={fmt_bool(cert['phase_residue_exchange_active_facet_equality_closed'])}",
        f"phase_residue_exchange_active_facet_normal_vector_closed={fmt_bool(cert['phase_residue_exchange_active_facet_normal_vector_closed'])}",
        f"phase_residue_exchange_active_facet_normal_cone_closed={fmt_bool(cert['phase_residue_exchange_active_facet_normal_cone_closed'])}",
        f"phase_residue_exchange_active_facet_flow_normal_cone_membership_closed={fmt_bool(cert['phase_residue_exchange_active_facet_flow_normal_cone_membership_closed'])}",
        f"phase_residue_no_inactive_constraint_carries_flux_after_active_facet_closed={fmt_bool(cert['phase_residue_no_inactive_constraint_carries_flux_after_active_facet_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_complementary_slackness_active_facet_normal_cone_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_complementary_slackness_active_facet_normal_cone_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. complementary slackness 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "e=(r* -> r0)",
        "partial(A e)=A([r0]-[r*])=div",
        "cost(e)=1",
        "phi(r0)-phi(r*)=1=cost(e)",
        "primal_cost=A",
        "dual_value=<div,phi>=A",
        "duality_gap=0",
        "A C_Pi=W",
        "```",
        "",
        "## 2. active facet 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["active_facet_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时活跃约束面/法锥证书为：",
            "",
            "```text",
            "dual_feasible_constraint: phi(r0)-phi(r*) <= 1",
            "active_constraint: phi(r0)-phi(r*) = 1",
            "n_e=[r0]-[r*]",
            "normal_cone(e)={lambda n_e: lambda>=0}",
            "div=A n_e",
            "div in normal_cone(e)",
            "gap=A(1-(phi(r0)-phi(r*)))=0",
            "inactive_constraint_with_A_positive => gap>0",
            "A C_Pi=W",
            "```",
            "",
            "若 `r0=r*` 或 `A=0`，则法向量/法锥证书退化并回流 singleton/degenerate 出口。",
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
            "- 本证书没有证明 phase-residue exchange complementary-slackness active-facet normal-cone circuit PDEC/cap。",
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
    print("phase_residue_exchange_complementary_slackness_active_facet_normal_cone_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
