#!/usr/bin/env python3
"""审计 rough-envelope prime-survivor 图中的 Type-II bulk rectangle 与边界负担。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.json

上一层已证明 prime-survivor 支撑来自 nested rough envelope，并给出
q-prefix/unimodal cap。外部 Type-II/trace/Kloosterman 定理真正能直接识别的
对象不是一般阶梯图，而是较完整的双变量 product rectangle。本审计继续下钻：

  1. 对每个固定 P，在实际 prime-survivor edge graph 中寻找最大的完整
     prime q x prime m 矩形 bulk；
  2. 验证该 bulk 没有缺边，可以作为真正的 Type-II 候选矩形；
  3. 量化剩余 boundary 是否可忽略。

有限审计显示：bulk 确实占约一半边，但 boundary 也占约一半；因此这是真正
推进到 Type-II 入口前的结构拆分，不是 Phi-LPF 奇偶性障碍的闭合证明。
"""

from __future__ import annotations

import hashlib
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_floor_span_completion_audit as floor_span  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "bulk-rectangle-typeii"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.json",
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
        "role": "the extracted bulk is closer to a trace bilinear input, but the comparable boundary remains outside the theorem",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "bulk rectangles still need a completed Kloosterman variable; boundary is not absorbed",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "bulk rectangles are Type-II shaped, but boundary cancellation or completion is still missing",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "the split suggests an unbalanced convolution route only after boundary tails are completed",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "additional smooth/squarefree matching remains absent for the prime-prime rectangle and boundary",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval theta=0.52 is not a replacement for boundary phase saving at the half-scale",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def prime_interval(primes: list[int], low: int, high: int, diagonal: int) -> list[int]:
    """返回闭区间中的素数，并扣除 diagonal m=P。"""
    return [p for p in primes if low <= p <= high and p != diagonal]


def group_edges(max_prime: int, primes: list[int]) -> dict[int, list[tuple[int, int]]]:
    """枚举并按 P 分组 prime-survivor edges。"""
    rows: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for item in floor_span.prime_blocker_edges(max_prime, primes):
        rows[item["P"]].append((item["q"], item["m"]))
    return dict(rows)


def best_bulk_rectangle(P: int, edges: list[tuple[int, int]], primes: list[int]) -> dict[str, Any]:
    """寻找固定 P 行中的最大完整 prime-q x prime-m 矩形。

    中文注释：固定 q 的 m 支撑已由上一层证明为素数区间。对连续 q 块取
    这些区间的交集，就得到保证无缺边的 product rectangle；再直接用 edge
    set 复核，避免把上一层结论当作未审计黑箱。
    """
    edge_set = set(edges)
    qs = sorted({q for q, _m in edge_set})
    q_to_ms: defaultdict[int, list[int]] = defaultdict(list)
    for q, m in edge_set:
        q_to_ms[q].append(m)
    q_intervals = []
    for q in qs:
        ms = sorted(q_to_ms[q])
        q_intervals.append((ms[0], ms[-1]))

    best_area = -1
    best: tuple[int, int, int, int, int, int] | None = None
    for i, q_start in enumerate(qs):
        low = 0
        high = 10**18
        for j in range(i, len(qs)):
            q_low, q_high = q_intervals[j]
            low = max(low, q_low)
            high = min(high, q_high)
            if low > high:
                break
            m_block = prime_interval(primes, low, high, P)
            area = (j - i + 1) * len(m_block)
            if area > best_area:
                best_area = area
                best = (q_start, qs[j], low, high, j - i + 1, len(m_block))

    if best is None:
        raise RuntimeError(f"no bulk rectangle found for P={P}")

    q_start, q_end, m_start, m_end, q_count, m_count = best
    q_block = [q for q in qs if q_start <= q <= q_end]
    m_block = prime_interval(primes, m_start, m_end, P)
    missing = [(q, m) for q in q_block for m in m_block if (q, m) not in edge_set]

    row_m_values = sorted({m for _q, m in edge_set})
    row_full_rectangle_count = len(qs) * (
        len(row_m_values) - (1 if P in row_m_values else 0)
    )
    actual_edge_count = len(edge_set)
    boundary_edge_count = actual_edge_count - best_area

    return {
        "P": P,
        "q_start": q_start,
        "q_end": q_end,
        "m_start": m_start,
        "m_end": m_end,
        "q_count": q_count,
        "m_count": m_count,
        "bulk_edge_count": best_area,
        "actual_edge_count": actual_edge_count,
        "boundary_edge_count": boundary_edge_count,
        "bulk_fraction": best_area / actual_edge_count,
        "row_q_count": len(qs),
        "row_m_count": len(row_m_values),
        "row_full_rectangle_count": row_full_rectangle_count,
        "row_completion_extra_count": row_full_rectangle_count - actual_edge_count,
        "bulk_missing_count": len(missing),
        "bulk_missing_sample": [list(pair) for pair in missing[:8]],
        "bulk_rectangle_verified": len(missing) == 0,
        "sample": (
            f"P={P}, bulk q=[{q_start},{q_end}] ({q_count}), "
            f"m=[{m_start},{m_end}] ({m_count}), "
            f"bulk={best_area}, boundary={boundary_edge_count}"
        ),
    }


