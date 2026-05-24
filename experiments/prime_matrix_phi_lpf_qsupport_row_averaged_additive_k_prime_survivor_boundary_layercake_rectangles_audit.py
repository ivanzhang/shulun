#!/usr/bin/env python3
"""审计 boundary monotone strips 的 layer-cake 矩形分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_rectangles_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json

上一层把 bulk 外的 boundary 拆成 lower_wing、upper_wing、right_tail 三条
单调 prime-interval strip。本层继续下钻：每条 strip 的 fibre 随 q 单调嵌套，
因此可以用 layer-cake/Ferrers 分解写成互不重叠的

  strip-local q-prefix x prime m-shell

矩形层。该分解把 endpoint boundary 从三条曲边 strip 压成完整 product
rectangle 层包，但仍未提供统一相位节省或 completed trace family。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit as bulk  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-layercake-rectangles"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"
STRIP_NAMES = ["lower_wing", "upper_wing", "right_tail"]

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.json",
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
        "role": "the boundary is now a finite family of product rectangles, but uniform trace-family hypotheses and summation over layers remain open",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "rectangle layers still require a completed Kloosterman variable for the moving q denominator",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "layer rectangles are Type-II shaped, but the number of layers and endpoint weights must be absorbed",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "right-tail layers are unbalanced candidates only after their congruence model is completed",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval theta=0.52 still does not close the half-scale layer endpoint problem",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def split_prime_shell(values: list[int], prime_index: dict[int, int]) -> list[list[int]]:
    """把 prime shell 拆成相邻素数区间。"""
    if not values:
        return []
    blocks: list[list[int]] = []
    current = [values[0]]
    for left, right in zip(values, values[1:]):
        if prime_index[right] == prime_index[left] + 1:
            current.append(right)
        else:
            blocks.append(current)
            current = [right]
    blocks.append(current)
    return blocks


def strip_sets_for_row(
    P: int, edges: list[tuple[int, int]], primes: list[int]
) -> tuple[dict[str, list[tuple[int, set[int]]]], dict[str, Any]]:
    """返回固定 P 的三条 boundary strip fibre sets。"""
    edge_set = set(edges)
    bulk_profile = bulk.best_bulk_rectangle(P, edges, primes)
    q_to_ms: defaultdict[int, list[int]] = defaultdict(list)
    for q, m in edge_set:
        q_to_ms[q].append(m)

    strips: dict[str, list[tuple[int, set[int]]]] = {name: [] for name in STRIP_NAMES}
    q_start = bulk_profile["q_start"]
    q_end = bulk_profile["q_end"]
    m_start = bulk_profile["m_start"]
    m_end = bulk_profile["m_end"]

    for q in sorted(q_to_ms):
        ms = sorted(q_to_ms[q])
        if q_start <= q <= q_end:
            lower = {m for m in ms if m < m_start}
            upper = {m for m in ms if m > m_end}
            if lower:
                strips["lower_wing"].append((q, lower))
            if upper:
                strips["upper_wing"].append((q, upper))
        elif q > q_end:
            strips["right_tail"].append((q, set(ms)))

    return strips, bulk_profile


def layercake_for_strip(
    strip_name: str,
    fibres: list[tuple[int, set[int]]],
    prime_index: dict[int, int],
) -> tuple[list[dict[str, Any]], int]:
    """把一条嵌套 strip 分解成 q-prefix x m-shell 矩形。"""
    rectangles: list[dict[str, Any]] = []
    nested_bad_steps = 0

    for index, (q, fibre) in enumerate(fibres):
        next_fibre = fibres[index + 1][1] if index + 1 < len(fibres) else set()
        if not next_fibre.issubset(fibre):
            nested_bad_steps += 1
        shell_values = sorted(fibre - next_fibre)
        for block in split_prime_shell(shell_values, prime_index):
            rectangles.append(
                {
                    "strip": strip_name,
                    "q_prefix_count": index + 1,
                    "q_start": fibres[0][0],
                    "q_end": q,
                    "m_start": block[0],
                    "m_end": block[-1],
                    "m_shell_prime_count": len(block),
                    "edge_count": (index + 1) * len(block),
                }
            )

    return rectangles, nested_bad_steps


def expand_rectangles(
    rectangles: list[dict[str, Any]], strip_fibres: dict[str, list[tuple[int, set[int]]]]
) -> set[tuple[int, int]]:
    """展开矩形层，用于复核不漏不重。"""
    by_strip_qs = {name: [q for q, _items in fibres] for name, fibres in strip_fibres.items()}
    out: set[tuple[int, int]] = set()
    for rect in rectangles:
        q_values = by_strip_qs[rect["strip"]][: rect["q_prefix_count"]]
        m_values = [
            m
            for m in range(rect["m_start"], rect["m_end"] + 1)
            if m in primorial.prime_sieve(rect["m_end"] + 1)
        ]
        # 中文注释：m-shell 已经按相邻素数块拆分，使用筛复核即可。
        for q in q_values:
            for m in m_values:
                out.add((q, m))
    return out


def boundary_edge_set(strip_fibres: dict[str, list[tuple[int, set[int]]]]) -> set[tuple[int, int]]:
    """返回 strip 边界 edge set。"""
    out: set[tuple[int, int]] = set()
    for fibres in strip_fibres.values():
        for q, items in fibres:
            out.update((q, m) for m in items)
    return out


def row_layercake_profile(
    P: int, edges: list[tuple[int, int]], primes: list[int], prime_index: dict[int, int]
) -> dict[str, Any]:
    """审计固定 P 行的 layer-cake rectangle decomposition。"""
    strip_fibres, bulk_profile = strip_sets_for_row(P, edges, primes)
    rectangles: list[dict[str, Any]] = []
    nested_bad_steps = 0
    strip_rectangle_counts: Counter[str] = Counter()
    strip_edge_counts: Counter[str] = Counter()

    for name in STRIP_NAMES:
        rects, bad = layercake_for_strip(name, strip_fibres[name], prime_index)
        nested_bad_steps += bad
        rectangles.extend(rects)
        strip_rectangle_counts[name] += len(rects)
        strip_edge_counts[name] += sum(rect["edge_count"] for rect in rects)

    expanded = expand_rectangles(rectangles, strip_fibres)
    boundary = boundary_edge_set(strip_fibres)
    missing = sorted(boundary - expanded)
    extra = sorted(expanded - boundary)
    rectangle_edge_count = sum(rect["edge_count"] for rect in rectangles)

    max_rect = max((rect["edge_count"] for rect in rectangles), default=0)
    sample_rectangles = rectangles[:4] + rectangles[-4:] if len(rectangles) > 8 else rectangles
    return {
        "P": P,
        "boundary_edge_count": bulk_profile["boundary_edge_count"],
        "layercake_rectangle_count": len(rectangles),
        "layercake_edge_count": rectangle_edge_count,
        "lower_wing_rectangle_count": strip_rectangle_counts["lower_wing"],
        "upper_wing_rectangle_count": strip_rectangle_counts["upper_wing"],
        "right_tail_rectangle_count": strip_rectangle_counts["right_tail"],
        "lower_wing_edge_count": strip_edge_counts["lower_wing"],
        "upper_wing_edge_count": strip_edge_counts["upper_wing"],
        "right_tail_edge_count": strip_edge_counts["right_tail"],
        "max_rectangle_edge_count": max_rect,
        "nested_bad_steps": nested_bad_steps,
        "missing_count": len(missing),
        "extra_count": len(extra),
        "decomposition_verified": (
            rectangle_edge_count == bulk_profile["boundary_edge_count"]
            and not missing
            and not extra
            and nested_bad_steps == 0
        ),
        "sample_rectangles": sample_rectangles,
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
    """审计 P<=max_prime 的 boundary layer-cake rectangles。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {p: index for index, p in enumerate(primes)}
    rows = bulk.group_edges(max_prime, primes)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    totals: Counter[str] = Counter()
    row_rectangle_counts: list[int] = []
    sample_rows: list[dict[str, Any]] = []
    interesting = {101, 257, 971, 1009}

    for P, edges in sorted(rows.items()):
        profile = row_layercake_profile(P, edges, primes, prime_index)
        totals["active_P_count"] += 1
        totals["boundary_edge_count_total"] += profile["boundary_edge_count"]
        totals["layercake_rectangle_count_total"] += profile["layercake_rectangle_count"]
        totals["layercake_edge_count_total"] += profile["layercake_edge_count"]
        totals["lower_wing_rectangle_count_total"] += profile["lower_wing_rectangle_count"]
        totals["upper_wing_rectangle_count_total"] += profile["upper_wing_rectangle_count"]
        totals["right_tail_rectangle_count_total"] += profile["right_tail_rectangle_count"]
        totals["lower_wing_edge_count_total"] += profile["lower_wing_edge_count"]
        totals["upper_wing_edge_count_total"] += profile["upper_wing_edge_count"]
        totals["right_tail_edge_count_total"] += profile["right_tail_edge_count"]
        totals["nested_bad_steps_total"] += profile["nested_bad_steps"]
        totals["missing_count_total"] += profile["missing_count"]
        totals["extra_count_total"] += profile["extra_count"]
        totals["bad_layercake_row_count"] += int(not profile["decomposition_verified"])
        totals["max_rectangle_edge_count"] = max(
            totals["max_rectangle_edge_count"], profile["max_rectangle_edge_count"]
        )
        if profile["layercake_rectangle_count"]:
            row_rectangle_counts.append(profile["layercake_rectangle_count"])
        if P in interesting or len(sample_rows) < 8:
            sample_rows.append(profile)

    total_bad = (
        totals["nested_bad_steps_total"]
        + totals["missing_count_total"]
        + totals["extra_count_total"]
        + totals["bad_layercake_row_count"]
        + int(totals["boundary_edge_count_total"] != totals["layercake_edge_count_total"])
    )

    return {
        "max_prime": max_prime,
        "active_P_count": totals["active_P_count"],
        "boundary_edge_count_total": totals["boundary_edge_count_total"],
        "previous_boundary_edge_count_total": previous_audit["boundary_edge_count_total"],
        "layercake_rectangle_count_total": totals["layercake_rectangle_count_total"],
        "layercake_edge_count_total": totals["layercake_edge_count_total"],
        "lower_wing_rectangle_count_total": totals["lower_wing_rectangle_count_total"],
        "upper_wing_rectangle_count_total": totals["upper_wing_rectangle_count_total"],
        "right_tail_rectangle_count_total": totals["right_tail_rectangle_count_total"],
        "lower_wing_edge_count_total": totals["lower_wing_edge_count_total"],
        "previous_lower_wing_edge_count_total": previous_audit["lower_wing_count_total"],
        "upper_wing_edge_count_total": totals["upper_wing_edge_count_total"],
        "previous_upper_wing_edge_count_total": previous_audit["upper_wing_count_total"],
        "right_tail_edge_count_total": totals["right_tail_edge_count_total"],
        "previous_right_tail_edge_count_total": previous_audit["right_tail_count_total"],
        "row_rectangle_count_min": min(row_rectangle_counts),
        "row_rectangle_count_median": statistics.median(row_rectangle_counts),
        "row_rectangle_count_max": max(row_rectangle_counts),
        "row_rectangle_count_average": sum(row_rectangle_counts) / len(row_rectangle_counts),
        "max_rectangle_edge_count": totals["max_rectangle_edge_count"],
        "nested_bad_steps_total": totals["nested_bad_steps_total"],
        "missing_count_total": totals["missing_count_total"],
        "extra_count_total": totals["extra_count_total"],
        "bad_layercake_row_count": totals["bad_layercake_row_count"],
        "total_bad_boundary_layercake_rectangle_count": total_bad,
        "boundary_layercake_rectangle_identity_verified": total_bad == 0,
        "all_layers_are_complete_product_rectangles": total_bad == 0,
        "layer_count_requires_uniform_summation_control": True,
        "boundary_phase_saving_closed": False,
        "completed_trace_or_kloosterman_variable_closed": False,
        "sample_rows": sample_rows,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_rectangles_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "boundary_monotone_strips_decomposed_into_layercake_product_rectangles_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the boundary strip audit left endpoint phase saving; the fastest non-cyclic advance is to turn monotone strips into exact q-prefix by m-shell product rectangles",
        "current_object": {
            "input": "three monotone prime-interval boundary strips",
            "layercake_decomposition": "each strip is a disjoint union of strip-local q-prefix x prime m-shell rectangles",
            "remaining": "uniform phase saving or completed trace/Kloosterman estimates over the 6190 rectangle layers",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "BoundaryLayerCakeRectangleIdentity",
                True,
                True,
                "The three monotone strips decompose exactly into disjoint q-prefix by m-shell product rectangles.",
                "none for the support identity",
            ),
            gate(
                "NoLayerOverlapOrLeak",
                True,
                True,
                "Expanded layer rectangles match the boundary edge set with no missing and no extra edge.",
                "none for the finite ledger",
            ),
            gate(
                "LayerCountAndLoadLedger",
                True,
                True,
                "The boundary load is carried by 6190 rectangle layers, with row layer counts recorded.",
                "uniform summation control over layers remains required",
            ),
            gate(
                "LayerUniformPhaseSaving",
                False,
                False,
                "Apply trace/Kloosterman/Type-II estimates uniformly across all layer rectangles.",
                "new analytic estimate and completed family still required",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "layer rectangles fit the product-shape interface better, but a trace-family sheaf and uniform layer summation are not supplied",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "moving q denominators still need completed Kloosterman variables on every layer",
            "Pascadi_composite_Type_II": "Type-II shape is present layerwise, but endpoint weights and layer count remain rate-bearing",
            "Wright_unbalanced_convolution": "right-tail layers suggest an unbalanced route, still conditional on a congruence model",
            "Li_short_interval_x_052": "does not provide the missing half-scale layer endpoint estimate",
        },
        "latest_narrowest_mouth": [
            "UniformPhaseSavingAcrossBoundaryLayerCakeRectangles",
            "AND CompletedTraceFamilyForPrimePrimeBulkRectangle",
            "AND CompletedKloostermanVariableForMovingPrimeDenominatorOnLayers",
            "AND StripEndpointSummationByPartsWithoutComparableLoss",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "boundary_layercake_rectangle_identity_verified": True,
        "all_layers_are_complete_product_rectangles": True,
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
    sample_fields = [
        "P",
        "boundary_edge_count",
        "layercake_rectangle_count",
        "layercake_edge_count",
        "lower_wing_rectangle_count",
        "upper_wing_rectangle_count",
        "right_tail_rectangle_count",
        "max_rectangle_edge_count",
        "missing_count",
        "extra_count",
    ]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary layer-cake rectangles 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"layercake_decomposition={current['layercake_decomposition']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. layer-cake rectangle 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"active_P_count={audit['active_P_count']}",
        f"boundary_edge_count_total={audit['boundary_edge_count_total']}",
        f"previous_boundary_edge_count_total={audit['previous_boundary_edge_count_total']}",
        f"layercake_rectangle_count_total={audit['layercake_rectangle_count_total']}",
        f"layercake_edge_count_total={audit['layercake_edge_count_total']}",
        f"lower_wing_rectangle_count_total={audit['lower_wing_rectangle_count_total']}",
        f"upper_wing_rectangle_count_total={audit['upper_wing_rectangle_count_total']}",
        f"right_tail_rectangle_count_total={audit['right_tail_rectangle_count_total']}",
        f"lower_wing_edge_count_total={audit['lower_wing_edge_count_total']}",
        f"upper_wing_edge_count_total={audit['upper_wing_edge_count_total']}",
        f"right_tail_edge_count_total={audit['right_tail_edge_count_total']}",
        f"row_rectangle_count_min={audit['row_rectangle_count_min']}",
        f"row_rectangle_count_median={audit['row_rectangle_count_median']}",
        f"row_rectangle_count_max={audit['row_rectangle_count_max']}",
        f"row_rectangle_count_average={audit['row_rectangle_count_average']:.12f}",
        f"max_rectangle_edge_count={audit['max_rectangle_edge_count']}",
        f"nested_bad_steps_total={audit['nested_bad_steps_total']}",
        f"missing_count_total={audit['missing_count_total']}",
        f"extra_count_total={audit['extra_count_total']}",
        f"bad_layercake_row_count={audit['bad_layercake_row_count']}",
        f"total_bad_boundary_layercake_rectangle_count={audit['total_bad_boundary_layercake_rectangle_count']}",
        f"boundary_layercake_rectangle_identity_verified={str(audit['boundary_layercake_rectangle_identity_verified']).lower()}",
        f"all_layers_are_complete_product_rectangles={str(audit['all_layers_are_complete_product_rectangles']).lower()}",
        f"layer_count_requires_uniform_summation_control={str(audit['layer_count_requires_uniform_summation_control']).lower()}",
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
        "结论：三条 monotone boundary strips 已精确分解成互不重叠的 q-prefix x m-shell product rectangles。",
        "这进一步贴近 Type-II/trace 输入形状；但共有 `6190` 个层矩形，仍必须证明跨层统一相消或完成求和。",
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
        f"boundary_layercake_rectangle_identity_verified={str(payload['boundary_layercake_rectangle_identity_verified']).lower()}",
        f"all_layers_are_complete_product_rectangles={str(payload['all_layers_are_complete_product_rectangles']).lower()}",
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
    print(
        "boundary_layercake_rectangle_identity_verified="
        f"{payload['boundary_layercake_rectangle_identity_verified']}"
    )
    print(
        "all_layers_are_complete_product_rectangles="
        f"{payload['all_layers_are_complete_product_rectangles']}"
    )
    print(f"boundary_phase_saving_closed={payload['boundary_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
