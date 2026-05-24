#!/usr/bin/env python3
"""审计 raw-base/signed-child 的符号镜像配平障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-audit.json

上一层把 weighted phase saving 的组合载体拆成 signed carriers 与
raw-base/signed-child fragmentation。本层继续下钻一个最自然的非循环候选：

    同 raw-base 内是否能用 A-step 符号镜像 positive <-> negative 配平？

该层关闭的是 signed-child mirror pairing 的有限账本；它不证明镜像配平足够，
也不证明 weighted phase saving。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit as carrier  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit as flow  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
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
        "role": "could matter only after mirror-imbalance carriers are realized as trace-function sums",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "does not by itself provide signed-child mirror balance",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "requires Type-II boxes rather than signed-child mirror packets",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "requires admissible fraction families after mirror imbalance is isolated",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "prime existence does not balance signed-child mirror masses",
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


def flip_sign(label: str) -> str:
    """翻转 A-step 符号标签。"""
    if label == "positive":
        return "negative"
    if label == "negative":
        return "positive"
    return label


def signed_mirror_template(cycle: list[tuple[int, int, str]]) -> str:
    """返回同 raw-base 下的 A-step 符号镜像模板。"""
    mirrored = [(gap, carry, flip_sign(sign)) for gap, carry, sign in cycle]
    return signature.signed_template(mirrored)


def top_base_rows(
    base_edge_mass: Counter[str],
    base_child_edge_mass: dict[str, Counter[str]],
    base_balanced_mass: Counter[str],
    base_imbalance_mass: Counter[str],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出镜像不平衡最高的 raw-base 行。"""
    order = sorted(
        base_edge_mass,
        key=lambda key: (-base_imbalance_mass[key], -base_edge_mass[key], key),
    )
    rows = []
    for key in order[:limit]:
        children = base_child_edge_mass[key]
        top_child, top_mass = children.most_common(1)[0]
        rows.append(
            {
                "raw_base_template": key,
                "signed_child_count": len(children),
                "signed_edge_mass": base_edge_mass[key],
                "mirror_balanced_edge_mass": base_balanced_mass[key],
                "mirror_imbalance_edge_mass": base_imbalance_mass[key],
                "mirror_imbalance_ratio": base_imbalance_mass[key] / base_edge_mass[key],
                "top_child_edge_share": top_mass / base_edge_mass[key],
                "top_signed_child": top_child,
            }
        )
    return rows


