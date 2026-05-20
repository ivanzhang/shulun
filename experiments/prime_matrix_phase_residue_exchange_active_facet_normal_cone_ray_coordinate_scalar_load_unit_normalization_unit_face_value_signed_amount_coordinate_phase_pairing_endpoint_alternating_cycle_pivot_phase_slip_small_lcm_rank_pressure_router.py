#!/usr/bin/env python3
"""生成 endpoint pivot small-LCM 分支的 rank-pressure 压缩证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_small_lcm_rank_pressure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.md
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
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.json"
)
FIRSTBREAK_SMALL_LCM_CERT = DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json"
LCM_DISCIPLINE_CERT = DOCS / "prime-matrix-strict-short-window-divisor-density-lcm-router.json"

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)

SOURCE_MULTIPLICITY = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
SMALL_LCM = "EndpointOrbitAlternatingCyclePivotPrimeSmallLCMColumnCRTPDECExclusion"
LOW_RESIDUE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierFixedResidueColumnCRTPDECExclusion"
LOW_SAE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "EndpointOrbitAlternatingCyclePivotPrimeHighCarrierRankDeficitOrSingletonSAE"
NONREPLAY_SAE = "EndpointOrbitAlternatingCyclePivotPrimeNonreplaySparseSAESummability"
MOVING_PIVOT = "EndpointOrbitAlternatingCycleMovingPivotPrimePhaseSlipPDECExclusion"
REDUCED_SMALL_LCM = f"{LOW_RESIDUE} AND {LOW_SAE} AND {HIGH_RANK}"

IMPORT = "StableLadderEndpointOrbitPivotPrimeSmallLCMImportedForRankPressureLedger"
WIDTH_GUARD = "StableLadderEndpointOrbitPivotPrimePositiveReplayWidthGuardLedger"
PRODUCT_LAW = "StableLadderEndpointOrbitPivotPrimeDistinctPrimeProductLawLedger"
RANK_PRESSURE = "StableLadderEndpointOrbitPivotPrimeSmallLCMRankPressureLedger"
SQRT_BARRIER = "StableLadderEndpointOrbitPivotPrimeTwoLargeCarrierSqrtBarrierLedger"
LCM_DISCIPLINE = "StableLadderEndpointOrbitPivotPrimeShortWindowLCMDisciplineImportedLedger"
LOW_RESIDUE_LEDGER = "StableLadderEndpointOrbitPivotPrimeLowCarrierFixedResidueRouteLedger"
LOW_SAE_LEDGER = "StableLadderEndpointOrbitPivotPrimeLowCarrierNonpersistentSparseRouteLedger"
HIGH_RANK_LEDGER = "StableLadderEndpointOrbitPivotPrimeHighCarrierRankDeficitRouteLedger"
NO_SMALL_LCM = "NoIndependentEndpointPivotPrimeSmallLCMAfterRankPressureLedger"


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
    """登记本脚本与上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, FIRSTBREAK_SMALL_LCM_CERT, LCM_DISCIPLINE_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 small-LCM 硬点替换为 rank-pressure 三出口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_SMALL_LCM})"
    if SMALL_LCM in target:
        return target.replace(SMALL_LCM, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        WIDTH_GUARD,
        PRODUCT_LAW,
        RANK_PRESSURE,
        SQRT_BARRIER,
        LCM_DISCIPLINE,
        LOW_RESIDUE_LEDGER,
        LOW_SAE_LEDGER,
        HIGH_RANK_LEDGER,
        NO_SMALL_LCM,
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


def rank_records() -> list[dict[str, str]]:
    """列出 rank-pressure 字段。"""
    return [
        {"field": "support_width", "meaning": "上一层 LCM-support 屏障给出的有限宽度 W。"},
        {"field": "small_lcm_condition", "meaning": "固定 pivot 标签集满足 L=lcm(Lambda)<=W。"},
        {"field": "threshold_B", "meaning": "任意分割阈值 B，用来区分低 carrier 与高 carrier。"},
        {"field": "high_rank_bound", "meaning": "q>B 的互异高 carrier 数至多 floor(log W/log B)。"},
        {"field": "sqrt_barrier", "meaning": "取 B=sqrt(W)，两个 q>sqrt(W) 不能同处一个 fixed small-LCM unit。"},
        {"field": "low_carrier_reuse", "meaning": "压力若由 q<=B 承担，必须表现为低 carrier 固定 residue 复用或非持久 sparse。"},
    ]


def build_rows(
    previous: dict[str, Any],
    firstbreak_small_lcm: dict[str, Any],
    lcm_discipline: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 rank-pressure 判定表。"""
    imported = SMALL_LCM in previous.get("hardpoint_after_router", "") or SMALL_LCM in previous.get("next_direct_attack_target", "")
    template_imported = firstbreak_small_lcm.get("small_lcm_rank_pressure_closed") is True
    discipline_imported = lcm_discipline.get("status") == (
        "short_window_divisor_density_reduced_to_lcm_multiplier_or_common_kernel_defect_open"
    )
    return [
        row("EndpointPivotSmallLCMImportedForRankPressure", imported, False, "导入上一层 small-LCM pivot 分支。", SMALL_LCM),
        row("PositiveReplayWidthGuardClosed", imported, True, "small-LCM fixed replay 只在 W>=1 的有限支撑宽度内有非零复现步长。", WIDTH_GUARD),
        row("DistinctPivotPrimeProductLawClosed", imported, True, "互异 pivot prime 标签集满足 L=lcm(Lambda)=prod_{q in Lambda} q；重复同 prime 不增加 L，进入 fixed-residue 复用。", PRODUCT_LAW),
        row("EndpointPivotSmallLCMRankPressureClosed", imported and template_imported, True, "由 L<=W 得到任意阈值 B 下 q>B 的 carrier 数至多 floor(log W/log B)。", RANK_PRESSURE),
        row("TwoLargePivotCarrierSqrtBarrierClosed", imported and template_imported, True, "取 B=sqrt(W)，两个 q>sqrt(W) 的 pivot carrier 不可能同处一个 fixed small-LCM unit。", HIGH_RANK),
        row("ShortWindowLCMDisciplineImported", discipline_imported, True, "已有短窗口 LCM 乘子纪律用于登记低乘子/固定 residue 回流。", LCM_DISCIPLINE),
        row("LowCarrierFixedResidueRouteRegistered", imported, False, "若压力由低 carrier q<=B 承担，则必须出现固定 residue 复用，进入 ColumnCRT/PDEC。", LOW_RESIDUE),
        row("LowCarrierNonpersistentSparseRouteRegistered", imported, False, "若低 carrier 不形成持久固定 residue，则只能作为非持久 sparse SAE 计费。", LOW_SAE),
        row("HighCarrierRankDeficitRouteRegistered", imported, False, "排除低 carrier 后，高 carrier rank 受限；若仍要承担压力，必须给出低秩容量缺口或 singleton SAE。", HIGH_RANK),
        row("NoIndependentEndpointPivotSmallLCMAfterRankPressure", imported, True, "small-LCM pivot 不再作为匿名宽口径出口保留。", NO_SMALL_LCM),
        row("EndpointPivotSmallLCMRankPressureStillOpen", False, False, "尚未排斥低 carrier 固定 residue、低 carrier sparse、高 carrier rank deficit、nonreplay、moving pivot 或并行 endpoint 出口。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    firstbreak_small_lcm = load_json(FIRSTBREAK_SMALL_LCM_CERT)
    lcm_discipline = load_json(LCM_DISCIPLINE_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, firstbreak_small_lcm, lcm_discipline, new_target)
    imported = any(item["gate"] == "EndpointPivotSmallLCMImportedForRankPressure" and item["closed"] for item in rows)
    removed = any(item["gate"] == "NoIndependentEndpointPivotSmallLCMAfterRankPressure" and item["closed"] for item in rows)
    plain = (
        "endpoint pivot small-LCM 分支已被压成 rank-pressure 三分："
        "固定 pivot 标签集满足 L=lcm(Lambda)<=W，因此任意阈值 B 以上的互异高 carrier 数"
        "至多为 floor(log W/log B)，特别是两个 q>sqrt(W) 的 pivot carrier 不能同处一个"
        " fixed small-LCM unit。剩余压力必须进入低 carrier 固定 residue、低 carrier 非持久 sparse，"
        "或高 carrier 低秩容量缺口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_phase_slip_small_lcm_rank_pressure_router",
        "status": "endpoint_pivot_small_lcm_reduced_to_rank_pressure_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "firstbreak_small_lcm_template_certificate": str(FIRSTBREAK_SMALL_LCM_CERT.relative_to(ROOT)),
        "lcm_discipline_certificate": str(LCM_DISCIPLINE_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_pivot_small_lcm_imported": imported,
        "endpoint_pivot_distinct_prime_product_law_closed": imported,
        "endpoint_pivot_small_lcm_rank_pressure_closed": imported,
        "endpoint_pivot_two_large_carrier_sqrt_barrier_closed": imported,
        "endpoint_pivot_small_lcm_reduced_to_rank_pressure": removed,
        "endpoint_pivot_low_carrier_fixed_residue_pdec_proved": False,
        "endpoint_pivot_low_carrier_nonpersistent_sparse_sae_proved": False,
        "endpoint_pivot_high_carrier_rank_deficit_proved": False,
        "endpoint_pivot_nonreplay_sparse_sae_proved": False,
        "endpoint_pivot_moving_prime_phase_slip_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SMALL_LCM,
        "hardpoint_after_router": REDUCED_SMALL_LCM,
        "old_exits": [SMALL_LCM],
        "new_exits": [LOW_RESIDUE, LOW_SAE, HIGH_RANK],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "rank_records": rank_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot small-LCM rank-pressure 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_pivot_small_lcm_imported={fmt_bool(cert['endpoint_pivot_small_lcm_imported'])}",
        f"endpoint_pivot_distinct_prime_product_law_closed={fmt_bool(cert['endpoint_pivot_distinct_prime_product_law_closed'])}",
        f"endpoint_pivot_small_lcm_rank_pressure_closed={fmt_bool(cert['endpoint_pivot_small_lcm_rank_pressure_closed'])}",
        f"endpoint_pivot_two_large_carrier_sqrt_barrier_closed={fmt_bool(cert['endpoint_pivot_two_large_carrier_sqrt_barrier_closed'])}",
        f"endpoint_pivot_small_lcm_reduced_to_rank_pressure={fmt_bool(cert['endpoint_pivot_small_lcm_reduced_to_rank_pressure'])}",
        f"endpoint_pivot_low_carrier_fixed_residue_pdec_proved={fmt_bool(cert['endpoint_pivot_low_carrier_fixed_residue_pdec_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. rank-pressure",
        "",
        "在上一层的 small-LCM 分支中，固定 pivot 标签集满足",
        "",
        "```text",
        "L = lcm(Lambda) <= W.",
        "```",
        "",
        "若只计互异 pivot primes，则 `L=prod_{q in Lambda} q`；重复同一 prime 不增加 L，必须登记为 fixed-residue 复用。任取阈值 `B>1`，所有 `q>B` 的互异高 carrier 个数 `r_B` 满足",
        "",
        "```text",
        "B^{r_B} <= prod_{q>B} q <= L <= W,",
        "r_B <= floor(log W / log B).",
        "```",
        "",
        "特别取 `B=sqrt(W)`，两个 `q>sqrt(W)` 不能同处一个 fixed small-LCM unit。",
        "",
        "## 2. 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["rank_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 三分出口",
            "",
            "```text",
            cert["hardpoint_before_router"],
            f"  -> {LOW_RESIDUE}",
            f"  AND {LOW_SAE}",
            f"  AND {HIGH_RANK}",
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
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
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
            "- 本证书不证明 endpoint pivot small-LCM 分支不存在。",
            "- 本证书只证明 small-LCM 强制 carrier rank 受限，并登记低 carrier fixed-residue、低 carrier sparse 与高 carrier rank-deficit 三出口。",
            "- nonreplay sparse、moving-pivot、endpoint singleton/full-cycle mean/source multiplicity 与 sparse SAE 仍未排斥。",
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
