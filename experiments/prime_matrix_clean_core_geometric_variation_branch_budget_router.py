#!/usr/bin/env python3
"""Prime Matrix clean-core 几何变差/分支预算攻关路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_geometric_variation_branch_budget_router.py

输出：
  docs/monograph/prime-matrix-clean-core-geometric-variation-branch-budget-router.json
  docs/monograph/prime-matrix-clean-core-geometric-variation-branch-budget-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-geometric-phi-budget-bridge-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_PAW = DOCS / "prime-matrix-pcolumn-anchor-wheel-field.md"
DEFAULT_DPRC = DOCS / "prime-matrix-dynamic-promoted-rough-capacity.md"
DEFAULT_CLW = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_ATLAS = DOCS / "prime-matrix-closure-input-atlas-router.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.md"


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


def ledger_rows(clb: str, paw: str, dprc: str, clw: str, atlas: str) -> list[dict[str, Any]]:
    """整理几何预算账本的已闭合字段和未闭合字段。"""
    return [
        {
            "ledger": "completed_line_support",
            "available": "CLB-FillerBound" in clb and "R_x\\setminus F_x" in clb,
            "pays": "低素完成骨架、未完成补洞和最终素数洞的支撑分解。",
            "open": "不控制 signed source 的绝对变差。",
        },
        {
            "ledger": "bottom_deficit_pair_curve",
            "available": "c=ab" in clb and "BottomDeficitPairBound" in clb,
            "pays": "底部带补洞必须落在二次曲线 c=a(h-a)，给出局部支撑容量上界。",
            "open": "只覆盖底部带，不能单独支付全局行。",
        },
        {
            "ledger": "pcolumn_anchor_phi_skeleton",
            "available": "PAW-10" in paw and "PAW-5" in paw,
            "pays": "所有行的轮骨架是第一行骨架的圆柱平移，给出统一 payment/Phi 支撑。",
            "open": "锚相位不生成 pre-Cauchy signed branch key。",
        },
        {
            "ledger": "dynamic_promoted_capacity",
            "available": "DPRC(alpha=0.43)" in dprc and "max(0,T-HS)<=3sqrt(S)" in dprc,
            "pays": "把全覆盖压力降为动态粗骨架正偏差平方根界或命名回流。",
            "open": "全局 DPRC 解析不等式仍未证明，只是最窄解析输入。",
        },
        {
            "ledger": "layered_wheel_return",
            "available": "LayeredClamp" in clw and "W-unit PDEC" in clw,
            "pays": "相位同步失败/未稀释峰回流 W-unit PDEC、SAE、ColumnCRT 或 CleanKLS。",
            "open": "未证明所有层的分散峰均由大筛吸收。",
        },
        {
            "ledger": "named_return_discipline",
            "available": "closure_input_atlas_complete_global_inputs_still_open" in atlas,
            "pays": "预算失败不能成为无名第五出口，必须落入命名输入包。",
            "open": "命名输入包本身仍需证明或独立接受。",
        },
    ]


def gate_rows(previous: dict[str, Any], ledgers: list[dict[str, Any]], dstructure: dict[str, Any]) -> list[dict[str, Any]]:
    """生成预算侧判定表。"""
    ledgers_available = all(row["available"] for row in ledgers)
    return [
        {
            "gate": "PreviousBridgeSplitAvailable",
            "closed": "GeometricVariationBranchBudgetCertificateOrNamedReturn"
            in previous.get("latest_internal_subinputs", []),
            "proved": True,
            "meaning": "上一层已把 signed source/Phi identity 与 geometric variation/branch budget 分开。",
            "remaining": "单独攻击预算侧原子。",
        },
        {
            "gate": "GeometryLedgerAlphabetClosed",
            "closed": ledgers_available,
            "proved": True,
            "meaning": "CLB/PAW/DPRC/LayeredWheel/Atlas 已给出支撑、容量、相位和命名回流字母表。",
            "remaining": "这只是 payment/geometric 账本。",
        },
        {
            "gate": "UnsignedSupportBudgetShapeClosed",
            "closed": True,
            "proved": True,
            "meaning": "几何层可把覆盖压力写成 S、T、H、正偏差、轮层峰和回流出口。",
            "remaining": "需证明 DPRC 正偏差平方根界或命名回流。",
        },
        {
            "gate": "DPRCAnalyticCapacityBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出所有 P 的 T_Y<S_Y 或 max(0,T-HS)<=3sqrt(S) 无条件证明。",
            "remaining": "证明 DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn。",
        },
        {
            "gate": "SignedVariationDominatedByGeometryLedger",
            "closed": False,
            "proved": False,
            "meaning": "signed alpha/delta 源的总变差可能在 Phi 纤维内因正负抵消而大于 payment 几何账本。",
            "remaining": "证明 SignedGeometricLedgerVariationBranchLiftAndReturn。",
        },
        {
            "gate": "BranchKeyMultiplicityBudgetProved",
            "closed": False,
            "proved": False,
            "meaning": "几何标签 q,m,W,phase 可登记，但 actual source branch key 的 polylog/K6 复杂度尚未由几何自动推出。",
            "remaining": "与 signed variation lift 同时证明，或把 branch 爆炸命名回流。",
        },
        {
            "gate": "GeometricVariationBranchBudgetCertificateProved",
            "closed": False,
            "proved": False,
            "meaning": "预算侧原子未闭合；它被压成一个几何解析锁和一个 signed 提升锁。",
            "remaining": (
                "DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND "
                "SignedGeometricLedgerVariationBranchLiftAndReturn"
            ),
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧和预算侧完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    clb_path: Path,
    paw_path: Path,
    dprc_path: Path,
    clw_path: Path,
    atlas_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行几何变差/分支预算攻关路由。"""
    source_paths = [
        previous_path,
        clb_path,
        paw_path,
        dprc_path,
        clw_path,
        atlas_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    clb = clb_path.read_text(encoding="utf-8")
    paw = paw_path.read_text(encoding="utf-8")
    dprc = dprc_path.read_text(encoding="utf-8")
    clw = clw_path.read_text(encoding="utf-8")
    atlas = atlas_path.read_text(encoding="utf-8")
    dstructure = load_json(dstructure_path)

    ledgers = ledger_rows(clb, paw, dprc, clw, atlas)
    rows = gate_rows(previous, ledgers, dstructure)
    signed_identity = "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn"
    dprc_input = "DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn"
    signed_budget_lift = "SignedGeometricLedgerVariationBranchLiftAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_geometric_variation_branch_budget_router",
        "status": "geometric_budget_reduced_to_dprc_and_signed_variation_lift",
        "previous_budget_input": "GeometricVariationBranchBudgetCertificateOrNamedReturn",
        "geometric_budget_attack_boundary_closed": all(
            row["closed"]
            for row in rows
            if row["gate"]
            not in {
                "DPRCAnalyticCapacityBoundProved",
                "SignedVariationDominatedByGeometryLedger",
                "BranchKeyMultiplicityBudgetProved",
                "GeometricVariationBranchBudgetCertificateProved",
                "DStructureRankinStillIndependent",
            }
        ),
        "geometry_ledger_alphabet_closed": all(row["available"] for row in ledgers),
        "dprc_analytic_capacity_bound_proved": False,
        "signed_variation_branch_lift_proved": False,
        "geometric_variation_branch_budget_certificate_proved": False,
        "row_column_unconditional_closed": False,
        "latest_internal_subinputs": [signed_identity, dprc_input, signed_budget_lift],
        "latest_external_subinput": latest_external,
        "latest_conditional_basis": (
            f"(({signed_identity} AND {dprc_input} AND {signed_budget_lift}) "
            f"OR {latest_external}) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            f"{signed_identity} AND {dprc_input} AND {signed_budget_lift} "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "core_reduction_law": (
            "几何模型已经闭合 payment 支撑字母表和命名回流字母表。"
            "预算侧真正剩余不是再找一个固定轮或固定常数，而是两把锁："
            "第一，动态提升轮的正偏差必须满足 DPRC 平方根界，或在某层回流 PDEC/SAE/ColumnCRT/CleanKLS；"
            "第二，actual signed source 的总变差和 branch key 复杂度必须被这个几何账本支配，"
            "不能在 Phi 纤维内靠正负抵消隐藏出超预算质量。"
        ),
        "ledger_rows": ledgers,
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
    lines: list[str] = [
        "# Prime Matrix clean-core 几何变差/分支预算攻关路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["core_reduction_law"],
        "",
        "```text",
        f"geometric_budget_attack_boundary_closed={fmt_bool(result['geometric_budget_attack_boundary_closed'])}",
        f"geometry_ledger_alphabet_closed={fmt_bool(result['geometry_ledger_alphabet_closed'])}",
        f"dprc_analytic_capacity_bound_proved={fmt_bool(result['dprc_analytic_capacity_bound_proved'])}",
        f"signed_variation_branch_lift_proved={fmt_bool(result['signed_variation_branch_lift_proved'])}",
        f"geometric_variation_branch_budget_certificate_proved={fmt_bool(result['geometric_variation_branch_budget_certificate_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 预算侧核心约化律",
        "",
        "几何预算不是一个单纯计数不等式。它由两个不同层次组成：",
        "",
        "- payment/geometric 层：支撑集合、覆盖总命中、轮层相位、命名回流出口；",
        "- signed-source 层：pre-Cauchy `alpha/delta` 源测度的总变差、branch key、sign/local factor 和 `Phi` 纤维内绝对质量。",
        "",
        "第一层已经由斜线圆柱、P列锚、动态提升轮和层叠轮筛形成统一账本；第二层不能由 unsigned 几何自动推出。",
        "",
        "因此预算原子被压成：",
        "",
        "```text",
        "GeometricVariationBranchBudgetCertificateOrNamedReturn",
        "  => DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn",
        "     AND SignedGeometricLedgerVariationBranchLiftAndReturn。",
        "```",
        "",
        "## 2. 几何账本表",
        "",
        "| ledger | available | pays | open |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["ledger_rows"]:
        lines.append(
            "| {ledger} | `{available}` | {pays} | {open} |".format(
                ledger=table_cell(row["ledger"]),
                available=fmt_bool(row["available"]),
                pays=table_cell(row["pays"]),
                open=table_cell(row["open"]),
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
            "本步关闭的是预算侧的接口误差：几何支撑和回流字母表已经足够清楚，不能再把剩余归因于"
            "“斜线/轮筛模型未建好”。真正剩余是 DPRC 正偏差解析界，以及 actual signed source 的"
            "变差/branch 提升纪律。当前材料仍未证明这些输入，也没有闭合无条件行/列命题。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--clb", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--paw", type=Path, default=DEFAULT_PAW)
    parser.add_argument("--dprc", type=Path, default=DEFAULT_DPRC)
    parser.add_argument("--clw", type=Path, default=DEFAULT_CLW)
    parser.add_argument("--atlas", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        args.previous,
        args.clb,
        args.paw,
        args.dprc,
        args.clw,
        args.atlas,
        args.dstructure,
        args.json_out,
        args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