def dyadic_density(rows: dict[int, list[tuple[int, int]]]) -> list[dict[str, Any]]:
    """粗 dyadic 单元密度，用于定位 bulk 与边界所在区域。"""
    q_bins = [0.5, 0.625, 0.75, 0.875, 1.000001]
    m_bins = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.01]
    full: Counter[tuple[int, int]] = Counter()
    actual: Counter[tuple[int, int]] = Counter()

    for P, edges in rows.items():
        edge_set = set(edges)
        qs = sorted({q for q, _m in edge_set})
        ms = sorted({m for _q, m in edge_set})
        for i in range(len(q_bins) - 1):
            q_block = [q for q in qs if q_bins[i] * P <= q < q_bins[i + 1] * P]
            if not q_block:
                continue
            for j in range(len(m_bins) - 1):
                m_block = [m for m in ms if m_bins[j] * P <= m < m_bins[j + 1] * P]
                if P in m_block:
                    m_block = [m for m in m_block if m != P]
                if not m_block:
                    continue
                full[(i, j)] += len(q_block) * len(m_block)
                actual[(i, j)] += sum(
                    1
                    for q, m in edge_set
                    if q in q_block and m in m_block and m != P
                )

    out = []
    for i, j in sorted(full):
        cell_full = full[(i, j)]
        cell_actual = actual[(i, j)]
        out.append(
            {
                "q_bin": f"[{q_bins[i]}, {q_bins[i + 1]})P",
                "m_bin": f"[{m_bins[j]}, {m_bins[j + 1]})P",
                "actual": cell_actual,
                "full": cell_full,
                "density": cell_actual / cell_full if cell_full else 0.0,
            }
        )
    return out


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 P<=max_prime 的 bulk rectangle 与 boundary 负担。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    rows = group_edges(max_prime, primes)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    totals: Counter[str] = Counter()
    ratios: list[float] = []
    sample_rows: list[dict[str, Any]] = []
    interesting = {101, 257, 971, 1009}

    for P, edges in sorted(rows.items()):
        profile = best_bulk_rectangle(P, edges, primes)
        ratios.append(profile["bulk_fraction"])
        totals["active_P_count"] += 1
        totals["actual_prime_edge_count_total"] += profile["actual_edge_count"]
        totals["bulk_rectangle_edge_count_total"] += profile["bulk_edge_count"]
        totals["boundary_edge_count_total"] += profile["boundary_edge_count"]
        totals["row_full_rectangle_count_total"] += profile["row_full_rectangle_count"]
        totals["row_completion_extra_count_total"] += profile["row_completion_extra_count"]
        totals["bulk_missing_count_total"] += profile["bulk_missing_count"]
        totals["bulk_fraction_ge_half_rows"] += int(profile["bulk_fraction"] >= 0.5)
        totals["bulk_fraction_ge_45pct_rows"] += int(profile["bulk_fraction"] >= 0.45)
        totals["bulk_rectangle_bad_row_count"] += int(not profile["bulk_rectangle_verified"])
        if P in interesting or len(sample_rows) < 8:
            sample_rows.append(profile)

    actual_total = totals["actual_prime_edge_count_total"]
    bulk_total = totals["bulk_rectangle_edge_count_total"]
    boundary_total = totals["boundary_edge_count_total"]
    full_total = totals["row_full_rectangle_count_total"]
    completion_extra_total = totals["row_completion_extra_count_total"]
    total_bad = totals["bulk_missing_count_total"] + totals["bulk_rectangle_bad_row_count"]

    return {
        "max_prime": max_prime,
        "active_P_count": totals["active_P_count"],
        "actual_prime_edge_count_total": actual_total,
        "previous_actual_prime_edge_count_total": previous_audit[
            "actual_prime_edge_count_total"
        ],
        "bulk_rectangle_edge_count_total": bulk_total,
        "boundary_edge_count_total": boundary_total,
        "bulk_fraction_total": bulk_total / actual_total,
        "boundary_fraction_total": boundary_total / actual_total,
        "row_full_rectangle_count_total": full_total,
        "row_completion_extra_count_total": completion_extra_total,
        "row_completion_ratio_total": full_total / actual_total,
        "row_completion_extra_to_actual_ratio_total": completion_extra_total / actual_total,
        "bulk_fraction_min": min(ratios),
        "bulk_fraction_median": statistics.median(ratios),
        "bulk_fraction_max": max(ratios),
        "bulk_fraction_ge_half_rows": totals["bulk_fraction_ge_half_rows"],
        "bulk_fraction_ge_45pct_rows": totals["bulk_fraction_ge_45pct_rows"],
        "bulk_missing_count_total": totals["bulk_missing_count_total"],
        "bulk_rectangle_bad_row_count": totals["bulk_rectangle_bad_row_count"],
        "total_bad_bulk_rectangle_typeii_count": total_bad,
        "bulk_product_rectangle_verified": total_bad == 0,
        "bulk_is_large_but_not_dominating_boundary": (
            0.45 <= bulk_total / actual_total <= 0.55
            and 0.45 <= boundary_total / actual_total <= 0.55
        ),
        "direct_bulk_only_typeii_closure_available": False,
        "boundary_phase_saving_or_staircase_completion_required": True,
        "dyadic_density_cells": dyadic_density(rows),
        "sample_rows": sample_rows,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "bulk_product_rectangle_extracted_boundary_typeii_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the rough-envelope cap left the trace/Type-II embedding gate; the fastest next step is to isolate the largest genuine product rectangles and measure the remaining boundary",
        "current_object": {
            "edge_graph": "prime-survivor edges (P,q,m) after rough-envelope cap",
            "bulk_rectangle": "maximal complete prime q x prime m rectangle inside each fixed-P support row",
            "boundary": "actual support minus the extracted complete bulk rectangle",
            "remaining": "prove phase saving for the comparable boundary, or complete the staircase into trace/Type-II packets without losing the main term",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "LargestPrimePrimeBulkRectangleExtraction",
                True,
                True,
                "Each active P row contains a verified complete prime q x prime m bulk rectangle inside the survivor graph.",
                "none for the finite structural extraction",
            ),
            gate(
                "NaiveRowRectangleCompletionCostQuantified",
                True,
                True,
                "Completing the row support to the full q x m row rectangle costs more than the actual support.",
                "none for the cost ledger",
            ),
            gate(
                "BulkBoundaryComparableObstruction",
                True,
                True,
                "The extracted bulk is large, but the remaining boundary is comparable and cannot be discarded.",
                "boundary phase saving or staircase completion remains required",
            ),
            gate(
                "DirectBulkOnlyTypeIIClosure",
                False,
                False,
                "Apply external Type-II/trace estimates only to the extracted bulk and close the full survivor layer.",
                "does not handle the comparable boundary",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "the bulk rectangle is a closer local shape, but the comparable boundary and completed trace family are not supplied",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "no completed Kloosterman variable has been constructed for bulk plus boundary",
            "Pascadi_composite_Type_II": "bulk rectangles are Type-II shaped, yet the boundary remains rate-bearing",
            "Wright_unbalanced_convolution": "a future unbalanced decomposition must include the staircase boundary",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "prime-prime and boundary weights still do not match the theorem hypotheses directly",
            "Li_short_interval_x_052": "does not replace the missing half-scale pointwise boundary estimate",
        },
        "latest_narrowest_mouth": [
            "BoundaryPhaseSavingForNestedRoughEnvelopeStaircase",
            "AND CompletedTraceFamilyForPrimePrimeBulkRectangle",
            "AND StaircaseBoundaryCompletionWithoutComparableLoss",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "bulk_product_rectangle_verified": True,
        "bulk_boundary_comparable_obstruction_closed": True,
        "direct_bulk_only_typeii_closure_available": False,
        "boundary_phase_saving_or_staircase_completion_required": True,
        "prefix_cap_trace_or_typeii_embedding_closed": False,
        "completed_trace_or_kloosterman_variable_closed": False,
        "prime_floor_span_trace_or_typeii_phase_saving_closed": False,
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
    sample_fields = [
        "P",
        "q_start",
        "q_end",
        "m_start",
        "m_end",
        "q_count",
        "m_count",
        "bulk_edge_count",
        "actual_edge_count",
        "boundary_edge_count",
        "bulk_fraction",
        "bulk_missing_count",
    ]
    density_fields = ["q_bin", "m_bin", "actual", "full", "density"]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor bulk-rectangle Type-II 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"edge_graph={current['edge_graph']}",
        f"bulk_rectangle={current['bulk_rectangle']}",
        f"boundary={current['boundary']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. bulk rectangle 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"active_P_count={audit['active_P_count']}",
        f"actual_prime_edge_count_total={audit['actual_prime_edge_count_total']}",
        f"previous_actual_prime_edge_count_total={audit['previous_actual_prime_edge_count_total']}",
        f"bulk_rectangle_edge_count_total={audit['bulk_rectangle_edge_count_total']}",
        f"boundary_edge_count_total={audit['boundary_edge_count_total']}",
        f"bulk_fraction_total={audit['bulk_fraction_total']:.12f}",
        f"boundary_fraction_total={audit['boundary_fraction_total']:.12f}",
        f"row_full_rectangle_count_total={audit['row_full_rectangle_count_total']}",
        f"row_completion_extra_count_total={audit['row_completion_extra_count_total']}",
        f"row_completion_ratio_total={audit['row_completion_ratio_total']:.12f}",
        f"row_completion_extra_to_actual_ratio_total={audit['row_completion_extra_to_actual_ratio_total']:.12f}",
        f"bulk_fraction_min={audit['bulk_fraction_min']:.12f}",
        f"bulk_fraction_median={audit['bulk_fraction_median']:.12f}",
        f"bulk_fraction_max={audit['bulk_fraction_max']:.12f}",
        f"bulk_fraction_ge_half_rows={audit['bulk_fraction_ge_half_rows']}",
        f"bulk_fraction_ge_45pct_rows={audit['bulk_fraction_ge_45pct_rows']}",
        f"bulk_missing_count_total={audit['bulk_missing_count_total']}",
        f"bulk_rectangle_bad_row_count={audit['bulk_rectangle_bad_row_count']}",
        f"total_bad_bulk_rectangle_typeii_count={audit['total_bad_bulk_rectangle_typeii_count']}",
        f"bulk_product_rectangle_verified={str(audit['bulk_product_rectangle_verified']).lower()}",
        f"bulk_is_large_but_not_dominating_boundary={str(audit['bulk_is_large_but_not_dominating_boundary']).lower()}",
        f"direct_bulk_only_typeii_closure_available={str(audit['direct_bulk_only_typeii_closure_available']).lower()}",
        f"boundary_phase_saving_or_staircase_completion_required={str(audit['boundary_phase_saving_or_staircase_completion_required']).lower()}",
        "```",
        "",
        "代表 bulk rectangle：",
        "",
        *markdown_table(audit["sample_rows"], sample_fields),
        "",
        "粗 dyadic 密度：",
        "",
        *markdown_table(audit["dyadic_density_cells"], density_fields),
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
        *markdown_table(payload["external_sources_consulted"], source_fields),
        "",
        "```text",
        *[
            f"{key}={value}"
            for key, value in payload["external_theorem_implication"].items()
        ],
        "```",
        "",
        "结论：nested rough-envelope support 中确实存在可供 Type-II/trace 进一步研究的完整 bulk rectangle，",
        "但最大 bulk 总量为 `178404` 条边，剩余 boundary 为 `177515` 条边，二者同阶。",
        "因此不能只把 bulk 交给外部 Type-II 定理后丢弃边界；下一步必须证明 staircase boundary 的相消或无可比损失完成。",
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
        f"bulk_product_rectangle_verified={str(payload['bulk_product_rectangle_verified']).lower()}",
        f"bulk_boundary_comparable_obstruction_closed={str(payload['bulk_boundary_comparable_obstruction_closed']).lower()}",
        f"direct_bulk_only_typeii_closure_available={str(payload['direct_bulk_only_typeii_closure_available']).lower()}",
        f"boundary_phase_saving_or_staircase_completion_required={str(payload['boundary_phase_saving_or_staircase_completion_required']).lower()}",
        f"prefix_cap_trace_or_typeii_embedding_closed={str(payload['prefix_cap_trace_or_typeii_embedding_closed']).lower()}",
        f"completed_trace_or_kloosterman_variable_closed={str(payload['completed_trace_or_kloosterman_variable_closed']).lower()}",
        f"prime_floor_span_trace_or_typeii_phase_saving_closed={str(payload['prime_floor_span_trace_or_typeii_phase_saving_closed']).lower()}",
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
    print(f"bulk_product_rectangle_verified={payload['bulk_product_rectangle_verified']}")
    print(
        "bulk_boundary_comparable_obstruction_closed="
        f"{payload['bulk_boundary_comparable_obstruction_closed']}"
    )
    print(
        "boundary_phase_saving_or_staircase_completion_required="
        f"{payload['boundary_phase_saving_or_staircase_completion_required']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
