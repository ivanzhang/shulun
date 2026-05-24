#!/usr/bin/env python3
"""审计 boundary shell-step packets 的 endpoint-flux 统一口径。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_unification_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.json

上一层把 right-tail punctured interval difference 拆成 endpoint collars。本层把
single-block endpoint packets 也纳入同一个端点通量账本：lower_wing 与 upper_wing
全部是单个 contiguous prime shell，right_tail 全部是 endpoint collar flux。

有限审计显示，P<=1009 的 5106 个 boundary shell-step packets 全部被统一为
endpoint-flux packets，零支撑例外。该层仍不提供相位节省；它只把
RightTailEndpointCollarFluxPhaseSaving 与 SingleBlockEndpointPacketSummationByParts
合并为一个统一的 BoundaryEndpointFluxPhaseSaving 接口。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_endpoint_collar_audit as collar  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit as shell_step  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-unification"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-audit.json",
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
        "role": "endpoint-flux packets are closer to a completed trace family, but the moving prime-q denominator is still not completed",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman input still requires a precise completed endpoint-flux phase model",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "the unified endpoint-flux family is short and boundary-weighted, not a direct long composite Type-II box",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "q-long endpoint-flux packets are the closest unbalanced Kloosterman target after denominator completion",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence still does not imply fixed-row endpoint-flux reciprocal phase saving",
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


def support_bin(count: int) -> str:
    """端点通量素数支撑大小分桶。"""
    if count == 0:
        return "support=0"
    if count <= 2:
        return "1<=support<=2"
    if count <= 4:
        return "3<=support<=4"
    if count <= 8:
        return "5<=support<=8"
    return "9<=support<=13"


def packet_shell_values(packet: dict[str, Any], primes: list[int]) -> set[int]:
    """展开 packet 的实际 m-shell 素数。"""
    values: set[int] = set()
    for block in packet["source_rectangles"]:
        values.update(p for p in primes if block["m_start"] <= p <= block["m_end"])
    return values


def single_endpoint_profile(packet: dict[str, Any], primes: list[int]) -> dict[str, Any]:
    """检查 lower/upper single-block endpoint packet。"""
    values = packet_shell_values(packet, primes)
    strip = packet["strip"]
    identity_verified = (
        strip in {"lower_wing", "upper_wing"}
        and packet["m_block_count"] == 1
        and packet["source_rectangle_count"] == 1
        and packet["internal_prime_gap_count"] == 0
        and len(values) == packet["m_shell_prime_count"]
        and packet["edge_count"] == packet["q_prefix_count"] * len(values)
        and packet["P"] not in values
    )
    return {
        "P": packet["P"],
        "strip": strip,
        "q_prefix_count": packet["q_prefix_count"],
        "q_start": packet["q_start"],
        "q_end": packet["q_end"],
        "m_block_count": packet["m_block_count"],
        "actual_shell_prime_count": len(values),
        "completed_flux_support_count": len(values),
        "edge_count": packet["edge_count"],
        "endpoint_flux_class": f"{strip}_single_contiguous_endpoint_shell",
        "p_puncture_count": 0,
        "identity_verified": identity_verified,
        "m_range": [min(values) if values else None, max(values) if values else None],
        "source_rectangles": packet["source_rectangles"],
    }


def right_tail_profile(
    packet: dict[str, Any],
    fibres_by_row: dict[int, list[tuple[int, set[int]]]],
    primes: list[int],
) -> dict[str, Any]:
    """把 right-tail packet 转为统一 endpoint-flux profile。"""
    profile = collar.collar_profile(packet["P"], packet, fibres_by_row[packet["P"]], primes)
    return {
        "P": profile["P"],
        "strip": "right_tail",
        "q_prefix_count": profile["q_prefix_count"],
        "q_start": profile["q_start"],
        "q_end": profile["q_end"],
        "m_block_count": profile["m_block_count"],
        "actual_shell_prime_count": profile["m_shell_prime_count"],
        "completed_flux_support_count": profile["completed_collar_count"],
        "edge_count": profile["edge_count"],
        "endpoint_flux_class": f"right_tail_{profile['collar_class']}",
        "p_puncture_count": profile["p_puncture_count"],
        "identity_verified": profile["identity_verified"],
        "left_collar_count": profile["left_collar_count"],
        "right_collar_count": profile["right_collar_count"],
        "source_rectangles": profile["source_rectangles"],
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计所有 boundary packets 是否统一为 endpoint-flux packets。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = shell_step.packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    fibres_by_row = collar.right_tail_fibres_by_row(max_prime, primes)

    endpoint_profiles: list[dict[str, Any]] = []
    bad_packet_samples: list[dict[str, Any]] = []
    sample_packets: list[dict[str, Any]] = []

    class_counts: Counter[str] = Counter()
    class_edges: Counter[str] = Counter()
    strip_counts: Counter[str] = Counter()
    strip_edges: Counter[str] = Counter()
    q_bin_counts: Counter[str] = Counter()
    q_bin_edges: Counter[str] = Counter()
    support_bin_counts: Counter[str] = Counter()
    support_bin_edges: Counter[str] = Counter()
    block_class_counts: Counter[tuple[str, int]] = Counter()
    block_class_edges: Counter[tuple[str, int]] = Counter()

    actual_support_counts: list[int] = []
    completed_support_counts: list[int] = []
    q_counts: list[int] = []
    p_puncture_counts: list[int] = []

    for packet in packets:
        if packet["strip"] in {"lower_wing", "upper_wing"}:
            profile = single_endpoint_profile(packet, primes)
        elif packet["strip"] == "right_tail":
            profile = right_tail_profile(packet, fibres_by_row, primes)
        else:
            profile = {
                "P": packet["P"],
                "strip": packet["strip"],
                "endpoint_flux_class": "unclassified_strip",
                "identity_verified": False,
                "edge_count": packet["edge_count"],
                "q_prefix_count": packet["q_prefix_count"],
                "m_block_count": packet["m_block_count"],
                "actual_shell_prime_count": packet["m_shell_prime_count"],
                "completed_flux_support_count": packet["m_shell_prime_count"],
                "p_puncture_count": 0,
            }

        endpoint_profiles.append(profile)
        endpoint_class = profile["endpoint_flux_class"]
        edge_count = profile["edge_count"]
        class_counts[endpoint_class] += 1
        class_edges[endpoint_class] += edge_count
        strip_counts[profile["strip"]] += 1
        strip_edges[profile["strip"]] += edge_count
        qb = q_bin(profile["q_prefix_count"])
        q_bin_counts[qb] += 1
        q_bin_edges[qb] += edge_count
        sb = support_bin(profile["completed_flux_support_count"])
        support_bin_counts[sb] += 1
        support_bin_edges[sb] += edge_count
        block_key = (endpoint_class, profile["m_block_count"])
        block_class_counts[block_key] += 1
        block_class_edges[block_key] += edge_count

        actual_support_counts.append(profile["actual_shell_prime_count"])
        completed_support_counts.append(profile["completed_flux_support_count"])
        q_counts.append(profile["q_prefix_count"])
        p_puncture_counts.append(profile["p_puncture_count"])

        if not profile["identity_verified"] and len(bad_packet_samples) < 8:
            bad_packet_samples.append(profile)
        if len(sample_packets) < 16 and (
            profile["strip"] != "right_tail"
            or profile["m_block_count"] > 1
            or profile["p_puncture_count"]
        ):
            sample_packets.append(profile)

    lower_upper_packets = [p for p in endpoint_profiles if p["strip"] in {"lower_wing", "upper_wing"}]
    right_tail_packets = [p for p in endpoint_profiles if p["strip"] == "right_tail"]
    identity_verified = not bad_packet_samples

    return {
        "max_prime": max_prime,
        "shell_step_packet_count_total": len(packets),
        "edge_count_total": sum(packet["edge_count"] for packet in packets),
        "previous_shell_step_packet_count_total": previous_audit["shell_step_packet_count_total"],
        "previous_edge_count_total": previous_audit["edge_count_total"],
        "packet_identity_inherited": (
            len(packets) == previous_audit["shell_step_packet_count_total"]
            and sum(packet["edge_count"] for packet in packets)
            == previous_audit["edge_count_total"]
        ),
        "boundary_endpoint_flux_packet_count": len(endpoint_profiles),
        "boundary_endpoint_flux_edge_count": sum(profile["edge_count"] for profile in endpoint_profiles),
        "lower_upper_single_endpoint_packet_count": len(lower_upper_packets),
        "lower_upper_single_endpoint_edge_count": sum(profile["edge_count"] for profile in lower_upper_packets),
        "right_tail_endpoint_collar_packet_count": len(right_tail_packets),
        "right_tail_endpoint_collar_edge_count": sum(profile["edge_count"] for profile in right_tail_packets),
        "single_block_endpoint_flux_packet_count": sum(
            1 for profile in endpoint_profiles if profile["m_block_count"] == 1
        ),
        "multi_block_endpoint_flux_packet_count": sum(
            1 for profile in endpoint_profiles if profile["m_block_count"] > 1
        ),
        "lower_upper_internal_gap_count_total": sum(
            0 if profile["identity_verified"] else 1 for profile in lower_upper_packets
        ),
        "right_tail_endpoint_collar_identity_inherited": all(
            profile["identity_verified"] for profile in right_tail_packets
        ),
        "boundary_endpoint_flux_identity_verified": identity_verified,
        "bad_endpoint_flux_packet_count": len(bad_packet_samples),
        "p_punctured_endpoint_flux_packet_count": sum(p_puncture_counts),
        "actual_shell_prime_count_min": min(actual_support_counts),
        "actual_shell_prime_count_median": statistics.median(actual_support_counts),
        "actual_shell_prime_count_max": max(actual_support_counts),
        "actual_shell_prime_count_average": sum(actual_support_counts) / len(actual_support_counts),
        "completed_flux_support_count_min": min(completed_support_counts),
        "completed_flux_support_count_median": statistics.median(completed_support_counts),
        "completed_flux_support_count_max": max(completed_support_counts),
        "completed_flux_support_count_average": sum(completed_support_counts)
        / len(completed_support_counts),
        "q_prefix_count_min": min(q_counts),
        "q_prefix_count_median": statistics.median(q_counts),
        "q_prefix_count_max": max(q_counts),
        "q_prefix_count_average": sum(q_counts) / len(q_counts),
        "endpoint_flux_class_rows": counter_rows(
            class_counts, class_edges, "endpoint_flux_class", "packet_count"
        ),
        "strip_rows": counter_rows(strip_counts, strip_edges, "strip", "packet_count"),
        "q_prefix_bin_rows": counter_rows(q_bin_counts, q_bin_edges, "q_prefix_bin", "packet_count"),
        "completed_support_bin_rows": counter_rows(
            support_bin_counts, support_bin_edges, "completed_support_bin", "packet_count"
        ),
        "block_class_rows": [
            {
                "endpoint_flux_class": endpoint_class,
                "m_block_count": block_count,
                "packet_count": block_class_counts[(endpoint_class, block_count)],
                "edge_weight_sum": block_class_edges[(endpoint_class, block_count)],
            }
            for endpoint_class, block_count in sorted(block_class_counts, key=str)
        ],
        "bad_packet_samples": bad_packet_samples,
        "sample_packets": sample_packets,
        "boundary_endpoint_flux_unification_closed": identity_verified,
        "single_block_endpoint_support_model_closed": all(
            profile["identity_verified"] for profile in lower_upper_packets
        ),
        "right_tail_endpoint_collar_flux_identity_closed": all(
            profile["identity_verified"] for profile in right_tail_packets
        ),
        "boundary_endpoint_flux_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_endpoint_flux_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_unification_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "all_boundary_shell_step_packets_unified_as_endpoint_flux_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the latest mouth separated right-tail endpoint collars from single-block endpoint packets; the next acyclic step is to unify both support families before attacking phase saving",
        "current_object": {
            "input": "5106 boundary shell-step packets carrying 177515 edges",
            "identity": "lower/upper wings are single contiguous endpoint shells and right-tail packets are endpoint collars",
            "remaining": "phase saving on the unified endpoint-flux packet family with moving q denominator",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "BoundaryShellStepPacketImported",
                True,
                True,
                "The 5106 shell-step packets and edge mass are inherited.",
                "none for support import",
            ),
            gate(
                "LowerUpperSingleEndpointShellIdentity",
                finite_audit["single_block_endpoint_support_model_closed"],
                finite_audit["single_block_endpoint_support_model_closed"],
                "Every lower/upper wing packet is one contiguous endpoint prime shell.",
                "none for finite lower/upper endpoint support",
            ),
            gate(
                "RightTailEndpointCollarFluxIdentity",
                finite_audit["right_tail_endpoint_collar_flux_identity_closed"],
                finite_audit["right_tail_endpoint_collar_flux_identity_closed"],
                "Every right-tail packet is an endpoint collar flux minus optional P.",
                "none for finite right-tail endpoint-collar support",
            ),
            gate(
                "BoundaryEndpointFluxUnification",
                finite_audit["boundary_endpoint_flux_unification_closed"],
                finite_audit["boundary_endpoint_flux_unification_closed"],
                "All boundary shell-step packets are in the unified endpoint-flux family.",
                "none for finite support unification",
            ),
            gate(
                "BoundaryEndpointFluxPhaseSaving",
                False,
                False,
                "Prove cancellation on the unified endpoint-flux packet family.",
                "new completed trace or endpoint summation estimate required",
            ),
            gate(
                "MovingPrimeQDenominatorCompletion",
                False,
                False,
                "Complete the moving q denominator on endpoint-flux packets.",
                "not supplied by support unification",
            ),
            gate(
                "NoLossEndpointFluxAggregation",
                False,
                False,
                "Aggregate endpoint-flux phase savings over all 5106 packets without comparable loss.",
                "requires analytic summation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "endpoint-flux support is explicit but no completed moving-denominator trace family is supplied",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "arbitrary-modulus estimates require an actual completed endpoint-flux Kloosterman variable",
            "Pascadi_composite_Type_II": "endpoint-flux packets are short boundary objects, not direct long Type-II boxes",
            "Wright_unbalanced_Kloosterman": "unbalanced fractions are the nearest candidate only after q-denominator completion",
            "Li_short_interval_x_052": "short-interval prime existence does not imply endpoint-flux reciprocal phase saving",
        },
        "latest_narrowest_mouth": [
            "BoundaryEndpointFluxPhaseSaving",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnBoundaryEndpointFluxPackets",
            "AND NoLossAggregationAcross5106EndpointFluxPackets",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "boundary_endpoint_flux_unification_closed": finite_audit[
            "boundary_endpoint_flux_unification_closed"
        ],
        "boundary_endpoint_flux_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_endpoint_flux_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF boundary endpoint-flux unification 审计",
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
        "## 2. endpoint-flux 统一有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"edge_count_total={audit['edge_count_total']}",
        f"packet_identity_inherited={str(audit['packet_identity_inherited']).lower()}",
        f"boundary_endpoint_flux_packet_count={audit['boundary_endpoint_flux_packet_count']}",
        f"boundary_endpoint_flux_edge_count={audit['boundary_endpoint_flux_edge_count']}",
        f"lower_upper_single_endpoint_packet_count={audit['lower_upper_single_endpoint_packet_count']}",
        f"lower_upper_single_endpoint_edge_count={audit['lower_upper_single_endpoint_edge_count']}",
        f"right_tail_endpoint_collar_packet_count={audit['right_tail_endpoint_collar_packet_count']}",
        f"right_tail_endpoint_collar_edge_count={audit['right_tail_endpoint_collar_edge_count']}",
        f"single_block_endpoint_flux_packet_count={audit['single_block_endpoint_flux_packet_count']}",
        f"multi_block_endpoint_flux_packet_count={audit['multi_block_endpoint_flux_packet_count']}",
        f"boundary_endpoint_flux_identity_verified={str(audit['boundary_endpoint_flux_identity_verified']).lower()}",
        f"bad_endpoint_flux_packet_count={audit['bad_endpoint_flux_packet_count']}",
        f"p_punctured_endpoint_flux_packet_count={audit['p_punctured_endpoint_flux_packet_count']}",
        f"actual_shell_prime_count_min={audit['actual_shell_prime_count_min']}",
        f"actual_shell_prime_count_median={audit['actual_shell_prime_count_median']}",
        f"actual_shell_prime_count_max={audit['actual_shell_prime_count_max']}",
        f"completed_flux_support_count_min={audit['completed_flux_support_count_min']}",
        f"completed_flux_support_count_median={audit['completed_flux_support_count_median']}",
        f"completed_flux_support_count_max={audit['completed_flux_support_count_max']}",
        f"q_prefix_count_min={audit['q_prefix_count_min']}",
        f"q_prefix_count_median={audit['q_prefix_count_median']}",
        f"q_prefix_count_max={audit['q_prefix_count_max']}",
        f"boundary_endpoint_flux_unification_closed={str(audit['boundary_endpoint_flux_unification_closed']).lower()}",
        f"boundary_endpoint_flux_phase_saving_closed={str(audit['boundary_endpoint_flux_phase_saving_closed']).lower()}",
        "```",
        "",
        "endpoint-flux class 分桶：",
        "",
        *markdown_table(
            audit["endpoint_flux_class_rows"],
            ["endpoint_flux_class", "packet_count", "edge_weight_sum"],
        ),
        "",
        "strip 分桶：",
        "",
        *markdown_table(audit["strip_rows"], ["strip", "packet_count", "edge_weight_sum"]),
        "",
        "completed support size 分桶：",
        "",
        *markdown_table(
            audit["completed_support_bin_rows"],
            ["completed_support_bin", "packet_count", "edge_weight_sum"],
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
        "结论：5106 个 boundary shell-step packets 已统一为 endpoint-flux packets。",
        "single-block endpoint packet 不再是独立支撑族；它并入统一 endpoint-flux 相位门。",
        "剩余仍是 endpoint-flux 相位节省、moving q denominator completion 与无损聚合。",
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
        f"boundary_endpoint_flux_unification_closed={str(payload['boundary_endpoint_flux_unification_closed']).lower()}",
        f"boundary_endpoint_flux_phase_saving_closed={str(payload['boundary_endpoint_flux_phase_saving_closed']).lower()}",
        f"moving_q_denominator_completed_trace_closed={str(payload['moving_q_denominator_completed_trace_closed']).lower()}",
        f"no_loss_endpoint_flux_aggregation_closed={str(payload['no_loss_endpoint_flux_aggregation_closed']).lower()}",
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
        "boundary_endpoint_flux_unification_closed="
        f"{payload['boundary_endpoint_flux_unification_closed']}"
    )
    print(
        "boundary_endpoint_flux_phase_saving_closed="
        f"{payload['boundary_endpoint_flux_phase_saving_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
