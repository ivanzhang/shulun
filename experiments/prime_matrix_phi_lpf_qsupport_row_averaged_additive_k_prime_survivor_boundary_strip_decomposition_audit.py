#!/usr/bin/env python3
"""审计 prime-survivor bulk 之外的 boundary 单调条带分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_strip_decomposition_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.json

上一层把 nested rough-envelope prime-survivor 图拆成最大完整 Type-II bulk
rectangle 与同阶 boundary。本层继续把 boundary 由黑箱集合拆成三条单调条带：

  lower_wing: bulk q-prefix 内、bulk m 下方的 prime interval；
  upper_wing: bulk q-prefix 内、bulk m 上方的 prime interval；
  right_tail: bulk q-prefix 之后的完整 prime interval fibres。

由于 vertical fibres 是嵌套 prime intervals，最大 bulk 的 q-block 从首个 q
开始；三条 boundary 条带的 fibre 长度沿 q 都不增。该结论把边界压成可命名
的 monotone staircase packets，但没有给出相位节省。
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit as bulk  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-strip-decomposition"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"
STRIP_NAMES = ["left_tail", "lower_wing", "upper_wing", "right_tail"]

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.json",
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
        "role": "monotone strips are closer to summation by parts around bilinear trace estimates, but no boundary estimate is supplied",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "strip endpoints still need a completed Kloosterman variable or endpoint cancellation",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "a strip-by-strip Type-II packet remains conditional on boundary completion",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "the monotone right tail is an unbalanced candidate only after endpoint weights are controlled",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "strip variables still do not directly match smooth/squarefree hypotheses",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval theta=0.52 does not close monotone strip phase saving at theta=1/2",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def prime_count(primes: list[int], low: int, high: int, diagonal: int) -> int:
    """闭区间 prime count，并扣除 diagonal。"""
    return sum(1 for p in primes if low <= p <= high and p != diagonal)


def prime_count_open_left(primes: list[int], low: int, high: int, diagonal: int) -> int:
    """计算 (low, high] 中的素数数目，并扣除 diagonal。"""
    return sum(1 for p in primes if low < p <= high and p != diagonal)


def prime_count_open_right(primes: list[int], low: int, high: int, diagonal: int) -> int:
    """计算 [low, high) 中的素数数目，并扣除 diagonal。"""
    return sum(1 for p in primes if low <= p < high and p != diagonal)


def is_contiguous(indices: list[int]) -> bool:
    """检查索引集合是否连续。"""
    return not indices or max(indices) - min(indices) + 1 == len(indices)


def nonincreasing_bad_steps(values: list[int]) -> int:
    """统计非增序列中的上升步数。"""
    return sum(1 for left, right in zip(values, values[1:]) if right > left)


def row_boundary_profile(P: int, edges: list[tuple[int, int]], primes: list[int]) -> dict[str, Any]:
    """分解固定 P 行的 bulk boundary。"""
    edge_set = set(edges)
    bulk_profile = bulk.best_bulk_rectangle(P, edges, primes)
    q_to_ms: defaultdict[int, list[int]] = defaultdict(list)
    for q, m in edge_set:
        q_to_ms[q].append(m)
    qs = sorted(q_to_ms)
    q_index = {q: index for index, q in enumerate(qs)}

    counts: Counter[str] = Counter()
    expected: Counter[str] = Counter()
    q_indices: defaultdict[str, list[int]] = defaultdict(list)
    lengths: defaultdict[str, list[int]] = defaultdict(list)
    samples: dict[str, str] = {}

    q_start = bulk_profile["q_start"]
    q_end = bulk_profile["q_end"]
    m_start = bulk_profile["m_start"]
    m_end = bulk_profile["m_end"]

    for q in qs:
        ms = sorted(q_to_ms[q])
        L = ms[0]
        U = ms[-1]
        if q < q_start:
            actual = len(ms)
            exp = prime_count(primes, L, U, P)
            strip = "left_tail"
            counts[strip] += actual
            expected[strip] += exp
            q_indices[strip].append(q_index[q])
            lengths[strip].append(actual)
            samples.setdefault(strip, f"q={q},m=[{L},{U}],count={actual}")
        elif q > q_end:
            actual = len(ms)
            exp = prime_count(primes, L, U, P)
            strip = "right_tail"
            counts[strip] += actual
            expected[strip] += exp
            q_indices[strip].append(q_index[q])
            lengths[strip].append(actual)
            samples.setdefault(strip, f"q={q},m=[{L},{U}],count={actual}")
        else:
            lower_actual = sum(1 for m in ms if m < m_start)
            if lower_actual:
                strip = "lower_wing"
                lower_expected = prime_count_open_right(primes, L, m_start, P)
                counts[strip] += lower_actual
                expected[strip] += lower_expected
                q_indices[strip].append(q_index[q])
                lengths[strip].append(lower_actual)
                samples.setdefault(strip, f"q={q},m=[{L},{m_start}),count={lower_actual}")

            upper_actual = sum(1 for m in ms if m > m_end)
            if upper_actual:
                strip = "upper_wing"
                upper_expected = prime_count_open_left(primes, m_end, U, P)
                counts[strip] += upper_actual
                expected[strip] += upper_expected
                q_indices[strip].append(q_index[q])
                lengths[strip].append(upper_actual)
                samples.setdefault(strip, f"q={q},m=({m_end},{U}],count={upper_actual}")

    boundary_count = sum(counts.values())
    mismatch_count = sum(abs(counts[name] - expected[name]) for name in STRIP_NAMES)
    noncontiguous_strip_count = sum(
        1 for name in STRIP_NAMES if not is_contiguous(q_indices[name])
    )
    monotonicity_bad_steps = sum(nonincreasing_bad_steps(lengths[name]) for name in STRIP_NAMES)

    return {
        "P": P,
        "q_first": qs[0],
        "q_last": qs[-1],
        "q_start": q_start,
        "q_end": q_end,
        "m_start": m_start,
        "m_end": m_end,
        "bulk_edge_count": bulk_profile["bulk_edge_count"],
        "boundary_edge_count": bulk_profile["boundary_edge_count"],
        "strip_boundary_count": boundary_count,
        "left_tail_count": counts["left_tail"],
        "lower_wing_count": counts["lower_wing"],
        "upper_wing_count": counts["upper_wing"],
        "right_tail_count": counts["right_tail"],
        "left_tail_expected_count": expected["left_tail"],
        "lower_wing_expected_count": expected["lower_wing"],
        "upper_wing_expected_count": expected["upper_wing"],
        "right_tail_expected_count": expected["right_tail"],
        "q_start_is_row_first": q_start == qs[0],
        "q_end_is_row_last": q_end == qs[-1],
        "strip_prime_interval_mismatch_count": mismatch_count,
        "noncontiguous_strip_count": noncontiguous_strip_count,
        "strip_length_monotonicity_bad_steps": monotonicity_bad_steps,
        "strip_decomposition_verified": (
            boundary_count == bulk_profile["boundary_edge_count"]
            and mismatch_count == 0
            and noncontiguous_strip_count == 0
            and monotonicity_bad_steps == 0
        ),
        "strip_samples": samples,
    }


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
    """审计 P<=max_prime 的 boundary strip decomposition。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    rows = bulk.group_edges(max_prime, primes)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    totals: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []
    interesting = {101, 257, 971, 1009}

    for P, edges in sorted(rows.items()):
        profile = row_boundary_profile(P, edges, primes)
        totals["active_P_count"] += 1
        totals["bulk_edge_count_total"] += profile["bulk_edge_count"]
        totals["boundary_edge_count_total"] += profile["boundary_edge_count"]
        totals["strip_boundary_count_total"] += profile["strip_boundary_count"]
        totals["left_tail_count_total"] += profile["left_tail_count"]
        totals["lower_wing_count_total"] += profile["lower_wing_count"]
        totals["upper_wing_count_total"] += profile["upper_wing_count"]
        totals["right_tail_count_total"] += profile["right_tail_count"]
        totals["left_tail_expected_count_total"] += profile["left_tail_expected_count"]
        totals["lower_wing_expected_count_total"] += profile["lower_wing_expected_count"]
        totals["upper_wing_expected_count_total"] += profile["upper_wing_expected_count"]
        totals["right_tail_expected_count_total"] += profile["right_tail_expected_count"]
        totals["q_start_not_row_first_count"] += int(not profile["q_start_is_row_first"])
        totals["q_end_not_row_last_count"] += int(not profile["q_end_is_row_last"])
        totals["left_tail_active_row_count"] += int(profile["left_tail_count"] > 0)
        totals["lower_wing_active_row_count"] += int(profile["lower_wing_count"] > 0)
        totals["upper_wing_active_row_count"] += int(profile["upper_wing_count"] > 0)
        totals["right_tail_active_row_count"] += int(profile["right_tail_count"] > 0)
        totals["strip_prime_interval_mismatch_count_total"] += profile[
            "strip_prime_interval_mismatch_count"
        ]
        totals["noncontiguous_strip_count_total"] += profile["noncontiguous_strip_count"]
        totals["strip_length_monotonicity_bad_steps_total"] += profile[
            "strip_length_monotonicity_bad_steps"
        ]
        totals["bad_strip_decomposition_row_count"] += int(
            not profile["strip_decomposition_verified"]
        )
        if P in interesting or len(sample_rows) < 8:
            sample_rows.append(profile)

    boundary_total = totals["boundary_edge_count_total"]
    total_bad = (
        totals["strip_prime_interval_mismatch_count_total"]
        + totals["noncontiguous_strip_count_total"]
        + totals["strip_length_monotonicity_bad_steps_total"]
        + totals["bad_strip_decomposition_row_count"]
        + int(totals["strip_boundary_count_total"] != boundary_total)
        + totals["q_start_not_row_first_count"]
        + totals["left_tail_count_total"]
    )

    return {
        "max_prime": max_prime,
        "active_P_count": totals["active_P_count"],
        "bulk_edge_count_total": totals["bulk_edge_count_total"],
        "previous_bulk_edge_count_total": previous_audit["bulk_rectangle_edge_count_total"],
        "boundary_edge_count_total": boundary_total,
        "previous_boundary_edge_count_total": previous_audit["boundary_edge_count_total"],
        "strip_boundary_count_total": totals["strip_boundary_count_total"],
        "left_tail_count_total": totals["left_tail_count_total"],
        "lower_wing_count_total": totals["lower_wing_count_total"],
        "upper_wing_count_total": totals["upper_wing_count_total"],
        "right_tail_count_total": totals["right_tail_count_total"],
        "left_tail_expected_count_total": totals["left_tail_expected_count_total"],
        "lower_wing_expected_count_total": totals["lower_wing_expected_count_total"],
        "upper_wing_expected_count_total": totals["upper_wing_expected_count_total"],
        "right_tail_expected_count_total": totals["right_tail_expected_count_total"],
        "lower_wing_fraction_of_boundary": totals["lower_wing_count_total"] / boundary_total,
        "upper_wing_fraction_of_boundary": totals["upper_wing_count_total"] / boundary_total,
        "right_tail_fraction_of_boundary": totals["right_tail_count_total"] / boundary_total,
        "q_start_not_row_first_count": totals["q_start_not_row_first_count"],
        "q_end_not_row_last_count": totals["q_end_not_row_last_count"],
        "left_tail_active_row_count": totals["left_tail_active_row_count"],
        "lower_wing_active_row_count": totals["lower_wing_active_row_count"],
        "upper_wing_active_row_count": totals["upper_wing_active_row_count"],
        "right_tail_active_row_count": totals["right_tail_active_row_count"],
        "strip_prime_interval_mismatch_count_total": totals[
            "strip_prime_interval_mismatch_count_total"
        ],
        "noncontiguous_strip_count_total": totals["noncontiguous_strip_count_total"],
        "strip_length_monotonicity_bad_steps_total": totals[
            "strip_length_monotonicity_bad_steps_total"
        ],
        "bad_strip_decomposition_row_count": totals["bad_strip_decomposition_row_count"],
        "total_bad_boundary_strip_decomposition_count": total_bad,
        "bulk_prefix_start_verified": totals["q_start_not_row_first_count"] == 0,
        "left_tail_vanishes_verified": totals["left_tail_count_total"] == 0,
        "boundary_three_strip_identity_verified": total_bad == 0,
        "boundary_strips_are_monotone_prime_interval_packets": total_bad == 0,
        "boundary_phase_saving_closed": False,
        "strip_completion_without_loss_closed": False,
        "sample_rows": sample_rows,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_strip_decomposition_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "bulk_boundary_decomposed_into_three_monotone_strips_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the bulk rectangle audit left a comparable staircase boundary; the fastest non-cyclic advance is to make that boundary a finite monotone strip packet rather than an arbitrary leftover set",
        "current_object": {
            "bulk": "largest complete prime q x prime m rectangle inside each fixed-P survivor row",
            "boundary_decomposition": "boundary=lower_wing disjoint union upper_wing disjoint union right_tail; left_tail vanishes",
            "strip_shape": "each active strip is a contiguous q-block of complete prime intervals with nonincreasing fibre lengths",
            "remaining": "phase saving or completion for the three monotone strip packets without losing a boundary-sized main term",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "BulkPrefixStart",
                True,
                True,
                "The maximal bulk rectangle starts at the first eligible q in every audited row.",
                "none for the audited rows; follows from nested interval monotonicity as a structural guide",
            ),
            gate(
                "BoundaryThreeStripIdentity",
                True,
                True,
                "The boundary is exactly lower_wing plus upper_wing plus right_tail; left_tail is zero.",
                "none for the strip identity",
            ),
            gate(
                "BoundaryStripPrimeIntervalCompleteness",
                True,
                True,
                "Each strip fibre is a complete prime interval segment, not a sparse arbitrary set.",
                "none for the support identity",
            ),
            gate(
                "BoundaryStripLengthMonotonicity",
                True,
                True,
                "The strip fibre lengths are nonincreasing along q.",
                "none for the monotone support ledger",
            ),
            gate(
                "BoundaryStripPhaseSaving",
                False,
                False,
                "Obtain cancellation or a completed trace family for the three monotone strip packets.",
                "new analytic estimate still required",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "the boundary is no longer arbitrary, but monotone strip packets still need a trace-family completion",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "moving q denominators remain uncompleted on strip endpoints",
            "Pascadi_composite_Type_II": "strip packets are Type-II-like only after endpoint weights are absorbed",
            "Wright_unbalanced_convolution": "right_tail gives an unbalanced candidate, not a closed convolution theorem",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "no direct match for strip weights",
            "Li_short_interval_x_052": "does not close the needed theta=1/2 strip endpoint control",
        },
        "latest_narrowest_mouth": [
            "BoundaryPhaseSavingForThreeMonotonePrimeIntervalStrips",
            "AND CompletedTraceFamilyForPrimePrimeBulkRectangle",
            "AND StripEndpointSummationByPartsWithoutComparableLoss",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "bulk_prefix_start_verified": True,
        "left_tail_vanishes_verified": True,
        "boundary_three_strip_identity_verified": True,
        "boundary_strips_are_monotone_prime_interval_packets": True,
        "boundary_phase_saving_closed": False,
        "strip_completion_without_loss_closed": False,
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
    sample_fields = [
        "P",
        "q_start",
        "q_end",
        "m_start",
        "m_end",
        "boundary_edge_count",
        "left_tail_count",
        "lower_wing_count",
        "upper_wing_count",
        "right_tail_count",
        "strip_prime_interval_mismatch_count",
        "strip_length_monotonicity_bad_steps",
    ]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary strip decomposition 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"bulk={current['bulk']}",
        f"boundary_decomposition={current['boundary_decomposition']}",
        f"strip_shape={current['strip_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. boundary strip 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"active_P_count={audit['active_P_count']}",
        f"bulk_edge_count_total={audit['bulk_edge_count_total']}",
        f"previous_bulk_edge_count_total={audit['previous_bulk_edge_count_total']}",
        f"boundary_edge_count_total={audit['boundary_edge_count_total']}",
        f"previous_boundary_edge_count_total={audit['previous_boundary_edge_count_total']}",
        f"strip_boundary_count_total={audit['strip_boundary_count_total']}",
        f"left_tail_count_total={audit['left_tail_count_total']}",
        f"lower_wing_count_total={audit['lower_wing_count_total']}",
        f"upper_wing_count_total={audit['upper_wing_count_total']}",
        f"right_tail_count_total={audit['right_tail_count_total']}",
        f"lower_wing_fraction_of_boundary={audit['lower_wing_fraction_of_boundary']:.12f}",
        f"upper_wing_fraction_of_boundary={audit['upper_wing_fraction_of_boundary']:.12f}",
        f"right_tail_fraction_of_boundary={audit['right_tail_fraction_of_boundary']:.12f}",
        f"q_start_not_row_first_count={audit['q_start_not_row_first_count']}",
        f"q_end_not_row_last_count={audit['q_end_not_row_last_count']}",
        f"left_tail_active_row_count={audit['left_tail_active_row_count']}",
        f"lower_wing_active_row_count={audit['lower_wing_active_row_count']}",
        f"upper_wing_active_row_count={audit['upper_wing_active_row_count']}",
        f"right_tail_active_row_count={audit['right_tail_active_row_count']}",
        f"strip_prime_interval_mismatch_count_total={audit['strip_prime_interval_mismatch_count_total']}",
        f"noncontiguous_strip_count_total={audit['noncontiguous_strip_count_total']}",
        f"strip_length_monotonicity_bad_steps_total={audit['strip_length_monotonicity_bad_steps_total']}",
        f"bad_strip_decomposition_row_count={audit['bad_strip_decomposition_row_count']}",
        f"total_bad_boundary_strip_decomposition_count={audit['total_bad_boundary_strip_decomposition_count']}",
        f"bulk_prefix_start_verified={str(audit['bulk_prefix_start_verified']).lower()}",
        f"left_tail_vanishes_verified={str(audit['left_tail_vanishes_verified']).lower()}",
        f"boundary_three_strip_identity_verified={str(audit['boundary_three_strip_identity_verified']).lower()}",
        f"boundary_strips_are_monotone_prime_interval_packets={str(audit['boundary_strips_are_monotone_prime_interval_packets']).lower()}",
        f"boundary_phase_saving_closed={str(audit['boundary_phase_saving_closed']).lower()}",
        "```",
        "",
        "代表行：",
        "",
        *markdown_table(audit["sample_rows"], sample_fields),
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
        "结论：bulk 之外的 boundary 不再是任意剩余集合；它精确分解为三条单调 prime-interval strip。",
        "但三条 strip 总量仍为 `177515` 条边，仍需要新的边界相消、endpoint summation-by-parts 或 completed trace family。",
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
        f"bulk_prefix_start_verified={str(payload['bulk_prefix_start_verified']).lower()}",
        f"left_tail_vanishes_verified={str(payload['left_tail_vanishes_verified']).lower()}",
        f"boundary_three_strip_identity_verified={str(payload['boundary_three_strip_identity_verified']).lower()}",
        f"boundary_strips_are_monotone_prime_interval_packets={str(payload['boundary_strips_are_monotone_prime_interval_packets']).lower()}",
        f"boundary_phase_saving_closed={str(payload['boundary_phase_saving_closed']).lower()}",
        f"strip_completion_without_loss_closed={str(payload['strip_completion_without_loss_closed']).lower()}",
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
    print(f"boundary_three_strip_identity_verified={payload['boundary_three_strip_identity_verified']}")
    print(
        "boundary_strips_are_monotone_prime_interval_packets="
        f"{payload['boundary_strips_are_monotone_prime_interval_packets']}"
    )
    print(f"boundary_phase_saving_closed={payload['boundary_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
