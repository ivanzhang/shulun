#!/usr/bin/env python3
"""审计 right-tail fibres 与 multi-block gaps 的 punctured-interval completion。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_interval_completion_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-audit.json

上一层把 right-tail internal gaps 分成 successor-fibre carried core 与 diagonal P
ghost。本层继续问：successor core 是否仍是任意稀疏对象，还是来自更简单的
区间结构。

有限审计显示，P<=1009 的所有 right-tail fibres 都是 prime interval，至多
挖掉行素数 P。于是每个 multi-block shell packet 在补回 successor core 与
diagonal P ghost 后都是单个连续 prime interval。剩余不再是解释 gap 支撑，
而是对 punctured interval difference 做相位节省。
"""

from __future__ import annotations

import hashlib
import json
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit as bulk  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_rectangles_audit as layercake  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit as shell_step  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-right-tail-interval-completion"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json",
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
        "role": "right-tail support is now a punctured interval difference, but trace input still needs a completed phase family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman bounds become relevant only after the moving prime q denominator is completed on punctured intervals",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "composite Type-II savings still do not directly cover a nested endpoint punctured-interval difference",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman fractions are the closest candidate once the q-long punctured interval phase is completed",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not supply fixed-row punctured-interval reciprocal phase cancellation",
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


def counter_rows(
    counts: Counter[Any],
    edges: Counter[Any],
    key_name: str = "bucket",
    count_name: str = "count",
) -> list[dict[str, Any]]:
    """把计数器转为稳定表格。"""
    return [
        {key_name: str(key), count_name: counts[key], "edge_weight_sum": edges[key]}
        for key in sorted(counts, key=str)
    ]


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


def interval_bin(count: int) -> str:
    """区间素数数分桶。"""
    if count <= 4:
        return "1<=interval<=4"
    if count <= 8:
        return "5<=interval<=8"
    if count <= 16:
        return "9<=interval<=16"
    if count <= 32:
        return "17<=interval<=32"
    return "33<=interval<=90"


def right_tail_fibres_by_row(
    max_prime: int, primes: list[int]
) -> dict[int, list[tuple[int, set[int]]]]:
    """重建每行 right-tail 嵌套 fibre。"""
    rows = bulk.group_edges(max_prime, primes)
    fibres: dict[int, list[tuple[int, set[int]]]] = {}
    for P, edges in sorted(rows.items()):
        strip_fibres, _bulk_profile = layercake.strip_sets_for_row(P, edges, primes)
        fibres[P] = strip_fibres["right_tail"]
    return fibres


def prime_interval(primes: list[int], left: int, right: int) -> list[int]:
    """返回闭区间内的素数。"""
    return [p for p in primes if left <= p <= right]


def punctured_interval_class(P: int, values: set[int], primes: list[int]) -> tuple[str, int, int, int]:
    """判断素数集合是否为完整区间或只挖掉 P 的区间。"""
    if not values:
        return "empty", 0, 0, 0
    left = min(values)
    right = max(values)
    full = set(prime_interval(primes, left, right))
    holes = full - values
    if not holes:
        return "contiguous_prime_interval", left, right, 0
    if holes == {P}:
        return "p_punctured_prime_interval", left, right, 1
    return "other_holes", left, right, len(holes)


