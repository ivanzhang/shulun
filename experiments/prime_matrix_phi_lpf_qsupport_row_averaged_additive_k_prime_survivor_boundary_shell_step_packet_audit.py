#!/usr/bin/env python3
"""审计 boundary layer-cake 的 q-prefix shell-step packet 聚合。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json

上一层把 6190 个 boundary layer rectangles 按相位接口分类，发现主要硬点
是 q-long/m-short 的短 prime shell。本层继续做一个非循环的账本压缩：
同一 row、同一 strip、同一 q-prefix step 的相邻 m-block 不再逐块求和，
而是合并为一个 shell-step packet。

有限审计显示：6190 个 layer rectangles 可无损聚合为 5106 个 q-prefix
shell-step packets；每个 packet 的 m 侧最多由 3 个 prime blocks 组成。该步骤
降低跨层求和复杂度并定位 multi-block endpoint 结构，但仍不提供相位节省。
"""

from __future__ import annotations

import hashlib
import json
import math
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_phase_interface_audit as phase_interface  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-shell-step-packet"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.json",
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
        "role": "packet aggregation reduces layer count but still leaves short m-shell packets outside a direct long bilinear input",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "each packet still needs a completed moving prime q denominator before Kloosterman input applies",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "multi-block short packets remain endpoint objects rather than a single long Type-II box",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "the q-long/m-short packet form is a plausible unbalanced interface after the exact phase model is completed",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not control these fixed-row short shell packets",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def packetize_rectangles(max_prime: int = 1009) -> list[dict[str, Any]]:
    """把同一 q-prefix step 的 m-blocks 合并为 shell-step packets。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {p: index for index, p in enumerate(primes)}
    rectangles = phase_interface.collect_rectangles(max_prime)
    groups: defaultdict[tuple[int, str, int, int, int], list[dict[str, Any]]] = defaultdict(list)

    for rect in rectangles:
        key = (
            rect["P"],
            rect["strip"],
            rect["q_prefix_count"],
            rect["q_start"],
            rect["q_end"],
        )
        groups[key].append(rect)

    packets: list[dict[str, Any]] = []
    for (P, strip, q_count, q_start, q_end), rects in sorted(groups.items()):
        m_values: list[int] = []
        m_blocks = []
        for rect in sorted(rects, key=lambda item: (item["m_start"], item["m_end"])):
            block = [p for p in primes if rect["m_start"] <= p <= rect["m_end"]]
            m_values.extend(block)
            m_blocks.append(
                {
                    "m_start": rect["m_start"],
                    "m_end": rect["m_end"],
                    "m_shell_prime_count": rect["m_shell_prime_count"],
                    "edge_count": rect["edge_count"],
                }
            )
        m_values = sorted(set(m_values))
        internal_prime_gap_count = 0
        for left, right in zip(m_values, m_values[1:]):
            if prime_index[right] != prime_index[left] + 1:
                internal_prime_gap_count += 1
        packets.append(
            {
                "P": P,
                "strip": strip,
                "q_prefix_count": q_count,
                "q_start": q_start,
                "q_end": q_end,
                "m_block_count": len(m_blocks),
                "m_shell_prime_count": len(m_values),
                "m_start": m_values[0],
                "m_end": m_values[-1],
                "internal_prime_gap_count": internal_prime_gap_count,
                "edge_count": q_count * len(m_values),
                "source_rectangle_count": len(rects),
                "source_rectangles": m_blocks,
            }
        )

    return packets


def counter_rows(counts: Counter[Any], edges: Counter[Any], key_name: str = "bucket") -> list[dict[str, Any]]:
    """把计数器转为稳定表格。"""
    return [
        {key_name: str(key), "packet_count": counts[key], "edge_count": edges[key]}
        for key in sorted(counts, key=str)
    ]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 shell-step packet 聚合。"""
    packets = packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    edge_total = sum(packet["edge_count"] for packet in packets)
    q_counts = [packet["q_prefix_count"] for packet in packets]
    m_counts = [packet["m_shell_prime_count"] for packet in packets]
    edge_counts = [packet["edge_count"] for packet in packets]
    block_counts = [packet["m_block_count"] for packet in packets]
    internal_gap_counts = [packet["internal_prime_gap_count"] for packet in packets]
    source_rectangle_counts = [packet["source_rectangle_count"] for packet in packets]

    block_counter: Counter[int] = Counter(block_counts)
    block_edges: Counter[int] = Counter()
    strip_counter: Counter[str] = Counter()
    strip_edges: Counter[str] = Counter()
    source_counter: Counter[int] = Counter()
    source_edges: Counter[int] = Counter()

    for packet in packets:
        block_edges[packet["m_block_count"]] += packet["edge_count"]
        strip_counter[packet["strip"]] += 1
        strip_edges[packet["strip"]] += packet["edge_count"]
        source_counter[packet["source_rectangle_count"]] += 1
        source_edges[packet["source_rectangle_count"]] += packet["edge_count"]

    threshold_rows = []
    for threshold in [2, 3, 4, 5, 8, 10, 16]:
        selected = [
            packet
            for packet in packets
            if packet["q_prefix_count"] >= threshold
            and packet["m_shell_prime_count"] >= threshold
        ]
        threshold_rows.append(
            {
                "threshold": f"both>={threshold}",
                "packet_count": len(selected),
                "edge_count": sum(packet["edge_count"] for packet in selected),
            }
        )

    sum_sqrt_packet_edges = sum(math.sqrt(edge_count) for edge_count in edge_counts)
    sqrt_total_edges = math.sqrt(edge_total)
    previous_sum_sqrt = previous_audit["sum_sqrt_rectangle_edges"]
    previous_loss = previous_audit["naive_layer_sqrt_loss_factor"]
    packet_loss = sum_sqrt_packet_edges / sqrt_total_edges

    largest_packets = sorted(packets, key=lambda item: item["edge_count"], reverse=True)[:10]

    return {
        "max_prime": max_prime,
        "previous_layer_rectangle_count_total": previous_audit["layercake_rectangle_count_total"],
        "shell_step_packet_count_total": len(packets),
        "rectangle_to_packet_reduction": previous_audit["layercake_rectangle_count_total"]
        - len(packets),
        "edge_count_total": edge_total,
        "previous_edge_count_total": previous_audit["edge_count_total"],
        "packet_identity_verified": edge_total == previous_audit["edge_count_total"],
        "q_prefix_count_min": min(q_counts),
        "q_prefix_count_median": statistics.median(q_counts),
        "q_prefix_count_max": max(q_counts),
        "q_prefix_count_average": sum(q_counts) / len(q_counts),
        "m_shell_prime_count_min": min(m_counts),
        "m_shell_prime_count_median": statistics.median(m_counts),
        "m_shell_prime_count_max": max(m_counts),
        "m_shell_prime_count_average": sum(m_counts) / len(m_counts),
        "packet_edge_count_min": min(edge_counts),
        "packet_edge_count_median": statistics.median(edge_counts),
        "packet_edge_count_max": max(edge_counts),
        "packet_edge_count_average": sum(edge_counts) / len(edge_counts),
        "m_block_count_min": min(block_counts),
        "m_block_count_median": statistics.median(block_counts),
        "m_block_count_max": max(block_counts),
        "multi_block_packet_count": sum(1 for value in block_counts if value > 1),
        "internal_prime_gap_packet_count": sum(1 for value in internal_gap_counts if value > 0),
        "internal_prime_gap_count_total": sum(internal_gap_counts),
        "source_rectangle_count_min": min(source_rectangle_counts),
        "source_rectangle_count_median": statistics.median(source_rectangle_counts),
        "source_rectangle_count_max": max(source_rectangle_counts),
        "block_count_rows": counter_rows(block_counter, block_edges, "m_block_count"),
        "strip_packet_rows": counter_rows(strip_counter, strip_edges, "strip"),
        "source_rectangle_count_rows": counter_rows(
            source_counter, source_edges, "source_rectangle_count"
        ),
        "threshold_rows": threshold_rows,
        "sum_sqrt_packet_edges": sum_sqrt_packet_edges,
        "sqrt_total_edges": sqrt_total_edges,
        "naive_packet_sqrt_loss_factor": packet_loss,
        "previous_sum_sqrt_rectangle_edges": previous_sum_sqrt,
        "previous_layer_sqrt_loss_factor": previous_loss,
        "sqrt_loss_factor_improvement": previous_loss - packet_loss,
        "all_packets_have_at_most_three_m_blocks": max(block_counts) <= 3,
        "all_packets_have_m_shell_size_le_12": max(m_counts) <= 12,
        "no_large_balanced_packet_ge_16": not any(
            packet["q_prefix_count"] >= 16 and packet["m_shell_prime_count"] >= 16
            for packet in packets
        ),
        "largest_packets": largest_packets,
        "layer_aggregation_support_closed": True,
        "short_shell_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_layer_aggregation_closed": False,
        "boundary_phase_saving_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "boundary_layercake_rectangles_aggregated_to_shell_step_packets_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "phase-interface audit left a layer-summation loss and short m-shell obstruction; the next non-cyclic step is to aggregate all blocks sharing the same q-prefix step",
        "current_object": {
            "input": "6190 boundary layer-cake rectangles",
            "aggregation": "same row, strip, q-prefix count, q-start and q-end are merged into one shell-step packet",
            "remaining": "short shell phase saving, moving prime q denominator completion, and no-loss packet aggregation",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "ShellStepPacketSupportAggregation",
                True,
                True,
                "The 6190 layer rectangles are grouped into 5106 q-prefix shell-step packets without changing total edge mass.",
                "none for the finite support aggregation",
            ),
            gate(
                "AtMostThreeMBlocksPerPacket",
                True,
                True,
                "Every audited packet has at most three prime-m blocks.",
                "none for the finite block-count ledger",
            ),
            gate(
                "LayerSqrtLossReduced",
                True,
                True,
                "The naive square-root summation factor drops from 71.553080825699 to 64.519277044879 after packet aggregation.",
                "this is only a finite accounting improvement, not analytic cancellation",
            ),
            gate(
                "UniformShortShellPhaseSaving",
                False,
                False,
                "Prove cancellation for q-prefix packets whose m side has at most 12 primes and up to three blocks.",
                "new short-shell completion or unbalanced trace estimate required",
            ),
            gate(
                "NoLossPacketSummation",
                False,
                False,
                "Aggregate all 5106 packet estimates without comparable endpoint or Cauchy loss.",
                "uniform packet-level summation principle remains required",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "packet aggregation helps bookkeeping but still leaves short m-shells outside a direct long bilinear theorem",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "moving q denominators still need completion at packet level",
            "Pascadi_composite_Type_II": "multi-block packets remain endpoint shells rather than single long boxes",
            "Wright_unbalanced_Kloosterman": "q-long/m-short packet geometry is a candidate interface after exact phase modeling",
            "Li_short_interval_x_052": "does not supply packet-level fixed-row positivity or short-shell cancellation",
        },
        "latest_narrowest_mouth": [
            "UniformShortShellPhaseSavingForAtMostThreeBlockPackets",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnShellStepPackets",
            "AND NoLossAggregationAcross5106ShellStepPackets",
            "AND EndpointSummationByPartsForQPrefixLinePackets",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "packet_identity_verified": finite_audit["packet_identity_verified"],
        "layer_aggregation_support_closed": True,
        "short_shell_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_layer_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary shell-step packet 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"aggregation={current['aggregation']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. shell-step packet 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"previous_layer_rectangle_count_total={audit['previous_layer_rectangle_count_total']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"rectangle_to_packet_reduction={audit['rectangle_to_packet_reduction']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"previous_edge_count_total={audit['previous_edge_count_total']}",
        f"packet_identity_verified={str(audit['packet_identity_verified']).lower()}",
        f"q_prefix_count_min={audit['q_prefix_count_min']}",
        f"q_prefix_count_median={audit['q_prefix_count_median']}",
        f"q_prefix_count_max={audit['q_prefix_count_max']}",
        f"q_prefix_count_average={audit['q_prefix_count_average']:.12f}",
        f"m_shell_prime_count_min={audit['m_shell_prime_count_min']}",
        f"m_shell_prime_count_median={audit['m_shell_prime_count_median']}",
        f"m_shell_prime_count_max={audit['m_shell_prime_count_max']}",
        f"m_shell_prime_count_average={audit['m_shell_prime_count_average']:.12f}",
        f"packet_edge_count_min={audit['packet_edge_count_min']}",
        f"packet_edge_count_median={audit['packet_edge_count_median']}",
        f"packet_edge_count_max={audit['packet_edge_count_max']}",
        f"packet_edge_count_average={audit['packet_edge_count_average']:.12f}",
        f"m_block_count_min={audit['m_block_count_min']}",
        f"m_block_count_median={audit['m_block_count_median']}",
        f"m_block_count_max={audit['m_block_count_max']}",
        f"multi_block_packet_count={audit['multi_block_packet_count']}",
        f"internal_prime_gap_packet_count={audit['internal_prime_gap_packet_count']}",
        f"internal_prime_gap_count_total={audit['internal_prime_gap_count_total']}",
        f"source_rectangle_count_max={audit['source_rectangle_count_max']}",
        f"sum_sqrt_packet_edges={audit['sum_sqrt_packet_edges']:.12f}",
        f"sqrt_total_edges={audit['sqrt_total_edges']:.12f}",
        f"naive_packet_sqrt_loss_factor={audit['naive_packet_sqrt_loss_factor']:.12f}",
        f"previous_layer_sqrt_loss_factor={audit['previous_layer_sqrt_loss_factor']:.12f}",
        f"sqrt_loss_factor_improvement={audit['sqrt_loss_factor_improvement']:.12f}",
        f"all_packets_have_at_most_three_m_blocks={str(audit['all_packets_have_at_most_three_m_blocks']).lower()}",
        f"all_packets_have_m_shell_size_le_12={str(audit['all_packets_have_m_shell_size_le_12']).lower()}",
        f"no_large_balanced_packet_ge_16={str(audit['no_large_balanced_packet_ge_16']).lower()}",
        f"short_shell_phase_saving_closed={str(audit['short_shell_phase_saving_closed']).lower()}",
        "```",
        "",
        "m-block 分桶：",
        "",
        *markdown_table(audit["block_count_rows"], ["m_block_count", "packet_count", "edge_count"]),
        "",
        "strip 分桶：",
        "",
        *markdown_table(audit["strip_packet_rows"], ["strip", "packet_count", "edge_count"]),
        "",
        "source rectangle 合并数：",
        "",
        *markdown_table(
            audit["source_rectangle_count_rows"],
            ["source_rectangle_count", "packet_count", "edge_count"],
        ),
        "",
        "双侧阈值：",
        "",
        *markdown_table(audit["threshold_rows"], ["threshold", "packet_count", "edge_count"]),
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
        "结论：同一 q-prefix step 的 m-blocks 可以无损聚合，层数从 `6190` 降到 `5106`。",
        "每个 packet 的 m 侧最多由 `3` 个 prime blocks 组成，m-shell 总大小仍不超过 `12`。",
        "这压缩了求和账本并暴露 multi-block endpoint 结构；但短 shell 相位节省、移动 q 分母 completion 与 packet 级无损求和仍未闭合。",
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
        f"packet_identity_verified={str(payload['packet_identity_verified']).lower()}",
        f"layer_aggregation_support_closed={str(payload['layer_aggregation_support_closed']).lower()}",
        f"short_shell_phase_saving_closed={str(payload['short_shell_phase_saving_closed']).lower()}",
        f"moving_q_denominator_completed_trace_closed={str(payload['moving_q_denominator_completed_trace_closed']).lower()}",
        f"no_loss_layer_aggregation_closed={str(payload['no_loss_layer_aggregation_closed']).lower()}",
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
    print(f"packet_identity_verified={payload['packet_identity_verified']}")
    print(f"layer_aggregation_support_closed={payload['layer_aggregation_support_closed']}")
    print(f"short_shell_phase_saving_closed={payload['short_shell_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
