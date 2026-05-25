#!/usr/bin/env python3
"""审计 repeated-node P-switch cut 的 occurrence splice。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_occurrence_splice_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-audit.json

上一层把 mixed-P source-sink path 的 P-switch 定位到两个 repeated nodes。本层
继续原子化：每个 switch cut 都是在同一个 signed atom 上，把 P=739 的 occurrence
splice 到 P=607 的 occurrence；它仍不是 uniform family bound。
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

PREVIOUS_P_SWITCH_CUT_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-p-switch-cut-audit.json"
)
DIRECTED_GRAPH_AUDIT = (
    DOCS / "prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-audit.json"
)
REPEATED_STEP_OCCURRENCE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-occurrence-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_P_SWITCH_CUT_AUDIT,
    DIRECTED_GRAPH_AUDIT,
    REPEATED_STEP_OCCURRENCE_AUDIT,
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


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def load_json(path: Path) -> dict[str, Any]:
    """读入 JSON 证书。"""
    return json.loads(path.read_text())


def edge_key(row: dict[str, Any]) -> str:
    """生成有向边键。"""
    return f"{row['from_atom']} -> {row['to_atom']}"


def occurrence_lookup_key(atom: str, p_value: int, step: int, m_pair: str) -> str:
    """生成 occurrence 查找键。"""
    return f"{atom}|P{p_value}|step{step}|{m_pair}"


def parse_m_pair(m_pair: str) -> tuple[int, int]:
    """解析形如 [757, 761] 的 m-pair。"""
    values = [int(item) for item in re.findall(r"-?\d+", m_pair)]
    if len(values) != 2:
        raise ValueError(f"bad m_pair: {m_pair}")
    return values[0], values[1]


def parse_q(witness_id: str) -> int | None:
    """从 witness id 中解析 q。"""
    match = re.search(r"_q(\d+)_", witness_id)
    return int(match.group(1)) if match else None


def p_transition(left_p: int, right_p: int) -> str:
    """生成 P-transition 标签。"""
    return f"{left_p}_to_{right_p}"


def counter_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total if total else 0.0}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def endpoint_occurrence_for_edge(
    switch_node: str,
    edge: dict[str, Any],
    occurrence_map: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """找到 switch edge 在 switch node 端点上的 occurrence。"""
    if edge["to_atom"] == switch_node:
        step = edge["to_step"]
    elif edge["from_atom"] == switch_node:
        step = edge["from_step"]
    else:
        raise ValueError(f"edge does not touch switch node: {edge_key(edge)}")
    key = occurrence_lookup_key(switch_node, edge["P"], step, edge["m_pair"])
    return occurrence_map[key]


def step_splice_kind(left_step: int, right_step: int) -> str:
    """标记 step splice 的方向。"""
    if right_step < left_step:
        return "rewind"
    if right_step > left_step:
        return "forward"
    return "same_slot"


def build_splice_rows(
    switch_rows: list[dict[str, Any]],
    edge_map: dict[str, dict[str, Any]],
    occurrence_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """把 P-switch cut 转成 occurrence splice rows。"""
    rows: list[dict[str, Any]] = []
    for row in switch_rows:
        switch_node = row["switch_node"]
        left_edge = edge_map[row["left_edge_key"]]
        right_edge = edge_map[row["right_edge_key"]]
        left_occ = endpoint_occurrence_for_edge(switch_node, left_edge, occurrence_map)
        right_occ = endpoint_occurrence_for_edge(switch_node, right_edge, occurrence_map)

        left_pair = parse_m_pair(left_occ["m_pair"])
        right_pair = parse_m_pair(right_occ["m_pair"])
        m_pair_delta = [right_pair[0] - left_pair[0], right_pair[1] - left_pair[1]]
        left_q = parse_q(left_occ["witness_id"])
        right_q = parse_q(right_occ["witness_id"])
        splice_mass = left_occ["occurrence_mass"] + right_occ["occurrence_mass"]
        step_delta = right_occ["step"] - left_occ["step"]

        rows.append(
            {
                "splice_id": row["switch_id"].replace("switch", "splice"),
                "source_switch_id": row["switch_id"],
                "path_id": row["path_id"],
                "switch_node": switch_node,
                "signed_atom": switch_node,
                "raw_step_signature": left_occ["raw_step_signature"],
                "sign": left_occ["sign"],
                "left_occurrence_key": left_occ["occurrence_key"],
                "right_occurrence_key": right_occ["occurrence_key"],
                "left_P": left_occ["P"],
                "right_P": right_occ["P"],
                "P_delta": right_occ["P"] - left_occ["P"],
                "P_transition": p_transition(left_occ["P"], right_occ["P"]),
                "left_witness_id": left_occ["witness_id"],
                "right_witness_id": right_occ["witness_id"],
                "left_q": left_q,
                "right_q": right_q,
                "q_delta": None if left_q is None or right_q is None else right_q - left_q,
                "left_m_pair": left_occ["m_pair"],
                "right_m_pair": right_occ["m_pair"],
                "m_pair_delta": m_pair_delta,
                "m_pair_width_preserved": (left_pair[1] - left_pair[0]) == (right_pair[1] - right_pair[0]),
                "left_step": left_occ["step"],
                "right_step": right_occ["step"],
                "step_delta": step_delta,
                "step_rewind_amount": -step_delta if step_delta < 0 else 0,
                "step_splice_kind": step_splice_kind(left_occ["step"], right_occ["step"]),
                "left_position_class": left_occ["position_class"],
                "right_position_class": right_occ["position_class"],
                "position_transition": f"{left_occ['position_class']}_to_{right_occ['position_class']}",
                "endpoint_orientation_preserved": left_occ["endpoint_orientation"]
                == right_occ["endpoint_orientation"],
                "same_signed_atom": left_occ["signed_step_signature"]
                == right_occ["signed_step_signature"]
                == switch_node,
                "same_gap_carry": left_occ["gap"] == right_occ["gap"]
                and left_occ["carry"] == right_occ["carry"],
                "same_sign": left_occ["sign"] == right_occ["sign"],
                "gap": left_occ["gap"],
                "carry": left_occ["carry"],
                "left_edge_key": row["left_edge_key"],
                "right_edge_key": row["right_edge_key"],
                "left_edge_class": row["left_edge_class"],
                "right_edge_class": row["right_edge_class"],
                "left_transition_role": row["left_transition_role"],
                "right_transition_role": row["right_transition_role"],
                "splice_occurrence_mass": splice_mass,
                "touches_repeated_bridge": row["touches_repeated_bridge"],
                "splice_signature": f"{left_occ['occurrence_key']} || {right_occ['occurrence_key']}",
            }
        )
    return rows


def build_occurrence_endpoint_rows(
    occurrence_rows: list[dict[str, Any]],
    splice_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """统计 occurrence 是否参与 splice。"""
    membership: Counter[str] = Counter()
    sides: dict[str, list[str]] = {}
    splice_ids: dict[str, list[str]] = {}
    for row in splice_rows:
        for side in ("left", "right"):
            key = row[f"{side}_occurrence_key"]
            membership[key] += 1
            sides.setdefault(key, []).append(side)
            splice_ids.setdefault(key, []).append(row["splice_id"])
    return [
        {
            "occurrence_key": row["occurrence_key"],
            "signed_step_signature": row["signed_step_signature"],
            "P": row["P"],
            "step": row["step"],
            "m_pair": row["m_pair"],
            "position_class": row["position_class"],
            "occurrence_mass": row["occurrence_mass"],
            "splice_membership_count": membership[row["occurrence_key"]],
            "splice_ids": splice_ids.get(row["occurrence_key"], []),
            "splice_sides": sides.get(row["occurrence_key"], []),
            "is_splice_endpoint": membership[row["occurrence_key"]] > 0,
        }
        for row in sorted(occurrence_rows, key=lambda item: (item["P"], item["step"]))
    ]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """生成 occurrence-splice 有限审计。"""
    switch_payload = load_json(PREVIOUS_P_SWITCH_CUT_AUDIT)
    graph_payload = load_json(DIRECTED_GRAPH_AUDIT)
    occurrence_payload = load_json(REPEATED_STEP_OCCURRENCE_AUDIT)

    switch_audit = switch_payload["finite_audit"]
    graph_audit = graph_payload["finite_audit"]
    occurrence_audit = occurrence_payload["finite_audit"]

    graph_edges = [row for row in graph_audit["directed_edge_rows"] if row["P"] <= max_prime]
    edge_map = {edge_key(row): row for row in graph_edges}
    occurrence_rows = [row for row in occurrence_audit["occurrence_rows"] if row["P"] <= max_prime]
    occurrence_map = {
        occurrence_lookup_key(row["signed_step_signature"], row["P"], row["step"], row["m_pair"]): row
        for row in occurrence_rows
    }
    splice_rows = build_splice_rows(switch_audit["switch_rows"], edge_map, occurrence_map)
    endpoint_rows = build_occurrence_endpoint_rows(occurrence_rows, splice_rows)

    total_splice_mass = sum(row["splice_occurrence_mass"] for row in splice_rows)
    p_transition_mass: Counter[str] = Counter()
    m_pair_delta_mass: Counter[str] = Counter()
    position_transition_mass: Counter[str] = Counter()
    step_splice_kind_mass: Counter[str] = Counter()
    q_delta_mass: Counter[str] = Counter()
    for row in splice_rows:
        mass = row["splice_occurrence_mass"]
        p_transition_mass[row["P_transition"]] += mass
        m_pair_delta_mass[str(row["m_pair_delta"])] += mass
        position_transition_mass[row["position_transition"]] += mass
        step_splice_kind_mass[row["step_splice_kind"]] += mass
        q_delta_mass[str(row["q_delta"])] += mass

    endpoint_cover_complete = all(row["is_splice_endpoint"] for row in endpoint_rows)
    endpoint_membership_total = sum(row["splice_membership_count"] for row in endpoint_rows)
    endpoint_mass_total = sum(
        row["occurrence_mass"] * row["splice_membership_count"] for row in endpoint_rows
    )
    step_rewind_total = sum(row["step_rewind_amount"] for row in splice_rows)

    ledger_closed = (
        switch_payload["repeated_step_p_switch_cut_ledger_closed"]
        and occurrence_payload["dominant_sign_word_repeated_step_occurrence_ledger_closed"]
        and len(splice_rows) == 2
        and all(row["same_signed_atom"] for row in splice_rows)
        and all(row["same_gap_carry"] for row in splice_rows)
        and all(row["same_sign"] for row in splice_rows)
        and all(row["endpoint_orientation_preserved"] for row in splice_rows)
        and all(row["P_transition"] == "739_to_607" for row in splice_rows)
        and all(row["m_pair_delta"] == [12, 12] for row in splice_rows)
        and all(row["m_pair_width_preserved"] for row in splice_rows)
        and all(row["q_delta"] == -21 for row in splice_rows)
        and all(row["step_splice_kind"] == "rewind" for row in splice_rows)
        and step_rewind_total == 5
        and total_splice_mass == 40
        and endpoint_cover_complete
        and endpoint_membership_total == 4
        and endpoint_mass_total == 40
    )

    return {
        "max_prime": max_prime,
        "target_sign_word": TARGET_SIGN_WORD,
        "previous_p_switch_cut_ledger_closed": switch_payload[
            "repeated_step_p_switch_cut_ledger_closed"
        ],
        "previous_repeated_step_occurrence_ledger_closed": occurrence_payload[
            "dominant_sign_word_repeated_step_occurrence_ledger_closed"
        ],
        "repeated_step_occurrence_splice_ledger_closed": ledger_closed,
        "occurrence_splice_count": len(splice_rows),
        "occurrence_splice_mass_total": total_splice_mass,
        "occurrence_splice_endpoint_count": endpoint_membership_total,
        "occurrence_splice_endpoint_mass": endpoint_mass_total,
        "occurrence_splice_endpoint_cover_complete": endpoint_cover_complete,
        "all_splices_same_signed_atom": all(row["same_signed_atom"] for row in splice_rows),
        "all_splices_same_gap_carry": all(row["same_gap_carry"] for row in splice_rows),
        "all_splices_same_sign": all(row["same_sign"] for row in splice_rows),
        "all_splices_same_orientation": all(
            row["endpoint_orientation_preserved"] for row in splice_rows
        ),
        "all_splices_739_to_607": all(row["P_transition"] == "739_to_607" for row in splice_rows),
        "all_splices_m_pair_delta_12_12": all(row["m_pair_delta"] == [12, 12] for row in splice_rows),
        "all_splices_q_delta_minus_21": all(row["q_delta"] == -21 for row in splice_rows),
        "all_splices_step_rewind": all(row["step_splice_kind"] == "rewind" for row in splice_rows),
        "step_rewind_total": step_rewind_total,
        "splice_rows": splice_rows,
        "occurrence_endpoint_rows": endpoint_rows,
        "p_transition_rows": counter_rows(p_transition_mass, total_splice_mass, "P_transition"),
        "m_pair_delta_rows": counter_rows(m_pair_delta_mass, total_splice_mass, "m_pair_delta"),
        "position_transition_rows": counter_rows(
            position_transition_mass, total_splice_mass, "position_transition"
        ),
        "step_splice_kind_rows": counter_rows(
            step_splice_kind_mass, total_splice_mass, "step_splice_kind"
        ),
        "q_delta_rows": counter_rows(q_delta_mass, total_splice_mass, "q_delta"),
        "occurrence_splice_uniform_family_bound_proved": False,
        "single_occurrence_orbit_repair_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    switch_payload = load_json(PREVIOUS_P_SWITCH_CUT_AUDIT)
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_dominant_sign_word_repeated_step_occurrence_splice_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "repeated_step_occurrence_splice_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the P-switch cut can be localized to a same-atom cross-witness occurrence splice",
        "current_object": {
            "input": "the two 739->607 repeated-node P-switch cuts",
            "operation": "identify the occurrence on each side of every switch cut",
            "dominant_shape": "two same-signed-atom occurrence splices from P739/[757,761] to P607/[769,773]",
            "remaining": "prove a uniform bound for same-atom cross-witness occurrence splices or replace them by PDEC/SAE certificates",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PSwitchCutImported",
                finite_audit["previous_p_switch_cut_ledger_closed"],
                finite_audit["previous_p_switch_cut_ledger_closed"],
                "The repeated-node P-switch cut ledger is imported.",
                "none for import",
            ),
            gate(
                "OccurrenceSpliceLedger",
                finite_audit["repeated_step_occurrence_splice_ledger_closed"],
                finite_audit["repeated_step_occurrence_splice_ledger_closed"],
                "Each P-switch cut is resolved into its left and right repeated-step occurrences.",
                "none for the finite occurrence-splice ledger",
            ),
            gate(
                "SameAtomCrossWitnessSpliceDetected",
                finite_audit["all_splices_same_signed_atom"],
                finite_audit["all_splices_same_signed_atom"],
                "Every splice keeps the same signed atom but changes P, q, m-pair and step slot.",
                "uniform proof must control cross-witness occurrence splices",
            ),
            gate(
                "OccurrenceSpliceUniformFamilyBound",
                False,
                False,
                "Control same-atom P739-to-P607 occurrence splices uniformly.",
                "finite occurrence-splice localization gives exact data but no global theorem",
            ),
        ],
        "external_sources_consulted": switch_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "the occurrence splice is still a two-witness local gluing datum, not a completed bilinear family",
            "prime_gap_inputs": "the splice keeps a signed atom but changes witness P/q/m-pair, so it is not a prime-gap existence statement",
            "short_interval_prime_inputs": "theta=0.52 does not control same-atom cross-witness occurrence splices",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepSameAtomOccurrenceSpliceUniformBound(two P739-to-P607 splices)",
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
            "AND Gap4RightTailLeftCollarCousinCollisionBound",
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
        "repeated_step_occurrence_splice_ledger_closed": finite_audit[
            "repeated_step_occurrence_splice_ledger_closed"
        ],
        "occurrence_splice_uniform_family_bound_proved": False,
        "single_occurrence_orbit_repair_proved": False,
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
        "# Prime Matrix Phi-LPF dominant-sign-word repeated-step occurrence splice 审计",
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
        "## 2. occurrence splice 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"repeated_step_occurrence_splice_ledger_closed={str(audit_result['repeated_step_occurrence_splice_ledger_closed']).lower()}",
        f"occurrence_splice_count={audit_result['occurrence_splice_count']}",
        f"occurrence_splice_mass_total={audit_result['occurrence_splice_mass_total']}",
        f"occurrence_splice_endpoint_count={audit_result['occurrence_splice_endpoint_count']}",
        f"occurrence_splice_endpoint_mass={audit_result['occurrence_splice_endpoint_mass']}",
        f"occurrence_splice_endpoint_cover_complete={str(audit_result['occurrence_splice_endpoint_cover_complete']).lower()}",
        f"all_splices_same_signed_atom={str(audit_result['all_splices_same_signed_atom']).lower()}",
        f"all_splices_same_gap_carry={str(audit_result['all_splices_same_gap_carry']).lower()}",
        f"all_splices_same_sign={str(audit_result['all_splices_same_sign']).lower()}",
        f"all_splices_same_orientation={str(audit_result['all_splices_same_orientation']).lower()}",
        f"all_splices_739_to_607={str(audit_result['all_splices_739_to_607']).lower()}",
        f"all_splices_m_pair_delta_12_12={str(audit_result['all_splices_m_pair_delta_12_12']).lower()}",
        f"all_splices_q_delta_minus_21={str(audit_result['all_splices_q_delta_minus_21']).lower()}",
        f"all_splices_step_rewind={str(audit_result['all_splices_step_rewind']).lower()}",
        f"step_rewind_total={audit_result['step_rewind_total']}",
        f"occurrence_splice_uniform_family_bound_proved={str(audit_result['occurrence_splice_uniform_family_bound_proved']).lower()}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "summary rows：",
        "",
        *markdown_table(audit_result["p_transition_rows"], ["P_transition", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["m_pair_delta_rows"], ["m_pair_delta", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["q_delta_rows"], ["q_delta", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["step_splice_kind_rows"], ["step_splice_kind", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["position_transition_rows"], ["position_transition", "mass", "ratio"]),
        "",
        "splice rows：",
        "",
        *markdown_table(
            audit_result["splice_rows"],
            [
                "splice_id",
                "switch_node",
                "P_transition",
                "left_q",
                "right_q",
                "m_pair_delta",
                "left_step",
                "right_step",
                "step_splice_kind",
                "position_transition",
                "splice_occurrence_mass",
            ],
        ),
        "",
        "occurrence endpoint rows：",
        "",
        *markdown_table(
            audit_result["occurrence_endpoint_rows"],
            [
                "occurrence_key",
                "signed_step_signature",
                "P",
                "step",
                "m_pair",
                "position_class",
                "splice_membership_count",
                "splice_sides",
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
        "结论：P-switch cut 已经进一步局部化为 same signed atom 的 cross-witness occurrence splice。",
        "但这仍只是有限局部拼接账本，不是 uniform family bound。",
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
        f"repeated_step_occurrence_splice_ledger_closed={str(payload['repeated_step_occurrence_splice_ledger_closed']).lower()}",
        f"occurrence_splice_uniform_family_bound_proved={str(payload['occurrence_splice_uniform_family_bound_proved']).lower()}",
        f"single_occurrence_orbit_repair_proved={str(payload['single_occurrence_orbit_repair_proved']).lower()}",
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
        "repeated_step_occurrence_splice_ledger_closed="
        f"{payload['repeated_step_occurrence_splice_ledger_closed']}"
    )
    print(f"occurrence_splice_count={audit_result['occurrence_splice_count']}")
    print(f"all_splices_739_to_607={audit_result['all_splices_739_to_607']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