def top_pair_rows(
    pair_rows: list[dict[str, Any]],
    limit: int = 20,
) -> list[dict[str, Any]]:
    """输出镜像 pair 中残差最大的行。"""
    return sorted(
        pair_rows,
        key=lambda row: (-row["imbalance_edge_mass"], -row["total_edge_mass"], row["raw_base_template"]),
    )[:limit]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 signed-child mirror reconciliation。"""
    primes = flow.primorial.prime_sieve(2 * max_prime + 10)
    packets = flow.qprefix_atom.shell_step.packetize_rectangles(max_prime)
    fibres_by_row = flow.qprefix_atom.collar.right_tail_fibres_by_row(max_prime, primes)
    previous_payload = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-audit.json"
        ).read_text()
    )
    previous = previous_payload["finite_audit"]

    totals: Counter[str] = Counter()
    signed_template_edge_mass: Counter[str] = Counter()
    signed_template_count: Counter[str] = Counter()
    mirror_of: dict[str, str] = {}
    signed_template_base: dict[str, str] = {}
    raw_base_edge_mass: Counter[str] = Counter()
    raw_base_child_edge_mass: dict[str, Counter[str]] = defaultdict(Counter)
    raw_base_child_count: Counter[str] = Counter()
    a_class_edge_mass: Counter[str] = Counter()

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
                mirror = signed_mirror_template(cycle)
                base = signature.raw_template([(item[0], item[1]) for item in cycle])
                length = len(cycle)
                cls = carrier.a_class(cycle)
                signed_template_edge_mass[template] += length
                signed_template_count[template] += 1
                mirror_of[template] = mirror
                signed_template_base[template] = base
                raw_base_edge_mass[base] += length
                raw_base_child_edge_mass[base][template] += length
                raw_base_child_count[base] += 1
                a_class_edge_mass[cls] += length
                totals["signed_cycle_packet_count"] += 1
                totals["signed_cycle_edge_mass"] += length

    visited: set[str] = set()
    pair_rows: list[dict[str, Any]] = []
    base_balanced_mass: Counter[str] = Counter()
    base_imbalance_mass: Counter[str] = Counter()
    self_mirror_edge_mass = 0
    missing_mirror_edge_mass = 0
    exact_pair_edge_mass = 0

    for template, mass in signed_template_edge_mass.items():
        if template in visited:
            continue
        mirror = mirror_of[template]
        raw_base = signed_template_base[template]
        mirror_mass = signed_template_edge_mass.get(mirror, 0)
        if mirror == template:
            balanced = mass
            imbalance = 0
            self_mirror_edge_mass += mass
            visited.add(template)
        elif mirror in signed_template_edge_mass:
            balanced = 2 * min(mass, mirror_mass)
            imbalance = abs(mass - mirror_mass)
            exact_pair_edge_mass += balanced if imbalance == 0 else 0
            visited.add(template)
            visited.add(mirror)
        else:
            balanced = 0
            imbalance = mass
            missing_mirror_edge_mass += mass
            visited.add(template)

        base_balanced_mass[raw_base] += balanced
        base_imbalance_mass[raw_base] += imbalance
        pair_rows.append(
            {
                "raw_base_template": raw_base,
                "signed_child": template,
                "mirror_child": mirror,
                "child_edge_mass": mass,
                "mirror_edge_mass": mirror_mass,
                "total_edge_mass": mass + mirror_mass if mirror != template else mass,
                "balanced_edge_mass": balanced,
                "imbalance_edge_mass": imbalance,
            }
        )

    total_balanced = sum(base_balanced_mass.values())
    total_imbalance = sum(base_imbalance_mass.values())
    exact_balance_base_count = sum(
        1
        for base, mass in raw_base_edge_mass.items()
        if base_imbalance_mass[base] == 0 and mass > 0
    )
    multi_child_base_count = sum(
        1 for children in raw_base_child_edge_mass.values() if len(children) > 1
    )
    multi_child_edge_mass = sum(
        raw_base_edge_mass[base]
        for base, children in raw_base_child_edge_mass.items()
        if len(children) > 1
    )
    base_imbalance_ratios = [
        base_imbalance_mass[base] / mass for base, mass in raw_base_edge_mass.items() if mass
    ]

    ledger_closed = (
        previous["cycle_signature_weight_carrier_ledger_closed"]
        and totals["atom_count_total"] == previous["cycle_signature_atom_count_total"]
        and totals["switch_atom_count"] == previous["switch_atom_count"]
        and totals["non_switch_atom_count"] == previous["non_switch_atom_count"]
        and totals["adjacent_letter_pair_count_inside_atoms"]
        == previous["adjacent_letter_pair_count_inside_atoms"]
        and totals["signed_cycle_packet_count"] == previous["signed_cycle_packet_count"]
        and totals["signed_cycle_edge_mass"] == previous["signed_cycle_edge_mass"]
        and totals["signed_residual_edge_mass"] == previous["signed_residual_edge_mass"]
        and len(signed_template_edge_mass) == previous["signed_cycle_signature_count"]
        and len(raw_base_edge_mass) == previous["raw_base_signed_refinement_count"]
        and multi_child_base_count == previous["raw_base_with_multiple_signed_children_count"]
        and total_balanced + total_imbalance == totals["signed_cycle_edge_mass"]
    )

    return {
        "max_prime": max_prime,
        "previous_cycle_signature_weight_carrier_ledger_closed": previous[
            "cycle_signature_weight_carrier_ledger_closed"
        ],
        "signed_child_mirror_reconciliation_ledger_closed": ledger_closed,
        "atom_count_total": totals["atom_count_total"],
        "switch_atom_count": totals["switch_atom_count"],
        "non_switch_atom_count": totals["non_switch_atom_count"],
        "adjacent_letter_pair_count_inside_atoms": totals[
            "adjacent_letter_pair_count_inside_atoms"
        ],
        "signed_cycle_packet_count": totals["signed_cycle_packet_count"],
        "signed_cycle_edge_mass": totals["signed_cycle_edge_mass"],
        "signed_residual_edge_mass": totals["signed_residual_edge_mass"],
        "signed_cycle_signature_count": len(signed_template_edge_mass),
        "raw_base_signed_refinement_count": len(raw_base_edge_mass),
        "raw_base_with_multiple_signed_children_count": multi_child_base_count,
        "raw_base_multi_child_signed_edge_mass": multi_child_edge_mass,
        "raw_base_multi_child_signed_edge_ratio": multi_child_edge_mass
        / totals["signed_cycle_edge_mass"],
        "mirror_balanced_edge_mass": total_balanced,
        "mirror_balanced_edge_ratio": total_balanced / totals["signed_cycle_edge_mass"],
        "mirror_imbalance_edge_mass": total_imbalance,
        "mirror_imbalance_edge_ratio": total_imbalance / totals["signed_cycle_edge_mass"],
        "missing_mirror_edge_mass": missing_mirror_edge_mass,
        "missing_mirror_edge_ratio": missing_mirror_edge_mass
        / totals["signed_cycle_edge_mass"],
        "self_mirror_edge_mass": self_mirror_edge_mass,
        "exact_mirror_pair_edge_mass": exact_pair_edge_mass,
        "raw_base_exact_mirror_balance_count": exact_balance_base_count,
        "raw_base_exact_mirror_balance_ratio": exact_balance_base_count
        / len(raw_base_edge_mass),
        "raw_base_mirror_imbalance_ratio_min": min(base_imbalance_ratios),
        "raw_base_mirror_imbalance_ratio_median": statistics.median(base_imbalance_ratios),
        "raw_base_mirror_imbalance_ratio_max": max(base_imbalance_ratios),
        "signed_A_class_edge_rows": [
            {
                "A_class": key,
                "edge_mass": a_class_edge_mass[key],
                "edge_ratio": a_class_edge_mass[key] / totals["signed_cycle_edge_mass"],
            }
            for key in sorted(a_class_edge_mass)
        ],
        "top_raw_base_mirror_imbalance_rows": top_base_rows(
            raw_base_edge_mass,
            raw_base_child_edge_mass,
            base_balanced_mass,
            base_imbalance_mass,
        ),
        "top_signed_child_mirror_pair_rows": top_pair_rows(pair_rows),
        "mirror_pairing_enough_for_reconciliation_closed": False,
        "raw_base_to_signed_child_weight_reconciliation_closed": False,
        "signed_cycle_signature_carrier_weighted_phase_saving_closed": False,
        "thin_P_support_carrier_summation_closed": False,
        "residual_endpoint_path_summation_closed": False,
        "completion_to_external_trace_or_kloosterman_closed": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "signed_child_mirror_pairing_ledger_closed_reconciliation_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after weight-carrier isolation, the most direct non-cyclic test is signed-child mirror pairing inside each raw base",
        "current_object": {
            "input": "signed children of each raw cycle-signature base",
            "operation": "A-step sign mirror positive<->negative pairing and edge-mass imbalance audit",
            "dominant_shape": "mirror pairing leaves a large imbalance rather than closing raw-base signed-child reconciliation",
            "remaining": "signed mirror-imbalance phase saving, thin support summation, residual endpoints, and trace/Kloosterman completion",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "CycleSignatureWeightCarrierImported",
                finite_audit["previous_cycle_signature_weight_carrier_ledger_closed"],
                finite_audit["previous_cycle_signature_weight_carrier_ledger_closed"],
                "The previous weight-carrier ledger is imported.",
                "none for import",
            ),
            gate(
                "SignedChildMirrorPairingLedger",
                finite_audit["signed_child_mirror_reconciliation_ledger_closed"],
                finite_audit["signed_child_mirror_reconciliation_ledger_closed"],
                "Every signed child is compared with its A-step sign mirror inside the same raw base.",
                "none for current deterministic mirror ledger",
            ),
            gate(
                "MirrorPairingEnoughForReconciliation",
                False,
                False,
                "Use sign-mirror pairing alone to reconcile raw-base signed-child weights.",
                "fails at the exposed mirror imbalance mass",
            ),
            gate(
                "MirrorImbalancePhaseSaving",
                False,
                False,
                "Prove cancellation for the mirror-imbalance residue.",
                "requires analytic phase input on the imbalanced signed-child carriers",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "not directly applicable before mirror-imbalance carriers become trace sums",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "does not supply signed-child mirror balance",
            "Pascadi_composite_Type_II": "not matched to the signed-child mirror ledger",
            "Wright_unbalanced_Kloosterman": "candidate only after mirror residues become admissible fractions",
            "Li_short_interval_x_052": "does not estimate mirror-pair imbalance",
        },
        "latest_narrowest_mouth": [
            "SignedChildMirrorImbalancePhaseSaving",
            "AND NonMirrorSignedChildCarrierControl",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND TraceKloostermanCompletionOfMirrorImbalanceAndResidualPackets",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "signed_child_mirror_reconciliation_ledger_closed": finite_audit[
            "signed_child_mirror_reconciliation_ledger_closed"
        ],
        "mirror_pairing_enough_for_reconciliation_closed": False,
        "raw_base_to_signed_child_weight_reconciliation_closed": False,
        "signed_child_mirror_imbalance_phase_saving_closed": False,
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
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature signed-child mirror reconciliation 审计",
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
        "## 2. signed-child mirror 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"signed_child_mirror_reconciliation_ledger_closed={str(audit['signed_child_mirror_reconciliation_ledger_closed']).lower()}",
        f"atom_count_total={audit['atom_count_total']}",
        f"switch_atom_count={audit['switch_atom_count']}",
        f"non_switch_atom_count={audit['non_switch_atom_count']}",
        f"adjacent_letter_pair_count_inside_atoms={audit['adjacent_letter_pair_count_inside_atoms']}",
        f"signed_cycle_packet_count={audit['signed_cycle_packet_count']}",
        f"signed_cycle_edge_mass={audit['signed_cycle_edge_mass']}",
        f"signed_cycle_signature_count={audit['signed_cycle_signature_count']}",
        f"raw_base_signed_refinement_count={audit['raw_base_signed_refinement_count']}",
        f"raw_base_with_multiple_signed_children_count={audit['raw_base_with_multiple_signed_children_count']}",
        f"raw_base_multi_child_signed_edge_ratio={audit['raw_base_multi_child_signed_edge_ratio']}",
        f"mirror_balanced_edge_mass={audit['mirror_balanced_edge_mass']}",
        f"mirror_balanced_edge_ratio={audit['mirror_balanced_edge_ratio']}",
        f"mirror_imbalance_edge_mass={audit['mirror_imbalance_edge_mass']}",
        f"mirror_imbalance_edge_ratio={audit['mirror_imbalance_edge_ratio']}",
        f"missing_mirror_edge_ratio={audit['missing_mirror_edge_ratio']}",
        f"raw_base_exact_mirror_balance_count={audit['raw_base_exact_mirror_balance_count']}",
        f"raw_base_exact_mirror_balance_ratio={audit['raw_base_exact_mirror_balance_ratio']}",
        f"raw_base_mirror_imbalance_ratio_min/median/max={audit['raw_base_mirror_imbalance_ratio_min']}/{audit['raw_base_mirror_imbalance_ratio_median']}/{audit['raw_base_mirror_imbalance_ratio_max']}",
        f"mirror_pairing_enough_for_reconciliation_closed={str(audit['mirror_pairing_enough_for_reconciliation_closed']).lower()}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "signed A-class edge mass：",
        "",
        *markdown_table(audit["signed_A_class_edge_rows"], ["A_class", "edge_mass", "edge_ratio"]),
        "",
        "最高 mirror-imbalance raw bases：",
        "",
        *markdown_table(
            audit["top_raw_base_mirror_imbalance_rows"],
            [
                "raw_base_template",
                "signed_child_count",
                "signed_edge_mass",
                "mirror_balanced_edge_mass",
                "mirror_imbalance_edge_mass",
                "mirror_imbalance_ratio",
                "top_child_edge_share",
                "top_signed_child",
            ],
        ),
        "",
        "最高 mirror-pair 残差：",
        "",
        *markdown_table(
            audit["top_signed_child_mirror_pair_rows"],
            [
                "raw_base_template",
                "signed_child",
                "mirror_child",
                "child_edge_mass",
                "mirror_edge_mass",
                "balanced_edge_mass",
                "imbalance_edge_mass",
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
        "结论：同 raw-base 内的 A-step 符号镜像配对已成账，但镜像配平本身",
        "不足以关闭 raw-base/signed-child reconciliation。剩余对象被压到",
        "mirror-imbalance signed-child carriers。",
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
        f"signed_child_mirror_reconciliation_ledger_closed={str(payload['signed_child_mirror_reconciliation_ledger_closed']).lower()}",
        f"mirror_pairing_enough_for_reconciliation_closed={str(payload['mirror_pairing_enough_for_reconciliation_closed']).lower()}",
        f"raw_base_to_signed_child_weight_reconciliation_closed={str(payload['raw_base_to_signed_child_weight_reconciliation_closed']).lower()}",
        f"signed_child_mirror_imbalance_phase_saving_closed={str(payload['signed_child_mirror_imbalance_phase_saving_closed']).lower()}",
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
        "signed_child_mirror_reconciliation_ledger_closed="
        f"{payload['signed_child_mirror_reconciliation_ledger_closed']}"
    )
    print(
        "mirror_pairing_enough_for_reconciliation_closed="
        f"{payload['mirror_pairing_enough_for_reconciliation_closed']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
