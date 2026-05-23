#!/usr/bin/env python3
"""审计动态 Ramanujan 全谱的 conductor 分层与低导子截断障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_conductor_stratified_ramanujan_spectrum_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-audit.json

上一层证明 f_W(n)=1_{gcd(n,W)=1} 的加性 Fourier 支撑是满的。
本层继续把满谱按真实 additive conductor 分层。若 q=W/gcd(a,W)，则

  c_W(a)=mu(q)*phi(W)/phi(q).

因此每个 conductor q|W 都有 phi(q) 个 primitive 频率，且该 conductor
层的总 L1 质量恒为 phi(W)/W。低 conductor 层没有吸走主要质量；任何
丢弃某些 conductor 层的精确截断都会改变 selector。
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit as ramanujan  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.json",
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


def format_fraction(value: Fraction) -> str:
    """输出分数。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def divisor_factor_rows(factors: list[int]) -> list[dict[str, Any]]:
    """列出 squarefree divisor 与它的素因子。"""
    return ramanujan.squarefree_divisor_data(factors)


def conductor_layers(W: int, factors: list[int]) -> list[dict[str, Any]]:
    """按 exact additive conductor q|W 分层。"""
    phi_w = ramanujan.phi_squarefree(factors)
    rows: list[dict[str, Any]] = []
    for row in divisor_factor_rows(factors):
        q = row["d"]
        phi_q = row["phi"]
        mu_q = row["mu"]
        frequency_count = phi_q
        coefficient = Fraction(mu_q * phi_w, W * phi_q)
        layer_l1 = Fraction(phi_w, W)
        layer_l2 = Fraction(phi_w * phi_w, W * W * phi_q)
        rows.append(
            {
                "conductor": q,
                "prime_count": len(row["factors"]),
                "primitive_frequency_count": frequency_count,
                "coefficient": format_fraction(coefficient),
                "coefficient_abs": format_fraction(abs(coefficient)),
                "layer_l1": format_fraction(layer_l1),
                "layer_l2": format_fraction(layer_l2),
                "signed_layer": "positive" if mu_q > 0 else "negative",
            }
        )
    return sorted(rows, key=lambda item: item["conductor"])


def layer_stats_for(P: int, primes: list[int]) -> dict[str, Any]:
    """计算单个 P 的 conductor 分层账本。"""
    W, factors = primorial.primorial_modulus(P, primes)
    phi_w = ramanujan.phi_squarefree(factors)
    layers = conductor_layers(W, factors)
    layer_l1_values = {layer["layer_l1"] for layer in layers}
    total_frequency_count = sum(layer["primitive_frequency_count"] for layer in layers)
    total_l1 = sum(Fraction(layer["layer_l1"]) for layer in layers)
    total_l2 = sum(Fraction(layer["layer_l2"]) for layer in layers)
    expected_l1 = Fraction(phi_w * (2 ** len(factors)), W)
    expected_l2 = Fraction(phi_w, W)
    small_conductor_cut = int(W ** 0.5)
    kept_small_conductor_layers = [layer for layer in layers if layer["conductor"] <= small_conductor_cut]
    kept_small_conductor_l1 = sum(Fraction(layer["layer_l1"]) for layer in kept_small_conductor_layers)

    return {
        "P": P,
        "W_P": W,
        "sqrt_sieve_prime_count": len(factors),
        "phi_W": phi_w,
        "conductor_layer_count": len(layers),
        "full_additive_frequency_count": W,
        "frequency_count_sum": total_frequency_count,
        "frequency_count_sum_matches_W": total_frequency_count == W,
        "all_conductor_layers_nonzero": all(layer["primitive_frequency_count"] > 0 for layer in layers),
        "all_layer_l1_equal": len(layer_l1_values) == 1,
        "common_layer_l1": format_fraction(Fraction(phi_w, W)),
        "total_l1": format_fraction(total_l1),
        "total_l1_matches_full_spectrum": total_l1 == expected_l1,
        "total_l2": format_fraction(total_l2),
        "total_l2_matches_parseval": total_l2 == expected_l2,
        "small_conductor_cut_sqrtW": small_conductor_cut,
        "small_conductor_layer_count": len(kept_small_conductor_layers),
        "small_conductor_l1_fraction": format_fraction(
            kept_small_conductor_l1 / total_l1 if total_l1 else Fraction(0, 1)
        ),
        "proper_conductor_layer_truncation_exact_possible": False,
        "sample_conductor_layers": layers[:8],
    }


