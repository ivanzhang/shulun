#!/usr/bin/env python3
"""审计 right-tail punctured interval difference 的 endpoint collar 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_endpoint_collar_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-audit.json

上一层证明每条 right-tail fibre 是 prime interval minus optional {P}。本层继续
原子化相邻 fibre 的差：它不是任意 punctured interval difference，而是两个端点
collar 的通量，或终端 full interval 通量，再挖掉可选 diagonal P。

有限审计显示，P<=1009 的 2107 个 right-tail shell-step packets 全部满足该
endpoint-collar 恒等式，零例外。该层仍不提供相位节省；它只把 right-tail
相位门改写为左右端点 collar flux 的相消问题。
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
    "boundary-right-tail-endpoint-collar"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json",
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
        "role": "endpoint-collar support is simpler, but trace bilinear estimates still need a completed moving-denominator phase family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "collar flux still has prime q denominators moving with the row before arbitrary-modulus Kloosterman input applies",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "endpoint collars are short flux packets, not a direct long composite Type-II rectangle",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "q-long endpoint collars are the closest unbalanced Kloosterman candidate after exact phase completion",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "prime existence in x^0.52 intervals still does not supply endpoint-collar reciprocal phase cancellation",
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
    count_name: str = "packet_count",
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


def collar_bin(count: int) -> str:
    """collar 素数个数分桶。"""
    if count == 0:
        return "collar=0"
    if count <= 2:
        return "1<=collar<=2"
    if count <= 4:
        return "3<=collar<=4"
    if count <= 8:
        return "5<=collar<=8"
    return "9<=collar<=13"


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


def prime_interval(primes: list[int], left: int, right: int) -> set[int]:
    """返回闭区间内的素数集合。"""
    return {p for p in primes if left <= p <= right}


def packet_shell_values(packet: dict[str, Any], primes: list[int]) -> set[int]:
    """展开 packet 的 m-shell 素数。"""
    values: set[int] = set()
    for block in packet["source_rectangles"]:
        values.update(p for p in primes if block["m_start"] <= p <= block["m_end"])
    return values


def collar_profile(
    P: int,
    packet: dict[str, Any],
    fibres: list[tuple[int, set[int]]],
    primes: list[int],
) -> dict[str, Any]:
    """计算一个 right-tail packet 的左右 endpoint collar。"""
    q_index = packet["q_prefix_count"] - 1
    q_end, current_fibre = fibres[q_index]
    next_fibre = fibres[q_index + 1][1] if q_index + 1 < len(fibres) else set()
    shell_values = packet_shell_values(packet, primes)
    if q_end != packet["q_end"] or shell_values != current_fibre - next_fibre:
        raise AssertionError(f"right-tail packet/fibre mismatch at P={P}, q={packet['q_end']}")

    current_full = prime_interval(primes, min(current_fibre), max(current_fibre))
    if next_fibre:
        left_collar = {p for p in current_full if p < min(next_fibre)}
        right_collar = {p for p in current_full if p > max(next_fibre)}
        terminal = False
    else:
        left_collar = set(current_full)
        right_collar = set()
        terminal = True

    completed_collar = left_collar | right_collar
    p_puncture = P in completed_collar
    expected_shell = completed_collar - ({P} if p_puncture else set())
    identity_verified = expected_shell == shell_values

    if terminal:
        collar_class = "terminal_full_interval"
    elif left_collar and right_collar:
        collar_class = "two_sided_left_and_right_collars"
    elif left_collar:
        collar_class = "left_collar_only"
    elif right_collar:
        collar_class = "right_collar_only"
    else:
        collar_class = "empty_collar_impossible"
    collar_class += "_with_P_puncture" if p_puncture else "_no_P_puncture"

    return {
        "P": P,
        "q_prefix_count": packet["q_prefix_count"],
        "q_start": packet["q_start"],
        "q_end": packet["q_end"],
        "m_block_count": packet["m_block_count"],
        "m_shell_prime_count": packet["m_shell_prime_count"],
        "edge_count": packet["edge_count"],
        "terminal": terminal,
        "collar_class": collar_class,
        "left_collar_count": len(left_collar),
        "right_collar_count": len(right_collar),
        "completed_collar_count": len(completed_collar),
        "p_puncture_count": 1 if p_puncture else 0,
        "identity_verified": identity_verified,
        "left_collar_range": [
            min(left_collar) if left_collar else None,
            max(left_collar) if left_collar else None,
        ],
        "right_collar_range": [
            min(right_collar) if right_collar else None,
            max(right_collar) if right_collar else None,
        ],
        "unexpected_missing": sorted(expected_shell - shell_values)[:12],
        "unexpected_extra": sorted(shell_values - expected_shell)[:12],
        "source_rectangles": packet["source_rectangles"],
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 right-tail endpoint collar 恒等式。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = shell_step.packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    fibres_by_row = right_tail_fibres_by_row(max_prime, primes)
    right_tail_packets = [packet for packet in packets if packet["strip"] == "right_tail"]

    collar_class_counts: Counter[str] = Counter()
    collar_class_edges: Counter[str] = Counter()
    block_class_counts: Counter[tuple[str, int]] = Counter()
    block_class_edges: Counter[tuple[str, int]] = Counter()
    q_bin_counts: Counter[str] = Counter()
    q_bin_edges: Counter[str] = Counter()
    left_bin_counts: Counter[str] = Counter()
    left_bin_edges: Counter[str] = Counter()
    right_bin_counts: Counter[str] = Counter()
    right_bin_edges: Counter[str] = Counter()
    completed_bin_counts: Counter[str] = Counter()
    completed_bin_edges: Counter[str] = Counter()

    left_counts: list[int] = []
    right_counts: list[int] = []
    completed_counts: list[int] = []
    p_puncture_counts: list[int] = []
    bad_packet_samples: list[dict[str, Any]] = []
    sample_packets: list[dict[str, Any]] = []

    for packet in right_tail_packets:
        profile = collar_profile(packet["P"], packet, fibres_by_row[packet["P"]], primes)
        collar_class = profile["collar_class"]
        edge_count = profile["edge_count"]
        collar_class_counts[collar_class] += 1
        collar_class_edges[collar_class] += edge_count
        block_key = (collar_class, profile["m_block_count"])
        block_class_counts[block_key] += 1
        block_class_edges[block_key] += edge_count

        qb = q_bin(profile["q_prefix_count"])
        q_bin_counts[qb] += 1
        q_bin_edges[qb] += edge_count
        lb = collar_bin(profile["left_collar_count"])
        rb = collar_bin(profile["right_collar_count"])
        cb = collar_bin(profile["completed_collar_count"])
        left_bin_counts[lb] += 1
        left_bin_edges[lb] += edge_count
        right_bin_counts[rb] += 1
        right_bin_edges[rb] += edge_count
        completed_bin_counts[cb] += 1
        completed_bin_edges[cb] += edge_count

        left_counts.append(profile["left_collar_count"])
        right_counts.append(profile["right_collar_count"])
        completed_counts.append(profile["completed_collar_count"])
        p_puncture_counts.append(profile["p_puncture_count"])

        if not profile["identity_verified"] and len(bad_packet_samples) < 8:
            bad_packet_samples.append(profile)
        if len(sample_packets) < 14 and (
            profile["m_block_count"] > 1
            or profile["p_puncture_count"]
            or "two_sided" in profile["collar_class"]
        ):
            sample_packets.append(profile)

    identity_verified = not bad_packet_samples
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
        "right_tail_packet_count": len(right_tail_packets),
        "right_tail_edge_count": sum(packet["edge_count"] for packet in right_tail_packets),
        "previous_right_tail_fibre_edge_proxy_total": previous_audit[
            "right_tail_fibre_edge_proxy_total"
        ],
        "right_tail_single_block_packet_count": sum(
            1 for packet in right_tail_packets if packet["m_block_count"] == 1
        ),
        "right_tail_multi_block_packet_count": sum(
            1 for packet in right_tail_packets if packet["m_block_count"] > 1
        ),
        "previous_right_tail_multi_block_packet_count": previous_audit[
            "right_tail_multi_block_packet_count"
        ],
        "right_tail_endpoint_collar_identity_verified": identity_verified,
        "bad_endpoint_collar_packet_count": len(bad_packet_samples),
        "terminal_full_interval_packet_count": sum(
            count
            for key, count in collar_class_counts.items()
            if key.startswith("terminal_full_interval")
        ),
        "two_sided_collar_packet_count": sum(
            count
            for key, count in collar_class_counts.items()
            if key.startswith("two_sided")
        ),
        "one_sided_collar_packet_count": sum(
            count
            for key, count in collar_class_counts.items()
            if key.startswith("left_collar") or key.startswith("right_collar")
        ),
        "p_punctured_packet_count": sum(p_puncture_counts),
        "left_collar_count_min": min(left_counts),
        "left_collar_count_median": statistics.median(left_counts),
        "left_collar_count_max": max(left_counts),
        "left_collar_count_average": sum(left_counts) / len(left_counts),
        "right_collar_count_min": min(right_counts),
        "right_collar_count_median": statistics.median(right_counts),
        "right_collar_count_max": max(right_counts),
        "right_collar_count_average": sum(right_counts) / len(right_counts),
        "completed_collar_count_min": min(completed_counts),
        "completed_collar_count_median": statistics.median(completed_counts),
        "completed_collar_count_max": max(completed_counts),
        "completed_collar_count_average": sum(completed_counts) / len(completed_counts),
        "collar_class_rows": counter_rows(
            collar_class_counts, collar_class_edges, "collar_class", "packet_count"
        ),
        "block_class_rows": [
            {
                "collar_class": collar_class,
                "m_block_count": block_count,
                "packet_count": block_class_counts[(collar_class, block_count)],
                "edge_weight_sum": block_class_edges[(collar_class, block_count)],
            }
            for collar_class, block_count in sorted(block_class_counts, key=str)
        ],
        "q_prefix_bin_rows": counter_rows(q_bin_counts, q_bin_edges, "q_prefix_bin", "packet_count"),
        "left_collar_bin_rows": counter_rows(
            left_bin_counts, left_bin_edges, "left_collar_bin", "packet_count"
        ),
        "right_collar_bin_rows": counter_rows(
            right_bin_counts, right_bin_edges, "right_collar_bin", "packet_count"
        ),
        "completed_collar_bin_rows": counter_rows(
            completed_bin_counts,
            completed_bin_edges,
            "completed_collar_bin",
            "packet_count",
        ),
        "bad_packet_samples": bad_packet_samples,
        "sample_packets": sample_packets,
        "right_tail_endpoint_collar_flux_identity_closed": identity_verified,
        "right_tail_endpoint_collar_phase_saving_closed": False,
        "single_block_packet_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_packet_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_endpoint_collar_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "right_tail_punctured_interval_differences_split_into_endpoint_collars_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the interval-completion audit left punctured interval differences; the next acyclic step is to split each difference into endpoint collar flux packets",
        "current_object": {
            "input": "2107 right-tail shell-step packets carrying 86751 edges",
            "identity": "each right-tail shell is a left collar, right collar, two endpoint collars, or terminal full interval, minus optional P",
            "remaining": "phase saving on endpoint collar flux with moving q denominator",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RightTailPuncturedIntervalImported",
                True,
                True,
                "Right-tail fibres are inherited as P-punctured prime intervals.",
                "none for support import",
            ),
            gate(
                "RightTailEndpointCollarFluxIdentity",
                finite_audit["right_tail_endpoint_collar_flux_identity_closed"],
                finite_audit["right_tail_endpoint_collar_flux_identity_closed"],
                "Every right-tail shell-step packet is an endpoint collar flux minus optional P.",
                "none for finite endpoint-collar support",
            ),
            gate(
                "RightTailEndpointCollarPhaseSaving",
                False,
                False,
                "Prove cancellation on left/right/terminal endpoint collar flux packets.",
                "new completed trace or unbalanced endpoint estimate required",
            ),
            gate(
                "MovingPrimeQDenominatorCompletion",
                False,
                False,
                "Complete the moving q denominator on endpoint collar packets.",
                "not supplied by the support ledger",
            ),
            gate(
                "NoLossPacketAggregation",
                False,
                False,
                "Aggregate endpoint collar phase savings over all shell-step packets without comparable loss.",
                "requires analytic summation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "endpoint collar support is explicit but no completed trace family is supplied",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "moving prime q denominators remain the central completion problem",
            "Pascadi_composite_Type_II": "short endpoint collar flux is not a direct long Type-II input",
            "Wright_unbalanced_Kloosterman": "q-long endpoint collars are the nearest unbalanced Kloosterman target after completion",
            "Li_short_interval_x_052": "short-interval prime existence does not imply fixed-row endpoint-collar reciprocal phase saving",
        },
        "latest_narrowest_mouth": [
            "RightTailEndpointCollarFluxPhaseSaving",
            "AND SingleBlockEndpointPacketSummationByParts",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnEndpointCollarsAndSingleBlockPackets",
            "AND NoLossAggregationAcross5106ShellStepPackets",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "right_tail_endpoint_collar_flux_identity_closed": finite_audit[
            "right_tail_endpoint_collar_flux_identity_closed"
        ],
        "right_tail_endpoint_collar_phase_saving_closed": False,
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
        "# Prime Matrix Phi-LPF right-tail endpoint collar 审计",
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
        "## 2. endpoint collar 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"packet_identity_inherited={str(audit['packet_identity_inherited']).lower()}",
        f"right_tail_packet_count={audit['right_tail_packet_count']}",
        f"right_tail_edge_count={audit['right_tail_edge_count']}",
        f"right_tail_single_block_packet_count={audit['right_tail_single_block_packet_count']}",
        f"right_tail_multi_block_packet_count={audit['right_tail_multi_block_packet_count']}",
        f"right_tail_endpoint_collar_identity_verified={str(audit['right_tail_endpoint_collar_identity_verified']).lower()}",
        f"bad_endpoint_collar_packet_count={audit['bad_endpoint_collar_packet_count']}",
        f"terminal_full_interval_packet_count={audit['terminal_full_interval_packet_count']}",
        f"two_sided_collar_packet_count={audit['two_sided_collar_packet_count']}",
        f"one_sided_collar_packet_count={audit['one_sided_collar_packet_count']}",
        f"p_punctured_packet_count={audit['p_punctured_packet_count']}",
        f"left_collar_count_min={audit['left_collar_count_min']}",
        f"left_collar_count_median={audit['left_collar_count_median']}",
        f"left_collar_count_max={audit['left_collar_count_max']}",
        f"right_collar_count_min={audit['right_collar_count_min']}",
        f"right_collar_count_median={audit['right_collar_count_median']}",
        f"right_collar_count_max={audit['right_collar_count_max']}",
        f"completed_collar_count_min={audit['completed_collar_count_min']}",
        f"completed_collar_count_median={audit['completed_collar_count_median']}",
        f"completed_collar_count_max={audit['completed_collar_count_max']}",
        f"right_tail_endpoint_collar_flux_identity_closed={str(audit['right_tail_endpoint_collar_flux_identity_closed']).lower()}",
        f"right_tail_endpoint_collar_phase_saving_closed={str(audit['right_tail_endpoint_collar_phase_saving_closed']).lower()}",
        "```",
        "",
        "collar class 分桶：",
        "",
        *markdown_table(
            audit["collar_class_rows"], ["collar_class", "packet_count", "edge_weight_sum"]
        ),
        "",
        "collar class x m-block 分桶：",
        "",
        *markdown_table(
            audit["block_class_rows"],
            ["collar_class", "m_block_count", "packet_count", "edge_weight_sum"],
        ),
        "",
        "q-prefix packet 分桶：",
        "",
        *markdown_table(
            audit["q_prefix_bin_rows"], ["q_prefix_bin", "packet_count", "edge_weight_sum"]
        ),
        "",
        "completed collar size 分桶：",
        "",
        *markdown_table(
            audit["completed_collar_bin_rows"],
            ["completed_collar_bin", "packet_count", "edge_weight_sum"],
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
        "结论：right-tail punctured interval difference 已经压成左右 endpoint collar flux 与 terminal full interval flux。",
        "multi-block 主要来自 two-sided collar，少数来自 P-punctured collar；没有其他支撑误差。",
        "剩余仍是 endpoint collar 相位节省与 moving q denominator completion。",
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
        f"right_tail_endpoint_collar_flux_identity_closed={str(payload['right_tail_endpoint_collar_flux_identity_closed']).lower()}",
        f"right_tail_endpoint_collar_phase_saving_closed={str(payload['right_tail_endpoint_collar_phase_saving_closed']).lower()}",
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
        "right_tail_endpoint_collar_flux_identity_closed="
        f"{payload['right_tail_endpoint_collar_flux_identity_closed']}"
    )
    print(
        "right_tail_endpoint_collar_phase_saving_closed="
        f"{payload['right_tail_endpoint_collar_phase_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