def packet_shell_values(packet: dict[str, Any], primes: list[int]) -> set[int]:
    """展开 packet 的 m-shell 素数。"""
    values: set[int] = set()
    for block in packet["source_rectangles"]:
        values.update(p for p in primes if block["m_start"] <= p <= block["m_end"])
    return values


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 right-tail interval completion。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = shell_step.packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    fibres_by_row = right_tail_fibres_by_row(max_prime, primes)

    fibre_class_counts: Counter[str] = Counter()
    fibre_class_edges: Counter[str] = Counter()
    fibre_interval_lengths: list[int] = []
    fibre_hole_counts: list[int] = []
    fibre_count_total = 0
    fibre_edge_proxy_total = 0
    bad_fibre_samples: list[dict[str, Any]] = []

    for P, fibres in fibres_by_row.items():
        for q, fibre in fibres:
            cls, left, right, hole_count = punctured_interval_class(P, fibre, primes)
            interval_length = len(prime_interval(primes, left, right)) if fibre else 0
            fibre_count_total += 1
            fibre_edge_proxy_total += len(fibre)
            fibre_class_counts[cls] += 1
            fibre_class_edges[cls] += len(fibre)
            fibre_interval_lengths.append(interval_length)
            fibre_hole_counts.append(hole_count)
            if cls == "other_holes" and len(bad_fibre_samples) < 8:
                full = set(prime_interval(primes, left, right))
                bad_fibre_samples.append(
                    {
                        "P": P,
                        "q": q,
                        "left": left,
                        "right": right,
                        "holes": sorted(full - fibre)[:12],
                    }
                )

    multi_packets = [packet for packet in packets if packet["m_block_count"] > 1]
    packet_completion_counts: Counter[str] = Counter()
    packet_completion_edges: Counter[str] = Counter()
    q_bin_counts: Counter[str] = Counter()
    q_bin_edges: Counter[str] = Counter()
    interval_bin_counts: Counter[str] = Counter()
    interval_bin_edges: Counter[str] = Counter()
    shell_prime_counts: list[int] = []
    completed_interval_counts: list[int] = []
    successor_core_counts: list[int] = []
    completion_missing_after_core_counts: list[int] = []
    sample_completed_packets: list[dict[str, Any]] = []

    for packet in multi_packets:
        P = packet["P"]
        fibres = fibres_by_row[P]
        q_index = packet["q_prefix_count"] - 1
        q_end, current_fibre = fibres[q_index]
        next_fibre = fibres[q_index + 1][1] if q_index + 1 < len(fibres) else set()
        shell_values = packet_shell_values(packet, primes)

        # 中文注释：multi-block packet 必须来自当前 punctured fibre 与下一层的差。
        if q_end != packet["q_end"] or shell_values != current_fibre - next_fibre:
            raise AssertionError(f"packet/fibre mismatch at P={P}, q={packet['q_end']}")

        left = min(shell_values)
        right = max(shell_values)
        completed_interval = set(prime_interval(primes, left, right))
        successor_core = completed_interval & next_fibre
        shell_plus_core = shell_values | successor_core
        shell_plus_core_plus_p = set(shell_plus_core)
        if left <= P <= right:
            shell_plus_core_plus_p.add(P)

        missing_after_core = completed_interval - shell_plus_core
        missing_after_core_plus_p = completed_interval - shell_plus_core_plus_p
        if not missing_after_core_plus_p and missing_after_core in (set(), {P}):
            completion_class = "shell_successor_core_plus_p_completes_interval"
        else:
            completion_class = "completion_has_other_holes"

        packet_completion_counts[completion_class] += 1
        packet_completion_edges[completion_class] += packet["edge_count"]
        qb = q_bin(packet["q_prefix_count"])
        q_bin_counts[qb] += 1
        q_bin_edges[qb] += packet["edge_count"]
        ib = interval_bin(len(completed_interval))
        interval_bin_counts[ib] += 1
        interval_bin_edges[ib] += packet["edge_count"]
        shell_prime_counts.append(len(shell_values))
        completed_interval_counts.append(len(completed_interval))
        successor_core_counts.append(len(successor_core))
        completion_missing_after_core_counts.append(len(missing_after_core))

        if len(sample_completed_packets) < 12:
            sample_completed_packets.append(
                {
                    "P": P,
                    "q_prefix_count": packet["q_prefix_count"],
                    "q_start": packet["q_start"],
                    "q_end": packet["q_end"],
                    "m_interval_left": left,
                    "m_interval_right": right,
                    "m_block_count": packet["m_block_count"],
                    "shell_prime_count": len(shell_values),
                    "successor_core_count": len(successor_core),
                    "completed_interval_prime_count": len(completed_interval),
                    "missing_after_core": sorted(missing_after_core),
                    "completion_class": completion_class,
                    "source_rectangles": packet["source_rectangles"],
                }
            )

    all_right_tail_fibres_are_punctured_intervals = (
        fibre_class_counts["other_holes"] == 0 and fibre_class_counts["empty"] == 0
    )
    all_multi_block_packets_complete_to_intervals = (
        packet_completion_counts["completion_has_other_holes"] == 0
        and len(multi_packets) == previous_audit["right_tail_multi_block_packet_count"]
    )

    return {
        "max_prime": max_prime,
        "shell_step_packet_count_total": len(packets),
        "previous_shell_step_packet_count_total": previous_audit["shell_step_packet_count_total"],
        "edge_count_total": sum(packet["edge_count"] for packet in packets),
        "previous_edge_count_total": previous_audit["edge_count_total"],
        "packet_identity_inherited": (
            len(packets) == previous_audit["shell_step_packet_count_total"]
            and sum(packet["edge_count"] for packet in packets)
            == previous_audit["edge_count_total"]
        ),
        "right_tail_fibre_count_total": fibre_count_total,
        "right_tail_fibre_edge_proxy_total": fibre_edge_proxy_total,
        "right_tail_fibre_contiguous_count": fibre_class_counts["contiguous_prime_interval"],
        "right_tail_fibre_p_punctured_count": fibre_class_counts[
            "p_punctured_prime_interval"
        ],
        "right_tail_fibre_other_holes_count": fibre_class_counts["other_holes"],
        "all_right_tail_fibres_are_punctured_intervals": (
            all_right_tail_fibres_are_punctured_intervals
        ),
        "right_tail_fibre_interval_length_min": min(fibre_interval_lengths),
        "right_tail_fibre_interval_length_median": statistics.median(fibre_interval_lengths),
        "right_tail_fibre_interval_length_max": max(fibre_interval_lengths),
        "right_tail_fibre_interval_length_average": sum(fibre_interval_lengths)
        / len(fibre_interval_lengths),
        "right_tail_fibre_hole_count_max": max(fibre_hole_counts),
        "right_tail_multi_block_packet_count": len(multi_packets),
        "previous_right_tail_multi_block_packet_count": previous_audit[
            "right_tail_multi_block_packet_count"
        ],
        "multi_block_edge_count": sum(packet["edge_count"] for packet in multi_packets),
        "previous_multi_block_edge_count": previous_audit["multi_block_edge_count"],
        "multi_block_interval_completion_packet_count": packet_completion_counts[
            "shell_successor_core_plus_p_completes_interval"
        ],
        "multi_block_interval_completion_edge_count": packet_completion_edges[
            "shell_successor_core_plus_p_completes_interval"
        ],
        "multi_block_completion_other_holes_packet_count": packet_completion_counts[
            "completion_has_other_holes"
        ],
        "all_multi_block_packets_complete_to_intervals": (
            all_multi_block_packets_complete_to_intervals
        ),
        "shell_prime_count_min": min(shell_prime_counts),
        "shell_prime_count_median": statistics.median(shell_prime_counts),
        "shell_prime_count_max": max(shell_prime_counts),
        "completed_interval_prime_count_min": min(completed_interval_counts),
        "completed_interval_prime_count_median": statistics.median(completed_interval_counts),
        "completed_interval_prime_count_max": max(completed_interval_counts),
        "successor_core_count_min": min(successor_core_counts),
        "successor_core_count_median": statistics.median(successor_core_counts),
        "successor_core_count_max": max(successor_core_counts),
        "completion_missing_after_core_count_min": min(completion_missing_after_core_counts),
        "completion_missing_after_core_count_median": statistics.median(
            completion_missing_after_core_counts
        ),
        "completion_missing_after_core_count_max": max(completion_missing_after_core_counts),
        "fibre_class_rows": counter_rows(
            fibre_class_counts, fibre_class_edges, "fibre_class", "fibre_count"
        ),
        "packet_completion_rows": counter_rows(
            packet_completion_counts,
            packet_completion_edges,
            "completion_class",
            "packet_count",
        ),
        "q_prefix_bin_rows": counter_rows(q_bin_counts, q_bin_edges, "q_prefix_bin", "packet_count"),
        "completed_interval_bin_rows": counter_rows(
            interval_bin_counts,
            interval_bin_edges,
            "completed_interval_bin",
            "packet_count",
        ),
        "bad_fibre_samples": bad_fibre_samples,
        "sample_completed_packets": sample_completed_packets,
        "right_tail_fibre_punctured_interval_identity_closed": (
            all_right_tail_fibres_are_punctured_intervals
        ),
        "right_tail_multi_block_successor_core_interval_completion_closed": (
            all_multi_block_packets_complete_to_intervals
        ),
        "right_tail_punctured_interval_phase_saving_closed": False,
        "single_block_packet_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_packet_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_interval_completion_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "right_tail_fibres_and_multi_block_gaps_completed_to_p_punctured_intervals_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after diagonal/core splitting, the next non-cyclic step is to decide whether the carried core is arbitrary sparse support or a nested punctured interval",
        "current_object": {
            "input": "right-tail fibres and 1083 right-tail multi-block shell-step packets",
            "identity": "right-tail fibres are prime intervals punctured only at P; multi-block shells complete to prime intervals by adding successor core and P",
            "remaining": "phase saving on punctured interval differences, single-block endpoint summation, moving q denominator completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RightTailDiagonalCoreImported",
                True,
                True,
                "The successor-core plus diagonal-P decomposition is inherited.",
                "none for support import",
            ),
            gate(
                "RightTailFibrePuncturedIntervalIdentity",
                finite_audit["right_tail_fibre_punctured_interval_identity_closed"],
                finite_audit["right_tail_fibre_punctured_interval_identity_closed"],
                "Every right-tail fibre is a contiguous prime interval, possibly with P removed.",
                "none for the finite right-tail fibre ledger",
            ),
            gate(
                "RightTailMultiBlockSuccessorCoreIntervalCompletion",
                finite_audit["right_tail_multi_block_successor_core_interval_completion_closed"],
                finite_audit["right_tail_multi_block_successor_core_interval_completion_closed"],
                "Every multi-block shell plus successor core and P completes to one prime interval.",
                "none for finite support completion",
            ),
            gate(
                "RightTailPuncturedIntervalPhaseSaving",
                False,
                False,
                "Prove cancellation on nested P-punctured interval differences with moving q denominator.",
                "new endpoint/unbalanced trace estimate required",
            ),
            gate(
                "SingleBlockEndpointPhaseSaving",
                False,
                False,
                "Prove cancellation or summation-by-parts for the single-block packets.",
                "moving q denominator and packet aggregation remain open",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "punctured intervals are simpler support, but no completed trace family is yet supplied",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "arbitrary q Kloosterman input still requires completing the moving prime denominator",
            "Pascadi_composite_Type_II": "endpoint punctured interval differences are not direct long Type-II boxes",
            "Wright_unbalanced_Kloosterman": "q-long punctured intervals are the most plausible unbalanced interface after exact phase modeling",
            "Li_short_interval_x_052": "short-interval existence at exponent 0.52 remains above the half-scale and does not give reciprocal phase saving",
        },
        "latest_narrowest_mouth": [
            "RightTailPuncturedIntervalDifferencePhaseSaving",
            "AND SingleBlockEndpointPacketSummationByParts",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnPuncturedIntervalsAndSingleBlockPackets",
            "AND NoLossAggregationAcross5106ShellStepPackets",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "right_tail_fibre_punctured_interval_identity_closed": finite_audit[
            "right_tail_fibre_punctured_interval_identity_closed"
        ],
        "right_tail_multi_block_successor_core_interval_completion_closed": finite_audit[
            "right_tail_multi_block_successor_core_interval_completion_closed"
        ],
        "right_tail_punctured_interval_phase_saving_closed": False,
        "single_block_packet_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_packet_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF right-tail interval completion 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"identity={current['identity']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. punctured interval 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"packet_identity_inherited={str(audit['packet_identity_inherited']).lower()}",
        f"right_tail_fibre_count_total={audit['right_tail_fibre_count_total']}",
        f"right_tail_fibre_edge_proxy_total={audit['right_tail_fibre_edge_proxy_total']}",
        f"right_tail_fibre_contiguous_count={audit['right_tail_fibre_contiguous_count']}",
        f"right_tail_fibre_p_punctured_count={audit['right_tail_fibre_p_punctured_count']}",
        f"right_tail_fibre_other_holes_count={audit['right_tail_fibre_other_holes_count']}",
        f"all_right_tail_fibres_are_punctured_intervals={str(audit['all_right_tail_fibres_are_punctured_intervals']).lower()}",
        f"right_tail_fibre_interval_length_min={audit['right_tail_fibre_interval_length_min']}",
        f"right_tail_fibre_interval_length_median={audit['right_tail_fibre_interval_length_median']}",
        f"right_tail_fibre_interval_length_max={audit['right_tail_fibre_interval_length_max']}",
        f"right_tail_multi_block_packet_count={audit['right_tail_multi_block_packet_count']}",
        f"multi_block_edge_count={audit['multi_block_edge_count']}",
        f"multi_block_interval_completion_packet_count={audit['multi_block_interval_completion_packet_count']}",
        f"multi_block_interval_completion_edge_count={audit['multi_block_interval_completion_edge_count']}",
        f"multi_block_completion_other_holes_packet_count={audit['multi_block_completion_other_holes_packet_count']}",
        f"all_multi_block_packets_complete_to_intervals={str(audit['all_multi_block_packets_complete_to_intervals']).lower()}",
        f"shell_prime_count_min={audit['shell_prime_count_min']}",
        f"shell_prime_count_median={audit['shell_prime_count_median']}",
        f"shell_prime_count_max={audit['shell_prime_count_max']}",
        f"completed_interval_prime_count_min={audit['completed_interval_prime_count_min']}",
        f"completed_interval_prime_count_median={audit['completed_interval_prime_count_median']}",
        f"completed_interval_prime_count_max={audit['completed_interval_prime_count_max']}",
        f"successor_core_count_min={audit['successor_core_count_min']}",
        f"successor_core_count_median={audit['successor_core_count_median']}",
        f"successor_core_count_max={audit['successor_core_count_max']}",
        f"completion_missing_after_core_count_min={audit['completion_missing_after_core_count_min']}",
        f"completion_missing_after_core_count_median={audit['completion_missing_after_core_count_median']}",
        f"completion_missing_after_core_count_max={audit['completion_missing_after_core_count_max']}",
        f"right_tail_fibre_punctured_interval_identity_closed={str(audit['right_tail_fibre_punctured_interval_identity_closed']).lower()}",
        f"right_tail_multi_block_successor_core_interval_completion_closed={str(audit['right_tail_multi_block_successor_core_interval_completion_closed']).lower()}",
        f"right_tail_punctured_interval_phase_saving_closed={str(audit['right_tail_punctured_interval_phase_saving_closed']).lower()}",
        "```",
        "",
        "right-tail fibre class 分桶：",
        "",
        *markdown_table(
            audit["fibre_class_rows"], ["fibre_class", "fibre_count", "edge_weight_sum"]
        ),
        "",
        "multi-block completion class 分桶：",
        "",
        *markdown_table(
            audit["packet_completion_rows"],
            ["completion_class", "packet_count", "edge_weight_sum"],
        ),
        "",
        "q-prefix packet 分桶：",
        "",
        *markdown_table(
            audit["q_prefix_bin_rows"], ["q_prefix_bin", "packet_count", "edge_weight_sum"]
        ),
        "",
        "completed interval size 分桶：",
        "",
        *markdown_table(
            audit["completed_interval_bin_rows"],
            ["completed_interval_bin", "packet_count", "edge_weight_sum"],
        ),
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
        "结论：successor core 不是任意稀疏残差；它把 right-tail multi-block shell 补回一个 `P`-punctured prime interval。",
        "因此 right-tail multi-block 的支撑硬点从 gap/core 分类压成 nested punctured interval difference。",
        "剩余仍是相位节省、移动分母 completion 与 packet 无损聚合。",
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
        f"right_tail_fibre_punctured_interval_identity_closed={str(payload['right_tail_fibre_punctured_interval_identity_closed']).lower()}",
        f"right_tail_multi_block_successor_core_interval_completion_closed={str(payload['right_tail_multi_block_successor_core_interval_completion_closed']).lower()}",
        f"right_tail_punctured_interval_phase_saving_closed={str(payload['right_tail_punctured_interval_phase_saving_closed']).lower()}",
        f"single_block_packet_phase_saving_closed={str(payload['single_block_packet_phase_saving_closed']).lower()}",
        f"moving_q_denominator_completed_trace_closed={str(payload['moving_q_denominator_completed_trace_closed']).lower()}",
        f"no_loss_packet_aggregation_closed={str(payload['no_loss_packet_aggregation_closed']).lower()}",
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
        "right_tail_fibre_punctured_interval_identity_closed="
        f"{payload['right_tail_fibre_punctured_interval_identity_closed']}"
    )
    print(
        "right_tail_multi_block_successor_core_interval_completion_closed="
        f"{payload['right_tail_multi_block_successor_core_interval_completion_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