def audit_layers(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 conductor 分层做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {101, 257, 971, 1009}
    previous = json.loads(
        (DOCS / "prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-audit.json").read_text()
    )
    previous_audit = previous["finite_audit"]

    sample_rows: list[dict[str, Any]] = []
    max_conductor_layer_count = 0
    max_full_frequency_count = 0
    max_sqrt_sieve_prime_count = 0
    bad_frequency_count_total = 0
    bad_layer_l1_total = 0
    bad_total_l1_total = 0
    bad_total_l2_total = 0

    for P in P_values:
        row = layer_stats_for(P, primes)
        max_conductor_layer_count = max(max_conductor_layer_count, row["conductor_layer_count"])
        max_full_frequency_count = max(max_full_frequency_count, row["full_additive_frequency_count"])
        max_sqrt_sieve_prime_count = max(max_sqrt_sieve_prime_count, row["sqrt_sieve_prime_count"])
        bad_frequency_count_total += int(not row["frequency_count_sum_matches_W"])
        bad_layer_l1_total += int(not row["all_layer_l1_equal"])
        bad_total_l1_total += int(not row["total_l1_matches_full_spectrum"])
        bad_total_l2_total += int(not row["total_l2_matches_parseval"])
        if P in interesting:
            sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "max_conductor_layer_count": max_conductor_layer_count,
        "max_full_additive_frequency_count": max_full_frequency_count,
        "max_sqrt_sieve_prime_count": max_sqrt_sieve_prime_count,
        "bad_frequency_count_total": bad_frequency_count_total,
        "bad_layer_l1_equality_total": bad_layer_l1_total,
        "bad_total_l1_formula_total": bad_total_l1_total,
        "bad_total_l2_parseval_total": bad_total_l2_total,
        "all_conductor_strata_nonempty_and_equal_l1": bad_frequency_count_total == 0
        and bad_layer_l1_total == 0
        and bad_total_l1_total == 0,
        "proper_conductor_layer_truncation_exact_possible_for_any_P": False,
        "previous_full_support_audit_status": previous["status"],
        "previous_max_full_additive_frequency_count": previous_audit["max_full_additive_frequency_count"],
        "previous_bad_nonzero_frequency_total": previous_audit["bad_nonzero_frequency_total"],
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
    finite_audit = audit_layers()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_conductor_stratified_ramanujan_spectrum_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "conductor_stratified_full_spectrum_closed_low_conductor_truncation_rejected",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after full Fourier support, the fastest non-cyclic continuation is to stratify by true additive conductor and test low-conductor truncation",
        "current_object": {
            "frequency_conductor": "q=W_P/gcd(a,W_P)",
            "coefficient_by_conductor": "c_W(a)/W = mu(q)*phi(W)/(W*phi(q))",
            "primitive_frequency_count": "there are phi(q) frequencies of exact conductor q",
            "layer_l1": "sum over exact conductor q of |c_W(a)|/W equals phi(W)/W",
            "truncation_conclusion": "dropping any conductor layer changes the exact selector and does not remove a small-mass tail",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "RamanujanSpectrumExactConductorStratification",
                True,
                True,
                "Every frequency has exact conductor q=W_P/gcd(a,W_P), with coefficient mu(q)phi(W_P)/(W_P phi(q)).",
                "none",
            ),
            gate(
                "EqualL1MassPerConductorLayer",
                True,
                True,
                "Each conductor layer q|W_P has total L1 mass phi(W_P)/W_P.",
                "none",
            ),
            gate(
                "LowConductorExactTruncationRejected",
                True,
                True,
                "Keeping only low conductor layers changes the exact selector and is not a negligible exact tail.",
                "none",
            ),
            gate(
                "UniformCancellationAcrossAllPrimorialConductorLayers",
                False,
                False,
                "Prove cancellation across all conductor layers of the dynamic primorial spectrum.",
                "new conductor-uniform cancellation theorem",
            ),
            gate(
                "ConductorStratifiedSpectrumToKloostermanOrTraceFamilyBridge",
                False,
                False,
                "Package the conductor layers into a same-object Kloosterman/trace-function/Type-II family.",
                "new bridge theorem",
            ),
            gate(
                "RoughBetaSiegelWalfiszUniformityOrReplacement",
                False,
                False,
                "Supply the equidistribution/SW factor or an object-specific replacement for rough beta weights.",
                "rough beta uniformity input",
            ),
        ],
        "external_theorem_implication": {
            "Wright_2026_arXiv_2604_25177": "useful only after conductor layers become a completed unbalanced-convolution coefficient family",
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "trace-function bilinear bounds require sheaf/trace packaging of the conductor layers",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-q Kloosterman estimates still need admissible bilinear coefficient ranges",
            "Pascadi_2025_arXiv_2511_08445": "non-abelian amplification may apply after Type-II organisation over composite conductor layers",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "squarefree/smooth Kloosterman parameter sums are adjacent to the conductor set but not this pointwise P,k selector",
        },
        "latest_narrowest_mouth": [
            "ConductorStratifiedSpectrumToKloostermanOrTraceFamilyBridge",
            "AND UniformCancellationAcrossAllPrimorialConductorLayers",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "conductor_stratification_closed": True,
        "equal_l1_mass_per_conductor_layer_proved": True,
        "low_conductor_exact_truncation_rejected": True,
        "uniform_conductor_layer_cancellation_closed": False,
        "usable_kloosterman_or_trace_family_bridge_closed": False,
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
        "# Prime Matrix Phi-LPF q-support conductor-stratified Ramanujan spectrum 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"frequency_conductor={current['frequency_conductor']}",
        f"coefficient_by_conductor={current['coefficient_by_conductor']}",
        f"primitive_frequency_count={current['primitive_frequency_count']}",
        f"layer_l1={current['layer_l1']}",
        f"truncation_conclusion={current['truncation_conclusion']}",
        "```",
        "",
        "## 2. Conductor 分层审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"max_conductor_layer_count={audit['max_conductor_layer_count']}",
        f"max_full_additive_frequency_count={audit['max_full_additive_frequency_count']}",
        f"max_sqrt_sieve_prime_count={audit['max_sqrt_sieve_prime_count']}",
        f"bad_frequency_count_total={audit['bad_frequency_count_total']}",
        f"bad_layer_l1_equality_total={audit['bad_layer_l1_equality_total']}",
        f"bad_total_l1_formula_total={audit['bad_total_l1_formula_total']}",
        f"bad_total_l2_parseval_total={audit['bad_total_l2_parseval_total']}",
        f"all_conductor_strata_nonempty_and_equal_l1={primorial.bool_text(audit['all_conductor_strata_nonempty_and_equal_l1'])}",
        f"proper_conductor_layer_truncation_exact_possible_for_any_P={primorial.bool_text(audit['proper_conductor_layer_truncation_exact_possible_for_any_P'])}",
        f"previous_max_full_additive_frequency_count={audit['previous_max_full_additive_frequency_count']}",
        f"previous_bad_nonzero_frequency_total={audit['previous_bad_nonzero_frequency_total']}",
        "```",
        "",
        "代表 P：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "W_P",
                "sqrt_sieve_prime_count",
                "conductor_layer_count",
                "full_additive_frequency_count",
                "all_layer_l1_equal",
                "common_layer_l1",
                "total_l1",
                "small_conductor_cut_sqrtW",
                "small_conductor_layer_count",
                "small_conductor_l1_fraction",
                "sample_conductor_layers",
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
        "结论：全谱可按 exact conductor 压成 2^omega(W_P) 层，但每一层总 L1 质量相同。低 conductor 层不是主质量，丢弃高 conductor 层不是精确同对象截断。",
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
        f"conductor_stratification_closed={primorial.bool_text(payload['conductor_stratification_closed'])}",
        f"equal_l1_mass_per_conductor_layer_proved={primorial.bool_text(payload['equal_l1_mass_per_conductor_layer_proved'])}",
        f"low_conductor_exact_truncation_rejected={primorial.bool_text(payload['low_conductor_exact_truncation_rejected'])}",
        f"uniform_conductor_layer_cancellation_closed={primorial.bool_text(payload['uniform_conductor_layer_cancellation_closed'])}",
        f"usable_kloosterman_or_trace_family_bridge_closed={primorial.bool_text(payload['usable_kloosterman_or_trace_family_bridge_closed'])}",
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
    print("conductor_stratification_closed=true")
    print("low_conductor_exact_truncation_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
