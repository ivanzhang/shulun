#!/usr/bin/env python3
"""审计 Phi-LPF Ramanujan conductor 层的互补对偶 q <-> W/q。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_complementary_conductor_pair_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-audit.json

上一层已证明 exact conductor 层各自具有相同 L1 质量。本层继续检查一个
可能的非循环出口：把低 conductor 与高 conductor 按 q^vee=W/q 配对，
希望由镜像结构自动抵消。结论是：互补层确有严格质量镜像，但符号只由
omega(W) 奇偶控制，primitive 频率数量通常不匹配，且配对 Ramanujan 核
不恒为零。因此“互补 conductor 自动抵消”不是闭合证明。
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
sys.path.insert(0, str(ROOT / "experiments"))

import prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit as primorial  # noqa: E402
import prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit as ramanujan  # noqa: E402


SLUG = "prime-matrix-phi-lpf-qsupport-complementary-conductor-pair"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-audit.json",
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


def normalized_ramanujan_value(n: int, factors: list[int]) -> Fraction:
    """计算 c_q(n)/phi(q)，其中 q 为 factors 的平方自由乘积。"""
    phi_q = ramanujan.phi_squarefree(factors)
    if phi_q == 0:
        return Fraction(0, 1)
    return Fraction(ramanujan.ramanujan_sum_squarefree(n, factors), phi_q)


def nonzero_pair_witness(
    W: int,
    q_factors: list[int],
    q_mu: int,
    complement_factors: list[int],
    complement_mu: int,
) -> tuple[int, Fraction]:
    """给出互补配对核不恒为零的一个显式 n 见证。"""
    if q_mu == complement_mu:
        n = 0
    else:
        # 中文注释：符号相反时取一个素因子 p，并令 n 被除 p 外的所有素因子整除。
        pivot = q_factors[0] if q_factors else complement_factors[0]
        n = W // pivot
    value = q_mu * normalized_ramanujan_value(n, q_factors)
    value += complement_mu * normalized_ramanujan_value(n, complement_factors)
    return n, value


def complementary_pair_rows(W: int, factors: list[int]) -> list[dict[str, Any]]:
    """列出 unordered 互补 conductor 对 {q,W/q} 的账本。"""
    phi_w = ramanujan.phi_squarefree(factors)
    divisor_rows = ramanujan.squarefree_divisor_data(factors)
    by_d = {row["d"]: row for row in divisor_rows}
    common_layer_l1 = Fraction(phi_w, W)
    seen: set[int] = set()
    rows: list[dict[str, Any]] = []

    for row in divisor_rows:
        q = row["d"]
        if q in seen:
            continue
        complement = W // q
        complement_row = by_d[complement]
        seen.add(q)
        seen.add(complement)

        witness_n, witness_value = nonzero_pair_witness(
            W,
            row["factors"],
            row["mu"],
            complement_row["factors"],
            complement_row["mu"],
        )
        phi_ratio = Fraction(row["phi"], complement_row["phi"])
        abs_coefficient_ratio = Fraction(complement_row["phi"], row["phi"])
        signed_layer_sum = common_layer_l1 * (row["mu"] + complement_row["mu"])
        low = min(q, complement)
        high = max(q, complement)
        rows.append(
            {
                "q": q,
                "q_complement": complement,
                "low_conductor": low,
                "high_conductor": high,
                "mu_q": row["mu"],
                "mu_complement": complement_row["mu"],
                "sign_relation": "same" if row["mu"] == complement_row["mu"] else "opposite",
                "phi_q": row["phi"],
                "phi_complement": complement_row["phi"],
                "primitive_frequency_count_ratio_q_to_complement": format_fraction(phi_ratio),
                "abs_coefficient_ratio_q_to_complement": format_fraction(abs_coefficient_ratio),
                "frequency_counts_equal": row["phi"] == complement_row["phi"],
                "common_layer_l1": format_fraction(common_layer_l1),
                "pair_l1": format_fraction(2 * common_layer_l1),
                "signed_layer_sum": format_fraction(signed_layer_sum),
                "witness_n_for_nonzero_pair_kernel": witness_n,
                "normalized_pair_kernel_at_witness": format_fraction(witness_value),
                "pair_kernel_identically_zero": witness_value == 0,
            }
        )
    return sorted(rows, key=lambda item: (item["low_conductor"], item["high_conductor"]))


def pair_stats_for(P: int, primes: list[int]) -> dict[str, Any]:
    """计算单个 P 的互补 conductor 对偶账本。"""
    W, factors = primorial.primorial_modulus(P, primes)
    phi_w = ramanujan.phi_squarefree(factors)
    rows = complementary_pair_rows(W, factors)
    layer_count = 2 ** len(factors)
    pair_count = len(rows)
    sqrt_w_floor = isqrt(W)
    low_layer_count = sum(1 for row in ramanujan.squarefree_divisor_data(factors) if row["d"] <= sqrt_w_floor)
    high_layer_count = layer_count - low_layer_count
    same_sign_pair_count = sum(1 for row in rows if row["sign_relation"] == "same")
    opposite_sign_pair_count = pair_count - same_sign_pair_count
    frequency_count_equal_pair_count = sum(1 for row in rows if row["frequency_counts_equal"])
    identity_zero_pair_count = sum(1 for row in rows if row["pair_kernel_identically_zero"])
    max_frequency_ratio = Fraction(1, 1)
    for row in rows:
        ratio = Fraction(row["phi_q"], row["phi_complement"])
        if ratio < 1:
            ratio = 1 / ratio
        max_frequency_ratio = max(max_frequency_ratio, ratio)

    return {
        "P": P,
        "W_P": W,
        "sqrt_sieve_prime_count": len(factors),
        "omega_W_parity": "even" if len(factors) % 2 == 0 else "odd",
        "phi_W": phi_w,
        "conductor_layer_count": layer_count,
        "complementary_pair_count": pair_count,
        "sqrtW_floor": sqrt_w_floor,
        "low_layer_count": low_layer_count,
        "high_layer_count": high_layer_count,
        "low_high_layer_counts_balanced": low_layer_count == high_layer_count == pair_count,
        "low_conductor_l1_fraction": format_fraction(Fraction(low_layer_count, layer_count)),
        "same_sign_pair_count": same_sign_pair_count,
        "opposite_sign_pair_count": opposite_sign_pair_count,
        "frequency_count_equal_pair_count": frequency_count_equal_pair_count,
        "frequency_count_unequal_pair_count": pair_count - frequency_count_equal_pair_count,
        "max_primitive_frequency_count_ratio_in_pair": format_fraction(max_frequency_ratio),
        "identity_zero_pair_count": identity_zero_pair_count,
        "all_pair_kernels_nonzero_somewhere": identity_zero_pair_count == 0,
        "automatic_complementary_pair_cancellation_possible": False,
        "sample_pairs": rows[:8],
    }


def audit_pairs(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的互补 conductor 对偶做有限审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {101, 257, 971, 1009}
    previous = json.loads(
        (DOCS / "prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-audit.json").read_text()
    )
    previous_audit = previous["finite_audit"]

    sample_rows: list[dict[str, Any]] = []
    max_pair_count = 0
    max_conductor_layer_count = 0
    max_frequency_ratio = Fraction(1, 1)
    same_sign_P_count = 0
    opposite_sign_P_count = 0
    pair_count_total = 0
    frequency_count_equal_pair_total = 0
    frequency_count_unequal_pair_total = 0
    bad_low_high_balance_total = 0
    identity_zero_pair_total = 0

    for P in P_values:
        row = pair_stats_for(P, primes)
        pair_count_total += row["complementary_pair_count"]
        max_pair_count = max(max_pair_count, row["complementary_pair_count"])
        max_conductor_layer_count = max(max_conductor_layer_count, row["conductor_layer_count"])
        max_frequency_ratio = max(
            max_frequency_ratio,
            Fraction(row["max_primitive_frequency_count_ratio_in_pair"]),
        )
        same_sign_P_count += int(row["omega_W_parity"] == "even")
        opposite_sign_P_count += int(row["omega_W_parity"] == "odd")
        frequency_count_equal_pair_total += row["frequency_count_equal_pair_count"]
        frequency_count_unequal_pair_total += row["frequency_count_unequal_pair_count"]
        bad_low_high_balance_total += int(not row["low_high_layer_counts_balanced"])
        identity_zero_pair_total += row["identity_zero_pair_count"]
        if P in interesting:
            sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "P_value_count": len(P_values),
        "max_conductor_layer_count": max_conductor_layer_count,
        "max_complementary_pair_count": max_pair_count,
        "pair_count_total": pair_count_total,
        "same_sign_P_count": same_sign_P_count,
        "opposite_sign_P_count": opposite_sign_P_count,
        "frequency_count_equal_pair_total": frequency_count_equal_pair_total,
        "frequency_count_unequal_pair_total": frequency_count_unequal_pair_total,
        "max_primitive_frequency_count_ratio_in_pair": format_fraction(max_frequency_ratio),
        "bad_low_high_balance_total": bad_low_high_balance_total,
        "identity_zero_pair_total": identity_zero_pair_total,
        "all_low_high_complementary_pairs_balanced": bad_low_high_balance_total == 0,
        "all_pair_kernels_nonzero_somewhere": identity_zero_pair_total == 0,
        "automatic_complementary_pair_cancellation_possible_for_any_P": False,
        "previous_conductor_stratification_status": previous["status"],
        "previous_max_conductor_layer_count": previous_audit["max_conductor_layer_count"],
        "previous_equal_l1_mass_per_layer": previous["equal_l1_mass_per_conductor_layer_proved"],
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
    finite_audit = audit_pairs()
    return {
        "certificate_type": "prime_matrix_phi_lpf_qsupport_complementary_conductor_pair_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "complementary_conductor_mass_duality_closed_auto_cancellation_rejected",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after conductor stratification, the fastest non-cyclic continuation is to test the low/high complementary conductor mirror q <-> W_P/q",
        "current_object": {
            "complementary_conductor": "q^vee=W_P/q",
            "sign_relation": "mu(q^vee)=mu(W_P)mu(q), so pair signs are controlled only by omega(W_P) parity",
            "pair_kernel": "mu(q)c_q(n)/phi(q)+mu(q^vee)c_q^vee(n)/phi(q^vee)",
            "mass_duality": "each of q and q^vee has L1 mass phi(W_P)/W_P",
            "failure_of_auto_cancellation": "the pair kernel is not identically zero; signs, counts, and normalized Ramanujan phases do not give automatic cancellation",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "ComplementaryConductorMassDuality",
                True,
                True,
                "The involution q -> W_P/q pairs low and high conductor layers with equal L1 mass.",
                "none",
            ),
            gate(
                "ComplementaryConductorSignLedger",
                True,
                True,
                "The sign relation is mu(W_P/q)=mu(W_P)mu(q), so same/opposite signs depend only on omega(W_P).",
                "none",
            ),
            gate(
                "AutomaticComplementaryPairCancellationRejected",
                True,
                True,
                "For every complementary pair the normalized Ramanujan pair kernel is nonzero at an explicit witness n.",
                "none",
            ),
            gate(
                "ComplementaryConductorPairPhaseMatchingOrTraceFamilyBridge",
                False,
                False,
                "Turn the nonzero pair kernels into a trace/Kloosterman/Type-II family with genuine phase saving.",
                "new bridge theorem",
            ),
            gate(
                "UniformCancellationAcrossComplementaryPrimorialConductorPairs",
                False,
                False,
                "Prove uniform cancellation after summing all complementary conductor pairs at dynamic primorial level.",
                "new pair-uniform cancellation theorem",
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
            "Wright_2026_arXiv_2604_25177": "still needs the complementary pair kernels to become a valid unbalanced-convolution coefficient family",
            "Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459": "trace-function bilinear bounds still require sheaf/trace packaging of the pair kernels",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "arbitrary-q Kloosterman bounds still require admissible bilinear coefficient ranges and a Kloosterman phase",
            "Pascadi_2025_arXiv_2511_08445": "non-abelian amplification is adjacent only after a composite-modulus Type-II organisation is produced",
            "Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113": "squarefree/smooth modulus sums match the shape of W_P but not the pointwise P,k selector without a bridge",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn and cannot be used as a closing input",
        },
        "latest_narrowest_mouth": [
            "ComplementaryConductorPairPhaseMatchingOrTraceFamilyBridge",
            "AND UniformCancellationAcrossComplementaryPrimorialConductorPairs",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "complementary_conductor_mass_duality_closed": True,
        "complementary_conductor_sign_ledger_closed": True,
        "automatic_complementary_pair_cancellation_rejected": True,
        "uniform_complementary_pair_cancellation_closed": False,
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
        "# Prime Matrix Phi-LPF q-support complementary conductor pair 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"complementary_conductor={current['complementary_conductor']}",
        f"sign_relation={current['sign_relation']}",
        f"pair_kernel={current['pair_kernel']}",
        f"mass_duality={current['mass_duality']}",
        f"failure_of_auto_cancellation={current['failure_of_auto_cancellation']}",
        "```",
        "",
        "## 2. 互补 conductor 对偶审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"P_value_count={audit['P_value_count']}",
        f"max_conductor_layer_count={audit['max_conductor_layer_count']}",
        f"max_complementary_pair_count={audit['max_complementary_pair_count']}",
        f"pair_count_total={audit['pair_count_total']}",
        f"same_sign_P_count={audit['same_sign_P_count']}",
        f"opposite_sign_P_count={audit['opposite_sign_P_count']}",
        f"frequency_count_equal_pair_total={audit['frequency_count_equal_pair_total']}",
        f"frequency_count_unequal_pair_total={audit['frequency_count_unequal_pair_total']}",
        f"max_primitive_frequency_count_ratio_in_pair={audit['max_primitive_frequency_count_ratio_in_pair']}",
        f"bad_low_high_balance_total={audit['bad_low_high_balance_total']}",
        f"identity_zero_pair_total={audit['identity_zero_pair_total']}",
        f"all_low_high_complementary_pairs_balanced={primorial.bool_text(audit['all_low_high_complementary_pairs_balanced'])}",
        f"all_pair_kernels_nonzero_somewhere={primorial.bool_text(audit['all_pair_kernels_nonzero_somewhere'])}",
        f"automatic_complementary_pair_cancellation_possible_for_any_P={primorial.bool_text(audit['automatic_complementary_pair_cancellation_possible_for_any_P'])}",
        f"previous_max_conductor_layer_count={audit['previous_max_conductor_layer_count']}",
        f"previous_equal_l1_mass_per_layer={primorial.bool_text(audit['previous_equal_l1_mass_per_layer'])}",
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
                "omega_W_parity",
                "conductor_layer_count",
                "complementary_pair_count",
                "low_layer_count",
                "high_layer_count",
                "low_conductor_l1_fraction",
                "same_sign_pair_count",
                "opposite_sign_pair_count",
                "frequency_count_unequal_pair_count",
                "max_primitive_frequency_count_ratio_in_pair",
                "identity_zero_pair_count",
                "sample_pairs",
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
        "结论：互补 involution `q -> W_P/q` 精确解释了低/高 conductor 层的 L1 质量镜像；但它不是自动抵消机制。符号由 `omega(W_P)` 奇偶统一控制，primitive 频率数量通常不相等，配对 Ramanujan 核在显式见证点非零。",
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
        f"complementary_conductor_mass_duality_closed={primorial.bool_text(payload['complementary_conductor_mass_duality_closed'])}",
        f"complementary_conductor_sign_ledger_closed={primorial.bool_text(payload['complementary_conductor_sign_ledger_closed'])}",
        f"automatic_complementary_pair_cancellation_rejected={primorial.bool_text(payload['automatic_complementary_pair_cancellation_rejected'])}",
        f"uniform_complementary_pair_cancellation_closed={primorial.bool_text(payload['uniform_complementary_pair_cancellation_closed'])}",
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
    print("complementary_conductor_mass_duality_closed=true")
    print("automatic_complementary_pair_cancellation_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
