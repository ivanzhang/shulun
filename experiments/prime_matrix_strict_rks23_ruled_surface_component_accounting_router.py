#!/usr/bin/env python3
"""把 ruled/non-ruled 剩余压成精确代数曲面结构定理包。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_ruled_surface_component_accounting_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-ruled-surface-component-accounting-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-ruled-surface-component-accounting-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-ruled-surface-component-accounting-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-line-intersection-elementary-surface-layer-router.json"
DEZEEUW = MONO / "prime-matrix-strict-rks23-point-plane-dezeeuw-line-intersection-router.json"

SOURCE_FILES = [PREVIOUS, DEZEEUW]

RULED_REMAINING = "SelfContainedRuledAndNonRuledSurfaceLineCountingWithPositiveCharacteristicCutoff"
STRUCTURE_PACK = "SelfContainedFlecnodeAndRuledSurfaceLineTheoremPackWithDegreeLessThanCharacteristic"
SINGLY_RULED = "SelfContainedSinglyRuledSurfaceExceptionalLineTheorem"
NON_RULED = "SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem"
CHAR_CUTOFF = "ExplicitDegreeLessThanCharacteristicCutoffForKollarLineCounting"
BIPARTITE_LINE_ATOM = "SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage"
POINT_PLANE_ATOM = "SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof"
RNRS_INPUT = "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造曲面分量记账证书。"""
    previous = load_json(PREVIOUS)
    dezeeuw = load_json(DEZEEUW)

    previous_ruled_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == RULED_REMAINING,
            previous.get("elementary_surface_layer_closed") is True,
            previous.get("ruled_and_nonruled_component_line_count_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            dezeeuw.get("next_direct_attack_target") == BIPARTITE_LINE_ATOM,
        ]
    )

    component_assignment_closed = previous_ruled_frontier_ready
    singly_ruled_accounting_reduction_closed = previous_ruled_frontier_ready
    non_ruled_accounting_reduction_closed = previous_ruled_frontier_ready
    degree_sum_ledger_closed = previous_ruled_frontier_ready
    positive_characteristic_cutoff_reduced_to_explicit_degree_constant = previous_ruled_frontier_ready

    # 这些是真正未内联的代数几何结构定理，不能伪称作者侧闭合。
    singly_ruled_exceptional_line_theorem_closed = False
    non_ruled_line_intersection_theorem_closed = False
    explicit_degree_less_than_characteristic_constant_closed = False
    ruled_and_nonruled_component_line_count_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    component_accounting = {
        "decomposition": "write the interpolation surface S as irreducible components S_i with degrees d_i",
        "assignment_rule": "each line contained in S is assigned to one component containing it, e.g. the smallest-index component",
        "mass_ledger": "sum_i |L_i|=|L| and sum_i |M_i|<=|M|",
        "degree_ledger": "sum_i d_i<=deg(S)=O(|L|^(1/2))",
        "why_closed": "this is a finite bookkeeping step after the elementary surface layer",
    }

    singly_ruled_accounting = {
        "conditional_input": SINGLY_RULED,
        "expected_content": "on a singly ruled irreducible component, at most O(1) exceptional lines meet infinitely many component lines; all other contained lines meet O(d_i) contained lines",
        "exceptional_charge": "O(1) exceptional lines per component contribute O(max(|L_i|,|M_i|)), summing harmlessly under |L|<=|M| and degree/component accounting",
        "ordinary_charge": "ordinary lines contribute O(d_i|L_i|), and O(sum_i d_i |L_i|)<=O(deg(S)|L|)<=O(|L|^(1/2)|M|)",
        "closed_scope": "the summation and absorption are closed once the exceptional-line theorem is available",
    }

    non_ruled_accounting = {
        "conditional_input": NON_RULED,
        "expected_content": "a non-ruled irreducible surface of degree d_i has O(d_i^3) line-line intersection points among contained lines",
        "component_charge": "sum_i O(d_i^3)<=O((sum_i d_i)^3)",
        "absorption": "deg(S)^3=O(|L|^(3/2))<=O(|L|^(1/2)|M|) because |L|<=|M|",
        "closed_scope": "the summation and target absorption are closed once the non-ruled O(d^3) theorem is available",
    }

    characteristic_cutoff = {
        "degree_relation": "the interpolation degree D is O(|L|^(1/2))",
        "needed_condition": "the non-ruled line-count theorem in positive characteristic requires component degree d_i<char(F)",
        "current_reduction": "it is enough to impose or extract an explicit constant c0 with |L|<=c0*p^2 so D<p",
        "not_yet_closed": "the manuscript has not fixed the absolute c0 hidden in the O(|L|=O(p^2)) condition",
    }

    final_surface_atoms = [
        {
            "atom": SINGLY_RULED,
            "status": "open",
            "needed_for": "singly ruled component contribution",
        },
        {
            "atom": NON_RULED,
            "status": "open",
            "needed_for": "non-ruled component contribution",
        },
        {
            "atom": CHAR_CUTOFF,
            "status": "open",
            "needed_for": "positive characteristic self-contained statement with explicit size constant",
        },
    ]

    rows = [
        row(
            "PreviousRuledFrontierReady",
            previous_ruled_frontier_ready,
            True,
            "上一证书已把剩余固定为 ruled/non-ruled 曲面线计数与正特征截断。",
            RULED_REMAINING,
        ),
        row(
            "ComponentAssignmentAndMassLedgerClosed",
            component_assignment_closed,
            True,
            "把曲面分解为不可约分量并将每条直线唯一分配，质量账本闭合。",
            "component accounting closed",
        ),
        row(
            "DegreeSumLedgerClosed",
            degree_sum_ledger_closed,
            True,
            "分量次数和由插值曲面总次数控制。",
            "degree ledger closed",
        ),
        row(
            "SinglyRuledContributionAccountingReduced",
            singly_ruled_accounting_reduction_closed,
            True,
            "一旦有 singly-ruled 异常线定理，该分量贡献可吸收到目标主项。",
            SINGLY_RULED,
        ),
        row(
            "NonRuledContributionAccountingReduced",
            non_ruled_accounting_reduction_closed,
            True,
            "一旦有非 ruled O(d^3) 线交点定理，该分量贡献可吸收到目标主项。",
            NON_RULED,
        ),
        row(
            "PositiveCharacteristicCutoffReducedToExplicitDegreeConstant",
            positive_characteristic_cutoff_reduced_to_explicit_degree_constant,
            True,
            "正特征条件已压成显式 c0：需保证插值曲面次数小于 p。",
            CHAR_CUTOFF,
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            False,
            "尚未作者侧证明 singly-ruled 曲面只有 O(1) 特殊线及普通线 O(d) 相交。",
            SINGLY_RULED,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "尚未作者侧证明非 ruled 曲面内部线交点 O(d^3)。",
            NON_RULED,
        ),
        row(
            "ExplicitDegreeLessThanCharacteristicConstantClosed",
            explicit_degree_less_than_characteristic_constant_closed,
            False,
            "正特征版本仍需固定 |L|<=c0 p^2 的显式常数。",
            CHAR_CUTOFF,
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_and_nonruled_component_line_count_closed,
            False,
            "曲面结构定理包未内联前，ruled/non-ruled 总包不闭合。",
            STRUCTURE_PACK,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "Kollár/Guth-Katz 曲面结构包仍是唯一内部自足剩余。",
            STRUCTURE_PACK,
        ),
        row(
            "SelfContainedBipartiteLineIntersectionBoundClosed",
            self_contained_bipartite_line_intersection_bound_closed,
            False,
            "线交点界依赖曲面结构包，仍未闭合。",
            BIPARTITE_LINE_ATOM,
        ),
        row(
            "SelfContainedPointPlaneIncidenceProofClosed",
            self_contained_point_plane_incidence_proof_closed,
            False,
            "点-平面 incidence 依赖线交点界，仍未闭合。",
            POINT_PLANE_ATOM,
        ),
        row(
            RNRS_INPUT,
            self_contained_rnrs_rudnev_proof_closed,
            False,
            "RNRS/Rudnev 输入仍未作者侧自足闭合。",
            POINT_PLANE_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "本步只闭合分量记账和条件吸收；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_ruled_surface_component_accounting_router",
        "status": "ruled_surface_component_accounting_closed_remaining_flecnode_structure_theorem_pack",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_ruled_frontier_ready": previous_ruled_frontier_ready,
        "component_assignment_closed": component_assignment_closed,
        "singly_ruled_accounting_reduction_closed": singly_ruled_accounting_reduction_closed,
        "non_ruled_accounting_reduction_closed": non_ruled_accounting_reduction_closed,
        "degree_sum_ledger_closed": degree_sum_ledger_closed,
        "positive_characteristic_cutoff_reduced_to_explicit_degree_constant": positive_characteristic_cutoff_reduced_to_explicit_degree_constant,
        "singly_ruled_exceptional_line_theorem_closed": singly_ruled_exceptional_line_theorem_closed,
        "non_ruled_line_intersection_theorem_closed": non_ruled_line_intersection_theorem_closed,
        "explicit_degree_less_than_characteristic_constant_closed": explicit_degree_less_than_characteristic_constant_closed,
        "ruled_and_nonruled_component_line_count_closed": ruled_and_nonruled_component_line_count_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": STRUCTURE_PACK,
        "next_required_input": "SinglyRuledExceptionalLineTheorem + NonRuledFlecnodeLineIntersectionO_d3 + explicit c0 p^2 cutoff",
        "component_accounting": component_accounting,
        "singly_ruled_accounting": singly_ruled_accounting,
        "non_ruled_accounting": non_ruled_accounting,
        "characteristic_cutoff": characteristic_cutoff,
        "final_surface_atoms": final_surface_atoms,
        "plain_conclusion": (
            "当前唯一内部自足线继续压窄：ruled/non-ruled 剩余中的分量分配、次数求和、"
            "singly-ruled 条件吸收、non-ruled 条件吸收都已闭合为账本。"
            "真正剩余不再是整个线交点界，而是三个精确代数曲面输入："
            "singly-ruled 异常线定理、非 ruled 曲面的 O(d^3) 线交点定理、"
            "以及正特征下 degree<p 的显式 c0 截断。"
            "这些结构定理未内联前，row_column_unconditional_closed 仍必须保持 false。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "source_hashes": source_hashes(),
    }
    return result


def write_markdown(result: dict[str, Any]) -> str:
    """生成 Markdown 审计文件。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 ruled 曲面分量记账证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(f"component_assignment_closed={fmt_bool(result['component_assignment_closed'])}")
    lines.append(
        "singly_ruled_accounting_reduction_closed="
        f"{fmt_bool(result['singly_ruled_accounting_reduction_closed'])}"
    )
    lines.append(
        "non_ruled_accounting_reduction_closed="
        f"{fmt_bool(result['non_ruled_accounting_reduction_closed'])}"
    )
    lines.append(
        "ruled_and_nonruled_component_line_count_closed="
        f"{fmt_bool(result['ruled_and_nonruled_component_line_count_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. 分量记账", "component_accounting"),
        ("2. singly-ruled 条件吸收", "singly_ruled_accounting"),
        ("3. non-ruled 条件吸收", "non_ruled_accounting"),
        ("4. 正特征截断", "characteristic_cutoff"),
    ]
    for title, key in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| field | value |")
        lines.append("| --- | --- |")
        for field, value in result[key].items():
            lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
        lines.append("")
    lines.append("## 5. 最终曲面原子")
    lines.append("")
    lines.append("| atom | status | needed_for |")
    lines.append("| --- | --- | --- |")
    for item in result["final_surface_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{table_cell(item['status'])}` | "
            f"{table_cell(item['needed_for'])} |"
        )
    lines.append("")
    lines.append("## 6. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | "
            f"{table_cell(item['remaining'])} |"
        )
    lines.append("")
    lines.append("## 7. 下一真正自足目标")
    lines.append("")
    lines.append("```text")
    lines.append(str(result["next_direct_attack_target"]))
    lines.append(str(result["next_required_input"]))
    lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"component_assignment_closed={fmt_bool(result['component_assignment_closed'])}")
    print(f"ruled_and_nonruled_component_line_count_closed={fmt_bool(result['ruled_and_nonruled_component_line_count_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
