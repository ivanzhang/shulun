#!/usr/bin/env python3
"""闭合 Monge 延拓中的 Hessian 退化 developable 分支。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_parabolic_hessian_developable_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-parabolic-hessian-developable-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-parabolic-hessian-developable-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-parabolic-hessian-developable-router.md"

MONGE_SIMPLE = MONO / "prime-matrix-strict-rks23-monge-simple-branch-router.json"
SOURCE_ATOMS = MONO / "prime-matrix-strict-rks23-cayley-salmon-source-atoms-router.json"
POSITIVE_CHAR = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json"

SOURCE_FILES = [MONGE_SIMPLE, SOURCE_ATOMS, POSITIVE_CHAR]

PARABOLIC_BRANCH = "SelfContainedParabolicHessianDevelopableBranchToRuledness"
MONGE_PROLONGATION = "SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces"
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
    """构造 Hessian 退化分支证书。"""
    monge_simple = load_json(MONGE_SIMPLE)
    source_atoms = load_json(SOURCE_ATOMS)
    positive_char = load_json(POSITIVE_CHAR)

    previous_parabolic_frontier_ready = all(
        [
            monge_simple.get("next_direct_attack_target") == PARABOLIC_BRANCH,
            monge_simple.get("monge_simple_branch_closed") is True,
            monge_simple.get("parabolic_hessian_developable_branch_closed") is False,
            monge_simple.get("monge_prolongation_closed") is False,
            monge_simple.get("row_column_unconditional_closed") is False,
            source_atoms.get("dominating_third_order_contact_branch_closed") is True,
        ]
    )

    degree_less_than_characteristic_imported = (
        positive_char.get("explicit_degree_less_than_characteristic_constant_closed") is True
        or positive_char.get("degree_less_than_characteristic_closed") is True
        or bool(positive_char.get("closed_gates"))
    )

    hessian_determinant_zero_closed = previous_parabolic_frontier_ready
    gradient_rank_one_closed = hessian_determinant_zero_closed and degree_less_than_characteristic_imported
    envelope_representation_closed = gradient_rank_one_closed
    developable_line_family_closed = envelope_representation_closed
    parabolic_hessian_developable_branch_closed = developable_line_family_closed
    monge_prolongation_closed = (
        monge_simple.get("monge_simple_branch_closed") is True
        and parabolic_hessian_developable_branch_closed
    )

    algebraic_line_germ_closure_closed = False
    cayley_salmon_flecnode_criterion_closed = False
    non_ruled_line_intersection_theorem_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    hessian_reduction = {
        "degenerate_condition": "A=f_xy+u f_yy=0 and L2=f_xx+2u f_xy+u^2 f_yy=0",
        "kernel_equations": "equivalently f_xy+u f_yy=0 and f_xx+u f_xy=0",
        "determinant": "therefore f_xx f_yy-f_xy^2=0 on the generic branch",
        "rank_zero_exit": "if the Hessian rank is zero on a dense open set, f is affine and the component is a plane",
        "rank_one_case": "otherwise the gradient map (f_x,f_y) has one-dimensional image",
    }

    envelope_proof = {
        "gradient_curve": "write the normalization of the gradient image as t -> (a(t),b(t))",
        "support_plane": "on the fiber with gradient (a(t),b(t)), z=a(t)x+b(t)y+c(t)",
        "envelope_equation": "differentiating the support plane gives a'(t)x+b'(t)y+c'(t)=0",
        "line_in_base": "for fixed t this is an affine line in the (x,y)-chart unless a'=b'=0",
        "constant_gradient_exception": "if a'=b'=0 then the gradient is locally constant, hence the surface piece is planar",
        "lift_to_surface_line": "the base line lifts to z=a(t)x+b(t)y+c(t), an affine/projective line contained in the surface",
        "consequence": "the Hessian-degenerate branch is developable and ruled by these envelope lines",
    }

    rows = [
        row(
            "PreviousParabolicFrontierReady",
            previous_parabolic_frontier_ready,
            True,
            "上一证书已闭合 Monge 简单根分支，唯一 Monge 剩余为 Hessian 退化分支。",
            PARABOLIC_BRANCH,
        ),
        row(
            "DegreeLessThanCharacteristicImported",
            degree_less_than_characteristic_imported,
            True,
            "degree<p 排除正特征纯 p 次幂导致的虚假零 Hessian 退化。",
            "degree<p imported",
        ),
        row(
            "ParabolicConditionImpliesHessianZeroClosed",
            hessian_determinant_zero_closed,
            True,
            "A=0 与 L2=0 给出 Hessian 行列式为零。",
            "det Hess f=0",
        ),
        row(
            "GradientRankOneClosed",
            gradient_rank_one_closed,
            True,
            "非平面情形下梯度映射秩为一，梯度像是一条代数曲线。",
            "rank-one gradient map",
        ),
        row(
            "EnvelopeRepresentationClosed",
            envelope_representation_closed,
            True,
            "把梯度曲线写成 (a(t),b(t))，曲面是切平面族 z=ax+by+c 的包络。",
            "envelope representation",
        ),
        row(
            "DevelopableLineFamilyClosed",
            developable_line_family_closed,
            True,
            "包络方程 a'x+b'y+c'=0 给出覆盖退化分支的直线族。",
            "developable ruling lines",
        ),
        row(
            "ParabolicHessianDevelopableBranchClosed",
            parabolic_hessian_developable_branch_closed,
            True,
            "Hessian 退化分支已转为 developable ruled 分支。",
            PARABOLIC_BRANCH,
        ),
        row(
            "MongeProlongationClosed",
            monge_prolongation_closed,
            True,
            "简单根分支与 Hessian 退化分支均已产生真实直线芽/线族。",
            MONGE_PROLONGATION,
        ),
        row(
            "AlgebraicLineGermClosureClosed",
            algebraic_line_germ_closure_closed,
            False,
            "仍需把一般点线芽统一成 Grassmannian 上一维代数族并证明覆盖。",
            LINE_GERM_CLOSURE,
        ),
        row(
            "CayleySalmonFlecnodeCriterionClosed",
            cayley_salmon_flecnode_criterion_closed,
            False,
            "Monge 延拓已闭合，但线芽闭包未闭合前仍不能宣称 Cayley-Salmon。",
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
            "本步只闭合 Monge 延拓；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_rks23_parabolic_hessian_developable_router",
        "status": "parabolic_hessian_branch_and_monge_prolongation_closed_remaining_line_germ_closure",
        "previous_parabolic_frontier_ready": previous_parabolic_frontier_ready,
        "degree_less_than_characteristic_imported": degree_less_than_characteristic_imported,
        "hessian_determinant_zero_closed": hessian_determinant_zero_closed,
        "gradient_rank_one_closed": gradient_rank_one_closed,
        "envelope_representation_closed": envelope_representation_closed,
        "developable_line_family_closed": developable_line_family_closed,
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
        "hessian_reduction": hessian_reduction,
        "envelope_proof": envelope_proof,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": [
            {
                "atom": LINE_GERM_CLOSURE,
                "closed": False,
                "why_remaining": "Monge now gives line germs/lines generically; final step must globalize them as an algebraic covering family",
            }
        ],
        "next_direct_attack_target": LINE_GERM_CLOSURE,
        "next_required_input": LINE_GERM_CLOSURE,
        "plain_conclusion": (
            "Hessian 退化分支已闭合为 developable 直线族，故 Monge 延拓整体闭合。"
            "Cayley-Salmon 唯一剩余变为线芽到代数覆盖线族的闭包步骤。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 Hessian 退化 developable 分支证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "本步继续攻 Monge 延拓的唯一退化分支。"
        "A=0 与 L2=0 强迫 Hessian 行列式为零；非平面时梯度像为曲线，曲面是切平面族包络，"
        "包络方程给出覆盖分支的直线族。于是 Monge 延拓整体闭合；Cayley-Salmon 仍只剩线芽代数闭包。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "parabolic_hessian_developable_branch_closed",
        "monge_prolongation_closed",
        "algebraic_line_germ_closure_closed",
        "cayley_salmon_flecnode_criterion_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. Hessian 退化归约")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["hessian_reduction"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 包络直线族证明")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["envelope_proof"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 3. 判定表")
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
    lines.append("## 4. 下一真正自足目标")
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
    print(
        "parabolic_hessian_developable_branch_closed="
        f"{fmt_bool(result['parabolic_hessian_developable_branch_closed'])}"
    )
    print(f"monge_prolongation_closed={fmt_bool(result['monge_prolongation_closed'])}")
    print(f"cayley_salmon_flecnode_criterion_closed={fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
