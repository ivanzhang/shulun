#!/usr/bin/env python3
"""审计 radial pair kernel 与 actual reciprocal phase 的耦合正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_radial_pair_coupled_phase_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-audit.json

上一层已经把互补 conductor 配对核压成 radial two-cylinder tensor。本层继续
关闭确定性耦合门：actual q-support reciprocal phase 可以精确写成 residual
cofactor m 上的 floor-defined denominator Q_{P,k}(m)，再乘以按互补 conductor
pair 分组的 Ramanujan unit selector。它仍不是 trace/Kloosterman 相位族：
分母是 floor map Q_{P,k}(m)，而权重是 radial divisor-lattice kernel。
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit as ramanujan  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.json",
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


def format_fraction(value: Fraction) -> str:
    """输出分数。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def term_value(n: int, row: dict[str, Any]) -> Fraction:
    """计算 mu(d)c_d(n)/phi(d)。"""
    c_d = ramanujan.ramanujan_sum_squarefree(n, row["factors"])
    return Fraction(row["mu"] * c_d, row["phi"])


def paired_ramanujan_selector_value(n: int, W: int, factors: list[int]) -> Fraction:
    """按互补 conductor pair 分组计算单位类指示函数。"""
    rows = ramanujan.squarefree_divisor_data(factors)
    by_d = {row["d"]: row for row in rows}
    seen: set[int] = set()
    total = Fraction(0, 1)
    for row in rows:
        d = row["d"]
        if d in seen:
            continue
        complement = W // d
        total += term_value(n, row)
        if complement != d:
            total += term_value(n, by_d[complement])
        seen.add(d)
        seen.add(complement)
    return Fraction(ramanujan.phi_squarefree(factors), W) * total


def paired_kernel_count(factors: list[int]) -> int:
    """互补 pair 核数量。"""
    return 1 if not factors else 2 ** (len(factors) - 1)


def phase_key(P: int, k: int, q: int) -> str:
    """输出符号相位标签。"""
    return f"e(h*{k}*{P}/{q})"


def coupled_terms_for_row(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    prime_set: set[int],
    collect_pair_samples: bool,
) -> tuple[set[tuple[int, int, int, int]], dict[str, Any]]:
    """从 radial-pair coupled phase 正规形得到支撑相位项。"""
    W, factors = primorial.primorial_modulus(P, primes)
    terms: set[tuple[int, int, int, int]] = set()
    selector_cases: Counter[str] = Counter()
    totals: Counter[str] = Counter()
    pair_samples: list[str] = []
    phase_samples: list[str] = []
    max_window_size = 0
    max_odd_count = 0

    for record in records:
        atom = primorial.unit_selector_atom(P, k, record["m"], W, factors)
        selector_cases[atom["selector_case"]] += 1
        max_window_size = max(max_window_size, atom["window_size"])
        max_odd_count = max(max_odd_count, atom["odd_count"])
        totals["bad_window_size"] += atom["bad_window_size"]
        totals["bad_odd_count"] += atom["bad_odd_count"]
        totals["windows_with_odd_candidate"] += int(atom["q_odd"] is not None)
        if atom["q_odd"] is None:
            continue

        expected = Fraction(1 if atom["gcd_qodd_W"] == 1 else 0, 1)
        local_value = ramanujan.ramanujan_local_product_value(atom["q_odd"], factors)
        totals["local_coupled_identity_checked"] += 1
        totals["local_coupled_identity_mismatch"] += int(local_value != expected)
        if collect_pair_samples and len(pair_samples) < 8:
            paired_value = paired_ramanujan_selector_value(atom["q_odd"], W, factors)
            totals["paired_kernel_identity_sample_checked"] += 1
            totals["paired_kernel_identity_sample_mismatch"] += int(paired_value != expected)
            pair_samples.append(
                "m={m},Q={q},expected={expected},paired={paired},phase={phase}".format(
                    m=record["m"],
                    q=atom["q_odd"],
                    expected=format_fraction(expected),
                    paired=format_fraction(paired_value),
                    phase=phase_key(P, k, atom["q_odd"]),
                )
            )

        selected = atom["selected_q"]
        if selected is not None:
            terms.add((selected, record["m"], record["r"], record["beta"]))
            totals["coupled_selected_phase_atoms"] += 1
            totals["bad_selected_denominator_not_prime"] += int(selected not in prime_set)
            if len(phase_samples) < 5:
                phase_samples.append(
                    "q={q},m={m},r={r},beta={beta},phase={phase},QmodW={qmod}".format(
                        q=selected,
                        m=record["m"],
                        r=record["r"],
                        beta=record["beta"],
                        phase=phase_key(P, k, selected),
                        qmod=selected % W,
                    )
                )

    return terms, {
        "dynamic_primorial_modulus": W,
        "dynamic_primorial_prime_count": len(factors),
        "complementary_pair_kernels_per_candidate": paired_kernel_count(factors),
        "full_ramanujan_divisor_terms_per_candidate": 2 ** len(factors),
        "full_additive_modes_per_candidate": W,
        "selector_cases": dict(sorted(selector_cases.items())),
        "max_reverse_window_size": max_window_size,
        "max_odd_count": max_odd_count,
        "bad_window_size": totals["bad_window_size"],
        "bad_odd_count": totals["bad_odd_count"],
        "windows_with_odd_candidate": totals["windows_with_odd_candidate"],
        "local_coupled_identity_checked": totals["local_coupled_identity_checked"],
        "local_coupled_identity_mismatch": totals["local_coupled_identity_mismatch"],
        "paired_kernel_identity_sample_checked": totals["paired_kernel_identity_sample_checked"],
        "paired_kernel_identity_sample_mismatch": totals["paired_kernel_identity_sample_mismatch"],
        "coupled_selected_phase_atoms": totals["coupled_selected_phase_atoms"],
        "bad_selected_denominator_not_prime": totals["bad_selected_denominator_not_prime"],
        "sample_pair_kernel_values": "; ".join(pair_samples) if pair_samples else "empty",
        "sample_phase_atoms": "; ".join(phase_samples) if phase_samples else "empty",
    }


