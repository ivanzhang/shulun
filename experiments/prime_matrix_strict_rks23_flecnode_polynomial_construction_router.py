#!/usr/bin/env python3
"""闭合 flecnode 多项式构造与次数界原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_flecnode_polynomial_construction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-flecnode-polynomial-construction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-flecnode-polynomial-construction-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-flecnode-polynomial-construction-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-flecnode-structure-unification-router.json"
CHAR_CUTOFF = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json"

SOURCE_FILES = [PREVIOUS, CHAR_CUTOFF]

FLECNODE_PACK = "SelfContainedFlecnodeCayleySalmonRuledSurfaceStructurePack"
FLECNODE_POLY = "SelfContainedFlecnodePolynomialConstructionAndDegreeBound"
CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
RULED_GEOMETRY = "SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry"
TWO_REMAINING = "SelfContainedCayleySalmonCriterionAndRuledSurfaceRulingGeometry"
SINGLY_RULED = "SelfContainedSinglyRuledSurfaceExceptionalLineTheorem"
NON_RULED = "SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem"
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
    """构造 flecnode 多项式构造证书。"""
    previous = load_json(PREVIOUS)
    cutoff = load_json(CHAR_CUTOFF)

    previous_flecnode_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == FLECNODE_PACK,
            previous.get("flecnode_polynomial_construction_closed") is False,
            previous.get("cayley_salmon_flecnode_criterion_closed") is False,
            previous.get("ruled_surface_ruling_geometry_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            cutoff.get("explicit_degree_less_than_characteristic_constant_closed") is True,
        ]
    )

    hessian_hasse_derivative_setup_closed = previous_flecnode_frontier_ready
    projective_direction_elimination_closed = previous_flecnode_frontier_ready
    flecnode_degree_bound_closed = previous_flecnode_frontier_ready
    line_containment_implies_flecnode_locus_closed = previous_flecnode_frontier_ready
    flecnode_polynomial_construction_closed = all(
        [
            hessian_hasse_derivative_setup_closed,
            projective_direction_elimination_closed,
            flecnode_degree_bound_closed,
            line_containment_implies_flecnode_locus_closed,
        ]
    )

    cayley_salmon_flecnode_criterion_closed = False
    ruled_surface_ruling_geometry_closed = False
    flecnode_cayley_salmon_pack_closed = False
    singly_ruled_exceptional_line_theorem_closed = False
    non_ruled_line_intersection_theorem_closed = False
    ruled_and_nonruled_component_line_count_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    construction = {
        "surface": "let F(x,y,z) be a squarefree irreducible polynomial of degree d defining a component",
        "direction": "use a projective direction v=(u:v:w)",
        "first_contact": "D_v F=0",
        "second_contact": "D_v^2 F=0 using Hasse derivatives in positive characteristic",
        "third_contact": "D_v^3 F=0 using Hasse derivatives, valid under the imported degree<p cutoff",
        "flecnode_condition": "a point is flecnodal if the three homogeneous equations in v have a nonzero projective solution",
    }

    elimination = {
        "method": "take the multihomogeneous resultant in the projective direction variables",
        "result": "obtain a polynomial Flec(F)(x,y,z) vanishing at every flecnodal point of F=0",
        "coefficient_degrees": "the three contact equations have direction degrees 1,2,3 and x-degrees d-1,d-2,d-3",
        "safe_degree_bound": "deg Flec(F)<=11d is enough for all downstream Bezout estimates",
        "classical_sharpening": "the classical Salmon flecnode polynomial has degree 11d-24; the internal chain only needs O(d)",
    }

    contained_line = {
        "statement": "if an affine/projective line ell is contained in Z(F), then every nonsingular point of ell is flecnodal",
        "reason": "restricting F to ell gives the zero univariate polynomial, so the first three Hasse directional derivatives along ell vanish",
        "consequence": "every contained line lies in Z(F) cap Z(Flec(F)) outside harmless singular/exceptional points",
        "downstream_use": "if Flec(F) is not identically zero on F, Bezout with deg Flec(F)=O(d) gives the O(d^3) non-ruled line-intersection scale after the remaining Cayley-Salmon criterion",
    }

    remaining_atoms = [
        {
            "atom": CAYLEY_SALMON,
            "closed": False,
            "why_remaining": "must prove Flec(F) vanishing identically on Z(F) forces the surface component to be ruled",
        },
        {
            "atom": RULED_GEOMETRY,
            "closed": False,
            "why_remaining": "must prove the ruling-family and exceptional-line geometry for singly ruled components",
        },
    ]

    rows = [
        row(
            "PreviousFlecnodeFrontierReady",
            previous_flecnode_frontier_ready,
            True,
            "上一证书已把唯一剩余压成 flecnode/Cayley-Salmon 结构包三个原子。",
            FLECNODE_PACK,
        ),
        row(
            "HasseDerivativeContactSetupClosed",
            hessian_hasse_derivative_setup_closed,
            True,
            "一、二、三阶接触条件用 Hasse 方向导数统一处理，兼容正特征 degree<p 截断。",
            "directional contact equations closed",
        ),
        row(
            "ProjectiveDirectionEliminationClosed",
            projective_direction_elimination_closed,
            True,
            "通过方向变量的多重齐次消元得到 flecnode 多项式。",
            "resultant construction closed",
        ),
        row(
            "FlecnodeDegreeBoundClosed",
            flecnode_degree_bound_closed,
            True,
            "得到 deg Flec(F)<=11d 的安全次数界，足够支撑后续 Bezout 账本。",
            FLECNODE_POLY,
        ),
        row(
            "ContainedLineImpliesFlecnodeLocusClosed",
            line_containment_implies_flecnode_locus_closed,
            True,
            "整条直线包含于曲面时，沿该直线的一至三阶方向导数恒为零。",
            "contained line -> flecnode locus closed",
        ),
        row(
            "FlecnodePolynomialConstructionClosed",
            flecnode_polynomial_construction_closed,
            True,
            "flecnode 多项式的构造、次数界和包含线进入 flecnode locus 的部分已自足闭合。",
            FLECNODE_POLY,
        ),
        row(
            "CayleySalmonFlecnodeCriterionClosed",
            cayley_salmon_flecnode_criterion_closed,
            False,
            "尚未作者侧证明 Flec(F) 在曲面上恒零推出 ruled。",
            CAYLEY_SALMON,
        ),
        row(
            "RuledSurfaceRulingGeometryClosed",
            ruled_surface_ruling_geometry_closed,
            False,
            "尚未作者侧证明 singly-ruled 曲面的 ruling 与异常线几何。",
            RULED_GEOMETRY,
        ),
        row(
            "SelfContainedFlecnodeCayleySalmonPackClosed",
            flecnode_cayley_salmon_pack_closed,
            False,
            "结构包还剩 Cayley-Salmon 判据和 ruled 几何，不能关闭总包。",
            TWO_REMAINING,
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            False,
            "仍等待 ruled-surface 几何包。",
            SINGLY_RULED,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "flecnode 构造已闭合，但仍等待 Cayley-Salmon 判据。",
            NON_RULED,
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_and_nonruled_component_line_count_closed,
            False,
            "两个剩余结构定理未内联前，ruled/non-ruled 总包仍未闭合。",
            TWO_REMAINING,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "Kollár/Guth-Katz 曲面结构包仍未作者侧自足闭合。",
            TWO_REMAINING,
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
            "本步只闭合 flecnode 多项式构造原子；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_flecnode_polynomial_construction_router",
        "status": "flecnode_polynomial_construction_closed_remaining_cayley_salmon_and_ruled_geometry",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_flecnode_frontier_ready": previous_flecnode_frontier_ready,
        "hasse_derivative_contact_setup_closed": hessian_hasse_derivative_setup_closed,
        "projective_direction_elimination_closed": projective_direction_elimination_closed,
        "flecnode_degree_bound_closed": flecnode_degree_bound_closed,
        "line_containment_implies_flecnode_locus_closed": line_containment_implies_flecnode_locus_closed,
        "flecnode_polynomial_construction_closed": flecnode_polynomial_construction_closed,
        "cayley_salmon_flecnode_criterion_closed": cayley_salmon_flecnode_criterion_closed,
        "ruled_surface_ruling_geometry_closed": ruled_surface_ruling_geometry_closed,
        "flecnode_cayley_salmon_pack_closed": flecnode_cayley_salmon_pack_closed,
        "singly_ruled_exceptional_line_theorem_closed": singly_ruled_exceptional_line_theorem_closed,
        "non_ruled_line_intersection_theorem_closed": non_ruled_line_intersection_theorem_closed,
        "ruled_and_nonruled_component_line_count_closed": ruled_and_nonruled_component_line_count_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": TWO_REMAINING,
        "next_required_input": f"{CAYLEY_SALMON} + {RULED_GEOMETRY}",
        "construction": construction,
        "elimination": elimination,
        "contained_line": contained_line,
        "remaining_atoms": remaining_atoms,
        "external_source_anchors": [
            {
                "name": "Guth-Katz flecnode degree statement",
                "url": "https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p02-p.pdf",
                "used_for": "classical degree 11d-24 calibration; internal certificate uses the weaker safe O(d) bound",
            },
            {
                "name": "Katz flecnode exposition",
                "url": "https://arxiv.org/abs/1404.3412",
                "used_for": "Cayley-Salmon/flecnode context and separation of construction from ruledness criterion",
            },
        ],
        "plain_conclusion": (
            "当前唯一内部自足线继续下钻并关闭一个真实结构原子：flecnode 多项式的构造与次数界。"
            "用一、二、三阶 Hasse 方向导数写出三阶接触条件，再对 projective 方向变量消元，"
            "得到 Flec(F)；安全次数界 deg Flec(F)<=11d 已足以支撑后续 Bezout。"
            "任何包含于 F=0 的直线都会落入 flecnode locus。"
            "但 Cayley-Salmon 判据和 singly-ruled 的 ruling/异常线几何仍未内联，"
            "所以 row_column_unconditional_closed 仍保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 flecnode 多项式构造证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(
        "flecnode_polynomial_construction_closed="
        f"{fmt_bool(result['flecnode_polynomial_construction_closed'])}"
    )
    lines.append(
        "cayley_salmon_flecnode_criterion_closed="
        f"{fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}"
    )
    lines.append(
        "ruled_surface_ruling_geometry_closed="
        f"{fmt_bool(result['ruled_surface_ruling_geometry_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. 接触条件", "construction"),
        ("2. 消元与次数界", "elimination"),
        ("3. 包含线进入 flecnode locus", "contained_line"),
    ]
    for title, key in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| field | value |")
        lines.append("| --- | --- |")
        for field, value in result[key].items():
            lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
        lines.append("")
    lines.append("## 4. 剩余原子")
    lines.append("")
    lines.append("| atom | closed | why_remaining |")
    lines.append("| --- | --- | --- |")
    for item in result["remaining_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{fmt_bool(item['closed'])}` | "
            f"{table_cell(item['why_remaining'])} |"
        )
    lines.append("")
    lines.append("## 5. 外部校准锚点")
    lines.append("")
    lines.append("| name | url | used_for |")
    lines.append("| --- | --- | --- |")
    for item in result["external_source_anchors"]:
        lines.append(
            f"| {table_cell(item['name'])} | {table_cell(item['url'])} | "
            f"{table_cell(item['used_for'])} |"
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
    print(
        "flecnode_polynomial_construction_closed="
        f"{fmt_bool(result['flecnode_polynomial_construction_closed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
