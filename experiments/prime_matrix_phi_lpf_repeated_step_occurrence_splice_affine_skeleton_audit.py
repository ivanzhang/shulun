#!/usr/bin/env python3
"""审计 repeated-step occurrence splice 的共享 witness-pair 仿射骨架。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_occurrence_splice_affine_skeleton_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-affine-skeleton-audit.json

上一层已经把两个 repeated-node P-switch cut 定位为 two same-signed-atom
cross-witness occurrence splices。本层继续下钻：检查这两条 splice 是否其实
来自同一个 left/right witness pair，以及它们共享的 P/q/m/packet/offset 仿射
差分。它仍不是 uniform family bound。
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-affine-skeleton"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

OCCURRENCE_SPLICE_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-audit.json"
)
M_PAIR_COORDINATE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition-audit.json"
)

DEPENDENCIES = [
    OCCURRENCE_SPLICE_AUDIT,
    M_PAIR_COORDINATE_AUDIT,
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


def parse_pair(text: str) -> tuple[int, int]:
    """解析形如 [757, 761] 的二元组。"""
    values = [int(item) for item in re.findall(r"-?\d+", text)]
    if len(values) != 2:
        raise ValueError(f"bad pair: {text}")
    return values[0], values[1]


def parse_packet(witness_id: str) -> int:
    """从 witness id 中解析 packet index。"""
    match = re.search(r"_packet(\d+)_", witness_id)
    if not match:
        raise ValueError(f"bad witness_id: {witness_id}")
    return int(match.group(1))


def fraction_text(value: Fraction) -> str:
    """输出稳定的分数字符串。"""
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def counter_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total if total else 0.0}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def witness_map(coordinate_payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按 witness_id 建立坐标 witness 查找表。"""
    rows = coordinate_payload["finite_audit"]["endpoint_coordinate_witness_rows"]
    return {row["witness_id"]: row for row in rows}


def midpoint_numerator(pair: tuple[int, int]) -> int:
    """返回中点的二倍，避免浮点误差。"""
    return pair[0] + pair[1]


