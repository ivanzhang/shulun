#!/usr/bin/env python3
"""闭合 ruled-surface 包中的正特征次数截断常数。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_positive_characteristic_cutoff_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-ruled-surface-component-accounting-router.json"
ELEMENTARY = MONO / "prime-matrix-strict-rks23-line-intersection-elementary-surface-layer-router.json"

SOURCE_FILES = [PREVIOUS, ELEMENTARY]

STRUCTURE_PACK = "SelfContainedFlecnodeAndRuledSurfaceLineTheoremPackWithDegreeLessThanCharacteristic"
SINGLY_RULED = "SelfContainedSinglyRuledSurfaceExceptionalLineTheorem"
NON_RULED = "SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem"
CHAR_CUTOFF = "ExplicitDegreeLessThanCharacteristicCutoffForKollarLineCounting"
TWO_STRUCTURE_ATOMS = "SelfContainedSinglyRuledAndNonRuledFlecnodeStructureTheorems"
BIPARTITE_LINE_ATOM = "SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage"
POINT_PLANE_ATOM = "SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof"
RNRS_INPUT = "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"

C0_NUMERATOR = 1
C0_DENOMINATOR = 54


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


def interpolation_degree(n: int) -> int:
    """显式插值次数：保证三变量多项式空间维数超过直线限制数。"""
    if n <= 0:
        return 0
    return math.ceil(math.sqrt(6 * n))


def cutoff_holds_for_prime_characteristic(p: int) -> bool:
    """有限检查辅助：在 |L|<=floor(p^2/54) 下验证 D<p。"""
    n_max = (p * p) // C0_DENOMINATOR
    return interpolation_degree(n_max) < p


def finite_cutoff_audit(limit: int = 10000) -> dict[str, Any]:
    """对小正特征做机械审计；一般证明见证书文本。"""
    failures = [p for p in range(2, limit + 1) if not cutoff_holds_for_prime_characteristic(p)]
    return {
        "checked_range": f"2<=p<={limit}",
        "failures": failures,
        "passed": not failures,
    }


def build_result() -> dict[str, Any]:
    """构造正特征截断证书。"""
    previous = load_json(PREVIOUS)
    elementary = load_json(ELEMENTARY)

    previous_surface_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == STRUCTURE_PACK,
            previous.get("explicit_degree_less_than_characteristic_constant_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            elementary.get("elementary_surface_layer_closed") is True,
        ]
    )
    interpolation_degree_formula_imported = elementary.get("interpolation_surface_through_all_lines_closed") is True
    explicit_cutoff_constant_closed = previous_surface_frontier_ready and interpolation_degree_formula_imported
    finite_audit = finite_cutoff_audit()
    mechanical_cutoff_audit_passed = finite_audit["passed"]

    singly_ruled_exceptional_line_theorem_closed = False
    non_ruled_line_intersection_theorem_closed = False
    ruled_and_nonruled_component_line_count_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    cutoff_proof = {
        "explicit_constant": f"c0={C0_NUMERATOR}/{C0_DENOMINATOR}",
        "hypothesis": "|L|<=p^2/54 in characteristic p>0",
        "degree_choice": "D=ceil(sqrt(6|L|))",
        "interpolation_inequality": "binomial(D+3,3)>(D+1)|L|, because (D+2)(D+3)/6>|L|",
        "degree_bound": "D<=ceil(p/3)<p under |L|<=p^2/54; p=2 is trivial since |L|=0",
        "consequence": "every irreducible component degree d_i<=D is also <p",
        "scope": "this closes the explicit positive-characteristic cutoff for the internal version; it does not prove the ruled/non-ruled structure theorems themselves",
    }

    remaining_atoms = [
        {
            "atom": SINGLY_RULED,
            "closed": False,
            "why_remaining": "requires an internal proof of the exceptional-line theorem for singly ruled surfaces",
        },
        {
            "atom": NON_RULED,
            "closed": False,
            "why_remaining": "requires an internal flecnode/Cayley-Salmon style proof of O(d^3) line intersections on non-ruled surfaces",
        },
    ]

    rows = [
        row(
            "PreviousFlecnodeStructureFrontierReady",
            previous_surface_frontier_ready,
            True,
            "上一证书已把剩余压成 singly-ruled、non-ruled 和正特征截断三个原子。",
            STRUCTURE_PACK,
        ),
        row(
            "InterpolationDegreeFormulaImported",
            interpolation_degree_formula_imported,
            True,
            "已从初等曲面层导入 D=ceil(sqrt(6|L|)) 的显式插值次数。",
            "explicit interpolation degree",
        ),
        row(
            "ExplicitDegreeLessThanCharacteristicConstantClosed",
            explicit_cutoff_constant_closed,
            True,
            "取 c0=1/54，则 |L|<=c0 p^2 保证插值曲面及其分量次数均小于 p。",
            CHAR_CUTOFF,
        ),
        row(
            "FiniteCutoffAuditPassed",
            mechanical_cutoff_audit_passed,
            True,
            "对小正特征范围机械核验 D<p，无失败样本；一般不等式已在证书中给出。",
            "finite audit closed",
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            False,
            "尚未作者侧证明 singly-ruled 曲面异常线结构。",
            SINGLY_RULED,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "尚未作者侧证明非 ruled 曲面 O(d^3) 线交点界。",
            NON_RULED,
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_and_nonruled_component_line_count_closed,
            False,
            "两个曲面结构定理未内联前，ruled/non-ruled 总包仍未闭合。",
            TWO_STRUCTURE_ATOMS,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "正特征截断已闭合，但 Kollár/Guth-Katz 曲面结构包仍差两个定理。",
            TWO_STRUCTURE_ATOMS,
        ),
        row(
            "SelfContainedBipartiteLineIntersectionBoundClosed",
            self_contained_bipartite_line_intersection_bound_closed,
            False,
            "二分线交点界仍依赖曲面结构包。",
            BIPARTITE_LINE_ATOM,
        ),
        row(
            "SelfContainedPointPlaneIncidenceProofClosed",
            self_contained_point_plane_incidence_proof_closed,
            False,
            "点-平面 incidence 仍依赖二分线交点界。",
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
            "本步只闭合正特征次数截断；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_positive_characteristic_cutoff_router",
        "status": "positive_characteristic_degree_cutoff_closed_remaining_two_surface_structure_theorems",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_surface_frontier_ready": previous_surface_frontier_ready,
        "interpolation_degree_formula_imported": interpolation_degree_formula_imported,
        "explicit_degree_less_than_characteristic_constant_closed": explicit_cutoff_constant_closed,
        "mechanical_cutoff_audit_passed": mechanical_cutoff_audit_passed,
        "c0_numerator": C0_NUMERATOR,
        "c0_denominator": C0_DENOMINATOR,
        "singly_ruled_exceptional_line_theorem_closed": singly_ruled_exceptional_line_theorem_closed,
        "non_ruled_line_intersection_theorem_closed": non_ruled_line_intersection_theorem_closed,
        "ruled_and_nonruled_component_line_count_closed": ruled_and_nonruled_component_line_count_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": TWO_STRUCTURE_ATOMS,
        "next_required_input": f"{SINGLY_RULED} + {NON_RULED}",
        "cutoff_proof": cutoff_proof,
        "finite_cutoff_audit": finite_audit,
        "remaining_atoms": remaining_atoms,
        "plain_conclusion": (
            "当前唯一内部自足线继续下钻并关闭一个真实原子：正特征 degree<p 截断已显式化。"
            "取插值次数 D=ceil(sqrt(6|L|))，并在正特征 p 中使用 |L|<=p^2/54，"
            "即可保证 D<p，因而所有不可约分量次数也小于 p。"
            "这样剩余不再包含正特征隐常数，只剩两个曲面结构定理："
            "singly-ruled 异常线定理与 non-ruled 曲面 O(d^3) 线交点定理。"
            "这两个定理未内联前，row_column_unconditional_closed 仍保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 正特征截断证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(
        "explicit_degree_less_than_characteristic_constant_closed="
        f"{fmt_bool(result['explicit_degree_less_than_characteristic_constant_closed'])}"
    )
    lines.append(
        "singly_ruled_exceptional_line_theorem_closed="
        f"{fmt_bool(result['singly_ruled_exceptional_line_theorem_closed'])}"
    )
    lines.append(
        "non_ruled_line_intersection_theorem_closed="
        f"{fmt_bool(result['non_ruled_line_intersection_theorem_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 截断证明")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for field, value in result["cutoff_proof"].items():
        lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 有限核验")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for field, value in result["finite_cutoff_audit"].items():
        lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 3. 剩余曲面原子")
    lines.append("")
    lines.append("| atom | closed | why_remaining |")
    lines.append("| --- | --- | --- |")
    for item in result["remaining_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{fmt_bool(item['closed'])}` | "
            f"{table_cell(item['why_remaining'])} |"
        )
    lines.append("")
    lines.append("## 4. 判定表")
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
    lines.append("## 5. 下一真正自足目标")
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
    print(
        "explicit_degree_less_than_characteristic_constant_closed="
        f"{fmt_bool(result['explicit_degree_less_than_characteristic_constant_closed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
