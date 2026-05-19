#!/usr/bin/env python3
"""生成 phase-residue exchange oriented root-source witness gap 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_oriented_root_source_witness_gap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.json

输出：
  data/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeRootSourcePairWitnessLocalizationCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeOrientedRootSourceWitnessGapCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairWitnessLocalizationImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeOrientedRootSourceWitnessGapLedger"
LOCALIZATION_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairWitnessLocalizationImportedForOrientedGapLedger"
NAMED_PAIR = "StableLadderEndpointOrbitPhaseResidueExchangeNamedRootSourcePairLedger"
WITNESS_ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeWitnessOrientationCarriedForwardLedger"
ROOT_SCORE = "StableLadderEndpointOrbitPhaseResidueExchangeRootWitnessScoreLedger"
SOURCE_SCORE = "StableLadderEndpointOrbitPhaseResidueExchangeSourceWitnessScoreLedger"
SIGNED_GAP = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedWitnessGapCoordinateLedger"
GAP_LOWER_BOUND = "StableLadderEndpointOrbitPhaseResidueExchangeWitnessGapLowerBoundLedger"
NO_PAIR_ANON = "StableLadderEndpointOrbitPhaseResidueNoAnonymousPairWitnessAfterOrientedGapLedger"
GAP_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedRootSourceWitnessGapPacketLedger"
NO_ANON = "NoAnonymousRootSourcePairWitnessLocalizationAfterOrientedGapLedger"


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
    """把 pair witness localization 硬点替换为 oriented witness gap 硬点。"""
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
        LOCALIZATION_IMPORT,
        NAMED_PAIR,
        WITNESS_ORIENTATION,
        ROOT_SCORE,
        SOURCE_SCORE,
        SIGNED_GAP,
        GAP_LOWER_BOUND,
        NO_PAIR_ANON,
        GAP_PACKET,
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


def gap_records() -> list[dict[str, str]]:
    """给出 oriented root-source witness gap 的字段。"""
    return [
        {
            "field": "named_pair",
            "meaning": "导入上一层定位出的命名单对 (s0,s*)。",
        },
        {
            "field": "oriented_witness",
            "meaning": "保留定向符号 sigma 与线性见证 Lambda。",
        },
        {
            "field": "root_score",
            "meaning": "根端分数 R=sigma*Lambda([s0])。",
        },
        {
            "field": "source_score",
            "meaning": "源端分数 T=sigma*Lambda([s*])。",
        },
        {
            "field": "oriented_gap",
            "meaning": "有向差值 G=R-T=sigma*Lambda([s0]-[s*])。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 oriented root-source witness gap 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeRootSourcePairWitnessLocalizationImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange root-source pair witness localization circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairWitnessLocalizationImportedForOrientedGap",
            True,
            True,
            "导入命名单对 s* 与定向见证 sigma*Lambda。",
            LOCALIZATION_IMPORT,
        ),
        row(
            "PhaseResidueExchangeNamedRootSourcePair",
            True,
            True,
            "剩余对象固定为一对端点 (s0,s*)，不再是平均扇。",
            NAMED_PAIR,
        ),
        row(
            "PhaseResidueExchangeWitnessOrientationCarriedForward",
            True,
            True,
            "上一层的定向符号 sigma 继续固定，保证见证值为非负方向。",
            WITNESS_ORIENTATION,
        ),
        row(
            "PhaseResidueExchangeRootWitnessScore",
            True,
            True,
            "登记根端分数 R=sigma*Lambda([s0])。",
            ROOT_SCORE,
        ),
        row(
            "PhaseResidueExchangeSourceWitnessScore",
            True,
            True,
            "登记源端分数 T=sigma*Lambda([s*])。",
            SOURCE_SCORE,
        ),
        row(
            "PhaseResidueExchangeOrientedWitnessGapCoordinate",
            True,
            True,
            "线性性给出 G=sigma*Lambda([s0]-[s*])=R-T。",
            SIGNED_GAP,
        ),
        row(
            "PhaseResidueExchangeWitnessGapLowerBound",
            True,
            True,
            "上一层定位值给出 G >= |Lambda(D)|，若平均见证非零则 G>0。",
            GAP_LOWER_BOUND,
        ),
        row(
            "PhaseResidueNoAnonymousPairWitnessAfterOrientedGap",
            True,
            True,
            "单对见证不再匿名保留；它是根端分数与源端分数的有向差。",
            NO_PAIR_ANON,
        ),
        row(
            "PhaseResidueExchangeOrientedRootSourceWitnessGapPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange oriented root-source witness gap circuit PDEC/cap。",
            GAP_PACKET,
        ),
        row(
            "NoAnonymousRootSourcePairWitnessLocalizationAfterOrientedGap",
            True,
            True,
            "root-source pair witness localization 不再匿名保留；它被压成有向两端点差值坐标。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeOrientedRootSourceWitnessGap",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeOrientedRootSourceWitnessGapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、oriented root-source witness gap、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange oriented root-source witness gap circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 oriented root-source witness gap 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange root-source pair witness localization 已把平均见证定位到一个命名单对。"
        "本步把该单对见证写成有向两端点差值："
        " G=sigma*Lambda([s0]-[s*])=sigma*Lambda([s0])-sigma*Lambda([s*])。"
        "上一层给出 G>=|Lambda(D)|；若平均见证非零，则 G>0。"
        "剩余反例不再是匿名单对见证，而必须表现为 oriented root-source witness gap circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_oriented_root_source_witness_gap_router",
        "status": "phase_residue_exchange_root_source_pair_witness_localization_reduced_to_oriented_root_source_witness_gap_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "oriented_root_source_witness_gap_records": gap_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_root_source_pair_witness_localization_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_root_source_pair_witness_localization_imported_for_oriented_gap": True,
        "phase_residue_exchange_named_root_source_pair_closed": True,
        "phase_residue_exchange_witness_orientation_carried_forward_closed": True,
        "phase_residue_exchange_root_witness_score_closed": True,
        "phase_residue_exchange_source_witness_score_closed": True,
        "phase_residue_exchange_oriented_witness_gap_coordinate_closed": True,
        "phase_residue_exchange_witness_gap_lower_bound_closed": True,
        "phase_residue_no_anonymous_pair_witness_after_oriented_gap_closed": True,
        "phase_residue_exchange_oriented_root_source_witness_gap_packet_registered": True,
        "anonymous_root_source_pair_witness_localization_removed_after_oriented_gap": True,
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
        "phase_residue_exchange_oriented_root_source_witness_gap_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange oriented root-source witness gap 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_root_source_pair_witness_localization_imported={fmt_bool(cert['phase_residue_exchange_root_source_pair_witness_localization_imported'])}",
        f"phase_residue_exchange_named_root_source_pair_closed={fmt_bool(cert['phase_residue_exchange_named_root_source_pair_closed'])}",
        f"phase_residue_exchange_oriented_witness_gap_coordinate_closed={fmt_bool(cert['phase_residue_exchange_oriented_witness_gap_coordinate_closed'])}",
        f"phase_residue_exchange_witness_gap_lower_bound_closed={fmt_bool(cert['phase_residue_exchange_witness_gap_lower_bound_closed'])}",
        f"phase_residue_exchange_oriented_root_source_witness_gap_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_oriented_root_source_witness_gap_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单对定位输入",
        "",
        "上一层给出一个命名源点 `s*` 与定向见证：",
        "",
        "```text",
        "sigma * Lambda([s0]-[s*]) >= |Lambda(D)|",
        "```",
        "",
        "这里 `sigma` 是 `Lambda(D)` 的符号。本证书继续不证明 `Lambda` 的存在。",
        "",
        "## 2. 两端点分数",
        "",
        "定义根端分数和源端分数：",
        "",
        "```text",
        "R = sigma * Lambda([s0])",
        "T = sigma * Lambda([s*])",
        "```",
        "",
        "由线性性得到有向差值坐标：",
        "",
        "```text",
        "G = R - T = sigma * Lambda([s0]-[s*])",
        "```",
        "",
        "## 3. 差值下界",
        "",
        "上一层的单对定位直接给出：",
        "",
        "```text",
        "G >= |Lambda(D)|",
        "```",
        "",
        "若平均见证非零，则 `G>0`。因此剩余压力被压成根端分数严格高于源端分数的有向差值口径。",
        "",
        "## 4. oriented root-source witness gap 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["oriented_root_source_witness_gap_records"]:
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
            "- 本证书没有证明 phase-residue exchange oriented root-source witness gap circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
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
    print("phase_residue_exchange_oriented_root_source_witness_gap_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
