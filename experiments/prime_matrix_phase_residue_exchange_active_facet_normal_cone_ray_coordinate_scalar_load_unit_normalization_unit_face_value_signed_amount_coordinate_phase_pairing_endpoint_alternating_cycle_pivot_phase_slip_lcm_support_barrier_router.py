#!/usr/bin/env python3
"""生成 endpoint pivot phase-slip 的 LCM-支撑宽度屏障证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_lcm_support_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.md
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
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.json"
)
FIRSTBREAK_LCM_CERT = DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json"

PREFIX = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitness"
    "CRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacet"
    "NormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinate"
    "PhasePairing"
)

SOURCE_MULTIPLICITY = f"{PREFIX}SourceAtomMultiplicityCapPDECCap"
PIVOT_SLIP = "EndpointOrbitSignedDepthFluxAlternatingCyclePivotPrimePhaseSlipPDECCap"
SMALL_LCM = "EndpointOrbitAlternatingCyclePivotPrimeSmallLCMColumnCRTPDECExclusion"
NONREPLAY_SAE = "EndpointOrbitAlternatingCyclePivotPrimeNonreplaySparseSAESummability"
MOVING_PIVOT = "EndpointOrbitAlternatingCycleMovingPivotPrimePhaseSlipPDECExclusion"
REDUCED_PIVOT = f"{SMALL_LCM} AND {NONREPLAY_SAE} AND {MOVING_PIVOT}"

IMPORT = "StableLadderEndpointOrbitAlternatingCyclePivotPhaseSlipImportedForLCMSupportBarrierLedger"
PHASE_MOTION = "StableLadderEndpointOrbitPivotPrimePhaseMotionFormulaLedger"
LCM_PERIOD = "StableLadderEndpointOrbitPivotPrimeFixedReplayLCMPeriodLedger"
SUPPORT_WIDTH = "StableLadderEndpointOrbitPivotPrimeSupportWidthLedger"
NO_REPLAY = "StableLadderEndpointOrbitPivotPrimeLCMExceedsSupportNoReplayLedger"
SMALL_LCM_LEDGER = "StableLadderEndpointOrbitPivotPrimeSmallLCMBranchLedger"
MOVING_LEDGER = "StableLadderEndpointOrbitPivotPrimeMovingLabelReturnLedger"
NO_PIVOT_EXIT = "NoIndependentEndpointPivotPrimePhaseSlipAfterLCMSupportBarrierLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEndpointPivotLCMSupportBarrierLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterEndpointPivotLCMSupportBarrierLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEndpointPivotLCMSupportBarrierLedger"
MULTIPLICITY = "StableLadderEndpointOrbitSourceMultiplicityCapCarriedForwardAfterEndpointPivotLCMSupportBarrierLedger"


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
    paths = [Path(__file__).resolve(), PREVIOUS_CERT, FIRSTBREAK_LCM_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 pivot phase-slip 硬点替换为 LCM-support 三出口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_PIVOT})"
    if PIVOT_SLIP in target:
        return target.replace(PIVOT_SLIP, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        PHASE_MOTION,
        LCM_PERIOD,
        SUPPORT_WIDTH,
        NO_REPLAY,
        SMALL_LCM_LEDGER,
        MOVING_LEDGER,
        NO_PIVOT_EXIT,
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


def support_records() -> list[dict[str, str]]:
    """列出 LCM-支撑屏障的坐标字段。"""
    return [
        {"field": "pivot_prime", "meaning": "上一层选择的最小非零 CRT prime-coordinate。"},
        {"field": "phase_slip_amount", "meaning": "该素模坐标上的非零相位滑移 sigma mod q。"},
        {"field": "fixed_replay_step", "meaning": "同一 pivot 标签复现时的 formal endpoint replay 位移 d。"},
        {"field": "prime_period", "meaning": "d*sigma == 0 mod q 且 sigma !=0，因此 q|d。"},
        {"field": "pivot_lcm", "meaning": "固定 pivot 标签集 Lambda 的复现步长必须被 lcm(Lambda) 整除。"},
        {"field": "endpoint_support_width", "meaning": "交替 endpoint cycle 内可承载固定复现的有限支撑宽度 W。"},
    ]


def build_rows(previous: dict[str, Any], firstbreak_lcm: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 LCM-support 判定表。"""
    imported = (
        PIVOT_SLIP in previous.get("next_direct_attack_target", "")
        and previous.get("endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip") is True
    )
    lcm_template_imported = firstbreak_lcm.get("fixed_carrier_lcm_replay_period_closed") is True
    return [
        row("EndpointPivotPhaseSlipImportedForLCMSupportBarrier", imported, False, "导入上一层的 pivot-prime 非零 phase-slip。", PIVOT_SLIP),
        row("PivotPrimePhaseMotionFormulaClosed", imported, True, "固定 pivot prime q 上的复现闭合要求 d*sigma==0 mod q；sigma 非零且 q 为素数，故 q|d。", PHASE_MOTION),
        row("FixedPivotSetLCMReplayPeriodClosed", imported and lcm_template_imported, True, "对固定 pivot 标签集 Lambda，精确同标签复现步长必须被 L=lcm(Lambda) 整除。", LCM_PERIOD),
        row("EndpointSupportWidthRegistered", imported, True, "endpoint alternating cycle 是有限支撑对象，固定复现只能落在其支撑宽度 W 内。", SUPPORT_WIDTH),
        row("LCMExceedsEndpointSupportNoFixedReplay", imported, True, "若 L>W，则 1<=d<=W 内没有非零固定 pivot-set 复现。", NONREPLAY_SAE),
        row("EndpointPivotSmallLCMBranchStructured", imported, False, "若 L<=W，则该 pivot-slip 压入小 LCM/固定 residue/ColumnCRT/PDEC 分支。", SMALL_LCM),
        row("MovingPivotPrimeIsNamedReturn", imported, False, "若通过更换 pivot prime 逃避固定 LCM 屏障，则它不是固定复现，而是 moving-pivot PDEC/SAE。", MOVING_PIVOT),
        row("NoIndependentEndpointPivotPhaseSlipAfterLCMSupportBarrier", imported, True, "pivot phase-slip 不再作为匿名单出口保留。", NO_PIVOT_EXIT),
        row("EndpointPivotLCMSupportBarrierStillOpen", False, False, "尚未排斥小 LCM、nonreplay sparse SAE、moving pivot、endpoint singleton/full mean/source multiplicity 或 sparse SAE。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    firstbreak_lcm = load_json(FIRSTBREAK_LCM_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, firstbreak_lcm, new_target)
    imported = any(item["gate"] == "EndpointPivotPhaseSlipImportedForLCMSupportBarrier" and item["closed"] for item in rows)
    removed = any(item["gate"] == "NoIndependentEndpointPivotPhaseSlipAfterLCMSupportBarrier" and item["closed"] for item in rows)
    plain = (
        "pivot-prime phase-slip 已被压成 LCM-支撑宽度屏障："
        "固定非零素模滑移若以同一 pivot 标签复现，其 replay 位移 d 必须被该素数整除；"
        "固定 pivot 标签集则要求 lcm(Lambda)|d。"
        "若该 LCM 超过 endpoint cycle 的有限支撑宽度 W，就没有非零固定复现；"
        "否则只剩小 LCM/ColumnCRT/PDEC 分支，逃避固定标签的情形登记为 moving-pivot PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_phase_slip_lcm_support_barrier_router",
        "status": "endpoint_pivot_phase_slip_reduced_to_lcm_support_barrier_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "firstbreak_lcm_template_certificate": str(FIRSTBREAK_LCM_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_pivot_phase_slip_imported": imported,
        "endpoint_pivot_prime_phase_motion_formula_closed": imported,
        "endpoint_pivot_fixed_set_lcm_replay_period_closed": imported,
        "endpoint_pivot_support_width_registered": imported,
        "endpoint_pivot_lcm_exceeds_support_no_fixed_replay": imported,
        "endpoint_pivot_phase_slip_reduced_to_lcm_support_barrier": removed,
        "endpoint_pivot_small_lcm_branch_excluded": False,
        "endpoint_pivot_nonreplay_sparse_sae_proved": False,
        "endpoint_pivot_moving_prime_phase_slip_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PIVOT_SLIP,
        "hardpoint_after_router": REDUCED_PIVOT,
        "old_exits": [PIVOT_SLIP],
        "new_exits": [SMALL_LCM, NONREPLAY_SAE, MOVING_PIVOT],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "support_records": support_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot phase-slip LCM-support 屏障证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_pivot_phase_slip_imported={fmt_bool(cert['endpoint_pivot_phase_slip_imported'])}",
        f"endpoint_pivot_prime_phase_motion_formula_closed={fmt_bool(cert['endpoint_pivot_prime_phase_motion_formula_closed'])}",
        f"endpoint_pivot_fixed_set_lcm_replay_period_closed={fmt_bool(cert['endpoint_pivot_fixed_set_lcm_replay_period_closed'])}",
        f"endpoint_pivot_support_width_registered={fmt_bool(cert['endpoint_pivot_support_width_registered'])}",
        f"endpoint_pivot_lcm_exceeds_support_no_fixed_replay={fmt_bool(cert['endpoint_pivot_lcm_exceeds_support_no_fixed_replay'])}",
        f"endpoint_pivot_phase_slip_reduced_to_lcm_support_barrier={fmt_bool(cert['endpoint_pivot_phase_slip_reduced_to_lcm_support_barrier'])}",
        f"endpoint_pivot_small_lcm_branch_excluded={fmt_bool(cert['endpoint_pivot_small_lcm_branch_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 支撑屏障",
        "",
        "设上一层给出 pivot prime `q` 与非零 phase-slip `sigma mod q`。若同一 pivot 标签在 formal endpoint orbit 中以位移 `d` 精确复现，则必须有",
        "",
        "```text",
        "d*sigma == 0 mod q.",
        "```",
        "",
        "因为 `q` 为素数且 `sigma != 0 mod q`，得到",
        "",
        "```text",
        "q | d.",
        "```",
        "",
        "对固定 pivot 标签集 `Lambda`，同标签复现步长必须满足",
        "",
        "```text",
        "lcm(Lambda) | d.",
        "```",
        "",
        "endpoint alternating cycle 是有限支撑对象。记其可承载固定复现的支撑宽度为 `W`。若 `lcm(Lambda)>W`，则 `1<=d<=W` 内没有非零固定复现；若 `lcm(Lambda)<=W`，该分支只能作为小 LCM/固定 residue/ColumnCRT/PDEC 处理。",
        "",
        "## 2. 坐标字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["support_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 三分出口",
            "",
            "```text",
            cert["hardpoint_before_router"],
            f"  -> {SMALL_LCM}",
            f"  AND {NONREPLAY_SAE}",
            f"  AND {MOVING_PIVOT}",
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
            "- 本证书不证明 pivot phase-slip 不存在。",
            "- 本证书只把固定 pivot phase-slip 压成 LCM-support 屏障，并登记小 LCM、nonreplay sparse SAE 与 moving-pivot 三出口。",
            "- endpoint singleton、full-cycle mean、source multiplicity 与 sparse SAE 仍未排斥。",
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
