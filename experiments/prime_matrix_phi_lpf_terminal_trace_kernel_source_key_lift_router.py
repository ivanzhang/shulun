#!/usr/bin/env python3
"""把 terminal trace-kernel 接口降到 source-key lift 的实际门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_trace_kernel_source_key_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CONTRACT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json"
ADJACENT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json"
PREFIX_JSON = DOCS / "prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json"
PARTITION_JSON = DOCS / "prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json"
BOUNDARY_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json"
SIBLING_QSPINE_JSON = DOCS / "prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json"
NEW_TAIL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json"
OLD_TAIL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json"

SOURCE_FILES = [
    Path(__file__).resolve(),
    CONTRACT_JSON,
    ADJACENT_JSON,
    PREFIX_JSON,
    PARTITION_JSON,
    BOUNDARY_JSON,
    SIBLING_QSPINE_JSON,
    NEW_TAIL_JSON,
    OLD_TAIL_JSON,
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "TraceKernelSourceKeyLiftReductionClosed "
    "AND BoundaryRatioSourceKeyLawOrPDEC "
    "AND NonBoundaryRecordJumpSourceKeyLiftOrPDEC "
    "AND InternalSurvivorPDEC "
    "AND TerminalSiblingQSpinePaymentOrPDEC "
    "AND PrimitiveOrientationLocalFactorProductLawBeforePushforward "
    "AND UniformAdjacentRunCancellationStillOpen"
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
    """把证书里的 fraction/decimal 字段压成短文本。"""
    if isinstance(value, dict):
        frac = value.get("fraction")
        dec = value.get("decimal")
        if frac and dec:
            return f"{dec} ({frac})"
        return str(frac or dec or value)
    return str(value)


def contract_map(contract: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """按合同名索引上一层 trace-admissibility 合同。"""
    return {row["contract"]: row for row in contract.get("trace_admissibility_contract", [])}


def build_kernel_dependency_rows(
    adjacent: dict[str, Any],
    prefix: dict[str, Any],
    partition: dict[str, Any],
    boundary: dict[str, Any],
    sibling: dict[str, Any],
) -> list[dict[str, Any]]:
    """组装 trace kernel 的实际依赖门。"""
    return [
        {
            "gate": "FormalJordanPhaseKernel",
            "closed": bool(adjacent.get("formal_jordan_cancellation_law_closed")),
            "proved": bool(adjacent.get("formal_jordan_cancellation_law_closed")),
            "load": f"{adjacent.get('terminal_transition_count_total')} transitions, "
            f"{adjacent.get('terminal_run_count_total')} runs",
            "meaning": "A(q)/q signed telescoping gives a finite post-pushforward phase kernel.",
            "remaining": "not yet a pre-Cauchy trace kernel",
        },
        {
            "gate": "PrefixRecordReflectionSchema",
            "closed": bool(prefix.get("prefix_record_reflection_schema_closed")),
            "proved": bool(prefix.get("prefix_record_reflection_schema_closed")),
            "load": f"{prefix.get('cancellation_event_count')} cancellation events",
            "meaning": "formal cancellation is a deterministic prefix-record reflection ledger.",
            "remaining": "source-key lift still open",
        },
        {
            "gate": "BoundaryRatioSourceKeyLaw",
            "closed": bool(boundary.get("boundary_ratio_spectrum_closed")),
            "proved": bool(boundary.get("boundary_synthetic_split_ratio_source_key_law_proved")),
            "load": f"{partition.get('q_boundary_synthetic_split_event_count')} q-boundary events",
            "meaning": "the dominant synthetic-split mass is adjacent in q but has unequal old/new run ratios.",
            "remaining": "BoundaryAdjacentRunMassRatioLawOrPDEC",
        },
        {
            "gate": "NonBoundaryRecordJumpSourceKeyLift",
            "closed": bool(partition.get("source_key_obstruction_partition_closed")),
            "proved": bool(partition.get("nonboundary_record_jump_source_key_lift_constructed")),
            "load": f"{partition.get('nonboundary_record_jump_event_count')} events on "
            f"{partition.get('nonboundary_record_jump_atom_count')} atoms",
            "meaning": "these cancellations jump across q-boundaries and cannot be certified by adjacent q-locality.",
            "remaining": "NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC",
        },
        {
            "gate": "InternalPrefixRecordSurvivor",
            "closed": bool(partition.get("source_key_obstruction_partition_closed")),
            "proved": bool(partition.get("internal_survivor_pdec_constructed")),
            "load": f"{partition.get('internal_survivor_fragment_count')} internal survivor fragment",
            "meaning": "a selected-terminal survivor lies inside the run path, not only at the terminal tail.",
            "remaining": "InternalPrefixRecordSurvivorPDEC",
        },
        {
            "gate": "SiblingQSpineKernelPayment",
            "closed": bool(sibling.get("terminal_double_awrap_sibling_qspine_kernel_closed")),
            "proved": bool(sibling.get("terminal_double_awrap_sibling_qspine_kernel_payment_law_proved")),
            "load": "m769/m773 shared double-Awrap q-spine",
            "meaning": "a finite P-scaled q-spine identity exists for the m773 tail packet.",
            "remaining": "TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC",
        },
    ]


def build_contract_reduction_rows(contracts: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把六接口合同压到本层依赖门。"""
    return [
        {
            "contract": "TerminalRunKernelFormula",
            "previous_proved": contracts["TerminalRunKernelFormula"]["proved"],
            "reduced_here": True,
            "proved_here": False,
            "actual_dependencies": (
                "FormalJordanPhaseKernel AND BoundaryRatioSourceKeyLaw AND "
                "NonBoundaryRecordJumpSourceKeyLift AND InternalPrefixRecordSurvivor "
                "AND SiblingQSpineKernelPayment AND PrimitiveOrientationLocalFactorProductLaw"
            ),
            "failure_return": "MissingTraceKernelFormulaPDEC",
        },
        {
            "contract": "SameTraceKeySourceConsistency",
            "previous_proved": contracts["SameTraceKeySourceConsistency"]["proved"],
            "reduced_here": True,
            "proved_here": False,
            "actual_dependencies": (
                "PrefixRecordSourceKeyLift AND BoundaryResidualFlowSourceKeyConservation "
                "AND PrimitiveOrientationLocalFactorProductLaw"
            ),
            "failure_return": "SameTraceKeySplitPDEC",
        },
        {
            "contract": "UniformFamilyInP",
            "previous_proved": contracts["UniformFamilyInP"]["proved"],
            "reduced_here": False,
            "proved_here": False,
            "actual_dependencies": "only meaningful after a forward source-key kernel exists",
            "failure_return": "FiniteLedgerOnlyLocalSurvivor",
        },
        {
            "contract": "TypeIICoefficientFactorability",
            "previous_proved": contracts["TypeIICoefficientFactorability"]["proved"],
            "reduced_here": False,
            "proved_here": False,
            "actual_dependencies": "requires source-keyed signed coefficients before factorability can be tested",
            "failure_return": "TypeIIFactorabilityFailureSAE",
        },
        {
            "contract": "ConductorOrModulusControl",
            "previous_proved": contracts["ConductorOrModulusControl"]["proved"],
            "reduced_here": False,
            "proved_here": False,
            "actual_dependencies": "requires an actual kernel family before conductor/modulus can be assigned",
            "failure_return": "ConductorRangePDEC",
        },
        {
            "contract": "UniformAdjacentRunCancellation",
            "previous_proved": contracts["UniformAdjacentRunCancellation"]["proved"],
            "reduced_here": True,
            "proved_here": False,
            "actual_dependencies": (
                "BoundaryRatioSourceKeyLaw AND NonBoundaryRecordJumpSourceKeyLift "
                "AND InternalPrefixRecordSurvivor"
            ),
            "failure_return": "AdjacentRunCancellationFailureLocalSurvivor",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    contract = load_json(CONTRACT_JSON)
    adjacent = load_json(ADJACENT_JSON)
    prefix = load_json(PREFIX_JSON)
    partition = load_json(PARTITION_JSON)
    boundary = load_json(BOUNDARY_JSON)
    sibling = load_json(SIBLING_QSPINE_JSON)
    new_tail = load_json(NEW_TAIL_JSON)
    old_tail = load_json(OLD_TAIL_JSON)
    contracts = contract_map(contract)

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_trace_kernel_source_key_lift_router",
        "status": "terminal_trace_kernel_source_key_lift_reduction_closed_kernel_open",
        "verified_date": "2026-05-26",
        "imported_trace_contract_status": contract.get("status"),
        "formal_jordan_phase_kernel_closed": bool(adjacent.get("formal_jordan_cancellation_law_closed")),
        "prefix_record_reflection_schema_closed": bool(prefix.get("prefix_record_reflection_schema_closed")),
        "source_key_obstruction_partition_closed": bool(partition.get("source_key_obstruction_partition_closed")),
        "boundary_ratio_spectrum_closed": bool(boundary.get("boundary_ratio_spectrum_closed")),
        "sibling_qspine_finite_kernel_closed": bool(sibling.get("terminal_double_awrap_sibling_qspine_kernel_closed")),
        "terminal_run_kernel_formula_reduced_to_actual_source_key_gates": True,
        "same_trace_key_source_consistency_reduced_to_actual_source_key_gates": True,
        "terminal_run_kernel_formula_proved": False,
        "same_trace_key_source_consistency_proved": False,
        "trace_or_typeii_family_admissible_now": False,
        "external_theorems_directly_attach_now": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "event_reduction_summary": {
            "terminal_transition_count_total": adjacent.get("terminal_transition_count_total"),
            "terminal_run_count_total": adjacent.get("terminal_run_count_total"),
            "cancellation_event_count": partition.get("cancellation_event_count"),
            "synthetic_split_event_count": partition.get("synthetic_split_event_count"),
            "q_boundary_synthetic_split_event_count": partition.get("q_boundary_synthetic_split_event_count"),
            "nonboundary_record_jump_event_count": partition.get("nonboundary_record_jump_event_count"),
            "internal_survivor_fragment_count": partition.get("internal_survivor_fragment_count"),
            "tail_survivor_fragment_count": partition.get("tail_survivor_fragment_count"),
            "old_consumed_new_residual_event_count": boundary.get("old_consumed_new_residual_event_count"),
            "old_residual_new_consumed_event_count": boundary.get("old_residual_new_consumed_event_count"),
            "whole_equal_pair_event_count": boundary.get("whole_equal_pair_event_count"),
        },
        "boundary_ratio_summary": {
            "ratio_min": compact(boundary.get("ratio_min")),
            "ratio_max": compact(boundary.get("ratio_max")),
            "boundary_chunk_mass_total": compact(boundary.get("boundary_chunk_mass_total")),
            "boundary_residual_gap_mass_total": compact(boundary.get("boundary_residual_gap_mass_total")),
            "boundary_residual_gap_mass_max": compact(boundary.get("boundary_residual_gap_mass_max")),
            "finite_margin_after_nonboundary_internal_payment_positive": bool(
                partition.get("finite_margin_after_nonboundary_internal_payment_positive")
            ),
            "nonboundary_plus_internal_obstruction_mass": compact(
                partition.get("nonboundary_plus_internal_obstruction_mass")
            ),
            "selected_finite_margin_after_nonboundary_internal_payment": compact(
                partition.get("selected_finite_margin_after_nonboundary_internal_payment")
            ),
        },
        "tail_alignment_summary": {
            "old_residual_return_alignment_closed": bool(old_tail.get("old_residual_return_alignment_closed")),
            "new_residual_tail_alignment_partial_closed": bool(new_tail.get("new_residual_tail_alignment_partial_closed")),
            "new_residual_event_count": new_tail.get("new_residual_event_count"),
            "new_residual_unmatched_after_tail_event_count": new_tail.get(
                "new_residual_unmatched_after_tail_event_count"
            ),
            "terminal_double_awrap_sibling_qspine_kernel_payment_law_proved": bool(
                sibling.get("terminal_double_awrap_sibling_qspine_kernel_payment_law_proved")
            ),
        },
        "kernel_dependency_rows": build_kernel_dependency_rows(adjacent, prefix, partition, boundary, sibling),
        "contract_reduction_rows": build_contract_reduction_rows(contracts),
        "next_primary_attack_target": "BoundaryRatioSourceKeyLawOrPDEC",
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The terminal trace-kernel problem is no longer a single opaque interface. "
            "The formal A(q)/q Jordan phase kernel and prefix-record reflection ledger are closed. "
            "A forward trace kernel still requires source-key lift: 47 adjacent q-boundary split ratios, "
            "4 non-boundary record jumps, 1 internal survivor, and the m773 sibling q-spine payment law "
            "must be proved or returned as named PDEC/SAE/LocalSurvivor gates.  Therefore external "
            "trace/Kloosterman/Type-II theorems remain unavailable at this layer."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    summary = payload["event_reduction_summary"]
    boundary = payload["boundary_ratio_summary"]
    tail = payload["tail_alignment_summary"]
    lines = [
        "# Prime Matrix Phi-LPF terminal trace-kernel source-key lift 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 总裁定",
        "",
        "```text",
        f"formal_jordan_phase_kernel_closed={fmt_bool(payload['formal_jordan_phase_kernel_closed'])}",
        f"prefix_record_reflection_schema_closed={fmt_bool(payload['prefix_record_reflection_schema_closed'])}",
        f"source_key_obstruction_partition_closed={fmt_bool(payload['source_key_obstruction_partition_closed'])}",
        f"boundary_ratio_spectrum_closed={fmt_bool(payload['boundary_ratio_spectrum_closed'])}",
        f"sibling_qspine_finite_kernel_closed={fmt_bool(payload['sibling_qspine_finite_kernel_closed'])}",
        "terminal_run_kernel_formula_reduced_to_actual_source_key_gates="
        f"{fmt_bool(payload['terminal_run_kernel_formula_reduced_to_actual_source_key_gates'])}",
        f"terminal_run_kernel_formula_proved={fmt_bool(payload['terminal_run_kernel_formula_proved'])}",
        f"same_trace_key_source_consistency_proved={fmt_bool(payload['same_trace_key_source_consistency_proved'])}",
        f"trace_or_typeii_family_admissible_now={fmt_bool(payload['trace_or_typeii_family_admissible_now'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. event reduction 摘要",
        "",
        "```text",
        f"terminal_transition_count_total={summary['terminal_transition_count_total']}",
        f"terminal_run_count_total={summary['terminal_run_count_total']}",
        f"cancellation_event_count={summary['cancellation_event_count']}",
        f"synthetic_split_event_count={summary['synthetic_split_event_count']}",
        f"q_boundary_synthetic_split_event_count={summary['q_boundary_synthetic_split_event_count']}",
        f"nonboundary_record_jump_event_count={summary['nonboundary_record_jump_event_count']}",
        f"internal_survivor_fragment_count={summary['internal_survivor_fragment_count']}",
        f"tail_survivor_fragment_count={summary['tail_survivor_fragment_count']}",
        f"whole_equal_pair_event_count={summary['whole_equal_pair_event_count']}",
        "```",
        "",
        "## 3. boundary ratio 摘要",
        "",
        "```text",
        f"ratio_min={boundary['ratio_min']}",
        f"ratio_max={boundary['ratio_max']}",
        f"boundary_chunk_mass_total={boundary['boundary_chunk_mass_total']}",
        f"boundary_residual_gap_mass_total={boundary['boundary_residual_gap_mass_total']}",
        f"boundary_residual_gap_mass_max={boundary['boundary_residual_gap_mass_max']}",
        "finite_margin_after_nonboundary_internal_payment_positive="
        f"{fmt_bool(boundary['finite_margin_after_nonboundary_internal_payment_positive'])}",
        "```",
        "",
        "## 4. tail/q-spine 摘要",
        "",
        "```text",
        f"old_residual_return_alignment_closed={fmt_bool(tail['old_residual_return_alignment_closed'])}",
        f"new_residual_tail_alignment_partial_closed={fmt_bool(tail['new_residual_tail_alignment_partial_closed'])}",
        f"new_residual_event_count={tail['new_residual_event_count']}",
        f"new_residual_unmatched_after_tail_event_count={tail['new_residual_unmatched_after_tail_event_count']}",
        "terminal_double_awrap_sibling_qspine_kernel_payment_law_proved="
        f"{fmt_bool(tail['terminal_double_awrap_sibling_qspine_kernel_payment_law_proved'])}",
        "```",
        "",
        "## 5. trace kernel 依赖门",
        "",
        "| gate | closed | proved | load | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["kernel_dependency_rows"]:
        lines.append(
            f"| {row['gate']} | {fmt_bool(row['closed'])} | {fmt_bool(row['proved'])} | "
            f"{row['load']} | {row['remaining']} |"
        )

    lines.extend(
        [
            "",
            "## 6. 六接口合同降维",
            "",
            "| contract | reduced here | proved here | actual dependencies | failure return |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["contract_reduction_rows"]:
        lines.append(
            f"| {row['contract']} | {fmt_bool(row['reduced_here'])} | "
            f"{fmt_bool(row['proved_here'])} | {row['actual_dependencies']} | {row['failure_return']} |"
        )

    lines.extend(
        [
            "",
            "## 7. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 8. 依赖哈希",
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
    print(f"terminal_run_kernel_formula_proved={fmt_bool(payload['terminal_run_kernel_formula_proved'])}")
    print(f"next_primary_attack_target={payload['next_primary_attack_target']}")


if __name__ == "__main__":
    main()
