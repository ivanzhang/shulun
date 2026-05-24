#!/usr/bin/env python3
"""审计 boundary endpoint-flux packets 的 q-prefix line atom 分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json

上一层把 5106 个 boundary shell-step packets 统一为 endpoint-flux packets。本层
继续原子化：每个 endpoint-flux packet 是若干固定 endpoint prime m 乘以一个
contiguous prime-q prefix。因此所有 boundary 边都拆成

    {m} x [q_start,q_end]_prime

line atoms。该分解不提供相位节省；它只把 endpoint-flux 相位门压成固定 m 的
prime-q prefix reciprocal orbit 相消问题。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_unification_audit as endpoint_flux  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_endpoint_collar_audit as collar  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit as shell_step  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-atom"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-audit.json",
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
        "role": "q-prefix line atoms are trace-shaped only after the moving denominator is completed",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "fixed-m q-prefix atoms still require a completed Kloosterman variable in q",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "one-dimensional q-prefix atoms are not direct composite Type-II rectangles",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman fractions are closest after the q-prefix atom phase is normalized",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not control q-prefix reciprocal orbit phases",
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
    count_name: str = "atom_count",
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


def atom_profile(
    packet_index: int,
    packet: dict[str, Any],
    profile: dict[str, Any],
    m_value: int,
    primes: list[int],
) -> dict[str, Any]:
    """构造一个固定 m 的 q-prefix line atom。"""
    q_values = [q for q in primes if packet["q_start"] <= q <= packet["q_end"]]
    q_prefix_contiguous = len(q_values) == packet["q_prefix_count"]
    return {
        "packet_index": packet_index,
        "P": packet["P"],
        "strip": packet["strip"],
        "endpoint_flux_class": profile["endpoint_flux_class"],
        "m": m_value,
        "q_start": packet["q_start"],
        "q_end": packet["q_end"],
        "q_prefix_count": packet["q_prefix_count"],
        "edge_count": packet["q_prefix_count"],
        "q_prefix_contiguous": q_prefix_contiguous,
        "q_prefix_sample": q_values[:6],
    }


def endpoint_profile_for_packet(
    packet: dict[str, Any],
    fibres_by_row: dict[int, list[tuple[int, set[int]]]],
    primes: list[int],
) -> dict[str, Any]:
    """复用上一层 endpoint-flux profile。"""
    if packet["strip"] in {"lower_wing", "upper_wing"}:
        return endpoint_flux.single_endpoint_profile(packet, primes)
    if packet["strip"] == "right_tail":
        return endpoint_flux.right_tail_profile(packet, fibres_by_row, primes)
    raise AssertionError(f"unknown strip: {packet['strip']}")


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 q-prefix line atom 分解。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = shell_step.packetize_rectangles(max_prime)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    fibres_by_row = collar.right_tail_fibres_by_row(max_prime, primes)

    atom_count_by_strip: Counter[str] = Counter()
    atom_edge_by_strip: Counter[str] = Counter()
    atom_count_by_class: Counter[str] = Counter()
    atom_edge_by_class: Counter[str] = Counter()
    atom_count_by_q_bin: Counter[str] = Counter()
    atom_edge_by_q_bin: Counter[str] = Counter()
    packet_support_counts: list[int] = []
    q_counts: list[int] = []
    atom_edges: set[tuple[int, int, int]] = set()
    duplicate_edge_count = 0
    bad_atom_samples: list[dict[str, Any]] = []
    sample_atoms: list[dict[str, Any]] = []

    for packet_index, packet in enumerate(packets):
        profile = endpoint_profile_for_packet(packet, fibres_by_row, primes)
        m_values = sorted(endpoint_flux.packet_shell_values(packet, primes))
        packet_support_counts.append(len(m_values))
        q_counts.append(packet["q_prefix_count"])
        for m_value in m_values:
            atom = atom_profile(packet_index, packet, profile, m_value, primes)
            atom_count_by_strip[packet["strip"]] += 1
            atom_edge_by_strip[packet["strip"]] += atom["edge_count"]
            atom_count_by_class[profile["endpoint_flux_class"]] += 1
            atom_edge_by_class[profile["endpoint_flux_class"]] += atom["edge_count"]
            qb = q_bin(packet["q_prefix_count"])
            atom_count_by_q_bin[qb] += 1
            atom_edge_by_q_bin[qb] += atom["edge_count"]

            if not atom["q_prefix_contiguous"] and len(bad_atom_samples) < 8:
                bad_atom_samples.append(atom)
            if len(sample_atoms) < 16 and (
                packet["strip"] != "right_tail"
                or packet["q_prefix_count"] >= 17
                or profile.get("p_puncture_count", 0)
            ):
                sample_atoms.append(atom)

            q_values = [q for q in primes if packet["q_start"] <= q <= packet["q_end"]]
            for q in q_values:
                edge = (packet["P"], q, m_value)
                if edge in atom_edges:
                    duplicate_edge_count += 1
                atom_edges.add(edge)

    atom_count_total = sum(atom_count_by_strip.values())
    atom_edge_count_total = sum(atom_edge_by_strip.values())
    identity_verified = (
        atom_edge_count_total == previous_audit["boundary_endpoint_flux_edge_count"]
        and len(atom_edges) == atom_edge_count_total
        and duplicate_edge_count == 0
        and not bad_atom_samples
    )

    return {
        "max_prime": max_prime,
        "shell_step_packet_count_total": len(packets),
        "previous_boundary_endpoint_flux_packet_count": previous_audit[
            "boundary_endpoint_flux_packet_count"
        ],
        "previous_boundary_endpoint_flux_edge_count": previous_audit[
            "boundary_endpoint_flux_edge_count"
        ],
        "qprefix_line_atom_count_total": atom_count_total,
        "qprefix_line_atom_edge_count_total": atom_edge_count_total,
        "expanded_edge_set_size": len(atom_edges),
        "duplicate_atom_edge_count": duplicate_edge_count,
        "qprefix_line_atom_identity_verified": identity_verified,
        "bad_qprefix_atom_count": len(bad_atom_samples),
        "packet_support_count_min": min(packet_support_counts),
        "packet_support_count_median": statistics.median(packet_support_counts),
        "packet_support_count_max": max(packet_support_counts),
        "packet_support_count_average": sum(packet_support_counts) / len(packet_support_counts),
        "q_prefix_count_min": min(q_counts),
        "q_prefix_count_median": statistics.median(q_counts),
        "q_prefix_count_max": max(q_counts),
        "q_prefix_count_average": sum(q_counts) / len(q_counts),
        "atom_count_by_strip_rows": counter_rows(
            atom_count_by_strip, atom_edge_by_strip, "strip", "atom_count"
        ),
        "atom_count_by_endpoint_flux_class_rows": counter_rows(
            atom_count_by_class,
            atom_edge_by_class,
            "endpoint_flux_class",
            "atom_count",
        ),
        "atom_count_by_q_prefix_bin_rows": counter_rows(
            atom_count_by_q_bin,
            atom_edge_by_q_bin,
            "q_prefix_bin",
            "atom_count",
        ),
        "bad_atom_samples": bad_atom_samples,
        "sample_atoms": sample_atoms,
        "qprefix_line_atomization_closed": identity_verified,
        "qprefix_line_atom_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_qprefix_atom_aggregation_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "boundary_endpoint_flux_split_into_qprefix_line_atoms_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after endpoint-flux unification, the next acyclic support step is to split every endpoint packet into fixed-m q-prefix line atoms",
        "current_object": {
            "input": "5106 boundary endpoint-flux packets carrying 177515 edges",
            "identity": "each endpoint-flux packet is a disjoint union of {m} x contiguous prime-q prefix line atoms",
            "remaining": "phase saving on fixed-m prime-q prefix reciprocal orbits and no-loss aggregation",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "BoundaryEndpointFluxImported",
                True,
                True,
                "The unified endpoint-flux packet ledger is inherited.",
                "none for support import",
            ),
            gate(
                "QPrefixContiguousPrimeIntervalIdentity",
                finite_audit["bad_qprefix_atom_count"] == 0,
                finite_audit["bad_qprefix_atom_count"] == 0,
                "Every atom uses a contiguous prime-q prefix interval.",
                "none for finite q-prefix support",
            ),
            gate(
                "EndpointFluxQPrefixLineAtomization",
                finite_audit["qprefix_line_atomization_closed"],
                finite_audit["qprefix_line_atomization_closed"],
                "All endpoint-flux edges expand disjointly into fixed-m q-prefix line atoms.",
                "none for finite atom support",
            ),
            gate(
                "QPrefixLineAtomPhaseSaving",
                False,
                False,
                "Prove cancellation on fixed-m prime-q prefix reciprocal orbits.",
                "new completed trace or reciprocal-orbit estimate required",
            ),
            gate(
                "NoLossQPrefixAtomAggregation",
                False,
                False,
                "Aggregate q-prefix atom phase savings without losing the endpoint-flux gain.",
                "requires analytic aggregation discipline",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "q-prefix atoms are explicit but still need completed moving-denominator trace normalization",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "arbitrary-modulus estimates do not start until the atom denominator is a valid Kloosterman variable",
            "Pascadi_composite_Type_II": "line atoms are one-dimensional q-prefix objects, not Type-II rectangles",
            "Wright_unbalanced_Kloosterman": "unbalanced estimates become plausible only after q-prefix reciprocal-orbit normalization",
            "Li_short_interval_x_052": "prime existence in short intervals does not supply reciprocal q-prefix phase cancellation",
        },
        "latest_narrowest_mouth": [
            "QPrefixLineAtomReciprocalOrbitPhaseSaving",
            "AND MovingPrimeQDenominatorCompletedTraceFamilyOnFixedMAtoms",
            "AND NoLossAggregationAcross15439QPrefixLineAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "qprefix_line_atomization_closed": finite_audit["qprefix_line_atomization_closed"],
        "qprefix_line_atom_phase_saving_closed": False,
        "moving_q_denominator_completed_trace_closed": False,
        "no_loss_qprefix_atom_aggregation_closed": False,
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
        "# Prime Matrix Phi-LPF boundary endpoint-flux q-prefix atom 审计",
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
        "## 2. q-prefix line atom 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"shell_step_packet_count_total={audit['shell_step_packet_count_total']}",
        f"previous_boundary_endpoint_flux_packet_count={audit['previous_boundary_endpoint_flux_packet_count']}",
        f"previous_boundary_endpoint_flux_edge_count={audit['previous_boundary_endpoint_flux_edge_count']}",
        f"qprefix_line_atom_count_total={audit['qprefix_line_atom_count_total']}",
        f"qprefix_line_atom_edge_count_total={audit['qprefix_line_atom_edge_count_total']}",
        f"expanded_edge_set_size={audit['expanded_edge_set_size']}",
        f"duplicate_atom_edge_count={audit['duplicate_atom_edge_count']}",
        f"qprefix_line_atom_identity_verified={str(audit['qprefix_line_atom_identity_verified']).lower()}",
        f"bad_qprefix_atom_count={audit['bad_qprefix_atom_count']}",
        f"packet_support_count_min={audit['packet_support_count_min']}",
        f"packet_support_count_median={audit['packet_support_count_median']}",
        f"packet_support_count_max={audit['packet_support_count_max']}",
        f"q_prefix_count_min={audit['q_prefix_count_min']}",
        f"q_prefix_count_median={audit['q_prefix_count_median']}",
        f"q_prefix_count_max={audit['q_prefix_count_max']}",
        f"qprefix_line_atomization_closed={str(audit['qprefix_line_atomization_closed']).lower()}",
        f"qprefix_line_atom_phase_saving_closed={str(audit['qprefix_line_atom_phase_saving_closed']).lower()}",
        "```",
        "",
        "atom strip 分桶：",
        "",
        *markdown_table(audit["atom_count_by_strip_rows"], ["strip", "atom_count", "edge_weight_sum"]),
        "",
        "atom endpoint-flux class 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_endpoint_flux_class_rows"],
            ["endpoint_flux_class", "atom_count", "edge_weight_sum"],
        ),
        "",
        "atom q-prefix 分桶：",
        "",
        *markdown_table(
            audit["atom_count_by_q_prefix_bin_rows"],
            ["q_prefix_bin", "atom_count", "edge_weight_sum"],
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
        "结论：boundary endpoint-flux 已无重叠展开为固定 m 的 q-prefix line atoms。",
        "该层关闭的是支撑原子化，不关闭 q-prefix reciprocal orbit 的相位节省。",
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
        f"qprefix_line_atomization_closed={str(payload['qprefix_line_atomization_closed']).lower()}",
        f"qprefix_line_atom_phase_saving_closed={str(payload['qprefix_line_atom_phase_saving_closed']).lower()}",
        f"moving_q_denominator_completed_trace_closed={str(payload['moving_q_denominator_completed_trace_closed']).lower()}",
        f"no_loss_qprefix_atom_aggregation_closed={str(payload['no_loss_qprefix_atom_aggregation_closed']).lower()}",
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
    print(f"qprefix_line_atomization_closed={payload['qprefix_line_atomization_closed']}")
    print(f"qprefix_line_atom_phase_saving_closed={payload['qprefix_line_atom_phase_saving_closed']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
