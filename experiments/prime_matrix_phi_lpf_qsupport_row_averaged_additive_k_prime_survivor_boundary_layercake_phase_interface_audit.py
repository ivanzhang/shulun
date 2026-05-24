#!/usr/bin/env python3
"""审计 boundary layer-cake rectangles 的相位接口形状。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_phase_interface_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-audit.json

上一层已经把三条 monotone boundary strips 分解成 6190 个
q-prefix x prime-m-shell product rectangles。本层继续问一个更窄的问题：
这些 product rectangles 是否真的已经是可直接调用 Type-II/trace/Kloosterman
估计的长双变量对象？

有限审计显示，多数边数确实在 q,m 双变量层内；但 m-shell 总是很短，审计范围
内最大只有 12 个素数。因此直接逐层套用长变量 Type-II 定理会留下短 shell、
移动 q 分母和跨层求和损耗。这个脚本记录该接口形状，不宣称闭合相位节省。
"""

from __future__ import annotations

import hashlib
import json
import math
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_rectangles_audit as layercake  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit as bulk  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-layercake-phase-interface"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "long bilinear trace input would need a completed family and uniform aggregation; thin m-shell layers are not supplied as a direct theorem instance",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman input is relevant only after the moving prime q denominator is completed layerwise",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "Type-II shape is present for many edges, but the m side is short and endpoint layer summation remains rate-bearing",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced estimates are a plausible interface for right-tail and q-long layers, still requiring the exact congruence model",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval theta=0.52 does not close the half-scale or short-shell phase interface",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def collect_rectangles(max_prime: int = 1009) -> list[dict[str, Any]]:
    """重新生成所有 boundary layer-cake rectangles。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {p: index for index, p in enumerate(primes)}
    rows = bulk.group_edges(max_prime, primes)
    rectangles: list[dict[str, Any]] = []

    for P, edges in sorted(rows.items()):
        strip_fibres, _bulk_profile = layercake.strip_sets_for_row(P, edges, primes)
        for name in layercake.STRIP_NAMES:
            rects, _bad = layercake.layercake_for_strip(name, strip_fibres[name], prime_index)
            for rect in rects:
                item = dict(rect)
                item["P"] = P
                rectangles.append(item)

    return rectangles


def phase_class(rect: dict[str, Any]) -> str:
    """按 q-prefix 与 m-shell 两侧长度分相位接口类型。"""
    q_count = rect["q_prefix_count"]
    m_count = rect["m_shell_prime_count"]
    if q_count == 1 and m_count == 1:
        return "point_layer"
    if q_count == 1:
        return "m_shell_line_layer"
    if m_count == 1:
        return "q_prefix_line_layer"
    return "genuine_qm_product_layer"


def q_bin(q_count: int) -> str:
    """q-prefix 长度分桶。"""
    if q_count == 1:
        return "q=1"
    if q_count <= 4:
        return "2<=q<=4"
    if q_count <= 8:
        return "5<=q<=8"
    if q_count <= 16:
        return "9<=q<=16"
    return "17<=q<=37"


def m_bin(m_count: int) -> str:
    """m-shell 素数个数分桶。"""
    if m_count == 1:
        return "m=1"
    if m_count == 2:
        return "m=2"
    if m_count <= 4:
        return "3<=m<=4"
    if m_count <= 8:
        return "5<=m<=8"
    return "9<=m<=12"


def counter_rows(counts: Counter[Any], edges: Counter[Any]) -> list[dict[str, Any]]:
    """把计数器转为稳定表格。"""
    rows = []
    for key in sorted(counts, key=str):
        rows.append({"bucket": str(key), "rectangle_count": counts[key], "edge_count": edges[key]})
    return rows


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 layer-cake rectangles 的相位接口形状。"""
    rectangles = collect_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    class_counts: Counter[str] = Counter()
    class_edges: Counter[str] = Counter()
    strip_class_counts: Counter[tuple[str, str]] = Counter()
    strip_class_edges: Counter[tuple[str, str]] = Counter()
    q_counts: list[int] = []
    m_counts: list[int] = []
    edge_counts: list[int] = []
    q_bucket_counts: Counter[str] = Counter()
    q_bucket_edges: Counter[str] = Counter()
    m_bucket_counts: Counter[str] = Counter()
    m_bucket_edges: Counter[str] = Counter()
    shape_bucket_counts: Counter[tuple[str, str]] = Counter()
    shape_bucket_edges: Counter[tuple[str, str]] = Counter()

    for rect in rectangles:
        cls = phase_class(rect)
        edge_count = rect["edge_count"]
        q_count = rect["q_prefix_count"]
        m_count = rect["m_shell_prime_count"]
        class_counts[cls] += 1
        class_edges[cls] += edge_count
        strip_class_counts[(rect["strip"], cls)] += 1
        strip_class_edges[(rect["strip"], cls)] += edge_count
        q_counts.append(q_count)
        m_counts.append(m_count)
        edge_counts.append(edge_count)
        qb = q_bin(q_count)
        mb = m_bin(m_count)
        q_bucket_counts[qb] += 1
        q_bucket_edges[qb] += edge_count
        m_bucket_counts[mb] += 1
        m_bucket_edges[mb] += edge_count
        shape_bucket_counts[(qb, mb)] += 1
        shape_bucket_edges[(qb, mb)] += edge_count

    threshold_rows = []
    for threshold in [2, 3, 4, 5, 8, 10, 16]:
        selected = [
            rect
            for rect in rectangles
            if rect["q_prefix_count"] >= threshold
            and rect["m_shell_prime_count"] >= threshold
        ]
        threshold_rows.append(
            {
                "threshold": f"both>={threshold}",
                "rectangle_count": len(selected),
                "edge_count": sum(rect["edge_count"] for rect in selected),
            }
        )

    total_edges = sum(edge_counts)
    sqrt_layer_sum = sum(math.sqrt(edge_count) for edge_count in edge_counts)
    sqrt_total_edges = math.sqrt(total_edges)
    largest_rectangles = sorted(rectangles, key=lambda item: item["edge_count"], reverse=True)[:10]

    return {
        "max_prime": max_prime,
        "layercake_rectangle_count_total": len(rectangles),
        "previous_layercake_rectangle_count_total": previous_audit["layercake_rectangle_count_total"],
        "edge_count_total": total_edges,
        "previous_layercake_edge_count_total": previous_audit["layercake_edge_count_total"],
        "phase_class_rows": counter_rows(class_counts, class_edges),
        "strip_phase_class_rows": [
            {
                "strip": strip,
                "phase_class": cls,
                "rectangle_count": strip_class_counts[(strip, cls)],
                "edge_count": strip_class_edges[(strip, cls)],
            }
            for strip, cls in sorted(strip_class_counts)
        ],
        "q_prefix_count_min": min(q_counts),
        "q_prefix_count_median": statistics.median(q_counts),
        "q_prefix_count_max": max(q_counts),
        "q_prefix_count_average": sum(q_counts) / len(q_counts),
        "m_shell_prime_count_min": min(m_counts),
        "m_shell_prime_count_median": statistics.median(m_counts),
        "m_shell_prime_count_max": max(m_counts),
        "m_shell_prime_count_average": sum(m_counts) / len(m_counts),
        "rectangle_edge_count_min": min(edge_counts),
        "rectangle_edge_count_median": statistics.median(edge_counts),
        "rectangle_edge_count_max": max(edge_counts),
        "rectangle_edge_count_average": sum(edge_counts) / len(edge_counts),
        "q_bucket_rows": counter_rows(q_bucket_counts, q_bucket_edges),
        "m_bucket_rows": counter_rows(m_bucket_counts, m_bucket_edges),
        "shape_bucket_rows": [
            {
                "q_bucket": qb,
                "m_bucket": mb,
                "rectangle_count": shape_bucket_counts[(qb, mb)],
                "edge_count": shape_bucket_edges[(qb, mb)],
            }
            for qb, mb in sorted(shape_bucket_counts)
        ],
        "threshold_rows": threshold_rows,
        "sum_sqrt_rectangle_edges": sqrt_layer_sum,
        "sqrt_total_edges": sqrt_total_edges,
        "naive_layer_sqrt_loss_factor": sqrt_layer_sum / sqrt_total_edges,
        "all_m_shells_le_12": max(m_counts) <= 12,
        "no_large_balanced_typeii_layer_ge_16": not any(
            rect["q_prefix_count"] >= 16 and rect["m_shell_prime_count"] >= 16
            for rect in rectangles
        ),
        "genuine_product_rectangle_count": class_counts["genuine_qm_product_layer"],
        "genuine_product_edge_count": class_edges["genuine_qm_product_layer"],
        "thin_or_line_rectangle_count": len(rectangles) - class_counts["genuine_qm_product_layer"],
        "thin_or_line_edge_count": total_edges - class_edges["genuine_qm_product_layer"],
        "largest_rectangles": largest_rectangles,
        "phase_interface_shape_verified": (
            len(rectangles) == previous_audit["layercake_rectangle_count_total"]
            and total_edges == previous_audit["layercake_edge_count_total"]
        ),
        "direct_long_typeii_layer_closure_available": False,
        "uniform_short_shell_completion_required": True,
        "boundary_phase_saving_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_phase_interface_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "boundary_layercake_rectangles_split_by_phase_interface_short_shell_completion_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "layer-cake rectangles closed the support identity; the next non-cyclic question is whether their q and m sides match current external Type-II/trace interfaces",
        "current_object": {
            "input": "6190 boundary layer-cake product rectangles",
            "phase_interface": "split into point, q-prefix line, m-shell line, and genuine q-m product layers",
            "remaining": "short prime-m shell completion, moving q-denominator trace family, and uniform summation over layers",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "BoundaryLayerCakeShapeImported",
                True,
                True,
                "The previous exact 6190-rectangle layer-cake support identity is preserved.",
                "none for support shape",
            ),
            gate(
                "PhaseInterfaceClassLedger",
                True,
                True,
                "Every layer is classified by its q-prefix and m-shell side lengths.",
                "none for finite classification",
            ),
            gate(
                "ThinPrimeShellObstructionLocated",
                True,
                True,
                "The audited m-shell side has median 2 and maximum 12, so long-m Type-II input is not directly available layerwise.",
                "prove short-shell completion or aggregate layers before applying external estimates",
            ),
            gate(
                "UniformShortShellPhaseSaving",
                False,
                False,
                "Prove cancellation for q-long but m-short prime shells with moving prime q denominator.",
                "new analytic estimate or completed trace family required",
            ),
            gate(
                "NoLossLayerSummation",
                False,
                False,
                "Sum the 6190 layer estimates without a comparable Cauchy/endpoint loss.",
                "uniform layer aggregation remains required",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "genuine product layers are present, but the short m side and cross-layer aggregation are not automatic theorem hypotheses",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "useful only after layerwise moving q denominators are completed as Kloosterman variables",
            "Pascadi_composite_Type_II": "does not by itself absorb q-prefix line layers or short m-shell endpoint layers",
            "Wright_unbalanced_Kloosterman": "most relevant to q-long/m-short layers, still requiring the exact reciprocal phase model",
            "Li_short_interval_x_052": "does not imply the needed half-scale or layer endpoint positivity",
        },
        "latest_narrowest_mouth": [
            "UniformShortPrimeShellCompletionAcrossLayerCakeRectangles",
            "AND MovingPrimeQDenominatorCompletedTraceFamily",
            "AND NoLossLayerAggregationFor6190ShortShellPackets",
            "AND EndpointSummationByPartsForQPrefixLineLayers",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "phase_interface_shape_verified": finite_audit["phase_interface_shape_verified"],
        "direct_long_typeii_layer_closure_available": False,
        "boundary_phase_saving_closed": False,
        "completed_trace_or_kloosterman_variable_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    """生成简单 Markdown 表格。"""
    lines = [
        "| " + " | ".join(fields) + " |",
        "| " + " | ".join(["---"] * len(fields)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    return lines


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary layer-cake phase-interface 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"phase_interface={current['phase_interface']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. 相位接口有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"layercake_rectangle_count_total={audit['layercake_rectangle_count_total']}",
        f"previous_layercake_rectangle_count_total={audit['previous_layercake_rectangle_count_total']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"previous_layercake_edge_count_total={audit['previous_layercake_edge_count_total']}",
        f"q_prefix_count_min={audit['q_prefix_count_min']}",
        f"q_prefix_count_median={audit['q_prefix_count_median']}",
        f"q_prefix_count_max={audit['q_prefix_count_max']}",
        f"q_prefix_count_average={audit['q_prefix_count_average']:.12f}",
        f"m_shell_prime_count_min={audit['m_shell_prime_count_min']}",
        f"m_shell_prime_count_median={audit['m_shell_prime_count_median']}",
        f"m_shell_prime_count_max={audit['m_shell_prime_count_max']}",
        f"m_shell_prime_count_average={audit['m_shell_prime_count_average']:.12f}",
        f"rectangle_edge_count_min={audit['rectangle_edge_count_min']}",
        f"rectangle_edge_count_median={audit['rectangle_edge_count_median']}",
        f"rectangle_edge_count_max={audit['rectangle_edge_count_max']}",
        f"rectangle_edge_count_average={audit['rectangle_edge_count_average']:.12f}",
        f"sum_sqrt_rectangle_edges={audit['sum_sqrt_rectangle_edges']:.12f}",
        f"sqrt_total_edges={audit['sqrt_total_edges']:.12f}",
        f"naive_layer_sqrt_loss_factor={audit['naive_layer_sqrt_loss_factor']:.12f}",
        f"all_m_shells_le_12={str(audit['all_m_shells_le_12']).lower()}",
        f"no_large_balanced_typeii_layer_ge_16={str(audit['no_large_balanced_typeii_layer_ge_16']).lower()}",
        f"phase_interface_shape_verified={str(audit['phase_interface_shape_verified']).lower()}",
        f"direct_long_typeii_layer_closure_available={str(audit['direct_long_typeii_layer_closure_available']).lower()}",
        f"uniform_short_shell_completion_required={str(audit['uniform_short_shell_completion_required']).lower()}",
        f"boundary_phase_saving_closed={str(audit['boundary_phase_saving_closed']).lower()}",
        "```",
        "",
        "相位接口分类：",
        "",
        *markdown_table(audit["phase_class_rows"], ["bucket", "rectangle_count", "edge_count"]),
        "",
        "strip x class 分类：",
        "",
        *markdown_table(
            audit["strip_phase_class_rows"],
            ["strip", "phase_class", "rectangle_count", "edge_count"],
        ),
        "",
        "q-prefix 分桶：",
        "",
        *markdown_table(audit["q_bucket_rows"], ["bucket", "rectangle_count", "edge_count"]),
        "",
        "m-shell 分桶：",
        "",
        *markdown_table(audit["m_bucket_rows"], ["bucket", "rectangle_count", "edge_count"]),
        "",
        "双侧阈值：",
        "",
        *markdown_table(audit["threshold_rows"], ["threshold", "rectangle_count", "edge_count"]),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(
            payload["closed_gates"],
            ["gate", "closed", "proved", "meaning", "remaining"],
        ),
        "",
        "## 4. 外部 theorem 影响",
        "",
        *markdown_table(payload["external_sources_consulted"], ["key", "url", "role"]),
        "",
        "```text",
        *[
            f"{key}={value}"
            for key, value in payload["external_theorem_implication"].items()
        ],
        "```",
        "",
        "结论：边界层包已经是 product rectangles，但逐层相位接口不是长双变量 Type-II 的直接输入。",
        "`genuine_qm_product_layer` 承载多数边数；然而 `m_shell_prime_count` 的中位数为 `2`，最大为 `12`。",
        "因此最新缺口从“曲边支撑”推进到短 prime-shell completion、移动 q 分母 completed trace family、以及 6190 层的无损求和。",
        "",
        "## 5. 最新最窄口",
        "",
        "```text",
        *payload["latest_narrowest_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"phase_interface_shape_verified={str(payload['phase_interface_shape_verified']).lower()}",
        f"direct_long_typeii_layer_closure_available={str(payload['direct_long_typeii_layer_closure_available']).lower()}",
        f"boundary_phase_saving_closed={str(payload['boundary_phase_saving_closed']).lower()}",
        f"completed_trace_or_kloosterman_variable_closed={str(payload['completed_trace_or_kloosterman_variable_closed']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    payload = build_payload()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload))
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"phase_interface_shape_verified={payload['phase_interface_shape_verified']}")
    print(
        "direct_long_typeii_layer_closure_available="
        f"{payload['direct_long_typeii_layer_closure_available']}"
    )
    print(f"boundary_phase_saving_closed={payload['boundary_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
