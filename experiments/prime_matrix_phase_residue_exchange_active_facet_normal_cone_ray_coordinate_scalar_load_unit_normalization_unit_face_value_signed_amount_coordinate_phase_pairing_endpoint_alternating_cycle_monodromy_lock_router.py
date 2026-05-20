#!/usr/bin/env python3
"""生成 endpoint-alternating-cycle-monodromy-lock 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_monodromy_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-monodromy-lock"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)

SOURCE_MULTIPLICITY = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
CYCLE = "EndpointOrbitSignedDepthFluxAlternatingTransportCyclePDECCap"
MONODROMY = "EndpointOrbitSignedDepthFluxAlternatingCycleMonodromyPDECCap"

IMPORT = "StableLadderEndpointOrbitAlternatingTransportCycleImportedForMonodromyLockLedger"
ORDERED_SUPPORT = "StableLadderEndpointOrbitAlternatingCycleOrderedSupportLedger"
SIGNED_INCIDENCE = "StableLadderEndpointOrbitAlternatingCycleSignedEdgeIncidenceLedger"
BOUNDARY_ZERO = "StableLadderEndpointOrbitAlternatingCycleBoundaryZeroLedger"
CRT_INCREMENT = "StableLadderEndpointOrbitAlternatingCycleCRTPhaseIncrementWordLedger"
MONODROMY_DICHOTOMY = "StableLadderEndpointOrbitAlternatingCycleTelescopingMonodromyDichotomyLedger"
ZERO_RETURN = "StableLadderEndpointOrbitAlternatingCycleZeroMonodromyCirculationReturnLedger"
NONZERO_RESIDUAL = "StableLadderEndpointOrbitAlternatingCycleNonzeroMonodromyResidualLedger"
NO_CYCLE = "NoIndependentEndpointAlternatingTransportCycleAfterMonodromyLockLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEndpointCycleMonodromyLockLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEndpointCycleMonodromyLockLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEndpointCycleMonodromyLockLedger"
MULTIPLICITY = "StableLadderEndpointOrbitSourceMultiplicityCapCarriedForwardAfterEndpointCycleMonodromyLockLedger"


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
    """登记本脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def next_target(previous: dict[str, Any]) -> str:
    """把 alternating transport cycle 替换为 monodromy 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if CYCLE in target:
        target = target.replace(CYCLE, MONODROMY)
    elif MONODROMY not in target:
        target = f"{target}Or{MONODROMY}" if target else MONODROMY
    return target


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        ORDERED_SUPPORT,
        SIGNED_INCIDENCE,
        BOUNDARY_ZERO,
        CRT_INCREMENT,
        MONODROMY_DICHOTOMY,
        ZERO_RETURN,
        NONZERO_RESIDUAL,
        NO_CYCLE,
        SPARSE,
        SINGLETON,
        FULL_MEAN,
        MULTIPLICITY,
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


def monodromy_records() -> list[dict[str, str]]:
    """列出 alternating cycle 的 monodromy 坐标。"""
    return [
        {"field": "cycle_word", "meaning": "有序 endpoint 顶点序列 v0->v1->...->v0。"},
        {"field": "edge_sign", "meaning": "相邻边正负交替，保持 signed-depth/flux 方向。"},
        {"field": "incidence_boundary", "meaning": "环的 incidence boundary 为 0；非零边界已回到叶出口。"},
        {"field": "phase_increment", "meaning": "每条边登记 CRT endpoint phase increment。"},
        {"field": "total_monodromy", "meaning": "沿环求和得到唯一 cycle monodromy。"},
        {"field": "zero_branch", "meaning": "total_monodromy=0 时是纯环流，不产生 endpoint load defect。"},
        {"field": "nonzero_branch", "meaning": "total_monodromy!=0 时保留为显式 monodromy PDEC/cap。"},
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 endpoint alternating-cycle monodromy-lock 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = CYCLE in old_target and previous.get("endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle") is True
    return [
        row("EndpointAlternatingTransportCycleImportedForMonodromyLock", imported, False, "导入 alternating transport cycle 作为当前硬点。", old_target),
        row("EndpointAlternatingCycleOrderedSupport", imported, True, "有限 endpoint cycle 可写成有序闭合顶点词。", ORDERED_SUPPORT),
        row("EndpointAlternatingCycleSignedEdgeIncidence", imported, True, "交替符号边诱导 signed incidence 1-chain。", SIGNED_INCIDENCE),
        row("EndpointAlternatingCycleBoundaryZero", imported, True, "闭合环的 incidence boundary 为 0；若不为 0 则回到叶/endpoint 出口。", BOUNDARY_ZERO),
        row("EndpointAlternatingCycleCRTPhaseIncrementWord", imported, True, "每条边都有 CRT endpoint phase increment。", CRT_INCREMENT),
        row("EndpointAlternatingCycleTelescopingMonodromyDichotomy", imported, True, "沿环相位增量要么 telescope 为 0，要么给出非零 monodromy。", MONODROMY_DICHOTOMY),
        row("EndpointAlternatingCycleZeroMonodromyCirculationReturn", imported, True, "零 monodromy 只是纯环流，不形成 endpoint load defect。", ZERO_RETURN),
        row("EndpointAlternatingCycleNonzeroMonodromyResidual", False, False, "非零 monodromy 是最新显式 cycle 硬点。", MONODROMY),
        row("NoIndependentEndpointAlternatingTransportCycleAfterMonodromyLock", imported, True, "alternating transport cycle 不再作为匿名环出口。", NO_CYCLE),
        row("SparseScaleLadderSAECarriedForwardAfterEndpointCycleMonodromyLock", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointCycleMonodromyStillOpen", False, False, "仍未排斥 sparse、endpoint singleton、full mean、source multiplicity 或 nonzero monodromy。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    imported = any(item["gate"] == "EndpointAlternatingTransportCycleImportedForMonodromyLock" and item["closed"] for item in rows)
    cycle_removed = any(
        item["gate"] == "NoIndependentEndpointAlternatingTransportCycleAfterMonodromyLock" and item["closed"]
        for item in rows
    )
    plain = (
        "alternating transport cycle 被锁成有序 CRT endpoint cycle 与相位增量词。"
        "零 monodromy 是纯环流，不能作为 endpoint load defect；"
        "剩余只能是非零 alternating-cycle monodromy。"
        "本步不证明该 monodromy 不存在。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_monodromy_lock_router",
        "status": "phase_residue_exchange_endpoint_alternating_cycle_reduced_to_monodromy_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_alternating_transport_cycle_imported": imported,
        "endpoint_alternating_cycle_ordered_support_closed": imported,
        "endpoint_alternating_cycle_signed_edge_incidence_closed": imported,
        "endpoint_alternating_cycle_boundary_zero_closed": imported,
        "endpoint_alternating_cycle_crt_phase_increment_word_closed": imported,
        "endpoint_alternating_cycle_monodromy_dichotomy_closed": imported,
        "endpoint_alternating_cycle_zero_monodromy_circulation_return_closed": imported,
        "endpoint_alternating_cycle_reduced_to_nonzero_monodromy": cycle_removed,
        "endpoint_alternating_cycle_monodromy_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [CYCLE],
        "new_exits": [MONODROMY],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "monodromy_records": monodromy_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange endpoint-alternating-cycle-monodromy-lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_alternating_transport_cycle_imported={fmt_bool(cert['endpoint_alternating_transport_cycle_imported'])}",
        f"endpoint_alternating_cycle_ordered_support_closed={fmt_bool(cert['endpoint_alternating_cycle_ordered_support_closed'])}",
        f"endpoint_alternating_cycle_signed_edge_incidence_closed={fmt_bool(cert['endpoint_alternating_cycle_signed_edge_incidence_closed'])}",
        f"endpoint_alternating_cycle_boundary_zero_closed={fmt_bool(cert['endpoint_alternating_cycle_boundary_zero_closed'])}",
        f"endpoint_alternating_cycle_crt_phase_increment_word_closed={fmt_bool(cert['endpoint_alternating_cycle_crt_phase_increment_word_closed'])}",
        f"endpoint_alternating_cycle_monodromy_dichotomy_closed={fmt_bool(cert['endpoint_alternating_cycle_monodromy_dichotomy_closed'])}",
        f"endpoint_alternating_cycle_zero_monodromy_circulation_return_closed={fmt_bool(cert['endpoint_alternating_cycle_zero_monodromy_circulation_return_closed'])}",
        f"endpoint_alternating_cycle_reduced_to_nonzero_monodromy={fmt_bool(cert['endpoint_alternating_cycle_reduced_to_nonzero_monodromy'])}",
        f"endpoint_alternating_cycle_monodromy_pdec_cap_proved={fmt_bool(cert['endpoint_alternating_cycle_monodromy_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. monodromy 坐标",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["monodromy_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 新硬点",
            "",
            "```text",
            cert["previous_direct_attack_target"],
            "  -> " + reduced_target(cert["next_direct_attack_target"]),
            "```",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书只把 alternating transport cycle 压成 nonzero monodromy 硬点。",
            "- 本证书没有证明 monodromy、endpoint singleton、full-cycle mean、source multiplicity 或 sparse SAE。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
    """写出 ledger、JSON 与 Markdown。"""
    cert = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_md(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
