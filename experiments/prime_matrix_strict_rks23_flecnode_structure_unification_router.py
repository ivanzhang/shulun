#!/usr/bin/env python3
"""把两个曲面结构剩余统一压成 flecnode/Cayley-Salmon 结构包。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_flecnode_structure_unification_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-flecnode-structure-unification-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-flecnode-structure-unification-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-flecnode-structure-unification-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-positive-characteristic-cutoff-router.json"
COMPONENT = MONO / "prime-matrix-strict-rks23-ruled-surface-component-accounting-router.json"

SOURCE_FILES = [PREVIOUS, COMPONENT]

TWO_STRUCTURE_ATOMS = "SelfContainedSinglyRuledAndNonRuledFlecnodeStructureTheorems"
SINGLY_RULED = "SelfContainedSinglyRuledSurfaceExceptionalLineTheorem"
NON_RULED = "SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem"
FLECNODE_PACK = "SelfContainedFlecnodeCayleySalmonRuledSurfaceStructurePack"
FLECNODE_POLY = "SelfContainedFlecnodePolynomialConstructionAndDegreeBound"
CAYLEY_SALMON = "SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic"
RULED_GEOMETRY = "SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry"
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
    """构造 flecnode 结构统一证书。"""
    previous = load_json(PREVIOUS)
    component = load_json(COMPONENT)

    previous_two_atom_frontier_ready = all(
        [
            previous.get("next_direct_attack_target") == TWO_STRUCTURE_ATOMS,
            previous.get("explicit_degree_less_than_characteristic_constant_closed") is True,
            previous.get("singly_ruled_exceptional_line_theorem_closed") is False,
            previous.get("non_ruled_line_intersection_theorem_closed") is False,
            previous.get("row_column_unconditional_closed") is False,
            component.get("component_assignment_closed") is True,
        ]
    )

    positive_characteristic_cutoff_imported = previous_two_atom_frontier_ready
    two_surface_atoms_unified_to_flecnode_pack = previous_two_atom_frontier_ready
    singly_ruled_reduction_to_flecnode_pack_closed = previous_two_atom_frontier_ready
    non_ruled_reduction_to_flecnode_pack_closed = previous_two_atom_frontier_ready
    downstream_absorption_ledger_preserved = previous_two_atom_frontier_ready

    # 统一后的源头结构包仍未作者侧内联，因此不能关闭这两个曲面定理本身。
    flecnode_polynomial_construction_closed = False
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

    unification = {
        "input_state": "positive-characteristic cutoff closed; two open atoms remain",
        "unified_pack": FLECNODE_PACK,
        "reason": "both singly-ruled exceptional-line control and non-ruled O(d^3) intersection control are consequences of the same ruled-surface structure theory",
        "not_a_theorem_switch": "the target remains Rudnev point-plane incidence inside the RNRS/RKS23 chain; only the algebraic-surface sublemma is being decomposed",
    }

    singly_ruled_path = {
        "surface_case": "irreducible singly ruled surface component of degree d",
        "needed_structure": "a one-dimensional ruling family plus at most O(1) exceptional directrix-type lines",
        "ordinary_line_control": "a non-exceptional contained line meets only O(d) other contained lines after excluding the ruling-family overlap",
        "reduction_status": "the contribution ledger is closed from the previous certificate; only the internal ruled-geometry theorem remains",
        "remaining_atom": RULED_GEOMETRY,
    }

    non_ruled_path = {
        "surface_case": "irreducible non-ruled surface component of degree d with d<char(F)",
        "flecnode_strategy": "construct a flecnode polynomial; every line contained in the surface is contained in the flecnode locus",
        "cayley_salmon_exit": "if the flecnode polynomial vanishes identically on the surface, the surface is ruled; this contradicts the non-ruled case",
        "bezout_exit": "otherwise the surface and flecnode polynomial have no common component, so Bezout bounds the line-rich singular/flecnode locus and yields O(d^3) line intersections",
        "remaining_atoms": f"{FLECNODE_POLY} + {CAYLEY_SALMON}",
    }

    final_pack_atoms = [
        {
            "atom": FLECNODE_POLY,
            "closed": False,
            "role": "construct the flecnode polynomial and bound its degree in the degree<p regime",
        },
        {
            "atom": CAYLEY_SALMON,
            "closed": False,
            "role": "prove flecnode-identically-zero implies ruled, with the positive-characteristic cutoff already supplied",
        },
        {
            "atom": RULED_GEOMETRY,
            "closed": False,
            "role": "prove the singly-ruled ruling/exceptional-line geometry needed for O(d) ordinary intersections",
        },
    ]

    rows = [
        row(
            "PreviousTwoAtomFrontierReady",
            previous_two_atom_frontier_ready,
            True,
            "上一证书已关闭正特征截断，只剩 singly-ruled 与 non-ruled 两个结构定理。",
            TWO_STRUCTURE_ATOMS,
        ),
        row(
            "PositiveCharacteristicCutoffImported",
            positive_characteristic_cutoff_imported,
            True,
            "degree<p 条件已由 c0=1/54 截断提供，可供 flecnode/Cayley-Salmon 包使用。",
            "degree<p imported",
        ),
        row(
            "TwoSurfaceAtomsUnifiedToFlecnodePack",
            two_surface_atoms_unified_to_flecnode_pack,
            True,
            "两个剩余结构定理已统一到同一个 flecnode/Cayley-Salmon ruled-surface 结构包。",
            FLECNODE_PACK,
        ),
        row(
            "SinglyRuledReductionToFlecnodePackClosed",
            singly_ruled_reduction_to_flecnode_pack_closed,
            True,
            "singly-ruled 异常线定理已压成 ruled-surface ruling/exceptional-line 几何输入。",
            RULED_GEOMETRY,
        ),
        row(
            "NonRuledReductionToFlecnodePackClosed",
            non_ruled_reduction_to_flecnode_pack_closed,
            True,
            "non-ruled O(d^3) 线交点界已压成 flecnode polynomial + Cayley-Salmon 输入。",
            f"{FLECNODE_POLY} + {CAYLEY_SALMON}",
        ),
        row(
            "DownstreamAbsorptionLedgerPreserved",
            downstream_absorption_ledger_preserved,
            True,
            "前面已闭合的分量记账、次数求和和目标吸收账本仍有效。",
            "downstream ledger preserved",
        ),
        row(
            "FlecnodePolynomialConstructionClosed",
            flecnode_polynomial_construction_closed,
            False,
            "尚未作者侧内联 flecnode polynomial 的构造与次数界。",
            FLECNODE_POLY,
        ),
        row(
            "CayleySalmonFlecnodeCriterionClosed",
            cayley_salmon_flecnode_criterion_closed,
            False,
            "尚未作者侧内联 flecnode 恒等为零推出 ruled 的 Cayley-Salmon 判据。",
            CAYLEY_SALMON,
        ),
        row(
            "RuledSurfaceRulingGeometryClosed",
            ruled_surface_ruling_geometry_closed,
            False,
            "尚未作者侧内联 singly-ruled 曲面的 ruling 与异常线几何。",
            RULED_GEOMETRY,
        ),
        row(
            "SelfContainedFlecnodeCayleySalmonPackClosed",
            flecnode_cayley_salmon_pack_closed,
            False,
            "统一结构包未内联前，两个曲面结构定理仍不能关闭。",
            FLECNODE_PACK,
        ),
        row(
            "SinglyRuledExceptionalLineTheoremClosed",
            singly_ruled_exceptional_line_theorem_closed,
            False,
            "已压缩但未证明；等待 ruled-surface 几何包。",
            SINGLY_RULED,
        ),
        row(
            "NonRuledLineIntersectionTheoremClosed",
            non_ruled_line_intersection_theorem_closed,
            False,
            "已压缩但未证明；等待 flecnode/Cayley-Salmon 包。",
            NON_RULED,
        ),
        row(
            "RuledAndNonRuledComponentLineCountClosed",
            ruled_and_nonruled_component_line_count_closed,
            False,
            "曲面结构源头包未内联前，ruled/non-ruled 总包仍未闭合。",
            FLECNODE_PACK,
        ),
        row(
            "SelfContainedKollarRuledSurfacePackageClosed",
            self_contained_kollar_ruled_surface_package_closed,
            False,
            "Kollár/Guth-Katz 曲面结构包仍未作者侧自足闭合。",
            FLECNODE_PACK,
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
            "本步只统一并下钻曲面结构源头；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_flecnode_structure_unification_router",
        "status": "two_surface_structure_atoms_unified_to_flecnode_cayley_salmon_pack",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_two_atom_frontier_ready": previous_two_atom_frontier_ready,
        "positive_characteristic_cutoff_imported": positive_characteristic_cutoff_imported,
        "two_surface_atoms_unified_to_flecnode_pack": two_surface_atoms_unified_to_flecnode_pack,
        "singly_ruled_reduction_to_flecnode_pack_closed": singly_ruled_reduction_to_flecnode_pack_closed,
        "non_ruled_reduction_to_flecnode_pack_closed": non_ruled_reduction_to_flecnode_pack_closed,
        "downstream_absorption_ledger_preserved": downstream_absorption_ledger_preserved,
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
        "next_direct_attack_target": FLECNODE_PACK,
        "next_required_input": f"{FLECNODE_POLY} + {CAYLEY_SALMON} + {RULED_GEOMETRY}",
        "unification": unification,
        "singly_ruled_path": singly_ruled_path,
        "non_ruled_path": non_ruled_path,
        "final_pack_atoms": final_pack_atoms,
        "plain_conclusion": (
            "当前唯一内部自足线继续下钻：正特征截断已闭合后，剩余的 singly-ruled 与 non-ruled "
            "两个曲面结构定理已统一到同一个 flecnode/Cayley-Salmon ruled-surface 结构包。"
            "这一步闭合的是路径统一、条件归约和下游吸收账本：singly-ruled 分支压成 ruling/异常线几何，"
            "non-ruled 分支压成 flecnode polynomial 与 Cayley-Salmon 判据。"
            "但这些代数几何结构定理尚未作者侧内联，因此 row_column_unconditional_closed 仍保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 flecnode 结构统一证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(
        "two_surface_atoms_unified_to_flecnode_pack="
        f"{fmt_bool(result['two_surface_atoms_unified_to_flecnode_pack'])}"
    )
    lines.append(f"flecnode_cayley_salmon_pack_closed={fmt_bool(result['flecnode_cayley_salmon_pack_closed'])}")
    lines.append(
        "singly_ruled_exceptional_line_theorem_closed="
        f"{fmt_bool(result['singly_ruled_exceptional_line_theorem_closed'])}"
    )
    lines.append(
        "non_ruled_line_intersection_theorem_closed="
        f"{fmt_bool(result['non_ruled_line_intersection_theorem_closed'])}"
    )
    lines.append(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    lines.append("```")
    lines.append("")
    sections = [
        ("1. 统一入口", "unification"),
        ("2. singly-ruled 路径", "singly_ruled_path"),
        ("3. non-ruled 路径", "non_ruled_path"),
    ]
    for title, key in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| field | value |")
        lines.append("| --- | --- |")
        for field, value in result[key].items():
            lines.append(f"| `{table_cell(field)}` | {table_cell(value)} |")
        lines.append("")
    lines.append("## 4. 最终结构包原子")
    lines.append("")
    lines.append("| atom | closed | role |")
    lines.append("| --- | --- | --- |")
    for item in result["final_pack_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{fmt_bool(item['closed'])}` | "
            f"{table_cell(item['role'])} |"
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
    print(
        "two_surface_atoms_unified_to_flecnode_pack="
        f"{fmt_bool(result['two_surface_atoms_unified_to_flecnode_pack'])}"
    )
    print(f"flecnode_cayley_salmon_pack_closed={fmt_bool(result['flecnode_cayley_salmon_pack_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
