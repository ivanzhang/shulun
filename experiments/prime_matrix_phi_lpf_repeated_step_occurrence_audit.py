#!/usr/bin/env python3
"""审计 dominant sign word 中重复 signed step atom 的发生位置。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_repeated_step_occurrence_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-occurrence-audit.json

上一层把 dominant sign word `--+-+` 的三条坐标路径拆成 step/transition
原子，并发现两个 repeated signed step atoms。本层只关闭这些重复原子的
occurrence-position/touching-transition 有限账本，不证明 uniform signed
collision bound，也不突破全局 Phi-LPF 奇偶障碍。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-"
    "occurrence"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

PREVIOUS_STEP_TRANSITION_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-step-transition-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_STEP_TRANSITION_AUDIT,
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


def load_previous_payload() -> dict[str, Any]:
    """读入上一层 step-transition 证书。"""
    return json.loads(PREVIOUS_STEP_TRANSITION_AUDIT.read_text())


def step_signature_from_transition(row: dict[str, Any], side: str) -> str:
    """从 transition row 恢复 from/to 端的 signed step 标签。"""
    return f"g={row[f'{side}_gap']},c={row[f'{side}_carry']},A={row[f'{side}_sign']}"


def position_class(step: int) -> str:
    """标记 occurrence 在路径中的端点/内部角色。"""
    if step == 1:
        return "initial"
    if step == 5:
        return "terminal"
    return "internal"


def edge_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def occurrence_key(row: dict[str, Any]) -> str:
    """构造短 occurrence 标签。"""
    return f"P{row['P']}:step{row['step']}:{row['m_pair']}:{row['endpoint_orientation']}"


def build_touching_transition_rows(
    transition_rows: list[dict[str, Any]], repeated_atoms: set[str]
) -> list[dict[str, Any]]:
    """抽取接触任一 repeated atom 的 transition。"""
    touching_rows: list[dict[str, Any]] = []
    for row in transition_rows:
        from_atom = step_signature_from_transition(row, "from")
        to_atom = step_signature_from_transition(row, "to")
        touched_atoms = [atom for atom in (from_atom, to_atom) if atom in repeated_atoms]
        if not touched_atoms:
            continue
        side = "both" if len(touched_atoms) == 2 else ("from" if from_atom in repeated_atoms else "to")
        touching_rows.append(
            {
                **row,
                "from_signed_step_signature": from_atom,
                "to_signed_step_signature": to_atom,
                "touch_side": side,
                "touched_repeated_atoms": touched_atoms,
                "touching_transition_mass": row["transition_mass"],
            }
        )
    return touching_rows


def build_repeated_atom_rows(
    occurrence_rows: list[dict[str, Any]], touching_rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """按 repeated atom 汇总 occurrence 与 touching-transition 入出边。"""
    by_atom: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in occurrence_rows:
        by_atom[row["signed_step_signature"]].append(row)

    incoming: Counter[str] = Counter()
    outgoing: Counter[str] = Counter()
    touching_incidence: Counter[str] = Counter()
    touching_incidence_mass: Counter[str] = Counter()
    for row in touching_rows:
        for atom in row["touched_repeated_atoms"]:
            touching_incidence[atom] += 1
            touching_incidence_mass[atom] += row["touching_transition_mass"]
        if row["to_signed_step_signature"] in by_atom:
            incoming[row["to_signed_step_signature"]] += 1
        if row["from_signed_step_signature"] in by_atom:
            outgoing[row["from_signed_step_signature"]] += 1

    result: list[dict[str, Any]] = []
    for atom, rows in sorted(by_atom.items()):
        position_counter = Counter(row["position_class"] for row in rows)
        result.append(
            {
                "repeated_signed_step_atom": atom,
                "occurrence_count": len(rows),
                "occurrence_mass": sum(row["step_mass"] for row in rows),
                "initial_occurrence_count": position_counter["initial"],
                "internal_occurrence_count": position_counter["internal"],
                "terminal_occurrence_count": position_counter["terminal"],
                "incoming_transition_count": incoming[atom],
                "outgoing_transition_count": outgoing[atom],
                "touching_transition_incidence_count": touching_incidence[atom],
                "touching_transition_incidence_mass": touching_incidence_mass[atom],
                "P_support": sorted({row["P"] for row in rows}),
                "m_pair_support": sorted({row["m_pair"] for row in rows}),
                "occurrence_keys": [occurrence_key(row) for row in sorted(rows, key=lambda item: (item["P"], item["step"]))],
            }
        )
    return result


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """生成 repeated step occurrence/touching-transition 有限账本。"""
    previous_payload = load_previous_payload()
    previous = previous_payload["finite_audit"]
    repeated_atom_mass = dict(previous["repeated_signed_step_atoms"])
    repeated_atoms = set(repeated_atom_mass)

    step_rows = [row for row in previous["step_atom_rows"] if row["P"] <= max_prime]
    transition_rows = [row for row in previous["transition_atom_rows"] if row["P"] <= max_prime]

    occurrence_rows = [
        {
            **row,
            "position_class": position_class(row["step"]),
            "occurrence_key": occurrence_key(row),
            "occurrence_mass": row["step_mass"],
        }
        for row in step_rows
        if row["signed_step_signature"] in repeated_atoms
    ]
    touching_rows = build_touching_transition_rows(transition_rows, repeated_atoms)
    repeated_atom_rows = build_repeated_atom_rows(occurrence_rows, touching_rows)

    occurrence_position_mass: Counter[str] = Counter()
    occurrence_atom_mass: Counter[str] = Counter()
    touch_side_mass: Counter[str] = Counter()
    touch_sign_pair_mass: Counter[str] = Counter()
    touch_incidence_count = 0
    touch_incidence_mass = 0
    for row in occurrence_rows:
        occurrence_position_mass[row["position_class"]] += row["occurrence_mass"]
        occurrence_atom_mass[row["signed_step_signature"]] += row["occurrence_mass"]
    for row in touching_rows:
        mass = row["touching_transition_mass"]
        touch_side_mass[row["touch_side"]] += mass
        touch_sign_pair_mass[row["sign_pair"]] += mass
        touch_incidence_count += len(row["touched_repeated_atoms"])
        touch_incidence_mass += mass * len(row["touched_repeated_atoms"])

    expected_occurrences = [
        ("g=2,c=2,A=negative", 607, 1, "[769, 773]", "above_P"),
        ("g=6,c=7,A=positive", 607, 3, "[769, 773]", "above_P"),
        ("g=2,c=2,A=negative", 739, 4, "[757, 761]", "above_P"),
        ("g=6,c=7,A=positive", 739, 5, "[757, 761]", "above_P"),
    ]
    actual_occurrences = [
        (
            row["signed_step_signature"],
            row["P"],
            row["step"],
            row["m_pair"],
            row["endpoint_orientation"],
        )
        for row in sorted(occurrence_rows, key=lambda item: (item["P"], item["step"]))
    ]
    endpoint_role_law_closed = sorted(
        (
            row["repeated_signed_step_atom"],
            row["initial_occurrence_count"],
            row["internal_occurrence_count"],
            row["terminal_occurrence_count"],
        )
        for row in repeated_atom_rows
    ) == [
        ("g=2,c=2,A=negative", 1, 1, 0),
        ("g=6,c=7,A=positive", 0, 1, 1),
    ]

    ledger_closed = (
        previous_payload["dominant_sign_word_step_transition_ledger_closed"]
        and previous["repeated_signed_step_atom_count"] == 2
        and repeated_atom_mass
        == {"g=2,c=2,A=negative": 20, "g=6,c=7,A=positive": 20}
        and len(occurrence_rows) == 4
        and sum(row["occurrence_mass"] for row in occurrence_rows) == 40
        and actual_occurrences == expected_occurrences
        and endpoint_role_law_closed
        and len(touching_rows) == 5
        and sum(row["touching_transition_mass"] for row in touching_rows) == 50
        and touch_incidence_count == 6
        and touch_incidence_mass == 60
        and all(row["occurrence_count"] == 2 for row in repeated_atom_rows)
        and all(row["occurrence_mass"] == 20 for row in repeated_atom_rows)
        and all(row["touching_transition_incidence_count"] == 3 for row in repeated_atom_rows)
    )

    return {
        "max_prime": max_prime,
        "previous_step_transition_ledger_closed": previous_payload[
            "dominant_sign_word_step_transition_ledger_closed"
        ],
        "target_sign_word": TARGET_SIGN_WORD,
        "dominant_sign_word_repeated_step_occurrence_ledger_closed": ledger_closed,
        "repeated_signed_step_atom_count": len(repeated_atoms),
        "repeated_signed_step_atoms": repeated_atom_mass,
        "repeated_step_occurrence_count": len(occurrence_rows),
        "repeated_step_occurrence_mass": sum(row["occurrence_mass"] for row in occurrence_rows),
        "endpoint_role_law_closed": endpoint_role_law_closed,
        "touching_transition_count": len(touching_rows),
        "touching_transition_mass": sum(row["touching_transition_mass"] for row in touching_rows),
        "touching_transition_repeated_endpoint_incidence_count": touch_incidence_count,
        "touching_transition_repeated_endpoint_incidence_mass": touch_incidence_mass,
        "occurrence_position_rows": edge_rows(
            occurrence_position_mass,
            sum(row["occurrence_mass"] for row in occurrence_rows),
            "position_class",
        ),
        "occurrence_atom_rows": edge_rows(
            occurrence_atom_mass,
            sum(row["occurrence_mass"] for row in occurrence_rows),
            "repeated_signed_step_atom",
        ),
        "touch_side_rows": edge_rows(
            touch_side_mass,
            sum(row["touching_transition_mass"] for row in touching_rows),
            "touch_side",
        ),
        "touch_sign_pair_rows": edge_rows(
            touch_sign_pair_mass,
            sum(row["touching_transition_mass"] for row in touching_rows),
            "sign_pair",
        ),
        "repeated_atom_rows": repeated_atom_rows,
        "occurrence_rows": sorted(occurrence_rows, key=lambda row: (row["P"], row["step"])),
        "touching_transition_rows": sorted(
            touching_rows, key=lambda row: (row["P"], row["from_step"], row["to_step"])
        ),
        "dominant_sign_word_repeated_step_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    previous_payload = load_previous_payload()
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_repeated_step_occurrence_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "dominant_sign_word_repeated_step_occurrence_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the step-transition grammar, the repeated signed step atoms are the next non-circular finite collision carrier",
        "current_object": {
            "input": "two repeated signed step atoms inside the --+-+ step-transition ledger",
            "operation": "split repeated atoms into occurrence positions and touching adjacent transitions",
            "dominant_shape": "4 repeated-step occurrences and 5 touching transitions, with 6 repeated-endpoint incidences",
            "remaining": "turn this finite collision carrier into a uniform signed collision bound or PDEC/SAE certificate",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "DominantSignWordStepTransitionImported",
                finite_audit["previous_step_transition_ledger_closed"],
                finite_audit["previous_step_transition_ledger_closed"],
                "The full --+-+ signed step/transition ledger is imported.",
                "none for import",
            ),
            gate(
                "RepeatedSignedStepOccurrenceLedger",
                finite_audit["dominant_sign_word_repeated_step_occurrence_ledger_closed"],
                finite_audit["dominant_sign_word_repeated_step_occurrence_ledger_closed"],
                "The two repeated signed step atoms are split into four exact occurrence positions.",
                "none for the finite occurrence ledger",
            ),
            gate(
                "RepeatedStepTouchingTransitionLedger",
                finite_audit["dominant_sign_word_repeated_step_occurrence_ledger_closed"],
                finite_audit["dominant_sign_word_repeated_step_occurrence_ledger_closed"],
                "All adjacent transitions touching the repeated atoms are listed.",
                "none for the finite touching-transition ledger",
            ),
            gate(
                "RepeatedStepUniformFamilyBound",
                False,
                False,
                "Control repeated signed step collisions uniformly in the full family.",
                "finite occurrence ledger gives exact witnesses but no global theorem",
            ),
        ],
        "external_sources_consulted": previous_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "touching-transition rows are still finite local grammar data, not a completed trace/bilinear family",
            "prime_gap_inputs": "the endpoint/internal roles are not prime-gap existence estimates",
            "short_interval_prime_inputs": "theta=0.52 does not imply a half-scale statement for this repeated-step carrier",
        },
        "latest_narrowest_mouth": [
            "RepeatedStepUniformFamilyBound(g=2,c=2,A=negative and g=6,c=7,A=positive)",
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
        "dominant_sign_word_repeated_step_occurrence_ledger_closed": finite_audit[
            "dominant_sign_word_repeated_step_occurrence_ledger_closed"
        ],
        "dominant_sign_word_repeated_step_family_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word repeated-step occurrence 审计",
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
        "## 2. repeated-step occurrence 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"dominant_sign_word_repeated_step_occurrence_ledger_closed={str(audit_result['dominant_sign_word_repeated_step_occurrence_ledger_closed']).lower()}",
        f"target_sign_word={audit_result['target_sign_word']}",
        f"repeated_signed_step_atom_count={audit_result['repeated_signed_step_atom_count']}",
        f"repeated_signed_step_atoms={audit_result['repeated_signed_step_atoms']}",
        f"repeated_step_occurrence_count={audit_result['repeated_step_occurrence_count']}",
        f"repeated_step_occurrence_mass={audit_result['repeated_step_occurrence_mass']}",
        f"endpoint_role_law_closed={str(audit_result['endpoint_role_law_closed']).lower()}",
        f"touching_transition_count={audit_result['touching_transition_count']}",
        f"touching_transition_mass={audit_result['touching_transition_mass']}",
        f"touching_transition_repeated_endpoint_incidence_count={audit_result['touching_transition_repeated_endpoint_incidence_count']}",
        f"touching_transition_repeated_endpoint_incidence_mass={audit_result['touching_transition_repeated_endpoint_incidence_mass']}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "repeated atom summary：",
        "",
        *markdown_table(
            audit_result["repeated_atom_rows"],
            [
                "repeated_signed_step_atom",
                "occurrence_count",
                "occurrence_mass",
                "initial_occurrence_count",
                "internal_occurrence_count",
                "terminal_occurrence_count",
                "incoming_transition_count",
                "outgoing_transition_count",
                "touching_transition_incidence_count",
                "P_support",
                "m_pair_support",
            ],
        ),
        "",
        "occurrence position rows：",
        "",
        *markdown_table(
            audit_result["occurrence_rows"],
            [
                "P",
                "m_pair",
                "endpoint_orientation",
                "step",
                "position_class",
                "signed_step_signature",
                "occurrence_mass",
                "witness_id",
            ],
        ),
        "",
        "touching transition rows：",
        "",
        *markdown_table(
            audit_result["touching_transition_rows"],
            [
                "P",
                "m_pair",
                "from_step",
                "to_step",
                "transition_signature",
                "touch_side",
                "touched_repeated_atoms",
                "sign_pair",
                "touching_transition_mass",
            ],
        ),
        "",
        "position/touch side summaries：",
        "",
        *markdown_table(audit_result["occurrence_position_rows"], ["position_class", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["touch_side_rows"], ["touch_side", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["touch_sign_pair_rows"], ["sign_pair", "mass", "ratio"]),
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
        "结论：两个 repeated signed step atoms 已经完全定位到四个 occurrence，并列出五条 touching transition。",
        "该账本仍是有限结构结果，尚未给出全局 uniform family bound。",
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
        f"dominant_sign_word_repeated_step_occurrence_ledger_closed={str(payload['dominant_sign_word_repeated_step_occurrence_ledger_closed']).lower()}",
        f"dominant_sign_word_repeated_step_family_bound_proved={str(payload['dominant_sign_word_repeated_step_family_bound_proved']).lower()}",
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
        "dominant_sign_word_repeated_step_occurrence_ledger_closed="
        f"{payload['dominant_sign_word_repeated_step_occurrence_ledger_closed']}"
    )
    print(f"repeated_step_occurrence_count={audit_result['repeated_step_occurrence_count']}")
    print(f"touching_transition_count={audit_result['touching_transition_count']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
