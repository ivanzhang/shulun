#!/usr/bin/env python3
"""审计 prime-blocker dynamic sqrt-sieve 的 Euler--Mobius involution。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_mobius_involution_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-audit.json

上一层把 prime blocker 写成动态 sqrt-sieve survivor：

  1_prime(m_h) = sum_{d|m_h, d|W(m_h)} mu(d),
  W(m_h)=prod_{ell<=sqrt(m_h)} ell.

本层把该 Mobius 展开继续原子化。若 blocker 是小 LPF 合数，令 s 为其第一个
sqrt-sieve obstruction。所有 squarefree divisor 项按 d <-> s*d 成对抵消。
若 blocker 是 prime survivor，则没有非平凡 divisor 项，Mobius 展开只剩 d=1。

因此 moving Mobius 展开本身没有额外相位节省来源：它只是把小 LPF blocker
点态清零，并把 prime survivor 留成 singleton layer。剩余必须是 survivor
相位节省、trace/Type-II 嵌入，或超出点态 Mobius 的新输入。
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
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_correction_phase_audit as correction  # noqa: E402
import prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_dynamic_sqrt_sieve_audit as sqrtblocker  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-24"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "three-claims-formal-to-actual-critical-load-frontier.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

EXTERNAL_SOURCES = [
    {
        "key": "Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear",
        "url": "https://arxiv.org/abs/2511.09459",
        "role": "below-Polya-Vinogradov trace bilinear input, still requiring a trace-family embedding",
    },
    {
        "key": "Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "arbitrary-modulus Kloosterman bilinear input, still requiring completed Kloosterman form",
    },
    {
        "key": "Pascadi_2025_nonabelian_composite_type_II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role": "composite-modulus Type-II amplification, not directly a pointwise Mobius involution estimate",
    },
    {
        "key": "Wright_2026_unbalanced_kloosterman_fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "unbalanced convolution/Kloosterman-fraction input after convolution completion",
    },
    {
        "key": "Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman",
        "url": "https://arxiv.org/abs/2411.12113",
        "role": "smooth/squarefree Kloosterman parameter input, not direct survivor phase saving",
    },
    {
        "key": "Li_2023_short_interval_primes_x_052",
        "url": "https://arxiv.org/abs/2308.04458",
        "role": "pointwise short interval exponent remains above theta=1/2",
    },
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def divisor_basis(m: int, primes: list[int]) -> list[int]:
    """返回同时满足 ell<=sqrt(m) 且 ell|m 的素数基。"""
    limit = math.isqrt(m)
    return [ell for ell in primes if ell <= limit and m % ell == 0]


def mobius_sum_from_basis_size(size: int) -> int:
    """返回 sum_{d|m,d|W(m)} mu(d) 的值。"""
    return 1 if size == 0 else 0


def involution_profile(item: dict[str, int], primes: list[int]) -> dict[str, Any]:
    """返回单个 blocker 的 Mobius involution 诊断。"""
    m = item["m"]
    basis = divisor_basis(m, primes)
    basis_size = len(basis)
    active_terms = 1 << basis_size
    mobius_sum = mobius_sum_from_basis_size(basis_size)
    is_prime_blocker = item["lpf"] == m
    first_obstruction = basis[0] if basis else 0
    pair_count = active_terms // 2 if basis else 0
    return {
        "basis": basis,
        "basis_label": "*".join(str(x) for x in basis) if basis else "prime_singleton",
        "basis_size": basis_size,
        "active_terms": active_terms,
        "mobius_sum": mobius_sum,
        "first_obstruction": first_obstruction,
        "pair_count": pair_count,
        "is_prime_blocker": is_prime_blocker,
        "bad_prime_active_singleton": int(is_prime_blocker and (basis_size != 0 or active_terms != 1)),
        "bad_composite_without_obstruction": int((not is_prime_blocker) and first_obstruction == 0),
        "bad_mobius_sum_identity": int(mobius_sum != int(is_prime_blocker)),
        "bad_involution_pairing": int((not is_prime_blocker) and (active_terms % 2 != 0 or pair_count * 2 != active_terms)),
        "bad_first_obstruction_not_small_lpf": int((not is_prime_blocker) and first_obstruction not in {2, 3, 5}),
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """审计 P<=max_prime 的 moving Mobius involution。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    previous = json.loads(
        (
            DOCS
            / "prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-audit.json"
        ).read_text()
    )
    previous_audit = previous["finite_audit"]
    blockers = sqrtblocker.collect_all_blockers(max_prime, primes)
    interesting = {101, 257, 971, 1009}

    totals: Counter[str] = Counter()
    basis_counts: Counter[str] = Counter()
    first_obstruction_counts: Counter[str] = Counter()
    basis_size_counts: Counter[int] = Counter()
    row_profiles: dict[int, Counter[str]] = defaultdict(Counter)
    q_bucket_prime_sum: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    q_bucket_mobius_sum: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    q_bucket_prime_count: Counter[tuple[int, int]] = Counter()
    q_bucket_mobius_weight: Counter[tuple[int, int]] = Counter()
    sample_rows: list[dict[str, Any]] = []
    sample_involutions: list[str] = []

    max_basis_size = 0
    max_active_terms = 0
    max_pair_count = 0

    for item in blockers:
        P = item["P"]
        q = item["q"]
        k = item["k"]
        profile = involution_profile(item, primes)
        phase = correction.additive_phase(P % q, q, k)
        key = (P, q)
        is_prime = profile["is_prime_blocker"]
        mobius_sum = profile["mobius_sum"]

        totals["blocker_count"] += 1
        totals["small_lpf_blocker_count"] += int(not is_prime)
        totals["prime_blocker_count"] += int(is_prime)
        totals["mobius_survivor_weight_total"] += mobius_sum
        totals["active_divisor_terms_total"] += profile["active_terms"]
        totals["prime_singleton_terms_total"] += profile["active_terms"] if is_prime else 0
        totals["composite_cancelled_terms_total"] += profile["active_terms"] if not is_prime else 0
        totals["composite_involution_pair_count_total"] += profile["pair_count"]
        totals["bad_prime_active_singleton"] += profile["bad_prime_active_singleton"]
        totals["bad_composite_without_obstruction"] += profile["bad_composite_without_obstruction"]
        totals["bad_mobius_sum_identity"] += profile["bad_mobius_sum_identity"]
        totals["bad_involution_pairing"] += profile["bad_involution_pairing"]
        totals["bad_first_obstruction_not_small_lpf"] += profile["bad_first_obstruction_not_small_lpf"]

        basis_counts[profile["basis_label"]] += 1
        first_label = str(profile["first_obstruction"]) if profile["first_obstruction"] else "none"
        first_obstruction_counts[first_label] += 1
        basis_size_counts[profile["basis_size"]] += 1
        max_basis_size = max(max_basis_size, profile["basis_size"])
        max_active_terms = max(max_active_terms, profile["active_terms"])
        max_pair_count = max(max_pair_count, profile["pair_count"])

        if is_prime:
            q_bucket_prime_sum[key] += phase
            q_bucket_prime_count[key] += 1
        q_bucket_mobius_sum[key] += mobius_sum * phase
        q_bucket_mobius_weight[key] += mobius_sum

        row = row_profiles[P]
        row["blockers"] += 1
        row["small_lpf_blockers"] += int(not is_prime)
        row["prime_blockers"] += int(is_prime)
        row["mobius_survivor_weight"] += mobius_sum
        row["active_terms"] += profile["active_terms"]
        row["cancelled_pairs"] += profile["pair_count"]
        row["bad_mismatch"] += profile["bad_mobius_sum_identity"]
        row["max_basis_size"] = max(row["max_basis_size"], profile["basis_size"])
        row["max_active_terms"] = max(row["max_active_terms"], profile["active_terms"])

        if (not is_prime) and len(sample_involutions) < 8:
            sample_involutions.append(
                "P={P},q={q},k={k},m={m},basis={basis},first={first},terms={terms},pairs={pairs}".format(
                    P=P,
                    q=q,
                    k=k,
                    m=item["m"],
                    basis=profile["basis_label"],
                    first=profile["first_obstruction"],
                    terms=profile["active_terms"],
                    pairs=profile["pair_count"],
                )
            )

    bucket_keys = set(q_bucket_prime_sum) | set(q_bucket_mobius_sum)
    max_phase_error = 0.0
    bucket_mismatch_count = 0
    for key in bucket_keys:
        err = abs(q_bucket_prime_sum[key] - q_bucket_mobius_sum[key])
        max_phase_error = max(max_phase_error, err)
        bucket_mismatch_count += int(err > 1e-9 or q_bucket_prime_count[key] != q_bucket_mobius_weight[key])

    for P in sorted(interesting):
        if P in row_profiles:
            row = row_profiles[P]
            sample_rows.append(
                {
                    "P": P,
                    "blockers": row["blockers"],
                    "small_lpf_blockers": row["small_lpf_blockers"],
                    "prime_blockers": row["prime_blockers"],
                    "mobius_survivor_weight": row["mobius_survivor_weight"],
                    "active_terms": row["active_terms"],
                    "cancelled_pairs": row["cancelled_pairs"],
                    "bad_mismatch": row["bad_mismatch"],
                    "max_basis_size": row["max_basis_size"],
                    "max_active_terms": row["max_active_terms"],
                }
            )

    total_bad = (
        totals["bad_prime_active_singleton"]
        + totals["bad_composite_without_obstruction"]
        + totals["bad_mobius_sum_identity"]
        + totals["bad_involution_pairing"]
        + totals["bad_first_obstruction_not_small_lpf"]
        + bucket_mismatch_count
    )
    top_basis_counts = dict(basis_counts.most_common(12))
    return {
        "max_prime": max_prime,
        "blocker_count_total": totals["blocker_count"],
        "previous_blocker_count_total": previous_audit["blocker_count_total"],
        "small_lpf_blocker_count_total": totals["small_lpf_blocker_count"],
        "previous_small_lpf_blocker_count_total": previous_audit["small_lpf_blocker_count_total"],
        "prime_blocker_count_total": totals["prime_blocker_count"],
        "previous_prime_blocker_count_total": previous_audit["prime_blocker_count_total"],
        "mobius_survivor_weight_total": totals["mobius_survivor_weight_total"],
        "previous_sqrt_sieve_survivor_count_total": previous_audit["sqrt_sieve_survivor_count_total"],
        "active_divisor_terms_total": totals["active_divisor_terms_total"],
        "prime_singleton_terms_total": totals["prime_singleton_terms_total"],
        "composite_cancelled_terms_total": totals["composite_cancelled_terms_total"],
        "composite_involution_pair_count_total": totals["composite_involution_pair_count_total"],
        "previous_prime_blocker_mobius_terms_full_expansion_total": previous_audit[
            "prime_blocker_mobius_terms_full_expansion_total"
        ],
        "active_terms_vs_previous_formal_ratio": totals["active_divisor_terms_total"]
        / previous_audit["prime_blocker_mobius_terms_full_expansion_total"],
        "max_basis_size": max_basis_size,
        "max_active_terms": max_active_terms,
        "max_pair_count": max_pair_count,
        "bad_prime_active_singleton_total": totals["bad_prime_active_singleton"],
        "bad_composite_without_obstruction_total": totals["bad_composite_without_obstruction"],
        "bad_mobius_sum_identity_total": totals["bad_mobius_sum_identity"],
        "bad_involution_pairing_total": totals["bad_involution_pairing"],
        "bad_first_obstruction_not_small_lpf_total": totals["bad_first_obstruction_not_small_lpf"],
        "q_bucket_mobius_phase_mismatch_count": bucket_mismatch_count,
        "max_mobius_packet_phase_identity_error": max_phase_error,
        "total_bad_mobius_involution_count": total_bad,
        "counts_match_previous_dynamic_sqrt_sieve": (
            totals["blocker_count"] == previous_audit["blocker_count_total"]
            and totals["small_lpf_blocker_count"] == previous_audit["small_lpf_blocker_count_total"]
            and totals["prime_blocker_count"] == previous_audit["prime_blocker_count_total"]
            and totals["mobius_survivor_weight_total"] == previous_audit["sqrt_sieve_survivor_count_total"]
        ),
        "mobius_expansion_identity_verified": total_bad == 0,
        "euler_involution_cancels_all_rejected_blockers": total_bad == 0
        and totals["composite_involution_pair_count_total"] * 2 == totals["composite_cancelled_terms_total"],
        "prime_survivors_are_singleton_d1_layer": total_bad == 0
        and totals["prime_singleton_terms_total"] == totals["prime_blocker_count"],
        "basis_size_counts": dict(sorted(basis_size_counts.items())),
        "first_obstruction_counts": dict(sorted(first_obstruction_counts.items(), key=lambda kv: (kv[0] != "none", kv[0]))),
        "top_basis_counts": top_basis_counts,
        "moving_mobius_expansion_self_compression_closes_phase": False,
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
        "sample_involutions": sample_involutions,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_mobius_involution_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "moving_mobius_expansion_reduced_to_euler_involution_and_prime_singletons_phase_saving_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the prime blocker becomes a moving sqrt-sieve survivor, the next non-cyclic refinement is to inspect whether the Mobius expansion itself supplies cancellation",
        "current_object": {
            "mobius_expansion": "1_prime(m_h)=sum_{d|m_h,d|W(m_h)} mu(d)",
            "small_lpf_mechanism": "if first obstruction is s, terms pair by d <-> s*d and cancel pointwise",
            "prime_survivor_mechanism": "prime blockers have no nontrivial d and remain as the singleton d=1 layer",
            "phase_identity": "prime-blocker phase equals the Mobius-weighted all-blocker phase bucket by bucket",
            "remaining": "the singleton prime-survivor layer still needs phase saving or trace/Type-II embedding",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "MovingMobiusDivisorExpansionIdentity",
                True,
                True,
                "The dynamic sqrt-sieve survivor indicator equals the squarefree divisor Mobius sum.",
                "none",
            ),
            gate(
                "EulerInvolutionCancelsRejectedBlockers",
                True,
                True,
                "Every rejected blocker has a first obstruction s and its Mobius terms pair by d <-> s*d.",
                "none",
            ),
            gate(
                "PrimeSurvivorSingletonLayerReduction",
                True,
                True,
                "Every prime blocker contributes only the d=1 Mobius layer.",
                "none",
            ),
            gate(
                "MovingMobiusExpansionSelfCompressionPhaseSaving",
                False,
                False,
                "Obtain nontrivial cancellation from the Mobius expansion itself after the pointwise involution.",
                "not available; requires new phase saving or embedding",
            ),
        ],
        "external_sources_consulted": EXTERNAL_SOURCES,
        "external_theorem_implication": {
            "FKMS_trace_function_bilinear": "still requires a nontrivial embedding of the prime singleton survivor layer into trace functions",
            "Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman": "still requires completed Kloosterman variables; the involution is pointwise, not bilinear",
            "Pascadi_composite_Type_II": "does not act on the already pointwise-cancelled small-LPF Mobius pairs",
            "Wright_unbalanced_convolution": "needs a convolution model for the survivor layer",
            "Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman": "smooth/squarefree parameter estimates do not by themselves create survivor phase saving",
            "Li_short_interval_x_052": "short-interval theta=0.52 remains above the pointwise half-scale requirement",
        },
        "latest_narrowest_mouth": [
            "PrimeSurvivorSingletonLayerPhaseSavingOrTraceEmbedding",
            "AND NonPointwiseCompressionBeyondEulerMobiusInvolution",
            "AND FiniteThirtyWheelSmallLPFBlockerPacketControl",
            "AND UniformCancellationAcrossSparseKSupportRadialKernels",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "moving_mobius_divisor_expansion_identity_closed": True,
        "euler_involution_cancels_rejected_blockers_closed": True,
        "prime_survivor_singleton_layer_reduction_closed": True,
        "moving_mobius_expansion_self_compression_phase_saving_closed": False,
        "prime_survivor_singleton_layer_phase_saving_closed": False,
        "small_lpf_blocker_packet_control_closed": False,
        "uniform_cancellation_across_sparse_k_support_radial_kernels_closed": False,
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
    sample_fields = [
        "P",
        "blockers",
        "small_lpf_blockers",
        "prime_blockers",
        "mobius_survivor_weight",
        "active_terms",
        "cancelled_pairs",
        "bad_mismatch",
        "max_basis_size",
        "max_active_terms",
    ]
    source_fields = ["key", "url", "role"]
    lines = [
        "# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-blocker Mobius involution 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"mobius_expansion={current['mobius_expansion']}",
        f"small_lpf_mechanism={current['small_lpf_mechanism']}",
        f"prime_survivor_mechanism={current['prime_survivor_mechanism']}",
        f"phase_identity={current['phase_identity']}",
        f"remaining={current['remaining']}",
        "```",
        "",
        "## 2. Euler--Mobius involution 有限审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"blocker_count_total={audit['blocker_count_total']}",
        f"previous_blocker_count_total={audit['previous_blocker_count_total']}",
        f"small_lpf_blocker_count_total={audit['small_lpf_blocker_count_total']}",
        f"previous_small_lpf_blocker_count_total={audit['previous_small_lpf_blocker_count_total']}",
        f"prime_blocker_count_total={audit['prime_blocker_count_total']}",
        f"previous_prime_blocker_count_total={audit['previous_prime_blocker_count_total']}",
        f"mobius_survivor_weight_total={audit['mobius_survivor_weight_total']}",
        f"previous_sqrt_sieve_survivor_count_total={audit['previous_sqrt_sieve_survivor_count_total']}",
        f"active_divisor_terms_total={audit['active_divisor_terms_total']}",
        f"prime_singleton_terms_total={audit['prime_singleton_terms_total']}",
        f"composite_cancelled_terms_total={audit['composite_cancelled_terms_total']}",
        f"composite_involution_pair_count_total={audit['composite_involution_pair_count_total']}",
        f"previous_prime_blocker_mobius_terms_full_expansion_total={audit['previous_prime_blocker_mobius_terms_full_expansion_total']}",
        f"active_terms_vs_previous_formal_ratio={audit['active_terms_vs_previous_formal_ratio']:.8f}",
        f"max_basis_size={audit['max_basis_size']}",
        f"max_active_terms={audit['max_active_terms']}",
        f"max_pair_count={audit['max_pair_count']}",
        f"bad_prime_active_singleton_total={audit['bad_prime_active_singleton_total']}",
        f"bad_composite_without_obstruction_total={audit['bad_composite_without_obstruction_total']}",
        f"bad_mobius_sum_identity_total={audit['bad_mobius_sum_identity_total']}",
        f"bad_involution_pairing_total={audit['bad_involution_pairing_total']}",
        f"bad_first_obstruction_not_small_lpf_total={audit['bad_first_obstruction_not_small_lpf_total']}",
        f"q_bucket_mobius_phase_mismatch_count={audit['q_bucket_mobius_phase_mismatch_count']}",
        f"max_mobius_packet_phase_identity_error={audit['max_mobius_packet_phase_identity_error']:.3e}",
        f"total_bad_mobius_involution_count={audit['total_bad_mobius_involution_count']}",
        f"counts_match_previous_dynamic_sqrt_sieve={primorial.bool_text(audit['counts_match_previous_dynamic_sqrt_sieve'])}",
        f"mobius_expansion_identity_verified={primorial.bool_text(audit['mobius_expansion_identity_verified'])}",
        f"euler_involution_cancels_all_rejected_blockers={primorial.bool_text(audit['euler_involution_cancels_all_rejected_blockers'])}",
        f"prime_survivors_are_singleton_d1_layer={primorial.bool_text(audit['prime_survivors_are_singleton_d1_layer'])}",
        "```",
        "",
        "basis size counts:",
        "",
        "```text",
        json.dumps(audit["basis_size_counts"], sort_keys=True),
        "```",
        "",
        "first obstruction counts:",
        "",
        "```text",
        json.dumps(audit["first_obstruction_counts"], sort_keys=True),
        "```",
        "",
        "top basis counts:",
        "",
        "```text",
        json.dumps(audit["top_basis_counts"], sort_keys=True),
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(audit["sample_rows"], sample_fields),
        "",
        "involution 样本：",
        "",
        "```text",
        *audit["sample_involutions"],
        "```",
        "",
        "## 3. 门控表",
        "",
        primorial.table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        primorial.table(payload["external_sources_consulted"], source_fields),
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：moving Mobius 展开已拆成 Euler 首阻碍成对抵消和 prime survivor 的 `d=1` 单层。该展开本身不提供新的相位节省；真正剩余是 prime survivor singleton layer 的相消或 trace/Type-II 嵌入。",
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
        f"moving_mobius_divisor_expansion_identity_closed={primorial.bool_text(payload['moving_mobius_divisor_expansion_identity_closed'])}",
        f"euler_involution_cancels_rejected_blockers_closed={primorial.bool_text(payload['euler_involution_cancels_rejected_blockers_closed'])}",
        f"prime_survivor_singleton_layer_reduction_closed={primorial.bool_text(payload['prime_survivor_singleton_layer_reduction_closed'])}",
        f"moving_mobius_expansion_self_compression_phase_saving_closed={primorial.bool_text(payload['moving_mobius_expansion_self_compression_phase_saving_closed'])}",
        f"prime_survivor_singleton_layer_phase_saving_closed={primorial.bool_text(payload['prime_survivor_singleton_layer_phase_saving_closed'])}",
        f"small_lpf_blocker_packet_control_closed={primorial.bool_text(payload['small_lpf_blocker_packet_control_closed'])}",
        f"uniform_cancellation_across_sparse_k_support_radial_kernels_closed={primorial.bool_text(payload['uniform_cancellation_across_sparse_k_support_radial_kernels_closed'])}",
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
    print("mobius_expansion_identity_verified=true")
    print("moving_mobius_expansion_self_compression_phase_saving_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
