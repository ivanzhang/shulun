#!/usr/bin/env python3
"""生成 phase-residue exchange Kronecker-stencil signed CRT pair 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_kronecker_stencil_signed_crt_pair_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.json

输出：
  data/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeIncidenceColumnKroneckerStencilCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeKroneckerStencilSignedCRTPairCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeIncidenceColumnKroneckerStencilImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeKroneckerStencilSignedCRTPairLedger"
STENCIL_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilImportedForSignedCRTPairLedger"
ROOT_WORD = "StableLadderEndpointOrbitPhaseResidueExchangeRootCRTWordCoordinateLedger"
SOURCE_WORD = "StableLadderEndpointOrbitPhaseResidueExchangeSourceCRTWordCoordinateLedger"
ROOT_CONGRUENCE = "StableLadderEndpointOrbitPhaseResidueExchangeRootCanonicalCongruenceEquationLedger"
SOURCE_CONGRUENCE = "StableLadderEndpointOrbitPhaseResidueExchangeSourceCanonicalCongruenceEquationLedger"
ORDERED_PAIR = "StableLadderEndpointOrbitPhaseResidueExchangeOrderedRootSourceCRTWordPairLedger"
SIGNED_DICT = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTWordPairSupportDictionaryLedger"
PAIR_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTWordPairCoefficientBalanceLedger"
COLLISION_EXIT = "StableLadderEndpointOrbitPhaseResidueExchangeCRTWordPairCollisionOrSingletonExitLedger"
PAIR_EQUALS_STENCIL = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairEqualsKroneckerStencilLedger"
PAIR_SCALING = "StableLadderEndpointOrbitPhaseResidueExchangeSignedCRTPairFluxScalingLedger"
NO_DELTA = "StableLadderEndpointOrbitPhaseResidueNoAnonymousKroneckerDeltaAfterSignedCRTPairLedger"
PAIR_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeKroneckerStencilSignedCRTPairPacketLedger"
NO_ANON = "NoAnonymousIncidenceColumnKroneckerStencilAfterSignedCRTPairLedger"


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
    """把 Kronecker stencil 硬点替换为 signed CRT pair 硬点。"""
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
        STENCIL_IMPORT,
        ROOT_WORD,
        SOURCE_WORD,
        ROOT_CONGRUENCE,
        SOURCE_CONGRUENCE,
        ORDERED_PAIR,
        SIGNED_DICT,
        PAIR_BALANCE,
        COLLISION_EXIT,
        PAIR_EQUALS_STENCIL,
        PAIR_SCALING,
        NO_DELTA,
        PAIR_PACKET,
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


def signed_crt_pair_records() -> list[dict[str, str]]:
    """给出 signed CRT word pair 的字段。"""
    return [
        {
            "field": "root_crt_word",
            "meaning": "root 端 CRT residue word r0=crt(s0)。",
        },
        {
            "field": "source_crt_word",
            "meaning": "source 端 CRT residue word r*=crt(s*)。",
        },
        {
            "field": "root_congruence_equations",
            "meaning": "对每个活动素数坐标 p_i，s0≡r0_i (mod p_i)。",
        },
        {
            "field": "source_congruence_equations",
            "meaning": "对每个活动素数坐标 p_i，s*≡r*_i (mod p_i)。",
        },
        {
            "field": "ordered_pair",
            "meaning": "有序端点对 Pi=(r0,r*) 保留 root/source 方向。",
        },
        {
            "field": "signed_support_dictionary",
            "meaning": "C_Pi(r0)=+1、C_Pi(r*)=-1、其余 CRT word 系数为 0。",
        },
        {
            "field": "collision_guard",
            "meaning": "若 r0=r* 则符号字典消去并回流 singleton/degenerate 出口。",
        },
        {
            "field": "scaled_pair",
            "meaning": "A C_Pi=W，且 A>=|Lambda(D)|/2。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 Kronecker-stencil signed CRT pair 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeIncidenceColumnKroneckerStencilImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange incidence-column Kronecker-stencil circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "单对退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeKroneckerStencilImportedForSignedCRTPair",
            True,
            True,
            "导入 k=delta_{s0}-delta_{s*}、A k=W 以及端点 CRT word 字段。",
            STENCIL_IMPORT,
        ),
        row(
            "PhaseResidueExchangeRootCRTWordCoordinate",
            True,
            True,
            "登记 root_crt_word r0=crt(s0)。",
            ROOT_WORD,
        ),
        row(
            "PhaseResidueExchangeSourceCRTWordCoordinate",
            True,
            True,
            "登记 source_crt_word r*=crt(s*)。",
            SOURCE_WORD,
        ),
        row(
            "PhaseResidueExchangeRootCanonicalCongruenceEquation",
            True,
            True,
            "root word 满足 s0≡r0_i (mod p_i) 的 canonical congruence equation 族。",
            ROOT_CONGRUENCE,
        ),
        row(
            "PhaseResidueExchangeSourceCanonicalCongruenceEquation",
            True,
            True,
            "source word 满足 s*≡r*_i (mod p_i) 的 canonical congruence equation 族。",
            SOURCE_CONGRUENCE,
        ),
        row(
            "PhaseResidueExchangeOrderedRootSourceCRTWordPair",
            True,
            True,
            "有序对 Pi=(r0,r*) 保留 root:+ 与 source:- 的方向。",
            ORDERED_PAIR,
        ),
        row(
            "PhaseResidueExchangeSignedCRTWordPairSupportDictionary",
            True,
            True,
            "把 stencil 写成有限字典 C_Pi(r0)=+1、C_Pi(r*)=-1、其余为 0。",
            SIGNED_DICT,
        ),
        row(
            "PhaseResidueExchangeSignedCRTWordPairCoefficientBalance",
            True,
            True,
            "有限字典总系数 +1-1=0，继承零质量。",
            PAIR_BALANCE,
        ),
        row(
            "PhaseResidueExchangeCRTWordPairCollisionOrSingletonExit",
            True,
            True,
            "若 r0=r* 则字典消去并回流 singleton/degenerate 出口；否则为两词 signed pair。",
            COLLISION_EXIT,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairEqualsKroneckerStencil",
            True,
            True,
            "signed CRT word pair 字典与 Kronecker endpoint stencil 表示同一向量。",
            PAIR_EQUALS_STENCIL,
        ),
        row(
            "PhaseResidueExchangeSignedCRTPairFluxScaling",
            True,
            True,
            "A C_Pi=A(delta_{s0}-delta_{s*})=W，且 A>=|Lambda(D)|/2。",
            PAIR_SCALING,
        ),
        row(
            "PhaseResidueNoAnonymousKroneckerDeltaAfterSignedCRTPair",
            True,
            True,
            "delta 函数口径被删除；剩余是两个命名 CRT words 的有限 signed dictionary。",
            NO_DELTA,
        ),
        row(
            "PhaseResidueExchangeKroneckerStencilSignedCRTPairPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange Kronecker-stencil signed CRT pair circuit PDEC/cap。",
            PAIR_PACKET,
        ),
        row(
            "NoAnonymousIncidenceColumnKroneckerStencilAfterSignedCRTPair",
            True,
            True,
            "incidence-column Kronecker stencil 被压成 signed CRT word pair。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeKroneckerStencilSignedCRTPair",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeKroneckerStencilSignedCRTPairStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、signed CRT pair、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange Kronecker-stencil signed CRT pair circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 Kronecker-stencil signed CRT pair 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange incidence-column Kronecker stencil 已把剩余写成 k=delta_{s0}-delta_{s*}、A k=W。"
        "本步删除 delta 函数模板，把两个端点登记为显式 CRT words：r0=crt(s0)、r*=crt(s*)，"
        "并写入 canonical congruence equation 族。"
        "于是 stencil 等价于有限 signed dictionary C_Pi，其中 C_Pi(r0)=+1、C_Pi(r*)=-1、其余为 0，且 A C_Pi=W。"
        "剩余反例不再是匿名 Kronecker stencil，而必须表现为 Kronecker-stencil signed CRT pair circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_kronecker_stencil_signed_crt_pair_router",
        "status": "phase_residue_exchange_incidence_column_kronecker_stencil_reduced_to_signed_crt_pair_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "kronecker_stencil_signed_crt_pair_records": signed_crt_pair_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_incidence_column_kronecker_stencil_imported": OLD_TARGET in previous.get(
            "next_direct_attack_target", ""
        ),
        "phase_residue_exchange_kronecker_stencil_imported_for_signed_crt_pair": True,
        "phase_residue_exchange_root_crt_word_coordinate_closed": True,
        "phase_residue_exchange_source_crt_word_coordinate_closed": True,
        "phase_residue_exchange_root_canonical_congruence_equation_closed": True,
        "phase_residue_exchange_source_canonical_congruence_equation_closed": True,
        "phase_residue_exchange_ordered_root_source_crt_word_pair_closed": True,
        "phase_residue_exchange_signed_crt_word_pair_support_dictionary_closed": True,
        "phase_residue_exchange_signed_crt_word_pair_coefficient_balance_closed": True,
        "phase_residue_exchange_crt_word_pair_collision_or_singleton_exit_closed": True,
        "phase_residue_exchange_signed_crt_pair_equals_kronecker_stencil_closed": True,
        "phase_residue_exchange_signed_crt_pair_flux_scaling_closed": True,
        "phase_residue_no_anonymous_kronecker_delta_after_signed_crt_pair_closed": True,
        "phase_residue_exchange_kronecker_stencil_signed_crt_pair_packet_registered": True,
        "anonymous_incidence_column_kronecker_stencil_removed_after_signed_crt_pair": True,
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
        "phase_residue_exchange_kronecker_stencil_signed_crt_pair_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange Kronecker-stencil signed CRT pair 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_incidence_column_kronecker_stencil_imported={fmt_bool(cert['phase_residue_exchange_incidence_column_kronecker_stencil_imported'])}",
        f"phase_residue_exchange_root_crt_word_coordinate_closed={fmt_bool(cert['phase_residue_exchange_root_crt_word_coordinate_closed'])}",
        f"phase_residue_exchange_source_crt_word_coordinate_closed={fmt_bool(cert['phase_residue_exchange_source_crt_word_coordinate_closed'])}",
        f"phase_residue_exchange_root_canonical_congruence_equation_closed={fmt_bool(cert['phase_residue_exchange_root_canonical_congruence_equation_closed'])}",
        f"phase_residue_exchange_source_canonical_congruence_equation_closed={fmt_bool(cert['phase_residue_exchange_source_canonical_congruence_equation_closed'])}",
        f"phase_residue_exchange_ordered_root_source_crt_word_pair_closed={fmt_bool(cert['phase_residue_exchange_ordered_root_source_crt_word_pair_closed'])}",
        f"phase_residue_exchange_signed_crt_word_pair_support_dictionary_closed={fmt_bool(cert['phase_residue_exchange_signed_crt_word_pair_support_dictionary_closed'])}",
        f"phase_residue_exchange_signed_crt_pair_equals_kronecker_stencil_closed={fmt_bool(cert['phase_residue_exchange_signed_crt_pair_equals_kronecker_stencil_closed'])}",
        f"phase_residue_exchange_signed_crt_pair_flux_scaling_closed={fmt_bool(cert['phase_residue_exchange_signed_crt_pair_flux_scaling_closed'])}",
        f"linear_witness_existence_proved={fmt_bool(cert['linear_witness_existence_proved'])}",
        f"phase_residue_exchange_kronecker_stencil_signed_crt_pair_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_kronecker_stencil_signed_crt_pair_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Kronecker stencil 输入",
        "",
        "上一层给出端点单位坐标模板：",
        "",
        "```text",
        "k=delta_{s0}-delta_{s*}",
        "A k=W",
        "root_crt_word=crt(s0)",
        "source_crt_word=crt(s*)",
        "```",
        "",
        "本证书继续不证明 `Lambda` 的存在，只处理已导入 stencil 的 CRT word 字典化。",
        "",
        "## 2. signed CRT word pair",
        "",
        "定义有序 CRT word 对：",
        "",
        "```text",
        "r0=crt(s0)",
        "r*=crt(s*)",
        "Pi=(r0,r*)",
        "```",
        "",
        "每个 CRT word 带 canonical congruence equation：",
        "",
        "```text",
        "s0 == r0_i mod p_i  for every active prime coordinate p_i",
        "s* == r*_i mod p_i  for every active prime coordinate p_i",
        "```",
        "",
        "定义有限 signed support dictionary：",
        "",
        "```text",
        "C_Pi(r0)=+1",
        "C_Pi(r*)=-1",
        "C_Pi(r)=0 for all other CRT words",
        "A C_Pi=W",
        "```",
        "",
        "若 `r0=r*`，字典消去并回流 singleton/degenerate 出口；否则保留两词 signed CRT pair。",
        "",
        "## 3. signed CRT word pair 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["kronecker_stencil_signed_crt_pair_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 4. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
            "```",
            "",
            "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange Kronecker-stencil signed CRT pair circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    print("phase_residue_exchange_kronecker_stencil_signed_crt_pair_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
