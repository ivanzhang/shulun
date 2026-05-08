#!/usr/bin/env python3
"""Prime Matrix clean-core DLS LowPhase PDEC/flat DLS 攻关路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_dls_lowphase_pdec_flat_router.py

输出：
  docs/monograph/prime-matrix-clean-core-dls-lowphase-pdec-flat-router.json
  docs/monograph/prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
AUDIT_DOCS = ROOT / "docs"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.json"
DEFAULT_WHEEL_MD = DOCS / "prime-matrix-dprc-wheel-unit-phase-balance.md"
DEFAULT_WHEEL_JSON = AUDIT_DOCS / "dprc_wheel_unit_phase_balance_w30_p100000_20260506.json"
DEFAULT_LAYERED_MD = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_LAYERED_JSON = AUDIT_DOCS / "dprc_layered_wheel_phase_scan_p100000_20260506.json"
DEFAULT_FOURIER_MD = DOCS / "prime-matrix-dprc-fourier-inheritance-classifier.md"
DEFAULT_FOURIER_JSON = AUDIT_DOCS / "dprc_fourier_inheritance_classifier_20260506.json"
DEFAULT_NEWLAYER_MD = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_NEWLAYER_JSON = AUDIT_DOCS / "dprc_newlayer_energy_scan_p100000_20260506.json"
DEFAULT_PDEC_TOWER = DOCS / "prime-matrix-newlayer-pdec-tower-entropy-contract.md"
DEFAULT_SN3 = DOCS / "prime-matrix-sn3-distributed-band-large-sieve-bridge.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def threshold_row(data: dict[str, Any], key: str, threshold: int) -> dict[str, Any]:
    """按阈值取 summary 行。"""
    for row in data.get(key, []):
        if row.get("threshold") == threshold:
            return row
    return {}


def wheel_metrics(wheel_json: dict[str, Any], layered_json: dict[str, Any], newlayer_json: dict[str, Any]) -> dict[str, Any]:
    """抽取 LowPhase 相关审计指标。"""
    wheel_2003 = threshold_row(wheel_json, "summaries", 2003)
    layered_2003 = threshold_row(layered_json, "summaries", 2003)
    newlayer_2003 = threshold_row(newlayer_json, "summaries", 2003)
    layered_wheels = {
        row.get("wheel"): row for row in layered_2003.get("wheels", [])
    }
    newlayer_wheels = {
        row.get("wheel"): row for row in newlayer_2003.get("wheels", [])
    }
    return {
        "wheel30_max_peak": wheel_2003.get("max_unit30_peak_over_sqrt", 0.0),
        "wheel30_high_l1_count": wheel_2003.get("high_l1_count", 0),
        "wheel30_high_l2_count": wheel_2003.get("high_l2_count", 0),
        "wheel30_high_l1_max_peak": wheel_2003.get("high_l1_max_unit30_peak", 0.0),
        "wheel30_max_l1_when_peak_ge_0_8": wheel_2003.get("max_l1_when_unit30_peak_ge_0_8", 0.0),
        "wheel30_max_l2_when_peak_ge_0_8": wheel_2003.get("max_l2_when_unit30_peak_ge_0_8", 0.0),
        "layered_max_peaks": {
            str(wheel): row.get("max_unit_peak_over_sqrt", 0.0)
            for wheel, row in layered_wheels.items()
        },
        "layered_high_l1_max_peaks": {
            str(wheel): row.get("high_l1_max_unit_peak", 0.0)
            for wheel, row in layered_wheels.items()
        },
        "newlayer_energy_shares": {
            str(wheel): row.get("newlayer_energy_share_stats", {})
            for wheel, row in newlayer_wheels.items()
        },
        "newlayer_high_l1_max_peaks": {
            str(wheel): row.get("high_l1_max_centered_top", 0.0)
            for wheel, row in newlayer_wheels.items()
        },
        "newlayer_high_l2_max_peaks": {
            str(wheel): row.get("high_l2_max_centered_top", 0.0)
            for wheel, row in newlayer_wheels.items()
        },
        "danger_l1_l2_6_5_count": layered_2003.get("danger_l1_l2_6_5_count", 0),
        "danger_l1_l2_cauchy_count": layered_2003.get("danger_l1_l2_cauchy_count", 0),
    }


def fourier_metrics(fourier_json: dict[str, Any]) -> dict[str, Any]:
    """抽取 Fourier 继承分类指标。"""
    summary = fourier_json.get("summary", {})
    wheel_rows = summary.get("wheel_summaries", [])
    return {
        "record_count": summary.get("record_count", 0),
        "high_l1_count": summary.get("high_l1_count", 0),
        "high_l2_cauchy_count": summary.get("high_l2_cauchy_count", 0),
        "danger_intersection_count": summary.get("danger_intersection_count", 0),
        "wheel_rows": [
            {
                "wheel": row.get("wheel"),
                "class_histogram": row.get("class_histogram", {}),
                "new_factor_histogram": row.get("new_factor_histogram", {}),
                "max_fourier_abs_over_sqrt": row.get("max_fourier_abs_over_sqrt", 0.0),
                "max_centered_top_over_sqrt": row.get("max_centered_top_over_sqrt", 0.0),
            }
            for row in wheel_rows
        ],
    }


def micro_rows(metrics: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 LowPhase 三微输入表。"""
    return [
        {
            "micro_input": "DLSFixedWheelUnitPeakDilutionOrPDECReturn",
            "route": "fixed W-unit PDEC or dilution",
            "closed": False,
            "evidence": (
                f"W=30 max peak={metrics['wheel30_max_peak']:.6f}, "
                f"high-L1 max peak={metrics['wheel30_high_l1_max_peak']:.6f}"
            ),
            "meaning": "固定轮单位类峰若与 BES 危险同步，必须给出 W-unit PDEC；若不同步，固定轮不能支付 LowPhase 危险质量。",
        },
        {
            "micro_input": "DLSNewLayerFourierConcentrationPDECReturn",
            "route": "new-layer PDEC or phase-dimension lower bound",
            "closed": False,
            "evidence": "Fourier 继承分类显示 W=2310 的代表强频率全部进入新增因子 11 层。",
            "meaning": "新增层强频率若低维集中，则给 new-layer PDEC；若高维分散，则不能形成单位相位尖峰。",
        },
        {
            "micro_input": "DLSFlatHighModLargeSieveAbsorption",
            "route": "flat high-mod DLS/KLS absorption",
            "closed": False,
            "evidence": "新增层能量强但高 BES 压力处 centered peak 明显下降。",
            "meaning": "若固定轮与新增层均不集中，剩余 LowPhase 必须由真正高模平坦大筛吸收。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    wheel_md: str,
    layered_md: str,
    fourier_md: str,
    newlayer_md: str,
    pdec_tower: str,
    sn3: str,
    metrics: dict[str, Any],
    fourier: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 LowPhase 判定表。"""
    return [
        {
            "gate": "PreviousLowPhaseInputPinned",
            "closed": "DLSLowPhasePDECNewLayerOrFlatDLSBound"
            in previous.get("latest_internal_subinputs", []),
            "proved": True,
            "meaning": "上一层已把 BES-DLS 最窄优先级定位为 LowPhase 的 PDEC/new-layer/flat DLS 二分。",
            "remaining": "单独攻击 LowPhase 输入。",
        },
        {
            "gate": "WheelUnitPhaseBalanceRouteAvailable",
            "closed": "WheelUnitPhaseBalance" in wheel_md and "LayeredClamp" in layered_md,
            "proved": False,
            "meaning": "固定轮和层叠轮单位类相位账本已建立。",
            "remaining": "证明固定轮峰同步必给 PDEC，或证明峰随层提升不能支付 BES 危险交集。",
        },
        {
            "gate": "CurrentAuditDangerSyncClear",
            "closed": metrics.get("danger_l1_l2_6_5_count") == 0
            and metrics.get("danger_l1_l2_cauchy_count") == 0,
            "proved": False,
            "meaning": "P<=100000 的层叠轮审计中 BES 危险交集为零。",
            "remaining": "审计不是全局证明。",
        },
        {
            "gate": "FourierInheritanceNewLayerRouteAvailable",
            "closed": "new-layer PDEC" in fourier_md
            and fourier.get("danger_intersection_count") == 0,
            "proved": False,
            "meaning": "代表样本的强 Fourier 频率可分为继承层与新增层，新增层偏斜可命名为 new-layer PDEC。",
            "remaining": "证明新增层低维集中必给 PDEC，或证明集中不能与 BES 危险同步。",
        },
        {
            "gate": "NewLayerEnergyDispersionRouteAvailable",
            "closed": "NewLayer Dispersion Clamp" in newlayer_md,
            "proved": False,
            "meaning": "新增层能量恒等式已把强能量与单峰集中区分开。",
            "remaining": "证明 phase-dimension 下界推出 flat DLS 吸收。",
        },
        {
            "gate": "NewLayerPDECTowerNoUnnamedEscape",
            "closed": "New-layer PDEC" in pdec_tower or "new-layer PDEC" in pdec_tower,
            "proved": False,
            "meaning": "若不断升层出现新增层偏斜，已有塔熵合同要求它进入 profinite/new-layer PDEC 或 CleanKLS。",
            "remaining": "仍需实际 PDEC/flat DLS 终端证明。",
        },
        {
            "gate": "FlatDLSAbsorptionInterfaceAvailable",
            "closed": "TrueDistributedDLS" in sn3 and "PDEC/ColumnCRT" in sn3,
            "proved": False,
            "meaning": "低维峰剥离后的平坦分散残余已有 SN3/DLS 接口。",
            "remaining": "证明 DLSFlatHighModLargeSieveAbsorption。",
        },
        {
            "gate": "LowPhasePDECFlatInputProved",
            "closed": False,
            "proved": False,
            "meaning": "LowPhase 输入未闭合；它被拆成固定轮峰、新增层集中和平坦高模吸收三项。",
            "remaining": (
                "DLSFixedWheelUnitPeakDilutionOrPDECReturn AND "
                "DLSNewLayerFourierConcentrationPDECReturn AND "
                "DLSFlatHighModLargeSieveAbsorption"
            ),
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "LowPhase、其余 DLS 微输入、signed 源锁和模型余量完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    wheel_md_path: Path,
    wheel_json_path: Path,
    layered_md_path: Path,
    layered_json_path: Path,
    fourier_md_path: Path,
    fourier_json_path: Path,
    newlayer_md_path: Path,
    newlayer_json_path: Path,
    pdec_tower_path: Path,
    sn3_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 LowPhase PDEC/flat DLS 路由。"""
    source_paths = [
        previous_path,
        wheel_md_path,
        wheel_json_path,
        layered_md_path,
        layered_json_path,
        fourier_md_path,
        fourier_json_path,
        newlayer_md_path,
        newlayer_json_path,
        pdec_tower_path,
        sn3_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    wheel_md = wheel_md_path.read_text(encoding="utf-8")
    wheel_json = load_json(wheel_json_path)
    layered_md = layered_md_path.read_text(encoding="utf-8")
    layered_json = load_json(layered_json_path)
    fourier_md = fourier_md_path.read_text(encoding="utf-8")
    fourier_json = load_json(fourier_json_path)
    newlayer_md = newlayer_md_path.read_text(encoding="utf-8")
    newlayer_json = load_json(newlayer_json_path)
    pdec_tower = pdec_tower_path.read_text(encoding="utf-8")
    sn3 = sn3_path.read_text(encoding="utf-8")
    dstructure = load_json(dstructure_path)
    metrics = wheel_metrics(wheel_json, layered_json, newlayer_json)
    fourier = fourier_metrics(fourier_json)
    micros = micro_rows(metrics)
    rows = gate_rows(
        previous,
        wheel_md,
        layered_md,
        fourier_md,
        newlayer_md,
        pdec_tower,
        sn3,
        metrics,
        fourier,
        dstructure,
    )

    signed_identity = "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn"
    modelgap_input = "ExplicitModelGapAndFiniteDPRCLedger"
    pointload_input = "DLSPointLoadColumnCRTBoundOrNamedReturn"
    shortwindow_input = "DLSShortWindowSAEBoundOrNamedReturn"
    fixedwheel_input = "DLSFixedWheelUnitPeakDilutionOrPDECReturn"
    newlayer_input = "DLSNewLayerFourierConcentrationPDECReturn"
    flat_input = "DLSFlatHighModLargeSieveAbsorption"
    signed_budget_lift = "SignedGeometricLedgerVariationBranchLiftAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_dls_lowphase_pdec_flat_router",
        "status": "dls_lowphase_reduced_to_fixedwheel_newlayer_flatdls",
        "previous_lowphase_input": "DLSLowPhasePDECNewLayerOrFlatDLSBound",
        "dls_lowphase_boundary_closed": all(
            row["closed"]
            for row in rows
            if row["gate"]
            not in {
                "WheelUnitPhaseBalanceRouteAvailable",
                "CurrentAuditDangerSyncClear",
                "FourierInheritanceNewLayerRouteAvailable",
                "NewLayerEnergyDispersionRouteAvailable",
                "NewLayerPDECTowerNoUnnamedEscape",
                "FlatDLSAbsorptionInterfaceAvailable",
                "LowPhasePDECFlatInputProved",
                "DStructureRankinStillIndependent",
            }
        ),
        "lowphase_input_proved": False,
        "row_column_unconditional_closed": False,
        "wheel_metrics": metrics,
        "fourier_metrics": fourier,
        "micro_rows": micros,
        "latest_internal_subinputs": [
            signed_identity,
            modelgap_input,
            pointload_input,
            shortwindow_input,
            fixedwheel_input,
            newlayer_input,
            flat_input,
            signed_budget_lift,
        ],
        "latest_external_subinput": latest_external,
        "latest_conditional_basis": (
            f"(({signed_identity} AND {modelgap_input} AND {pointload_input} "
            f"AND {shortwindow_input} AND {fixedwheel_input} AND {newlayer_input} "
            f"AND {flat_input} AND {signed_budget_lift}) OR {latest_external}) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            f"{signed_identity} AND {modelgap_input} AND {pointload_input} "
            f"AND {shortwindow_input} AND {fixedwheel_input} AND {newlayer_input} "
            f"AND {flat_input} AND {signed_budget_lift} "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "core_reduction_law": (
            "LowPhase 不是单个固定模规律。固定轮单位类峰若持续同步，给 W-unit PDEC；"
            "升层后若新增 Fourier 频率低维集中，给 new-layer PDEC；若固定轮和新增层均被稀释，"
            "剩余只能是高模平坦分散能量，必须由 flat DLS/KLS 大筛吸收。"
            "因此 LowPhase 输入被拆成固定轮峰稀释/回流、新增层集中/回流、flat DLS 吸收三项。"
        ),
        "rows": rows,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
    }
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_out.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 归档。"""
    metrics = result["wheel_metrics"]
    fourier = result["fourier_metrics"]
    lines: list[str] = [
        "# Prime Matrix clean-core DLS LowPhase PDEC/flat DLS 攻关路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["core_reduction_law"],
        "",
        "```text",
        f"dls_lowphase_boundary_closed={fmt_bool(result['dls_lowphase_boundary_closed'])}",
        f"lowphase_input_proved={fmt_bool(result['lowphase_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 审计摘要",
        "",
        "| metric | value |",
        "| --- | --- |",
        f"| W=30 max peak | `{metrics['wheel30_max_peak']:.6f}` |",
        f"| W=30 high-L1 max peak | `{metrics['wheel30_high_l1_max_peak']:.6f}` |",
        f"| W=30 max L1 when peak>=0.8 | `{metrics['wheel30_max_l1_when_peak_ge_0_8']:.6f}` |",
        f"| W=30 max L2 when peak>=0.8 | `{metrics['wheel30_max_l2_when_peak_ge_0_8']:.6f}` |",
        f"| layered danger count | `{metrics['danger_l1_l2_6_5_count']}` |",
        f"| layered cauchy danger count | `{metrics['danger_l1_l2_cauchy_count']}` |",
        f"| Fourier representative danger count | `{fourier['danger_intersection_count']}` |",
        "",
        "层叠轮最大单位峰：",
        "",
        "| W | max peak | high-L1 max peak |",
        "| ---: | ---: | ---: |",
    ]
    for wheel, value in sorted(metrics["layered_max_peaks"].items(), key=lambda item: int(item[0])):
        high_l1 = metrics["layered_high_l1_max_peaks"].get(wheel, 0.0)
        lines.append(f"| `{wheel}` | `{value:.6f}` | `{high_l1:.6f}` |")
    lines.extend(
        [
            "",
            "Fourier 继承代表样本：",
            "",
            "| W | class_histogram | new_factor_histogram | max Fourier/sqrt | max centered peak/sqrt |",
            "| ---: | --- | --- | ---: | ---: |",
        ]
    )
    for row in fourier["wheel_rows"]:
        lines.append(
            "| `{wheel}` | `{class_histogram}` | `{new_factor_histogram}` | `{fourier:.6f}` | `{peak:.6f}` |".format(
                wheel=row["wheel"],
                class_histogram=table_cell(row["class_histogram"]),
                new_factor_histogram=table_cell(row["new_factor_histogram"]),
                fourier=row["max_fourier_abs_over_sqrt"],
                peak=row["max_centered_top_over_sqrt"],
            )
        )
    lines.extend(
        [
            "",
            "这些读数只用于定位结构，不是证明。",
            "",
            "## 2. 三个 LowPhase 微输入",
            "",
            "| micro_input | route | closed | evidence | meaning |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["micro_rows"]:
        lines.append(
            "| `{micro_input}` | {route} | `{closed}` | {evidence} | {meaning} |".format(
                micro_input=table_cell(row["micro_input"]),
                route=table_cell(row["route"]),
                closed=fmt_bool(row["closed"]),
                evidence=table_cell(row["evidence"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 当前结论",
            "",
            "本步关闭的是 LowPhase 的路线边界：它不能再作为一个整体黑箱。"
            "下一步应直接攻 fixed-wheel 峰稀释/new-layer PDEC/flat DLS 三个微输入，"
            "其中最贴近现有结构材料的是 `DLSNewLayerFourierConcentrationPDECReturn`。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--wheel-md", type=Path, default=DEFAULT_WHEEL_MD)
    parser.add_argument("--wheel-json", type=Path, default=DEFAULT_WHEEL_JSON)
    parser.add_argument("--layered-md", type=Path, default=DEFAULT_LAYERED_MD)
    parser.add_argument("--layered-json", type=Path, default=DEFAULT_LAYERED_JSON)
    parser.add_argument("--fourier-md", type=Path, default=DEFAULT_FOURIER_MD)
    parser.add_argument("--fourier-json", type=Path, default=DEFAULT_FOURIER_JSON)
    parser.add_argument("--newlayer-md", type=Path, default=DEFAULT_NEWLAYER_MD)
    parser.add_argument("--newlayer-json", type=Path, default=DEFAULT_NEWLAYER_JSON)
    parser.add_argument("--pdec-tower", type=Path, default=DEFAULT_PDEC_TOWER)
    parser.add_argument("--sn3", type=Path, default=DEFAULT_SN3)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        args.previous,
        args.wheel_md,
        args.wheel_json,
        args.layered_md,
        args.layered_json,
        args.fourier_md,
        args.fourier_json,
        args.newlayer_md,
        args.newlayer_json,
        args.pdec_tower,
        args.sn3,
        args.dstructure,
        args.json_out,
        args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
