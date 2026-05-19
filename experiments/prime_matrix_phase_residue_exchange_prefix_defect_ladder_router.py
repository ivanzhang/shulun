#!/usr/bin/env python3
"""生成 phase-residue exchange prefix defect ladder 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_prefix_defect_ladder_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.json

输出：
  data/prime-matrix-phase-residue-exchange-prefix-defect-ladder-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-prefix-defect-ladder"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-toggle-word-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeToggleWordCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangePrefixDefectLadderCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeToggleWordImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangePrefixDefectLadderLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangePrefixDefectLadderLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangePrefixDefectLadderLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangePrefixDefectLadderLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangePrefixDefectLadderLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangePrefixDefectLadderLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangePrefixDefectLadderLedger"
TOGGLE_WORD = "StableLadderEndpointOrbitPhaseResidueExchangeToggleWordImportedForPrefixLadderLedger"
PREFIX_SOURCE_SET = "StableLadderEndpointOrbitPhaseResidueExchangePrefixSourceSetLedger"
PREFIX_BOUNDARY_SET = "StableLadderEndpointOrbitPhaseResidueExchangePrefixBoundarySetLedger"
PREFIX_UNIT_DEFECT = "StableLadderEndpointOrbitPhaseResidueExchangePrefixUnitDefectIdentityLedger"
PREFIX_NESTED = "StableLadderEndpointOrbitPhaseResidueExchangePrefixNestedLadderLedger"
PREFIX_TOGGLE_TRANSPORT = "StableLadderEndpointOrbitPhaseResidueExchangePrefixToggleStateTransportLedger"
PREFIX_BOUNDARY_INCREMENT = "StableLadderEndpointOrbitPhaseResidueExchangePrefixOneBoundaryIncrementLedger"
LADDER_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangePrefixDefectLadderPacketLedger"
NO_ANON = "NoAnonymousExchangeToggleWordAfterPrefixDefectLadderLedger"


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
    """把 exchange toggle word 硬点替换为 prefix defect ladder 硬点。"""
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
        TOGGLE_WORD,
        PREFIX_SOURCE_SET,
        PREFIX_BOUNDARY_SET,
        PREFIX_UNIT_DEFECT,
        PREFIX_NESTED,
        PREFIX_BOUNDARY_INCREMENT,
        PREFIX_TOGGLE_TRANSPORT,
        LADDER_PACKET,
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


def prefix_ladder_records() -> list[dict[str, str]]:
    """给出 prefix defect ladder 的字段。"""
    return [
        {
            "field": "prefix_source_set",
            "meaning": "第 t 个前缀源点集为 U_t={u_0,...,u_t}。",
        },
        {
            "field": "prefix_boundary_set",
            "meaning": "第 t 个前缀边界集为 B_t={b_1,...,b_t}。",
        },
        {
            "field": "unit_defect_identity",
            "meaning": "对每个 t>=1 都有 |U_t|=t+1、|B_t|=t，因此 |U_t|-|B_t|=1。",
        },
        {
            "field": "nested_ladder",
            "meaning": "U_t 与 B_t 随 t 单调嵌套，每步只新增一个源点和一个边界槽。",
        },
        {
            "field": "toggle_transport",
            "meaning": "前缀有序切换把缺失源状态从 u_0 逐步输运到 u_t。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 prefix defect ladder 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeToggleWordImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange toggle word circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "前缀链退化为孤立单点时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeToggleWordImportedForPrefixLadder",
            True,
            True,
            "导入上一层交替顶点词和局部 pivot 有序乘积。",
            TOGGLE_WORD,
        ),
        row(
            "PhaseResidueExchangePrefixSourceSet",
            True,
            True,
            "每个前缀定义 U_t={u_0,...,u_t}。",
            PREFIX_SOURCE_SET,
        ),
        row(
            "PhaseResidueExchangePrefixBoundarySet",
            True,
            True,
            "每个前缀定义 B_t={b_1,...,b_t}。",
            PREFIX_BOUNDARY_SET,
        ),
        row(
            "PhaseResidueExchangePrefixUnitDefectIdentity",
            True,
            True,
            "简单性给出 |U_t|=t+1 与 |B_t|=t，所以每个非空前缀都有精确单位容量缺口。",
            PREFIX_UNIT_DEFECT,
        ),
        row(
            "PhaseResidueExchangePrefixNestedLadder",
            True,
            True,
            "前缀集按 t 嵌套，每步只加入一个新源点和一个新边界槽。",
            PREFIX_NESTED,
        ),
        row(
            "PhaseResidueExchangePrefixOneBoundaryIncrement",
            True,
            True,
            "边界侧增量逐步为一个新槽，排除同一词内的边界匿名重放。",
            PREFIX_BOUNDARY_INCREMENT,
        ),
        row(
            "PhaseResidueExchangePrefixToggleStateTransport",
            True,
            True,
            "前缀有序切换把缺失源状态从 u_0 输运到 u_t。",
            PREFIX_TOGGLE_TRANSPORT,
        ),
        row(
            "PhaseResidueExchangePrefixDefectLadderPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange prefix defect ladder circuit PDEC/cap。",
            LADDER_PACKET,
        ),
        row(
            "NoAnonymousExchangeToggleWordAfterPrefixDefectLadder",
            True,
            True,
            "exchange toggle word 不再匿名保留；它含嵌套前缀单位缺口链或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangePrefixDefectLadder",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangePrefixDefectLadderStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、exchange prefix defect ladder、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange prefix defect ladder circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 prefix defect ladder 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange toggle word 已把路径写成 u_0=s,b_1,u_1,...,b_r,u_r=s0。"
        "对每个前缀定义 U_t={u_0,...,u_t} 与 B_t={b_1,...,b_t}；简单性给出"
        " |U_t|=t+1、|B_t|=t，因此每个非空前缀都是精确单位缺口。"
        "前缀链嵌套且每步只新增一个边界槽，前缀切换把缺失源从 u_0 输运到 u_t。"
        "剩余反例不再是匿名切换词，而是嵌套的 exchange prefix defect ladder circuit PDEC/cap。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_prefix_defect_ladder_router",
        "status": "phase_residue_exchange_toggle_word_reduced_to_exchange_prefix_defect_ladder_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "prefix_ladder_records": prefix_ladder_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_toggle_word_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_toggle_word_imported_for_prefix_ladder": True,
        "phase_residue_exchange_prefix_source_set_closed": True,
        "phase_residue_exchange_prefix_boundary_set_closed": True,
        "phase_residue_exchange_prefix_unit_defect_identity_closed": True,
        "phase_residue_exchange_prefix_nested_ladder_closed": True,
        "phase_residue_exchange_prefix_one_boundary_increment_closed": True,
        "phase_residue_exchange_prefix_toggle_state_transport_closed": True,
        "phase_residue_exchange_prefix_defect_ladder_packet_registered": True,
        "anonymous_exchange_toggle_word_removed_after_prefix_defect_ladder": True,
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
        "phase_residue_exchange_prefix_defect_ladder_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange prefix defect ladder 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_toggle_word_imported={fmt_bool(cert['phase_residue_exchange_toggle_word_imported'])}",
        f"phase_residue_exchange_prefix_unit_defect_identity_closed={fmt_bool(cert['phase_residue_exchange_prefix_unit_defect_identity_closed'])}",
        f"phase_residue_exchange_prefix_nested_ladder_closed={fmt_bool(cert['phase_residue_exchange_prefix_nested_ladder_closed'])}",
        f"phase_residue_exchange_prefix_toggle_state_transport_closed={fmt_bool(cert['phase_residue_exchange_prefix_toggle_state_transport_closed'])}",
        f"phase_residue_exchange_prefix_defect_ladder_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_prefix_defect_ladder_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前缀单位缺口",
        "",
        "上一层把路径写成有限交替词：",
        "",
        "```text",
        "P_s = (u_0=s, b_1, u_1, ..., b_r, u_r=s0)",
        "```",
        "",
        "对任意 `1<=t<=r` 定义前缀：",
        "",
        "```text",
        "U_t = {u_0,...,u_t}",
        "B_t = {b_1,...,b_t}",
        "```",
        "",
        "由于词内源点和边界槽分别互异，`|U_t|=t+1` 且 `|B_t|=t`，所以每个非空前缀都有精确单位缺口 `|U_t|-|B_t|=1`。",
        "",
        "## 2. 嵌套前缀链",
        "",
        "`U_t` 与 `B_t` 随 `t` 单调嵌套；从第 `t-1` 层到第 `t` 层只新增源点 `u_t` 和边界槽 `b_t`。因此剩余结构不是无序切换词，而是一条逐步增长的容量缺口链。",
        "",
        "## 3. 前缀切换输运",
        "",
        "第 `t` 个前缀的有序 pivot 乘积把缺失源状态从 `u_0` 输运到 `u_t`。整个词的最终状态是 `u_r=s0`，中间每个前缀状态都带有同一个精确单位缺口。",
        "",
        "## 4. prefix defect ladder 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["prefix_ladder_records"]:
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
            "- 本证书没有证明 phase-residue exchange prefix defect ladder circuit PDEC/cap。",
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
    print("phase_residue_exchange_prefix_defect_ladder_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
