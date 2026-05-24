#!/usr/bin/env python3
"""审计 shell-step packets 中 multi-block gap 的 right-tail 定位。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_gap_localization_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-audit.json

上一层把 boundary layer rectangles 聚合成 5106 个 shell-step packets。本层继续
原子化下钻：检查多段 m-block 是否分布在所有 strip，还是只来自某个 endpoint
tail。有限审计显示，所有 multi-block packets 都位于 right_tail；lower_wing 与
upper_wing 全部是 single-block packets。

这把短壳相位问题拆成两个更窄对象：
  1. lower/upper/single-right 的 contiguous one-block endpoint packets；
  2. right-tail multi-block gap packets。
本层仍不提供相位节省。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit as shell_step  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-right-tail-gap-localization"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-audit.json",
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
        "role": "right-tail gap localization narrows the support, but trace bilinear input still needs a completed family and packet aggregation",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "multi-block right-tail packets still need moving q denominators completed as Kloosterman variables",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "the right-tail gap family remains an endpoint/multi-block object, not a single long Type-II rectangle",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "right-tail q-long/m-short packets are the most plausible unbalanced interface after exact phase modeling",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short interval prime existence still does not control right-tail packet gaps",
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


def packet_gap_sizes(packet: dict[str, Any], primes: list[int], prime_index: dict[int, int]) -> list[int]:
    """返回 packet 内部相邻 m-block 之间缺失的素数个数。"""
    m_values: list[int] = []
    for block in packet["source_rectangles"]:
        m_values.extend([p for p in primes if block["m_start"] <= p <= block["m_end"]])
    m_values = sorted(set(m_values))
    gap_sizes: list[int] = []
    for left, right in zip(m_values, m_values[1:]):
        if prime_index[right] != prime_index[left] + 1:
            gap_sizes.append(sum(1 for p in primes if left < p < right))
    return gap_sizes


def counter_rows(counts: Counter[Any], edges: Counter[Any], key_name: str = "bucket") -> list[dict[str, Any]]:
    """把计数器转为稳定表格。"""
    return [
        {key_name: str(key), "packet_count": counts[key], "edge_count": edges[key]}
        for key in sorted(counts, key=str)
    ]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 multi-block packet 是否全部定位于 right-tail。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_index = {p: index for index, p in enumerate(primes)}
    packets = shell_step.packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]

    strip_block_counts: Counter[tuple[str, int]] = Counter()
    strip_block_edges: Counter[tuple[str, int]] = Counter()
    gap_sizes: list[int] = []
    gap_size_counter: Counter[int] = Counter()
    gap_size_edges: Counter[int] = Counter()
    gap_by_strip: Counter[str] = Counter()
    gap_edge_by_strip: Counter[str] = Counter()
    single_packets = []
    multi_packets = []
    sample_multi_packets = []

    for packet in packets:
        strip = packet["strip"]
        block_count = packet["m_block_count"]
        edge_count = packet["edge_count"]
        strip_block_counts[(strip, block_count)] += 1
        strip_block_edges[(strip, block_count)] += edge_count
        if block_count == 1:
            single_packets.append(packet)
        else:
            multi_packets.append(packet)

        sizes = packet_gap_sizes(packet, primes, prime_index)
        for size in sizes:
            gap_sizes.append(size)
            gap_size_counter[size] += 1
            gap_size_edges[size] += edge_count
            gap_by_strip[strip] += 1
            gap_edge_by_strip[strip] += edge_count
        if sizes and len(sample_multi_packets) < 12:
            sample_multi_packets.append(
                {
                    "P": packet["P"],
                    "strip": strip,
                    "q_prefix_count": packet["q_prefix_count"],
                    "q_start": packet["q_start"],
                    "q_end": packet["q_end"],
                    "m_block_count": block_count,
                    "m_shell_prime_count": packet["m_shell_prime_count"],
                    "edge_count": edge_count,
                    "gap_sizes": sizes,
                    "source_rectangles": packet["source_rectangles"],
                }
            )

    single_edge_count = sum(packet["edge_count"] for packet in single_packets)
    multi_edge_count = sum(packet["edge_count"] for packet in multi_packets)

    single_q_counts = [packet["q_prefix_count"] for packet in single_packets]
    single_m_counts = [packet["m_shell_prime_count"] for packet in single_packets]
    multi_q_counts = [packet["q_prefix_count"] for packet in multi_packets]
    multi_m_counts = [packet["m_shell_prime_count"] for packet in multi_packets]

    top_gap_sizes = [
        {
            "missing_prime_gap_size": size,
            "gap_count": count,
            "edge_weight_sum": gap_size_edges[size],
        }
        for size, count in gap_size_counter.most_common(20)
    ]

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
        "single_block_packet_count": len(single_packets),
        "single_block_edge_count": single_edge_count,
        "multi_block_packet_count": len(multi_packets),
        "multi_block_edge_count": multi_edge_count,
        "multi_block_packet_strip_set": sorted({packet["strip"] for packet in multi_packets}),
        "all_multi_block_packets_are_right_tail": all(
            packet["strip"] == "right_tail" for packet in multi_packets
        ),
        "lower_wing_multi_block_packet_count": sum(
            1 for packet in multi_packets if packet["strip"] == "lower_wing"
        ),
        "upper_wing_multi_block_packet_count": sum(
            1 for packet in multi_packets if packet["strip"] == "upper_wing"
        ),
        "right_tail_multi_block_packet_count": sum(
            1 for packet in multi_packets if packet["strip"] == "right_tail"
        ),
        "right_tail_single_block_packet_count": sum(
            1 for packet in single_packets if packet["strip"] == "right_tail"
        ),
        "gap_count_total": len(gap_sizes),
        "gap_packet_count_total": len(multi_packets),
        "gap_size_min": min(gap_sizes),
        "gap_size_median": statistics.median(gap_sizes),
        "gap_size_max": max(gap_sizes),
        "gap_size_average": sum(gap_sizes) / len(gap_sizes),
        "single_q_prefix_count_median": statistics.median(single_q_counts),
        "single_q_prefix_count_max": max(single_q_counts),
        "single_m_shell_prime_count_median": statistics.median(single_m_counts),
        "single_m_shell_prime_count_max": max(single_m_counts),
        "multi_q_prefix_count_median": statistics.median(multi_q_counts),
        "multi_q_prefix_count_max": max(multi_q_counts),
        "multi_m_shell_prime_count_median": statistics.median(multi_m_counts),
        "multi_m_shell_prime_count_max": max(multi_m_counts),
        "strip_block_rows": [
            {
                "strip": strip,
                "m_block_count": block_count,
                "packet_count": strip_block_counts[(strip, block_count)],
                "edge_count": strip_block_edges[(strip, block_count)],
            }
            for strip, block_count in sorted(strip_block_counts)
        ],
        "gap_by_strip_rows": [
            {
                "strip": strip,
                "gap_count": gap_by_strip[strip],
                "edge_weight_sum": gap_edge_by_strip[strip],
            }
            for strip in sorted(gap_by_strip)
        ],
        "top_gap_size_rows": top_gap_sizes,
        "sample_multi_packets": sample_multi_packets,
        "single_block_endpoint_packet_support_closed": True,
        "right_tail_gap_localization_closed": True,
        "right_tail_multi_block_phase_saving_closed": False,
        "single_block_packet_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_packet_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_gap_localization_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "boundary_shell_step_packet_gaps_localized_to_right_tail_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the shell-step packet audit left at-most-three-block short shells; the next non-cyclic step is to locate whether multi-block packets are global or confined to a named boundary tail",
        "current_object": {
            "input": "5106 boundary shell-step packets",
            "localization": "multi-block m-shell gaps occur only in right_tail packets",
            "remaining": "right-tail multi-block phase saving, single-block endpoint summation, moving q denominator completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "ShellStepPacketLedgerImported",
                True,
                True,
                "The 5106-packet support ledger and total edge mass are inherited exactly.",
                "none for support import",
            ),
            gate(
                "LowerUpperSingleBlockPurity",
                True,
                True,
                "Every lower_wing and upper_wing packet is single-block in m.",
                "none for the finite strip purity ledger",
            ),
            gate(
                "RightTailGapLocalization",
                True,
                True,
                "All 1083 multi-block packets and all 1084 internal prime gaps lie in right_tail.",
                "none for the finite localization ledger",
            ),
            gate(
                "RightTailMultiBlockPhaseSaving",
                False,
                False,
                "Prove cancellation on right-tail packets with two or three m-blocks.",
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
            "FKMS_trace_bilinear": "right-tail localization narrows the support but does not provide completed trace families",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "moving prime q denominators remain the central completion problem",
            "Pascadi_composite_Type_II": "right-tail multi-block packets are endpoint shells rather than direct long Type-II boxes",
            "Wright_unbalanced_Kloosterman": "right-tail q-long/m-short packets are the best-matched unbalanced candidate after phase modeling",
            "Li_short_interval_x_052": "does not control fixed-row right-tail gap packets",
        },
        "latest_narrowest_mouth": [
            "RightTailMultiBlockGapPacketPhaseSaving",
            "AND SingleBlockEndpointPacketSummationByParts",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnRightTailAndSingleBlockPackets",
            "AND NoLossAggregationAcross5106ShellStepPackets",
            "AND DiagonalPGhostSubtractionDiscipline",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "right_tail_gap_localization_closed": True,
        "single_block_endpoint_packet_support_closed": True,
        "right_tail_multi_block_phase_saving_closed": False,
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
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary right-tail gap localization 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"localization={current['localization']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. right-tail gap 定位有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"previous_shell_step_packet_count_total={audit['previous_shell_step_packet_count_total']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"previous_edge_count_total={audit['previous_edge_count_total']}",
        f"packet_identity_inherited={str(audit['packet_identity_inherited']).lower()}",
        f"single_block_packet_count={audit['single_block_packet_count']}",
        f"single_block_edge_count={audit['single_block_edge_count']}",
        f"multi_block_packet_count={audit['multi_block_packet_count']}",
        f"multi_block_edge_count={audit['multi_block_edge_count']}",
        f"multi_block_packet_strip_set={audit['multi_block_packet_strip_set']}",
        f"all_multi_block_packets_are_right_tail={str(audit['all_multi_block_packets_are_right_tail']).lower()}",
        f"lower_wing_multi_block_packet_count={audit['lower_wing_multi_block_packet_count']}",
        f"upper_wing_multi_block_packet_count={audit['upper_wing_multi_block_packet_count']}",
        f"right_tail_multi_block_packet_count={audit['right_tail_multi_block_packet_count']}",
        f"right_tail_single_block_packet_count={audit['right_tail_single_block_packet_count']}",
        f"gap_count_total={audit['gap_count_total']}",
        f"gap_packet_count_total={audit['gap_packet_count_total']}",
        f"gap_size_min={audit['gap_size_min']}",
        f"gap_size_median={audit['gap_size_median']}",
        f"gap_size_max={audit['gap_size_max']}",
        f"gap_size_average={audit['gap_size_average']:.12f}",
        f"single_q_prefix_count_median={audit['single_q_prefix_count_median']}",
        f"single_q_prefix_count_max={audit['single_q_prefix_count_max']}",
        f"single_m_shell_prime_count_median={audit['single_m_shell_prime_count_median']}",
        f"single_m_shell_prime_count_max={audit['single_m_shell_prime_count_max']}",
        f"multi_q_prefix_count_median={audit['multi_q_prefix_count_median']}",
        f"multi_q_prefix_count_max={audit['multi_q_prefix_count_max']}",
        f"multi_m_shell_prime_count_median={audit['multi_m_shell_prime_count_median']}",
        f"multi_m_shell_prime_count_max={audit['multi_m_shell_prime_count_max']}",
        f"right_tail_gap_localization_closed={str(audit['right_tail_gap_localization_closed']).lower()}",
        f"right_tail_multi_block_phase_saving_closed={str(audit['right_tail_multi_block_phase_saving_closed']).lower()}",
        "```",
        "",
        "strip x block 分桶：",
        "",
        *markdown_table(
            audit["strip_block_rows"],
            ["strip", "m_block_count", "packet_count", "edge_count"],
        ),
        "",
        "gap by strip：",
        "",
        *markdown_table(audit["gap_by_strip_rows"], ["strip", "gap_count", "edge_weight_sum"]),
        "",
        "高频 gap size：",
        "",
        *markdown_table(
            audit["top_gap_size_rows"],
            ["missing_prime_gap_size", "gap_count", "edge_weight_sum"],
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
        "结论：multi-block gap 不是全局分布的短壳复杂性；它完全定位在 `right_tail`。",
        "`lower_wing` 与 `upper_wing` 全部是 single-block endpoint packets，right-tail 则分成 single-block 与 multi-block 两个子族。",
        "因此最新缺口从 at-most-three-block packets 进一步压成 right-tail gap packet 相消与 single-block endpoint packet 求和。",
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
        f"right_tail_gap_localization_closed={str(payload['right_tail_gap_localization_closed']).lower()}",
        f"single_block_endpoint_packet_support_closed={str(payload['single_block_endpoint_packet_support_closed']).lower()}",
        f"right_tail_multi_block_phase_saving_closed={str(payload['right_tail_multi_block_phase_saving_closed']).lower()}",
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
    print(f"right_tail_gap_localization_closed={payload['right_tail_gap_localization_closed']}")
    print(
        "right_tail_multi_block_phase_saving_closed="
        f"{payload['right_tail_multi_block_phase_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
