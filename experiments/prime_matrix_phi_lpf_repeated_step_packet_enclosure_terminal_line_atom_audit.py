#!/usr/bin/env python3
"""审计 repeated-step packet enclosure 的 terminal q-prefix line atoms。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_line_atom_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-line-atom-audit.json

上一层把共享 affine skeleton 嵌回两个 right-tail shell-step packets。本层再向下
拆一格：把这两个 packet 的 selected terminal m-pairs 与 extra m-shell 点都写成
固定 m 的 q-prefix line atoms，并显式区分唯一支撑质量与两条 splice 的 incidence
重复质量。该层只关闭有限 line-atom 账本，不证明 terminal atom 的 uniform bound。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-line-atom"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"

PACKET_ENCLOSURE_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-affine-skeleton-packet-enclosure-audit.json"
)
QPREFIX_LINE_ATOM_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json"
)
SHELL_STEP_PACKET_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json"
)

DEPENDENCIES = [
    PACKET_ENCLOSURE_AUDIT,
    QPREFIX_LINE_ATOM_AUDIT,
    SHELL_STEP_PACKET_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "trace bilinear input; terminal line atoms still lack a completed moving q denominator family",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "power-saving Kloosterman bilinear input applies after a valid completed Kloosterman variable is exposed",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "composite-modulus Type-II input does not directly estimate two fixed prime-q prefixes",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced Kloosterman-fraction geometry is closest after line atoms are promoted to a family",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052_v8",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "short-interval prime existence does not supply fixed terminal line-atom phase cancellation",
    },
    {
        "key": "Maynard_2015_small_gaps_prime_gaps",
        "url": "https://doi.org/10.4007/annals.2015.181.1.7",
        "role": "small-gap existence does not control signed Phi-LPF terminal packet line atoms",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def load_json(path: Path) -> dict[str, Any]:
    """读入 JSON 证书。"""
    return json.loads(path.read_text())


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def line_atom(packet_side: str, packet: dict[str, Any], m_value: int, role: str) -> dict[str, Any]:
    """构造一个固定 m 的 q-prefix line atom。"""
    m_values = packet["m_values"]
    rank = m_values.index(m_value) + 1
    terminal_ranks = {len(m_values) - 1, len(m_values)}
    q_values = packet["q_values"]
    return {
        "packet_side": packet_side,
        "packet_index": packet["packet_index"],
        "P": packet["P"],
        "strip": packet["strip"],
        "role": role,
        "m": m_value,
        "m_rank": rank,
        "m_offset_from_P": m_value - packet["P"],
        "m_rank_terminal": rank in terminal_ranks,
        "q_start": packet["q_start"],
        "q_end": packet["q_end"],
        "q_values": q_values,
        "q_prefix_count": packet["q_prefix_count"],
        "q_prefix_contiguous": packet["q_prefix_contiguous"],
        "edge_count": packet["q_prefix_count"],
    }


def line_atoms_from_packet(packet_side: str, packet: dict[str, Any]) -> list[dict[str, Any]]:
    """把一个 packet 拆成 selected terminal 与 extra line atoms。"""
    selected = set(packet["selected_m_pair"])
    atoms = []
    for m_value in packet["m_values"]:
        role = "selected_terminal" if m_value in selected else "extra_shell"
        atoms.append(line_atom(packet_side, packet, m_value, role))
    return atoms


def expanded_edges(atoms: list[dict[str, Any]]) -> set[tuple[int, int, int]]:
    """展开 line atoms 的唯一边集合。"""
    edges: set[tuple[int, int, int]] = set()
    for atom in atoms:
        for q_value in atom["q_values"]:
            edges.add((atom["P"], q_value, atom["m"]))
    return edges


def summarize_atoms(atoms: list[dict[str, Any]], role: str) -> dict[str, Any]:
    """汇总某类 line atoms。"""
    selected = [atom for atom in atoms if atom["role"] == role]
    return {
        "role": role,
        "line_atom_count": len(selected),
        "edge_mass": sum(atom["edge_count"] for atom in selected),
        "packet_indices": sorted({atom["packet_index"] for atom in selected}),
        "m_values": [atom["m"] for atom in selected],
    }


def audit() -> dict[str, Any]:
    """生成 terminal line atom 审计。"""
    packet_payload = load_json(PACKET_ENCLOSURE_AUDIT)
    qprefix_payload = load_json(QPREFIX_LINE_ATOM_AUDIT)
    shell_payload = load_json(SHELL_STEP_PACKET_AUDIT)
    packet_audit = packet_payload["finite_audit"]
    profiles = packet_audit["packet_pair_profiles"]
    first_profile = profiles[0]
    left_packet = first_profile["left_packet_profile"]
    right_packet = first_profile["right_packet_profile"]

    left_atoms = line_atoms_from_packet("left", left_packet)
    right_atoms = line_atoms_from_packet("right", right_packet)
    unique_atoms = left_atoms + right_atoms
    unique_edges = expanded_edges(unique_atoms)

    selected_atoms = [atom for atom in unique_atoms if atom["role"] == "selected_terminal"]
    extra_atoms = [atom for atom in unique_atoms if atom["role"] == "extra_shell"]
    selected_edges = expanded_edges(selected_atoms)
    extra_edges = expanded_edges(extra_atoms)
    packet_edge_mass = left_packet["edge_count"] + right_packet["edge_count"]
    selected_edge_mass = sum(atom["edge_count"] for atom in selected_atoms)
    extra_edge_mass = sum(atom["edge_count"] for atom in extra_atoms)
    splice_count = packet_audit["splice_count"]

    packet_support_identity = (
        packet_payload["packet_enclosure_ledger_closed"]
        and qprefix_payload["qprefix_line_atomization_closed"]
        and shell_payload["packet_identity_verified"]
        and len(unique_edges) == packet_edge_mass
        and selected_edge_mass + extra_edge_mass == packet_edge_mass
        and len(selected_edges & extra_edges) == 0
        and all(atom["q_prefix_contiguous"] for atom in unique_atoms)
    )
    selected_terminal_closed = (
        packet_support_identity
        and len(selected_atoms) == 4
        and selected_edge_mass == 70
        and all(atom["m_rank_terminal"] for atom in selected_atoms)
        and [atom["m"] for atom in selected_atoms] == [757, 761, 769, 773]
    )

    return {
        "max_prime": packet_audit["max_prime"],
        "previous_packet_enclosure_ledger_closed": packet_payload["packet_enclosure_ledger_closed"],
        "previous_qprefix_line_atomization_closed": qprefix_payload["qprefix_line_atomization_closed"],
        "previous_shell_step_packet_identity_verified": shell_payload["packet_identity_verified"],
        "splice_count": splice_count,
        "support_packet_indices": [
            left_packet["packet_index"],
            right_packet["packet_index"],
        ],
        "support_packet_edge_mass": packet_edge_mass,
        "unique_line_atom_count_total": len(unique_atoms),
        "unique_line_atom_edge_mass_total": sum(atom["edge_count"] for atom in unique_atoms),
        "unique_expanded_edge_set_size": len(unique_edges),
        "selected_terminal_line_atom_count": len(selected_atoms),
        "selected_terminal_line_atom_edge_mass": selected_edge_mass,
        "extra_line_atom_count": len(extra_atoms),
        "extra_line_atom_edge_mass": extra_edge_mass,
        "selected_plus_extra_edge_mass": selected_edge_mass + extra_edge_mass,
        "selected_terminal_line_atom_edge_mass_by_packet": [
            {
                "packet_side": "left",
                "packet_index": left_packet["packet_index"],
                "selected_m_values": left_packet["selected_m_pair"],
                "q_prefix_count": left_packet["q_prefix_count"],
                "selected_line_atom_count": len(left_packet["selected_m_pair"]),
                "selected_edge_mass": len(left_packet["selected_m_pair"])
                * left_packet["q_prefix_count"],
            },
            {
                "packet_side": "right",
                "packet_index": right_packet["packet_index"],
                "selected_m_values": right_packet["selected_m_pair"],
                "q_prefix_count": right_packet["q_prefix_count"],
                "selected_line_atom_count": len(right_packet["selected_m_pair"]),
                "selected_edge_mass": len(right_packet["selected_m_pair"])
                * right_packet["q_prefix_count"],
            },
        ],
        "extra_line_atom_edge_mass_by_packet": [
            {
                "packet_side": "left",
                "packet_index": left_packet["packet_index"],
                "extra_m_values": left_packet["extra_m_values"],
                "q_prefix_count": left_packet["q_prefix_count"],
                "extra_line_atom_count": len(left_packet["extra_m_values"]),
                "extra_edge_mass": len(left_packet["extra_m_values"]) * left_packet["q_prefix_count"],
            },
            {
                "packet_side": "right",
                "packet_index": right_packet["packet_index"],
                "extra_m_values": right_packet["extra_m_values"],
                "q_prefix_count": right_packet["q_prefix_count"],
                "extra_line_atom_count": len(right_packet["extra_m_values"]),
                "extra_edge_mass": len(right_packet["extra_m_values"]) * right_packet["q_prefix_count"],
            },
        ],
        "selected_atom_summary": summarize_atoms(unique_atoms, "selected_terminal"),
        "extra_atom_summary": summarize_atoms(unique_atoms, "extra_shell"),
        "line_atoms": unique_atoms,
        "selected_and_extra_edges_disjoint": len(selected_edges & extra_edges) == 0,
        "all_line_atoms_qprefix_contiguous": all(atom["q_prefix_contiguous"] for atom in unique_atoms),
        "all_selected_line_atoms_terminal": all(atom["m_rank_terminal"] for atom in selected_atoms),
        "packet_line_atom_mass_identity_verified": packet_support_identity,
        "terminal_line_atom_ledger_closed": selected_terminal_closed,
        "splice_incidence_selected_line_atom_count": len(selected_atoms) * splice_count,
        "splice_incidence_selected_edge_mass": selected_edge_mass * splice_count,
        "splice_incidence_extra_line_atom_count": len(extra_atoms) * splice_count,
        "splice_incidence_extra_edge_mass": extra_edge_mass * splice_count,
        "support_vs_splice_incidence_duplicate_factor": splice_count,
        "selected_terminal_line_atom_uniform_bound_proved": False,
        "packet_extra_line_atom_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_packet_enclosure_terminal_line_atom_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "terminal_line_atom_ledger_closed_uniform_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the packet enclosure is fixed; the next acyclic refinement is to split selected terminal pairs and extra shell points into fixed-m q-prefix line atoms",
        "current_object": {
            "input": "packet2842 and packet1887 from the repeated-step affine-skeleton packet enclosure",
            "operation": "deduplicate the two splices to unique packet support and split support into selected terminal versus extra q-prefix line atoms",
            "dominant_shape": "selected terminal support has 4 line atoms and edge mass 70; extra shell support has 3 line atoms and edge mass 63",
            "remaining": "prove a uniform bound for these terminal q-prefix line atoms or convert them into a summable trace/Kloosterman family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PacketEnclosureImported",
                finite_audit["previous_packet_enclosure_ledger_closed"],
                finite_audit["previous_packet_enclosure_ledger_closed"],
                "The affine-skeleton packet enclosure is imported.",
                "none for import",
            ),
            gate(
                "GlobalQPrefixLineAtomizationImported",
                finite_audit["previous_qprefix_line_atomization_closed"],
                finite_audit["previous_qprefix_line_atomization_closed"],
                "The global fixed-m q-prefix line atom identity is imported.",
                "none for support import",
            ),
            gate(
                "PacketLineAtomMassIdentity",
                finite_audit["packet_line_atom_mass_identity_verified"],
                finite_audit["packet_line_atom_mass_identity_verified"],
                "The two packets split into seven unique line atoms with edge mass 133.",
                "none for finite packet support",
            ),
            gate(
                "SelectedTerminalLineAtomLedger",
                finite_audit["terminal_line_atom_ledger_closed"],
                finite_audit["terminal_line_atom_ledger_closed"],
                "The selected witness pairs are exactly four terminal line atoms of edge mass 70.",
                "none for finite terminal atom ledger",
            ),
            gate(
                "SelectedTerminalLineAtomUniformBound",
                False,
                False,
                "Control the selected terminal q-prefix line atoms uniformly.",
                "requires cancellation beyond finite packet support",
            ),
            gate(
                "ExtraLineAtomAbsorption",
                False,
                False,
                "Absorb the three extra packet line atoms without losing the terminal gain.",
                "requires a summable family or PDEC/SAE certificate",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "terminal atoms are explicit but remain fixed short prime-q prefixes rather than a completed trace bilinear family",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "the Kloosterman input still needs a completed moving denominator and averaging range",
            "Pascadi_composite_Type_II": "the seven line atoms are one-dimensional supports, not composite Type-II boxes",
            "Wright_unbalanced_Kloosterman": "the packet geometry resembles an unbalanced interface only after promotion to a family",
            "Li_short_interval_x_052": "prime existence in short intervals does not control terminal line-atom phases",
            "Maynard_small_gaps": "bounded prime-gap existence does not supply signed packet cancellation",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepPacketEnclosureTerminalLineAtomUniformBound(packet2842:selected m={757,761}, q=541..709; packet1887:selected m={769,773}, q=439..467)",
            "AND PacketEnclosureExtraLineAtomAbsorption(m={719,751,479})",
            "AND RepeatedStepAffineSkeletonPacketEnclosureUniformBoundOutsideTerminalLineAtoms",
            "AND RepeatedStepSharedWitnessPairAffineSkeletonUniformBoundOutsidePacketEnclosure",
            "AND RepeatedStepSameAtomOccurrenceSpliceUniformBoundOutsideSharedWitnessPairSkeleton",
            "AND RepeatedStepRepeatedNodePSwitchCutUniformBoundOutsideOccurrenceSplice",
            "AND RepeatedStepMixedPSourceSinkPathCoverUniformBoundOutsideSwitchCuts",
            "AND RepeatedStepDirectedIncidenceGraphUniformBoundOutsidePathCover",
            "AND RepeatedStepUniformFamilyBoundOutsideDirectedIncidenceGraph",
            "AND DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar outside repeated atoms)",
            "AND OtherLargestAtomTemplateWitnessFamilyBounds",
            "AND OtherCoreRouteCycleSwitchAtomBounds",
            "AND TopTwoNonCoreSignCycleResidualBound",
            "AND Gap2LowerWingTwinCollisionBound",
            "AND Gap2RightTailTwoSidedTwinResidualCollisionBound",
            "AND Gap4RightTailLeftCollarCousinResidualCollisionBound",
            "AND Gap4UpperWingCousinResidualCollisionBound",
            "AND Gap4LowerWingCousinResidualCollisionBound",
            "AND Gap6SexyAdjacentPairCollisionBound",
            "AND GapGe8AdjacentPairCollisionBound",
            "AND NonAdjacentPrimePairCollisionBound",
            "AND AdjacentPrimeChainCollisionBound",
            "AND MultiPacketDuplicateTransportBound",
            "AND SinglePacketSingleMMultiCycleSuppression",
            "AND RepeatedOccurrenceAggregationOrPDEC",
            "AND CycleOccurrenceProductBoundOrPDEC",
            "AND SinglePSliceEndpointPacketSummationOrPDEC",
            "AND MultiPPureEndpointTraceKloostermanCompletion",
            "AND PureEndpointCarrierPhaseSaving",
            "AND MixedRightTailEndpointRouterNoLoss",
            "AND UnequalMirrorPairResidualPhaseSaving",
            "AND ThinPSupportCarrierSummationWithoutLoss",
            "AND ResidualEndpointPathSummationWithoutBoundaryLoss",
            "AND NoLossAggregationAcross15439QPrefixFlowAtoms",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "terminal_line_atom_ledger_closed": finite_audit["terminal_line_atom_ledger_closed"],
        "selected_terminal_line_atom_uniform_bound_proved": False,
        "packet_extra_line_atom_absorption_proved": False,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
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
    audit_result = payload["finite_audit"]
    current = payload["current_object"]
    atom_rows = [
        {
            "side": atom["packet_side"],
            "packet": atom["packet_index"],
            "P": atom["P"],
            "role": atom["role"],
            "m": atom["m"],
            "rank": atom["m_rank"],
            "terminal": atom["m_rank_terminal"],
            "q_window": f"[{atom['q_start']},{atom['q_end']}]",
            "q_count": atom["q_prefix_count"],
            "edge": atom["edge_count"],
        }
        for atom in audit_result["line_atoms"]
    ]
    lines = [
        "# Prime Matrix Phi-LPF repeated-step packet-enclosure terminal line atom 审计",
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
        "## 2. terminal line atom 有限审计",
        "",
        "```text",
        f"previous_packet_enclosure_ledger_closed={str(audit_result['previous_packet_enclosure_ledger_closed']).lower()}",
        f"previous_qprefix_line_atomization_closed={str(audit_result['previous_qprefix_line_atomization_closed']).lower()}",
        f"splice_count={audit_result['splice_count']}",
        f"support_packet_indices={audit_result['support_packet_indices']}",
        f"support_packet_edge_mass={audit_result['support_packet_edge_mass']}",
        f"unique_line_atom_count_total={audit_result['unique_line_atom_count_total']}",
        f"unique_line_atom_edge_mass_total={audit_result['unique_line_atom_edge_mass_total']}",
        f"unique_expanded_edge_set_size={audit_result['unique_expanded_edge_set_size']}",
        f"selected_terminal_line_atom_count={audit_result['selected_terminal_line_atom_count']}",
        f"selected_terminal_line_atom_edge_mass={audit_result['selected_terminal_line_atom_edge_mass']}",
        f"extra_line_atom_count={audit_result['extra_line_atom_count']}",
        f"extra_line_atom_edge_mass={audit_result['extra_line_atom_edge_mass']}",
        f"selected_and_extra_edges_disjoint={str(audit_result['selected_and_extra_edges_disjoint']).lower()}",
        f"all_line_atoms_qprefix_contiguous={str(audit_result['all_line_atoms_qprefix_contiguous']).lower()}",
        f"all_selected_line_atoms_terminal={str(audit_result['all_selected_line_atoms_terminal']).lower()}",
        f"packet_line_atom_mass_identity_verified={str(audit_result['packet_line_atom_mass_identity_verified']).lower()}",
        f"terminal_line_atom_ledger_closed={str(audit_result['terminal_line_atom_ledger_closed']).lower()}",
        f"splice_incidence_selected_edge_mass={audit_result['splice_incidence_selected_edge_mass']}",
        f"splice_incidence_extra_edge_mass={audit_result['splice_incidence_extra_edge_mass']}",
        f"selected_terminal_line_atom_uniform_bound_proved={str(audit_result['selected_terminal_line_atom_uniform_bound_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "line atom rows：",
        "",
        *markdown_table(
            atom_rows,
            ["side", "packet", "P", "role", "m", "rank", "terminal", "q_window", "q_count", "edge"],
        ),
        "",
        "selected edge mass by packet：",
        "",
        *markdown_table(
            audit_result["selected_terminal_line_atom_edge_mass_by_packet"],
            [
                "packet_side",
                "packet_index",
                "selected_m_values",
                "q_prefix_count",
                "selected_line_atom_count",
                "selected_edge_mass",
            ],
        ),
        "",
        "extra edge mass by packet：",
        "",
        *markdown_table(
            audit_result["extra_line_atom_edge_mass_by_packet"],
            [
                "packet_side",
                "packet_index",
                "extra_m_values",
                "q_prefix_count",
                "extra_line_atom_count",
                "extra_edge_mass",
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
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：两个 packet 的唯一支撑被拆成 `7` 个固定 `m` 的 q-prefix line atoms。",
        "selected terminal 部分是 `4` 个 line atoms，唯一边质量 `70`；extra shell 部分是 `3` 个 line atoms，唯一边质量 `63`。",
        "两条 splice 共享同一 packet 支撑，所以 splice-incidence 质量是唯一支撑质量的两倍；这不是新的相消。",
        "本层关闭 finite terminal line-atom ledger，但不关闭 uniform bound、extra absorption 或 trace/Kloosterman completion。",
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
        f"terminal_line_atom_ledger_closed={str(payload['terminal_line_atom_ledger_closed']).lower()}",
        f"selected_terminal_line_atom_uniform_bound_proved={str(payload['selected_terminal_line_atom_uniform_bound_proved']).lower()}",
        f"packet_extra_line_atom_absorption_proved={str(payload['packet_extra_line_atom_absorption_proved']).lower()}",
        f"summable_family_created={str(payload['summable_family_created']).lower()}",
        f"trace_or_kloosterman_completion_ready={str(payload['trace_or_kloosterman_completion_ready']).lower()}",
        f"phi_lpf_parity_barrier_globally_broken={str(payload['phi_lpf_parity_barrier_globally_broken']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        "```",
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
    OUT_MD.write_text(build_markdown(payload).rstrip() + "\n")
    audit_result = payload["finite_audit"]
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"terminal_line_atom_ledger_closed={payload['terminal_line_atom_ledger_closed']}")
    print(
        "selected_terminal_line_atom_edge_mass="
        f"{audit_result['selected_terminal_line_atom_edge_mass']}"
    )
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
