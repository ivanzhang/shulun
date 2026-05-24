#!/usr/bin/env python3
"""审计 signed-child mirror-imbalance 的支撑账本。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_mirror_imbalance_support_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support-audit.json

上一层证明：同 raw-base 内的 A-step 符号镜像只能配平一部分 signed-child
edge mass。本层继续非循环下钻，把剩余 mirror-imbalance edge mass 拆成
missing-mirror 与 unequal-mirror-pair 两类，并登记其 P/strip/endpoint 支撑。

该层只关闭有限支撑账本；它不证明这些 residual carriers 存在相位节省。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_audit as signature  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit as mirror  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit as carrier  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

MIRROR_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-audit.json"
)

DEPENDENCIES = [
    MIRROR_AUDIT,
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-audit.json",
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-audit.json",
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
        "role": "candidate only after missing/unequal mirror carriers become trace-function sums",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "candidate only after residual carriers are completed to Kloosterman variables",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "requires Type-II boxes; this ledger exposes residual signed-child support only",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "candidate after the residual support is converted to admissible unbalanced fractions",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not estimate mirror-imbalance phase",
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


def profile_string(counts: Counter[str]) -> str:
    """把分类计数器转为稳定字符串。"""
    return ",".join(f"{key}:{counts[key]}" for key in sorted(counts))


def support_summary(
    residual_edge_mass: Counter[str],
    template_p_sets: dict[str, set[int]],
    template_strip_counts: dict[str, Counter[str]],
) -> dict[str, Any]:
    """汇总 residual carrier 的支撑宽度。

    residual mass 按 mirror-pair 的较重 signed child 归属；P/strip 支撑是该
    child 在原 signed-cycle 账本中的承载支撑，因此是确定的有限支撑账本。
    """
    p_widths = [len(template_p_sets[key]) for key in residual_edge_mass]
    strip_widths = [len(template_strip_counts[key]) for key in residual_edge_mass]
    total = sum(residual_edge_mass.values())
    multi_p_edge_mass = sum(
        residual_edge_mass[key] for key in residual_edge_mass if len(template_p_sets[key]) > 1
    )
    multi_strip_edge_mass = sum(
        residual_edge_mass[key]
        for key in residual_edge_mass
        if len(template_strip_counts[key]) > 1
    )
    return {
        "residual_carrier_count": len(residual_edge_mass),
        "multi_P_residual_carrier_count": sum(
            1 for key in residual_edge_mass if len(template_p_sets[key]) > 1
        ),
        "multi_P_residual_edge_mass": multi_p_edge_mass,
        "multi_P_residual_edge_ratio": multi_p_edge_mass / total,
        "multi_strip_residual_carrier_count": sum(
            1 for key in residual_edge_mass if len(template_strip_counts[key]) > 1
        ),
        "multi_strip_residual_edge_mass": multi_strip_edge_mass,
        "multi_strip_residual_edge_ratio": multi_strip_edge_mass / total,
        "P_support_width_min": min(p_widths),
        "P_support_width_median": statistics.median(p_widths),
        "P_support_width_max": max(p_widths),
        "strip_support_width_min": min(strip_widths),
        "strip_support_width_median": statistics.median(strip_widths),
        "strip_support_width_max": max(strip_widths),
    }


def top_residual_carrier_rows(
    residual_edge_mass: Counter[str],
    template_p_sets: dict[str, set[int]],
    template_strip_counts: dict[str, Counter[str]],
    template_endpoint_counts: dict[str, Counter[str]],
    template_a_class: dict[str, str],
    template_base: dict[str, str],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出 residual signed-child carrier 的最高质量行。"""
    rows = []
    order = sorted(residual_edge_mass, key=lambda key: (-residual_edge_mass[key], key))
    for key in order[:limit]:
        rows.append(
            {
                "signed_child": key,
                "raw_base_template": template_base[key],
                "residual_edge_mass": residual_edge_mass[key],
                "A_class": template_a_class[key],
                "distinct_P_count": len(template_p_sets[key]),
                "strip_edge_profile": profile_string(template_strip_counts[key]),
                "endpoint_edge_profile": profile_string(template_endpoint_counts[key]),
            }
        )
    return rows


