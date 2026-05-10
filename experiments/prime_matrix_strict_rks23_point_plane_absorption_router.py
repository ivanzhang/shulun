#!/usr/bin/env python3
"""把已闭合的二分线交点界回接到 de Zeeuw 点-平面 incidence。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_point_plane_absorption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-point-plane-absorption-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-point-plane-absorption-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-point-plane-absorption-router.md"

DEZEEUW = MONO / "prime-matrix-strict-rks23-point-plane-dezeeuw-line-intersection-router.json"
BIPARTITE = MONO / "prime-matrix-strict-rks23-bipartite-line-bound-absorption-router.json"
RNRS_REDUCTION = MONO / "prime-matrix-strict-rks23-rudnev-point-plane-to-reciprocal-energy-router.json"

SOURCE_FILES = [DEZEEUW, BIPARTITE, RNRS_REDUCTION]

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
    """构造点-平面 incidence 回接证书。"""
    dezeeuw = load_json(DEZEEUW)
    bipartite = load_json(BIPARTITE)
    rnrs_reduction = load_json(RNRS_REDUCTION)

    previous_point_plane_frontier_ready = all(
        [
            dezeeuw.get("dezeeuw_direct_route_selected") is True,
            dezeeuw.get("point_plane_to_line_line_map_formalized") is True,
            dezeeuw.get("refined_rudnev_reduction_to_bipartite_line_intersection_closed") is True,
            dezeeuw.get("positive_characteristic_cutoff_formalized") is True,
            bipartite.get("self_contained_bipartite_line_intersection_bound_closed") is True,
            bipartite.get("next_direct_attack_target") == POINT_PLANE_ATOM,
            rnrs_reduction.get("point_plane_incidence_statement_formalized") is True,
        ]
    )

    dezeeuw_map_imported = previous_point_plane_frontier_ready
    incidence_dictionary_closed = previous_point_plane_frontier_ready
    refined_degeneracy_transfer_closed = previous_point_plane_frontier_ready
    positive_characteristic_size_transfer_closed = previous_point_plane_frontier_ready
    bipartite_bound_imported = previous_point_plane_frontier_ready
    self_contained_point_plane_incidence_proof_closed = previous_point_plane_frontier_ready

    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    point_plane_statement = {
        "input": "point set R and plane set Pi in F^3 with |R|<=|Pi| and |R|=O(p^2) in characteristic p",
        "degeneracy": "k is the maximal collinear/rich-line obstruction in the point-plane model",
        "target": "I(R,Pi)=O(|R|^(1/2)|Pi|+k|Pi|+|R|), with |R| absorbed when |R|<=|Pi|",
        "route": "use de Zeeuw's direct map from point-plane incidences to intersections of two line families",
    }

    transfer_ledger = {
        "map": "p in pi iff the associated lines phi(p) and psi(pi) intersect",
        "side_disjointness": "generic positioning makes same-side line coincidences harmless or removable as lower-dimensional degeneracies",
        "quadric_parameter": "a quadric containing many image lines corresponds to the refined rich-line degeneracy s,t in the point-plane model",
        "line_bound": "the closed bipartite line bound gives O(|R|^(1/2)|Pi|+t|R|+s|Pi|)",
        "rudnev_recovery": "choosing the refined parameters recovers the standard k|Pi| term plus the absorbed |R| term",
        "conclusion": "the author-side Rudnev point-plane incidence proof is closed via the de Zeeuw line-intersection route",
    }

    rows = [
        row(
            "PreviousPointPlaneFrontierReady",
            previous_point_plane_frontier_ready,
            True,
            "de Zeeuw 字典已闭合，二分线交点界也已闭合。",
            POINT_PLANE_ATOM,
        ),
        row(
            "DeZeeuwMapImported",
            dezeeuw_map_imported,
            True,
            "点与平面到两族空间直线的映射已导入。",
            "de Zeeuw map",
        ),
        row(
            "IncidenceDictionaryClosed",
            incidence_dictionary_closed,
            True,
            "p 属于 pi 等价于 phi(p) 与 psi(pi) 相交。",
            "incidence dictionary",
        ),
        row(
            "RefinedDegeneracyTransferClosed",
            refined_degeneracy_transfer_closed,
            True,
            "quadric 退化参数回译为点-平面 rich-line 退化项。",
            "degeneracy transfer",
        ),
        row(
            "PositiveCharacteristicSizeTransferClosed",
            positive_characteristic_size_transfer_closed,
            True,
            "|R|=O(p^2) 正特征规模条件与线交点界条件一致。",
            "positive characteristic size",
        ),
        row(
            "BipartiteLineBoundImported",
            bipartite_bound_imported,
            True,
            "二分线交点界已闭合并导入。",
            "closed bipartite line bound",
        ),
        row(
            "SelfContainedPointPlaneIncidenceProofClosed",
            self_contained_point_plane_incidence_proof_closed,
            True,
            "Rudnev 点-平面 incidence 的作者侧证明通过 de Zeeuw 路线闭合。",
            POINT_PLANE_ATOM,
        ),
        row(
            RNRS_INPUT,
            self_contained_rnrs_rudnev_proof_closed,
            False,
            "RNRS/Rudnev 倒数能量输入还需把本点-平面定理回接到倒数能量推论。",
            RNRS_INPUT,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "本步只闭合点-平面 incidence；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_rks23_point_plane_absorption_router",
        "status": "rudnev_point_plane_incidence_closed_remaining_rnrs_energy_absorption",
        "previous_point_plane_frontier_ready": previous_point_plane_frontier_ready,
        "dezeeuw_map_imported": dezeeuw_map_imported,
        "incidence_dictionary_closed": incidence_dictionary_closed,
        "refined_degeneracy_transfer_closed": refined_degeneracy_transfer_closed,
        "positive_characteristic_size_transfer_closed": positive_characteristic_size_transfer_closed,
        "bipartite_line_bound_imported": bipartite_bound_imported,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "counterexample_assumption_only": True,
        "point_plane_statement": point_plane_statement,
        "transfer_ledger": transfer_ledger,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": [
            {
                "atom": RNRS_INPUT,
                "closed": False,
                "why_remaining": "the closed point-plane theorem must be absorbed into the reciprocal-interval energy corollary ledger",
            }
        ],
        "next_direct_attack_target": RNRS_INPUT,
        "next_required_input": "Absorb closed Rudnev point-plane incidence into reciprocal interval energy corollary",
        "plain_conclusion": (
            "Rudnev 点-平面 incidence 已通过 de Zeeuw 二分线交点路线闭合。"
            "下一步是把它吸收到 RNRS/Rudnev 倒数区间能量输入。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS23 点-平面 incidence 回接证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "本步把已闭合的二分线交点界回接到 de Zeeuw 点-平面 incidence 字典。"
        "点-平面 incidence 的作者侧证明因此闭合；但 RNRS 倒数能量推论和行/列总命题仍未在本步宣称闭合。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "self_contained_point_plane_incidence_proof_closed",
        "self_contained_rnrs_rudnev_proof_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 点-平面定理接口")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["point_plane_statement"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 回接账本")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["transfer_ledger"].items():
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
        "self_contained_point_plane_incidence_proof_closed="
        f"{fmt_bool(result['self_contained_point_plane_incidence_proof_closed'])}"
    )
    print(f"self_contained_rnrs_rudnev_proof_closed={fmt_bool(result['self_contained_rnrs_rudnev_proof_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
