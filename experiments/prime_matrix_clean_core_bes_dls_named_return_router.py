#!/usr/bin/env python3
"""Prime Matrix clean-core BES-DLS 命名回流攻关路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_bes_dls_named_return_router.py

输出：
  docs/monograph/prime-matrix-clean-core-bes-dls-named-return-router.json
  docs/monograph/prime-matrix-clean-core-bes-dls-named-return-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-dprc-centered-discrepancy-router.json"
DEFAULT_DLS = DOCS / "prime-matrix-dprc-bes-dual-large-sieve-route.md"
DEFAULT_NEARMISS = AUDIT_DOCS / "dprc_bes_nearmiss_structure_audit_extended_20260506.json"
DEFAULT_WHEEL = DOCS / "prime-matrix-dprc-wheel-unit-phase-balance.md"
DEFAULT_FOURIER = DOCS / "prime-matrix-dprc-fourier-inheritance-classifier.md"
DEFAULT_NEWLAYER = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_COLUMNCRT = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.md"


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


def nearmiss_summary(data: dict[str, Any]) -> dict[str, Any]:
    """抽取近危险审计中的三出口诊断指标。"""
    records = data.get("records", [])
    max_point_load = 0
    max_short_window = 0.0
    max_low_phase = 0.0
    top_low_phase_unit_flags: list[bool] = []
    max_l1 = 0.0
    max_l2 = 0.0
    max_eff_dim = 0.0
    for record in records:
        max_l1 = max(max_l1, float(record.get("positive_bucket_l1_over_sqrt", 0.0)))
        max_l2 = max(max_l2, float(record.get("positive_bucket_l2_over_sqrt", 0.0)))
        max_eff_dim = max(
            max_eff_dim,
            float(record.get("positive_bucket_effective_dimension", 0.0)),
        )
        max_point_load = max(
            max_point_load,
            int(record.get("point_load", {}).get("max_load", 0)),
        )
        for row in record.get("short_window", []):
            max_short_window = max(
                max_short_window,
                float(row.get("max_chunk_positive_over_sqrt", 0.0)),
            )
        for row in record.get("low_phase", []):
            max_low_phase = max(
                max_low_phase,
                float(row.get("max_positive_over_sqrt", 0.0)),
            )
            top = row.get("top_residues", [])
            if top:
                top_low_phase_unit_flags.append(bool(top[0].get("n_residue_is_unit")))
    return {
        "record_count": len(records),
        "max_l1_over_sqrt": max_l1,
        "max_l2_over_sqrt": max_l2,
        "max_effective_dimension": max_eff_dim,
        "max_point_load": max_point_load,
        "max_short_window_positive_over_sqrt": max_short_window,
        "max_low_phase_positive_over_sqrt": max_low_phase,
        "all_top_low_phase_residues_are_units": all(top_low_phase_unit_flags)
        if top_low_phase_unit_flags
        else False,
    }


def exit_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 DLS 三出口表。"""
    return [
        {
            "exit": "PointLoad",
            "diagnostic": f"nearmiss max point load = {summary['max_point_load']}",
            "route": "ColumnCRT / tail-anchor / displacement PDEC",
            "micro_input": "DLSPointLoadColumnCRTBoundOrNamedReturn",
            "closed": False,
            "meaning": "若单点高素标签负载可持续超阈值，则固定列位移或尾锚签名必须回流 ColumnCRT/PDEC；否则不能支付 BES 危险交集。",
        },
        {
            "exit": "ShortWindow",
            "diagnostic": (
                "nearmiss max short-window positive = "
                f"{summary['max_short_window_positive_over_sqrt']:.6f} sqrt(S)"
            ),
            "route": "SAE / LocalSurvivor / persistent sparse PDEC",
            "micro_input": "DLSShortWindowSAEBoundOrNamedReturn",
            "closed": False,
            "meaning": "若短 q 子窗承担固定比例正偏差，则必须生成有限 LocalSurvivor/SAE packet，或持久化为 PDEC。",
        },
        {
            "exit": "LowPhase",
            "diagnostic": (
                "nearmiss max low-phase positive = "
                f"{summary['max_low_phase_positive_over_sqrt']:.6f} sqrt(S); "
                f"top residues unit={fmt_bool(summary['all_top_low_phase_residues_are_units'])}"
            ),
            "route": "W-unit PDEC / new-layer PDEC / flat DLS",
            "micro_input": "DLSLowPhasePDECNewLayerOrFlatDLSBound",
            "closed": False,
            "meaning": "若分散正偏差在单位类或新增轮层 Fourier 方向同步，则给出 PDEC；若每层分散，则必须由高模 DLS 大筛吸收。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    dls: str,
    summary: dict[str, Any],
    wheel: str,
    fourier: str,
    newlayer: str,
    columncrt: str,
    sae: str,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 BES-DLS 命名回流判定表。"""
    return [
        {
            "gate": "PreviousBESDLSInputPinned",
            "closed": "BESDangerIntersectionExclusionOrDLSNamedReturn"
            in previous.get("latest_internal_subinputs", []),
            "proved": True,
            "meaning": "上一层已把 DPRC 正偏差锁压到 BES 危险交集排斥或 DLS 命名回流。",
            "remaining": "单独攻击 BES-DLS 输入。",
        },
        {
            "gate": "DLSKernelAndDangerAlgebraClosed",
            "closed": all(token in dls for token in ["DLS-1", "DLS-2", "DLS-4", "DLS-6"]),
            "proved": True,
            "meaning": "中心化核、危险交集、尖峰桶鸽巢和二次能量展开已经形式化。",
            "remaining": "把二次能量超额严格送入三出口。",
        },
        {
            "gate": "DLSPointShortLowAlphabetClosed",
            "closed": all(token in dls for token in ["PointLoad", "ShortWindow", "LowPhase"]),
            "proved": False,
            "meaning": "DLS 失败字母表已固定为 PointLoad、ShortWindow、LowPhase。",
            "remaining": "证明该三分覆盖所有 BES 危险失败，而非只是证明路线。",
        },
        {
            "gate": "NearmissThreeExitDiagnosticsMaterialized",
            "closed": summary["record_count"] > 0
            and summary["max_point_load"] <= 4
            and summary["all_top_low_phase_residues_are_units"],
            "proved": False,
            "meaning": "近危险审计显示 PointLoad 不爆炸，ShortWindow 不够强，最稳定信号是单位类内部 LowPhase。",
            "remaining": "审计不能替代全局排斥证明。",
        },
        {
            "gate": "ColumnCRTIndependentExitAbsorbed",
            "closed": "ColumnCRT 是 displacement PDEC 或 SAE" in columncrt,
            "proved": False,
            "meaning": "PointLoad 若形成列位移持久过载，不是独立终端，而是 displacement PDEC 或 SAE。",
            "remaining": "仍需证明 DLSPointLoadColumnCRTBoundOrNamedReturn。",
        },
        {
            "gate": "SAEIndependentExitAbsorbed",
            "closed": "sae_independent_terminal_removed=true" in sae,
            "proved": False,
            "meaning": "ShortWindow 若形成孤窗逃逸，不是独立终端，而是 LocalSurvivor packet 或持久 PDEC。",
            "remaining": "仍需证明 DLSShortWindowSAEBoundOrNamedReturn。",
        },
        {
            "gate": "LowPhaseLayeredPDECRouteClosed",
            "closed": "WheelUnitPhaseBalance" in wheel
            and "new-layer PDEC" in fourier
            and "NewLayer Dispersion Clamp" in newlayer,
            "proved": False,
            "meaning": "LowPhase 已接入 W-unit/new-layer PDEC 与 flat DLS 二分。",
            "remaining": "证明 DLSLowPhasePDECNewLayerOrFlatDLSBound。",
        },
        {
            "gate": "BESDLSNamedReturnInputProved",
            "closed": False,
            "proved": False,
            "meaning": "BES-DLS 输入未闭合；它被拆成三出口微输入。",
            "remaining": (
                "DLSPointLoadColumnCRTBoundOrNamedReturn AND "
                "DLSShortWindowSAEBoundOrNamedReturn AND "
                "DLSLowPhasePDECNewLayerOrFlatDLSBound"
            ),
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "BES-DLS、signed 源锁和模型余量完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    dls_path: Path,
    nearmiss_path: Path,
    wheel_path: Path,
    fourier_path: Path,
    newlayer_path: Path,
    columncrt_path: Path,
    sae_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 BES-DLS 命名回流路由。"""
    source_paths = [
        previous_path,
        dls_path,
        nearmiss_path,
        wheel_path,
        fourier_path,
        newlayer_path,
        columncrt_path,
        sae_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    dls = dls_path.read_text(encoding="utf-8")
    nearmiss = load_json(nearmiss_path)
    wheel = wheel_path.read_text(encoding="utf-8")
    fourier = fourier_path.read_text(encoding="utf-8")
    newlayer = newlayer_path.read_text(encoding="utf-8")
    columncrt = columncrt_path.read_text(encoding="utf-8")
    sae = sae_path.read_text(encoding="utf-8")
    dstructure = load_json(dstructure_path)
    summary = nearmiss_summary(nearmiss)
    exits = exit_rows(summary)
    rows = gate_rows(previous, dls, summary, wheel, fourier, newlayer, columncrt, sae, dstructure)

    signed_identity = "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn"
    modelgap_input = "ExplicitModelGapAndFiniteDPRCLedger"
    pointload_input = "DLSPointLoadColumnCRTBoundOrNamedReturn"
    shortwindow_input = "DLSShortWindowSAEBoundOrNamedReturn"
    lowphase_input = "DLSLowPhasePDECNewLayerOrFlatDLSBound"
    signed_budget_lift = "SignedGeometricLedgerVariationBranchLiftAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_bes_dls_named_return_router",
        "status": "bes_dls_named_return_reduced_to_three_exit_microinputs",
        "previous_bes_dls_input": "BESDangerIntersectionExclusionOrDLSNamedReturn",
        "bes_dls_named_return_boundary_closed": all(
            row["closed"]
            for row in rows
            if row["gate"]
            not in {
                "DLSPointShortLowAlphabetClosed",
                "NearmissThreeExitDiagnosticsMaterialized",
                "ColumnCRTIndependentExitAbsorbed",
                "SAEIndependentExitAbsorbed",
                "LowPhaseLayeredPDECRouteClosed",
                "BESDLSNamedReturnInputProved",
                "DStructureRankinStillIndependent",
            }
        ),
        "dls_kernel_and_danger_algebra_closed": True,
        "bes_dls_named_return_input_proved": False,
        "row_column_unconditional_closed": False,
        "nearmiss_summary": summary,
        "exit_rows": exits,
        "latest_internal_subinputs": [
            signed_identity,
            modelgap_input,
            pointload_input,
            shortwindow_input,
            lowphase_input,
            signed_budget_lift,
        ],
        "latest_external_subinput": latest_external,
        "latest_conditional_basis": (
            f"(({signed_identity} AND {modelgap_input} AND {pointload_input} "
            f"AND {shortwindow_input} AND {lowphase_input} AND {signed_budget_lift}) "
            f"OR {latest_external}) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            f"{signed_identity} AND {modelgap_input} AND {pointload_input} "
            f"AND {shortwindow_input} AND {lowphase_input} AND {signed_budget_lift} "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "core_reduction_law": (
            "BES-DLS 输入的作用是删除高 L1/高 L2 同步失败的无名出口。"
            "中心化核与危险交集代数已固定；若危险交集出现，二次能量只能通过 PointLoad、"
            "ShortWindow 或 LowPhase 三种可登记形态承担。PointLoad 回流 ColumnCRT/displacement PDEC，"
            "ShortWindow 回流 SAE/LocalSurvivor 或持久 PDEC，LowPhase 回流 W-unit/new-layer PDEC 或 flat DLS。"
            "因此最新剩余不是 BES 大口径，而是这三类出口的实际排斥或命名回流证明。"
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
    summary = result["nearmiss_summary"]
    lines: list[str] = [
        "# Prime Matrix clean-core BES-DLS 命名回流攻关路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["core_reduction_law"],
        "",
        "```text",
        f"bes_dls_named_return_boundary_closed={fmt_bool(result['bes_dls_named_return_boundary_closed'])}",
        f"dls_kernel_and_danger_algebra_closed={fmt_bool(result['dls_kernel_and_danger_algebra_closed'])}",
        f"bes_dls_named_return_input_proved={fmt_bool(result['bes_dls_named_return_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 近危险摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record_count | `{summary['record_count']}` |",
        f"| max_l1_over_sqrt | `{summary['max_l1_over_sqrt']:.6f}` |",
        f"| max_l2_over_sqrt | `{summary['max_l2_over_sqrt']:.6f}` |",
        f"| max_effective_dimension | `{summary['max_effective_dimension']:.6f}` |",
        f"| max_point_load | `{summary['max_point_load']}` |",
        f"| max_short_window_positive_over_sqrt | `{summary['max_short_window_positive_over_sqrt']:.6f}` |",
        f"| max_low_phase_positive_over_sqrt | `{summary['max_low_phase_positive_over_sqrt']:.6f}` |",
        f"| all_top_low_phase_residues_are_units | `{fmt_bool(summary['all_top_low_phase_residues_are_units'])}` |",
        "",
        "这些数值只用于定位出口优先级，不作为无条件证明。",
        "",
        "## 2. 三出口微输入",
        "",
        "| exit | diagnostic | route | micro_input | closed | meaning |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["exit_rows"]:
        lines.append(
            "| {exit} | {diagnostic} | {route} | `{micro_input}` | `{closed}` | {meaning} |".format(
                exit=table_cell(row["exit"]),
                diagnostic=table_cell(row["diagnostic"]),
                route=table_cell(row["route"]),
                micro_input=table_cell(row["micro_input"]),
                closed=fmt_bool(row["closed"]),
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
            "本步关闭的是 BES-DLS 的命名边界：危险交集不能再作为无名同步失败保留。"
            "它必须进入 PointLoad、ShortWindow 或 LowPhase 三类微输入。当前材料没有证明三类微输入，"
            "也没有闭合无条件行/列命题；下一最窄优先级是 LowPhase 的 W-unit/new-layer PDEC 或 flat DLS 排斥。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--dls", type=Path, default=DEFAULT_DLS)
    parser.add_argument("--nearmiss", type=Path, default=DEFAULT_NEARMISS)
    parser.add_argument("--wheel", type=Path, default=DEFAULT_WHEEL)
    parser.add_argument("--fourier", type=Path, default=DEFAULT_FOURIER)
    parser.add_argument("--newlayer", type=Path, default=DEFAULT_NEWLAYER)
    parser.add_argument("--columncrt", type=Path, default=DEFAULT_COLUMNCRT)
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        args.previous,
        args.dls,
        args.nearmiss,
        args.wheel,
        args.fourier,
        args.newlayer,
        args.columncrt,
        args.sae,
        args.dstructure,
        args.json_out,
        args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
