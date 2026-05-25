#!/usr/bin/env python3
"""审计 affine skeleton 所在的 right-tail shell-step packet enclosure。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_affine_skeleton_packet_enclosure_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-affine-skeleton-packet-enclosure-audit.json

上一层把两个 occurrence splices 压成一个共享 witness-pair 仿射骨架。本层继续
下钻：把该 witness-pair 嵌回它实际所在的 right-tail shell-step packets，
检查 q-window、m-shell、终端 m-pair rank 与额外支撑点。该层仍只是有限包络
账本，不生成 trace/Kloosterman 可求和族。
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit as shell_step  # noqa: E402


SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-affine-skeleton-packet-enclosure"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

AFFINE_SKELETON_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-affine-skeleton-audit.json"
)
SHELL_STEP_PACKET_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json"
)

DEPENDENCIES = [
    AFFINE_SKELETON_AUDIT,
    SHELL_STEP_PACKET_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
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


def primes_in_interval(primes: list[int], start: int, end: int) -> list[int]:
    """取闭区间内素数。"""
    return [prime for prime in primes if start <= prime <= end]


def packet_m_values(packet: dict[str, Any], primes: list[int]) -> list[int]:
    """按 source rectangles 取 packet 的 m-shell 素数支撑。"""
    values: list[int] = []
    for rect in packet["source_rectangles"]:
        values.extend(primes_in_interval(primes, rect["m_start"], rect["m_end"]))
    return sorted(set(values))


def rank_values(values: list[int], selected: list[int]) -> list[int]:
    """返回 selected 在 values 中的 1-based rank。"""
    return [values.index(item) + 1 for item in selected]


def packet_profile(
    packet_index: int,
    packet: dict[str, Any],
    selected_m_pair: list[int],
    primes: list[int],
) -> dict[str, Any]:
    """构造 shell-step packet 包络 profile。"""
    q_values = primes_in_interval(primes, packet["q_start"], packet["q_end"])
    m_values = packet_m_values(packet, primes)
    selected_ranks = rank_values(m_values, selected_m_pair)
    selected_set = set(selected_m_pair)
    return {
        "packet_index": packet_index,
        "P": packet["P"],
        "strip": packet["strip"],
        "q_start": packet["q_start"],
        "q_end": packet["q_end"],
        "q_values": q_values,
        "q_prefix_count": packet["q_prefix_count"],
        "q_prefix_count_recomputed": len(q_values),
        "q_prefix_contiguous": len(q_values) == packet["q_prefix_count"],
        "m_start": packet["m_start"],
        "m_end": packet["m_end"],
        "m_values": m_values,
        "m_offsets_from_P": [m_value - packet["P"] for m_value in m_values],
        "m_shell_prime_count": packet["m_shell_prime_count"],
        "m_shell_prime_count_recomputed": len(m_values),
        "m_block_count": packet["m_block_count"],
        "internal_prime_gap_count": packet["internal_prime_gap_count"],
        "edge_count": packet["edge_count"],
        "source_rectangle_count": packet["source_rectangle_count"],
        "source_rectangles": packet["source_rectangles"],
        "selected_m_pair": selected_m_pair,
        "selected_m_pair_ranks": selected_ranks,
        "selected_m_pair_terminal": selected_ranks == [len(m_values) - 1, len(m_values)],
        "selected_m_pair_width": selected_m_pair[1] - selected_m_pair[0],
        "extra_m_values": [m_value for m_value in m_values if m_value not in selected_set],
        "extra_m_offsets_from_P": [
            m_value - packet["P"] for m_value in m_values if m_value not in selected_set
        ],
        "selected_pair_inside_packet": all(m_value in m_values for m_value in selected_m_pair),
    }


def build_pair_profile(affine_row: dict[str, Any], packets: list[dict[str, Any]], primes: list[int]) -> dict[str, Any]:
    """把一个 affine row 嵌入 left/right shell-step packets。"""
    left_packet = packets[affine_row["left_packet"]]
    right_packet = packets[affine_row["right_packet"]]
    left_selected = [int(item) for item in json.loads(affine_row["left_m_pair"])]
    right_selected = [int(item) for item in json.loads(affine_row["right_m_pair"])]
    left = packet_profile(affine_row["left_packet"], left_packet, left_selected, primes)
    right = packet_profile(affine_row["right_packet"], right_packet, right_selected, primes)
    q_intersection = sorted(set(left["q_values"]) & set(right["q_values"]))
    m_intersection = sorted(set(left["m_values"]) & set(right["m_values"]))
    return {
        "splice_id": affine_row["splice_id"],
        "signed_atom": affine_row["signed_atom"],
        "left_packet_profile": left,
        "right_packet_profile": right,
        "q_window_delta": [right["q_start"] - left["q_start"], right["q_end"] - left["q_end"]],
        "q_prefix_count_delta": right["q_prefix_count"] - left["q_prefix_count"],
        "q_prefix_count_ratio": f"{right['q_prefix_count']}/{left['q_prefix_count']}",
        "q_windows_disjoint": len(q_intersection) == 0,
        "right_q_window_strictly_left_of_left": right["q_end"] < left["q_start"],
        "q_window_intersection": q_intersection,
        "m_shell_prime_count_delta": right["m_shell_prime_count"] - left["m_shell_prime_count"],
        "edge_count_delta": right["edge_count"] - left["edge_count"],
        "edge_count_ratio": f"{right['edge_count']}/{left['edge_count']}",
        "m_shell_intersection": m_intersection,
        "m_shells_disjoint": len(m_intersection) == 0,
        "both_selected_pairs_terminal": left["selected_m_pair_terminal"]
        and right["selected_m_pair_terminal"],
        "both_selected_pairs_inside_packets": left["selected_pair_inside_packet"]
        and right["selected_pair_inside_packet"],
        "both_packets_right_tail": left["strip"] == right["strip"] == "right_tail",
        "left_extra_m_value_count": len(left["extra_m_values"]),
        "right_extra_m_value_count": len(right["extra_m_values"]),
        "extra_m_total_count": len(left["extra_m_values"]) + len(right["extra_m_values"]),
    }


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """生成 packet enclosure 审计。"""
    affine_payload = load_json(AFFINE_SKELETON_AUDIT)
    shell_payload = load_json(SHELL_STEP_PACKET_AUDIT)
    affine_rows = affine_payload["finite_audit"]["affine_rows"]
    primes = primorial.prime_sieve(2 * max_prime + 10)
    packets = shell_step.packetize_rectangles(max_prime)
    pair_profiles = [build_pair_profile(row, packets, primes) for row in affine_rows]

    unique_left_packets = {profile["left_packet_profile"]["packet_index"] for profile in pair_profiles}
    unique_right_packets = {profile["right_packet_profile"]["packet_index"] for profile in pair_profiles}
    q_disjoint = all(profile["q_windows_disjoint"] for profile in pair_profiles)
    right_q_left = all(profile["right_q_window_strictly_left_of_left"] for profile in pair_profiles)
    m_disjoint = all(profile["m_shells_disjoint"] for profile in pair_profiles)
    selected_terminal = all(profile["both_selected_pairs_terminal"] for profile in pair_profiles)
    selected_inside = all(profile["both_selected_pairs_inside_packets"] for profile in pair_profiles)
    packet_identity = (
        shell_payload["finite_audit"]["packet_identity_verified"]
        and len(packets) == shell_payload["finite_audit"]["shell_step_packet_count_total"]
    )

    enclosure_closed = (
        affine_payload["shared_witness_pair_affine_skeleton_ledger_closed"]
        and packet_identity
        and len(pair_profiles) == 2
        and unique_left_packets == {2842}
        and unique_right_packets == {1887}
        and all(profile["both_packets_right_tail"] for profile in pair_profiles)
        and all(profile["left_packet_profile"]["q_prefix_count"] == 28 for profile in pair_profiles)
        and all(profile["right_packet_profile"]["q_prefix_count"] == 7 for profile in pair_profiles)
        and all(profile["left_packet_profile"]["m_shell_prime_count"] == 4 for profile in pair_profiles)
        and all(profile["right_packet_profile"]["m_shell_prime_count"] == 3 for profile in pair_profiles)
        and q_disjoint
        and right_q_left
        and m_disjoint
        and selected_terminal
        and selected_inside
    )

    return {
        "max_prime": max_prime,
        "previous_affine_skeleton_ledger_closed": affine_payload[
            "shared_witness_pair_affine_skeleton_ledger_closed"
        ],
        "previous_shell_step_packet_identity_verified": shell_payload["finite_audit"][
            "packet_identity_verified"
        ],
        "packet_enclosure_ledger_closed": enclosure_closed,
        "splice_count": len(pair_profiles),
        "unique_left_packet_indices": sorted(unique_left_packets),
        "unique_right_packet_indices": sorted(unique_right_packets),
        "left_packet_index": 2842,
        "right_packet_index": 1887,
        "left_q_prefix_count": pair_profiles[0]["left_packet_profile"]["q_prefix_count"],
        "right_q_prefix_count": pair_profiles[0]["right_packet_profile"]["q_prefix_count"],
        "q_prefix_count_delta": pair_profiles[0]["q_prefix_count_delta"],
        "q_prefix_count_ratio": pair_profiles[0]["q_prefix_count_ratio"],
        "left_m_shell_prime_count": pair_profiles[0]["left_packet_profile"]["m_shell_prime_count"],
        "right_m_shell_prime_count": pair_profiles[0]["right_packet_profile"]["m_shell_prime_count"],
        "m_shell_prime_count_delta": pair_profiles[0]["m_shell_prime_count_delta"],
        "left_edge_count": pair_profiles[0]["left_packet_profile"]["edge_count"],
        "right_edge_count": pair_profiles[0]["right_packet_profile"]["edge_count"],
        "edge_count_delta": pair_profiles[0]["edge_count_delta"],
        "edge_count_ratio": pair_profiles[0]["edge_count_ratio"],
        "all_q_windows_disjoint": q_disjoint,
        "all_right_q_windows_strictly_left_of_left": right_q_left,
        "all_m_shells_disjoint": m_disjoint,
        "all_selected_pairs_terminal": selected_terminal,
        "all_selected_pairs_inside_packets": selected_inside,
        "all_packets_right_tail": all(profile["both_packets_right_tail"] for profile in pair_profiles),
        "packet_pair_profiles": pair_profiles,
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "packet_enclosure_uniform_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    affine_payload = load_json(AFFINE_SKELETON_AUDIT)
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_affine_skeleton_packet_enclosure_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "packet_enclosure_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the shared affine skeleton must be embedded in its actual q-window/m-shell packets before any summation theorem can apply",
        "current_object": {
            "input": "the shared P739-to-P607 witness-pair affine skeleton",
            "operation": "embed the selected m-pairs in their shell-step packet q-windows and m-shell supports",
            "dominant_shape": "P739 packet2842 q-window [541,709] with 28 q-primes to P607 packet1887 q-window [439,467] with 7 q-primes",
            "remaining": "convert this asymmetric right-tail packet enclosure into a summable family or a PDEC/SAE certificate",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "SharedAffineSkeletonImported",
                finite_audit["previous_affine_skeleton_ledger_closed"],
                finite_audit["previous_affine_skeleton_ledger_closed"],
                "The shared witness-pair affine skeleton is imported.",
                "none for import",
            ),
            gate(
                "ShellStepPacketIdentityImported",
                finite_audit["previous_shell_step_packet_identity_verified"],
                finite_audit["previous_shell_step_packet_identity_verified"],
                "The boundary shell-step packet identity is imported.",
                "none for import",
            ),
            gate(
                "PacketEnclosureLedger",
                finite_audit["packet_enclosure_ledger_closed"],
                finite_audit["packet_enclosure_ledger_closed"],
                "The affine skeleton is enclosed in packet2842 and packet1887 with exact q-window and m-shell support.",
                "none for the finite packet enclosure",
            ),
            gate(
                "PacketEnclosureUniformBound",
                False,
                False,
                "Control the asymmetric right-tail packet enclosure uniformly.",
                "finite enclosure data still has disjoint q-windows and no completed summable family",
            ),
        ],
        "external_sources_consulted": affine_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "the packets expose q-windows, but they are two fixed disjoint prime-q prefixes rather than a completed bilinear family",
            "short_interval_prime_inputs": "Li's x^0.52 theorem gives prime existence, not cancellation across this fixed packet enclosure",
            "prime_gap_inputs": "Maynard-type gap inputs do not control the q-window/m-shell enclosure of a signed Phi-LPF packet",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepAffineSkeletonPacketEnclosureUniformBound(packet2842:[q=541..709,m={719,751,757,761}] -> packet1887:[q=439..467,m={479,769,773}])",
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
        "packet_enclosure_ledger_closed": finite_audit["packet_enclosure_ledger_closed"],
        "packet_enclosure_uniform_bound_proved": False,
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
    profile_rows = []
    for profile in audit_result["packet_pair_profiles"]:
        left = profile["left_packet_profile"]
        right = profile["right_packet_profile"]
        profile_rows.append(
            {
                "splice_id": profile["splice_id"],
                "signed_atom": profile["signed_atom"],
                "left_packet": left["packet_index"],
                "right_packet": right["packet_index"],
                "left_q_window": f"[{left['q_start']},{left['q_end']}]",
                "right_q_window": f"[{right['q_start']},{right['q_end']}]",
                "q_prefix_count_delta": profile["q_prefix_count_delta"],
                "left_m_values": left["m_values"],
                "right_m_values": right["m_values"],
                "m_shell_prime_count_delta": profile["m_shell_prime_count_delta"],
                "selected_terminal": profile["both_selected_pairs_terminal"],
            }
        )

    lines = [
        "# Prime Matrix Phi-LPF repeated-step affine-skeleton packet enclosure 审计",
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
        "## 2. packet enclosure 审计",
        "",
        "```text",
        f"packet_enclosure_ledger_closed={str(audit_result['packet_enclosure_ledger_closed']).lower()}",
        f"splice_count={audit_result['splice_count']}",
        f"unique_left_packet_indices={audit_result['unique_left_packet_indices']}",
        f"unique_right_packet_indices={audit_result['unique_right_packet_indices']}",
        f"left_q_prefix_count={audit_result['left_q_prefix_count']}",
        f"right_q_prefix_count={audit_result['right_q_prefix_count']}",
        f"q_prefix_count_delta={audit_result['q_prefix_count_delta']}",
        f"q_prefix_count_ratio={audit_result['q_prefix_count_ratio']}",
        f"left_m_shell_prime_count={audit_result['left_m_shell_prime_count']}",
        f"right_m_shell_prime_count={audit_result['right_m_shell_prime_count']}",
        f"m_shell_prime_count_delta={audit_result['m_shell_prime_count_delta']}",
        f"left_edge_count={audit_result['left_edge_count']}",
        f"right_edge_count={audit_result['right_edge_count']}",
        f"edge_count_delta={audit_result['edge_count_delta']}",
        f"edge_count_ratio={audit_result['edge_count_ratio']}",
        f"all_q_windows_disjoint={str(audit_result['all_q_windows_disjoint']).lower()}",
        f"all_right_q_windows_strictly_left_of_left={str(audit_result['all_right_q_windows_strictly_left_of_left']).lower()}",
        f"all_m_shells_disjoint={str(audit_result['all_m_shells_disjoint']).lower()}",
        f"all_selected_pairs_terminal={str(audit_result['all_selected_pairs_terminal']).lower()}",
        f"all_selected_pairs_inside_packets={str(audit_result['all_selected_pairs_inside_packets']).lower()}",
        f"packet_enclosure_uniform_bound_proved={str(audit_result['packet_enclosure_uniform_bound_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "packet pair rows：",
        "",
        *markdown_table(
            profile_rows,
            [
                "splice_id",
                "signed_atom",
                "left_packet",
                "right_packet",
                "left_q_window",
                "right_q_window",
                "q_prefix_count_delta",
                "left_m_values",
                "right_m_values",
                "m_shell_prime_count_delta",
                "selected_terminal",
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
        "结论：共享 affine skeleton 已嵌入两个具体 right-tail shell-step packets。",
        "两个 q-window 不相交，两个 m-shell 也不相交；所选 m-pair 都是各自 packet 的终端 pair。",
        "这定位了下一硬点，但仍没有形成可调用 trace/Kloosterman 平均定理的可求和族。",
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
        f"packet_enclosure_ledger_closed={str(payload['packet_enclosure_ledger_closed']).lower()}",
        f"packet_enclosure_uniform_bound_proved={str(payload['packet_enclosure_uniform_bound_proved']).lower()}",
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
    print(f"packet_enclosure_ledger_closed={payload['packet_enclosure_ledger_closed']}")
    print(f"left_packet_index={audit_result['left_packet_index']}")
    print(f"right_packet_index={audit_result['right_packet_index']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
