#!/usr/bin/env python3
"""审计 dominant sign word 坐标路径的 signed step/transition 原子分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_dominant_sign_word_step_transition_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-step-transition-audit.json

上一层把 dominant sign word `--+-+` 的全部 30 质量写成 3 个
m-pair/offset/orientation coordinate witnesses。本层把每条长度 5 的 signed
coordinate path 拆成 step atoms 与相邻 transition atoms。它关闭的是有限
step/transition 字符串账本，不证明全局 signed collision bound。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-core-largest-atom-dominant-sign-word-step-transition"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-25"
TARGET_SIGN_WORD = "--+-+"

PREVIOUS_COORDINATE_PARTITION_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_COORDINATE_PARTITION_AUDIT,
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


def edge_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成质量表。"""
    return [
        {field: key, "mass": counter[key], "ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def load_previous_payload() -> dict[str, Any]:
    """读入上一层 coordinate partition 证书。"""
    return json.loads(PREVIOUS_COORDINATE_PARTITION_AUDIT.read_text())


def step_signature(coord: dict[str, Any]) -> str:
    """生成 signed step 原子标签。"""
    return f"g={coord['gap']},c={coord['carry']},A={coord['sign']}"


def raw_step_signature(coord: dict[str, Any]) -> str:
    """生成不带符号的 step 标签。"""
    return f"g={coord['gap']},c={coord['carry']}"


def transition_signature(left: dict[str, Any], right: dict[str, Any]) -> str:
    """生成相邻 transition 原子标签。"""
    return f"{step_signature(left)} -> {step_signature(right)}"


def sign_char(sign: str) -> str:
    """把 sign 标签转为 +/-。"""
    if sign == "positive":
        return "+"
    if sign == "negative":
        return "-"
    raise ValueError(f"bad sign: {sign}")


def build_atoms(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """从 coordinate witnesses 生成 step atoms 与 transition atoms。"""
    step_rows: list[dict[str, Any]] = []
    transition_rows: list[dict[str, Any]] = []
    for row in rows:
        coords = row["signed_coordinate_path"]
        mass = row["edge_mass"]
        for coord in coords:
            step_rows.append(
                {
                    "witness_id": row["witness_id"],
                    "P": row["P"],
                    "m_pair": row["m_pair"],
                    "endpoint_orientation": row["endpoint_orientation"],
                    "step": coord["step"],
                    "gap": coord["gap"],
                    "carry": coord["carry"],
                    "sign": coord["sign"],
                    "sign_char": sign_char(coord["sign"]),
                    "signed_step_signature": step_signature(coord),
                    "raw_step_signature": raw_step_signature(coord),
                    "step_mass": mass,
                }
            )
        for left, right in zip(coords, coords[1:]):
            sign_pair = sign_char(left["sign"]) + sign_char(right["sign"])
            transition_rows.append(
                {
                    "witness_id": row["witness_id"],
                    "P": row["P"],
                    "m_pair": row["m_pair"],
                    "endpoint_orientation": row["endpoint_orientation"],
                    "from_step": left["step"],
                    "to_step": right["step"],
                    "from_gap": left["gap"],
                    "to_gap": right["gap"],
                    "from_carry": left["carry"],
                    "to_carry": right["carry"],
                    "gap_delta": right["gap"] - left["gap"],
                    "carry_delta": right["carry"] - left["carry"],
                    "from_sign": left["sign"],
                    "to_sign": right["sign"],
                    "sign_pair": sign_pair,
                    "is_sign_switch": sign_pair[0] != sign_pair[1],
                    "transition_signature": transition_signature(left, right),
                    "transition_mass": mass,
                }
            )
    return step_rows, transition_rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 step/transition 原子账本。"""
    previous_payload = load_previous_payload()
    previous = previous_payload["finite_audit"]
    coordinate_rows = [
        row
        for row in previous["endpoint_coordinate_witness_rows"]
        if row["P"] <= max_prime
    ]
    step_rows, transition_rows = build_atoms(coordinate_rows)

    witness_edge_mass = sum(row["edge_mass"] for row in coordinate_rows)
    step_mass = sum(row["step_mass"] for row in step_rows)
    transition_mass = sum(row["transition_mass"] for row in transition_rows)

    signed_step_mass: Counter[str] = Counter()
    raw_step_mass: Counter[str] = Counter()
    sign_position_mass: Counter[str] = Counter()
    sign_mass: Counter[str] = Counter()
    transition_sig_mass: Counter[str] = Counter()
    sign_pair_mass: Counter[str] = Counter()
    carry_delta_mass: Counter[int] = Counter()
    gap_delta_mass: Counter[int] = Counter()
    endpoint_step_mass: Counter[str] = Counter()

    for row in step_rows:
        mass = row["step_mass"]
        signed_step_mass[row["signed_step_signature"]] += mass
        raw_step_mass[row["raw_step_signature"]] += mass
        sign_position_mass[f"step{row['step']}:{row['sign_char']}"] += mass
        sign_mass[row["sign_char"]] += mass
        if row["step"] == 1:
            endpoint_step_mass[f"initial:{row['sign_char']}"] += mass
        if row["step"] == 5:
            endpoint_step_mass[f"terminal:{row['sign_char']}"] += mass

    for row in transition_rows:
        mass = row["transition_mass"]
        transition_sig_mass[row["transition_signature"]] += mass
        sign_pair_mass[row["sign_pair"]] += mass
        carry_delta_mass[row["carry_delta"]] += mass
        gap_delta_mass[row["gap_delta"]] += mass

    all_witness_length_five = all(len(row["signed_coordinate_path"]) == 5 for row in coordinate_rows)
    all_step_mass_ten = all(row["step_mass"] == 10 for row in step_rows)
    all_transition_mass_ten = all(row["transition_mass"] == 10 for row in transition_rows)
    all_initial_negative = endpoint_step_mass["initial:-"] == witness_edge_mass
    all_terminal_positive = endpoint_step_mass["terminal:+"] == witness_edge_mass
    sign_word_position_law_closed = (
        sign_position_mass["step1:-"] == 30
        and sign_position_mass["step2:-"] == 30
        and sign_position_mass["step3:+"] == 30
        and sign_position_mass["step4:-"] == 30
        and sign_position_mass["step5:+"] == 30
    )
    transition_sign_law_closed = (
        sign_pair_mass["--"] == 30
        and sign_pair_mass["-+"] == 60
        and sign_pair_mass["+-"] == 30
        and sum(row["transition_mass"] for row in transition_rows if row["is_sign_switch"]) == 90
    )
    repeated_signed_step_atoms = sorted(
        key for key, mass in signed_step_mass.items() if mass > 10
    )
    repeated_signed_step_atom_mass = {
        key: signed_step_mass[key] for key in repeated_signed_step_atoms
    }

    ledger_closed = (
        previous_payload["dominant_sign_word_m_pair_coordinate_partition_ledger_closed"]
        and previous["path_template_count"] == 3
        and previous["path_edge_mass"] == 30
        and len(coordinate_rows) == 3
        and witness_edge_mass == 30
        and len(step_rows) == 15
        and step_mass == 150
        and len(transition_rows) == 12
        and transition_mass == 120
        and all_witness_length_five
        and all_step_mass_ten
        and all_transition_mass_ten
        and all_initial_negative
        and all_terminal_positive
        and sign_word_position_law_closed
        and transition_sign_law_closed
        and sign_mass["-"] == 90
        and sign_mass["+"] == 60
        and len(signed_step_mass) == 13
        and repeated_signed_step_atoms
        == ["g=2,c=2,A=negative", "g=6,c=7,A=positive"]
        and all(mass == 20 for mass in repeated_signed_step_atom_mass.values())
    )

    return {
        "max_prime": max_prime,
        "previous_coordinate_partition_ledger_closed": previous_payload[
            "dominant_sign_word_m_pair_coordinate_partition_ledger_closed"
        ],
        "target_sign_word": TARGET_SIGN_WORD,
        "dominant_sign_word_step_transition_ledger_closed": ledger_closed,
        "coordinate_witness_count": len(coordinate_rows),
        "coordinate_witness_edge_mass": witness_edge_mass,
        "step_atom_count": len(step_rows),
        "step_atom_mass": step_mass,
        "transition_atom_count": len(transition_rows),
        "transition_atom_mass": transition_mass,
        "all_witness_length_equals_5": all_witness_length_five,
        "all_step_atom_mass_equals_10": all_step_mass_ten,
        "all_transition_atom_mass_equals_10": all_transition_mass_ten,
        "all_initial_steps_negative": all_initial_negative,
        "all_terminal_steps_positive": all_terminal_positive,
        "sign_word_position_law_closed": sign_word_position_law_closed,
        "transition_sign_law_closed": transition_sign_law_closed,
        "negative_step_mass": sign_mass["-"],
        "positive_step_mass": sign_mass["+"],
        "same_sign_transition_mass": sign_pair_mass["--"],
        "sign_switch_transition_mass": sign_pair_mass["-+"] + sign_pair_mass["+-"],
        "distinct_signed_step_atom_count": len(signed_step_mass),
        "distinct_raw_step_atom_count": len(raw_step_mass),
        "repeated_signed_step_atom_count": len(repeated_signed_step_atoms),
        "repeated_signed_step_atoms": repeated_signed_step_atom_mass,
        "signed_step_atom_rows": edge_rows(signed_step_mass, step_mass, "signed_step_atom"),
        "raw_step_atom_rows": edge_rows(raw_step_mass, step_mass, "raw_step_atom"),
        "sign_position_rows": edge_rows(sign_position_mass, step_mass, "sign_position"),
        "sign_pair_transition_rows": edge_rows(sign_pair_mass, transition_mass, "sign_pair"),
        "carry_delta_transition_rows": edge_rows(carry_delta_mass, transition_mass, "carry_delta"),
        "gap_delta_transition_rows": edge_rows(gap_delta_mass, transition_mass, "gap_delta"),
        "step_atom_rows": sorted(
            step_rows, key=lambda row: (row["P"], row["witness_id"], row["step"])
        ),
        "transition_atom_rows": sorted(
            transition_rows, key=lambda row: (row["P"], row["witness_id"], row["from_step"])
        ),
        "dominant_sign_word_step_transition_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    previous_payload = load_previous_payload()
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_step_transition_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "dominant_sign_word_step_transition_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after m-pair coordinate partition, the path strings themselves are the next non-circular object to atomize",
        "current_object": {
            "input": "three m-pair coordinate witnesses of sign word --+-+",
            "operation": "split length-5 signed coordinate paths into step atoms and adjacent transition atoms",
            "dominant_shape": "15 signed step atoms and 12 adjacent transition atoms with fixed sign-position law",
            "remaining": "turn the step-transition grammar into a uniform signed collision bound or a PDEC/SAE certificate",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "DominantSignWordCoordinatePartitionImported",
                finite_audit["previous_coordinate_partition_ledger_closed"],
                finite_audit["previous_coordinate_partition_ledger_closed"],
                "The full --+-+ m-pair coordinate partition is imported.",
                "none for import",
            ),
            gate(
                "SignedStepAtomLedger",
                finite_audit["dominant_sign_word_step_transition_ledger_closed"],
                finite_audit["dominant_sign_word_step_transition_ledger_closed"],
                "The three paths are split into 15 signed step atoms.",
                "none for the finite step ledger",
            ),
            gate(
                "AdjacentTransitionAtomLedger",
                finite_audit["dominant_sign_word_step_transition_ledger_closed"],
                finite_audit["dominant_sign_word_step_transition_ledger_closed"],
                "The three paths are split into 12 adjacent transition atoms.",
                "none for the finite transition ledger",
            ),
            gate(
                "StepTransitionUniformFamilyBound",
                False,
                False,
                "Control the step-transition grammar as a uniform family.",
                "finite grammar audit gives exact atoms but no global theorem",
            ),
        ],
        "external_sources_consulted": previous_payload["external_sources_consulted"],
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "step atoms still need aggregation into a nonlocal trace or bilinear sum before these theorems apply",
            "prime_gap_inputs": "the gap labels are local path grammar data, not prime-gap existence estimates",
            "short_interval_prime_inputs": "theta=0.52 remains above the endpoint half-scale and does not estimate this fixed grammar",
        },
        "latest_narrowest_mouth": [
            "DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar)",
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
        "dominant_sign_word_step_transition_ledger_closed": finite_audit[
            "dominant_sign_word_step_transition_ledger_closed"
        ],
        "dominant_sign_word_step_transition_family_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word step-transition 审计",
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
        "## 2. signed step/transition 审计",
        "",
        "```text",
        f"max_prime={audit_result['max_prime']}",
        f"dominant_sign_word_step_transition_ledger_closed={str(audit_result['dominant_sign_word_step_transition_ledger_closed']).lower()}",
        f"target_sign_word={audit_result['target_sign_word']}",
        f"coordinate_witness_count={audit_result['coordinate_witness_count']}",
        f"coordinate_witness_edge_mass={audit_result['coordinate_witness_edge_mass']}",
        f"step_atom_count={audit_result['step_atom_count']}",
        f"step_atom_mass={audit_result['step_atom_mass']}",
        f"transition_atom_count={audit_result['transition_atom_count']}",
        f"transition_atom_mass={audit_result['transition_atom_mass']}",
        f"all_witness_length_equals_5={str(audit_result['all_witness_length_equals_5']).lower()}",
        f"all_step_atom_mass_equals_10={str(audit_result['all_step_atom_mass_equals_10']).lower()}",
        f"all_transition_atom_mass_equals_10={str(audit_result['all_transition_atom_mass_equals_10']).lower()}",
        f"all_initial_steps_negative={str(audit_result['all_initial_steps_negative']).lower()}",
        f"all_terminal_steps_positive={str(audit_result['all_terminal_steps_positive']).lower()}",
        f"sign_word_position_law_closed={str(audit_result['sign_word_position_law_closed']).lower()}",
        f"transition_sign_law_closed={str(audit_result['transition_sign_law_closed']).lower()}",
        f"negative_step_mass={audit_result['negative_step_mass']}",
        f"positive_step_mass={audit_result['positive_step_mass']}",
        f"same_sign_transition_mass={audit_result['same_sign_transition_mass']}",
        f"sign_switch_transition_mass={audit_result['sign_switch_transition_mass']}",
        f"distinct_signed_step_atom_count={audit_result['distinct_signed_step_atom_count']}",
        f"repeated_signed_step_atom_count={audit_result['repeated_signed_step_atom_count']}",
        f"repeated_signed_step_atoms={audit_result['repeated_signed_step_atoms']}",
        f"row_column_unconditional_closed={str(audit_result['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "signed step atom subledger：",
        "",
        *markdown_table(
            audit_result["signed_step_atom_rows"],
            ["signed_step_atom", "mass", "ratio"],
        ),
        "",
        "sign-position and transition-sign laws：",
        "",
        *markdown_table(audit_result["sign_position_rows"], ["sign_position", "mass", "ratio"]),
        "",
        *markdown_table(
            audit_result["sign_pair_transition_rows"],
            ["sign_pair", "mass", "ratio"],
        ),
        "",
        "carry/gap delta transition subledgers：",
        "",
        *markdown_table(audit_result["carry_delta_transition_rows"], ["carry_delta", "mass", "ratio"]),
        "",
        *markdown_table(audit_result["gap_delta_transition_rows"], ["gap_delta", "mass", "ratio"]),
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
        "结论：dominant sign word `--+-+` 的三条坐标路径已拆成 15 个 signed step atoms 与 12 个 adjacent transition atoms。",
        "该账本仍是有限结构结果，尚未给出全局 signed collision bound。",
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
        f"dominant_sign_word_step_transition_ledger_closed={str(payload['dominant_sign_word_step_transition_ledger_closed']).lower()}",
        f"dominant_sign_word_step_transition_family_bound_proved={str(payload['dominant_sign_word_step_transition_family_bound_proved']).lower()}",
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
        "dominant_sign_word_step_transition_ledger_closed="
        f"{payload['dominant_sign_word_step_transition_ledger_closed']}"
    )
    print(f"step_atom_count={audit_result['step_atom_count']}")
    print(f"transition_atom_count={audit_result['transition_atom_count']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
