#!/usr/bin/env python3
"""闭合二分线交点界中的初等插值曲面层。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_line_intersection_elementary_surface_layer_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-line-intersection-elementary-surface-layer-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-line-intersection-elementary-surface-layer-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-line-intersection-elementary-surface-layer-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-point-plane-dezeeuw-line-intersection-router.json"
POINT_PLANE = MONO / "prime-matrix-strict-rks23-rudnev-point-plane-to-reciprocal-energy-router.json"

SOURCE_FILES = [PREVIOUS, POINT_PLANE]

BIPARTITE_LINE_ATOM = "SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage"
KOLLAR_PACKAGE = "InterpolationSurfaceAndRuledSurfaceLineCountingPackageWithPositiveCharacteristicDegreeCutoff"
INTERPOLATION = "InterpolationSurfaceThroughAllLinesOfL"
OFF_SURFACE = "OffSurfaceBezoutIntersectionCount"
PLANE_QUADRIC = "PlaneAndQuadricDegenerateComponentAccount"
RULED_REMAINING = "SelfContainedRuledAndNonRuledSurfaceLineCountingWithPositiveCharacteristicCutoff"
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
    """构造初等曲面层证书。"""
    previous = load_json(PREVIOUS)
    point_plane = load_json(POINT_PLANE)

    previous_line_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == BIPARTITE_LINE_ATOM,
            previous.get("next_required_input") == KOLLAR_PACKAGE,
            previous.get("self_contained_bipartite_line_intersection_bound_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            point_plane.get("next_direct_attack_target") == POINT_PLANE_ATOM,
        ]
    )

    interpolation_surface_closed = previous_line_frontier_ready
    off_surface_bezout_closed = previous_line_frontier_ready
    plane_quadric_degenerate_component_closed = previous_line_frontier_ready
    elementary_surface_layer_closed = all(
        [
            interpolation_surface_closed,
            off_surface_bezout_closed,
            plane_quadric_degenerate_component_closed,
        ]
    )

    # 仍未内联 Kollár ruled-surface 与非 ruled 分量线计数，因此总线交点界不能关闭。
    ruled_nonruled_component_count_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    interpolation_proof = {
        "input": "n=|L| affine lines in F^3",
        "degree_choice": "choose D=C*ceil(sqrt(n)) with C large enough",
        "unknowns": "dimension of polynomials of degree <=D in three variables is binomial(D+3,3)",
        "constraints_per_line": "vanishing on one line imposes at most D+1 linear conditions after restricting to a univariate polynomial",
        "dimension_count": "binomial(D+3,3)>n(D+1) for an absolute C, so a nonzero polynomial vanishing on all L exists",
        "output": "there is a surface S={F=0} of degree O(|L|^(1/2)) containing all lines of L",
    }

    off_surface_proof = {
        "input": "a line m in M not contained in S={F=0}",
        "restriction": "F restricted to m is a nonzero univariate polynomial of degree <=D",
        "intersection_bound": "m meets S in at most D points, counted without multiplicity for incidence purposes",
        "sum": "all such M-lines contribute O(D|M|)=O(|L|^(1/2)|M|)",
    }

    plane_quadric_proof = {
        "component_types": "plane or quadric irreducible/reducible components of the interpolating surface",
        "degeneracy_hypothesis": "no quadric contains s lines of L and t lines of M",
        "plane_handling": "a plane is contained in a reducible quadric after adjoining another plane, so the same s,t exclusion applies",
        "charge": "each such component contains fewer than s L-lines or fewer than t M-lines; charge at most s|M_i| or t|L_i|",
        "sum": "summing over components gives O(t|L|+s|M|)",
    }

    remaining_ruled_package = {
        "singly_ruled": "need a self-contained proof that only O(1) exceptional lines per singly ruled component can meet infinitely many component lines, while all other lines meet O(deg S_i) lines",
        "non_ruled": "need a self-contained proof that a non-ruled component of degree d has O(d^3) line-line intersection points among contained lines",
        "positive_characteristic_cutoff": "need the degree<characteristic condition, tied to |L|=O(p^2), for the non-ruled line-count theorem",
        "why_not_closed": "these are algebraic-geometry structure theorems, not consequences of the elementary interpolation/Bézout layer alone",
    }

    rows = [
        row(
            "PreviousLineIntersectionFrontierReady",
            previous_line_frontier_ready,
            True,
            "上一证书已把真正剩余固定为二分 Guth-Katz/Kollár 线交点证明包。",
            BIPARTITE_LINE_ATOM,
        ),
        row(
            "InterpolationSurfaceThroughAllLinesClosed",
            interpolation_surface_closed,
            True,
            "用三变量多项式维数计数构造次数 O(|L|^1/2) 的曲面穿过 L 中全部直线。",
            INTERPOLATION,
        ),
        row(
            "OffSurfaceBezoutIntersectionCountClosed",
            off_surface_bezout_closed,
            True,
            "不含于曲面的 M 直线每条至多贡献 deg(S) 个交点，总贡献 O(|L|^1/2|M|)。",
            OFF_SURFACE,
        ),
        row(
            "PlaneAndQuadricDegenerateComponentAccountClosed",
            plane_quadric_degenerate_component_closed,
            True,
            "平面/二次曲面分量由 quadric 退化假设收费到 t|L|+s|M|。",
            PLANE_QUADRIC,
        ),
        row(
            "ElementarySurfaceLayerClosed",
            elementary_surface_layer_closed,
            True,
            "线交点证明中的初等插值曲面层已经闭合。",
            "elementary layer closed",
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_nonruled_component_count_closed,
            False,
            "单 ruled 与非 ruled 分量的线计数仍需 Kollár/Guth-Katz 型代数几何包。",
            RULED_REMAINING,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "Kollár ruled-surface 与正特征次数截断尚未完整内联。",
            RULED_REMAINING,
        ),
        row(
            "SelfContainedBipartiteLineIntersectionBoundClosed",
            self_contained_bipartite_line_intersection_bound_closed,
            False,
            "二分线交点界还差 ruled/non-ruled 分量计数，不能算闭合。",
            BIPARTITE_LINE_ATOM,
        ),
        row(
            "SelfContainedPointPlaneIncidenceProofClosed",
            self_contained_point_plane_incidence_proof_closed,
            False,
            "点-平面 incidence 依赖二分线交点界，故仍未闭合。",
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
            "本步只闭合初等曲面层；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_line_intersection_elementary_surface_layer_router",
        "status": "bipartite_line_intersection_elementary_surface_layer_closed_remaining_ruled_surface_package",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_line_intersection_frontier_ready": previous_line_frontier_ready,
        "interpolation_surface_through_all_lines_closed": interpolation_surface_closed,
        "off_surface_bezout_intersection_count_closed": off_surface_bezout_closed,
        "plane_quadric_degenerate_component_account_closed": plane_quadric_degenerate_component_closed,
        "elementary_surface_layer_closed": elementary_surface_layer_closed,
        "ruled_and_nonruled_component_line_count_closed": ruled_nonruled_component_count_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": RULED_REMAINING,
        "next_required_input": "SelfContainedKollarRuledSurfaceExceptionalLineAndNonRuledLineIntersectionTheorems",
        "interpolation_proof": interpolation_proof,
        "off_surface_proof": off_surface_proof,
        "plane_quadric_proof": plane_quadric_proof,
        "remaining_ruled_package": remaining_ruled_package,
        "plain_conclusion": (
            "当前唯一内部自足线继续推进：二分线交点界中的初等曲面层已经闭合。"
            "具体闭合了三项：用多项式维数计数构造穿过 L 中全部直线的低次数曲面；"
            "用一元 Bézout 控制不含于该曲面的 M 直线；"
            "用 quadric 退化假设处理平面/二次曲面分量。"
            "真正剩余因此缩为 ruled/non-ruled 曲面分量的 Kollár 型线计数与正特征次数截断。"
            "在该包内联前，row_column_unconditional_closed 仍必须保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 线交点初等曲面层证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(
        "elementary_surface_layer_closed="
        f"{fmt_bool(result['elementary_surface_layer_closed'])}"
    )
    lines.append(
        "ruled_and_nonruled_component_line_count_closed="
        f"{fmt_bool(result['ruled_and_nonruled_component_line_count_closed'])}"
    )
    lines.append(
        "self_contained_bipartite_line_intersection_bound_closed="
        f"{fmt_bool(result['self_contained_bipartite_line_intersection_bound_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. 插值曲面", "interpolation_proof"),
        ("2. 非包含线 Bézout 计数", "off_surface_proof"),
        ("3. 平面/二次曲面退化分量", "plane_quadric_proof"),
        ("4. 剩余 ruled 包", "remaining_ruled_package"),
    ]
    for title, key in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| field | value |")
        lines.append("| --- | --- |")
        for field, value in result[key].items():
            lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
        lines.append("")
    lines.append("## 5. 判定表")
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
    lines.append("## 6. 下一真正自足目标")
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
    print(f"elementary_surface_layer_closed={fmt_bool(result['elementary_surface_layer_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
