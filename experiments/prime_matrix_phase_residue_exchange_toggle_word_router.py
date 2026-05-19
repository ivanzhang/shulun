#!/usr/bin/env python3
"""生成 phase-residue exchange toggle word 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_toggle_word_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.json

输出：
  data/prime-matrix-phase-residue-exchange-toggle-word-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-toggle-word"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-rooted-directed-exchange-path-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomRootedDirectedExchangePathCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeToggleWordCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueRootedDirectedExchangePathImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeToggleWordLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeToggleWordLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeToggleWordLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeToggleWordLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeToggleWordLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeToggleWordLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeToggleWordLedger"
ROOTED_PATH = "StableLadderEndpointOrbitPhaseResidueRootedDirectedExchangePathImportedForToggleWordLedger"
ALTERNATING_WORD = "StableLadderEndpointOrbitPhaseResidueAlternatingVertexWordNormalFormLedger"
SOURCE_DISTINCT = "StableLadderEndpointOrbitPhaseResidueExchangeWordSourceDistinctnessLedger"
BOUNDARY_DISTINCT = "StableLadderEndpointOrbitPhaseResidueExchangeWordBoundaryDistinctnessLedger"
LOCAL_PIVOTS = "StableLadderEndpointOrbitPhaseResidueExchangeWordLocalPivotCellLedger"
ORDERED_PRODUCT = "StableLadderEndpointOrbitPhaseResidueOrderedToggleProductLedger"
NO_REUSE = "StableLadderEndpointOrbitPhaseResidueNoInternalBoundaryReuseInToggleWordLedger"
WORD_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeToggleWordPacketLedger"
NO_ANON = "NoAnonymousRootedDirectedExchangePathAfterToggleWordLedger"


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
    """把 rooted directed exchange path 硬点替换为 exchange toggle word 硬点。"""
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
        ROOTED_PATH,
        ALTERNATING_WORD,
        SOURCE_DISTINCT,
        BOUNDARY_DISTINCT,
        LOCAL_PIVOTS,
        ORDERED_PRODUCT,
        NO_REUSE,
        WORD_PACKET,
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


def toggle_word_records() -> list[dict[str, str]]:
    """给出 exchange toggle word 的字段。"""
    return [
        {
            "field": "vertex_word",
            "meaning": "每条路径写成 u_0=s,b_1,u_1,...,b_r,u_r=s0。",
        },
        {
            "field": "distinctness",
            "meaning": "简单路径保证 u_i 互异且 b_i 互异；路径内没有边界槽复用。",
        },
        {
            "field": "local_pivot_cell",
            "meaning": "第 i 个二步单元为 u_{i-1}->b_i->u_i。",
        },
        {
            "field": "toggle_rule",
            "meaning": "局部 pivot 将 M0 边 (u_{i-1},b_i) 替换为 M_s 边 (u_i,b_i)。",
        },
        {
            "field": "ordered_product",
            "meaning": "整条路径切换是这些局部 pivot 的有序有限乘积。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 exchange toggle word 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueRootedDirectedExchangePathImported",
            imported,
            False,
            "上一层剩余含 phase-residue rooted directed exchange path circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "切换词退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueRootedDirectedExchangePathImportedForToggleWord",
            True,
            True,
            "导入上一层根向有向简单交替路径。",
            ROOTED_PATH,
        ),
        row(
            "PhaseResidueAlternatingVertexWordNormalForm",
            True,
            True,
            "把路径写成 u_0,b_1,u_1,...,b_r,u_r 的交替顶点词。",
            ALTERNATING_WORD,
        ),
        row(
            "PhaseResidueExchangeWordSourceDistinctness",
            True,
            True,
            "简单路径保证词内源点 u_i 互异。",
            SOURCE_DISTINCT,
        ),
        row(
            "PhaseResidueExchangeWordBoundaryDistinctness",
            True,
            True,
            "简单路径保证词内边界槽 b_i 互异。",
            BOUNDARY_DISTINCT,
        ),
        row(
            "PhaseResidueExchangeWordLocalPivotCell",
            True,
            True,
            "每个二步片段 u_{i-1}->b_i->u_i 是一个局部 pivot cell。",
            LOCAL_PIVOTS,
        ),
        row(
            "PhaseResidueOrderedToggleProduct",
            True,
            True,
            "整条路径切换是局部 pivot 的有序有限乘积。",
            ORDERED_PRODUCT,
        ),
        row(
            "PhaseResidueNoInternalBoundaryReuseInToggleWord",
            True,
            True,
            "词内边界槽不复用，容量支付不能在同一路径内匿名重放。",
            NO_REUSE,
        ),
        row(
            "PhaseResidueExchangeToggleWordPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange toggle word circuit PDEC/cap。",
            WORD_PACKET,
        ),
        row(
            "NoAnonymousRootedDirectedExchangePathAfterToggleWord",
            True,
            True,
            "rooted directed exchange path 不再匿名保留；它含交替顶点词和局部 pivot 切换规则或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeToggleWord",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeToggleWordStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、exchange toggle word、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange toggle word circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 exchange toggle word 证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    plain = (
        "phase-residue rooted directed exchange path 已把每个源点 s 指向基准缺失源点 s0。"
        "任一简单有向交替路径可唯一写成 u_0=s,b_1,u_1,...,b_r,u_r=s0。"
        "简单性给出 u_i 与 b_i 在词内分别互异；每个二步片段 u_{i-1}->b_i->u_i 是局部 pivot，"
        "把 M0 边 (u_{i-1},b_i) 替换为 M_s 边 (u_i,b_i)。"
        "整条切换是这些局部 pivot 的有序有限乘积。"
        "剩余反例不再是匿名有向路径，而是边界不复用的 exchange toggle word circuit PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_toggle_word_router",
        "status": "phase_residue_rooted_directed_exchange_path_reduced_to_exchange_toggle_word_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": old_target or OLD_TARGET,
        "hardpoint_after_router": reduced,
        "phase_residue_rooted_directed_exchange_path_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "phase_residue_rooted_directed_exchange_path_imported_for_toggle_word": True,
        "phase_residue_alternating_vertex_word_normal_form_closed": True,
        "phase_residue_exchange_word_source_distinctness_closed": True,
        "phase_residue_exchange_word_boundary_distinctness_closed": True,
        "phase_residue_exchange_word_local_pivot_cell_closed": True,
        "phase_residue_ordered_toggle_product_closed": True,
        "phase_residue_no_internal_boundary_reuse_in_toggle_word_closed": True,
        "phase_residue_exchange_toggle_word_packet_registered": True,
        "anonymous_rooted_directed_exchange_path_removed_after_toggle_word": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "phase_residue_exchange_toggle_word_circuit_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "exchange_toggle_word_formulas": {
            "word": "P_s=(u_0=s,b_1,u_1,...,b_r,u_r=s0)",
            "source_distinct": "u_i are pairwise distinct inside P_s",
            "boundary_distinct": "b_i are pairwise distinct inside P_s",
            "local_pivot": "C_i=(u_{i-1},b_i,u_i)",
            "toggle_rule": "(u_{i-1},b_i) in M0, (u_i,b_i) in M_s",
            "ordered_product": "toggle(P_s)=C_r o ... o C_1",
            "new_exit": NEW_TARGET,
        },
        "exchange_toggle_word_records": toggle_word_records(),
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "decision_rows": build_rows(previous, new_target),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange toggle word 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_rooted_directed_exchange_path_imported={fmt_bool(cert['phase_residue_rooted_directed_exchange_path_imported'])}",
        f"phase_residue_alternating_vertex_word_normal_form_closed={fmt_bool(cert['phase_residue_alternating_vertex_word_normal_form_closed'])}",
        f"phase_residue_exchange_word_boundary_distinctness_closed={fmt_bool(cert['phase_residue_exchange_word_boundary_distinctness_closed'])}",
        f"phase_residue_no_internal_boundary_reuse_in_toggle_word_closed={fmt_bool(cert['phase_residue_no_internal_boundary_reuse_in_toggle_word_closed'])}",
        f"phase_residue_exchange_toggle_word_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_toggle_word_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 交替顶点词",
        "",
        "上一层给出从 `s` 到 `s0` 的简单根向有向交替路径。",
        "把该路径写成有限交替词：",
        "",
        "```text",
        "P_s = (u_0=s, b_1, u_1, ..., b_r, u_r=s0)",
        "```",
        "",
        "简单路径意味着词内源点 `u_i` 两两不同，边界槽 `b_i` 两两不同。",
        "因此同一条交换词内没有边界槽复用，也不能靠同一路径内部重放同一支付槽来隐藏容量缺口。",
        "",
        "## 2. 局部 pivot 单元",
        "",
        "每个二步片段形成一个局部 pivot：",
        "",
        "```text",
        "C_i = (u_{i-1} -> b_i -> u_i)",
        "```",
        "",
        "其中 `(u_{i-1},b_i)` 是 `M0` 的边，`(u_i,b_i)` 是 `M_s` 的边。",
        "局部切换把前者替换为后者；整条路径切换是这些局部 pivot 的有序有限乘积。",
        "",
        "## 3. exchange toggle word 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["exchange_toggle_word_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend([
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 5. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend([
        "",
        "## 6. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 7. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 phase-residue exchange toggle word circuit PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 8. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for file_name, digest in cert["source_hashes"].items():
        lines.append(f"| `{file_name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 ledger、JSON 证书和 Markdown 说明。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
        "outputs": [
            str(OUT_LEDGER.relative_to(ROOT)),
            str(OUT_JSON.relative_to(ROOT)),
            str(OUT_MD.relative_to(ROOT)),
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
