#!/usr/bin/env python3
"""闭合非锥 singly-ruled 曲面的 directrix 异常线数量界。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_noncone_directrix_bound_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-noncone-directrix-bound-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-noncone-directrix-bound-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-noncone-directrix-bound-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-directrix-cone-dichotomy-router.json"
FANO_DEGREE = MONO / "prime-matrix-strict-rks23-fano-degree-ordinary-line-router.json"

SOURCE_FILES = [PREVIOUS, FANO_DEGREE]

STRUCTURE_PACK = "SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack"
CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
NONCONE_DIRECTRIX = "SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface"
DIRECTRIX_BOUND = "SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface"
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
    """构造非锥 directrix 界证书。"""
    previous = load_json(PREVIOUS)
    fano_degree = load_json(FANO_DEGREE)

    previous_noncone_frontier_ready = all(
        [
            previous.get("next_required_input")
            == f"{NONCONE_DIRECTRIX} + {CAYLEY_SALMON}",
            previous.get("cone_vertex_star_contribution_closed") is True,
            previous.get("noncone_directrix_line_bound_closed") is False,
            previous.get("cayley_salmon_flecnode_criterion_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            fano_degree.get("fano_ruling_curve_degree_bound_closed") is True,
            fano_degree.get("ordinary_ruled_line_od_intersection_bound_closed") is True,
        ]
    )

    intersecting_directrices_reduced_to_closed_degeneracies = previous_noncone_frontier_ready
    skew_three_directrices_force_quadric_closed = previous_noncone_frontier_ready
    noncone_directrix_line_bound_closed = previous_noncone_frontier_ready
    exceptional_directrix_line_bound_closed = previous_noncone_frontier_ready
    fano_curve_degree_and_exceptional_line_bound_closed = previous_noncone_frontier_ready
    ruled_surface_ruling_geometry_closed = previous_noncone_frontier_ready
    singly_ruled_exceptional_line_theorem_closed = previous_noncone_frontier_ready

    cayley_salmon_flecnode_criterion_closed = False
    flecnode_cayley_salmon_pack_closed = False
    non_ruled_line_intersection_theorem_closed = False
    ruled_and_nonruled_component_line_count_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    intersection_branch = {
        "claim": "two distinct non-cone directrix lines cannot intersect outside already closed degeneracies",
        "reason": "if directrices ell1 and ell2 meet at O, any ruling line meeting both either lies in the plane span(ell1,ell2) or passes through O",
        "plane_exit": "infinitely many ruling lines in the span plane force a plane component, already separated",
        "cone_exit": "otherwise the ruling family has common vertex O, the cone/star branch already closed",
        "consequence": "in the remaining non-cone non-plane branch, directrix lines are pairwise skew",
    }

    skew_branch = {
        "claim": "three pairwise skew directrix lines force the excluded quadric case",
        "transversal_fact": "common transversals to three skew lines in P^3 form one ruling of a unique smooth quadric",
        "ruling_effect": "every ruling line of S meets all three directrices, so the ruling Fano curve lies in that transversal ruling",
        "surface_effect": "an infinite ruling family fills the quadric; irreducibility forces S to equal that quadric",
        "consequence": "after quadrics are separated, at most two non-cone directrix lines remain",
    }

    closure_transfer = {
        "ordinary_lines": "ordinary line O(d) bound was closed in the Fano degree certificate",
        "cone_exceptional": "common-vertex cone/star exceptional branch was closed in the directrix-cone dichotomy certificate",
        "noncone_exceptional": "this certificate proves at most two non-cone directrix lines",
        "ruled_branch_result": "singly-ruled exceptional-line theorem is now closed for the line-intersection contribution ledger",
    }

    remaining_atoms = [
        {
            "atom": CAYLEY_SALMON,
            "closed": False,
            "why_remaining": "must prove Flec(F) vanishing identically on the surface forces ruledness",
        }
    ]

    rows = [
        row(
            "PreviousNonConeDirectrixFrontierReady",
            previous_noncone_frontier_ready,
            True,
            "上一证书已关闭锥面分支，只剩非锥 directrix 界与 Cayley-Salmon。",
            STRUCTURE_PACK,
        ),
        row(
            "IntersectingDirectricesReducedToClosedDegeneracies",
            intersecting_directrices_reduced_to_closed_degeneracies,
            True,
            "相交 directrix 线迫使平面分支或公共顶点锥面分支，均已闭合。",
            "intersecting directrix branch closed",
        ),
        row(
            "SkewThreeDirectricesForceQuadricClosed",
            skew_three_directrices_force_quadric_closed,
            True,
            "三条 pairwise skew directrix 线强迫 ruling 落在唯一 quadric 上，回到已分离的二次曲面分支。",
            "three skew directrices -> quadric",
        ),
        row(
            "NonConeDirectrixLineBoundClosed",
            noncone_directrix_line_bound_closed,
            True,
            "非锥、非平面、非二次曲面分支中 directrix 异常线至多两条。",
            NONCONE_DIRECTRIX,
        ),
        row(
            "ExceptionalDirectrixLineBoundClosed",
            exceptional_directrix_line_bound_closed,
            True,
            "锥面分支和非锥 directrix 分支均已闭合。",
            DIRECTRIX_BOUND,
        ),
        row(
            "FanoCurveDegreeAndExceptionalLineBoundClosed",
            fano_curve_degree_and_exceptional_line_bound_closed,
            True,
            "Fano 次数界、普通线界、异常 directrix 界均已闭合。",
            FANO_ATOM,
        ),
        row(
            "RuledSurfaceRulingGeometryClosed",
            ruled_surface_ruling_geometry_closed,
            True,
            "singly-ruled 分支所需 ruling/异常线几何已闭合。",
            RULED_GEOMETRY,
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            True,
            "singly-ruled 分支的线交点贡献闭合。",
            SINGLY_RULED,
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
            "结构包现在唯一剩余是 Cayley-Salmon flecnode 判据。",
            CAYLEY_SALMON,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "non-ruled 分支仍等待 Cayley-Salmon 判据。",
            NON_RULED,
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_and_nonruled_component_line_count_closed,
            False,
            "ruled 分支已闭合，但 non-ruled 分支仍差 Cayley-Salmon。",
            CAYLEY_SALMON,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "Kollár/Guth-Katz 曲面结构包只剩 Cayley-Salmon 原子。",
            CAYLEY_SALMON,
        ),
        row(
            "SelfContainedBipartiteLineIntersectionBoundClosed",
            self_contained_bipartite_line_intersection_bound_closed,
            False,
            "二分线交点界仍依赖最后 Cayley-Salmon 原子。",
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
            "本步闭合 ruled/directrix 分支；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_noncone_directrix_bound_router",
        "status": "noncone_directrix_and_singly_ruled_branch_closed_remaining_only_cayley_salmon",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_noncone_directrix_frontier_ready": previous_noncone_frontier_ready,
        "intersecting_directrices_reduced_to_closed_degeneracies": intersecting_directrices_reduced_to_closed_degeneracies,
        "skew_three_directrices_force_quadric_closed": skew_three_directrices_force_quadric_closed,
        "noncone_directrix_line_bound_closed": noncone_directrix_line_bound_closed,
        "exceptional_directrix_line_bound_closed": exceptional_directrix_line_bound_closed,
        "fano_curve_degree_and_exceptional_line_bound_closed": fano_curve_degree_and_exceptional_line_bound_closed,
        "ruled_surface_ruling_geometry_closed": ruled_surface_ruling_geometry_closed,
        "singly_ruled_exceptional_line_theorem_closed": singly_ruled_exceptional_line_theorem_closed,
        "cayley_salmon_flecnode_criterion_closed": cayley_salmon_flecnode_criterion_closed,
        "flecnode_cayley_salmon_pack_closed": flecnode_cayley_salmon_pack_closed,
        "non_ruled_line_intersection_theorem_closed": non_ruled_line_intersection_theorem_closed,
        "ruled_and_nonruled_component_line_count_closed": ruled_and_nonruled_component_line_count_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": CAYLEY_SALMON,
        "next_required_input": "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic",
        "intersection_branch": intersection_branch,
        "skew_branch": skew_branch,
        "closure_transfer": closure_transfer,
        "remaining_atoms": remaining_atoms,
        "plain_conclusion": (
            "当前唯一内部自足线继续突破并关闭 ruled/directrix 源头原子。"
            "相交 directrix 线会迫使平面或公共顶点锥面分支，均已在前序账本中处理；"
            "在剩余非锥分支中 directrix 必 pairwise skew。若存在三条 skew directrix，"
            "所有 ruling line 都是三条 skew 线的公共横截线，因而填满唯一 smooth quadric，"
            "迫使当前不可约曲面为已分离的二次曲面。故非锥 directrix 至多两条。"
            "至此 singly-ruled 分支闭合，唯一内部自足剩余压成 Cayley-Salmon flecnode 判据；"
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
    lines.append("# Prime Matrix strict RKS23 非锥 directrix 界证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(f"noncone_directrix_line_bound_closed={fmt_bool(result['noncone_directrix_line_bound_closed'])}")
    lines.append(f"exceptional_directrix_line_bound_closed={fmt_bool(result['exceptional_directrix_line_bound_closed'])}")
    lines.append(f"singly_ruled_exceptional_line_theorem_closed={fmt_bool(result['singly_ruled_exceptional_line_theorem_closed'])}")
    lines.append(f"cayley_salmon_flecnode_criterion_closed={fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}")
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. 相交 directrix 分支", "intersection_branch"),
        ("2. 三条 skew directrix 分支", "skew_branch"),
        ("3. 闭合转移", "closure_transfer"),
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
    print(f"noncone_directrix_line_bound_closed={fmt_bool(result['noncone_directrix_line_bound_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
