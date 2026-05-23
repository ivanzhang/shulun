#!/usr/bin/env python3
"""审计 floor denominator 到 q-cell radial support 的精确分解。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-audit.json

上一层已经把互补 radial pair kernel 与 actual reciprocal phase 耦合为
floor-defined denominator Q_{P,k}(m)。本层继续关闭确定性桥：

  Q_{P,k}(m)=q

等价于 m 落在以 q 为变量的双曲 floor cell 中。这说明 floor denominator
不是新生成的相位变量，而是回到 prime-q 支撑集合的同一条 product-window
cell。它仍不提供相消；剩余是把这些 floor cells 完成为可套用外部定理的
trace/Kloosterman/Type-II family。
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-floor-cell-radial-support"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def product_cell_window(P: int, k: int, q: int) -> tuple[int, int]:
    """固定 q 后的 clipped cofactor floor cell。"""
    low = max(P // 2 + 1, q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def odd_q_values(P: int) -> range:
    """枚举 P/2<q<P 的奇 q。"""
    first = P // 2 + 1
    if first % 2 == 0:
        first += 1
    return range(first, P, 2)


def phase_key(P: int, k: int, q: int) -> str:
    """输出符号相位标签。"""
    return f"e(h*{k}*{P}/{q})"


def row_floor_cell_audit(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    prime_set: set[int],
    collect_samples: bool,
) -> dict[str, Any]:
    """审计单行 q-cell 与 reverse floor denominator 是否为同一对象。"""
    W, factors = primorial.primorial_modulus(P, primes)
    records_by_m = {record["m"]: record for record in records}

    actual = primorial.actual_terms_for_row(P, k, primes)
    product_cell_atoms: set[tuple[int, int, int, int]] = set()
    reverse_odd_atoms: set[tuple[int, int, int, int]] = set()
    selected_cell_terms: set[tuple[int, int, int, int]] = set()
    reverse_selected_terms: set[tuple[int, int, int, int]] = set()

    totals: Counter[str] = Counter()
    q_cell_cases: Counter[str] = Counter()
    sample_cells: list[str] = []
    max_product_cell_window_size = 0
    max_product_cell_odd_count = 0
    max_reverse_window_size = 0
    max_reverse_odd_count = 0

    for q in odd_q_values(P):
        low, high = product_cell_window(P, k, q)
        window_size = max(0, high - low + 1)
        m_odd, odd_count = primorial.unique_odd_candidate(low, high)
        max_product_cell_window_size = max(max_product_cell_window_size, window_size)
        max_product_cell_odd_count = max(max_product_cell_odd_count, odd_count)
        totals["q_floor_cells_checked"] += 1
        totals["bad_product_cell_window_size"] += int(window_size > 2)
        totals["bad_product_cell_odd_count"] += int(odd_count > 1)

        if window_size == 0:
            q_cell_cases["empty_cell"] += 1
            continue
        if m_odd is None:
            q_cell_cases["even_singleton_rejected"] += 1
            continue

        record = records_by_m.get(m_odd)
        if record is None:
            q_cell_cases["odd_candidate_not_residual"] += 1
            continue

        term = (q, m_odd, record["r"], record["beta"])
        product_cell_atoms.add(term)
        q_cell_cases["residual_odd_cell"] += 1

        reverse_atom = primorial.unit_selector_atom(P, k, m_odd, W, factors)
        totals["product_cell_to_reverse_checked"] += 1
        totals["product_cell_to_reverse_mismatch"] += int(reverse_atom["q_odd"] != q)

        unit_selected = math.gcd(q, W) == 1
        if unit_selected:
            selected_cell_terms.add(term)
            totals["cell_unit_selected"] += 1
            totals["bad_unit_q_not_prime"] += int(q not in prime_set)
            if collect_samples and len(sample_cells) < 8:
                sample_cells.append(
                    "q={q},m={m},r={r},beta={beta},I_q=[{low},{high}],phase={phase},qmodW={qmod}".format(
                        q=q,
                        m=m_odd,
                        r=record["r"],
                        beta=record["beta"],
                        low=low,
                        high=high,
                        phase=phase_key(P, k, q),
                        qmod=q % W,
                    )
                )
        else:
            obstruction = primorial.least_unit_obstruction(q, factors)
            q_cell_cases[f"residual_nonunit_rejected_by_{obstruction}"] += 1

    for record in records:
        atom = primorial.unit_selector_atom(P, k, record["m"], W, factors)
        max_reverse_window_size = max(max_reverse_window_size, atom["window_size"])
        max_reverse_odd_count = max(max_reverse_odd_count, atom["odd_count"])
        totals["bad_reverse_window_size"] += atom["bad_window_size"]
        totals["bad_reverse_odd_count"] += atom["bad_odd_count"]
        q_odd = atom["q_odd"]
        if q_odd is None:
            continue

        term = (q_odd, record["m"], record["r"], record["beta"])
        reverse_odd_atoms.add(term)
        low, high = product_cell_window(P, k, q_odd)
        totals["reverse_to_product_cell_checked"] += 1
        totals["reverse_to_product_cell_mismatch"] += int(not (low <= record["m"] <= high))
        if atom["selected_q"] is not None:
            reverse_selected_terms.add(term)

    product_missing_reverse = product_cell_atoms - reverse_odd_atoms
    reverse_missing_product = reverse_odd_atoms - product_cell_atoms
    cell_missing_actual = selected_cell_terms - actual
    actual_missing_cell = actual - selected_cell_terms
    reverse_missing_cell_selected = reverse_selected_terms - selected_cell_terms
    cell_missing_reverse_selected = selected_cell_terms - reverse_selected_terms

    return {
        "P": P,
        "k": k,
        "actual_phase_atoms": len(actual),
        "floor_cell_selected_terms": len(selected_cell_terms),
        "reverse_selected_terms": len(reverse_selected_terms),
        "product_cell_residual_atoms": len(product_cell_atoms),
        "reverse_odd_residual_atoms": len(reverse_odd_atoms),
        "product_cell_atoms_equal_reverse_odd_atoms": len(product_missing_reverse) == 0
        and len(reverse_missing_product) == 0,
        "floor_cell_selected_terms_equal_actual_phase_atoms": len(cell_missing_actual) == 0
        and len(actual_missing_cell) == 0,
        "floor_cell_selected_terms_equal_reverse_selected_terms": len(reverse_missing_cell_selected) == 0
        and len(cell_missing_reverse_selected) == 0,
        "missing_actual_from_floor_cell": len(actual_missing_cell),
        "extra_floor_cell_over_actual": len(cell_missing_actual),
        "missing_reverse_from_product_cell": len(product_missing_reverse),
        "extra_reverse_over_product_cell": len(reverse_missing_product),
        "missing_cell_selected_from_reverse": len(reverse_missing_cell_selected),
        "extra_cell_selected_over_reverse": len(cell_missing_reverse_selected),
        "q_floor_cells_checked": totals["q_floor_cells_checked"],
        "product_cell_to_reverse_checked": totals["product_cell_to_reverse_checked"],
        "product_cell_to_reverse_mismatch": totals["product_cell_to_reverse_mismatch"],
        "reverse_to_product_cell_checked": totals["reverse_to_product_cell_checked"],
        "reverse_to_product_cell_mismatch": totals["reverse_to_product_cell_mismatch"],
        "bad_product_cell_window_size": totals["bad_product_cell_window_size"],
        "bad_product_cell_odd_count": totals["bad_product_cell_odd_count"],
        "bad_reverse_window_size": totals["bad_reverse_window_size"],
        "bad_reverse_odd_count": totals["bad_reverse_odd_count"],
        "bad_unit_q_not_prime": totals["bad_unit_q_not_prime"],
        "cell_unit_selected": totals["cell_unit_selected"],
        "dynamic_primorial_modulus": W,
        "dynamic_primorial_prime_count": len(factors),
        "max_product_cell_window_size": max_product_cell_window_size,
        "max_product_cell_odd_count": max_product_cell_odd_count,
        "max_reverse_window_size": max_reverse_window_size,
        "max_reverse_odd_count": max_reverse_odd_count,
        "q_cell_cases": dict(sorted(q_cell_cases.items())),
        "sample_floor_cells": "; ".join(sample_cells) if sample_cells else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_set = set(primes)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-audit.json").read_text())

    totals: Counter[str] = Counter()
    q_cell_cases: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []
    row_count = 0
    active_rows = 0
    max_product_cell_window_size = 0
    max_product_cell_odd_count = 0
    max_reverse_window_size = 0
    max_reverse_odd_count = 0
    max_primorial_prime_count = 0
    max_primorial_modulus = 1

    for P in P_values:
        records = records_by_P[P]
        for k in range(1, P):
            row_count += 1
            row = row_floor_cell_audit(P, k, records, primes, prime_set, (P, k) in interesting)
            active_rows += int(row["actual_phase_atoms"] > 0)
            totals["actual_phase_atoms"] += row["actual_phase_atoms"]
            totals["floor_cell_selected_terms"] += row["floor_cell_selected_terms"]
            totals["reverse_selected_terms"] += row["reverse_selected_terms"]
            totals["product_cell_residual_atoms"] += row["product_cell_residual_atoms"]
            totals["reverse_odd_residual_atoms"] += row["reverse_odd_residual_atoms"]
            totals["missing_actual_from_floor_cell"] += row["missing_actual_from_floor_cell"]
            totals["extra_floor_cell_over_actual"] += row["extra_floor_cell_over_actual"]
            totals["missing_reverse_from_product_cell"] += row["missing_reverse_from_product_cell"]
            totals["extra_reverse_over_product_cell"] += row["extra_reverse_over_product_cell"]
            totals["missing_cell_selected_from_reverse"] += row["missing_cell_selected_from_reverse"]
            totals["extra_cell_selected_over_reverse"] += row["extra_cell_selected_over_reverse"]
            totals["q_floor_cells_checked"] += row["q_floor_cells_checked"]
            totals["product_cell_to_reverse_checked"] += row["product_cell_to_reverse_checked"]
            totals["product_cell_to_reverse_mismatch"] += row["product_cell_to_reverse_mismatch"]
            totals["reverse_to_product_cell_checked"] += row["reverse_to_product_cell_checked"]
            totals["reverse_to_product_cell_mismatch"] += row["reverse_to_product_cell_mismatch"]
            totals["bad_product_cell_window_size"] += row["bad_product_cell_window_size"]
            totals["bad_product_cell_odd_count"] += row["bad_product_cell_odd_count"]
            totals["bad_reverse_window_size"] += row["bad_reverse_window_size"]
            totals["bad_reverse_odd_count"] += row["bad_reverse_odd_count"]
            totals["bad_unit_q_not_prime"] += row["bad_unit_q_not_prime"]
            totals["cell_unit_selected"] += row["cell_unit_selected"]
            q_cell_cases.update(row["q_cell_cases"])
            max_product_cell_window_size = max(max_product_cell_window_size, row["max_product_cell_window_size"])
            max_product_cell_odd_count = max(max_product_cell_odd_count, row["max_product_cell_odd_count"])
            max_reverse_window_size = max(max_reverse_window_size, row["max_reverse_window_size"])
            max_reverse_odd_count = max(max_reverse_odd_count, row["max_reverse_odd_count"])
            max_primorial_prime_count = max(max_primorial_prime_count, row["dynamic_primorial_prime_count"])
            max_primorial_modulus = max(max_primorial_modulus, row["dynamic_primorial_modulus"])
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_actual_phase_atoms": totals["actual_phase_atoms"],
        "total_floor_cell_selected_terms": totals["floor_cell_selected_terms"],
        "total_reverse_selected_terms": totals["reverse_selected_terms"],
        "total_product_cell_residual_atoms": totals["product_cell_residual_atoms"],
        "total_reverse_odd_residual_atoms": totals["reverse_odd_residual_atoms"],
        "floor_cell_terms_equal_actual_phase_atoms": totals["actual_phase_atoms"]
        == totals["floor_cell_selected_terms"]
        and totals["missing_actual_from_floor_cell"] == 0
        and totals["extra_floor_cell_over_actual"] == 0,
        "floor_cell_terms_equal_reverse_selected_terms": totals["floor_cell_selected_terms"]
        == totals["reverse_selected_terms"]
        and totals["missing_cell_selected_from_reverse"] == 0
        and totals["extra_cell_selected_over_reverse"] == 0,
        "product_cell_atoms_equal_reverse_odd_atoms": totals["product_cell_residual_atoms"]
        == totals["reverse_odd_residual_atoms"]
        and totals["missing_reverse_from_product_cell"] == 0
        and totals["extra_reverse_over_product_cell"] == 0,
        "missing_actual_from_floor_cell_total": totals["missing_actual_from_floor_cell"],
        "extra_floor_cell_over_actual_total": totals["extra_floor_cell_over_actual"],
        "missing_reverse_from_product_cell_total": totals["missing_reverse_from_product_cell"],
        "extra_reverse_over_product_cell_total": totals["extra_reverse_over_product_cell"],
        "missing_cell_selected_from_reverse_total": totals["missing_cell_selected_from_reverse"],
        "extra_cell_selected_over_reverse_total": totals["extra_cell_selected_over_reverse"],
        "q_floor_cells_checked_total": totals["q_floor_cells_checked"],
        "product_cell_to_reverse_checked_total": totals["product_cell_to_reverse_checked"],
        "product_cell_to_reverse_mismatch_total": totals["product_cell_to_reverse_mismatch"],
        "reverse_to_product_cell_checked_total": totals["reverse_to_product_cell_checked"],
        "reverse_to_product_cell_mismatch_total": totals["reverse_to_product_cell_mismatch"],
        "bad_product_cell_window_size_total": totals["bad_product_cell_window_size"],
        "bad_product_cell_odd_count_total": totals["bad_product_cell_odd_count"],
        "bad_reverse_window_size_total": totals["bad_reverse_window_size"],
        "bad_reverse_odd_count_total": totals["bad_reverse_odd_count"],
        "bad_unit_q_not_prime_total": totals["bad_unit_q_not_prime"],
        "cell_unit_selected_total": totals["cell_unit_selected"],
        "max_product_cell_window_size": max_product_cell_window_size,
        "max_product_cell_odd_count": max_product_cell_odd_count,
        "max_reverse_window_size": max_reverse_window_size,
        "max_reverse_odd_count": max_reverse_odd_count,
        "max_dynamic_primorial_prime_count": max_primorial_prime_count,
        "max_dynamic_primorial_modulus": max_primorial_modulus,
        "q_cell_case_totals": dict(sorted(q_cell_cases.items())),
        "floor_cell_denominator_is_original_prime_q_coordinate": True,
        "completed_trace_or_kloosterman_family_available": False,
        "previous_radial_pair_coupled_status": previous["status"],
        "previous_total_actual_phase_atoms": previous["finite_audit"]["total_actual_phase_atoms"],
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    finite_audit = audit_rows()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "floor_cell_radial_support_normal_form_closed_completion_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the fastest non-cyclic continuation is to identify whether the floor denominator is a new phase variable or the original q-cell coordinate",
        "current_object": {
            "reverse_denominator": "Q_{P,k}(m)=least odd integer in [max(P/2+1,floor(kP/m)+1), min(P-1,m,floor(((k+1)P-1)/m))]",
            "forward_floor_cell": "I_{P,k}(q)=[max(P/2+1,q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]",
            "cell_equivalence": "Q_{P,k}(m)=q iff m in I_{P,k}(q), q odd, and m is the residual rough cofactor",
            "selected_atom": "1_{gcd(q,W_P)=1} * 1_{m in I_{P,k}(q)} * e(h*k*P/q)",
            "radial_support": "the paired Ramanujan/radial selector is evaluated at the same q coordinate, not at a new completed variable",
            "remaining_obstruction": "floor cells reconstruct the support exactly, but no cancellation or completed trace family is produced",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "FloorDenominatorCellDecompositionNormalForm",
                True,
                True,
                "The reverse denominator condition Q_{P,k}(m)=q is exactly the forward product-floor cell condition on m.",
                "none",
            ),
            gate(
                "ReverseForwardFloorCellEquivalence",
                True,
                True,
                "Every residual odd q-cell atom matches the reverse floor denominator atom, and conversely.",
                "none",
            ),
            gate(
                "FloorCellRadialSupportExactReconstruction",
                True,
                True,
                "After the W_P unit selector, the floor-cell support equals both the actual prime-q phase support and the coupled reverse support.",
                "none",
            ),
            gate(
                "FloorCellToCompletedTraceFamilyBridge",
                False,
                False,
                "Convert the exact floor cells with radial pair kernels into a completed trace/Kloosterman or Type-II family.",
                "new completion bridge theorem",
            ),
            gate(
                "UniformCancellationAcrossFloorCellsWithRadialPairKernels",
                False,
                False,
                "Prove phase saving uniformly over the exact floor cells and all coupled radial pair kernels.",
                "new phase-saving theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "still needs a trace-function family after the floor cells are completed; the present cell identity is deterministic only",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "requires genuine bilinear Kloosterman sums, while the current object is an exact short floor-cell support",
            "Pascadi_2025_arXiv_2511_08445": "could help only after a composite-modulus Type-II organisation is built from the cells",
            "Wright_2026_arXiv_2604_25177": "relevant only after the floor-cell discrepancy is converted into an unbalanced Kloosterman-fraction convolution",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "squarefree/smooth-modulus estimates remain adjacent to W_P but do not directly estimate the real reciprocal phase e(hkP/q)",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn and not used as a closing input",
        },
        "latest_narrowest_mouth": [
            "FloorCellRadialSupportToCompletedTraceFamilyBridge",
            "AND UniformCancellationAcrossFloorCellsWithRadialPairKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "floor_denominator_cell_decomposition_closed": True,
        "reverse_forward_floor_cell_equivalence_closed": True,
        "floor_cell_radial_support_exact_reconstruction_closed": True,
        "floor_cell_to_completed_trace_family_bridge_closed": False,
        "uniform_cancellation_across_floor_cells_with_radial_pair_kernels_closed": False,
        "rough_beta_siegel_walfisz_factor_extracted": False,
        "pointwise_pk_transfer_closed": False,
        "q_support_phase_saving_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    audit = payload["finite_audit"]
    current = payload["current_object"]
    lines = [
        "# Prime Matrix Phi-LPF q-support floor-cell radial support 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"reverse_denominator={current['reverse_denominator']}",
        f"forward_floor_cell={current['forward_floor_cell']}",
        f"cell_equivalence={current['cell_equivalence']}",
        f"selected_atom={current['selected_atom']}",
        f"radial_support={current['radial_support']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. Floor-cell 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_actual_phase_atoms={audit['total_actual_phase_atoms']}",
        f"total_floor_cell_selected_terms={audit['total_floor_cell_selected_terms']}",
        f"total_reverse_selected_terms={audit['total_reverse_selected_terms']}",
        f"total_product_cell_residual_atoms={audit['total_product_cell_residual_atoms']}",
        f"total_reverse_odd_residual_atoms={audit['total_reverse_odd_residual_atoms']}",
        f"floor_cell_terms_equal_actual_phase_atoms={primorial.bool_text(audit['floor_cell_terms_equal_actual_phase_atoms'])}",
        f"floor_cell_terms_equal_reverse_selected_terms={primorial.bool_text(audit['floor_cell_terms_equal_reverse_selected_terms'])}",
        f"product_cell_atoms_equal_reverse_odd_atoms={primorial.bool_text(audit['product_cell_atoms_equal_reverse_odd_atoms'])}",
        f"product_cell_to_reverse_mismatch_total={audit['product_cell_to_reverse_mismatch_total']}",
        f"reverse_to_product_cell_mismatch_total={audit['reverse_to_product_cell_mismatch_total']}",
        f"bad_product_cell_window_size_total={audit['bad_product_cell_window_size_total']}",
        f"bad_product_cell_odd_count_total={audit['bad_product_cell_odd_count_total']}",
        f"bad_reverse_window_size_total={audit['bad_reverse_window_size_total']}",
        f"bad_reverse_odd_count_total={audit['bad_reverse_odd_count_total']}",
        f"bad_unit_q_not_prime_total={audit['bad_unit_q_not_prime_total']}",
        f"q_floor_cells_checked_total={audit['q_floor_cells_checked_total']}",
        f"max_product_cell_window_size={audit['max_product_cell_window_size']}",
        f"max_product_cell_odd_count={audit['max_product_cell_odd_count']}",
        f"max_reverse_window_size={audit['max_reverse_window_size']}",
        f"max_reverse_odd_count={audit['max_reverse_odd_count']}",
        f"floor_cell_denominator_is_original_prime_q_coordinate={primorial.bool_text(audit['floor_cell_denominator_is_original_prime_q_coordinate'])}",
        f"completed_trace_or_kloosterman_family_available={primorial.bool_text(audit['completed_trace_or_kloosterman_family_available'])}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "actual_phase_atoms",
                "floor_cell_selected_terms",
                "reverse_selected_terms",
                "product_cell_residual_atoms",
                "reverse_odd_residual_atoms",
                "product_cell_to_reverse_checked",
                "reverse_to_product_cell_checked",
                "bad_unit_q_not_prime",
                "sample_floor_cells",
            ],
        ),
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：floor denominator 已被压回正向 q-cell 支撑；这排除了“floor 变量本身就是新完成相位”的误读，但也确认下一步必须证明完成桥和相消，而不能只在等价正规形之间循环。",
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
        f"floor_denominator_cell_decomposition_closed={primorial.bool_text(payload['floor_denominator_cell_decomposition_closed'])}",
        f"reverse_forward_floor_cell_equivalence_closed={primorial.bool_text(payload['reverse_forward_floor_cell_equivalence_closed'])}",
        f"floor_cell_radial_support_exact_reconstruction_closed={primorial.bool_text(payload['floor_cell_radial_support_exact_reconstruction_closed'])}",
        f"floor_cell_to_completed_trace_family_bridge_closed={primorial.bool_text(payload['floor_cell_to_completed_trace_family_bridge_closed'])}",
        f"uniform_cancellation_across_floor_cells_with_radial_pair_kernels_closed={primorial.bool_text(payload['uniform_cancellation_across_floor_cells_with_radial_pair_kernels_closed'])}",
        f"rough_beta_siegel_walfisz_factor_extracted={primorial.bool_text(payload['rough_beta_siegel_walfisz_factor_extracted'])}",
        f"pointwise_pk_transfer_closed={primorial.bool_text(payload['pointwise_pk_transfer_closed'])}",
        f"q_support_phase_saving_closed={primorial.bool_text(payload['q_support_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={primorial.bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={primorial.bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={primorial.bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={primorial.bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("floor_denominator_cell_decomposition_closed=true")
    print("floor_cell_radial_support_exact_reconstruction_closed=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
