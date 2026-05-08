#!/usr/bin/env python3
"""Prime Matrix clean-core 几何 Phi/预算桥路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_geometric_phi_budget_bridge_router.py

输出：
  docs/monograph/prime-matrix-clean-core-geometric-phi-budget-bridge-router.json
  docs/monograph/prime-matrix-clean-core-geometric-phi-budget-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-disintegration-automaticity-router.json"
DEFAULT_ATLAS = DOCS / "prime-matrix-closure-input-atlas-router.md"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_CLW = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_PAW = DOCS / "prime-matrix-pcolumn-anchor-wheel-field.md"
DEFAULT_DYN = DOCS / "prime-matrix-dynamic-promoted-rough-capacity.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-geometric-phi-budget-bridge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-geometric-phi-budget-bridge-router.md"


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


def model_rows(atlas: str, clb: str, clw: str, paw: str, dyn: str) -> list[dict[str, Any]]:
    """把几何模型映射到 signed-source 残余字段。"""
    return [
        {
            "model": "cylindrical_completed_line",
            "closed": "R_x\\setminus F_x" in clb and "CLB-FillerBound" in clb,
            "provides": "低素骨架 R_x、未完成斜线补洞 F_x、最终洞 U_x 的确定性覆盖恒等式。",
            "does_not_provide": "signed alpha/delta 源测度或 local factor 符号。",
            "field": "payment_base_map / absolute support skeleton",
        },
        {
            "model": "bottom_pair_deficit",
            "closed": "c=ab" in clb and "BottomDeficitPairBound" in clb,
            "provides": "底部带补洞点 c=a(h-a) 的二次曲线刚性，可作为支撑/重叠预算证书。",
            "does_not_provide": "pre-Cauchy signed summand 生成公式。",
            "field": "support budget / named return",
        },
        {
            "model": "pcolumn_anchor_wheel_field",
            "closed": "PAW-10" in paw and "PAW-5" in paw,
            "provides": "全行骨架 S_W(P,y) 是第一行骨架的圆柱平移，给出统一覆盖-筛除 Phi 基底。",
            "does_not_provide": "Phi_*nu 等于 signed alpha/delta payment-side 系数的恒等式。",
            "field": "geometric Phi base map",
        },
        {
            "model": "dynamic_promoted_rough_capacity",
            "closed": "T_Y<|S_Y|" in dyn or "T_Y(P,y)<" in paw,
            "provides": "把低素斜线提升进轮底座后，剩余高素总命中 T_Y 与粗骨架 S_Y 的容量门。",
            "does_not_provide": "signed 总变差等于覆盖容量的证明。",
            "field": "variation/support budget candidate",
        },
        {
            "model": "layered_wheel_phase_clamp",
            "closed": "LayeredClamp" in clw and "W-unit PDEC" in clw,
            "provides": "若高素补洞在层叠轮单位类中同步，则回流 W-unit PDEC/SAE/ColumnCRT；否则进入分散 KLS 形状。",
            "does_not_provide": "noncanonical signed source 的 branch key 表。",
            "field": "branch budget / phase return",
        },
        {
            "model": "closure_input_atlas",
            "closed": "closure_input_atlas_complete_global_inputs_still_open" in atlas,
            "provides": "所有几何路线已归入命名输入包，不再允许无名逃逸。",
            "does_not_provide": "三包本身的无条件证明。",
            "field": "return discipline",
        },
    ]


def residual_inputs() -> list[dict[str, str]]:
    """列出几何桥之后的两个源侧/预算侧输入。"""
    return [
        {
            "input": "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn",
            "meaning": "定义 actual noncanonical signed alpha/delta 源测度 nu，并证明它沿几何/first-cover Phi 推前为目标 payment-side 系数。",
        },
        {
            "input": "GeometricVariationBranchBudgetCertificateOrNamedReturn",
            "meaning": "用圆柱骨架、P列锚、层叠轮和动态容量证明总变差/绝对支撑/branch key 在预算内，或命名回流。",
        },
    ]


def gate_rows(
    previous: dict[str, Any],
    models: list[dict[str, Any]],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成几何桥判定表。"""
    all_models_closed = all(row["closed"] for row in models)
    return [
        {
            "gate": "PriorSourcePhiBudgetPinned",
            "closed": previous.get("latest_internal_subinput")
            == "ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn",
            "proved": False,
            "meaning": "上一层已把自足硬点压成 actual signed 源测度、Phi 兼容恒等式和预算。",
            "remaining": "判断几何模型能闭合哪些字段。",
        },
        {
            "gate": "GeometricPaymentBaseAvailable",
            "closed": all_models_closed,
            "proved": True,
            "meaning": "斜线圆柱、P列锚和层叠轮筛给出统一覆盖-筛除 Phi 基底和命名回流场。",
            "remaining": "这仍是 unsigned/geometric payment 基底。",
        },
        {
            "gate": "GeometryDoesNotDefineSignedSourceMeasure",
            "closed": True,
            "proved": True,
            "meaning": "几何覆盖只告诉哪些数被哪些斜线命中，不定义 pre-Cauchy signed alpha/delta 源测度。",
            "remaining": "必须提交 actual signed source，或走外部谱输入。",
        },
        {
            "gate": "GeometryDoesNotProvePhiPushforwardIdentity",
            "closed": True,
            "proved": True,
            "meaning": "圆柱/轮筛 Phi 与 signed source 的 Phi_*nu 恒等式不是自动的，需要系数级证明。",
            "remaining": "证明 ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn。",
        },
        {
            "gate": "GeometrySuppliesBudgetAndReturnShape",
            "closed": True,
            "proved": False,
            "meaning": "现有几何模型给出总变差/支撑/branch 预算的候选证书形状和 PDEC/SAE/ColumnCRT 回流出口。",
            "remaining": "仍需正式预算不等式或命名回流证书全集。",
        },
        {
            "gate": "GeometricBridgeSplitsLatestInput",
            "closed": True,
            "proved": True,
            "meaning": "最新输入可分解为 signed source/Phi identity 与 geometric variation/branch budget 两个原子。",
            "remaining": "两个原子当前均未由材料无条件证明。",
        },
        {
            "gate": "ActualSignedSourceMeasurePhiCompatibilityBudgetCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未同时证明 signed source、Phi 恒等式与几何预算。",
            "remaining": (
                "证明 ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn "
                "和 GeometricVariationBranchBudgetCertificateOrNamedReturn。"
            ),
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    atlas_path: Path,
    clb_path: Path,
    clw_path: Path,
    paw_path: Path,
    dyn_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行几何 Phi/预算桥路由。"""
    source_paths = [
        previous_path,
        atlas_path,
        clb_path,
        clw_path,
        paw_path,
        dyn_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    atlas = atlas_path.read_text(encoding="utf-8")
    clb = clb_path.read_text(encoding="utf-8")
    clw = clw_path.read_text(encoding="utf-8")
    paw = paw_path.read_text(encoding="utf-8")
    dyn = dyn_path.read_text(encoding="utf-8")
    dstructure = load_json(dstructure_path)

    models = model_rows(atlas, clb, clw, paw, dyn)
    rows = gate_rows(previous, models, dstructure)
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"]
        not in {
            "ActualSignedSourceMeasurePhiCompatibilityBudgetCurrentCorpusProved",
            "DStructureRankinStillIndependent",
        }
    )
    signed_input = "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn"
    budget_input = "GeometricVariationBranchBudgetCertificateOrNamedReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_geometric_phi_budget_bridge_router",
        "status": "geometric_phi_budget_bridge_closed_signed_source_and_budget_open",
        "previous_input": previous.get("latest_internal_subinput"),
        "geometric_phi_budget_bridge_boundary_closed": boundary_closed,
        "geometric_payment_base_available": True,
        "geometry_defines_signed_source_measure": False,
        "geometry_proves_phi_pushforward_identity": False,
        "geometry_supplies_budget_return_shape": True,
        "actual_signed_source_measure_phi_compatibility_budget_proved": False,
        "row_column_unconditional_closed": False,
        "dstructure_rankin_independent_acceptance_completed": dstructure.get(
            "promotion_package_independently_accepted",
            False,
        ),
        "latest_internal_subinputs": [signed_input, budget_input],
        "latest_external_subinput": latest_external,
        "latest_conditional_basis": (
            f"(({signed_input} AND {budget_input}) OR {latest_external}) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            f"{signed_input} AND {budget_input} "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "geometric_bridge_law": (
            "斜线覆盖、圆柱环绕、第P列锚和层叠轮筛共同给出的是 signed source 的几何基底与预算场："
            "它们定义哪些 payment atoms 可以由哪些斜线/锚相位/轮层命中，并说明容量失败、同步尖峰或 branch 爆炸"
            "必须回流 PDEC/SAE/ColumnCRT/CleanKLS。"
            "但这些几何对象本身不生成 pre-Cauchy signed alpha/delta 源测度，也不自动证明 Phi_*nu 等于"
            "目标 payment-side 系数。因此最新输入被拆为源侧 Phi 恒等式和几何预算/回流证书两个原子。"
        ),
        "plain_conclusion": (
            "几何模型提供了可用的 Phi 基底和预算/回流桥，但不能直接闭合 signed source。"
            "最新自足剩余分裂为 signed source/Phi identity 与 geometric variation/branch budget 两个未证原子。"
        ),
        "model_rows": models,
        "residual_inputs": residual_inputs(),
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
        "# Prime Matrix clean-core 几何 Phi/预算桥路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"geometric_phi_budget_bridge_boundary_closed={fmt_bool(result['geometric_phi_budget_bridge_boundary_closed'])}",
        f"geometric_payment_base_available={fmt_bool(result['geometric_payment_base_available'])}",
        f"geometry_defines_signed_source_measure={fmt_bool(result['geometry_defines_signed_source_measure'])}",
        f"geometry_proves_phi_pushforward_identity={fmt_bool(result['geometry_proves_phi_pushforward_identity'])}",
        f"geometry_supplies_budget_return_shape={fmt_bool(result['geometry_supplies_budget_return_shape'])}",
        f"actual_signed_source_measure_phi_compatibility_budget_proved={fmt_bool(result['actual_signed_source_measure_phi_compatibility_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 几何桥律",
        "",
        result["geometric_bridge_law"],
        "",
        "```text",
        "cylindrical lines + P-column anchor + layered wheel",
        "  => geometric Phi base map + variation/support/branch return shape;",
        "not => signed alpha/delta source measure;",
        "not => Phi_*nu coefficient identity.",
        "```",
        "",
        "## 2. 模型映射表",
        "",
        "| model | closed | provides | does not provide | field |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["model_rows"]:
        lines.append(
            "| {model} | `{closed}` | {provides} | {does_not_provide} | {field} |".format(
                model=table_cell(row["model"]),
                closed=fmt_bool(row["closed"]),
                provides=table_cell(row["provides"]),
                does_not_provide=table_cell(row["does_not_provide"]),
                field=table_cell(row["field"]),
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
            "## 4. 最新原子",
            "",
            "| input | meaning |",
            "| --- | --- |",
        ]
    )
    for row in result["residual_inputs"]:
        lines.append(f"| `{table_cell(row['input'])}` | {table_cell(row['meaning'])} |")
    lines.extend(
        [
            "",
            "## 5. 最新输入基",
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
            "## 6. 当前结论",
            "",
            "本步没有证明 signed source，也没有证明几何预算证书全集。它关闭的是接口层：几何模型已经足以提供",
            "Phi 基底和预算/回流场；剩余必须分别证明 signed source/Phi 恒等式和几何预算证书。",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--atlas", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--clb", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--clw", type=Path, default=DEFAULT_CLW)
    parser.add_argument("--paw", type=Path, default=DEFAULT_PAW)
    parser.add_argument("--dynamic", type=Path, default=DEFAULT_DYN)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        atlas_path=args.atlas,
        clb_path=args.clb,
        clw_path=args.clw,
        paw_path=args.paw,
        dyn_path=args.dynamic,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