def top_residual_base_rows(
    residual_base_edge_mass: Counter[str],
    raw_base_edge_mass: Counter[str],
    raw_base_child_edge_mass: dict[str, Counter[str]],
    residual_base_type_edge_mass: dict[str, Counter[str]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出 residual raw-base 的最高质量行。"""
    rows = []
    order = sorted(
        residual_base_edge_mass,
        key=lambda key: (-residual_base_edge_mass[key], -raw_base_edge_mass[key], key),
    )
    for key in order[:limit]:
        rows.append(
            {
                "raw_base_template": key,
                "residual_edge_mass": residual_base_edge_mass[key],
                "raw_base_signed_edge_mass": raw_base_edge_mass[key],
                "residual_share_inside_raw_base": residual_base_edge_mass[key]
                / raw_base_edge_mass[key],
                "signed_child_count": len(raw_base_child_edge_mass[key]),
                "residual_type_profile": profile_string(residual_base_type_edge_mass[key]),
            }
        )
    return rows


def top_pair_rows(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """输出 residual mirror-pair 的最高质量行。"""
    return sorted(
        rows,
        key=lambda row: (
            -row["residual_edge_mass"],
            -row["larger_child_edge_mass"],
            row["raw_base_template"],
            row["dominant_signed_child"],
        ),
    )[:limit]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 mirror-imbalance support。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(MIRROR_AUDIT.read_text())
    previous = previous_payload["finite_audit"]

    totals: Counter[str] = Counter()
    template_edge_mass: Counter[str] = Counter()
    template_cycle_count: Counter[str] = Counter()
    template_p_sets: dict[str, set[int]] = defaultdict(set)
    template_strip_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_endpoint_counts: dict[str, Counter[str]] = defaultdict(Counter)
    template_mirror: dict[str, str] = {}
    template_base: dict[str, str] = {}
    template_a_class: dict[str, str] = {}
    raw_base_edge_mass: Counter[str] = Counter()
    raw_base_child_edge_mass: dict[str, Counter[str]] = defaultdict(Counter)

    for packet_index, packet in enumerate(packets):
        endpoint_profile = flow.qprefix_atom.endpoint_profile_for_packet(packet, fibres_by_row, primes)
        q_values = flow.phase_normal.q_values_for_packet(packet, primes)
        m_values = sorted(flow.qprefix_atom.endpoint_flux.packet_shell_values(packet, primes))
        endpoint_class = endpoint_profile["endpoint_flux_class"]

        for m_value in m_values:
            _, transitions = flow.carry_dynamics.atom_transition_profile(
                packet_index, packet, endpoint_class, m_value, q_values
            )
            totals["atom_count_total"] += 1
            if len(transitions) < 2:
                totals["non_switch_atom_count"] += 1
                continue

            signed_seq: list[tuple[int, int, str]] = []
            for transition in transitions:
                signed_seq.append(
                    (
                        transition["q_gap"],
                        transition["carry_delta_k"],
                        flow.letter_run.sign_label(transition["A_step"]),
                    )
                )

            totals["switch_atom_count"] += 1
            totals["adjacent_letter_pair_count_inside_atoms"] += len(signed_seq) - 1
            signed_cycles, signed_stack = signature.loop_erased_cycle_packets(signed_seq)
            totals["signed_residual_edge_mass"] += max(0, len(signed_stack) - 1)

            for cycle in signed_cycles:
                template = signature.signed_template(cycle)
                base = signature.raw_template([(item[0], item[1]) for item in cycle])
                length = len(cycle)
                template_edge_mass[template] += length
                template_cycle_count[template] += 1
                template_p_sets[template].add(packet["P"])
                template_strip_counts[template][packet["strip"]] += length
                template_endpoint_counts[template][endpoint_class] += length
                template_mirror[template] = mirror.signed_mirror_template(cycle)
                template_base[template] = base
                template_a_class[template] = carrier.a_class(cycle)
                raw_base_edge_mass[base] += length
                raw_base_child_edge_mass[base][template] += length
                totals["signed_cycle_packet_count"] += 1
                totals["signed_cycle_edge_mass"] += length

    residual_edge_mass: Counter[str] = Counter()
    residual_type_edge_mass: Counter[str] = Counter()
    residual_type_pair_count: Counter[str] = Counter()
    residual_a_class_edge_mass: Counter[str] = Counter()
    residual_base_edge_mass: Counter[str] = Counter()
    residual_base_type_edge_mass: dict[str, Counter[str]] = defaultdict(Counter)
    pair_rows: list[dict[str, Any]] = []
    visited: set[str] = set()

    for template, mass in template_edge_mass.items():
        if template in visited:
            continue

        mirror_template = template_mirror[template]
        raw_base = template_base[template]
        mirror_mass = template_edge_mass.get(mirror_template, 0)

        if mirror_template == template:
            visited.add(template)
            continue

        if mirror_template not in template_edge_mass:
            residual_type = "missing_mirror"
            dominant = template
            minority = mirror_template
            residual = mass
            smaller_mass = 0
            larger_mass = mass
            visited.add(template)
        else:
            visited.add(template)
            visited.add(mirror_template)
            if mass == mirror_mass:
                continue
            residual_type = "unequal_mirror_pair"
            if mass > mirror_mass:
                dominant = template
                minority = mirror_template
                larger_mass = mass
                smaller_mass = mirror_mass
            else:
                dominant = mirror_template
                minority = template
                larger_mass = mirror_mass
                smaller_mass = mass
            residual = larger_mass - smaller_mass

        residual_edge_mass[dominant] += residual
        residual_type_edge_mass[residual_type] += residual
        residual_type_pair_count[residual_type] += 1
        residual_a_class_edge_mass[template_a_class[dominant]] += residual
        residual_base_edge_mass[raw_base] += residual
        residual_base_type_edge_mass[raw_base][residual_type] += residual
        pair_rows.append(
            {
                "residual_type": residual_type,
                "raw_base_template": raw_base,
                "dominant_signed_child": dominant,
                "minority_or_missing_child": minority,
                "larger_child_edge_mass": larger_mass,
                "smaller_or_missing_edge_mass": smaller_mass,
                "residual_edge_mass": residual,
                "dominant_A_class": template_a_class[dominant],
                "dominant_distinct_P_count": len(template_p_sets[dominant]),
                "dominant_strip_edge_profile": profile_string(template_strip_counts[dominant]),
                "dominant_endpoint_edge_profile": profile_string(
                    template_endpoint_counts[dominant]
                ),
            }
        )

    residual_total = sum(residual_edge_mass.values())
    residual_base_ratios = [
        residual_base_edge_mass[base] / raw_base_edge_mass[base] for base in residual_base_edge_mass
    ]
    support = support_summary(residual_edge_mass, template_p_sets, template_strip_counts)
    missing_edge_mass = residual_type_edge_mass["missing_mirror"]
    unequal_edge_mass = residual_type_edge_mass["unequal_mirror_pair"]

    ledger_closed = (
        previous["signed_child_mirror_reconciliation_ledger_closed"]
        and totals["atom_count_total"] == previous["atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and totals["signed_cycle_packet_count"] == previous["signed_cycle_packet_count"]
        and totals["signed_cycle_edge_mass"] == previous["signed_cycle_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and len(template_edge_mass) == previous["signed_cycle_signature_count"]
        and len(raw_base_edge_mass) == previous["raw_base_signed_refinement_count"]
        and residual_total == previous["mirror_imbalance_edge_mass"]
        and missing_edge_mass == previous["missing_mirror_edge_mass"]
        and residual_total + previous["mirror_balanced_edge_mass"]
        == previous["signed_cycle_edge_mass"]
    )

    return {
        "max_prime": max_prime,
        "previous_signed_child_mirror_reconciliation_ledger_closed": previous[
            "signed_child_mirror_reconciliation_ledger_closed"
        ],
        "mirror_imbalance_support_ledger_closed": ledger_closed,
        "atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "signed_cycle_packet_count": totals["signed_cycle_packet_count"],
        "signed_cycle_edge_mass": totals["signed_cycle_edge_mass"],
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "signed_cycle_signature_count": len(template_edge_mass),
        "raw_base_signed_refinement_count": len(raw_base_edge_mass),
        "mirror_balanced_edge_mass_imported": previous["mirror_balanced_edge_mass"],
        "mirror_imbalance_edge_mass": residual_total,
        "mirror_imbalance_edge_ratio": residual_total / totals["signed_cycle_edge_mass"],
        "missing_mirror_edge_mass": missing_edge_mass,
        "missing_mirror_within_imbalance_ratio": missing_edge_mass / residual_total,
        "unequal_mirror_pair_residual_edge_mass": unequal_edge_mass,
        "unequal_mirror_pair_within_imbalance_ratio": unequal_edge_mass / residual_total,
        "missing_mirror_pair_count": residual_type_pair_count["missing_mirror"],
        "unequal_mirror_pair_residual_count": residual_type_pair_count[
            "unequal_mirror_pair"
        ],
        "residual_raw_base_count": len(residual_base_edge_mass),
        "residual_raw_base_share_min": min(residual_base_ratios),
        "residual_raw_base_share_median": statistics.median(residual_base_ratios),
        "residual_raw_base_share_max": max(residual_base_ratios),
        "residual_carrier_support": support,
        "residual_type_edge_rows": [
            {
                "residual_type": key,
                "pair_count": residual_type_pair_count[key],
                "edge_mass": residual_type_edge_mass[key],
                "within_imbalance_ratio": residual_type_edge_mass[key] / residual_total,
            }
            for key in sorted(residual_type_edge_mass)
        ],
        "residual_A_class_edge_rows": [
            {
                "A_class": key,
                "edge_mass": residual_a_class_edge_mass[key],
                "within_imbalance_ratio": residual_a_class_edge_mass[key] / residual_total,
            }
            for key in sorted(residual_a_class_edge_mass)
        ],
        "top_residual_signed_child_carrier_rows": top_residual_carrier_rows(
            residual_edge_mass,
            template_p_sets,
            template_strip_counts,
            template_endpoint_counts,
            template_a_class,
            template_base,
        ),
        "top_residual_raw_base_rows": top_residual_base_rows(
            residual_base_edge_mass,
            raw_base_edge_mass,
            raw_base_child_edge_mass,
            residual_base_type_edge_mass,
        ),
        "top_residual_mirror_pair_rows": top_pair_rows(pair_rows),
        "signed_child_mirror_imbalance_phase_saving_closed": False,
        "missing_mirror_carrier_phase_saving_closed": False,
        "unequal_mirror_pair_residual_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_mirror_imbalance_support_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "mirror_imbalance_support_ledger_closed_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the previous signed-child mirror ledger leaves mirror-imbalance carriers as the narrowest direct hard point",
        "current_object": {
            "input": "mirror-imbalance signed-child carriers from the q-prefix carry cycle-signature ledger",
            "operation": "split residual mass into missing-mirror and unequal-mirror-pair carriers, with P/strip/endpoint support",
            "dominant_shape": "most imbalance is missing-mirror mass; unequal pairs form the smaller but still nonzero residual",
            "remaining": "phase saving for missing-mirror and unequal-pair residual carriers plus thin-support and completion losses",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SignedChildMirrorLedgerImported",
                finite_audit["previous_signed_child_mirror_reconciliation_ledger_closed"],
                finite_audit["previous_signed_child_mirror_reconciliation_ledger_closed"],
                "The previous signed-child mirror pairing ledger is imported.",
                "none for import",
            ),
            gate(
                "MirrorImbalanceSupportLedger",
                finite_audit["mirror_imbalance_support_ledger_closed"],
                finite_audit["mirror_imbalance_support_ledger_closed"],
                "Every mirror-imbalance edge is assigned to missing-mirror or unequal-mirror-pair support.",
                "none for the finite support ledger",
            ),
            gate(
                "MissingMirrorCarrierPhaseSaving",
                False,
                False,
                "Prove cancellation or a positive lower bound after the missing-mirror carriers are isolated.",
                "requires analytic phase input on carriers with no sign mirror",
            ),
            gate(
                "UnequalMirrorPairResidualPhaseSaving",
                False,
                False,
                "Prove cancellation for the residual after unequal mirror-pair cancellation.",
                "requires analytic phase input on the heavier signed-child side",
            ),
            gate(
                "TraceKloostermanCompletion",
                False,
                False,
                "Convert the isolated residual carriers to admissible trace/Kloosterman families.",
                "requires a new completion map and no-loss aggregation",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "candidate only after missing/unequal residual carriers become trace sums",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "candidate only after residual carriers expose bilinear Kloosterman variables",
            "Pascadi_composite_Type_II": "not directly matched to signed-child mirror-imbalance support",
            "Wright_unbalanced_Kloosterman": "candidate only after dominant-side residuals become admissible unbalanced fractions",
            "Li_short_interval_x_052": "does not estimate the mirror-imbalance support ledger",
        },
        "latest_narrowest_mouth": [
            "MissingMirrorCarrierPhaseSaving",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND TraceKloostermanCompletionOfMirrorImbalanceAndResidualPackets",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "mirror_imbalance_support_ledger_closed": finite_audit[
            "mirror_imbalance_support_ledger_closed"
        ],
        "signed_child_mirror_imbalance_phase_saving_closed": False,
        "missing_mirror_carrier_phase_saving_closed": False,
        "unequal_mirror_pair_residual_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def markdown_table(rows: list[dict[str, Any]], fields: list[str]) -> list[str]:
    """生成 Markdown 表格。"""
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
    support = audit["residual_carrier_support"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature mirror-imbalance support 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"input={current['input']}",
        f"operation={current['operation']}",
        f"dominant_shape={current['dominant_shape']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. mirror-imbalance support 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"mirror_imbalance_support_ledger_closed={str(audit['mirror_imbalance_support_ledger_closed']).lower()}",
        f"signed_cycle_edge_mass={audit['signed_cycle_edge_mass']}",
        f"mirror_balanced_edge_mass_imported={audit['mirror_balanced_edge_mass_imported']}",
        f"mirror_imbalance_edge_mass={audit['mirror_imbalance_edge_mass']}",
        f"mirror_imbalance_edge_ratio={audit['mirror_imbalance_edge_ratio']}",
        f"missing_mirror_edge_mass={audit['missing_mirror_edge_mass']}",
        f"missing_mirror_within_imbalance_ratio={audit['missing_mirror_within_imbalance_ratio']}",
        f"unequal_mirror_pair_residual_edge_mass={audit['unequal_mirror_pair_residual_edge_mass']}",
        f"unequal_mirror_pair_within_imbalance_ratio={audit['unequal_mirror_pair_within_imbalance_ratio']}",
        f"missing_mirror_pair_count={audit['missing_mirror_pair_count']}",
        f"unequal_mirror_pair_residual_count={audit['unequal_mirror_pair_residual_count']}",
        f"residual_raw_base_count={audit['residual_raw_base_count']}",
        f"residual_raw_base_share_min/median/max={audit['residual_raw_base_share_min']}/{audit['residual_raw_base_share_median']}/{audit['residual_raw_base_share_max']}",
        f"residual_carrier_count={support['residual_carrier_count']}",
        f"multi_P_residual_edge_ratio={support['multi_P_residual_edge_ratio']}",
        f"P_support_width_min/median/max={support['P_support_width_min']}/{support['P_support_width_median']}/{support['P_support_width_max']}",
        f"multi_strip_residual_edge_ratio={support['multi_strip_residual_edge_ratio']}",
        f"strip_support_width_min/median/max={support['strip_support_width_min']}/{support['strip_support_width_median']}/{support['strip_support_width_max']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "residual type edge mass：",
        "",
        *markdown_table(
            audit["residual_type_edge_rows"],
            ["residual_type", "pair_count", "edge_mass", "within_imbalance_ratio"],
        ),
        "",
        "residual A-class edge mass：",
        "",
        *markdown_table(
            audit["residual_A_class_edge_rows"],
            ["A_class", "edge_mass", "within_imbalance_ratio"],
        ),
        "",
        "最高 residual signed-child carriers：",
        "",
        *markdown_table(
            audit["top_residual_signed_child_carrier_rows"],
            [
                "signed_child",
                "raw_base_template",
                "residual_edge_mass",
                "A_class",
                "distinct_P_count",
                "strip_edge_profile",
                "endpoint_edge_profile",
            ],
        ),
        "",
        "最高 residual raw bases：",
        "",
        *markdown_table(
            audit["top_residual_raw_base_rows"],
            [
                "raw_base_template",
                "residual_edge_mass",
                "raw_base_signed_edge_mass",
                "residual_share_inside_raw_base",
                "signed_child_count",
                "residual_type_profile",
            ],
        ),
        "",
        "最高 residual mirror pairs：",
        "",
        *markdown_table(
            audit["top_residual_mirror_pair_rows"],
            [
                "residual_type",
                "raw_base_template",
                "dominant_signed_child",
                "minority_or_missing_child",
                "larger_child_edge_mass",
                "smaller_or_missing_edge_mass",
                "residual_edge_mass",
                "dominant_distinct_P_count",
            ],
        ),
        "",
        "## 3. 门控表",
        "",
        *markdown_table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
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
        "结论：mirror-imbalance 已被继续拆成 missing-mirror 与 unequal-mirror-pair",
        "两类 residual carriers。多数剩余来自没有符号镜像的 signed child；这压缩了",
        "目标对象，但尚未给出任何相位节省或 trace/Kloosterman 完成。",
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
        f"mirror_imbalance_support_ledger_closed={str(payload['mirror_imbalance_support_ledger_closed']).lower()}",
        f"missing_mirror_carrier_phase_saving_closed={str(payload['missing_mirror_carrier_phase_saving_closed']).lower()}",
        f"unequal_mirror_pair_residual_phase_saving_closed={str(payload['unequal_mirror_pair_residual_phase_saving_closed']).lower()}",
        f"thin_P_support_carrier_summation_closed={str(payload['thin_P_support_carrier_summation_closed']).lower()}",
        f"residual_endpoint_path_summation_closed={str(payload['residual_endpoint_path_summation_closed']).lower()}",
        f"completion_to_external_trace_or_kloosterman_closed={str(payload['completion_to_external_trace_or_kloosterman_closed']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """生成审计证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n")
    OUT_JSON.write_text(text + "\n")
    OUT_MD.write_text(build_markdown(payload))
    audit = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(
        "mirror_imbalance_support_ledger_closed="
        f"{payload['mirror_imbalance_support_ledger_closed']}"
    )
    print(f"mirror_imbalance_edge_mass={audit['mirror_imbalance_edge_mass']}")
    print(f"missing_mirror_edge_mass={audit['missing_mirror_edge_mass']}")
    print(
        "unequal_mirror_pair_residual_edge_mass="
        f"{audit['unequal_mirror_pair_residual_edge_mass']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
