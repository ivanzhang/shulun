#!/usr/bin/env python3
"""审计跨 k 平均后的 q-support mixed-modulus graph 正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_mixed_modulus_graph_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-audit.json

上一层排除了单行 floor-cell 直接给 Type-II 长纤维的假出口。本层检查
最新剩余口 SameObjectAveragedGraphDispersionOrTraceEmbedding 的最自然下钻：
把所有 1<=k<P 行合并后，固定 (q,m) 唯一决定

  k=floor(qm/P),  D=qm-kP=qm mod P.

因此跨行平均确实产生长的 q-m 图纤维，但相位变成

  e(h*k*P/q)=e(-h*D/q),  D=qm mod P.

这是分子按模 P 取余、分母按 q 振荡的 mixed-modulus graph phase，不是
现有同模 Kloosterman/trace-function 输入可直接读取的对象。
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


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-audit.json",
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


def add_degree(bucket: dict[Any, set[Any]], key: Any, value: Any) -> None:
    """登记纤维度。"""
    bucket[key].add(value)


def max_bucket_size(bucket: dict[Any, set[Any]]) -> int:
    """返回最大纤维大小。"""
    return max((len(values) for values in bucket.values()), default=0)


def phase_key(P: int, q: int, m: int) -> str:
    """输出跨行相位标签。"""
    k = (q * m) // P
    d = q * m - k * P
    return f"k={k},D={d},phase=e(-h*{d}/{q})"


def row_averaged_edges_for_P(
    P: int,
    records: list[dict[str, int]],
    primes: list[int],
    collect_samples: bool,
) -> dict[str, Any]:
    """审计固定 P 的跨 k 合并图。"""
    W, _factors = primorial.primorial_modulus(P, primes)
    records_by_m = {record["m"]: record for record in records}

    q_to_m: dict[int, set[int]] = defaultdict(set)
    m_to_q: dict[int, set[int]] = defaultdict(set)
    q_to_k: dict[int, set[int]] = defaultdict(set)
    k_to_q: dict[int, set[int]] = defaultdict(set)
    selected_q_to_m: dict[int, set[int]] = defaultdict(set)
    selected_m_to_q: dict[int, set[int]] = defaultdict(set)
    selected_q_to_k: dict[int, set[int]] = defaultdict(set)
    selected_k_to_q: dict[int, set[int]] = defaultdict(set)
    mod_q_residue_to_phase_numerators: dict[tuple[int, int], set[int]] = defaultdict(set)

    totals: Counter[str] = Counter()
    sample_edges: list[str] = []
    first_trace_conflict = "none"

    for q in floorcell.odd_q_values(P):
        q_is_unit = math.gcd(q, W) == 1
        for record in records:
            m = record["m"]
            if m < q:
                continue
            product = q * m
            k = product // P
            d = product - k * P
            if not (1 <= k < P):
                continue
            if d == 0:
                totals["bad_zero_displacement"] += 1
                continue

            low, high = floorcell.product_cell_window(P, k, q)
            totals["floor_cell_membership_mismatch"] += int(not (low <= m <= high))
            q_odd, odd_count = primorial.unique_odd_candidate(low, high)
            totals["floor_cell_odd_candidate_mismatch"] += int(q_odd is None or q_odd != m)
            totals["bad_floor_cell_odd_count"] += int(odd_count > 1)

            totals["row_averaged_residual_edges"] += 1
            add_degree(q_to_m, q, m)
            add_degree(m_to_q, m, q)
            add_degree(q_to_k, q, k)
            add_degree(k_to_q, k, q)

            if q_is_unit:
                totals["row_averaged_selected_edges"] += 1
                add_degree(selected_q_to_m, q, m)
                add_degree(selected_m_to_q, m, q)
                add_degree(selected_q_to_k, q, k)
                add_degree(selected_k_to_q, k, q)
                # 中文注释：若同一 m mod q 对应不同 D mod q，则不能直接视作 q 模上的单变量 trace function。
                key = (q, m % q)
                before = len(mod_q_residue_to_phase_numerators[key])
                mod_q_residue_to_phase_numerators[key].add(d % q)
                after = len(mod_q_residue_to_phase_numerators[key])
                if before == 1 and after > 1 and first_trace_conflict == "none":
                    values = sorted(mod_q_residue_to_phase_numerators[key])
                    first_trace_conflict = f"q={q},m_mod_q={m % q},D_mod_q_values={values}"
                if collect_samples and len(sample_edges) < 8:
                    sample_edges.append(
                        "q={q},m={m},r={r},beta={beta},{phase},qmodW={qmod}".format(
                            q=q,
                            m=m,
                            r=record["r"],
                            beta=record["beta"],
                            phase=phase_key(P, q, m),
                            qmod=q % W,
                        )
                    )

    trace_conflict_residue_count = sum(
        1 for values in mod_q_residue_to_phase_numerators.values() if len(values) > 1
    )
    trace_conflict_q_count = len(
        {q for (q, _residue), values in mod_q_residue_to_phase_numerators.items() if len(values) > 1}
    )

    return {
        "P": P,
        "row_averaged_residual_edges": totals["row_averaged_residual_edges"],
        "row_averaged_selected_edges": totals["row_averaged_selected_edges"],
        "floor_cell_membership_mismatch": totals["floor_cell_membership_mismatch"],
        "floor_cell_odd_candidate_mismatch": totals["floor_cell_odd_candidate_mismatch"],
        "bad_floor_cell_odd_count": totals["bad_floor_cell_odd_count"],
        "bad_zero_displacement": totals["bad_zero_displacement"],
        "max_q_to_m_fiber": max_bucket_size(q_to_m),
        "max_m_to_q_fiber": max_bucket_size(m_to_q),
        "max_q_to_k_fiber": max_bucket_size(q_to_k),
        "max_k_to_q_fiber": max_bucket_size(k_to_q),
        "max_selected_q_to_m_fiber": max_bucket_size(selected_q_to_m),
        "max_selected_m_to_q_fiber": max_bucket_size(selected_m_to_q),
        "max_selected_q_to_k_fiber": max_bucket_size(selected_q_to_k),
        "max_selected_k_to_q_fiber": max_bucket_size(selected_k_to_q),
        "trace_mod_q_conflict_residue_count": trace_conflict_residue_count,
        "trace_mod_q_conflict_q_count": trace_conflict_q_count,
        "first_trace_mod_q_conflict": first_trace_conflict,
        "row_averaging_creates_long_q_fibers": max_bucket_size(selected_q_to_m) > 1,
        "phase_uses_mod_P_residue_with_denominator_q": totals["row_averaged_selected_edges"] > 0,
        "sample_edges": "; ".join(sample_edges) if sample_edges else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的跨 k 合并图做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    interesting = {101, 257, 971, 1009}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-audit.json").read_text())

    totals: Counter[str] = Counter()
    maxima: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []
    rows_with_long_q_fibers = 0
    rows_with_trace_mod_q_conflict = 0
    first_global_trace_conflict = "none"

    for P in P_values:
        row = row_averaged_edges_for_P(P, records_by_P[P], primes, P in interesting)
        for key in [
            "row_averaged_residual_edges",
            "row_averaged_selected_edges",
            "floor_cell_membership_mismatch",
            "floor_cell_odd_candidate_mismatch",
            "bad_floor_cell_odd_count",
            "bad_zero_displacement",
            "trace_mod_q_conflict_residue_count",
            "trace_mod_q_conflict_q_count",
        ]:
            totals[key] += row[key]
        for key in [
            "max_q_to_m_fiber",
            "max_m_to_q_fiber",
            "max_q_to_k_fiber",
            "max_k_to_q_fiber",
            "max_selected_q_to_m_fiber",
            "max_selected_m_to_q_fiber",
            "max_selected_q_to_k_fiber",
            "max_selected_k_to_q_fiber",
        ]:
            maxima[key] = max(maxima[key], row[key])
        rows_with_long_q_fibers += int(row["row_averaging_creates_long_q_fibers"])
        rows_with_trace_mod_q_conflict += int(row["trace_mod_q_conflict_residue_count"] > 0)
        if first_global_trace_conflict == "none" and row["first_trace_mod_q_conflict"] != "none":
            first_global_trace_conflict = f"P={P},{row['first_trace_mod_q_conflict']}"
        if P in interesting:
            sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "total_row_averaged_residual_edges": totals["row_averaged_residual_edges"],
        "total_row_averaged_selected_edges": totals["row_averaged_selected_edges"],
        "previous_single_row_selected_edge_total": previous["finite_audit"]["total_floor_cell_selected_terms"],
        "row_averaged_selected_edges_match_previous_total": totals["row_averaged_selected_edges"]
        == previous["finite_audit"]["total_floor_cell_selected_terms"],
        "floor_cell_membership_mismatch_total": totals["floor_cell_membership_mismatch"],
        "floor_cell_odd_candidate_mismatch_total": totals["floor_cell_odd_candidate_mismatch"],
        "bad_floor_cell_odd_count_total": totals["bad_floor_cell_odd_count"],
        "bad_zero_displacement_total": totals["bad_zero_displacement"],
        "max_q_to_m_fiber": maxima["max_q_to_m_fiber"],
        "max_m_to_q_fiber": maxima["max_m_to_q_fiber"],
        "max_q_to_k_fiber": maxima["max_q_to_k_fiber"],
        "max_k_to_q_fiber": maxima["max_k_to_q_fiber"],
        "max_selected_q_to_m_fiber": maxima["max_selected_q_to_m_fiber"],
        "max_selected_m_to_q_fiber": maxima["max_selected_m_to_q_fiber"],
        "max_selected_q_to_k_fiber": maxima["max_selected_q_to_k_fiber"],
        "max_selected_k_to_q_fiber": maxima["max_selected_k_to_q_fiber"],
        "P_values_with_long_selected_q_fibers": rows_with_long_q_fibers,
        "row_averaging_creates_long_selected_q_fibers_for_some_P": rows_with_long_q_fibers > 0,
        "trace_mod_q_conflict_residue_count_total": totals["trace_mod_q_conflict_residue_count"],
        "trace_mod_q_conflict_q_count_total": totals["trace_mod_q_conflict_q_count"],
        "P_values_with_trace_mod_q_conflict": rows_with_trace_mod_q_conflict,
        "first_trace_mod_q_conflict": first_global_trace_conflict,
        "phase_normal_form": "for each edge k=floor(q*m/P), D=q*m-k*P=q*m mod P, e(h*k*P/q)=e(-h*D/q)",
        "phase_residue_modulus": "P",
        "phase_denominator_modulus": "q",
        "same_modulus_trace_family_available_directly": False,
        "kloosterman_inverse_variable_available_directly": False,
        "row_averaged_graph_normal_form_closed": True,
        "mixed_modulus_trace_embedding_closed": False,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_mixed_modulus_graph_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "row_averaged_graph_normal_form_closed_mixed_modulus_trace_embedding_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after direct single-row Type-II completion is rejected, the next non-cyclic continuation is to test whether averaging over k creates a usable same-object graph family",
        "current_object": {
            "row_averaged_edge": "q odd, m=r*beta residual, k=floor(q*m/P), 1<=k<P",
            "displacement": "D=q*m-k*P=q*m mod P, 1<=D<P",
            "phase": "e(h*k*P/q)=e(-h*D/q)",
            "long_fiber_gain": "after averaging over k, fixed q can have many m and many k",
            "mixed_modulus_obstruction": "D is a mod-P residue while the phase denominator is q",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RowAveragedQSupportGraphNormalForm",
                True,
                True,
                "Averaging over k identifies each edge by k=floor(qm/P) and D=qm mod P.",
                "none",
            ),
            gate(
                "RowAveragingLongFiberGainLedger",
                True,
                True,
                "Unlike one row, the all-k graph has long q-to-m and q-to-k fibers.",
                "none",
            ),
            gate(
                "MixedModulusPhaseLedger",
                True,
                True,
                "The row-averaged phase is e(-h(qm mod P)/q), coupling mod-P residue with denominator q.",
                "none",
            ),
            gate(
                "DirectSameModulusTraceEmbeddingFromRowAverage",
                False,
                False,
                "Identify the mixed-modulus graph phase as a same-modulus trace/Kloosterman family without changing the object.",
                "new mixed-modulus embedding theorem",
            ),
            gate(
                "UniformCancellationAcrossRowAveragedMixedModulusRadialGraph",
                False,
                False,
                "Prove phase saving over the row-averaged mixed-modulus graph and radial kernels.",
                "new phase-saving theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "row averaging supplies long fibers, but still lacks a same-modulus ell-adic trace-function family",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-q Kloosterman bilinear estimates still require Kloosterman variables modulo q, not a mod-P numerator divided by q",
            "Pascadi_2025_arXiv_2511_08445": "composite-modulus Type-II amplification is relevant only after the mixed-modulus graph is embedded into a genuine Kloosterman family",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution estimates require congruence/convolution structure; the present graph has k=floor(qm/P) and D=qm mod P",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree parameters remain adjacent to W_P but do not by themselves remove the mixed-modulus obstruction",
        },
        "latest_narrowest_mouth": [
            "MixedModulusRowAveragedGraphToTraceOrKloostermanEmbedding",
            "AND UniformCancellationAcrossRowAveragedMixedModulusRadialGraph",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "row_averaged_qsupport_graph_normal_form_closed": True,
        "row_averaging_long_fiber_gain_ledger_closed": True,
        "mixed_modulus_phase_ledger_closed": True,
        "direct_same_modulus_trace_embedding_from_row_average_closed": False,
        "uniform_cancellation_across_row_averaged_mixed_modulus_radial_graph_closed": False,
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
        "# Prime Matrix Phi-LPF q-support row-averaged mixed-modulus graph 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"row_averaged_edge={current['row_averaged_edge']}",
        f"displacement={current['displacement']}",
        f"phase={current['phase']}",
        f"long_fiber_gain={current['long_fiber_gain']}",
        f"mixed_modulus_obstruction={current['mixed_modulus_obstruction']}",
        "```",
        "",
        "## 2. 跨 k 图审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"total_row_averaged_residual_edges={audit['total_row_averaged_residual_edges']}",
        f"total_row_averaged_selected_edges={audit['total_row_averaged_selected_edges']}",
        f"previous_single_row_selected_edge_total={audit['previous_single_row_selected_edge_total']}",
        f"row_averaged_selected_edges_match_previous_total={primorial.bool_text(audit['row_averaged_selected_edges_match_previous_total'])}",
        f"floor_cell_membership_mismatch_total={audit['floor_cell_membership_mismatch_total']}",
        f"floor_cell_odd_candidate_mismatch_total={audit['floor_cell_odd_candidate_mismatch_total']}",
        f"bad_floor_cell_odd_count_total={audit['bad_floor_cell_odd_count_total']}",
        f"bad_zero_displacement_total={audit['bad_zero_displacement_total']}",
        f"max_q_to_m_fiber={audit['max_q_to_m_fiber']}",
        f"max_m_to_q_fiber={audit['max_m_to_q_fiber']}",
        f"max_q_to_k_fiber={audit['max_q_to_k_fiber']}",
        f"max_k_to_q_fiber={audit['max_k_to_q_fiber']}",
        f"max_selected_q_to_m_fiber={audit['max_selected_q_to_m_fiber']}",
        f"max_selected_m_to_q_fiber={audit['max_selected_m_to_q_fiber']}",
        f"max_selected_q_to_k_fiber={audit['max_selected_q_to_k_fiber']}",
        f"max_selected_k_to_q_fiber={audit['max_selected_k_to_q_fiber']}",
        f"P_values_with_long_selected_q_fibers={audit['P_values_with_long_selected_q_fibers']}",
        f"row_averaging_creates_long_selected_q_fibers_for_some_P={primorial.bool_text(audit['row_averaging_creates_long_selected_q_fibers_for_some_P'])}",
        f"trace_mod_q_conflict_residue_count_total={audit['trace_mod_q_conflict_residue_count_total']}",
        f"trace_mod_q_conflict_q_count_total={audit['trace_mod_q_conflict_q_count_total']}",
        f"P_values_with_trace_mod_q_conflict={audit['P_values_with_trace_mod_q_conflict']}",
        f"first_trace_mod_q_conflict={audit['first_trace_mod_q_conflict']}",
        f"phase_normal_form={audit['phase_normal_form']}",
        f"same_modulus_trace_family_available_directly={primorial.bool_text(audit['same_modulus_trace_family_available_directly'])}",
        f"kloosterman_inverse_variable_available_directly={primorial.bool_text(audit['kloosterman_inverse_variable_available_directly'])}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "row_averaged_residual_edges",
                "row_averaged_selected_edges",
                "max_selected_q_to_m_fiber",
                "max_selected_m_to_q_fiber",
                "max_selected_q_to_k_fiber",
                "max_selected_k_to_q_fiber",
                "trace_mod_q_conflict_residue_count",
                "first_trace_mod_q_conflict",
                "sample_edges",
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
        "结论：跨 k 平均确实恢复长纤维，但相位是 mixed-modulus graph phase。下一步不是再证明有长纤维，而是把 `D=qm mod P` 与分母 `q` 的混合模数结构嵌入同模 trace/Kloosterman/dispersion 对象。",
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
        f"row_averaged_qsupport_graph_normal_form_closed={primorial.bool_text(payload['row_averaged_qsupport_graph_normal_form_closed'])}",
        f"row_averaging_long_fiber_gain_ledger_closed={primorial.bool_text(payload['row_averaging_long_fiber_gain_ledger_closed'])}",
        f"mixed_modulus_phase_ledger_closed={primorial.bool_text(payload['mixed_modulus_phase_ledger_closed'])}",
        f"direct_same_modulus_trace_embedding_from_row_average_closed={primorial.bool_text(payload['direct_same_modulus_trace_embedding_from_row_average_closed'])}",
        f"uniform_cancellation_across_row_averaged_mixed_modulus_radial_graph_closed={primorial.bool_text(payload['uniform_cancellation_across_row_averaged_mixed_modulus_radial_graph_closed'])}",
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
    print("row_averaged_qsupport_graph_normal_form_closed=true")
    print("mixed_modulus_phase_ledger_closed=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
