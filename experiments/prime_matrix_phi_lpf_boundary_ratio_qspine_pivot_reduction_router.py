#!/usr/bin/env python3
"""把 boundary ratio source-key 门降到 q-spine pivot enclosure。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_boundary_ratio_qspine_pivot_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-router.json

输出：
  data/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-ledger.json
  docs/monograph/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-router.json
  docs/monograph/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TRACE_KERNEL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json"
RESIDUAL_FLOW_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json"
OLD_RETURN_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json"
NEW_TAIL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json"
BULK_CARRY_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json"
CARRY_BREAK_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json"
PIVOT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json"
SIBLING_QSPINE_JSON = DOCS / "prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json"

SOURCE_FILES = [
    Path(__file__).resolve(),
    TRACE_KERNEL_JSON,
    RESIDUAL_FLOW_JSON,
    OLD_RETURN_JSON,
    NEW_TAIL_JSON,
    BULK_CARRY_JSON,
    CARRY_BREAK_JSON,
    PIVOT_JSON,
    SIBLING_QSPINE_JSON,
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "BoundaryRatioQSpinePivotReductionClosed "
    "AND BridgeRootQSpinePivotEnclosureLawOrPDEC "
    "AND RightSelectedTerminalTailOverhangPDEC "
    "AND TerminalSiblingQSpinePaymentOrPDEC "
    "AND PrimitiveOrientationLocalFactorProductLawBeforePushforward "
    "AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving "
    "AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def compact(value: Any) -> str:
    """把 fraction/decimal 字段压成短文本。"""
    if isinstance(value, dict):
        frac = value.get("fraction")
        dec = value.get("decimal")
        if frac and dec:
            return f"{dec} ({frac})"
        return str(frac or dec or value)
    return str(value)


def dependency_rows(
    residual: dict[str, Any],
    old_return: dict[str, Any],
    new_tail: dict[str, Any],
    bulk: dict[str, Any],
    carry: dict[str, Any],
    pivot: dict[str, Any],
    sibling: dict[str, Any],
) -> list[dict[str, Any]]:
    """把 boundary ratio law 的实际依赖逐层列出。"""
    return [
        {
            "gate": "ResidualFlowSideLedger",
            "closed": bool(residual.get("residual_flow_side_decomposition_closed")),
            "proved": bool(residual.get("residual_flow_side_decomposition_closed")),
            "load": f"{residual.get('new_residual_side_event_count')} new-side, "
            f"{residual.get('old_residual_side_event_count')} old-side",
            "remaining": "local conservation refuted; route to residual transport",
        },
        {
            "gate": "OldResidualReturnAlignment",
            "closed": bool(old_return.get("old_residual_return_alignment_closed")),
            "proved": bool(old_return.get("old_residual_return_alignment_closed")),
            "load": f"{old_return.get('old_residual_event_count')} old residuals",
            "remaining": "old-side transport closed only",
        },
        {
            "gate": "NewResidualTailAlignment",
            "closed": bool(new_tail.get("new_residual_tail_alignment_partial_closed")),
            "proved": bool(new_tail.get("new_residual_tail_alignment_partial_closed")),
            "load": f"{new_tail.get('new_residual_tail_matched_event_count')} matched, "
            f"{new_tail.get('new_residual_unmatched_after_tail_event_count')} unmatched",
            "remaining": "bulk new residual source law",
        },
        {
            "gate": "BulkCarryChainNormalForm",
            "closed": bool(bulk.get("bulk_carry_chain_normal_form_closed")),
            "proved": bool(bulk.get("bulk_carry_chain_normal_form_closed")),
            "load": f"{bulk.get('carry_segment_count')} carry segments, "
            f"{bulk.get('carry_transition_count')} transitions",
            "remaining": "carry segment roots and breaks",
        },
        {
            "gate": "CarryBreakSourcePackets",
            "closed": bool(carry.get("carry_break_source_packet_reduction_closed")),
            "proved": bool(carry.get("carry_break_source_packet_reduction_closed")),
            "load": f"{carry.get('bridge_root_debt_break_count')} bridge debts, "
            f"{carry.get('unit_old_return_echo_break_count')} unit echoes",
            "remaining": "bridge-root debt source law",
        },
        {
            "gate": "BridgeRootQSpinePivotEnclosure",
            "closed": bool(pivot.get("bridge_root_qspine_pivot_enclosure_reduction_closed")),
            "proved": bool(pivot.get("bridge_root_qspine_pivot_enclosure_reduction_closed")),
            "load": f"{pivot.get('pivot_enclosure_row_count')} pivot rows, "
            f"{pivot.get('exact_pivot_contact_count')} exact contact",
            "remaining": "uniform pivot enclosure law",
        },
        {
            "gate": "TerminalSiblingQSpinePayment",
            "closed": bool(sibling.get("terminal_double_awrap_sibling_qspine_kernel_closed")),
            "proved": bool(sibling.get("terminal_double_awrap_sibling_qspine_kernel_payment_law_proved")),
            "load": "right m769/m773 q-spine packet",
            "remaining": "terminal sibling q-spine payment law",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    trace = load_json(TRACE_KERNEL_JSON)
    residual = load_json(RESIDUAL_FLOW_JSON)
    old_return = load_json(OLD_RETURN_JSON)
    new_tail = load_json(NEW_TAIL_JSON)
    bulk = load_json(BULK_CARRY_JSON)
    carry = load_json(CARRY_BREAK_JSON)
    pivot = load_json(PIVOT_JSON)
    sibling = load_json(SIBLING_QSPINE_JSON)

    chain_closed = all(
        [
            trace.get("terminal_run_kernel_formula_reduced_to_actual_source_key_gates") is True,
            residual.get("residual_flow_side_decomposition_closed") is True,
            old_return.get("old_residual_return_alignment_closed") is True,
            new_tail.get("new_residual_tail_alignment_partial_closed") is True,
            bulk.get("bulk_carry_chain_normal_form_closed") is True,
            carry.get("carry_break_source_packet_reduction_closed") is True,
            pivot.get("bridge_root_qspine_pivot_enclosure_reduction_closed") is True,
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_boundary_ratio_qspine_pivot_reduction_router",
        "status": "boundary_ratio_reduced_to_qspine_pivot_enclosure_uniform_law_open",
        "verified_date": "2026-05-26",
        "imported_trace_kernel_status": trace.get("status"),
        "boundary_ratio_source_key_law_reduced_to_qspine_pivot": chain_closed,
        "old_residual_side_closed": bool(old_return.get("old_residual_return_alignment_closed")),
        "new_residual_tail_alignment_partial_closed": bool(new_tail.get("new_residual_tail_alignment_partial_closed")),
        "bulk_carry_chain_normal_form_closed": bool(bulk.get("bulk_carry_chain_normal_form_closed")),
        "carry_break_source_packet_reduction_closed": bool(carry.get("carry_break_source_packet_reduction_closed")),
        "bridge_root_qspine_pivot_enclosure_reduction_closed": bool(
            pivot.get("bridge_root_qspine_pivot_enclosure_reduction_closed")
        ),
        "bridge_root_uniform_qspine_pivot_enclosure_law_proved": False,
        "right_selected_terminal_tail_overhang_pdec_constructed": False,
        "terminal_sibling_qspine_payment_law_proved": bool(
            sibling.get("terminal_double_awrap_sibling_qspine_kernel_payment_law_proved")
        ),
        "trace_or_typeii_family_admissible_now": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "residual_flow_summary": {
            "q_boundary_synthetic_split_event_count": residual.get("q_boundary_synthetic_split_event_count"),
            "new_residual_side_event_count": residual.get("new_residual_side_event_count"),
            "old_residual_side_event_count": residual.get("old_residual_side_event_count"),
            "new_residual_mass_total": compact(residual.get("new_residual_mass_total")),
            "old_residual_mass_total": compact(residual.get("old_residual_mass_total")),
            "net_new_minus_old_residual_mass": compact(residual.get("net_new_minus_old_residual_mass")),
            "finite_boundary_local_opposite_side_cancellation_refuted": bool(
                residual.get("finite_boundary_local_opposite_side_cancellation_refuted")
            ),
        },
        "return_and_bulk_summary": {
            "old_residual_return_aligned_event_count": old_return.get("old_residual_return_aligned_event_count"),
            "new_residual_tail_matched_event_count": new_tail.get("new_residual_tail_matched_event_count"),
            "new_residual_unmatched_after_tail_event_count": new_tail.get(
                "new_residual_unmatched_after_tail_event_count"
            ),
            "new_residual_unmatched_after_tail_mass": compact(new_tail.get("new_residual_unmatched_after_tail_mass")),
            "carry_segment_count": bulk.get("carry_segment_count"),
            "carry_transition_count": bulk.get("carry_transition_count"),
            "carry_break_count": bulk.get("carry_break_count"),
            "bridge_root_debt_break_count": carry.get("bridge_root_debt_break_count"),
            "bridge_root_debt_still_open": compact(carry.get("bridge_root_debt_open_mass")),
        },
        "qspine_pivot_summary": {
            "q_spine_nodes": pivot.get("q_spine_nodes"),
            "shared_pivot_q": pivot.get("shared_pivot_q"),
            "shared_pivot_index": pivot.get("shared_pivot_index"),
            "pivot_enclosure_row_count": pivot.get("pivot_enclosure_row_count"),
            "exact_pivot_contact_count": pivot.get("exact_pivot_contact_count"),
            "finite_pivot_enclosure_closed": bool(pivot.get("finite_pivot_enclosure_closed")),
            "endpoint_slack_equals_pivot_gap_sum_closed": bool(
                pivot.get("endpoint_slack_equals_pivot_gap_sum_closed")
            ),
        },
        "dependency_rows": dependency_rows(residual, old_return, new_tail, bulk, carry, pivot, sibling),
        "next_primary_attack_target": "BridgeRootQSpinePivotEnclosureLawOrPDEC",
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The boundary ratio source-key law has been reduced past residual-side bookkeeping: "
            "old-side residuals are exactly returned, six new-side residuals are terminal-tail returns, "
            "the remaining bulk is in carry-chain normal form, carry breaks are packetized, and the "
            "two bridge-root debts are enclosed by a finite q-spine pivot ledger.  The proof is still "
            "not closed: a uniform pivot-enclosure law, right-tail overhang PDEC, terminal sibling "
            "q-spine payment, and primitive orientation/local-factor source law are still missing."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    residual = payload["residual_flow_summary"]
    bulk = payload["return_and_bulk_summary"]
    pivot = payload["qspine_pivot_summary"]
    lines = [
        "# Prime Matrix Phi-LPF boundary ratio q-spine pivot reduction 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 总裁定",
        "",
        "```text",
        "boundary_ratio_source_key_law_reduced_to_qspine_pivot="
        f"{fmt_bool(payload['boundary_ratio_source_key_law_reduced_to_qspine_pivot'])}",
        f"old_residual_side_closed={fmt_bool(payload['old_residual_side_closed'])}",
        "new_residual_tail_alignment_partial_closed="
        f"{fmt_bool(payload['new_residual_tail_alignment_partial_closed'])}",
        f"bulk_carry_chain_normal_form_closed={fmt_bool(payload['bulk_carry_chain_normal_form_closed'])}",
        "carry_break_source_packet_reduction_closed="
        f"{fmt_bool(payload['carry_break_source_packet_reduction_closed'])}",
        "bridge_root_qspine_pivot_enclosure_reduction_closed="
        f"{fmt_bool(payload['bridge_root_qspine_pivot_enclosure_reduction_closed'])}",
        "bridge_root_uniform_qspine_pivot_enclosure_law_proved="
        f"{fmt_bool(payload['bridge_root_uniform_qspine_pivot_enclosure_law_proved'])}",
        f"trace_or_typeii_family_admissible_now={fmt_bool(payload['trace_or_typeii_family_admissible_now'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. residual flow 摘要",
        "",
        "```text",
        f"q_boundary_synthetic_split_event_count={residual['q_boundary_synthetic_split_event_count']}",
        f"new_residual_side_event_count={residual['new_residual_side_event_count']}",
        f"old_residual_side_event_count={residual['old_residual_side_event_count']}",
        f"new_residual_mass_total={residual['new_residual_mass_total']}",
        f"old_residual_mass_total={residual['old_residual_mass_total']}",
        f"net_new_minus_old_residual_mass={residual['net_new_minus_old_residual_mass']}",
        "finite_boundary_local_opposite_side_cancellation_refuted="
        f"{fmt_bool(residual['finite_boundary_local_opposite_side_cancellation_refuted'])}",
        "```",
        "",
        "## 3. return/bulk 摘要",
        "",
        "```text",
        f"old_residual_return_aligned_event_count={bulk['old_residual_return_aligned_event_count']}",
        f"new_residual_tail_matched_event_count={bulk['new_residual_tail_matched_event_count']}",
        "new_residual_unmatched_after_tail_event_count="
        f"{bulk['new_residual_unmatched_after_tail_event_count']}",
        f"new_residual_unmatched_after_tail_mass={bulk['new_residual_unmatched_after_tail_mass']}",
        f"carry_segment_count={bulk['carry_segment_count']}",
        f"carry_transition_count={bulk['carry_transition_count']}",
        f"carry_break_count={bulk['carry_break_count']}",
        f"bridge_root_debt_break_count={bulk['bridge_root_debt_break_count']}",
        f"bridge_root_debt_still_open={bulk['bridge_root_debt_still_open']}",
        "```",
        "",
        "## 4. q-spine pivot 摘要",
        "",
        "```text",
        f"q_spine_nodes={pivot['q_spine_nodes']}",
        f"shared_pivot_q={pivot['shared_pivot_q']}",
        f"shared_pivot_index={pivot['shared_pivot_index']}",
        f"pivot_enclosure_row_count={pivot['pivot_enclosure_row_count']}",
        f"exact_pivot_contact_count={pivot['exact_pivot_contact_count']}",
        f"finite_pivot_enclosure_closed={fmt_bool(pivot['finite_pivot_enclosure_closed'])}",
        "endpoint_slack_equals_pivot_gap_sum_closed="
        f"{fmt_bool(pivot['endpoint_slack_equals_pivot_gap_sum_closed'])}",
        "```",
        "",
        "## 5. 依赖门",
        "",
        "| gate | closed | proved | load | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["dependency_rows"]:
        lines.append(
            f"| {row['gate']} | {fmt_bool(row['closed'])} | {fmt_bool(row['proved'])} | "
            f"{row['load']} | {row['remaining']} |"
        )

    lines.extend(
        [
            "",
            "## 6. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in payload["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(
        "boundary_ratio_source_key_law_reduced_to_qspine_pivot="
        f"{fmt_bool(payload['boundary_ratio_source_key_law_reduced_to_qspine_pivot'])}"
    )
    print(f"next_primary_attack_target={payload['next_primary_attack_target']}")


if __name__ == "__main__":
    main()
