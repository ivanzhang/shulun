#!/usr/bin/env python3
"""生成 endpoint-alternating-cycle-pivot-phase-slip 证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.md
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
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.json"
)

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)

SOURCE_MULTIPLICITY = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
MONODROMY = "EndpointOrbitSignedDepthFluxAlternatingCycleMonodromyPDECCap"
PIVOT_SLIP = "EndpointOrbitSignedDepthFluxAlternatingCyclePivotPrimePhaseSlipPDECCap"

IMPORT = "StableLadderEndpointOrbitAlternatingCycleMonodromyImportedForPivotPhaseSlipLedger"
CRT_VECTOR = "StableLadderEndpointOrbitAlternatingCycleMonodromyCRTVectorLedger"
NONZERO_COORD = "StableLadderEndpointOrbitAlternatingCycleNonzeroCRTCoordinateLocalizationLedger"
PIVOT_PRIME = "StableLadderEndpointOrbitAlternatingCyclePivotPrimeSelectionLedger"
PHASE_SLIP = "StableLadderEndpointOrbitAlternatingCyclePivotPrimePhaseSlipLedger"
ZERO_ALL_RETURN = "StableLadderEndpointOrbitAlternatingCycleAllCoordinatesZeroReturnLedger"
NO_MONODROMY = "NoIndependentEndpointAlternatingCycleMonodromyAfterPivotPhaseSlipLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEndpointPivotPhaseSlipLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEndpointPivotPhaseSlipLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEndpointPivotPhaseSlipLedger"
MULTIPLICITY = "StableLadderEndpointOrbitSourceMultiplicityCapCarriedForwardAfterEndpointPivotPhaseSlipLedger"


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
    """把 monodromy 硬点替换为 pivot-prime phase-slip 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if MONODROMY in target:
        target = target.replace(MONODROMY, PIVOT_SLIP)
    elif PIVOT_SLIP not in target:
        target = f"{target}Or{PIVOT_SLIP}" if target else PIVOT_SLIP
    return target


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        CRT_VECTOR,
        NONZERO_COORD,
        PIVOT_PRIME,
        PHASE_SLIP,
        ZERO_ALL_RETURN,
        NO_MONODROMY,
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


def pivot_records() -> list[dict[str, str]]:
    """列出 pivot phase-slip 的坐标字段。"""
    return [
        {"field": "monodromy_vector", "meaning": "把 cycle monodromy 投影到有限 CRT prime-coordinate 向量。"},
        {"field": "zero_vector", "meaning": "所有素模坐标为 0 时回到 zero monodromy circulation return。"},
        {"field": "nonzero_coordinate", "meaning": "非零 monodromy 必有至少一个素模坐标非零。"},
        {"field": "pivot_prime", "meaning": "取最小非零坐标 prime 作为规范 pivot，消除匿名选择。"},
        {"field": "phase_slip_amount", "meaning": "pivot 坐标上的非零相位增量是最新显式硬点。"},
        {"field": "named_returns", "meaning": "若 pivot 选择退化，则回流 singleton、full mean 或 source multiplicity。"},
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 pivot phase-slip 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = MONODROMY in old_target and previous.get("endpoint_alternating_cycle_reduced_to_nonzero_monodromy") is True
    return [
        row("EndpointAlternatingCycleMonodromyImportedForPivotPhaseSlip", imported, False, "导入 nonzero alternating-cycle monodromy。", old_target),
        row("EndpointAlternatingCycleMonodromyCRTVector", imported, True, "monodromy 写成有限 CRT prime-coordinate 向量。", CRT_VECTOR),
        row("EndpointAlternatingCycleNonzeroCRTCoordinateLocalization", imported, True, "非零 CRT 向量必有非零素模坐标。", NONZERO_COORD),
        row("EndpointAlternatingCyclePivotPrimeSelection", imported, True, "选择最小非零素模坐标作为规范 pivot prime。", PIVOT_PRIME),
        row("EndpointAlternatingCyclePivotPrimePhaseSlip", False, False, "pivot prime 上的非零 phase slip 是最新硬点。", PIVOT_SLIP),
        row("EndpointAlternatingCycleAllCoordinatesZeroReturn", imported, True, "若所有坐标为 0，则并非 nonzero monodromy，回到零环流分支。", ZERO_ALL_RETURN),
        row("NoIndependentEndpointAlternatingCycleMonodromyAfterPivotPhaseSlip", imported, True, "monodromy 不再作为匿名整体出口。", NO_MONODROMY),
        row("SparseScaleLadderSAECarriedForwardAfterEndpointPivotPhaseSlip", True, False, "sparse SAE 继续前传。", SPARSE),
        row("EndpointPivotPhaseSlipStillOpen", False, False, "仍未排斥 sparse、endpoint singleton、full mean、source multiplicity 或 pivot phase slip。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    new_target = next_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, new_target)
    imported = any(item["gate"] == "EndpointAlternatingCycleMonodromyImportedForPivotPhaseSlip" and item["closed"] for item in rows)
    removed = any(item["gate"] == "NoIndependentEndpointAlternatingCycleMonodromyAfterPivotPhaseSlip" and item["closed"] for item in rows)
    plain = (
        "nonzero alternating-cycle monodromy 被投影到有限 CRT prime-coordinate 向量。"
        "若所有坐标为零，就回到 zero monodromy circulation；"
        "否则最小非零坐标给出规范 pivot prime phase-slip。"
        "本步只做坐标定位，不证明该 pivot slip 不存在。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_router",
        "status": "phase_residue_exchange_endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_alternating_cycle_monodromy_imported": imported,
        "endpoint_alternating_cycle_monodromy_crt_vector_closed": imported,
        "endpoint_alternating_cycle_nonzero_crt_coordinate_localized": imported,
        "endpoint_alternating_cycle_pivot_prime_selected": imported,
        "endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip": removed,
        "endpoint_alternating_cycle_pivot_prime_phase_slip_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "old_exits": [MONODROMY],
        "new_exits": [PIVOT_SLIP],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "pivot_records": pivot_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange endpoint-alternating-cycle-pivot-phase-slip 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_alternating_cycle_monodromy_imported={fmt_bool(cert['endpoint_alternating_cycle_monodromy_imported'])}",
        f"endpoint_alternating_cycle_monodromy_crt_vector_closed={fmt_bool(cert['endpoint_alternating_cycle_monodromy_crt_vector_closed'])}",
        f"endpoint_alternating_cycle_nonzero_crt_coordinate_localized={fmt_bool(cert['endpoint_alternating_cycle_nonzero_crt_coordinate_localized'])}",
        f"endpoint_alternating_cycle_pivot_prime_selected={fmt_bool(cert['endpoint_alternating_cycle_pivot_prime_selected'])}",
        f"endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip={fmt_bool(cert['endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip'])}",
        f"endpoint_alternating_cycle_pivot_prime_phase_slip_pdec_cap_proved={fmt_bool(cert['endpoint_alternating_cycle_pivot_prime_phase_slip_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. pivot 坐标",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["pivot_records"]:
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
            "- 本证书只把 nonzero monodromy 压成 pivot prime phase-slip 硬点。",
            "- 本证书没有证明 pivot slip、endpoint singleton、full-cycle mean、source multiplicity 或 sparse SAE。",
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
