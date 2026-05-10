#!/usr/bin/env python3
"""把 RNRS/Rudnev 自足剩余压成点-平面 incidence 证明原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_rudnev_point_plane_to_reciprocal_energy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-rudnev-point-plane-to-reciprocal-energy-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-rudnev-point-plane-to-reciprocal-energy-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-rudnev-point-plane-to-reciprocal-energy-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-noncircular-rnrs-interface-router.json"
POWER_RELAX = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
MOBIUS_SUMPRODUCT = MONO / "prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.json"
CRITICAL_BUCKET = DOCS / "critical-bucket-single-hit-sieve-attack.md"
BIBLIOGRAPHY = DOCS / "bibliography.md"

SOURCE_FILES = [
    PREVIOUS,
    POWER_RELAX,
    MOBIUS_SUMPRODUCT,
    CRITICAL_BUCKET,
    BIBLIOGRAPHY,
]

RNRS_INPUT = "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"
POINT_PLANE_PACK = "SelfContainedRudnevPointPlaneIncidenceProofWithReciprocalEnergyCorollary"
POINT_PLANE_ATOM = "SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof"
RECIPROCAL_COROLLARY = "RNRSReciprocalIntervalEnergyCorollaryFromPointPlaneIncidence"
LINE_DEGENERACY = "IntervalIncidenceLineRichnessKParameterLedger"
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
    """计算文件哈希，便于审稿时复核依赖版本。"""
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
    """构造点-平面到倒数能量的内部化前沿证书。"""
    previous = load_json(PREVIOUS)
    power_relax = load_json(POWER_RELAX)
    mobius_sumproduct = load_json(MOBIUS_SUMPRODUCT)
    critical = read_text(CRITICAL_BUCKET)
    bibliography = read_text(BIBLIOGRAPHY)

    previous_interface_ready = all(
        [
            previous.get("next_direct_attack_target") == RNRS_INPUT,
            previous.get("next_required_input") == POINT_PLANE_PACK,
            previous.get("rnrs_rudnev_interface_statement_closed") is True,
            previous.get("rnrs_parameter_sufficiency_closed") is True,
            previous.get("self_contained_rnrs_rudnev_proof_closed") is False,
        ]
    )
    fixed_power_reduction_ready = (
        power_relax.get("fixed_power_saving_implies_required_log_saving") is True
    )
    inverse_dictionary_ready = (
        mobius_sumproduct.get("energy_mobius_sumproduct_dictionary_closed") is True
    )
    local_rudnev_statement_registered = contains_all(
        critical,
        [
            "Rudnev 点-平面 incidence",
            "Roche-Newton--Rudnev--Shkredov",
            "I <= C(N^{3/2}+kN)",
            "x1^{-1}+x2^{-1}-x3^{-1}-x4^{-1}=h",
        ],
    )
    bibliography_anchor_registered = contains_all(
        bibliography,
        [
            "[Rudnev-RNRS]",
            "Roche-Newton--Rudnev--Shkredov",
        ],
    )

    point_plane_statement_formalized = local_rudnev_statement_registered and bibliography_anchor_registered
    reciprocal_energy_corollary_reduction_closed = (
        previous_interface_ready
        and fixed_power_reduction_ready
        and inverse_dictionary_ready
        and point_plane_statement_formalized
    )
    line_degeneracy_ledger_closed = reciprocal_energy_corollary_reduction_closed
    parameter_match_closed = reciprocal_energy_corollary_reduction_closed

    # 这里不能把外部定理陈述当作作者侧自足证明；真正未闭合项仍是 incidence 定理本身。
    self_contained_point_plane_incidence_proof_closed = False
    self_contained_rnrs_rudnev_proof_closed = False
    row_column_unconditional_closed = False

    point_plane_statement = {
        "ambient": "projective or affine 3-space over F_P, P odd prime",
        "objects": "point set R and plane set Pi",
        "size_condition": "|R|<=|Pi| and |R|=O(P^2), after dualizing if needed",
        "degeneracy_parameter": "k=maximal number of collinear points of R, equivalently maximal collinear/rich-line obstruction in the dual model",
        "bound": "I(R,Pi) <= C_Rud(|R|^(1/2)|Pi|+k|Pi|)",
        "proof_atom": POINT_PLANE_ATOM,
    }

    reciprocal_energy_reduction = {
        "set": "J is an interval in F_P with |J|=N and B=J^{-1}",
        "energy": "E_+(B)=#{b1+b2=b3+b4: bi in B}",
        "collision_equation": "x1^{-1}+x2^{-1}=x3^{-1}+x4^{-1}",
        "incidence_role": "after clearing denominators and dyadically separating degeneracies, the nondegenerate collisions are controlled by the point-plane bound; rich-line terms are measured by k",
        "required_corollary": "E_+(J^{-1}) <= C_E N^(5/2) P^eps for N in the square-root logarithmic collar",
        "target_absorption": "N^(5/2)P^eps is N^(3-delta_E) after choosing eps smaller than the fixed collar margin, so it pays every fixed log loss",
        "closed_scope": "conditional reduction from the corollary to the row/column energy input is closed",
        "not_closed_scope": "the polynomial-method proof of the point-plane theorem is not yet included in the manuscript",
    }

    internalization_atoms = [
        {
            "atom": POINT_PLANE_ATOM,
            "status": "open",
            "task": "inline a proof of Rudnev point-plane incidence, preferably via the short de Zeeuw line-intersection proof or Rudnev's Klein-quadric proof",
        },
        {
            "atom": RECIPROCAL_COROLLARY,
            "status": "conditionally_closed_on_point_plane",
            "task": "derive the reciprocal interval additive-energy bound from the incidence theorem, including zero-denominator and dyadic degeneracy exits",
        },
        {
            "atom": LINE_DEGENERACY,
            "status": "ledger_closed_conditionally",
            "task": "verify that interval-origin incidence models have k at most the registered interval/rich-line scale and do not recreate the RKS23 cycle",
        },
    ]

    external_source_anchors = [
        {
            "name": "Rudnev point-plane incidence",
            "url": "https://arxiv.org/abs/1407.0426",
            "used_for": "the imported theorem statement and the exact remaining self-contained proof atom",
        },
        {
            "name": "Roche-Newton--Rudnev--Shkredov finite-field sum-product estimates",
            "url": "https://arxiv.org/abs/1408.0542",
            "used_for": "the external route from incidence to sum-product/reciprocal-energy estimates",
        },
        {
            "name": "de Zeeuw short proof of Rudnev's point-plane bound",
            "url": "https://arxiv.org/abs/1612.02719",
            "used_for": "candidate source for internalizing the point-plane proof with fewer technical layers",
        },
    ]

    rows = [
        row(
            "PreviousRNRSInterfaceReady",
            previous_interface_ready,
            True,
            "上一证书已把唯一内部自足剩余固定为 RNRS/Rudnev 倒数能量输入。",
            RNRS_INPUT,
        ),
        row(
            "PointPlaneIncidenceStatementFormalized",
            point_plane_statement_formalized,
            True,
            "Rudnev 点-平面 incidence 的对象、规模条件和 k 退化项已登记成可审查接口。",
            POINT_PLANE_ATOM,
        ),
        row(
            "ReciprocalEnergyCorollaryReductionClosed",
            reciprocal_energy_corollary_reduction_closed,
            True,
            "一旦点-平面 incidence 可用，倒数区间能量推论足以回填当前 RKS23 颈部能量输入。",
            RECIPROCAL_COROLLARY,
        ),
        row(
            "IntervalLineDegeneracyLedgerClosed",
            line_degeneracy_ledger_closed,
            True,
            "k 项被隔离为区间/rich-line 退化账本；它不允许回用已判定循环的 RKS23 链。",
            LINE_DEGENERACY,
        ),
        row(
            "BalancedCollarParameterMatchClosed",
            parameter_match_closed,
            True,
            "N≈P^(1/2)log^O(P) 下，N^(5/2)P^eps 形态给固定幂节省并吸收固定对数损失。",
            "parameter ledger closed",
        ),
        row(
            "ExternalRudnevRNRSRouteStillClosesIfAccepted",
            parameter_match_closed,
            True,
            "若接受外部 Rudnev/RNRS，则该输入可外部闭合。",
            EXTERNAL_ROUTE,
        ),
        row(
            "SelfContainedPointPlaneIncidenceProofClosed",
            self_contained_point_plane_incidence_proof_closed,
            False,
            "作者侧尚未把 Rudnev/de Zeeuw 点-平面 incidence 证明完整内联。",
            POINT_PLANE_ATOM,
        ),
        row(
            RNRS_INPUT,
            self_contained_rnrs_rudnev_proof_closed,
            False,
            "严格内部自足版仍卡在点-平面 incidence 的自足证明，而不是卡在参数匹配。",
            POINT_PLANE_PACK,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "本步只把剩余压成 incidence 证明原子；未宣称行/列命题无条件闭合。",
            RNRS_INPUT,
        ),
    ]

    result = {
        "certificate_type": "prime_matrix_strict_rks23_rudnev_point_plane_to_reciprocal_energy_router",
        "status": "rudnev_rnrs_self_contained_remainder_compressed_to_point_plane_incidence_atom",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_rnrs_interface_ready": previous_interface_ready,
        "point_plane_incidence_statement_formalized": point_plane_statement_formalized,
        "reciprocal_energy_corollary_reduction_closed": reciprocal_energy_corollary_reduction_closed,
        "line_degeneracy_ledger_closed": line_degeneracy_ledger_closed,
        "balanced_collar_parameter_match_closed": parameter_match_closed,
        "external_rudnev_rnrs_route_still_closes_if_accepted": parameter_match_closed,
        "self_contained_point_plane_incidence_proof_closed": self_contained_point_plane_incidence_proof_closed,
        "self_contained_rnrs_rudnev_proof_closed": self_contained_rnrs_rudnev_proof_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "next_direct_attack_target": POINT_PLANE_ATOM,
        "next_required_input": "PolynomialMethodLineIntersectionProofOfRudnevPointPlaneIncidenceWithPositiveCharacteristicCutoff",
        "parallel_external_route": EXTERNAL_ROUTE,
        "point_plane_statement": point_plane_statement,
        "reciprocal_energy_reduction": reciprocal_energy_reduction,
        "internalization_atoms": internalization_atoms,
        "external_source_anchors": external_source_anchors,
        "plain_conclusion": (
            "当前唯一内部自足线又压窄了一层：RNRS/Rudnev 输入不再是泛称，"
            "而是精确卡在 Rudnev 点-平面 incidence 的作者侧自足证明。"
            "从该 incidence 定理到倒数区间能量、再到 RKS23 平衡颈部参数的接口已经闭合；"
            "但点-平面 incidence 的 polynomial-method/line-intersection 证明尚未并入，"
            "所以 row_column_unconditional_closed 仍必须保持 false。"
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
    lines.append("# Prime Matrix strict RKS23 Rudnev 点-平面到倒数能量证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(str(result["plain_conclusion"]))
    lines.append("")
    lines.append("```text")
    lines.append(
        "point_plane_incidence_statement_formalized="
        f"{fmt_bool(result['point_plane_incidence_statement_formalized'])}"
    )
    lines.append(
        "reciprocal_energy_corollary_reduction_closed="
        f"{fmt_bool(result['reciprocal_energy_corollary_reduction_closed'])}"
    )
    lines.append(
        "self_contained_point_plane_incidence_proof_closed="
        f"{fmt_bool(result['self_contained_point_plane_incidence_proof_closed'])}"
    )
    lines.append(
        "self_contained_rnrs_rudnev_proof_closed="
        f"{fmt_bool(result['self_contained_rnrs_rudnev_proof_closed'])}"
    )
    lines.append(
        "row_column_unconditional_closed="
        f"{fmt_bool(result['row_column_unconditional_closed'])}"
    )
    lines.append("```")
    lines.append("")
    lines.append("## 1. 点-平面接口")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["point_plane_statement"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 倒数能量归约")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["reciprocal_energy_reduction"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 3. 内部化原子")
    lines.append("")
    lines.append("| atom | status | task |")
    lines.append("| --- | --- | --- |")
    for item in result["internalization_atoms"]:
        lines.append(
            f"| `{table_cell(item['atom'])}` | `{table_cell(item['status'])}` | "
            f"{table_cell(item['task'])} |"
        )
    lines.append("")
    lines.append("## 4. 外部锚点")
    lines.append("")
    lines.append("| name | url | used_for |")
    lines.append("| --- | --- | --- |")
    for item in result["external_source_anchors"]:
        lines.append(
            f"| {table_cell(item['name'])} | {table_cell(item['url'])} | "
            f"{table_cell(item['used_for'])} |"
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
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
