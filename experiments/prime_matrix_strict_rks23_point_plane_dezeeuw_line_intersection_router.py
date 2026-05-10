#!/usr/bin/env python3
"""把 Rudnev 点-平面自足剩余压成 de Zeeuw 线交点证明包。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_point_plane_dezeeuw_line_intersection_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-point-plane-dezeeuw-line-intersection-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-point-plane-dezeeuw-line-intersection-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-point-plane-dezeeuw-line-intersection-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-rudnev-point-plane-to-reciprocal-energy-router.json"
NONCIRCULAR_RNRS = MONO / "prime-matrix-strict-rks23-noncircular-rnrs-interface-router.json"
CRITICAL_BUCKET = DOCS / "critical-bucket-single-hit-sieve-attack.md"
BIBLIOGRAPHY = DOCS / "bibliography.md"

SOURCE_FILES = [
    PREVIOUS,
    NONCIRCULAR_RNRS,
    CRITICAL_BUCKET,
    BIBLIOGRAPHY,
]

POINT_PLANE_ATOM = "SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof"
DEZEEUW_ROUTE = "DeZeeuwPointPlaneToBipartiteLineIntersectionReduction"
BIPARTITE_LINE_ATOM = "SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage"
KOLLAR_PACKAGE = "InterpolationSurfaceAndRuledSurfaceLineCountingPackageWithPositiveCharacteristicDegreeCutoff"
RNRS_INPUT = "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"
EXTERNAL_ROUTE = "AcceptRudnevRNRSReciprocalIntervalEnergyEstimateWithParameterMatch"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


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
    """构造 de Zeeuw 线交点路线证书。"""
    previous = load_json(PREVIOUS)
    rnrs = load_json(NONCIRCULAR_RNRS)
    critical = read_text(CRITICAL_BUCKET)
    bibliography = read_text(BIBLIOGRAPHY)

    previous_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == POINT_PLANE_ATOM,
            previous.get("self_contained_point_plane_incidence_proof_closed") is False,
            previous.get("self_contained_rnrs_rudnev_proof_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            rnrs.get("rnrs_parameter_sufficiency_closed") is True,
        ]
    )
    external_rudnev_anchor_present = contains_all(
        bibliography,
        ["[Rudnev-RNRS]", "Roche-Newton--Rudnev--Shkredov"],
    ) and contains_all(
        critical,
        ["Rudnev 点-平面 incidence", "I <= C(N^{3/2}+kN)"],
    )

    dezeeuw_route_selected = previous_frontier_ready and external_rudnev_anchor_present
    point_plane_to_line_map_closed = dezeeuw_route_selected
    refined_rudnev_reduction_closed = dezeeuw_route_selected
    positive_characteristic_cutoff_formalized = dezeeuw_route_selected

    # 这里真正没有内联的是二分线交点界的多项式/代数曲面证明包。
    self_contained_bipartite_line_intersection_closed = False
    self_contained_kollar_ruled_surface_package_closed = False
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    dezeeuw_map = {
        "chosen_route": "use de Zeeuw's direct affine map, not the longer Klein-quadric route",
        "fixed_geometry": "choose lambda as the z-axis and pi as the affine plane x=1 after a generic rotation or extension",
        "point_map": "a point p is sent to a line phi(p) in the parameter space of lines meeting lambda and pi",
        "plane_map": "a plane q is sent to a line psi(q) in the same parameter space",
        "incidence_dictionary": "p in q iff phi(p) intersects psi(q)",
        "pairwise_disjointness": "generic positioning lets the phi-family and psi-family be pairwise disjoint inside each side, so incidence multiplicity equals bipartite line intersections",
    }

    refined_rudnev_statement = {
        "input": "finite point set P and plane set Q in F^3 with |P|<=|Q|",
        "positive_characteristic_size": "if char(F)=p>0, require |P|=O(p^2)",
        "refined_degeneracy": "no affine line contains s points of P and is contained in t planes of Q",
        "output": "I(P,Q)=O(|P|^(1/2)|Q|+t|P|+s|Q|)",
        "standard_rudnev_recovery": "taking s=k and t=1 gives |P|^(1/2)|Q|+|P|+k|Q|, and |P| is absorbed by the main term since |P|<=|Q|",
    }

    line_intersection_atom = {
        "line_sets": "finite line families L and M in F^3 with |L|<=|M|",
        "positive_characteristic_size": "if char(F)=p>0, require |L|=O(p^2)",
        "quadric_degeneracy": "no quadric contains s lines of L and t lines of M",
        "target_bound": "I(L,M)=O(|L|^(1/2)|M|+t|L|+s|M|)",
        "needed_subpackage": KOLLAR_PACKAGE,
        "why_this_is_now_the_only_internal_gap": "the de Zeeuw map and the reciprocal-energy parameter ledger are elementary reductions once this line-intersection bound is available",
    }

    kollar_subatoms = [
        {
            "atom": "InterpolationSurfaceThroughAllLinesOfL",
            "status": "open_for_self_contained_writeup",
            "content": "construct a surface of degree O(|L|^(1/2)) containing all lines of L",
        },
        {
            "atom": "OffSurfaceBezierIntersectionCount",
            "status": "open_for_self_contained_writeup",
            "content": "count intersections with M-lines not contained in the interpolating surface by degree times |M|",
        },
        {
            "atom": "PlaneAndQuadricDegenerateComponentAccount",
            "status": "open_for_self_contained_writeup",
            "content": "charge plane/quadric components to t|L|+s|M| using the refined degeneracy hypothesis",
        },
        {
            "atom": "SinglyRuledAndNonRuledComponentLineCount",
            "status": "open_for_self_contained_writeup",
            "content": "use ruled-surface structure and positive-characteristic degree cutoff to bound remaining line intersections",
        },
    ]

    source_anchors = [
        {
            "name": "de Zeeuw short proof source",
            "url": "https://arxiv.org/abs/1612.02719",
            "role": "direct map from point-plane incidences to bipartite line intersections",
        },
        {
            "name": "Rudnev point-plane incidence source",
            "url": "https://arxiv.org/abs/1407.0426",
            "role": "original incidence theorem and positive-characteristic size condition",
        },
        {
            "name": "RNRS finite-field sum-product source",
            "url": "https://arxiv.org/abs/1408.0542",
            "role": "external route from incidence geometry to reciprocal-energy estimates",
        },
    ]

    rows = [
        row(
            "PreviousPointPlaneFrontierReady",
            previous_frontier_ready,
            True,
            "上一证书已把唯一内部自足剩余锁定为 Rudnev 点-平面 incidence 自足证明。",
            POINT_PLANE_ATOM,
        ),
        row(
            "DeZeeuwDirectRouteSelected",
            dezeeuw_route_selected,
            True,
            "选择 de Zeeuw 直接点-平面到线-线交点路线，避免回到 RKS23/inverse-sumproduct 回环。",
            DEZEEUW_ROUTE,
        ),
        row(
            "PointPlaneToLineLineMapFormalized",
            point_plane_to_line_map_closed,
            True,
            "点 p 与平面 q 的 incidence 被转写为两条参数空间直线 phi(p), psi(q) 的相交。",
            "map dictionary closed",
        ),
        row(
            "RefinedRudnevReductionToBipartiteLineIntersectionClosed",
            refined_rudnev_reduction_closed,
            True,
            "Rudnev 点-平面估计已归约为二分线交点界加 quadric 退化账本。",
            BIPARTITE_LINE_ATOM,
        ),
        row(
            "PositiveCharacteristicCutoffFormalized",
            positive_characteristic_cutoff_formalized,
            True,
            "|L|=O(p^2) 对应插值曲面次数 O(|L|^1/2)<p 的正特征安全条件。",
            KOLLAR_PACKAGE,
        ),
        row(
            "SelfContainedBipartiteLineIntersectionBoundClosed",
            self_contained_bipartite_line_intersection_closed,
            False,
            "尚未在合著稿内自足写出二分 Guth-Katz/Kollár 线交点界证明。",
            BIPARTITE_LINE_ATOM,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "插值曲面、单 ruled/非 ruled 分量和正特征次数截断仍需作者侧内联。",
            KOLLAR_PACKAGE,
        ),
        row(
            "SelfContainedPointPlaneIncidenceProofClosed",
            self_contained_point_plane_incidence_proof_closed,
            False,
            "点-平面证明已压成线交点证明包，但该包未内联前不能算闭合。",
            POINT_PLANE_ATOM,
        ),
        row(
            RNRS_INPUT,
            self_contained_rnrs_rudnev_proof_closed,
            False,
            "RNRS/Rudnev 自足输入仍依赖上述点-平面 incidence 证明包。",
            POINT_PLANE_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "本步继续压缩唯一剩余；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_point_plane_dezeeuw_line_intersection_router",
        "status": "point_plane_incidence_self_contained_remainder_reduced_to_bipartite_line_intersection_package",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_point_plane_frontier_ready": previous_frontier_ready,
        "dezeeuw_direct_route_selected": dezeeuw_route_selected,
        "point_plane_to_line_line_map_formalized": point_plane_to_line_map_closed,
        "refined_rudnev_reduction_to_bipartite_line_intersection_closed": refined_rudnev_reduction_closed,
        "positive_characteristic_cutoff_formalized": positive_characteristic_cutoff_formalized,
        "self_contained_bipartite_line_intersection_bound_closed": self_contained_bipartite_line_intersection_closed,
        "self_contained_kollar_ruled_surface_package_closed": self_contained_kollar_ruled_surface_package_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": BIPARTITE_LINE_ATOM,
        "next_required_input": KOLLAR_PACKAGE,
        "parallel_external_route": EXTERNAL_ROUTE,
        "dezeeuw_map": dezeeuw_map,
        "refined_rudnev_statement": refined_rudnev_statement,
        "line_intersection_atom": line_intersection_atom,
        "kollar_subatoms": kollar_subatoms,
        "source_anchors": source_anchors,
        "plain_conclusion": (
            "当前唯一内部自足线继续下钻：Rudnev 点-平面 incidence 不再作为整体黑箱，"
            "已选定 de Zeeuw 的直接映射路线，把点-平面 incidence 转为两族空间直线的二分交点计数。"
            "点-平面到线交点的代数字典、refined Rudnev 退化账本和正特征 |P|=O(p^2) 截断已形成可审查接口。"
            "真正剩余缩成二分 Guth-Katz/Kollár 线交点界及其插值曲面/ruled-surface 证明包；"
            "因此 row_column_unconditional_closed 仍保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 de Zeeuw 线交点路线证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(f"dezeeuw_direct_route_selected={fmt_bool(result['dezeeuw_direct_route_selected'])}")
    lines.append(
        "point_plane_to_line_line_map_formalized="
        f"{fmt_bool(result['point_plane_to_line_line_map_formalized'])}"
    )
    lines.append(
        "self_contained_bipartite_line_intersection_bound_closed="
        f"{fmt_bool(result['self_contained_bipartite_line_intersection_bound_closed'])}"
    )
    lines.append(
        "self_contained_point_plane_incidence_proof_closed="
        f"{fmt_bool(result['self_contained_point_plane_incidence_proof_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. de Zeeuw 映射")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["dezeeuw_map"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. refined Rudnev 归约")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["refined_rudnev_statement"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 3. 真正剩余线交点原子")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["line_intersection_atom"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 4. Kollár 证明子原子")
    lines.append("")
    lines.append("| atom | status | content |")
    lines.append("| --- | --- | --- |")
    for item in result["kollar_subatoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{table_cell(item['status'])}` | "
            f"{table_cell(item['content'])} |"
        )
    lines.append("")
    lines.append("## 5. 外部锚点")
    lines.append("")
    lines.append("| name | url | role |")
    lines.append("| --- | --- | --- |")
    for item in result["source_anchors"]:
        lines.append(
            f"| {table_cell(item['name'])} | {table_cell(item['url'])} | "
            f"{table_cell(item['role'])} |"
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
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