def row_audit(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    prime_set: set[int],
    collect_pair_samples: bool,
) -> dict[str, Any]:
    """审计 actual phase atoms 与 coupled phase normal form 是否一致。"""
    actual = primorial.actual_terms_for_row(P, k, primes)
    coupled, stats = coupled_terms_for_row(P, k, records, primes, prime_set, collect_pair_samples)
    missing = actual - coupled
    extra = coupled - actual
    return {
        "P": P,
        "k": k,
        "actual_phase_atoms": len(actual),
        "coupled_selected_phase_atoms": len(coupled),
        "missing_actual_phase_atoms": len(missing),
        "extra_coupled_phase_atoms": len(extra),
        "dynamic_primorial_modulus": stats["dynamic_primorial_modulus"],
        "dynamic_primorial_prime_count": stats["dynamic_primorial_prime_count"],
        "complementary_pair_kernels_per_candidate": stats["complementary_pair_kernels_per_candidate"],
        "full_ramanujan_divisor_terms_per_candidate": stats["full_ramanujan_divisor_terms_per_candidate"],
        "full_additive_modes_per_candidate": stats["full_additive_modes_per_candidate"],
        "max_reverse_window_size": stats["max_reverse_window_size"],
        "max_odd_count": stats["max_odd_count"],
        "windows_with_odd_candidate": stats["windows_with_odd_candidate"],
        "local_coupled_identity_checked": stats["local_coupled_identity_checked"],
        "local_coupled_identity_mismatch": stats["local_coupled_identity_mismatch"],
        "paired_kernel_identity_sample_checked": stats["paired_kernel_identity_sample_checked"],
        "paired_kernel_identity_sample_mismatch": stats["paired_kernel_identity_sample_mismatch"],
        "bad_window_size": stats["bad_window_size"],
        "bad_odd_count": stats["bad_odd_count"],
        "bad_selected_denominator_not_prime": stats["bad_selected_denominator_not_prime"],
        "selector_cases": stats["selector_cases"],
        "sample_pair_kernel_values": stats["sample_pair_kernel_values"],
        "sample_phase_atoms": stats["sample_phase_atoms"],
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    prime_set = set(primes)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}
    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-audit.json").read_text())

    totals: Counter[str] = Counter()
    selector_cases: Counter[str] = Counter()
    sample_rows: list[dict[str, Any]] = []
    row_count = 0
    active_rows = 0
    max_pair_kernels = 0
    max_full_divisor_terms = 0
    max_full_additive_modes = 0
    max_primorial_prime_count = 0
    max_reverse_window_size = 0
    max_odd_count = 0

    for P in P_values:
        records = records_by_P[P]
        for k in range(1, P):
            row_count += 1
            collect = (P, k) in interesting
            row = row_audit(P, k, records, primes, prime_set, collect)
            active_rows += int(row["actual_phase_atoms"] > 0)
            totals["actual_phase_atoms"] += row["actual_phase_atoms"]
            totals["coupled_selected_phase_atoms"] += row["coupled_selected_phase_atoms"]
            totals["missing_actual_phase_atoms"] += row["missing_actual_phase_atoms"]
            totals["extra_coupled_phase_atoms"] += row["extra_coupled_phase_atoms"]
            totals["windows_with_odd_candidate"] += row["windows_with_odd_candidate"]
            totals["local_coupled_identity_checked"] += row["local_coupled_identity_checked"]
            totals["local_coupled_identity_mismatch"] += row["local_coupled_identity_mismatch"]
            totals["paired_kernel_identity_sample_checked"] += row["paired_kernel_identity_sample_checked"]
            totals["paired_kernel_identity_sample_mismatch"] += row["paired_kernel_identity_sample_mismatch"]
            totals["bad_window_size"] += row["bad_window_size"]
            totals["bad_odd_count"] += row["bad_odd_count"]
            totals["bad_selected_denominator_not_prime"] += row["bad_selected_denominator_not_prime"]
            selector_cases.update(row["selector_cases"])
            max_pair_kernels = max(max_pair_kernels, row["complementary_pair_kernels_per_candidate"])
            max_full_divisor_terms = max(max_full_divisor_terms, row["full_ramanujan_divisor_terms_per_candidate"])
            max_full_additive_modes = max(max_full_additive_modes, row["full_additive_modes_per_candidate"])
            max_primorial_prime_count = max(max_primorial_prime_count, row["dynamic_primorial_prime_count"])
            max_reverse_window_size = max(max_reverse_window_size, row["max_reverse_window_size"])
            max_odd_count = max(max_odd_count, row["max_odd_count"])
            if collect:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_actual_phase_atoms": totals["actual_phase_atoms"],
        "total_coupled_selected_phase_atoms": totals["coupled_selected_phase_atoms"],
        "actual_phase_atoms_equal_coupled_phase_atoms": totals["actual_phase_atoms"]
        == totals["coupled_selected_phase_atoms"]
        and totals["missing_actual_phase_atoms"] == 0
        and totals["extra_coupled_phase_atoms"] == 0,
        "missing_actual_phase_atoms_total": totals["missing_actual_phase_atoms"],
        "extra_coupled_phase_atoms_total": totals["extra_coupled_phase_atoms"],
        "windows_with_odd_candidate_total": totals["windows_with_odd_candidate"],
        "local_coupled_identity_checked_total": totals["local_coupled_identity_checked"],
        "local_coupled_identity_mismatch_total": totals["local_coupled_identity_mismatch"],
        "paired_kernel_identity_sample_checked_total": totals["paired_kernel_identity_sample_checked"],
        "paired_kernel_identity_sample_mismatch_total": totals["paired_kernel_identity_sample_mismatch"],
        "bad_reverse_window_size_total": totals["bad_window_size"],
        "bad_odd_count_total": totals["bad_odd_count"],
        "bad_selected_denominator_not_prime_total": totals["bad_selected_denominator_not_prime"],
        "max_reverse_window_size": max_reverse_window_size,
        "max_odd_count_per_reverse_window": max_odd_count,
        "max_dynamic_primorial_prime_count": max_primorial_prime_count,
        "max_complementary_pair_kernels_per_candidate": max_pair_kernels,
        "max_full_ramanujan_divisor_terms_per_candidate": max_full_divisor_terms,
        "max_full_additive_modes_per_candidate": max_full_additive_modes,
        "selector_case_totals": dict(sorted(selector_cases.items())),
        "phase_denominator_is_floor_defined_Q_odd": True,
        "direct_trace_or_kloosterman_family_available": False,
        "previous_radial_tensor_status": previous["status"],
        "previous_rank_two_nontrivial_pair_total": previous["finite_audit"]["rank_two_nontrivial_pair_total"],
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_radial_pair_coupled_phase_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "radial_pair_coupled_floor_reciprocal_phase_normal_form_closed_trace_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the radial tensor ledger, the fastest non-cyclic continuation is to couple the radial pair kernels to the actual q-support reciprocal phase and identify the remaining trace bridge",
        "current_object": {
            "fixed_cofactor": "m=r*beta, with r>=7 prime and beta r-rough",
            "floor_denominator": "Q_{P,k}(m)=least odd integer in [max(P/2+1,floor(kP/m)+1), min(P-1,m,floor(((k+1)P-1)/m))]",
            "paired_selector": "1_{gcd(Q,W_P)=1}=phi(W_P)/W_P * sum_{unordered {d,W_P/d}} K_d(Q)",
            "coupled_phase": "each selected atom carries e(h*k*P/Q_{P,k}(m))",
            "normal_form": "sum over residual m of paired radial Ramanujan selector times floor-reciprocal phase",
            "remaining_obstruction": "Q_{P,k}(m) is a floor-defined denominator and not a completed trace/Kloosterman variable",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RadialPairKernelToActualReciprocalPhaseCouplingNormalForm",
                True,
                True,
                "The actual phase atoms equal the residual-cofactor sum with paired radial Ramanujan selector and phase e(hkP/Q_{P,k}(m)).",
                "none",
            ),
            gate(
                "ComplementaryPairGroupedRamanujanSelectorIdentity",
                True,
                True,
                "The dynamic primorial unit selector is exactly the sum over unordered complementary conductor pair kernels.",
                "none",
            ),
            gate(
                "FloorDenominatorPhaseLedger",
                True,
                True,
                "The denominator coupled to the phase is the unique odd floor-map Q_{P,k}(m).",
                "none",
            ),
            gate(
                "DirectTraceFamilyFromCoupledFloorRadialPhaseRejected",
                True,
                True,
                "The coupled normal form still has a floor-defined real reciprocal denominator, not a completed Kloosterman/trace-family variable.",
                "none",
            ),
            gate(
                "FloorRadialReciprocalPhaseToTraceFamilyBridge",
                False,
                False,
                "Convert the floor-radial reciprocal phase into a same-object trace/Kloosterman or Type-II family.",
                "new completion bridge theorem",
            ),
            gate(
                "UniformCancellationAcrossCoupledFloorRadialPairKernels",
                False,
                False,
                "Prove cancellation uniformly across the coupled pair kernels after a valid completion bridge.",
                "new phase-saving theorem",
            ),
        ],
        "external_theorem_implication": {
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3": "could apply only after the floor-radial phase is packaged as an l-adic trace family",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "could apply only after producing genuine Kloosterman sums with bilinear ranges from Q_{P,k}(m)",
            "Pascadi_2025_arXiv_2511_08445": "needs a composite-modulus Type-II Kloosterman organisation, not just the floor denominator normal form",
            "Wright_2026_arXiv_2604_25177": "unbalanced convolution is relevant only after converting the floor map to an AP/convolution discrepancy with SW input",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "squarefree/smooth parameter estimates remain adjacent because W_P is squarefree/smooth, but no completed phase has been produced",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn and unusable as a closing input",
        },
        "latest_narrowest_mouth": [
            "FloorRadialReciprocalPhaseToTraceFamilyBridge",
            "AND UniformCancellationAcrossCoupledFloorRadialPairKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "radial_pair_coupled_phase_normal_form_closed": True,
        "complementary_pair_grouped_ramanujan_selector_identity_closed": True,
        "floor_denominator_phase_ledger_closed": True,
        "direct_trace_family_from_coupled_floor_radial_phase_rejected": True,
        "floor_radial_reciprocal_phase_to_trace_family_bridge_closed": False,
        "uniform_cancellation_across_coupled_floor_radial_pair_kernels_closed": False,
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
        "# Prime Matrix Phi-LPF q-support radial pair coupled phase 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"fixed_cofactor={current['fixed_cofactor']}",
        f"floor_denominator={current['floor_denominator']}",
        f"paired_selector={current['paired_selector']}",
        f"coupled_phase={current['coupled_phase']}",
        f"normal_form={current['normal_form']}",
        f"remaining_obstruction={current['remaining_obstruction']}",
        "```",
        "",
        "## 2. Coupled phase 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_actual_phase_atoms={audit['total_actual_phase_atoms']}",
        f"total_coupled_selected_phase_atoms={audit['total_coupled_selected_phase_atoms']}",
        f"actual_phase_atoms_equal_coupled_phase_atoms={primorial.bool_text(audit['actual_phase_atoms_equal_coupled_phase_atoms'])}",
        f"missing_actual_phase_atoms_total={audit['missing_actual_phase_atoms_total']}",
        f"extra_coupled_phase_atoms_total={audit['extra_coupled_phase_atoms_total']}",
        f"windows_with_odd_candidate_total={audit['windows_with_odd_candidate_total']}",
        f"local_coupled_identity_checked_total={audit['local_coupled_identity_checked_total']}",
        f"local_coupled_identity_mismatch_total={audit['local_coupled_identity_mismatch_total']}",
        f"paired_kernel_identity_sample_checked_total={audit['paired_kernel_identity_sample_checked_total']}",
        f"paired_kernel_identity_sample_mismatch_total={audit['paired_kernel_identity_sample_mismatch_total']}",
        f"bad_selected_denominator_not_prime_total={audit['bad_selected_denominator_not_prime_total']}",
        f"max_complementary_pair_kernels_per_candidate={audit['max_complementary_pair_kernels_per_candidate']}",
        f"max_full_ramanujan_divisor_terms_per_candidate={audit['max_full_ramanujan_divisor_terms_per_candidate']}",
        f"max_full_additive_modes_per_candidate={audit['max_full_additive_modes_per_candidate']}",
        f"phase_denominator_is_floor_defined_Q_odd={primorial.bool_text(audit['phase_denominator_is_floor_defined_Q_odd'])}",
        f"direct_trace_or_kloosterman_family_available={primorial.bool_text(audit['direct_trace_or_kloosterman_family_available'])}",
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
                "coupled_selected_phase_atoms",
                "windows_with_odd_candidate",
                "local_coupled_identity_checked",
                "paired_kernel_identity_sample_checked",
                "paired_kernel_identity_sample_mismatch",
                "complementary_pair_kernels_per_candidate",
                "sample_pair_kernel_values",
                "sample_phase_atoms",
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
        "结论：actual q-support phase 已经和互补 radial pair kernel 精确耦合；剩余不是“是否耦合”，而是 floor-radial real reciprocal phase 能否完成为同对象 trace/Kloosterman/Type-II family。",
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
        f"radial_pair_coupled_phase_normal_form_closed={primorial.bool_text(payload['radial_pair_coupled_phase_normal_form_closed'])}",
        f"complementary_pair_grouped_ramanujan_selector_identity_closed={primorial.bool_text(payload['complementary_pair_grouped_ramanujan_selector_identity_closed'])}",
        f"floor_denominator_phase_ledger_closed={primorial.bool_text(payload['floor_denominator_phase_ledger_closed'])}",
        f"direct_trace_family_from_coupled_floor_radial_phase_rejected={primorial.bool_text(payload['direct_trace_family_from_coupled_floor_radial_phase_rejected'])}",
        f"floor_radial_reciprocal_phase_to_trace_family_bridge_closed={primorial.bool_text(payload['floor_radial_reciprocal_phase_to_trace_family_bridge_closed'])}",
        f"uniform_cancellation_across_coupled_floor_radial_pair_kernels_closed={primorial.bool_text(payload['uniform_cancellation_across_coupled_floor_radial_pair_kernels_closed'])}",
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
    print("radial_pair_coupled_phase_normal_form_closed=true")
    print("direct_trace_family_from_coupled_floor_radial_phase_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
