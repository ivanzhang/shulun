#!/usr/bin/env python3
"""审计动态 Ramanujan 单位类的满 Fourier 支撑与精确截断障碍。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_full_ramanujan_spectrum_obstruction_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-audit.json

上一层把动态 primorial 单位类写成 Ramanujan 加性字符展开。本层继续
下钻“能否精确丢掉大多数模式”的问题。对

  f_W(n)=1_{gcd(n,W)=1}

在 Z/WZ 上的加性 Fourier 系数为

  fhat(a)=c_W(a)/W.

当 W 是平方自由 primorial 时，c_W(a) 对每个 a mod W 都非零；因此
精确 Fourier 支撑是满的，任何 proper mode truncation 都会改变 selector。
这不排除未来证明全谱抵消，但排除了“只保留少数精确模式”的非同对象捷径。
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


SLUG = "prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-external-theorem-match-audit.json",
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


def exact_gcd_bucket_stats(W: int, factors: list[int]) -> dict[str, Any]:
    """按 g=(a,W) 的精确桶核验满支撑、L1 与 L2 账本。"""
    divisor_rows = ramanujan.squarefree_divisor_data(factors)
    total_frequency_count = 0
    nonzero_frequency_count = 0
    l1_numerator = 0
    l2_numerator = 0
    min_abs_cw = None
    max_abs_cw = 0
    sample_buckets: list[dict[str, int]] = []

    for row in divisor_rows:
        g = row["d"]
        phi_g = row["phi"]
        W_over_g_factors = [ell for ell in factors if g % ell != 0]
        count = ramanujan.phi_squarefree(W_over_g_factors)
        abs_cw = phi_g
        total_frequency_count += count
        nonzero_frequency_count += count if abs_cw != 0 else 0
        l1_numerator += count * abs_cw
        l2_numerator += count * abs_cw * abs_cw
        min_abs_cw = abs_cw if min_abs_cw is None else min(min_abs_cw, abs_cw)
        max_abs_cw = max(max_abs_cw, abs_cw)
        if len(sample_buckets) < 8:
            sample_buckets.append({"g": g, "frequency_count": count, "abs_cW": abs_cw})

    phi_w = ramanujan.phi_squarefree(factors)
    l1 = Fraction(l1_numerator, W)
    l2 = Fraction(l2_numerator, W * W)
    return {
        "frequency_count_sum": total_frequency_count,
        "nonzero_frequency_count": nonzero_frequency_count,
        "all_frequencies_nonzero": nonzero_frequency_count == W,
        "minimum_exact_modes_for_exact_fourier_selector": W,
        "proper_exact_truncation_possible": False,
        "min_abs_cW": min_abs_cw,
        "max_abs_cW": max_abs_cw,
        "min_abs_normalized_coefficient": f"1/{W}",
        "max_abs_normalized_coefficient": format_fraction(Fraction(phi_w, W)),
        "l1_norm": format_fraction(l1),
        "l1_norm_matches_product_formula": l1 == Fraction((2 ** len(factors)) * phi_w, W),
        "l2_norm_squared": format_fraction(l2),
        "l2_norm_squared_matches_parseval": l2 == Fraction(phi_w, W),
        "sample_gcd_buckets": sample_buckets,
    }


def spectrum_stats_for(P: int, primes: list[int]) -> dict[str, Any]:
    """计算单个 P 的满谱障碍账本。"""
    W, factors = primorial.primorial_modulus(P, primes)
    phi_w = ramanujan.phi_squarefree(factors)
    bucket = exact_gcd_bucket_stats(W, factors)
    return {
        "P": P,
        "W_P": W,
        "sqrt_sieve_prime_count": len(factors),
        "phi_W": phi_w,
        "ramanujan_divisor_terms": 2 ** len(factors),
        "full_additive_frequency_count": W,
        "unit_density": format_fraction(Fraction(phi_w, W)),
        **bucket,
    }


def audit_spectrum(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的 primorial 模式族做满谱审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {101, 257, 971, 1009}

    sample_rows: list[dict[str, Any]] = []
    max_full_modes = 1
    max_divisor_terms = 1
    max_prime_count = 0
    max_l1_norm = Fraction(0, 1)
    bad_frequency_count_total = 0
    bad_nonzero_total = 0
    bad_l1_total = 0
    bad_l2_total = 0

    for P in P_values:
        row = spectrum_stats_for(P, primes)
        max_full_modes = max(max_full_modes, row["full_additive_frequency_count"])
        max_divisor_terms = max(max_divisor_terms, row["ramanujan_divisor_terms"])
        max_prime_count = max(max_prime_count, row["sqrt_sieve_prime_count"])
        l1_value = Fraction(row["l1_norm"]) if "/" in row["l1_norm"] else Fraction(int(row["l1_norm"]), 1)
        max_l1_norm = max(max_l1_norm, l1_value)
        bad_frequency_count_total += int(row["frequency_count_sum"] != row["W_P"])
        bad_nonzero_total += int(not row["all_frequencies_nonzero"])
        bad_l1_total += int(not row["l1_norm_matches_product_formula"])
        bad_l2_total += int(not row["l2_norm_squared_matches_parseval"])
        if P in interesting:
            compact = dict(row)
            compact["sample_gcd_buckets"] = row["sample_gcd_buckets"]
            sample_rows.append(compact)

    previous = json.loads((DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.json").read_text())
    previous_audit = previous["finite_audit"]
    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "max_full_additive_frequency_count": max_full_modes,
        "max_ramanujan_divisor_terms": max_divisor_terms,
        "max_sqrt_sieve_prime_count": max_prime_count,
        "max_l1_norm": format_fraction(max_l1_norm),
        "bad_frequency_count_total": bad_frequency_count_total,
        "bad_nonzero_frequency_total": bad_nonzero_total,
        "bad_l1_formula_total": bad_l1_total,
        "bad_l2_parseval_total": bad_l2_total,
        "all_exact_fourier_supports_full": bad_nonzero_total == 0 and bad_frequency_count_total == 0,
        "proper_exact_mode_truncation_possible_for_any_P": False,
        "previous_ramanujan_identity_checked_total": previous_audit["ramanujan_product_identity_checked_total"],
        "previous_ramanujan_identity_mismatch_total": previous_audit["ramanujan_product_identity_mismatch_total"],
        "previous_primorial_unit_selected_total": previous_audit["primorial_unit_selected_total"],
        "previous_primorial_unit_rejected_total": previous_audit["primorial_unit_rejected_total"],
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
    finite_audit = audit_spectrum()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_full_ramanujan_spectrum_obstruction_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "full_ramanujan_spectrum_obstruction_closed_exact_truncation_rejected",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after the dynamic Ramanujan expansion, the fastest non-cyclic continuation is to decide whether exact mode truncation is possible",
        "current_object": {
            "unit_selector": "f_W(n)=1_{gcd(n,W_P)=1} on Z/W_PZ",
            "additive_fourier_coefficient": "fhat(a)=c_{W_P}(a)/W_P",
            "squarefree_coefficient": "c_W(a)=prod_{ell|W, ell|a}(ell-1) prod_{ell|W, ell not|a}(-1)",
            "full_support": "c_{W_P}(a)!=0 for every a mod W_P",
            "exact_truncation_conclusion": "any proper additive-mode truncation changes the selector",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "AdditiveFourierFullSupportForPrimorialUnitSelector",
                True,
                True,
                "For squarefree W_P every additive Fourier coefficient c_{W_P}(a)/W_P is nonzero.",
                "none",
            ),
            gate(
                "ExactRamanujanModeTruncationRejected",
                True,
                True,
                "No proper subset of additive modes can reproduce the exact W_P-unit selector.",
                "none",
            ),
            gate(
                "RamanujanSpectrumL1L2Ledger",
                True,
                True,
                "The full-spectrum L1 and Parseval L2 ledgers are explicit and match product formulas.",
                "none",
            ),
            gate(
                "UniformCancellationAcrossFullDynamicRamanujanSpectrum",
                False,
                False,
                "Prove cancellation after keeping the full W_P dynamic frequency spectrum.",
                "new full-spectrum cancellation theorem",
            ),
            gate(
                "DynamicFullRamanujanSpectrumToUsableKloostermanCompletionBridge",
                False,
                False,
                "Organise the full dynamic spectrum into a same-object completed Kloosterman or Type-II family.",
                "new completion bridge",
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
            "Wright_2026_arXiv_2604_25177": "trilinear Kloosterman fractions still need a completed coefficient family; full W_P spectrum is not already organised",
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "bilinear trace-function technology is relevant after sheaf/trace-family packaging, but the current full W_P spectrum lacks that packaging",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-q bilinear Kloosterman estimates still require admissible bilinear ranges and coefficients",
            "Pascadi_2025_arXiv_2511_08445": "composite-modulus amplification still needs Type-II organisation beyond raw dynamic Fourier support",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "smooth/squarefree Kloosterman parameter sums are adjacent but do not estimate this pointwise P,k full-spectrum selector",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn; not usable as an external input",
        },
        "latest_narrowest_mouth": [
            "DynamicFullRamanujanSpectrumToUsableKloostermanCompletionBridge",
            "AND UniformCancellationAcrossFullDynamicRamanujanSpectrum",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "full_ramanujan_spectrum_obstruction_closed": True,
        "additive_fourier_full_support_proved": True,
        "exact_mode_truncation_rejected": True,
        "full_spectrum_cancellation_closed": False,
        "usable_kloosterman_completion_bridge_closed": False,
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
        "# Prime Matrix Phi-LPF q-support full Ramanujan spectrum obstruction 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"unit_selector={current['unit_selector']}",
        f"additive_fourier_coefficient={current['additive_fourier_coefficient']}",
        f"squarefree_coefficient={current['squarefree_coefficient']}",
        f"full_support={current['full_support']}",
        f"exact_truncation_conclusion={current['exact_truncation_conclusion']}",
        "```",
        "",
        "## 2. 满谱审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"max_full_additive_frequency_count={audit['max_full_additive_frequency_count']}",
        f"max_ramanujan_divisor_terms={audit['max_ramanujan_divisor_terms']}",
        f"max_sqrt_sieve_prime_count={audit['max_sqrt_sieve_prime_count']}",
        f"max_l1_norm={audit['max_l1_norm']}",
        f"bad_frequency_count_total={audit['bad_frequency_count_total']}",
        f"bad_nonzero_frequency_total={audit['bad_nonzero_frequency_total']}",
        f"bad_l1_formula_total={audit['bad_l1_formula_total']}",
        f"bad_l2_parseval_total={audit['bad_l2_parseval_total']}",
        f"all_exact_fourier_supports_full={primorial.bool_text(audit['all_exact_fourier_supports_full'])}",
        f"proper_exact_mode_truncation_possible_for_any_P={primorial.bool_text(audit['proper_exact_mode_truncation_possible_for_any_P'])}",
        f"previous_ramanujan_identity_checked_total={audit['previous_ramanujan_identity_checked_total']}",
        f"previous_ramanujan_identity_mismatch_total={audit['previous_ramanujan_identity_mismatch_total']}",
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
                "phi_W",
                "unit_density",
                "ramanujan_divisor_terms",
                "full_additive_frequency_count",
                "all_frequencies_nonzero",
                "minimum_exact_modes_for_exact_fourier_selector",
                "l1_norm",
                "l2_norm_squared",
                "sample_gcd_buckets",
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
        "结论：精确加性 Fourier 支撑是满的。Ramanujan 展开不能靠丢弃大多数模式成为 completed Kloosterman 输入；若要继续，必须对完整动态谱建立同对象 completion 与抵消。",
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
        f"full_ramanujan_spectrum_obstruction_closed={primorial.bool_text(payload['full_ramanujan_spectrum_obstruction_closed'])}",
        f"additive_fourier_full_support_proved={primorial.bool_text(payload['additive_fourier_full_support_proved'])}",
        f"exact_mode_truncation_rejected={primorial.bool_text(payload['exact_mode_truncation_rejected'])}",
        f"full_spectrum_cancellation_closed={primorial.bool_text(payload['full_spectrum_cancellation_closed'])}",
        f"usable_kloosterman_completion_bridge_closed={primorial.bool_text(payload['usable_kloosterman_completion_bridge_closed'])}",
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
    print("additive_fourier_full_support_proved=true")
    print("exact_mode_truncation_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
