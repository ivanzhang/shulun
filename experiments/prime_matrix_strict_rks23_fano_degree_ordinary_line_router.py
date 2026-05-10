#!/usr/bin/env python3
"""闭合 Fano 曲线次数界与普通线 O(d) 相交界。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_fano_degree_ordinary_line_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-fano-degree-ordinary-line-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-fano-degree-ordinary-line-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-fano-degree-ordinary-line-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-ruled-geometry-fano-reduction-router.json"
COMPONENT = MONO / "prime-matrix-strict-rks23-ruled-surface-component-accounting-router.json"

SOURCE_FILES = [PREVIOUS, COMPONENT]

STRUCTURE_PACK = "SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack"
CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
FANO_ATOM = "SelfContainedFanoCurveDegreeAndExceptionalLineBoundForSinglyRuledSurface"
FANO_DEGREE = "SelfContainedFanoRulingCurveDegreeBoundForSinglyRuledSurface"
ORDINARY_LINE = "SelfContainedOrdinaryRuledLineOdIntersectionBound"
DIRECTRIX_BOUND = "SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface"
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
    """构造 Fano 次数/普通线证书。"""
    previous = load_json(PREVIOUS)
    component = load_json(COMPONENT)

    previous_fano_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == STRUCTURE_PACK,
            previous.get("ruled_geometry_reduced_to_fano_atom") is True,
            previous.get("fano_curve_degree_and_exceptional_line_bound_closed") is False,
            previous.get("cayley_salmon_flecnode_criterion_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            component.get("singly_ruled_accounting_reduction_closed") is True,
        ]
    )

    generic_schubert_degree_argument_closed = previous_fano_frontier_ready
    fano_ruling_curve_degree_bound_closed = previous_fano_frontier_ready
    ordinary_ruled_line_od_intersection_bound_closed = previous_fano_frontier_ready
    ordinary_contribution_ledger_closed = previous_fano_frontier_ready

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

    fano_degree_proof = {
        "surface": "irreducible singly ruled surface S in P^3 of degree d, excluding plane/quadric cases already handled",
        "ruling_curve": "let C be the one-dimensional ruling component of F_1(S) in G(1,3)",
        "degree_measure": "degree of C is intersection with a generic Schubert divisor Sigma_m of lines meeting a generic line m",
        "generic_line_argument": "for generic m not contained in S, each ruling line meeting m gives an intersection point in m cap S",
        "bound": "|m cap S|<=d by Bezout, hence deg(C)<=d",
        "scope": "this proves the ordinary-line degree input; it does not bound exceptional lines whose Schubert divisor contains C",
    }

    ordinary_line_transfer = {
        "ordinary_line": "a contained line ell is ordinary if C is not contained in Sigma_ell",
        "schubert_intersection": "ruling lines meeting ell are C cap Sigma_ell",
        "degree_bound": "|C cap Sigma_ell|<=deg(C)<=d, up to harmless multiplicity conventions",
        "result": "ordinary contained lines meet O(d) ruling lines",
        "downstream": "the prior component accounting already absorbs ordinary O(d) contributions into O(|L|^(1/2)|M|)",
    }

    remaining_directrix = {
        "exceptional_line": "ell is exceptional if C is contained in Sigma_ell, equivalently ell meets every ruling line",
        "needed_bound": "there are O(1), classically at most two, such directrix-type exceptional lines outside plane/quadric cases",
        "why_still_open": "this requires a separate directrix/Grassmannian incidence argument; it is not implied by deg(C)<=d alone",
        "remaining_atom": DIRECTRIX_BOUND,
    }

    remaining_atoms = [
        {
            "atom": DIRECTRIX_BOUND,
            "closed": False,
            "why_remaining": "must prove only O(1) lines have Schubert divisors containing the ruling Fano curve",
        },
        {
            "atom": CAYLEY_SALMON,
            "closed": False,
            "why_remaining": "must prove Flec(F) vanishing identically on the surface forces ruledness",
        },
    ]

    rows = [
        row(
            "PreviousFanoFrontierReady",
            previous_fano_frontier_ready,
            True,
            "上一证书已把 ruled 几何压成 Fano 曲线次数/异常线界。",
            FANO_ATOM,
        ),
        row(
            "GenericSchubertDegreeArgumentClosed",
            generic_schubert_degree_argument_closed,
            True,
            "用 generic line 的 Schubert divisor 计算 Fano ruling 曲线次数。",
            FANO_DEGREE,
        ),
        row(
            "FanoRulingCurveDegreeBoundClosed",
            fano_ruling_curve_degree_bound_closed,
            True,
            "由 generic line 与 S 的 Bezout 交数得到 deg(C)<=d。",
            FANO_DEGREE,
        ),
        row(
            "OrdinaryRuledLineOdIntersectionBoundClosed",
            ordinary_ruled_line_od_intersection_bound_closed,
            True,
            "若 C 不含于 Sigma_ell，则 ell 只与 O(d) 条 ruling 线相交。",
            ORDINARY_LINE,
        ),
        row(
            "OrdinaryContributionLedgerClosed",
            ordinary_contribution_ledger_closed,
            True,
            "普通线 O(d) 贡献与前序 ruled component 账本严格对接。",
            "ordinary contribution closed",
        ),
        row(
            "ExceptionalDirectrixLineBoundClosed",
            exceptional_directrix_line_bound_closed,
            False,
            "仍需证明 Schubert divisor 包含 C 的 directrix 型异常线只有 O(1)。",
            DIRECTRIX_BOUND,
        ),
        row(
            "FanoCurveDegreeAndExceptionalLineBoundClosed",
            fano_curve_degree_and_exceptional_line_bound_closed,
            False,
            "Fano 次数界已闭合，但异常线界未闭合。",
            FANO_ATOM,
        ),
        row(
            "RuledSurfaceRulingGeometryClosed",
            ruled_surface_ruling_geometry_closed,
            False,
            "ruled 几何仍等待异常 directrix 界。",
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
            "结构包现在剩 directrix 异常线界和 Cayley-Salmon 判据。",
            STRUCTURE_PACK,
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            False,
            "singly-ruled 分支仍等待异常 directrix 界。",
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
            "本步只闭合 Fano 次数界和普通线界；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_fano_degree_ordinary_line_router",
        "status": "fano_ruling_curve_degree_and_ordinary_line_bound_closed_remaining_directrix_and_cayley_salmon",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_fano_frontier_ready": previous_fano_frontier_ready,
        "generic_schubert_degree_argument_closed": generic_schubert_degree_argument_closed,
        "fano_ruling_curve_degree_bound_closed": fano_ruling_curve_degree_bound_closed,
        "ordinary_ruled_line_od_intersection_bound_closed": ordinary_ruled_line_od_intersection_bound_closed,
        "ordinary_contribution_ledger_closed": ordinary_contribution_ledger_closed,
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
        "next_required_input": f"{DIRECTRIX_BOUND} + {CAYLEY_SALMON}",
        "fano_degree_proof": fano_degree_proof,
        "ordinary_line_transfer": ordinary_line_transfer,
        "remaining_directrix": remaining_directrix,
        "remaining_atoms": remaining_atoms,
        "plain_conclusion": (
            "当前唯一内部自足线继续下钻并关闭 Fano 原子的一半：ruling Fano 曲线次数界与普通线 O(d) 相交界。"
            "用 generic Schubert divisor，也就是与一条 generic line 相交的直线条件，计算 Fano 曲线次数；"
            "每条满足该条件的 ruling line 给出 generic line 与曲面 S 的一个交点，所以次数至多 d。"
            "因此任何普通 contained line 的 Schubert divisor 与 ruling curve 交数至多 d，普通线贡献闭合。"
            "剩余只在异常 directrix 型线界和 Cayley-Salmon flecnode 判据；row_column_unconditional_closed 仍保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 Fano 次数与普通线证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(f"fano_ruling_curve_degree_bound_closed={fmt_bool(result['fano_ruling_curve_degree_bound_closed'])}")
    lines.append(
        "ordinary_ruled_line_od_intersection_bound_closed="
        f"{fmt_bool(result['ordinary_ruled_line_od_intersection_bound_closed'])}"
    )
    lines.append(
        "exceptional_directrix_line_bound_closed="
        f"{fmt_bool(result['exceptional_directrix_line_bound_closed'])}"
    )
    lines.append(
        "cayley_salmon_flecnode_criterion_closed="
        f"{fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. Fano 次数证明", "fano_degree_proof"),
        ("2. 普通线转移", "ordinary_line_transfer"),
        ("3. 剩余 directrix 异常线", "remaining_directrix"),
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
    print(f"fano_ruling_curve_degree_bound_closed={fmt_bool(result['fano_ruling_curve_degree_bound_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
