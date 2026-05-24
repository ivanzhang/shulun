#!/usr/bin/env python3
"""审计最大 core atom 中 dominant sign word 的路径见证分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_path_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-path-audit.json

上一层把最大 core atom 的 70 质量拆成 7 个模板见证；其中 dominant sign word
为 --+-+，质量 30。本层只处理这个 dominant sign-word family，并继续拆成
3 个 raw-base / signed-child 路径见证。该层关闭有限路径账本，不证明全局
signed collision bound。
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_template_witness_audit as witness_audit  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-core-largest-atom-dominant-sign-word-path"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_WITNESS_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-template-witness-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_WITNESS_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

TARGET_SIGN_WORD = "--+-+"
EXTERNAL_SOURCES = witness_audit.EXTERNAL_SOURCES


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
    """把 Counter 转成 edge-mass 表。"""
    return [
        {field: key, "edge_mass": counter[key], "edge_ratio": counter[key] / total}
        for key in sorted(counter, key=lambda item: (-counter[item], str(item)))
    ]


def pair_rows(
    counter: Counter[tuple[Any, Any]],
    total: int,
    left_field: str,
    right_field: str,
) -> list[dict[str, Any]]:
    """输出二元 edge-mass 表。"""
    return [
        {
            left_field: left,
            right_field: right,
            "edge_mass": counter[(left, right)],
            "edge_ratio": counter[(left, right)] / total,
        }
        for left, right in sorted(counter, key=lambda key: (-counter[key], str(key[0]), str(key[1])))
    ]


def selected_dominant_rows(max_prime: int) -> list[dict[str, Any]]:
    """抽取 dominant sign word 的路径见证行。"""
    return [
        row
        for row in witness_audit.selected_largest_atom_rows(max_prime)
        if row["sign_word"] == TARGET_SIGN_WORD
    ]


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计 dominant sign-word path witness 账本。"""
    previous_payload = json.loads(PREVIOUS_WITNESS_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    rows = selected_dominant_rows(max_prime)

    p_band_edge_mass: Counter[str] = Counter()
    q_prefix_count_edge_mass: Counter[int] = Counter()
    q_prefix_band_edge_mass: Counter[str] = Counter()
    m_shell_prime_count_edge_mass: Counter[int] = Counter()
    m_pair_edge_mass: Counter[str] = Counter()
    raw_base_edge_mass: Counter[str] = Counter()
    signed_child_edge_mass: Counter[str] = Counter()
    q_m_pair_edge_mass: Counter[tuple[str, str]] = Counter()

    path_rows: list[dict[str, Any]] = []
    for row in rows:
        mass = row["edge_mass"]
        p_band_edge_mass[row["P_band"]] += mass
        q_prefix_count_edge_mass[row["q_prefix_count"]] += mass
        q_prefix_band_edge_mass[row["q_prefix_band"]] += mass
        m_shell_prime_count_edge_mass[row["m_shell_prime_count"]] += mass
        m_pair_edge_mass[row["m_pair"]] += mass
        raw_base_edge_mass[row["raw_base_template"]] += mass
        signed_child_edge_mass[row["signed_child"]] += mass
        q_m_pair_edge_mass[(row["q_prefix_band"], row["m_pair"])] += mass
        path_rows.append(
            {
                "P": row["P"],
                "P_band": row["P_band"],
                "packet_index": row["packet_index"],
                "edge_mass": mass,
                "integer_gap": row["integer_gap"],
                "occurrence_count": row["occurrence_count"],
                "m_pair": row["m_pair"],
                "q_prefix_count": row["q_prefix_count"],
                "q_prefix_band": row["q_prefix_band"],
                "m_shell_prime_count": row["m_shell_prime_count"],
                "m_shell_band": row["m_shell_band"],
                "raw_base_template": row["raw_base_template"],
                "signed_child": row["signed_child"],
            }
        )

    total_template_count = len(rows)
    total_edge_mass = sum(row["edge_mass"] for row in rows)
    all_mass_ten = all(row["edge_mass"] == 10 for row in rows)
    all_pairwise_occurrence = all(row["occurrence_count"] == 2 for row in rows)
    all_gap4 = all(row["integer_gap"] == 4 for row in rows)
    all_m_shell_le4 = all(row["m_shell_band"] == "m<=4" for row in rows)
    all_sign_balance_fixed = all(row["sign_balance"] == "plus=2,minus=3" for row in rows)
    distinct_raw_base_count = len(raw_base_edge_mass)
    distinct_signed_child_count = len(signed_child_edge_mass)
    distinct_m_pair_count = len(m_pair_edge_mass)
    dominant_m_pair = max(m_pair_edge_mass, key=lambda key: m_pair_edge_mass[key])
    dominant_m_pair_mass = m_pair_edge_mass[dominant_m_pair]

    ledger_closed = (
        previous_payload["largest_atom_template_witness_ledger_closed"]
        and previous["dominant_sign_word"] == TARGET_SIGN_WORD
        and previous["dominant_sign_word_edge_mass"] == 30
        and total_template_count == 3
        and total_edge_mass == 30
        and all_mass_ten
        and all_pairwise_occurrence
        and all_gap4
        and all_m_shell_le4
        and all_sign_balance_fixed
        and distinct_raw_base_count == 3
        and distinct_signed_child_count == 3
        and distinct_m_pair_count == 2
        and dominant_m_pair == "[769, 773]"
        and dominant_m_pair_mass == 20
        and q_prefix_band_edge_mass["q<=10"] == 20
        and q_prefix_band_edge_mass["q>20"] == 10
    )

    return {
        "max_prime": max_prime,
        "previous_largest_atom_template_witness_ledger_closed": previous_payload[
            "largest_atom_template_witness_ledger_closed"
        ],
        "dominant_sign_word_path_ledger_closed": ledger_closed,
        "target_sign_word": TARGET_SIGN_WORD,
        "previous_dominant_sign_word_edge_mass": previous["dominant_sign_word_edge_mass"],
        "path_template_count": total_template_count,
        "path_edge_mass": total_edge_mass,
        "all_path_edge_mass_equals_10": all_mass_ten,
        "all_path_occurrence_count_equals_2": all_pairwise_occurrence,
        "all_path_integer_gap_equals_4": all_gap4,
        "all_path_m_shell_band_m_le_4": all_m_shell_le4,
        "all_path_sign_balance_plus2_minus3": all_sign_balance_fixed,
        "distinct_raw_base_template_count": distinct_raw_base_count,
        "distinct_signed_child_count": distinct_signed_child_count,
        "distinct_m_pair_count": distinct_m_pair_count,
        "dominant_m_pair": dominant_m_pair,
        "dominant_m_pair_edge_mass": dominant_m_pair_mass,
        "q_prefix_band_q_le_10_edge_mass": q_prefix_band_edge_mass["q<=10"],
        "q_prefix_band_q_gt_20_edge_mass": q_prefix_band_edge_mass["q>20"],
        "P_band_edge_rows": edge_rows(p_band_edge_mass, total_edge_mass, "P_band"),
        "q_prefix_count_edge_rows": edge_rows(
            q_prefix_count_edge_mass, total_edge_mass, "q_prefix_count"
        ),
        "q_prefix_band_edge_rows": edge_rows(q_prefix_band_edge_mass, total_edge_mass, "q_prefix_band"),
        "m_shell_prime_count_edge_rows": edge_rows(
            m_shell_prime_count_edge_mass, total_edge_mass, "m_shell_prime_count"
        ),
        "m_pair_edge_rows": edge_rows(m_pair_edge_mass, total_edge_mass, "m_pair"),
        "raw_base_template_edge_rows": edge_rows(
            raw_base_edge_mass, total_edge_mass, "raw_base_template"
        ),
        "signed_child_edge_rows": edge_rows(signed_child_edge_mass, total_edge_mass, "signed_child"),
        "q_m_pair_edge_rows": pair_rows(
            q_m_pair_edge_mass,
            total_edge_mass,
            "q_prefix_band",
            "m_pair",
        ),
        "path_witness_rows": sorted(
            path_rows,
            key=lambda row: (row["P"], row["packet_index"], row["m_pair"], row["raw_base_template"]),
        ),
        "dominant_sign_word_path_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_path_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "dominant_largest_atom_sign_word_path_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the dominant sign word --+-+ is the largest subfamily inside the current largest core atom",
        "current_object": {
            "input": "dominant sign word --+-+ inside the largest core atom",
            "operation": "split its 30 edge mass into exact raw-base and signed-child path witnesses",
            "dominant_shape": "3 equal-mass path witnesses with distinct raw-base templates and shared gap4/m<=4 structure",
            "remaining": "turn the three path witnesses into a uniform family bound or route the family through PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "LargestAtomTemplateWitnessLedgerImported",
                finite_audit["previous_largest_atom_template_witness_ledger_closed"],
                finite_audit["previous_largest_atom_template_witness_ledger_closed"],
                "The 7-witness largest atom ledger is imported.",
                "none for import",
            ),
            gate(
                "DominantSignWordPathLedger",
                finite_audit["dominant_sign_word_path_ledger_closed"],
                finite_audit["dominant_sign_word_path_ledger_closed"],
                "The --+-+ subfamily is split into three path witnesses.",
                "none for the finite path ledger",
            ),
            gate(
                "DominantSignWordUniformFamilyBound",
                False,
                False,
                "Control the three path witnesses as a uniform family.",
                "finite audit gives exact paths but no global theorem",
            ),
            gate(
                "OtherLargestAtomTemplateWitnessFamilyBounds",
                False,
                False,
                "Control the other sign-word witnesses inside the largest atom.",
                "carried forward from the 7-witness ledger",
            ),
            gate(
                "ResidualCoreAndTopTwoBounds",
                False,
                False,
                "Control remaining core atoms and top-two noncore residuals.",
                "carried forward from the core atom ledger",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "trace_or_kloosterman_inputs": "need a nonlocal completion from these three path witnesses to a bilinear or trace-family sum",
            "prime_gap_inputs": "the gap4 label is structural here but prime-gap existence theorems do not bound signed local equality",
            "short_interval_prime_inputs": "theta=0.52 remains above the endpoint half-scale and does not see the path witnesses",
        },
        "latest_narrowest_mouth": [
            "DominantLargestAtomPathWitnessUniformFamilyBound(--+-+)",
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
        "dominant_sign_word_path_ledger_closed": finite_audit[
            "dominant_sign_word_path_ledger_closed"
        ],
        "dominant_sign_word_path_family_bound_proved": False,
        "other_largest_atom_template_witness_family_bounds_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word path 审计",
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
        "## 2. dominant sign-word path 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"dominant_sign_word_path_ledger_closed={str(audit['dominant_sign_word_path_ledger_closed']).lower()}",
        f"target_sign_word={audit['target_sign_word']}",
        f"previous_dominant_sign_word_edge_mass={audit['previous_dominant_sign_word_edge_mass']}",
        f"path_template_count={audit['path_template_count']}",
        f"path_edge_mass={audit['path_edge_mass']}",
        f"all_path_edge_mass_equals_10={str(audit['all_path_edge_mass_equals_10']).lower()}",
        f"all_path_occurrence_count_equals_2={str(audit['all_path_occurrence_count_equals_2']).lower()}",
        f"all_path_integer_gap_equals_4={str(audit['all_path_integer_gap_equals_4']).lower()}",
        f"all_path_m_shell_band_m_le_4={str(audit['all_path_m_shell_band_m_le_4']).lower()}",
        f"all_path_sign_balance_plus2_minus3={str(audit['all_path_sign_balance_plus2_minus3']).lower()}",
        f"distinct_raw_base_template_count={audit['distinct_raw_base_template_count']}",
        f"distinct_signed_child_count={audit['distinct_signed_child_count']}",
        f"distinct_m_pair_count={audit['distinct_m_pair_count']}",
        f"dominant_m_pair={audit['dominant_m_pair']}",
        f"dominant_m_pair_edge_mass={audit['dominant_m_pair_edge_mass']}",
        f"q_prefix_band_q_le_10_edge_mass={audit['q_prefix_band_q_le_10_edge_mass']}",
        f"q_prefix_band_q_gt_20_edge_mass={audit['q_prefix_band_q_gt_20_edge_mass']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "path witnesses：",
        "",
        *markdown_table(
            audit["path_witness_rows"],
            [
                "P",
                "P_band",
                "packet_index",
                "edge_mass",
                "integer_gap",
                "occurrence_count",
                "m_pair",
                "q_prefix_count",
                "q_prefix_band",
                "m_shell_prime_count",
                "m_shell_band",
                "raw_base_template",
                "signed_child",
            ],
        ),
        "",
        "m-pair and q-prefix subledgers：",
        "",
        *markdown_table(audit["m_pair_edge_rows"], ["m_pair", "edge_mass", "edge_ratio"]),
        "",
        *markdown_table(audit["q_prefix_band_edge_rows"], ["q_prefix_band", "edge_mass", "edge_ratio"]),
        "",
        "raw-base templates：",
        "",
        *markdown_table(audit["raw_base_template_edge_rows"], ["raw_base_template", "edge_mass", "edge_ratio"]),
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
        "结论：dominant sign word `--+-+` 已被压成 3 个等质量路径见证。",
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
        f"dominant_sign_word_path_ledger_closed={str(payload['dominant_sign_word_path_ledger_closed']).lower()}",
        f"dominant_sign_word_path_family_bound_proved={str(payload['dominant_sign_word_path_family_bound_proved']).lower()}",
        f"other_largest_atom_template_witness_family_bounds_proved={str(payload['other_largest_atom_template_witness_family_bounds_proved']).lower()}",
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
    print(f"dominant_sign_word_path_ledger_closed={payload['dominant_sign_word_path_ledger_closed']}")
    print(f"path_edge_mass={audit['path_edge_mass']}")
    print(f"path_template_count={audit['path_template_count']}")
    print(f"dominant_m_pair={audit['dominant_m_pair']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