def build_affine_rows(
    splice_rows: list[dict[str, Any]],
    witnesses: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成每条 splice 的仿射差分记录。"""
    rows: list[dict[str, Any]] = []
    for row in splice_rows:
        left = witnesses[row["left_witness_id"]]
        right = witnesses[row["right_witness_id"]]
        left_pair = parse_pair(left["m_pair"])
        right_pair = parse_pair(right["m_pair"])
        left_offsets = left["m_offsets_from_P"]
        right_offsets = right["m_offsets_from_P"]
        m_delta = [right_pair[0] - left_pair[0], right_pair[1] - left_pair[1]]
        offset_delta = [
            right_offsets[0] - left_offsets[0],
            right_offsets[1] - left_offsets[1],
        ]
        p_delta = right["P"] - left["P"]
        q_delta = right["q_prefix_count"] - left["q_prefix_count"]
        packet_delta = right["packet_index"] - left["packet_index"]
        midpoint_delta = Fraction(midpoint_numerator(right_pair) - midpoint_numerator(left_pair), 2)
        width_left = left_pair[1] - left_pair[0]
        width_right = right_pair[1] - right_pair[0]
        offset_identity_delta = [m_delta[0] - p_delta, m_delta[1] - p_delta]
        left_path_steps = {item["step"]: item for item in left["signed_coordinate_path"]}
        right_path_steps = {item["step"]: item for item in right["signed_coordinate_path"]}
        left_step = left_path_steps[row["left_step"]]
        right_step = right_path_steps[row["right_step"]]

        rows.append(
            {
                "splice_id": row["splice_id"],
                "signed_atom": row["signed_atom"],
                "left_witness_id": row["left_witness_id"],
                "right_witness_id": row["right_witness_id"],
                "witness_pair_key": f"{row['left_witness_id']} -> {row['right_witness_id']}",
                "left_P": left["P"],
                "right_P": right["P"],
                "P_delta": p_delta,
                "left_q": left["q_prefix_count"],
                "right_q": right["q_prefix_count"],
                "q_delta": q_delta,
                "left_packet": left["packet_index"],
                "right_packet": right["packet_index"],
                "packet_delta": packet_delta,
                "left_m_pair": left["m_pair"],
                "right_m_pair": right["m_pair"],
                "m_pair_delta": m_delta,
                "m_midpoint_delta": fraction_text(midpoint_delta),
                "m_width_left": width_left,
                "m_width_right": width_right,
                "m_width_preserved": width_left == width_right,
                "left_offsets_from_P": left_offsets,
                "right_offsets_from_P": right_offsets,
                "offset_delta": offset_delta,
                "offset_delta_equals_m_delta_minus_P_delta": offset_delta == offset_identity_delta,
                "left_orientation": left["endpoint_orientation"],
                "right_orientation": right["endpoint_orientation"],
                "orientation_preserved": left["endpoint_orientation"] == right["endpoint_orientation"],
                "left_step": row["left_step"],
                "right_step": row["right_step"],
                "step_delta": row["step_delta"],
                "step_rewind_amount": row["step_rewind_amount"],
                "left_path_gap_carry_sign": (
                    left_step["gap"],
                    left_step["carry"],
                    left_step["sign"],
                ),
                "right_path_gap_carry_sign": (
                    right_step["gap"],
                    right_step["carry"],
                    right_step["sign"],
                ),
                "same_atom_step_coordinates": (
                    left_step["gap"] == right_step["gap"] == row["gap"]
                    and left_step["carry"] == right_step["carry"] == row["carry"]
                    and left_step["sign"] == right_step["sign"] == row["sign"]
                ),
                "splice_occurrence_mass": row["splice_occurrence_mass"],
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """生成共享 witness-pair 仿射骨架审计。"""
    occurrence_payload = load_json(OCCURRENCE_SPLICE_AUDIT)
    coordinate_payload = load_json(M_PAIR_COORDINATE_AUDIT)
    finite_occurrence = occurrence_payload["finite_audit"]
    witnesses = witness_map(coordinate_payload)
    affine_rows = build_affine_rows(finite_occurrence["splice_rows"], witnesses)

    total_mass = sum(row["splice_occurrence_mass"] for row in affine_rows)
    witness_pair_counter: Counter[str] = Counter()
    p_delta_counter: Counter[int] = Counter()
    q_delta_counter: Counter[int] = Counter()
    packet_delta_counter: Counter[int] = Counter()
    offset_delta_counter: Counter[str] = Counter()
    step_delta_counter: Counter[int] = Counter()
    signed_atom_counter: Counter[str] = Counter()
    for row in affine_rows:
        mass = row["splice_occurrence_mass"]
        witness_pair_counter[row["witness_pair_key"]] += mass
        p_delta_counter[row["P_delta"]] += mass
        q_delta_counter[row["q_delta"]] += mass
        packet_delta_counter[row["packet_delta"]] += mass
        offset_delta_counter[str(row["offset_delta"])] += mass
        step_delta_counter[row["step_delta"]] += mass
        signed_atom_counter[row["signed_atom"]] += mass

    distinct_witness_pairs = {row["witness_pair_key"] for row in affine_rows}
    shared_witness_pair = len(distinct_witness_pairs) == 1
    all_same_affine_deltas = (
        len({row["P_delta"] for row in affine_rows}) == 1
        and len({row["q_delta"] for row in affine_rows}) == 1
        and len({row["packet_delta"] for row in affine_rows}) == 1
        and len({str(row["m_pair_delta"]) for row in affine_rows}) == 1
        and len({str(row["offset_delta"]) for row in affine_rows}) == 1
    )
    affine_identity_closed = all(
        row["offset_delta_equals_m_delta_minus_P_delta"] for row in affine_rows
    )
    coordinate_atom_closed = all(row["same_atom_step_coordinates"] for row in affine_rows)
    ledger_closed = (
        occurrence_payload["repeated_step_occurrence_splice_ledger_closed"]
        and len(affine_rows) == 2
        and total_mass == 40
        and shared_witness_pair
        and all_same_affine_deltas
        and affine_identity_closed
        and coordinate_atom_closed
        and all(row["m_width_preserved"] for row in affine_rows)
        and all(row["orientation_preserved"] for row in affine_rows)
    )

    return {
        "target_sign_word": TARGET_SIGN_WORD,
        "previous_occurrence_splice_ledger_closed": occurrence_payload[
            "repeated_step_occurrence_splice_ledger_closed"
        ],
        "shared_witness_pair_affine_skeleton_ledger_closed": ledger_closed,
        "splice_count": len(affine_rows),
        "splice_mass_total": total_mass,
        "distinct_witness_pair_count": len(distinct_witness_pairs),
        "shared_witness_pair": shared_witness_pair,
        "all_same_affine_deltas": all_same_affine_deltas,
        "affine_identity_offset_delta_equals_m_delta_minus_P_delta": affine_identity_closed,
        "coordinate_atom_recheck_closed": coordinate_atom_closed,
        "all_width_preserved": all(row["m_width_preserved"] for row in affine_rows),
        "all_orientation_preserved": all(row["orientation_preserved"] for row in affine_rows),
        "affine_rows": affine_rows,
        "witness_pair_rows": counter_rows(witness_pair_counter, total_mass, "witness_pair_key"),
        "p_delta_rows": counter_rows(p_delta_counter, total_mass, "P_delta"),
        "q_delta_rows": counter_rows(q_delta_counter, total_mass, "q_delta"),
        "packet_delta_rows": counter_rows(packet_delta_counter, total_mass, "packet_delta"),
        "offset_delta_rows": counter_rows(offset_delta_counter, total_mass, "offset_delta"),
        "step_delta_rows": counter_rows(step_delta_counter, total_mass, "step_delta"),
        "signed_atom_rows": counter_rows(signed_atom_counter, total_mass, "signed_atom"),
        "summable_family_created": False,
        "trace_or_kloosterman_completion_ready": False,
        "shared_witness_pair_affine_skeleton_uniform_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    occurrence_payload = load_json(OCCURRENCE_SPLICE_AUDIT)
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_occurrence_splice_affine_skeleton_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "shared_witness_pair_affine_skeleton_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the two occurrence splices collapse to one shared left/right witness pair with fixed affine deltas",
        "current_object": {
            "input": "the two same-atom P739-to-P607 occurrence splices",
            "operation": "resolve their shared witness pair and affine P/q/m/offset/packet skeleton",
            "dominant_shape": "one witness-pair skeleton P739/q28/[757,761]/packet2842 -> P607/q7/[769,773]/packet1887",
            "remaining": "turn the one-pair skeleton into a uniform family bound or a PDEC/SAE certificate",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "OccurrenceSpliceImported",
                finite_audit["previous_occurrence_splice_ledger_closed"],
                finite_audit["previous_occurrence_splice_ledger_closed"],
                "The same-atom occurrence-splice ledger is imported.",
                "none for import",
            ),
            gate(
                "SharedWitnessPairAffineSkeletonLedger",
                finite_audit["shared_witness_pair_affine_skeleton_ledger_closed"],
                finite_audit["shared_witness_pair_affine_skeleton_ledger_closed"],
                "Both occurrence splices use the same left/right witness pair and the same affine deltas.",
                "none for the finite affine skeleton ledger",
            ),
            gate(
                "AffineOffsetIdentity",
                finite_audit["affine_identity_offset_delta_equals_m_delta_minus_P_delta"],
                finite_audit["affine_identity_offset_delta_equals_m_delta_minus_P_delta"],
                "For each endpoint, offset_delta equals m_delta minus P_delta.",
                "none for this finite identity",
            ),
            gate(
                "SummableFamilyCreated",
                False,
                False,
                "Promote the one witness-pair skeleton to a summable trace/Kloosterman family.",
                "the present ledger has one witness pair, not a completed family",
            ),
            gate(
                "SharedWitnessPairAffineSkeletonUniformBound",
                False,
                False,
                "Control the P739/q28 to P607/q7 affine skeleton uniformly.",
                "finite affine localization gives exact data but no global theorem",
            ),
        ],
        "external_sources_consulted": occurrence_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "FKMS, Milićević-Qin-Wu and Wright become relevant only after this one-pair skeleton is embedded into a summable family",
            "short_interval_prime_inputs": "Li's x^0.52 short-interval existence theorem does not bound a fixed cross-witness affine skeleton",
            "prime_gap_inputs": "Maynard-type bounded gap inputs do not control the local P/q/m/packet affine splice",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepSharedWitnessPairAffineSkeletonUniformBound(P739/q28/[757,761]/packet2842 -> P607/q7/[769,773]/packet1887)",
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
        "shared_witness_pair_affine_skeleton_ledger_closed": finite_audit[
            "shared_witness_pair_affine_skeleton_ledger_closed"
        ],
        "shared_witness_pair_affine_skeleton_uniform_bound_proved": False,
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
    lines = [
        "# Prime Matrix Phi-LPF repeated-step occurrence-splice affine skeleton 审计",
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
        "## 2. 仿射骨架审计",
        "",
        "```text",
        f"previous_occurrence_splice_ledger_closed={str(audit_result['previous_occurrence_splice_ledger_closed']).lower()}",
        f"shared_witness_pair_affine_skeleton_ledger_closed={str(audit_result['shared_witness_pair_affine_skeleton_ledger_closed']).lower()}",
        f"splice_count={audit_result['splice_count']}",
        f"splice_mass_total={audit_result['splice_mass_total']}",
        f"distinct_witness_pair_count={audit_result['distinct_witness_pair_count']}",
        f"shared_witness_pair={str(audit_result['shared_witness_pair']).lower()}",
        f"all_same_affine_deltas={str(audit_result['all_same_affine_deltas']).lower()}",
        f"affine_identity_offset_delta_equals_m_delta_minus_P_delta={str(audit_result['affine_identity_offset_delta_equals_m_delta_minus_P_delta']).lower()}",
        f"coordinate_atom_recheck_closed={str(audit_result['coordinate_atom_recheck_closed']).lower()}",
        f"summable_family_created={str(audit_result['summable_family_created']).lower()}",
        f"trace_or_kloosterman_completion_ready={str(audit_result['trace_or_kloosterman_completion_ready']).lower()}",
        f"shared_witness_pair_affine_skeleton_uniform_bound_proved={str(audit_result['shared_witness_pair_affine_skeleton_uniform_bound_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "summary rows：",
        "",
        *markdown_table(audit_result["witness_pair_rows"], ["witness_pair_key", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["p_delta_rows"], ["P_delta", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["q_delta_rows"], ["q_delta", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["packet_delta_rows"], ["packet_delta", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["offset_delta_rows"], ["offset_delta", "mass", "ratio"]),
        "",
        "affine rows：",
        "",
        *markdown_table(
            audit_result["affine_rows"],
            [
                "splice_id",
                "signed_atom",
                "left_P",
                "right_P",
                "P_delta",
                "left_q",
                "right_q",
                "q_delta",
                "left_packet",
                "right_packet",
                "packet_delta",
                "left_m_pair",
                "right_m_pair",
                "m_pair_delta",
                "offset_delta",
                "left_step",
                "right_step",
                "step_delta",
                "splice_occurrence_mass",
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
        "结论：两条 occurrence splice 不是两个独立 witness-pair；它们共享同一",
        "left/right witness pair，并且所有 P/q/m/offset/packet 仿射差分一致。",
        "这进一步压缩了有限对象，但仍没有生成可求和族，因此不能调用",
        "trace/Kloosterman 平均定理来闭合全局命题。",
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
        f"shared_witness_pair_affine_skeleton_ledger_closed={str(payload['shared_witness_pair_affine_skeleton_ledger_closed']).lower()}",
        f"shared_witness_pair_affine_skeleton_uniform_bound_proved={str(payload['shared_witness_pair_affine_skeleton_uniform_bound_proved']).lower()}",
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
    print(
        "shared_witness_pair_affine_skeleton_ledger_closed="
        f"{payload['shared_witness_pair_affine_skeleton_ledger_closed']}"
    )
    print(f"distinct_witness_pair_count={audit_result['distinct_witness_pair_count']}")
    print(f"all_same_affine_deltas={audit_result['all_same_affine_deltas']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
