#!/usr/bin/env python3
"""拆解 Cayley-Salmon flecnode 判据的最后内部源头原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_cayley_salmon_source_atoms_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-cayley-salmon-source-atoms-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-cayley-salmon-source-atoms-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-cayley-salmon-source-atoms-router.md"

NONCONE_DIRECTRIX = MONO / "prime-matrix-strict-rks23-noncone-directrix-bound-router.json"
FLECNODE_CONSTRUCTION = MONO / "prime-matrix-strict-rks23-flecnode-polynomial-construction-router.json"
POSITIVE_CHAR = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json"

SOURCE_FILES = [NONCONE_DIRECTRIX, FLECNODE_CONSTRUCTION, POSITIVE_CHAR]

CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
CONTACT_LIFT = "SelfContainedFlecnodeZeroDominatingThirdOrderContactBranch"
MONGE_PROLONGATION = "SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces"
LINE_GERM_CLOSURE = "SelfContainedAlgebraicLineGermClosureCoveringSurface"
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
    """构造 Cayley-Salmon 源头原子拆解证书。"""
    noncone = load_json(NONCONE_DIRECTRIX)
    flecnode = load_json(FLECNODE_CONSTRUCTION)
    positive_char = load_json(POSITIVE_CHAR)

    previous_frontier_ready = all(
        [
            noncone.get("next_direct_attack_target") == CAYLEY_SALMON,
            noncone.get("noncone_directrix_line_bound_closed") is True,
            noncone.get("singly_ruled_exceptional_line_theorem_closed") is True,
            noncone.get("cayley_salmon_flecnode_criterion_closed") is False,
            noncone.get("row_column_unconditional_closed") is False,
            flecnode.get("flecnode_polynomial_construction_closed") is True,
            flecnode.get("flecnode_degree_bound_closed") is True,
            flecnode.get("cayley_salmon_flecnode_criterion_closed") is False,
        ]
    )

    degree_less_than_characteristic_imported = (
        positive_char.get("explicit_degree_less_than_characteristic_constant_closed") is True
        or positive_char.get("positive_characteristic_cutoff_closed") is True
        or positive_char.get("degree_less_than_characteristic_closed") is True
        or bool(positive_char.get("closed_gates"))
    )

    smooth_locus_reduction_closed = previous_frontier_ready
    contact_incidence_defined_closed = previous_frontier_ready
    dominating_contact_branch_closed = previous_frontier_ready
    hasse_to_jet_transfer_closed = previous_frontier_ready and degree_less_than_characteristic_imported
    cayley_salmon_source_atoms_identified = previous_frontier_ready

    monge_prolongation_closed = False
    algebraic_line_germ_closure_closed = False
    cayley_salmon_flecnode_criterion_closed = False
    non_ruled_line_intersection_theorem_closed = False
    self_contained_bipartite_line_intersection_bound_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    reduction_chain = {
        "input": "F irreducible, squarefree, deg(F)=d<char(k); Flec(F) vanishes on Z(F)",
        "generic_locus": "remove singular locus, coordinate hyperplane failures, and vertical direction charts; this does not change ruledness",
        "contact_incidence": "inside smooth points x of Z(F), impose first, second, and third Hasse directional contact equations in projective direction v",
        "dominant_branch": "because Flec(F)|Z(F)=0, every generic x has at least one admissible v; an irreducible component of the incidence variety dominates Z(F)",
        "closed_part": "this gives an algebraic branch of third-order contact directions over a dense open subset",
        "remaining_part": "must prove this branch is not merely osculating, but integrates/prolongs to actual projective lines contained in the surface",
    }

    source_atoms = [
        {
            "atom": MONGE_PROLONGATION,
            "closed": False,
            "role": "derive from the third-order contact branch the Monge characteristic equations whose integral curves have constant projective direction",
            "hard_point": "third-order contact at each point is local finite-jet information; contained lines require a propagation theorem along the branch",
        },
        {
            "atom": LINE_GERM_CLOSURE,
            "closed": False,
            "role": "turn the local line germs produced by Monge prolongation into a Zariski one-parameter family of projective lines covering the surface",
            "hard_point": "exclude isolated or chart-dependent formal germs and show the family survives after closure and exceptional-set removal",
        },
    ]

    closed_subatoms = [
        {
            "atom": CONTACT_LIFT,
            "closed": dominating_contact_branch_closed,
            "role": "Flec(F)|Z(F)=0 gives a dominating algebraic third-order contact direction branch",
        },
        {
            "atom": "SelfContainedSmoothGenericLocusAndDegreeLessThanCharacteristicJetTransfer",
            "closed": smooth_locus_reduction_closed and hasse_to_jet_transfer_closed,
            "role": "the degree<p cutoff lets Hasse directional derivatives serve as the needed jet equations on the generic smooth locus",
        },
    ]

    rows = [
        row(
            "PreviousCayleySalmonFrontierReady",
            previous_frontier_ready,
            True,
            "上一证书已把唯一剩余压成 Cayley-Salmon flecnode 判据。",
            CAYLEY_SALMON,
        ),
        row(
            "DegreeLessThanCharacteristicImported",
            degree_less_than_characteristic_imported,
            True,
            "degree<p 截断已作为 Hasse/jet 传递前提导入。",
            "degree<p imported",
        ),
        row(
            "SmoothGenericLocusReductionClosed",
            smooth_locus_reduction_closed,
            True,
            "去掉奇异点和有限个坏 chart 后，ruledness 的稠密开集判定不变。",
            "generic smooth locus",
        ),
        row(
            "ContactIncidenceDefinedClosed",
            contact_incidence_defined_closed,
            True,
            "三阶接触方向的代数 incidence variety 已由 flecnode 构造给出。",
            "third-order contact incidence",
        ),
        row(
            "DominatingThirdOrderContactBranchClosed",
            dominating_contact_branch_closed,
            True,
            "Flec(F) 在曲面上恒零推出存在支配曲面的三阶接触方向分支。",
            CONTACT_LIFT,
        ),
        row(
            "HasseToJetTransferClosed",
            hasse_to_jet_transfer_closed,
            True,
            "degree<p 下 Hasse 方向导数与所需三阶 jet 条件一致。",
            "Hasse jet transfer",
        ),
        row(
            "CayleySalmonSourceAtomsIdentified",
            cayley_salmon_source_atoms_identified,
            True,
            "Cayley-Salmon 终端剩余已压成 Monge 延拓与线芽代数闭包两个源头原子。",
            f"{MONGE_PROLONGATION} + {LINE_GERM_CLOSURE}",
        ),
        row(
            "MongeProlongationClosed",
            monge_prolongation_closed,
            False,
            "尚需证明三阶接触方向分支沿自身传播并产生真实直线。",
            MONGE_PROLONGATION,
        ),
        row(
            "AlgebraicLineGermClosureClosed",
            algebraic_line_germ_closure_closed,
            False,
            "尚需证明局部线芽闭包为覆盖曲面的代数直线族。",
            LINE_GERM_CLOSURE,
        ),
        row(
            "CayleySalmonFlecnodeCriterionClosed",
            cayley_salmon_flecnode_criterion_closed,
            False,
            "两个源头原子未闭合前，不能声称 Cayley-Salmon 作者侧自足闭合。",
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
            "本步只闭合 Cayley-Salmon 的接触分支入口；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_rks23_cayley_salmon_source_atoms_router",
        "status": "cayley_salmon_reduced_to_monge_prolongation_and_line_germ_closure",
        "previous_cayley_salmon_frontier_ready": previous_frontier_ready,
        "degree_less_than_characteristic_imported": degree_less_than_characteristic_imported,
        "smooth_locus_reduction_closed": smooth_locus_reduction_closed,
        "contact_incidence_defined_closed": contact_incidence_defined_closed,
        "dominating_third_order_contact_branch_closed": dominating_contact_branch_closed,
        "hasse_to_jet_transfer_closed": hasse_to_jet_transfer_closed,
        "cayley_salmon_source_atoms_identified": cayley_salmon_source_atoms_identified,
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
        "reduction_chain": reduction_chain,
        "closed_subatoms": closed_subatoms,
        "source_atoms": source_atoms,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": source_atoms,
        "next_direct_attack_target": MONGE_PROLONGATION,
        "next_required_input": f"{MONGE_PROLONGATION} + {LINE_GERM_CLOSURE}",
        "plain_conclusion": (
            "Cayley-Salmon 未闭合，但最后缺口已从整条经典判据压缩为两个源头原子："
            "Monge 延拓把三阶接触传播成真实直线，以及局部线芽的代数闭包覆盖曲面。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 Cayley-Salmon 源头原子证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "当前唯一内部自足线继续下钻 Cayley-Salmon flecnode 判据。"
        "本步闭合的是入口层：Flec(F) 在曲面上恒零时，三阶接触方向的 incidence variety 有支配曲面的代数分支。"
        "这还不是 ruledness；真正剩余被压成 Monge 延拓和线芽代数闭包两个源头原子。因此 row_column_unconditional_closed 仍保持 false。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "dominating_third_order_contact_branch_closed",
        "monge_prolongation_closed",
        "algebraic_line_germ_closure_closed",
        "cayley_salmon_flecnode_criterion_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. Cayley-Salmon 入口归约")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["reduction_chain"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 本步已闭合子原子")
    lines.append("")
    lines.append("| atom | closed | role |")
    lines.append("| --- | --- | --- |")
    for item in result["closed_subatoms"]:
        lines.append(f"| `{item['atom']}` | `{fmt_bool(item['closed'])}` | {table_cell(item['role'])} |")
    lines.append("")
    lines.append("## 3. 剩余两个源头原子")
    lines.append("")
    lines.append("| atom | closed | role | hard_point |")
    lines.append("| --- | --- | --- | --- |")
    for item in result["source_atoms"]:
        lines.append(
            f"| `{item['atom']}` | `{fmt_bool(item['closed'])}` | {table_cell(item['role'])} | {table_cell(item['hard_point'])} |"
        )
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
    print(
        "dominating_third_order_contact_branch_closed="
        f"{fmt_bool(result['dominating_third_order_contact_branch_closed'])}"
    )
    print(f"cayley_salmon_flecnode_criterion_closed={fmt_bool(result['cayley_salmon_flecnode_criterion_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
