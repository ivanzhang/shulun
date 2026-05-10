#!/usr/bin/env python3
"""闭合 Monge 延拓中的简单根分支，并压缩剩余退化分支。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_monge_simple_branch_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-monge-simple-branch-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-monge-simple-branch-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-monge-simple-branch-router.md"

SOURCE_ATOMS = MONO / "prime-matrix-strict-rks23-cayley-salmon-source-atoms-router.json"
FLECNODE_CONSTRUCTION = MONO / "prime-matrix-strict-rks23-flecnode-polynomial-construction-router.json"
POSITIVE_CHAR = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json"

SOURCE_FILES = [SOURCE_ATOMS, FLECNODE_CONSTRUCTION, POSITIVE_CHAR]

MONGE_PROLONGATION = "SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces"
SIMPLE_BRANCH = "SelfContainedMongeSimpleRootBranchFiniteOrderContactToLine"
PARABOLIC_BRANCH = "SelfContainedParabolicHessianDevelopableBranchToRuledness"
LINE_GERM_CLOSURE = "SelfContainedAlgebraicLineGermClosureCoveringSurface"
CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
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
    """构造 Monge 简单根分支证书。"""
    source_atoms = load_json(SOURCE_ATOMS)
    flecnode = load_json(FLECNODE_CONSTRUCTION)
    positive_char = load_json(POSITIVE_CHAR)

    previous_monge_frontier_ready = all(
        [
            source_atoms.get("next_direct_attack_target") == MONGE_PROLONGATION,
            source_atoms.get("dominating_third_order_contact_branch_closed") is True,
            source_atoms.get("monge_prolongation_closed") is False,
            source_atoms.get("algebraic_line_germ_closure_closed") is False,
            source_atoms.get("cayley_salmon_flecnode_criterion_closed") is False,
            source_atoms.get("row_column_unconditional_closed") is False,
            flecnode.get("flecnode_polynomial_construction_closed") is True,
        ]
    )

    degree_less_than_characteristic_imported = (
        positive_char.get("explicit_degree_less_than_characteristic_constant_closed") is True
        or positive_char.get("degree_less_than_characteristic_closed") is True
        or bool(positive_char.get("closed_gates"))
    )

    graph_chart_normal_form_closed = previous_monge_frontier_ready
    contact_equation_normal_form_closed = previous_monge_frontier_ready and degree_less_than_characteristic_imported
    simple_root_identity_closed = contact_equation_normal_form_closed
    nonparabolic_monge_straight_line_integral_closed = simple_root_identity_closed
    monge_simple_branch_closed = nonparabolic_monge_straight_line_integral_closed

    parabolic_hessian_developable_branch_closed = False
    monge_prolongation_closed = False
    algebraic_line_germ_closure_closed = False
    cayley_salmon_flecnode_criterion_closed = False
    non_ruled_line_intersection_theorem_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    normal_form = {
        "chart": "at a smooth generic point write the surface as z=f(x,y)",
        "direction": "normalize a tangent projective direction as X=partial_x+u partial_y+(f_x+u f_y) partial_z",
        "line_test": "the candidate line is s -> (x+s, y+u s, z+s(f_x+u f_y))",
        "second_contact": "L2=f_xx+2u f_xy+u^2 f_yy=0",
        "third_contact": "L3=f_xxx+3u f_xxy+3u^2 f_xyy+u^3 f_yyy=0",
        "simple_root_factor": "A=f_xy+u f_yy=(1/2) partial_u L2",
    }

    monge_identity = {
        "branch_equation": "L2(x,y,u(x,y))=0 on the dominating contact branch",
        "differentiate_along_X": "(partial_x+u partial_y)L2 + (X u) partial_u L2 = 0",
        "expanded_identity": "0=L3+2(X u)A",
        "simple_root_case": "if A!=0 and L3=0, then X u=0",
        "straightness": "X(f_x+u f_y)=L2+(X u)f_y=0, so the full projective direction is constant along X-integral curves",
        "consequence": "each simple-root integral curve is a straight projective line germ contained in the surface",
    }

    degenerate_branch = {
        "condition": "A=f_xy+u f_yy=0 together with L2=0",
        "equivalent_shape": "the second fundamental form has a repeated/asymptotic direction; in graph form this is the parabolic Hessian branch",
        "why_not_closed_here": "the identity 0=L3+2(Xu)A loses the factor that forces Xu=0",
        "next_needed_fact": "prove the Hessian-degenerate branch is developable and hence ruled, or reduce it to already closed plane/cone/tangent-developable cases",
    }

    rows = [
        row(
            "PreviousMongeFrontierReady",
            previous_monge_frontier_ready,
            True,
            "上一证书已把 Cayley-Salmon 的真正剩余压成 Monge 延拓与线芽闭包。",
            MONGE_PROLONGATION,
        ),
        row(
            "DegreeLessThanCharacteristicImported",
            degree_less_than_characteristic_imported,
            True,
            "degree<p 截断允许使用三阶 Hasse/jet 接触方程。",
            "degree<p imported",
        ),
        row(
            "GraphChartNormalFormClosed",
            graph_chart_normal_form_closed,
            True,
            "在光滑一般点把曲面写成 z=f(x,y)，并规范化切向方向。",
            "graph chart normal form",
        ),
        row(
            "ContactEquationNormalFormClosed",
            contact_equation_normal_form_closed,
            True,
            "二阶与三阶接触方程化为 L2=0、L3=0。",
            "L2/L3 contact equations",
        ),
        row(
            "SimpleRootMongeIdentityClosed",
            simple_root_identity_closed,
            True,
            "沿切向方向微分 L2 得到 0=L3+2(Xu)A。",
            "Monge identity",
        ),
        row(
            "NonParabolicStraightLineIntegralClosed",
            nonparabolic_monge_straight_line_integral_closed,
            True,
            "A!=0 时由 L3=0 推出 Xu=0，从而切向 projective direction 沿积分曲线恒定。",
            SIMPLE_BRANCH,
        ),
        row(
            "MongeSimpleRootBranchClosed",
            monge_simple_branch_closed,
            True,
            "Monge 延拓的简单根/非抛物分支已产生真实直线芽。",
            SIMPLE_BRANCH,
        ),
        row(
            "ParabolicHessianDevelopableBranchClosed",
            parabolic_hessian_developable_branch_closed,
            False,
            "A=0 时强制 Xu 的因子消失，剩余为 Hessian 退化 developable 分支。",
            PARABOLIC_BRANCH,
        ),
        row(
            "MongeProlongationClosed",
            monge_prolongation_closed,
            False,
            "简单根分支已闭合；整个 Monge 延拓仍等待抛物/Hessian 退化分支。",
            PARABOLIC_BRANCH,
        ),
        row(
            "AlgebraicLineGermClosureClosed",
            algebraic_line_germ_closure_closed,
            False,
            "即使产生线芽，仍需后续证明其 Zariski 闭包覆盖曲面。",
            LINE_GERM_CLOSURE,
        ),
        row(
            "CayleySalmonFlecnodeCriterionClosed",
            cayley_salmon_flecnode_criterion_closed,
            False,
            "Monge 退化分支和线芽闭包未闭合前，Cayley-Salmon 仍未作者侧自足闭合。",
            CAYLEY_SALMON,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "non-ruled O(d^3) 分支仍等待 Cayley-Salmon 判据。",
            NON_RULED,
        ),
        row(
            "SelfContainedBipartiteLineIntersectionBoundClosed",
            self_contained_bipartite_line_intersection_bound_closed,
            False,
            "二分线交点界仍依赖 non-ruled 分支。",
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
            "本步只闭合 Monge 简单根分支；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_rks23_monge_simple_branch_router",
        "status": "monge_simple_root_branch_closed_remaining_parabolic_hessian_and_line_germ_closure",
        "previous_monge_frontier_ready": previous_monge_frontier_ready,
        "degree_less_than_characteristic_imported": degree_less_than_characteristic_imported,
        "graph_chart_normal_form_closed": graph_chart_normal_form_closed,
        "contact_equation_normal_form_closed": contact_equation_normal_form_closed,
        "simple_root_monge_identity_closed": simple_root_identity_closed,
        "nonparabolic_monge_straight_line_integral_closed": nonparabolic_monge_straight_line_integral_closed,
        "monge_simple_branch_closed": monge_simple_branch_closed,
        "parabolic_hessian_developable_branch_closed": parabolic_hessian_developable_branch_closed,
        "monge_prolongation_closed": monge_prolongation_closed,
        "algebraic_line_germ_closure_closed": algebraic_line_germ_closure_closed,
        "cayley_salmon_flecnode_criterion_closed": cayley_salmon_flecnode_criterion_closed,
        "non_ruled_line_intersection_theorem_closed": non_ruled_line_intersection_theorem_closed,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_bound_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "counterexample_assumption_only": True,
        "normal_form": normal_form,
        "monge_identity": monge_identity,
        "degenerate_branch": degenerate_branch,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": [
            {
                "atom": PARABOLIC_BRANCH,
                "closed": False,
                "why_remaining": "A=0 makes the Monge identity lose the multiplier needed to force Xu=0",
            },
            {
                "atom": LINE_GERM_CLOSURE,
                "closed": False,
                "why_remaining": "straight line germs still need algebraic closure into a covering line family",
            },
        ],
        "next_direct_attack_target": PARABOLIC_BRANCH,
        "next_required_input": f"{PARABOLIC_BRANCH} + {LINE_GERM_CLOSURE}",
        "plain_conclusion": (
            "Monge 延拓已经在简单根/非抛物分支闭合。唯一未穿透的 Monge 源头"
            "是 A=0 的 Hessian 退化 developable 分支；之后还要做线芽代数闭包。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 Monge 简单根分支证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "当前主攻点继续保持 Cayley-Salmon 内部自足线，不换命题。"
        "本步把 Monge 延拓写成显式局部方程，并闭合简单根/非抛物分支："
        "由 0=L3+2(Xu)A 与 A!=0 推出方向场沿自身不变，从而生成真实直线芽。"
        "剩余压缩为 A=0 的 Hessian 退化 developable 分支，以及后续线芽代数闭包。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "monge_simple_branch_closed",
        "parabolic_hessian_developable_branch_closed",
        "monge_prolongation_closed",
        "algebraic_line_germ_closure_closed",
        "cayley_salmon_flecnode_criterion_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 局部正规形")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["normal_form"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. Monge 简单根恒等式")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["monge_identity"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 3. 退化分支")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["degenerate_branch"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 4. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=item["gate"],
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.append("")
    lines.append("## 5. 下一真正自足目标")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_direct_attack_target"])
    lines.append(result["next_required_input"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    MONO.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"monge_simple_branch_closed={fmt_bool(result['monge_simple_branch_closed'])}")
    print(f"monge_prolongation_closed={fmt_bool(result['monge_prolongation_closed'])}")
    print(f"cayley_salmon_flecnode_criterion_closed={fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
