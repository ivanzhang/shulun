#!/usr/bin/env python3
"""审计 top-two core 中最大 route-cycle-switch atom 的模板见证分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_template_witness_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-template-witness-audit.json

上一层把 top-two core 的 270 质量拆成 11 个 route-cycle-switch 原子。
本层只取最大原子：
  gap4_right_tail_two_sided, cycle_length=5, sign_switch_count=3.
该原子质量为 70。本层继续拆成 7 个模板见证与 sign-word/q-prefix/m-shell
子账本。它关闭有限见证账本，不证明全局 signed collision bound。
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

import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_route_cycle_switch_audit as core_audit  # noqa: E402


SLUG = (
    "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-"
    "boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-"
    "gap2-gap4-top-two-core-largest-atom-template-witness"
)
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

PREVIOUS_CORE_AUDIT = (
    DOCS
    / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-route-cycle-switch-audit.json"
)

DEPENDENCIES = [
    PREVIOUS_CORE_AUDIT,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

TARGET_ROUTE = "gap4_right_tail_two_sided"
TARGET_CYCLE = 5
TARGET_SWITCH = 3
EXTERNAL_SOURCES = core_audit.EXTERNAL_SOURCES


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


def template_rows(counter: Counter[Any], total: int, field: str) -> list[dict[str, Any]]:
    """把 Counter 转成 template-count 表。"""
    return [
        {field: key, "template_count": counter[key], "template_ratio": counter[key] / total}
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


def p_band(prime: int) -> str:
    """把 P 分成三段，避免把样本坐标误当成证明。"""
    if prime <= 700:
        return "P<=700"
    if prime <= 850:
        return "P<=850"
    return "P>850"


def selected_largest_atom_rows(max_prime: int) -> list[dict[str, Any]]:
    """抽取最大 route-cycle-switch atom 的模板行。"""
    rows = []
    for row in core_audit.selected_core_rows(max_prime):
        if (
            row["route_label"] == TARGET_ROUTE
            and row["cycle_length"] == TARGET_CYCLE
            and row["sign_switch_count"] == TARGET_SWITCH
        ):
            rows.append({**row, "P_band": p_band(row["P"])})
    return rows


def audit(max_prime: int = 1009) -> dict[str, Any]:
    """审计最大 atom 的模板见证账本。"""
    previous_payload = json.loads(PREVIOUS_CORE_AUDIT.read_text())
    previous = previous_payload["finite_audit"]
    rows = selected_largest_atom_rows(max_prime)

    sign_word_edge_mass: Counter[str] = Counter()
    sign_word_template_count: Counter[str] = Counter()
    sign_balance_edge_mass: Counter[str] = Counter()
    q_prefix_edge_mass: Counter[int] = Counter()
    q_prefix_band_edge_mass: Counter[str] = Counter()
    m_shell_edge_mass: Counter[int] = Counter()
    m_shell_band_edge_mass: Counter[str] = Counter()
    p_band_edge_mass: Counter[str] = Counter()
    q_m_band_edge_mass: Counter[tuple[str, str]] = Counter()
    sign_q_band_edge_mass: Counter[tuple[str, str]] = Counter()
    sign_m_band_edge_mass: Counter[tuple[str, str]] = Counter()

    witness_rows: list[dict[str, Any]] = []
    for row in rows:
        mass = row["edge_mass"]
        sign_word_edge_mass[row["sign_word"]] += mass
        sign_word_template_count[row["sign_word"]] += 1
        sign_balance_edge_mass[row["sign_balance"]] += mass
        q_prefix_edge_mass[row["q_prefix_count"]] += mass
        q_prefix_band_edge_mass[row["q_prefix_band"]] += mass
        m_shell_edge_mass[row["m_shell_prime_count"]] += mass
        m_shell_band_edge_mass[row["m_shell_band"]] += mass
        p_band_edge_mass[row["P_band"]] += mass
        q_m_band_edge_mass[(row["q_prefix_band"], row["m_shell_band"])] += mass
        sign_q_band_edge_mass[(row["sign_word"], row["q_prefix_band"])] += mass
        sign_m_band_edge_mass[(row["sign_word"], row["m_shell_band"])] += mass
        witness_rows.append(
            {
                "P": row["P"],
                "packet_index": row["packet_index"],
                "edge_mass": mass,
                "sign_word": row["sign_word"],
                "sign_balance": row["sign_balance"],
                "m_pair": row["m_pair"],
                "q_prefix_count": row["q_prefix_count"],
                "q_prefix_band": row["q_prefix_band"],
                "m_shell_prime_count": row["m_shell_prime_count"],
                "m_shell_band": row["m_shell_band"],
                "P_band": row["P_band"],
            }
        )

    total_template_count = len(rows)
    total_edge_mass = sum(row["edge_mass"] for row in rows)
    all_witness_mass_ten = all(row["edge_mass"] == 10 for row in rows)
    dominant_sign_word = max(sign_word_edge_mass, key=lambda key: sign_word_edge_mass[key])
    dominant_sign_word_mass = sign_word_edge_mass[dominant_sign_word]
    distinct_sign_words = len(sign_word_edge_mass)
    distinct_q_prefix_counts = len(q_prefix_edge_mass)
    distinct_m_shell_counts = len(m_shell_edge_mass)
    previous_largest_atom_rows = [
        row
        for row in previous["route_cycle_switch_edge_rows"]
        if row["route_label"] == TARGET_ROUTE
        and row["cycle_length"] == TARGET_CYCLE
        and row["sign_switch_count"] == TARGET_SWITCH
    ]
    previous_largest_atom_mass = previous_largest_atom_rows[0]["edge_mass"]

    ledger_closed = (
        previous_payload["top_two_core_route_cycle_switch_ledger_closed"]
        and previous_largest_atom_mass == 70
        and total_template_count == 7
        and total_edge_mass == previous_largest_atom_mass
        and total_edge_mass == 70
        and all_witness_mass_ten
        and distinct_sign_words == 5
        and dominant_sign_word == "--+-+"
        and dominant_sign_word_mass == 30
        and q_prefix_band_edge_mass["q<=10"] == 30
        and q_prefix_band_edge_mass["q>20"] == 30
        and q_prefix_band_edge_mass["q<=20"] == 10
        and m_shell_band_edge_mass["m<=8"] == 40
        and m_shell_band_edge_mass["m<=4"] == 30
        and distinct_q_prefix_counts == 5
        and distinct_m_shell_counts == 5
    )

    return {
        "max_prime": max_prime,
        "previous_top_two_core_route_cycle_switch_ledger_closed": previous_payload[
            "top_two_core_route_cycle_switch_ledger_closed"
        ],
        "largest_atom_template_witness_ledger_closed": ledger_closed,
        "target_route": TARGET_ROUTE,
        "target_cycle_length": TARGET_CYCLE,
        "target_sign_switch_count": TARGET_SWITCH,
        "previous_largest_atom_edge_mass": previous_largest_atom_mass,
        "witness_template_count": total_template_count,
        "witness_edge_mass": total_edge_mass,
        "all_witness_edge_mass_equals_10": all_witness_mass_ten,
        "distinct_sign_word_count": distinct_sign_words,
        "dominant_sign_word": dominant_sign_word,
        "dominant_sign_word_edge_mass": dominant_sign_word_mass,
        "dominant_sign_word_ratio": dominant_sign_word_mass / total_edge_mass,
        "distinct_q_prefix_count_count": distinct_q_prefix_counts,
        "distinct_m_shell_prime_count_count": distinct_m_shell_counts,
        "q_prefix_band_q_le_10_edge_mass": q_prefix_band_edge_mass["q<=10"],
        "q_prefix_band_q_le_20_edge_mass": q_prefix_band_edge_mass["q<=20"],
        "q_prefix_band_q_gt_20_edge_mass": q_prefix_band_edge_mass["q>20"],
        "m_shell_band_m_le_4_edge_mass": m_shell_band_edge_mass["m<=4"],
        "m_shell_band_m_le_8_edge_mass": m_shell_band_edge_mass["m<=8"],
        "sign_word_edge_rows": edge_rows(sign_word_edge_mass, total_edge_mass, "sign_word"),
        "sign_word_template_rows": template_rows(sign_word_template_count, total_template_count, "sign_word"),
        "sign_balance_edge_rows": edge_rows(sign_balance_edge_mass, total_edge_mass, "sign_balance"),
        "q_prefix_count_edge_rows": edge_rows(q_prefix_edge_mass, total_edge_mass, "q_prefix_count"),
        "q_prefix_band_edge_rows": edge_rows(q_prefix_band_edge_mass, total_edge_mass, "q_prefix_band"),
        "m_shell_prime_count_edge_rows": edge_rows(
            m_shell_edge_mass, total_edge_mass, "m_shell_prime_count"
        ),
        "m_shell_band_edge_rows": edge_rows(m_shell_band_edge_mass, total_edge_mass, "m_shell_band"),
        "P_band_edge_rows": edge_rows(p_band_edge_mass, total_edge_mass, "P_band"),
        "q_m_band_edge_rows": pair_rows(
            q_m_band_edge_mass,
            total_edge_mass,
            "q_prefix_band",
            "m_shell_band",
        ),
        "sign_q_band_edge_rows": pair_rows(
            sign_q_band_edge_mass,
            total_edge_mass,
            "sign_word",
            "q_prefix_band",
        ),
        "sign_m_band_edge_rows": pair_rows(
            sign_m_band_edge_mass,
            total_edge_mass,
            "sign_word",
            "m_shell_band",
        ),
        "template_witness_rows": sorted(
            witness_rows,
            key=lambda row: (row["P"], row["packet_index"], row["sign_word"], row["m_pair"]),
        ),
        "largest_atom_template_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_template_witness_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "largest_core_atom_template_witness_ledger_closed_family_bound_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the largest remaining core atom is now the smallest current finite carrier with edge mass 70",
        "current_object": {
            "input": "largest route-cycle-switch atom inside the top-two core",
            "operation": "split the 70 edge mass into exact template witnesses and sign/q/m subledgers",
            "dominant_shape": "7 equal-mass template witnesses; the largest sign word --+-+ carries edge mass 30",
            "remaining": "turn these finite witnesses into a uniform family bound or route the family through PDEC/SAE",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "TopTwoCoreRouteCycleSwitchLedgerImported",
                finite_audit["previous_top_two_core_route_cycle_switch_ledger_closed"],
                finite_audit["previous_top_two_core_route_cycle_switch_ledger_closed"],
                "The 11-atom top-two core ledger is imported.",
                "none for import",
            ),
            gate(
                "LargestCoreAtomTemplateWitnessLedger",
                finite_audit["largest_atom_template_witness_ledger_closed"],
                finite_audit["largest_atom_template_witness_ledger_closed"],
                "The 70-mass largest atom is split into 7 template witnesses.",
                "none for the finite witness ledger",
            ),
            gate(
                "DominantSignWordFamilyBound",
                False,
                False,
                "Control the dominant --+-+ sign-word family.",
                "finite audit shows mass 30 but no global theorem",
            ),
            gate(
                "AllSevenWitnessFamiliesOrPDEC",
                False,
                False,
                "Control the seven witness templates uniformly or route them through PDEC/SAE.",
                "requires a uniform lift beyond the finite audit range",
            ),
            gate(
                "ResidualCoreAtomBounds",
                False,
                False,
                "Control the other 10 route-cycle-switch atoms and the top-two noncore residual.",
                "carried forward from the core atom ledger",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_bilinear": "nontrivial below Polya-Vinogradov range after sheaf/trace completion; still not a fixed template witness theorem",
            "Milicevic_Qin_Wu_Kloosterman": "arbitrary-modulus bilinear Kloosterman power saving after completion; no direct local witness equality",
            "Wright_unbalanced_Kloosterman": "useful for unbalanced convolution ranges; does not estimate one fixed endpoint packet",
            "Li_short_intervals": "x^0.52 short interval prime existence is above theta=1/2 and does not see the signed template witness",
        },
        "latest_narrowest_mouth": [
            "DominantLargestAtomSignWordFamilyBound(--+-+)",
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
        "largest_atom_template_witness_ledger_closed": finite_audit[
            "largest_atom_template_witness_ledger_closed"
        ],
        "largest_atom_template_family_bound_proved": False,
        "dominant_sign_word_family_bound_proved": False,
        "all_seven_witness_families_bound_proved": False,
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
        "# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom template-witness 审计",
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
        "## 2. largest atom template-witness 分类审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"largest_atom_template_witness_ledger_closed={str(audit['largest_atom_template_witness_ledger_closed']).lower()}",
        f"target_route={audit['target_route']}",
        f"target_cycle_length={audit['target_cycle_length']}",
        f"target_sign_switch_count={audit['target_sign_switch_count']}",
        f"previous_largest_atom_edge_mass={audit['previous_largest_atom_edge_mass']}",
        f"witness_template_count={audit['witness_template_count']}",
        f"witness_edge_mass={audit['witness_edge_mass']}",
        f"all_witness_edge_mass_equals_10={str(audit['all_witness_edge_mass_equals_10']).lower()}",
        f"distinct_sign_word_count={audit['distinct_sign_word_count']}",
        f"dominant_sign_word={audit['dominant_sign_word']}",
        f"dominant_sign_word_edge_mass={audit['dominant_sign_word_edge_mass']}",
        f"dominant_sign_word_ratio={audit['dominant_sign_word_ratio']}",
        f"q_prefix_band_q_le_10_edge_mass={audit['q_prefix_band_q_le_10_edge_mass']}",
        f"q_prefix_band_q_le_20_edge_mass={audit['q_prefix_band_q_le_20_edge_mass']}",
        f"q_prefix_band_q_gt_20_edge_mass={audit['q_prefix_band_q_gt_20_edge_mass']}",
        f"m_shell_band_m_le_4_edge_mass={audit['m_shell_band_m_le_4_edge_mass']}",
        f"m_shell_band_m_le_8_edge_mass={audit['m_shell_band_m_le_8_edge_mass']}",
        f"row_column_unconditional_closed={str(audit['row_column_unconditional_closed']).lower()}",
        "```",
        "",
        "sign-word edge mass：",
        "",
        *markdown_table(audit["sign_word_edge_rows"], ["sign_word", "edge_mass", "edge_ratio"]),
        "",
        "q-prefix bands：",
        "",
        *markdown_table(audit["q_prefix_band_edge_rows"], ["q_prefix_band", "edge_mass", "edge_ratio"]),
        "",
        "m-shell bands：",
        "",
        *markdown_table(audit["m_shell_band_edge_rows"], ["m_shell_band", "edge_mass", "edge_ratio"]),
        "",
        "sign/q and sign/m bands：",
        "",
        *markdown_table(audit["sign_q_band_edge_rows"], ["sign_word", "q_prefix_band", "edge_mass", "edge_ratio"]),
        "",
        *markdown_table(audit["sign_m_band_edge_rows"], ["sign_word", "m_shell_band", "edge_mass", "edge_ratio"]),
        "",
        "template witnesses：",
        "",
        *markdown_table(
            audit["template_witness_rows"],
            [
                "P",
                "packet_index",
                "edge_mass",
                "sign_word",
                "sign_balance",
                "m_pair",
                "q_prefix_count",
                "q_prefix_band",
                "m_shell_prime_count",
                "m_shell_band",
                "P_band",
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
        "结论：最大 core atom 已被压成 7 个等质量模板见证。",
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
        f"largest_atom_template_witness_ledger_closed={str(payload['largest_atom_template_witness_ledger_closed']).lower()}",
        f"largest_atom_template_family_bound_proved={str(payload['largest_atom_template_family_bound_proved']).lower()}",
        f"dominant_sign_word_family_bound_proved={str(payload['dominant_sign_word_family_bound_proved']).lower()}",
        f"all_seven_witness_families_bound_proved={str(payload['all_seven_witness_families_bound_proved']).lower()}",
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
        "largest_atom_template_witness_ledger_closed="
        f"{payload['largest_atom_template_witness_ledger_closed']}"
    )
    print(f"witness_edge_mass={audit['witness_edge_mass']}")
    print(f"witness_template_count={audit['witness_template_count']}")
    print(f"dominant_sign_word={audit['dominant_sign_word']}")
    print(f"row_column_unconditional_closed={payload['row_column_unconditional_closed']}")


if __name__ == "__main__":
    main()
