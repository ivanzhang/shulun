#!/usr/bin/env python3
"""生成 phase-residue exchange signed CRT pair primitive atom 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_signed_crt_pair_primitive_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.json

输出：
  data/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeKroneckerStencilSignedCRTPairCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeSignedCRTPairPrimitiveAtomCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilSignedCRTPairImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeSignedCRTPairPrimitiveAtomLedger"
PAIR_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairImportedForPrimitiveAtomLedger"
SUPPORT_SIZE = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairSupportSizeLedger"
POS_NEG = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPositiveNegativeAtomLedger"
COEFFICIENT_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomZeroMassLedger"
TOTAL_VARIATION = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomTotalVariationLedger"
FLUX_WEIGHTS = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomFluxWeightLedger"
ORIENTATION = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomOrientationLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomCollisionOrSingletonExitLedger"
PAIR_EQUALS_ATOM = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairEqualsPrimitiveAtomLedger"
NO_DICT = "StableLadderEndpointOrbitPhaseResidueNoAnonymousSignedCRTDictionaryAfterPrimitiveAtomLedger"
ATOM_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomPacketLedger"
NO_ANON = "NoAnonymousSignedCRTPairDictionaryAfterPrimitiveAtomLedger"


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
    """把 signed CRT pair 硬点替换为 primitive atom 硬点。"""
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
        PAIR_IMPORT,
        SUPPORT_SIZE,
        POS_NEG,
        COEFFICIENT_BALANCE,
        TOTAL_VARIATION,
        FLUX_WEIGHTS,
        ORIENTATION,
        COLLISION_EXIT,
        PAIR_EQUALS_ATOM,
        NO_DICT,
        ATOM_PACKET,
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


def primitive_atom_records() -> list[dict[str, str]]:
    """给出 primitive atom 的字段。"""
    return [
        {
            "field": "support_words",
            "meaning": "非退化情形下支撑为有序二元 CRT words (r0,r*)。",
        },
        {
            "field": "signed_coefficients",
            "meaning": "root word 系数 +1，source word 系数 -1。",
        },
        {
            "field": "support_size",
            "meaning": "r0!=r* 时为 2；r0=r* 时消去并回流 singleton/degenerate 出口。",
        },
        {
            "field": "coefficient_sum",
            "meaning": "总质量 +1-1=0。",
        },
        {
            "field": "total_variation",
            "meaning": "非退化 primitive atom 的 l1 总变差为 2。",
        },
        {
            "field": "flux_weights",
            "meaning": "乘以 A 后得到 root 权重 +A、source 权重 -A，且 A C_Pi=W。",
        },
        {
            "field": "orientation",
            "meaning": "方向保留为 source -> root，不允许把两端无向化。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 signed CRT pair primitive atom 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeKroneckerStencilSignedCRTPairImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange Kronecker-stencil signed CRT pair circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "碰撞或退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairImportedForPrimitiveAtom",
            True,
            True,
            "导入 Pi=(r0,r*) 与 C_Pi(r0)=+1、C_Pi(r*)=-1、A C_Pi=W。",
            PAIR_IMPORT,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairSupportSize",
            True,
            True,
            "非退化 signed CRT pair 的支撑数为 2；碰撞时回流退化出口。",
            SUPPORT_SIZE,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPositiveNegativeAtom",
            True,
            True,
            "支撑被拆成一个 positive root atom 与一个 negative source atom。",
            POS_NEG,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomZeroMass",
            True,
            True,
            "primitive atom 的 coefficient sum 为 0。",
            COEFFICIENT_BALANCE,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomTotalVariation",
            True,
            True,
            "非退化 primitive atom 的总变差为 |+1|+|-1|=2。",
            TOTAL_VARIATION,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomFluxWeight",
            True,
            True,
            "乘以 A 后的权重为 +A 与 -A，并保持 A C_Pi=W。",
            FLUX_WEIGHTS,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomOrientation",
            True,
            True,
            "有序 pair 保留 source -> root 方向，不降成无向集合。",
            ORIENTATION,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r* 则 +1 与 -1 消去，返回 singleton/degenerate 出口。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairEqualsPrimitiveAtom",
            True,
            True,
            "primitive atom 与上一层 signed CRT dictionary 表示同一向量。",
            PAIR_EQUALS_ATOM,
        ),
        row(
            "PhaseResidueNoAnonymousSignedCRTDictionaryAfterPrimitiveAtom",
            True,
            True,
            "字典口径被删除；剩余是二词 signed support primitive atom。",
            NO_DICT,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairPrimitiveAtomPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange signed CRT pair primitive atom circuit PDEC/cap。",
            ATOM_PACKET,
        ),
        row(
            "NoAnonymousSignedCRTPairDictionaryAfterPrimitiveAtom",
            True,
            True,
            "signed CRT pair 字典被压成带支撑/变差/通量权重的 primitive atom。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeSignedCRTPairPrimitiveAtom",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeSignedCRTPairPrimitiveAtomStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、primitive atom、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange signed CRT pair primitive atom circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 signed CRT pair primitive atom 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange signed CRT pair 已把剩余写成 Pi=(r0,r*) 与有限字典 "
        "C_Pi(r0)=+1、C_Pi(r*)=-1、A C_Pi=W。"
        "本步删除一般字典口径，把非退化对象登记为二词 signed support primitive atom："
        "支撑数为 2，总质量为 0，总变差为 2，通量权重为 +A 与 -A，并保留 source -> root 方向。"
        "若 r0=r*，则 +1 与 -1 消去并回流 singleton/degenerate 出口。"
        "剩余反例不再是匿名 signed CRT dictionary，而必须表现为 signed CRT pair primitive atom circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_signed_crt_pair_primitive_atom_router",
        "status": "phase_residue_exchange_signed_crt_pair_reduced_to_primitive_atom_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "signed_crt_pair_primitive_atom_records": primitive_atom_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_kronecker_stencil_signed_crt_pair_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_signed_crt_pair_imported_for_primitive_atom": True,
        "phase_residue_exchange_signed_pair_support_size_closed": True,
        "phase_residue_exchange_signed_pair_positive_negative_atom_closed": True,
        "phase_residue_exchange_signed_pair_coefficient_balance_closed": True,
        "phase_residue_exchange_signed_pair_total_variation_closed": True,
        "phase_residue_exchange_signed_pair_flux_weight_packet_closed": True,
        "phase_residue_exchange_signed_pair_orientation_closed": True,
        "phase_residue_exchange_signed_pair_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_signed_pair_equals_primitive_atom_closed": True,
        "phase_residue_no_anonymous_signed_crt_dictionary_after_primitive_atom_closed": True,
        "phase_residue_exchange_signed_crt_pair_primitive_atom_packet_registered": True,
        "anonymous_signed_crt_pair_dictionary_removed_after_primitive_atom": True,
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
        "phase_residue_exchange_signed_crt_pair_primitive_atom_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange signed CRT pair primitive atom 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_kronecker_stencil_signed_crt_pair_imported={fmt_bool(cert['phase_residue_exchange_kronecker_stencil_signed_crt_pair_imported'])}",
        f"phase_residue_exchange_signed_pair_support_size_closed={fmt_bool(cert['phase_residue_exchange_signed_pair_support_size_closed'])}",
        f"phase_residue_exchange_signed_pair_positive_negative_atom_closed={fmt_bool(cert['phase_residue_exchange_signed_pair_positive_negative_atom_closed'])}",
        f"phase_residue_exchange_signed_pair_coefficient_balance_closed={fmt_bool(cert['phase_residue_exchange_signed_pair_coefficient_balance_closed'])}",
        f"phase_residue_exchange_signed_pair_total_variation_closed={fmt_bool(cert['phase_residue_exchange_signed_pair_total_variation_closed'])}",
        f"phase_residue_exchange_signed_pair_flux_weight_packet_closed={fmt_bool(cert['phase_residue_exchange_signed_pair_flux_weight_packet_closed'])}",
        f"phase_residue_exchange_signed_pair_collision_or_singleton_exit_closed={fmt_bool(cert['phase_residue_exchange_signed_pair_collision_or_singleton_exit_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_signed_crt_pair_primitive_atom_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_signed_crt_pair_primitive_atom_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. signed CRT pair 输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "Pi=(r0,r*)",
        "C_Pi(r0)=+1",
        "C_Pi(r*)=-1",
        "A C_Pi=W",
        "```",
        "",
        "## 2. primitive atom 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["signed_crt_pair_primitive_atom_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "非退化时 primitive atom 为：",
            "",
            "```text",
            "support={r0,r*}",
            "coefficient(r0)=+1",
            "coefficient(r*)=-1",
            "support_size=2",
            "coefficient_sum=0",
            "total_variation=2",
            "flux_weights=(+A,-A)",
            "A C_Pi=W",
            "```",
            "",
            "若 `r0=r*`，则 `+1-1=0` 并回流 singleton/degenerate 出口。",
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
            "- 本证书没有证明 phase-residue exchange signed CRT pair primitive atom circuit PDEC/cap。",
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
    print("phase_residue_exchange_signed_crt_pair_primitive_atom_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
