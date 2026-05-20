#!/usr/bin/env python3
"""生成 endpoint pivot 低 carrier fixed-residue 的 AP-envelope 路由证书。

用法示例：
  python3 experiments/prime_matrix_endpoint_pivot_low_carrier_fixed_residue_ap_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.json

输出：
  data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.md
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
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-"
    "fixed-residue-ap-table"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = (
    DOCS
    / "prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-"
    "scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-"
    "phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-"
    "rank-pressure-router.json"
)
FIRSTBREAK_RESIDUE_AP_CERT = DOCS / "prime-matrix-firstbreak-low-carrier-residue-ap-router.json"
FIRSTBREAK_AP_ENVELOPE_CERT = DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json"
LOW_EFFECTIVE_MOD_CERT = DOCS / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json"
PHASE_SCHEMA_CERT = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"

SOURCE_MULTIPLICITY = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiber"
    "PhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
LOW_RESIDUE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierFixedResidueColumnCRTPDECExclusion"
ENDPOINT_DEMAND = "EndpointOrbitAlternatingCyclePivotPrimeActualLowCarrierRowIncidenceDemandLowerBound"
ENDPOINT_STRICT_GAP = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierAPEnvelopeStrictGapOrDenseTablePDEC"
DENSE_TABLE = "EndpointOrbitAlternatingCyclePivotPrimeDenseLowCarrierResidueTablePDECExclusion"
SPARSE_CELL = "EndpointOrbitAlternatingCyclePivotPrimeSparseLowCarrierResidueCellSAESummability"
LOW_SAE = "EndpointOrbitAlternatingCyclePivotPrimeLowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "EndpointOrbitAlternatingCyclePivotPrimeHighCarrierRankDeficitOrSingletonSAE"
NONREPLAY_SAE = "EndpointOrbitAlternatingCyclePivotPrimeNonreplaySparseSAESummability"
MOVING_PIVOT = "EndpointOrbitAlternatingCycleMovingPivotPrimePhaseSlipPDECExclusion"

REDUCED_LOW_RESIDUE = (
    f"{ENDPOINT_DEMAND} AND {ENDPOINT_STRICT_GAP} "
    f"AND {DENSE_TABLE} AND {SPARSE_CELL}"
)

IMPORT = "StableLadderEndpointOrbitPivotPrimeLowCarrierFixedResidueImportedForAPEnvelopeLedger"
BOUNDARY = "StableLadderEndpointOrbitPivotPrimeBoundaryCarrierDegeneratesToColumnCRTOrEndpointSingletonLedger"
AP_FORMULA = "StableLadderEndpointOrbitPivotPrimeLowCarrierResidueToRowAPFormulaLedger"
SINGLE_CELL = "StableLadderEndpointOrbitPivotPrimeLowCarrierSingleResidueSharpEnvelopeLedger"
ALL_RESIDUES = "StableLadderEndpointOrbitPivotPrimeLowCarrierAllResiduesExactMassLedger"
TABLE_ENV = "StableLadderEndpointOrbitPivotPrimeLowCarrierSelectedTableExactEnvelopeLedger"
FINITE_TABLE = "StableLadderEndpointOrbitPivotPrimeLowCarrierResidueTableFiniteLedger"
LOWMOD_IMPORT = "StableLadderEndpointOrbitPivotPrimeLowEffectiveModColumnCRTImportedLedger"
DENSE_ROUTE = "StableLadderEndpointOrbitPivotPrimeDenseLowCarrierResidueTableRouteLedger"
SPARSE_ROUTE = "StableLadderEndpointOrbitPivotPrimeSparseLowCarrierResidueCellRouteLedger"
DEMAND_GUARD = "StableLadderEndpointOrbitPivotPrimeActualDemandLowerBoundStillOpenLedger"
NO_LOW_RESIDUE = "NoIndependentEndpointPivotPrimeLowCarrierFixedResidueAfterAPEnvelopeLedger"


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
    paths = [
        Path(__file__).resolve(),
        PREVIOUS_CERT,
        FIRSTBREAK_RESIDUE_AP_CERT,
        FIRSTBREAK_AP_ENVELOPE_CERT,
        LOW_EFFECTIVE_MOD_CERT,
        PHASE_SCHEMA_CERT,
    ]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_target(previous: dict[str, Any]) -> str:
    """把 endpoint low-carrier fixed-residue 硬点替换为 AP-envelope 接口。"""
    target = previous.get("next_direct_attack_target", "")
    grouped = f"({REDUCED_LOW_RESIDUE})"
    if LOW_RESIDUE in target:
        return target.replace(LOW_RESIDUE, grouped)
    return f"{target} AND {grouped}" if target else grouped


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        BOUNDARY,
        AP_FORMULA,
        SINGLE_CELL,
        ALL_RESIDUES,
        TABLE_ENV,
        FINITE_TABLE,
        LOWMOD_IMPORT,
        DENSE_ROUTE,
        SPARSE_ROUTE,
        DEMAND_GUARD,
        NO_LOW_RESIDUE,
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


def ap_records() -> list[dict[str, str]]:
    """列出 endpoint AP-envelope 字段。"""
    return [
        {"field": "endpoint_row_coordinate", "meaning": "endpoint orbit 内规范化后的行/相位坐标 t。"},
        {"field": "pivot_prime_q", "meaning": "低 carrier pivot prime；AP 公式只在 q<P 时使用。"},
        {"field": "fixed_residue_a", "meaning": "固定列/相位 residue a mod q。"},
        {"field": "row_ap_class", "meaning": "t == -a P^{-1} mod q 的唯一行同余类。"},
        {"field": "interval_height_H", "meaning": "当前 endpoint 支撑窗口的有效行长度。"},
        {"field": "cell_envelope", "meaning": "单 cell 至多命中 ceil(H/q) 个 endpoint 行位置。"},
        {"field": "all_residue_mass", "meaning": "固定 q 时所有 residue cell 精确分割窗口，总量为 H。"},
    ]


def build_rows(
    previous: dict[str, Any],
    residue_ap: dict[str, Any],
    ap_envelope: dict[str, Any],
    lowmod: dict[str, Any],
    phase_schema: dict[str, Any],
    new_target: str,
) -> list[dict[str, Any]]:
    """构造 endpoint AP-envelope 判定表。"""
    imported = LOW_RESIDUE in previous.get("next_direct_attack_target", "")
    firstbreak_formula = (
        residue_ap.get("residue_to_row_ap_formula_closed") is True
        and residue_ap.get("single_residue_ap_envelope_closed") is True
    )
    exact_envelope = (
        ap_envelope.get("all_residues_exact_mass_closed") is True
        and ap_envelope.get("selected_table_envelope_closed") is True
    )
    lowmod_imported = lowmod.get("pdec_columncrt_route_registered") is True
    phase_schema_imported = phase_schema.get("early_zero_phase_defect_schema_admission_closed") is True
    return [
        row("EndpointPivotLowCarrierFixedResidueImported", imported, False, "导入 rank-pressure 后的 endpoint low-carrier fixed-residue 出口。", LOW_RESIDUE),
        row("BoundaryCarrierDegeneratesToEndpointExit", imported, True, "若 pivot carrier 为 q=P，则 P 不可逆；该项不走 AP 公式，而退化为列边界 ColumnCRT 或 endpoint singleton/source-multiplicity 已命名出口。", BOUNDARY),
        row("EndpointResidueToRowAPFormulaClosed", imported and firstbreak_formula, True, "对 q<P，P 在 mod q 可逆；固定 residue a 强制 endpoint 行坐标 t 落在唯一 AP 类 t==-aP^{-1} mod q。", AP_FORMULA),
        row("EndpointSingleResidueSharpEnvelopeClosed", imported and firstbreak_formula, True, "长度 H 的 endpoint 支撑窗口内，同一 (q,a) cell 至多命中 ceil(H/q) 个行位置。", SINGLE_CELL),
        row("EndpointAllResiduesExactMassClosed", imported and exact_envelope, True, "固定 q 时所有 residue cell 精确分割 endpoint 窗口，发生总量为 H。", ALL_RESIDUES),
        row("EndpointSelectedTableExactEnvelopeClosed", imported and exact_envelope, True, "任意低 carrier residue table T 的发生量由 cell envelope 求和控制，并受 H*|Q(T)| 控制。", TABLE_ENV),
        row("EndpointLowCarrierResidueTableFiniteClosed", imported, True, "固定阈值 B 后，q<=B 且 q<P 的低 carrier residue cells 是有限低维表。", FINITE_TABLE),
        row("EndpointLowEffectiveModColumnCRTImport", lowmod_imported, lowmod_imported, "已有低有效模/共同因子路由可登记持久低维 residue table 的 ColumnCRT/PDEC 形态。", LOWMOD_IMPORT),
        row("EndpointDenseResidueTablePDECRouteRegistered", imported and lowmod_imported, phase_schema_imported, "若低维 table 持久接近 envelope 或承担正密度压力，则登记为 endpoint dense residue table PDEC。", DENSE_TABLE),
        row("EndpointSparseResidueCellSAERouteRegistered", imported, phase_schema_imported, "若低 carrier cells 不持久或稀疏，则只能进入 endpoint sparse cell SAE/LocalSurvivor 计费。", SPARSE_CELL),
        row("EndpointActualDemandLowerBoundStillOpen", False, False, "尚未证明反例链强制的 endpoint low-carrier actual row-incidence demand 超过 exact envelope。", ENDPOINT_DEMAND),
        row("EndpointAPEnvelopeStrictGapStillOpen", False, False, "尚未证明 exact envelope 与实际支付义务之间的 strict gap，或排斥所有 dense-table PDEC。", ENDPOINT_STRICT_GAP),
        row("NoIndependentEndpointLowCarrierFixedResidueAfterAPEnvelope", imported, True, "endpoint low-carrier fixed-residue 不再作为匿名单出口保留。", NO_LOW_RESIDUE),
        row("EndpointLowCarrierFixedResidueReduced", imported, False, "本步只完成 AP-envelope 降维；低 carrier actual demand、strict gap、dense-table 与 sparse-cell 终端仍待排斥。", REDUCED_LOW_RESIDUE),
        row("EndpointLowCarrierFixedResidueExcluded", False, False, "未证明 endpoint low-carrier fixed-residue 分支不存在。", new_target),
        row("RowColumnUnconditionalClosureReached", False, False, "行/列命题仍未无条件闭合。", new_target),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    previous = load_json(PREVIOUS_CERT)
    residue_ap = load_json(FIRSTBREAK_RESIDUE_AP_CERT)
    ap_envelope = load_json(FIRSTBREAK_AP_ENVELOPE_CERT)
    lowmod = load_json(LOW_EFFECTIVE_MOD_CERT)
    phase_schema = load_json(PHASE_SCHEMA_CERT)
    new_target = replace_target(previous)
    reduced = reduced_target(new_target)
    rows = build_rows(previous, residue_ap, ap_envelope, lowmod, phase_schema, new_target)
    imported = any(item["gate"] == "EndpointPivotLowCarrierFixedResidueImported" and item["closed"] for item in rows)
    reduced_closed = any(item["gate"] == "NoIndependentEndpointLowCarrierFixedResidueAfterAPEnvelope" and item["closed"] for item in rows)
    plain = (
        "endpoint pivot low-carrier fixed-residue 分支已被压成 AP-envelope 接口："
        "当 q<P 时，固定 residue a 迫使 endpoint 行坐标 t 落在唯一同余类 "
        "t==-aP^{-1} mod q；长度 H 的支撑窗口中单 cell 至多给出 ceil(H/q) 个命中，"
        "固定 q 的全部 residue cell 总量精确为 H。q=P 的边界 carrier 不走 AP 公式，"
        "退化为既有 ColumnCRT 或 endpoint singleton/source-multiplicity 出口。"
    )
    return {
        "certificate_type": "prime_matrix_phase_residue_exchange_endpoint_alternating_cycle_pivot_low_carrier_fixed_residue_ap_table_router",
        "status": "endpoint_pivot_low_carrier_fixed_residue_reduced_to_ap_envelope_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "firstbreak_residue_ap_template_certificate": str(FIRSTBREAK_RESIDUE_AP_CERT.relative_to(ROOT)),
        "firstbreak_ap_envelope_template_certificate": str(FIRSTBREAK_AP_ENVELOPE_CERT.relative_to(ROOT)),
        "low_effective_mod_certificate": str(LOW_EFFECTIVE_MOD_CERT.relative_to(ROOT)),
        "phase_schema_certificate": str(PHASE_SCHEMA_CERT.relative_to(ROOT)),
        "previous_direct_attack_target": previous.get("next_direct_attack_target", ""),
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "no_theorem_switch": True,
        "endpoint_pivot_low_carrier_fixed_residue_imported": imported,
        "endpoint_pivot_boundary_carrier_degeneracy_closed": imported,
        "endpoint_pivot_residue_to_row_ap_formula_closed": imported,
        "endpoint_pivot_single_residue_sharp_envelope_closed": imported,
        "endpoint_pivot_all_residues_exact_mass_closed": imported,
        "endpoint_pivot_selected_table_exact_envelope_closed": imported,
        "endpoint_pivot_low_carrier_residue_table_finite_closed": imported,
        "endpoint_pivot_dense_residue_table_pdec_registered": imported,
        "endpoint_pivot_sparse_residue_cell_sae_registered": imported,
        "endpoint_pivot_low_carrier_fixed_residue_reduced_to_ap_envelope": reduced_closed,
        "endpoint_pivot_actual_demand_lower_bound_proved": False,
        "endpoint_pivot_ap_envelope_strict_gap_proved": False,
        "endpoint_pivot_dense_low_carrier_residue_table_pdec_proved": False,
        "endpoint_pivot_sparse_low_carrier_residue_cell_sae_proved": False,
        "endpoint_pivot_low_carrier_fixed_residue_excluded": False,
        "endpoint_pivot_low_carrier_nonpersistent_sparse_sae_proved": False,
        "endpoint_pivot_high_carrier_rank_deficit_proved": False,
        "endpoint_pivot_nonreplay_sparse_sae_proved": False,
        "endpoint_pivot_moving_prime_phase_slip_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": LOW_RESIDUE,
        "hardpoint_after_router": REDUCED_LOW_RESIDUE,
        "old_exits": [LOW_RESIDUE],
        "new_exits": [ENDPOINT_DEMAND, ENDPOINT_STRICT_GAP, DENSE_TABLE, SPARSE_CELL],
        "boundary_carrier_q_equals_P_route": [
            "ColumnCRT boundary degeneracy",
            "StableLadderEndpointSingletonAtomSAE",
            SOURCE_MULTIPLICITY,
        ],
        "next_direct_attack_target": new_target,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous, reduced),
        "ap_records": ap_records(),
        "gates": rows,
        "plain_conclusion": plain,
        "source_hashes": source_hashes(),
    }


def render_md(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix endpoint pivot low-carrier fixed-residue AP-envelope 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_pivot_low_carrier_fixed_residue_imported={fmt_bool(cert['endpoint_pivot_low_carrier_fixed_residue_imported'])}",
        f"endpoint_pivot_boundary_carrier_degeneracy_closed={fmt_bool(cert['endpoint_pivot_boundary_carrier_degeneracy_closed'])}",
        f"endpoint_pivot_residue_to_row_ap_formula_closed={fmt_bool(cert['endpoint_pivot_residue_to_row_ap_formula_closed'])}",
        f"endpoint_pivot_selected_table_exact_envelope_closed={fmt_bool(cert['endpoint_pivot_selected_table_exact_envelope_closed'])}",
        f"endpoint_pivot_low_carrier_fixed_residue_reduced_to_ap_envelope={fmt_bool(cert['endpoint_pivot_low_carrier_fixed_residue_reduced_to_ap_envelope'])}",
        f"endpoint_pivot_actual_demand_lower_bound_proved={fmt_bool(cert['endpoint_pivot_actual_demand_lower_bound_proved'])}",
        f"endpoint_pivot_low_carrier_fixed_residue_excluded={fmt_bool(cert['endpoint_pivot_low_carrier_fixed_residue_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. AP-envelope 降维",
        "",
        "在 endpoint 支撑窗口中取规范行/相位坐标 `t`，窗口长度为 `H`。对低 carrier pivot prime `q<P` 与固定 residue `a mod q`，fixed-residue 覆盖条件给出",
        "",
        "```text",
        "tP + a == 0 mod q.",
        "```",
        "",
        "由于 `(P,q)=1`，这等价于唯一 AP 类",
        "",
        "```text",
        "t == -a P^{-1} mod q.",
        "```",
        "",
        "因此单个 `(q,a)` cell 在长度 `H` 的 endpoint 窗口中至多命中 `ceil(H/q)` 次。固定 `q` 时，所有 `a mod q` 的 residue cells 精确分割该窗口，总发生量为 `H`。",
        "",
        "`q=P` 是边界 carrier：此时 `P` 不可逆，不能进入 AP 公式；它退化为列边界 ColumnCRT 或 endpoint singleton/source-multiplicity 已命名出口。",
        "",
        "## 2. 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for record in cert["ap_records"]:
        lines.append(f"| `{cell(record['field'])}` | {cell(record['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 出口更新",
            "",
            "```text",
            cert["hardpoint_before_router"],
            f"  -> {ENDPOINT_DEMAND}",
            f"  AND {ENDPOINT_STRICT_GAP}",
            f"  AND {DENSE_TABLE}",
            f"  AND {SPARSE_CELL}",
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
            "- 本证书不证明 endpoint low-carrier fixed-residue 分支不存在。",
            "- 本证书只关闭 q<P 的 AP-envelope 公式，并把 q=P 边界 carrier 登记到既有 endpoint 出口。",
            "- actual demand 下界、strict gap、dense-table PDEC 与 sparse-cell SAE 仍未排斥。",
            "- low carrier nonpersistent sparse、high carrier rank-deficit、nonreplay、moving-pivot、endpoint singleton/full mean/source multiplicity 与 sparse SAE 仍未完成。",
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
