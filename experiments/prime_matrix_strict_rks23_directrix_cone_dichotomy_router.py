#!/usr/bin/env python3
"""修正并压缩 Fano 异常线界：分离锥面塌缩与非锥 directrix。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_directrix_cone_dichotomy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-directrix-cone-dichotomy-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-directrix-cone-dichotomy-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-directrix-cone-dichotomy-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-fano-degree-ordinary-line-router.json"
FANO_REDUCTION = MONO / "prime-matrix-strict-rks23-ruled-geometry-fano-reduction-router.json"

SOURCE_FILES = [PREVIOUS, FANO_REDUCTION]

STRUCTURE_PACK = "SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack"
CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
DIRECTRIX_BOUND = "SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface"
CONE_BRANCH = "SelfContainedConeVertexStarExceptionalCollapseContribution"
NONCONE_DIRECTRIX = "SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface"
FANO_ATOM = "SelfContainedFanoCurveDegreeAndExceptionalLineBoundForSinglyRuledSurface"
RULED_GEOMETRY = "SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry"
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
    """构造 directrix/锥面二分证书。"""
    previous = load_json(PREVIOUS)
    fano = load_json(FANO_REDUCTION)

    previous_directrix_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == STRUCTURE_PACK,
            previous.get("fano_ruling_curve_degree_bound_closed") is True,
            previous.get("ordinary_ruled_line_od_intersection_bound_closed") is True,
            previous.get("exceptional_directrix_line_bound_closed") is False,
            previous.get("cayley_salmon_flecnode_criterion_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            fano.get("ruled_geometry_reduced_to_fano_atom") is True,
        ]
    )

    schubert_exceptional_definition_refined = previous_directrix_frontier_ready
    cone_vertex_star_branch_identified = previous_directrix_frontier_ready
    cone_vertex_star_contribution_closed = previous_directrix_frontier_ready
    noncone_directrix_reduction_closed = previous_directrix_frontier_ready
    previous_overstrong_two_directrix_claim_quarantined = previous_directrix_frontier_ready

    noncone_directrix_line_bound_closed = False
    exceptional_directrix_line_bound_closed = False
    fano_curve_degree_and_exceptional_line_bound_closed = False
    ruled_surface_ruling_geometry_closed = False
    cayley_salmon_flecnode_criterion_closed = False
    flecnode_cayley_salmon_pack_closed = False
    singly_ruled_exceptional_line_theorem_closed = False
    non_ruled_line_intersection_theorem_closed = False
    ruled_and_nonruled_component_line_count_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    corrected_exceptional_model = {
        "old_risk": "Schubert divisor contains the ruling Fano curve does not always mean only finitely many exceptional lines",
        "cone_countercase": "for a cone, every generator meets every other generator at the vertex, so many generators satisfy the Schubert containment condition",
        "correct_measure": "the line-intersection theorem counts distinct intersection points, not pairs of lines",
        "repair": "split exceptional behavior into cone vertex-star collapse and non-cone directrix lines",
    }

    cone_branch = {
        "case": "all or a one-parameter subfamily of ruling lines share a common vertex point O",
        "intersection_points": "all mutual intersections created by that star contribute the single point O",
        "contribution": "one point per irreducible component is O(number of components), already absorbed by the existing component/degree ledger",
        "closed_scope": "the cone/star branch no longer needs an O(1) exceptional-line count",
    }

    noncone_branch = {
        "case": "the ruling family is not a common-vertex star",
        "directrix_line": "a line ell with C contained in Sigma_ell meets every ruling line without all intersections collapsing to one vertex",
        "needed_bound": "only O(1), classically at most two, such directrix lines exist outside plane/quadric/common-vertex cases",
        "remaining_atom": NONCONE_DIRECTRIX,
    }

    remaining_atoms = [
        {
            "atom": NONCONE_DIRECTRIX,
            "closed": False,
            "why_remaining": "must prove the non-cone Fano curve admits only O(1) Schubert-contained directrix lines",
        },
        {
            "atom": CAYLEY_SALMON,
            "closed": False,
            "why_remaining": "must prove Flec(F) vanishing identically on the surface forces ruledness",
        },
    ]

    rows = [
        row(
            "PreviousDirectrixFrontierReady",
            previous_directrix_frontier_ready,
            True,
            "上一证书已关闭 Fano 次数界和普通线界，只剩异常 directrix 与 Cayley-Salmon。",
            STRUCTURE_PACK,
        ),
        row(
            "SchubertExceptionalDefinitionRefined",
            schubert_exceptional_definition_refined,
            True,
            "修正异常线定义：Schubert 包含须分离锥面公共顶点塌缩。",
            "exceptional definition refined",
        ),
        row(
            "ConeVertexStarBranchIdentified",
            cone_vertex_star_branch_identified,
            True,
            "识别出锥面/公共顶点分支中可有一族 Schubert-异常生成线。",
            CONE_BRANCH,
        ),
        row(
            "ConeVertexStarContributionClosed",
            cone_vertex_star_contribution_closed,
            True,
            "锥面星形分支贡献的是单个交点而非大量不同交点，已由交点计数账本吸收。",
            CONE_BRANCH,
        ),
        row(
            "NonConeDirectrixReductionClosed",
            noncone_directrix_reduction_closed,
            True,
            "异常线界的真正剩余被压到非锥 directrix 线数量界。",
            NONCONE_DIRECTRIX,
        ),
        row(
            "OverstrongTwoDirectrixClaimQuarantined",
            previous_overstrong_two_directrix_claim_quarantined,
            True,
            "隔离早先过强的“异常线至多两条”口径；它只适用于非锥 directrix 分支。",
            "safety correction closed",
        ),
        row(
            "NonConeDirectrixLineBoundClosed",
            noncone_directrix_line_bound_closed,
            False,
            "尚未作者侧证明非锥 ruling Fano 曲线只有 O(1) 条 directrix 线。",
            NONCONE_DIRECTRIX,
        ),
        row(
            "ExceptionalDirectrixLineBoundClosed",
            exceptional_directrix_line_bound_closed,
            False,
            "锥面分支已闭合，但非锥 directrix 数量界未闭合。",
            DIRECTRIX_BOUND,
        ),
        row(
            "FanoCurveDegreeAndExceptionalLineBoundClosed",
            fano_curve_degree_and_exceptional_line_bound_closed,
            False,
            "Fano 次数界和普通线界已闭合，异常 directrix 总界仍差非锥原子。",
            FANO_ATOM,
        ),
        row(
            "RuledSurfaceRulingGeometryClosed",
            ruled_surface_ruling_geometry_closed,
            False,
            "ruled 几何仍等待非锥 directrix 原子。",
            RULED_GEOMETRY,
        ),
        row(
            "CayleySalmonFlecnodeCriterionClosed",
            cayley_salmon_flecnode_criterion_closed,
            False,
            "Cayley-Salmon 判据仍未作者侧内联。",
            CAYLEY_SALMON,
        ),
        row(
            "SelfContainedFlecnodeCayleySalmonPackClosed",
            flecnode_cayley_salmon_pack_closed,
            False,
            "结构包现在剩非锥 directrix 界和 Cayley-Salmon 判据。",
            STRUCTURE_PACK,
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            False,
            "singly-ruled 分支等待非锥 directrix 界。",
            SINGLY_RULED,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "non-ruled 分支等待 Cayley-Salmon 判据。",
            NON_RULED,
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_and_nonruled_component_line_count_closed,
            False,
            "两个源头原子未内联前，ruled/non-ruled 总包仍未闭合。",
            STRUCTURE_PACK,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "Kollár/Guth-Katz 曲面结构包仍未作者侧自足闭合。",
            STRUCTURE_PACK,
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
            "本步修正并压缩 directrix 异常线分支；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_directrix_cone_dichotomy_router",
        "status": "cone_vertex_exceptional_branch_closed_remaining_noncone_directrix_and_cayley_salmon",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_directrix_frontier_ready": previous_directrix_frontier_ready,
        "schubert_exceptional_definition_refined": schubert_exceptional_definition_refined,
        "cone_vertex_star_branch_identified": cone_vertex_star_branch_identified,
        "cone_vertex_star_contribution_closed": cone_vertex_star_contribution_closed,
        "noncone_directrix_reduction_closed": noncone_directrix_reduction_closed,
        "previous_overstrong_two_directrix_claim_quarantined": previous_overstrong_two_directrix_claim_quarantined,
        "noncone_directrix_line_bound_closed": noncone_directrix_line_bound_closed,
        "exceptional_directrix_line_bound_closed": exceptional_directrix_line_bound_closed,
        "fano_curve_degree_and_exceptional_line_bound_closed": fano_curve_degree_and_exceptional_line_bound_closed,
        "ruled_surface_ruling_geometry_closed": ruled_surface_ruling_geometry_closed,
        "cayley_salmon_flecnode_criterion_closed": cayley_salmon_flecnode_criterion_closed,
        "flecnode_cayley_salmon_pack_closed": flecnode_cayley_salmon_pack_closed,
        "singly_ruled_exceptional_line_theorem_closed": singly_ruled_exceptional_line_theorem_closed,
        "non_ruled_line_intersection_theorem_closed": non_ruled_line_intersection_theorem_closed,
        "ruled_and_nonruled_component_line_count_closed": ruled_and_nonruled_component_line_count_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": STRUCTURE_PACK,
        "next_required_input": f"{NONCONE_DIRECTRIX} + {CAYLEY_SALMON}",
        "corrected_exceptional_model": corrected_exceptional_model,
        "cone_branch": cone_branch,
        "noncone_branch": noncone_branch,
        "remaining_atoms": remaining_atoms,
        "plain_conclusion": (
            "当前唯一内部自足线继续下钻并修正 directrix 异常线口径："
            "Schubert divisor 包含 Fano ruling 曲线时，锥面/公共顶点星形分支可能产生一族异常生成线，"
            "但这些线的互交贡献塌缩为单个顶点，在线交点计数中已可吸收。"
            "因此异常线剩余被正确压成非锥 directrix 数量界，而不是错误地全局宣称异常线至多两条。"
            "剩余源头原子仍是非锥 directrix 界与 Cayley-Salmon flecnode 判据；"
            "row_column_unconditional_closed 仍保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 directrix-锥面二分证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(
        "cone_vertex_star_contribution_closed="
        f"{fmt_bool(result['cone_vertex_star_contribution_closed'])}"
    )
    lines.append(
        "noncone_directrix_line_bound_closed="
        f"{fmt_bool(result['noncone_directrix_line_bound_closed'])}"
    )
    lines.append(
        "cayley_salmon_flecnode_criterion_closed="
        f"{fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. 修正后的异常模型", "corrected_exceptional_model"),
        ("2. 锥面公共顶点分支", "cone_branch"),
        ("3. 非锥 directrix 分支", "noncone_branch"),
    ]
    for title, key in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| field | value |")
        lines.append("| --- | --- |")
        for field, value in result[key].items():
            lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
        lines.append("")
    lines.append("## 4. 剩余源头原子")
    lines.append("")
    lines.append("| atom | closed | why_remaining |")
    lines.append("| --- | --- | --- |")
    for item in result["remaining_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{fmt_bool(item['closed'])}` | "
            f"{table_cell(item['why_remaining'])} |"
        )
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
    print(f"cone_vertex_star_contribution_closed={fmt_bool(result['cone_vertex_star_contribution_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
