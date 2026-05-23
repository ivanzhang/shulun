#!/usr/bin/env python3
"""审计 floor-cell 支撑能否直接形成 Type-II/Kloosterman 长纤维。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_floor_cell_typeii_fiber_obstruction_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-audit.json

上一层已经证明 floor denominator 可完全回收到正向 q-cell。外部前沿定理
通常需要同对象的 bilinear/trilinear 长变量、Kloosterman 变量或 trace-family
变量。本层审计一个最自然但危险的出口：把 floor cells 直接看成 Type-II
长纤维。结论是该出口不成立；每个 q-cell 的 odd residual cofactor 是单点，
每个因子化后的 (q,r)、(q,beta)、(r,beta) 同对象纤维也仍是单点。
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit as floorcell  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-audit.json",
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


def phase_key(P: int, k: int, q: int) -> str:
    """输出符号相位标签。"""
    return f"e(h*{k}*{P}/{q})"


def add_degree(bucket: dict[Any, set[Any]], key: Any, value: Any) -> None:
    """登记纤维度。"""
    bucket[key].add(value)


def max_bucket_size(bucket: dict[Any, set[Any]]) -> int:
    """返回最大纤维大小。"""
    return max((len(values) for values in bucket.values()), default=0)


def row_typeii_fiber_audit(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    collect_samples: bool,
) -> dict[str, Any]:
    """审计单行 floor-cell 支撑的同对象纤维是否有长变量。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    records_by_m = {record["m"]: record for record in records}

    q_to_m: dict[int, set[int]] = defaultdict(set)
    m_to_q: dict[int, set[int]] = defaultdict(set)
    q_to_factor_pair: dict[int, set[tuple[int, int]]] = defaultdict(set)
    qr_to_beta: dict[tuple[int, int], set[int]] = defaultdict(set)
    qbeta_to_r: dict[tuple[int, int], set[int]] = defaultdict(set)
    rbeta_to_q: dict[tuple[int, int], set[int]] = defaultdict(set)
    selected_q_to_m: dict[int, set[int]] = defaultdict(set)
    selected_qr_to_beta: dict[tuple[int, int], set[int]] = defaultdict(set)

    totals: Counter[str] = Counter()
    sample_cells: list[str] = []
    max_product_cell_window_size = 0
    max_product_cell_odd_count = 0

    for q in floorcell.odd_q_values(P):
        low, high = floorcell.product_cell_window(P, k, q)
        window_size = max(0, high - low + 1)
        m_odd, odd_count = primorial.unique_odd_candidate(low, high)
        max_product_cell_window_size = max(max_product_cell_window_size, window_size)
        max_product_cell_odd_count = max(max_product_cell_odd_count, odd_count)
        totals["q_floor_cells_checked"] += 1
        totals["bad_product_cell_window_size"] += int(window_size > 2)
        totals["bad_product_cell_odd_count"] += int(odd_count > 1)
        if m_odd is None:
            continue

        record = records_by_m.get(m_odd)
        if record is None:
            continue

        r = record["r"]
        beta = record["beta"]
        add_degree(q_to_m, q, m_odd)
        add_degree(m_to_q, m_odd, q)
        add_degree(q_to_factor_pair, q, (r, beta))
        add_degree(qr_to_beta, (q, r), beta)
        add_degree(qbeta_to_r, (q, beta), r)
        add_degree(rbeta_to_q, (r, beta), q)
        totals["floor_cell_residual_atoms"] += 1

        unit_selected = math.gcd(q, W) == 1
        if unit_selected:
            add_degree(selected_q_to_m, q, m_odd)
            add_degree(selected_qr_to_beta, (q, r), beta)
            totals["floor_cell_selected_terms"] += 1
            if collect_samples and len(sample_cells) < 8:
                sample_cells.append(
                    "q={q},m={m},r={r},beta={beta},I_q=[{low},{high}],phase={phase}".format(
                        q=q,
                        m=m_odd,
                        r=r,
                        beta=beta,
                        low=low,
                        high=high,
                        phase=phase_key(P, k, q),
                    )
                )

    max_q_to_m = max_bucket_size(q_to_m)
    max_m_to_q = max_bucket_size(m_to_q)
    max_q_to_factor_pair = max_bucket_size(q_to_factor_pair)
    max_qr_to_beta = max_bucket_size(qr_to_beta)
    max_qbeta_to_r = max_bucket_size(qbeta_to_r)
    max_rbeta_to_q = max_bucket_size(rbeta_to_q)
    max_selected_q_to_m = max_bucket_size(selected_q_to_m)
    max_selected_qr_to_beta = max_bucket_size(selected_qr_to_beta)
    any_long_same_object_fiber = any(
        value > 1
        for value in [
            max_q_to_m,
            max_m_to_q,
            max_q_to_factor_pair,
            max_qr_to_beta,
            max_qbeta_to_r,
            max_rbeta_to_q,
            max_selected_q_to_m,
            max_selected_qr_to_beta,
        ]
    )

    return {
        "P": P,
        "k": k,
        "floor_cell_residual_atoms": totals["floor_cell_residual_atoms"],
        "floor_cell_selected_terms": totals["floor_cell_selected_terms"],
        "q_floor_cells_checked": totals["q_floor_cells_checked"],
        "bad_product_cell_window_size": totals["bad_product_cell_window_size"],
        "bad_product_cell_odd_count": totals["bad_product_cell_odd_count"],
        "max_product_cell_window_size": max_product_cell_window_size,
        "max_product_cell_odd_count": max_product_cell_odd_count,
        "max_q_to_m_fiber": max_q_to_m,
        "max_m_to_q_fiber": max_m_to_q,
        "max_q_to_factor_pair_fiber": max_q_to_factor_pair,
        "max_qr_to_beta_fiber": max_qr_to_beta,
        "max_qbeta_to_r_fiber": max_qbeta_to_r,
        "max_rbeta_to_q_fiber": max_rbeta_to_q,
        "max_selected_q_to_m_fiber": max_selected_q_to_m,
        "max_selected_qr_to_beta_fiber": max_selected_qr_to_beta,
        "same_object_long_fiber_available": any_long_same_object_fiber,
        "sample_floor_cells": "; ".join(sample_cells) if sample_cells else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-audit.json").read_text())

    totals: Counter[str] = Counter()
    row_count = 0
    active_rows = 0
    rows_with_long_same_object_fiber = 0
    sample_rows: list[dict[str, Any]] = []
    maxima: Counter[str] = Counter()

    for P in P_values:
        records = records_by_P[P]
        for k in range(1, P):
            row_count += 1
            row = row_typeii_fiber_audit(P, k, records, primes, (P, k) in interesting)
            active_rows += int(row["floor_cell_selected_terms"] > 0)
            rows_with_long_same_object_fiber += int(row["same_object_long_fiber_available"])
            for key in [
                "floor_cell_residual_atoms",
                "floor_cell_selected_terms",
                "q_floor_cells_checked",
                "bad_product_cell_window_size",
                "bad_product_cell_odd_count",
            ]:
                totals[key] += row[key]
            for key in [
                "max_product_cell_window_size",
                "max_product_cell_odd_count",
                "max_q_to_m_fiber",
                "max_m_to_q_fiber",
                "max_q_to_factor_pair_fiber",
                "max_qr_to_beta_fiber",
                "max_qbeta_to_r_fiber",
                "max_rbeta_to_q_fiber",
                "max_selected_q_to_m_fiber",
                "max_selected_qr_to_beta_fiber",
            ]:
                maxima[key] = max(maxima[key], row[key])
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_floor_cell_residual_atoms": totals["floor_cell_residual_atoms"],
        "total_floor_cell_selected_terms": totals["floor_cell_selected_terms"],
        "q_floor_cells_checked_total": totals["q_floor_cells_checked"],
        "bad_product_cell_window_size_total": totals["bad_product_cell_window_size"],
        "bad_product_cell_odd_count_total": totals["bad_product_cell_odd_count"],
        "max_product_cell_window_size": maxima["max_product_cell_window_size"],
        "max_product_cell_odd_count": maxima["max_product_cell_odd_count"],
        "max_q_to_m_fiber": maxima["max_q_to_m_fiber"],
        "max_m_to_q_fiber": maxima["max_m_to_q_fiber"],
        "max_q_to_factor_pair_fiber": maxima["max_q_to_factor_pair_fiber"],
        "max_qr_to_beta_fiber": maxima["max_qr_to_beta_fiber"],
        "max_qbeta_to_r_fiber": maxima["max_qbeta_to_r_fiber"],
        "max_rbeta_to_q_fiber": maxima["max_rbeta_to_q_fiber"],
        "max_selected_q_to_m_fiber": maxima["max_selected_q_to_m_fiber"],
        "max_selected_qr_to_beta_fiber": maxima["max_selected_qr_to_beta_fiber"],
        "rows_with_long_same_object_fiber": rows_with_long_same_object_fiber,
        "same_object_long_fiber_available_for_any_row": rows_with_long_same_object_fiber > 0,
        "direct_typeii_bilinear_fiber_available": False,
        "direct_kloosterman_variable_available": False,
        "phase_is_denominator_graph_phase_not_inverse_variable": True,
        "previous_floor_cell_status": previous["status"],
        "previous_total_floor_cell_selected_terms": previous["finite_audit"]["total_floor_cell_selected_terms"],
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_floor_cell_typeii_fiber_obstruction_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "direct_floor_cell_typeii_completion_rejected_same_object_trace_embedding_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after floor-cell reconstruction, the fastest non-cyclic check is whether those cells already supply the long variables required by current bilinear Kloosterman or trace-function theorems",
        "current_object": {
            "floor_cell": "I_{P,k}(q)=[max(P/2+1,q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]",
            "factor_split": "m=r*beta with r>=7 prime and beta r-rough",
            "same_object_fibers_checked": "q->m, m->q, q->(r,beta), (q,r)->beta, (q,beta)->r, (r,beta)->q",
            "phase": "e(h*k*P/q), equivalently e(-h*(qm-kP)/q) on the graph",
            "obstruction": "all same-object fibers are singleton, so floor cells do not directly form a long Type-II/Kloosterman family",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "FloorCellSameObjectFiberSingletonLedger",
                True,
                True,
                "The q-cell support and all immediate factor fibers are singleton fibers in the same object.",
                "none",
            ),
            gate(
                "DirectFloorCellTypeIICompletionRejected",
                True,
                True,
                "The exact floor-cell graph does not itself supply the long bilinear/trilinear variables required by Type-II Kloosterman inputs.",
                "none",
            ),
            gate(
                "DirectKloostermanVariableFromFloorCellRejected",
                True,
                True,
                "The phase remains a denominator graph phase e(hkP/q), not a completed inverse-variable Kloosterman sum.",
                "none",
            ),
            gate(
                "SameObjectAveragedGraphDispersionOrTraceEmbedding",
                False,
                False,
                "Build a new embedding that averages the sparse denominator graph into a legitimate trace/Kloosterman or dispersion family without changing the object.",
                "new same-object completion theorem",
            ),
            gate(
                "UniformCancellationAcrossGraphSupportedRadialKernels",
                False,
                False,
                "Prove cancellation after such an embedding, uniformly across the radial pair kernels and q-support graph.",
                "new phase-saving theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "requires a genuine trace-function family and bilinear variables; singleton floor-cell fibers do not provide it directly",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "power-saving bilinear Kloosterman sums need actual Kloosterman variables modulo q; the present phase is still a q-graph denominator phase",
            "Pascadi_2025_arXiv_2511_08445": "composite-modulus Type-II amplification remains relevant only after a nontrivial same-object embedding creates long variables",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution hypotheses require a congruence/convolution family with a nontrivial inner variable; direct floor-cell fibers are singleton",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree parameter inputs remain adjacent to W_P but do not overcome the missing trace embedding",
        },
        "latest_narrowest_mouth": [
            "SameObjectAveragedGraphDispersionOrTraceEmbedding",
            "AND UniformCancellationAcrossGraphSupportedRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "floor_cell_same_object_fiber_singleton_ledger_closed": True,
        "direct_floor_cell_typeii_completion_rejected": True,
        "direct_kloosterman_variable_from_floor_cell_rejected": True,
        "same_object_averaged_graph_dispersion_or_trace_embedding_closed": False,
        "uniform_cancellation_across_graph_supported_radial_kernels_closed": False,
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
        "# Prime Matrix Phi-LPF q-support floor-cell Type-II fiber obstruction 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"floor_cell={current['floor_cell']}",
        f"factor_split={current['factor_split']}",
        f"same_object_fibers_checked={current['same_object_fibers_checked']}",
        f"phase={current['phase']}",
        f"obstruction={current['obstruction']}",
        "```",
        "",
        "## 2. Fiber 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_floor_cell_residual_atoms={audit['total_floor_cell_residual_atoms']}",
        f"total_floor_cell_selected_terms={audit['total_floor_cell_selected_terms']}",
        f"q_floor_cells_checked_total={audit['q_floor_cells_checked_total']}",
        f"bad_product_cell_window_size_total={audit['bad_product_cell_window_size_total']}",
        f"bad_product_cell_odd_count_total={audit['bad_product_cell_odd_count_total']}",
        f"max_product_cell_window_size={audit['max_product_cell_window_size']}",
        f"max_product_cell_odd_count={audit['max_product_cell_odd_count']}",
        f"max_q_to_m_fiber={audit['max_q_to_m_fiber']}",
        f"max_m_to_q_fiber={audit['max_m_to_q_fiber']}",
        f"max_q_to_factor_pair_fiber={audit['max_q_to_factor_pair_fiber']}",
        f"max_qr_to_beta_fiber={audit['max_qr_to_beta_fiber']}",
        f"max_qbeta_to_r_fiber={audit['max_qbeta_to_r_fiber']}",
        f"max_rbeta_to_q_fiber={audit['max_rbeta_to_q_fiber']}",
        f"max_selected_q_to_m_fiber={audit['max_selected_q_to_m_fiber']}",
        f"max_selected_qr_to_beta_fiber={audit['max_selected_qr_to_beta_fiber']}",
        f"rows_with_long_same_object_fiber={audit['rows_with_long_same_object_fiber']}",
        f"same_object_long_fiber_available_for_any_row={primorial.bool_text(audit['same_object_long_fiber_available_for_any_row'])}",
        f"direct_typeii_bilinear_fiber_available={primorial.bool_text(audit['direct_typeii_bilinear_fiber_available'])}",
        f"direct_kloosterman_variable_available={primorial.bool_text(audit['direct_kloosterman_variable_available'])}",
        f"phase_is_denominator_graph_phase_not_inverse_variable={primorial.bool_text(audit['phase_is_denominator_graph_phase_not_inverse_variable'])}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "floor_cell_residual_atoms",
                "floor_cell_selected_terms",
                "max_q_to_m_fiber",
                "max_m_to_q_fiber",
                "max_qr_to_beta_fiber",
                "max_qbeta_to_r_fiber",
                "max_rbeta_to_q_fiber",
                "same_object_long_fiber_available",
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
        "结论：floor-cell 支撑虽然已精确闭合，但直接 Type-II/Kloosterman 完成出口被排除。下一步必须构造新的 same-object averaged graph dispersion 或 trace embedding，而不能把单点纤维误认为长双线性变量。",
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
        f"floor_cell_same_object_fiber_singleton_ledger_closed={primorial.bool_text(payload['floor_cell_same_object_fiber_singleton_ledger_closed'])}",
        f"direct_floor_cell_typeii_completion_rejected={primorial.bool_text(payload['direct_floor_cell_typeii_completion_rejected'])}",
        f"direct_kloosterman_variable_from_floor_cell_rejected={primorial.bool_text(payload['direct_kloosterman_variable_from_floor_cell_rejected'])}",
        f"same_object_averaged_graph_dispersion_or_trace_embedding_closed={primorial.bool_text(payload['same_object_averaged_graph_dispersion_or_trace_embedding_closed'])}",
        f"uniform_cancellation_across_graph_supported_radial_kernels_closed={primorial.bool_text(payload['uniform_cancellation_across_graph_supported_radial_kernels_closed'])}",
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
    print("direct_floor_cell_typeii_completion_rejected=true")
    print("same_object_averaged_graph_dispersion_or_trace_embedding_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
