#!/usr/bin/env python3
"""审计 right-tail multi-block gap 的 diagonal/core 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_gap_diagonal_core_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-audit.json

上一层证明所有 multi-block shell gaps 都位于 right_tail。本层继续下钻：
对每个 internal prime gap，检查缺失素数是新的未解释洞，还是由下一层
right-tail fibre 继续携带的 core 与行素数 P 的 diagonal ghost 组成。

有限审计显示，在 P<=1009 的 1084 个 internal gaps 中，没有 unexplained
gap。每个 gap 都满足

  missing primes = successor-fibre carried core disjoint union optional {P}.

这把 right-tail 多段 gap 的支撑障碍压成 successor-fibre core 相消问题；
它仍不提供相位节省，也不闭合 Phi-LPF 奇偶性障碍。
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
    "boundary-right-tail-gap-diagonal-core"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json",
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
        "role": "diagonal/core support splitting removes unexplained gaps, but still needs a completed trace family for successor-fibre cores",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "successor-fibre cores still have moving prime q denominators before arbitrary-modulus Kloosterman input can apply",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "the remaining core is nested endpoint support, not a single long Type-II rectangle",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "the q-long/successor-core form is the closest unbalanced interface after the diagonal ghost is isolated",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval existence does not control successor-fibre carried cores at fixed row and moving q",
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
    count_name: str = "gap_count",
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


def carried_bin(count: int) -> str:
    """successor-fibre carried core 大小分桶。"""
    if count == 0:
        return "carried=0"
    if count <= 4:
        return "1<=carried<=4"
    if count <= 16:
        return "5<=carried<=16"
    if count <= 32:
        return "17<=carried<=32"
    return "33<=carried<=78"


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


def packet_shell_values(packet: dict[str, Any], primes: list[int]) -> list[int]:
    """展开 packet 的 m-shell 素数。"""
    values: list[int] = []
    for block in packet["source_rectangles"]:
        values.extend([p for p in primes if block["m_start"] <= p <= block["m_end"]])
    return sorted(set(values))


def classify_gap(
    P: int,
    gap_values: list[int],
    current_fibre: set[int],
    next_fibre: set[int],
) -> dict[str, Any]:
    """把一个 internal gap 分成 successor core 与 diagonal P ghost。"""
    carried_core = [p for p in gap_values if p in next_fibre]
    diagonal_ghost = [P] if P in gap_values else []
    unexplained = [p for p in gap_values if p not in next_fibre and p != P]
    diagonal_is_absent = P not in current_fibre if diagonal_ghost else True
    verified = not unexplained and diagonal_is_absent

    if not verified:
        gap_class = "unexplained_gap"
    elif diagonal_ghost and carried_core:
        gap_class = "diagonal_plus_carried_core"
    elif diagonal_ghost:
        gap_class = "pure_diagonal_slit"
    else:
        gap_class = "carried_core_without_diagonal"

    if not diagonal_ghost:
        diagonal_position = "no_P_in_gap"
    elif P == gap_values[0]:
        diagonal_position = "P_first_missing_prime"
    elif P == gap_values[-1]:
        diagonal_position = "P_last_missing_prime"
    else:
        diagonal_position = "P_interior_missing_prime"

    return {
        "gap_class": gap_class,
        "verified": verified,
        "gap_size": len(gap_values),
        "carried_core_count": len(carried_core),
        "diagonal_ghost_count": len(diagonal_ghost),
        "diagonal_position": diagonal_position,
        "unexplained_count": len(unexplained),
        "carried_core_sample": carried_core[:6],
        "unexplained_sample": unexplained[:6],
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 right-tail gap 的 diagonal/core 恒等式。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {p: index for index, p in enumerate(primes)}
    packets = shell_step.packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    fibres_by_row = right_tail_fibres_by_row(max_prime, primes)
    multi_packets = [packet for packet in packets if packet["m_block_count"] > 1]

    gap_class_counts: Counter[str] = Counter()
    gap_class_edges: Counter[str] = Counter()
    packet_class_counts: Counter[str] = Counter()
    packet_class_edges: Counter[str] = Counter()
    diagonal_position_counts: Counter[str] = Counter()
    diagonal_position_edges: Counter[str] = Counter()
    carried_bin_counts: Counter[str] = Counter()
    carried_bin_edges: Counter[str] = Counter()
    q_bin_counts: Counter[str] = Counter()
    q_bin_edges: Counter[str] = Counter()
    block_count_counts: Counter[int] = Counter()
    block_count_edges: Counter[int] = Counter()

    gap_sizes: list[int] = []
    carried_counts: list[int] = []
    gap_missing_prime_count_total = 0
    carried_core_prime_count_total = 0
    diagonal_ghost_count_total = 0
    unexplained_prime_count_total = 0
    sample_gap_packets: list[dict[str, Any]] = []

    for packet in multi_packets:
        P = packet["P"]
        q_index = packet["q_prefix_count"] - 1
        fibres = fibres_by_row[P]
        q_end, current_fibre = fibres[q_index]
        next_fibre = fibres[q_index + 1][1] if q_index + 1 < len(fibres) else set()
        shell_values = packet_shell_values(packet, primes)

        # 中文注释：packet 的 shell 应当正好是当前 fibre 剥离下一层 fibre 后的部分。
        if q_end != packet["q_end"] or set(shell_values) != current_fibre - next_fibre:
            raise AssertionError(f"right-tail packet/fibre mismatch at P={P}, q={packet['q_end']}")

        gap_classes_for_packet: list[str] = []
        gap_records: list[dict[str, Any]] = []
        for left, right in zip(shell_values, shell_values[1:]):
            if prime_index[right] == prime_index[left] + 1:
                continue
            gap_values = [p for p in primes if left < p < right]
            record = classify_gap(P, gap_values, current_fibre, next_fibre)
            record.update(
                {
                    "left_shell_prime": left,
                    "right_shell_prime": right,
                    "first_missing_prime": gap_values[0],
                    "last_missing_prime": gap_values[-1],
                }
            )
            gap_classes_for_packet.append(record["gap_class"])
            gap_records.append(record)

            gap_class_counts[record["gap_class"]] += 1
            gap_class_edges[record["gap_class"]] += packet["edge_count"]
            diagonal_position_counts[record["diagonal_position"]] += 1
            diagonal_position_edges[record["diagonal_position"]] += packet["edge_count"]
            cb = carried_bin(record["carried_core_count"])
            carried_bin_counts[cb] += 1
            carried_bin_edges[cb] += packet["edge_count"]

            gap_sizes.append(record["gap_size"])
            carried_counts.append(record["carried_core_count"])
            gap_missing_prime_count_total += record["gap_size"]
            carried_core_prime_count_total += record["carried_core_count"]
            diagonal_ghost_count_total += record["diagonal_ghost_count"]
            unexplained_prime_count_total += record["unexplained_count"]

        if not gap_classes_for_packet:
            raise AssertionError(f"multi-block packet without internal gap at P={P}")

        if len(set(gap_classes_for_packet)) == 1 and len(gap_classes_for_packet) == 1:
            packet_class = f"{gap_classes_for_packet[0]}_packet"
        else:
            packet_class = "+".join(sorted(gap_classes_for_packet)) + "_packet"
        packet_class_counts[packet_class] += 1
        packet_class_edges[packet_class] += packet["edge_count"]

        qb = q_bin(packet["q_prefix_count"])
        q_bin_counts[qb] += 1
        q_bin_edges[qb] += packet["edge_count"]
        block_count_counts[packet["m_block_count"]] += 1
        block_count_edges[packet["m_block_count"]] += packet["edge_count"]

        if len(sample_gap_packets) < 12:
            sample_gap_packets.append(
                {
                    "P": P,
                    "q_prefix_count": packet["q_prefix_count"],
                    "q_start": packet["q_start"],
                    "q_end": packet["q_end"],
                    "m_block_count": packet["m_block_count"],
                    "m_shell_prime_count": packet["m_shell_prime_count"],
                    "edge_count": packet["edge_count"],
                    "gap_records": gap_records,
                    "source_rectangles": packet["source_rectangles"],
                }
            )

    gap_decomposition_verified = unexplained_prime_count_total == 0
    gap_count_total = len(gap_sizes)

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
        "right_tail_multi_block_packet_count": len(multi_packets),
        "previous_right_tail_multi_block_packet_count": previous_audit[
            "right_tail_multi_block_packet_count"
        ],
        "multi_block_edge_count": sum(packet["edge_count"] for packet in multi_packets),
        "previous_multi_block_edge_count": previous_audit["multi_block_edge_count"],
        "gap_count_total": gap_count_total,
        "previous_gap_count_total": previous_audit["gap_count_total"],
        "gap_decomposition_verified": gap_decomposition_verified,
        "unexplained_gap_count": gap_class_counts["unexplained_gap"],
        "unexplained_prime_count_total": unexplained_prime_count_total,
        "gap_missing_prime_count_total": gap_missing_prime_count_total,
        "carried_core_prime_count_total": carried_core_prime_count_total,
        "diagonal_ghost_count_total": diagonal_ghost_count_total,
        "diagonal_ghost_gap_count": gap_count_total - diagonal_position_counts["no_P_in_gap"],
        "no_diagonal_gap_count": diagonal_position_counts["no_P_in_gap"],
        "gap_size_min": min(gap_sizes),
        "gap_size_median": statistics.median(gap_sizes),
        "gap_size_max": max(gap_sizes),
        "gap_size_average": sum(gap_sizes) / gap_count_total,
        "carried_core_count_min": min(carried_counts),
        "carried_core_count_median": statistics.median(carried_counts),
        "carried_core_count_max": max(carried_counts),
        "carried_core_count_average": sum(carried_counts) / gap_count_total,
        "gap_class_rows": counter_rows(gap_class_counts, gap_class_edges, "gap_class"),
        "packet_class_rows": counter_rows(
            packet_class_counts, packet_class_edges, "packet_class", "packet_count"
        ),
        "diagonal_position_rows": counter_rows(
            diagonal_position_counts, diagonal_position_edges, "diagonal_position"
        ),
        "carried_core_bin_rows": counter_rows(carried_bin_counts, carried_bin_edges, "carried_bin"),
        "q_prefix_bin_rows": counter_rows(q_bin_counts, q_bin_edges, "q_prefix_bin", "packet_count"),
        "m_block_count_rows": counter_rows(
            block_count_counts, block_count_edges, "m_block_count", "packet_count"
        ),
        "sample_gap_packets": sample_gap_packets,
        "right_tail_gap_diagonal_core_identity_closed": gap_decomposition_verified,
        "right_tail_diagonal_p_ghost_support_subtraction_closed": gap_decomposition_verified,
        "right_tail_successor_fibre_core_phase_saving_closed": False,
        "single_block_packet_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_packet_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_gap_diagonal_core_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "right_tail_multi_block_gaps_split_into_successor_core_plus_diagonal_ghost_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the previous right-tail localization left diagonal P ghost subtraction and right-tail gap phase saving as distinct support/analytic gates; this audit separates the support identity from the analytic phase-saving problem",
        "current_object": {
            "input": "1083 right-tail multi-block shell-step packets and 1084 internal prime gaps",
            "identity": "each internal gap equals successor-fibre carried core disjoint union optional row-prime P diagonal ghost",
            "remaining": "phase saving on successor-fibre carried cores, single-block endpoint summation, moving q denominator completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RightTailGapLocalizationImported",
                True,
                True,
                "The 1083 multi-block packets and 1084 gaps are inherited from the right-tail localization ledger.",
                "none for support import",
            ),
            gate(
                "RightTailGapDiagonalCoreIdentity",
                finite_audit["gap_decomposition_verified"],
                finite_audit["gap_decomposition_verified"],
                "Every internal gap decomposes into successor-fibre carried primes plus optional row-prime P.",
                "none for the finite diagonal/core identity ledger",
            ),
            gate(
                "RightTailDiagonalPGhostSupportSubtraction",
                finite_audit["right_tail_diagonal_p_ghost_support_subtraction_closed"],
                finite_audit["right_tail_diagonal_p_ghost_support_subtraction_closed"],
                "The only gap element not carried by the successor fibre is the row-prime diagonal ghost P.",
                "none for right-tail multi-block support subtraction",
            ),
            gate(
                "RightTailSuccessorFibreCorePhaseSaving",
                False,
                False,
                "Prove cancellation on the carried core after diagonal support subtraction.",
                "new completed trace or endpoint summation estimate required",
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
            "FKMS_trace_bilinear": "support identity removes unexplained gaps but still lacks completed trace families for successor cores",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "moving prime q denominators remain the central completion problem",
            "Pascadi_composite_Type_II": "successor cores are nested endpoint supports rather than direct long Type-II boxes",
            "Wright_unbalanced_Kloosterman": "right-tail q-long/successor-core packets are the closest unbalanced candidate after diagonal subtraction",
            "Li_short_interval_x_052": "short-interval existence does not control fixed-row successor-core phase sums",
        },
        "latest_narrowest_mouth": [
            "RightTailSuccessorFibreCorePhaseSaving",
            "AND SingleBlockEndpointPacketSummationByParts",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnSuccessorCoreAndSingleBlockPackets",
            "AND NoLossAggregationAcross5106ShellStepPackets",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "right_tail_gap_diagonal_core_identity_closed": finite_audit[
            "right_tail_gap_diagonal_core_identity_closed"
        ],
        "right_tail_diagonal_p_ghost_support_subtraction_closed": finite_audit[
            "right_tail_diagonal_p_ghost_support_subtraction_closed"
        ],
        "right_tail_successor_fibre_core_phase_saving_closed": False,
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
        "# Prime Matrix Phi-LPF right-tail gap diagonal/core 审计",
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
        "## 2. diagonal/core 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"previous_shell_step_packet_count_total={audit['previous_shell_step_packet_count_total']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"previous_edge_count_total={audit['previous_edge_count_total']}",
        f"packet_identity_inherited={str(audit['packet_identity_inherited']).lower()}",
        f"right_tail_multi_block_packet_count={audit['right_tail_multi_block_packet_count']}",
        f"previous_right_tail_multi_block_packet_count={audit['previous_right_tail_multi_block_packet_count']}",
        f"multi_block_edge_count={audit['multi_block_edge_count']}",
        f"previous_multi_block_edge_count={audit['previous_multi_block_edge_count']}",
        f"gap_count_total={audit['gap_count_total']}",
        f"previous_gap_count_total={audit['previous_gap_count_total']}",
        f"gap_decomposition_verified={str(audit['gap_decomposition_verified']).lower()}",
        f"unexplained_gap_count={audit['unexplained_gap_count']}",
        f"unexplained_prime_count_total={audit['unexplained_prime_count_total']}",
        f"gap_missing_prime_count_total={audit['gap_missing_prime_count_total']}",
        f"carried_core_prime_count_total={audit['carried_core_prime_count_total']}",
        f"diagonal_ghost_count_total={audit['diagonal_ghost_count_total']}",
        f"diagonal_ghost_gap_count={audit['diagonal_ghost_gap_count']}",
        f"no_diagonal_gap_count={audit['no_diagonal_gap_count']}",
        f"gap_size_min={audit['gap_size_min']}",
        f"gap_size_median={audit['gap_size_median']}",
        f"gap_size_max={audit['gap_size_max']}",
        f"gap_size_average={audit['gap_size_average']:.12f}",
        f"carried_core_count_min={audit['carried_core_count_min']}",
        f"carried_core_count_median={audit['carried_core_count_median']}",
        f"carried_core_count_max={audit['carried_core_count_max']}",
        f"carried_core_count_average={audit['carried_core_count_average']:.12f}",
        f"right_tail_gap_diagonal_core_identity_closed={str(audit['right_tail_gap_diagonal_core_identity_closed']).lower()}",
        f"right_tail_successor_fibre_core_phase_saving_closed={str(audit['right_tail_successor_fibre_core_phase_saving_closed']).lower()}",
        "```",
        "",
        "gap class 分桶：",
        "",
        *markdown_table(audit["gap_class_rows"], ["gap_class", "gap_count", "edge_weight_sum"]),
        "",
        "packet class 分桶：",
        "",
        *markdown_table(
            audit["packet_class_rows"], ["packet_class", "packet_count", "edge_weight_sum"]
        ),
        "",
        "diagonal P 位置分桶：",
        "",
        *markdown_table(
            audit["diagonal_position_rows"],
            ["diagonal_position", "gap_count", "edge_weight_sum"],
        ),
        "",
        "successor-fibre carried core 分桶：",
        "",
        *markdown_table(
            audit["carried_core_bin_rows"], ["carried_bin", "gap_count", "edge_weight_sum"]
        ),
        "",
        "q-prefix packet 分桶：",
        "",
        *markdown_table(
            audit["q_prefix_bin_rows"], ["q_prefix_bin", "packet_count", "edge_weight_sum"]
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
        "结论：right-tail multi-block gap 中没有第三类未知缺口。",
        "每个 gap 都是 successor-fibre carried core 加可选 diagonal `P` ghost。",
        "因此 `DiagonalPGhostSubtractionDiscipline` 在 right-tail multi-block 支撑层已经被剥离为显式恒等式；剩余是真正的 carried-core 相位节省。",
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
        f"right_tail_gap_diagonal_core_identity_closed={str(payload['right_tail_gap_diagonal_core_identity_closed']).lower()}",
        f"right_tail_diagonal_p_ghost_support_subtraction_closed={str(payload['right_tail_diagonal_p_ghost_support_subtraction_closed']).lower()}",
        f"right_tail_successor_fibre_core_phase_saving_closed={str(payload['right_tail_successor_fibre_core_phase_saving_closed']).lower()}",
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
        "right_tail_gap_diagonal_core_identity_closed="
        f"{payload['right_tail_gap_diagonal_core_identity_closed']}"
    )
    print(
        "right_tail_successor_fibre_core_phase_saving_closed="
        f"{payload['right_tail_successor_fibre_core_phase_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
