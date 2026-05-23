#!/usr/bin/env python3
"""审计 q-support 动态 primorial 单位类的 Ramanujan 展开正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.json

上一层已经得到动态 primorial 单位类：

  W_P = product_{ell prime, ell<=sqrt(P-1)} ell,
  selected iff Q_odd exists and gcd(Q_odd, W_P)=1.

本层继续把单位类指示函数写成 Ramanujan 加性字符正规形：

  1_{(n,W)=1} = phi(W)/W * sum_{d|W} mu(d)c_d(n)/phi(d),

其中 c_d(n) 是 Ramanujan sum。对平方自由 W，这还等于每个 ell|W 的
局部乘积。本层关闭的是 exact CRT/Ramanujan 展开；它不关闭 analytic
completion，因为完全打开后有 sum_{d|W}phi(d)=W 个动态加性模式。
"""

from __future__ import annotations

import hashlib
import json
import math
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


SLUG = "prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-sqrt-sieve-selector-audit.json",
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


def phi_squarefree(factors: list[int]) -> int:
    """计算平方自由数的 Euler phi。"""
    value = 1
    for ell in factors:
        value *= ell - 1
    return value


def squarefree_divisor_data(factors: list[int]) -> list[dict[str, Any]]:
    """列出 d|W 的 d、mu(d)、phi(d) 与素因子。"""
    rows: list[dict[str, Any]] = [{"d": 1, "mu": 1, "phi": 1, "factors": []}]
    for ell in factors:
        new_rows = []
        for row in rows:
            new_rows.append(
                {
                    "d": row["d"] * ell,
                    "mu": -row["mu"],
                    "phi": row["phi"] * (ell - 1),
                    "factors": [*row["factors"], ell],
                }
            )
        rows.extend(new_rows)
    return sorted(rows, key=lambda item: item["d"])


def ramanujan_sum_squarefree(n: int, factors: list[int]) -> int:
    """计算平方自由 d 的 Ramanujan sum c_d(n)。"""
    value = 1
    for ell in factors:
        value *= ell - 1 if n % ell == 0 else -1
    return value


def ramanujan_divisor_identity_value(n: int, W: int, factors: list[int]) -> Fraction:
    """用 d|W 的 Ramanujan 展开计算单位类指示函数。"""
    phi_w = phi_squarefree(factors)
    total = Fraction(0, 1)
    for row in squarefree_divisor_data(factors):
        c_d = ramanujan_sum_squarefree(n, row["factors"])
        total += Fraction(row["mu"] * c_d, row["phi"])
    return Fraction(phi_w, W) * total


def ramanujan_local_product_value(n: int, factors: list[int]) -> Fraction:
    """用局部乘积计算 Ramanujan 单位类指示函数。"""
    value = Fraction(1, 1)
    for ell in factors:
        c_ell = ell - 1 if n % ell == 0 else -1
        value *= Fraction(ell - 1, ell) * (1 - Fraction(c_ell, ell - 1))
        if value == 0:
            break
    return value


def format_fraction(value: Fraction) -> str:
    """输出分数。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def mode_stats_for(P: int, primes: list[int]) -> dict[str, Any]:
    """计算动态 Ramanujan 展开的模式账本。"""
    W, factors = primorial.primorial_modulus(P, primes)
    phi_w = phi_squarefree(factors)
    full_l1 = Fraction(phi_w * (2 ** len(factors)), W)
    return {
        "P": P,
        "W": W,
        "prime_count": len(factors),
        "phi_W": phi_w,
        "ramanujan_divisor_terms": 2 ** len(factors),
        "full_additive_character_modes": W,
        "full_additive_mode_l1": format_fraction(full_l1),
        "full_additive_mode_l1_float": float(full_l1),
    }


def row_audit(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    mode_stats: dict[str, Any],
    collect_divisor_samples: bool,
) -> dict[str, Any]:
    """审计一行中的 Ramanujan 单位类身份。"""
    W = mode_stats["W"]
    factors = primorial.sqrt_sieve_primes(P, primes)
    totals: Counter[str] = Counter()
    selector_cases: Counter[str] = Counter()
    samples: list[dict[str, Any]] = []

    for record in records:
        atom = primorial.unit_selector_atom(P, k, record["m"], W, factors)
        selector_cases[atom["selector_case"]] += 1
        q_odd = atom["q_odd"]
        if q_odd is None:
            continue

        expected = Fraction(1 if atom["gcd_qodd_W"] == 1 else 0, 1)
        local_value = ramanujan_local_product_value(q_odd, factors)
        totals["ramanujan_product_identity_checked"] += 1
        totals["ramanujan_product_identity_mismatch"] += int(local_value != expected)
        totals["unit_selected"] += int(expected == 1)
        totals["unit_rejected"] += int(expected == 0)

        if collect_divisor_samples:
            divisor_value = ramanujan_divisor_identity_value(q_odd, W, factors)
            totals["ramanujan_divisor_sum_sample_checked"] += 1
            totals["ramanujan_divisor_sum_sample_mismatch"] += int(divisor_value != expected)
            if len(samples) < 5:
                samples.append(
                    {
                        "m": record["m"],
                        "r": record["r"],
                        "beta": record["beta"],
                        "Q_odd": q_odd,
                        "gcd_Q_W": atom["gcd_qodd_W"],
                        "expected_unit": int(expected),
                        "local_product": format_fraction(local_value),
                        "divisor_sum": format_fraction(divisor_value),
                    }
                )

    return {
        "P": P,
        "k": k,
        "ramanujan_product_identity_checked": totals["ramanujan_product_identity_checked"],
        "ramanujan_product_identity_mismatch": totals["ramanujan_product_identity_mismatch"],
        "ramanujan_divisor_sum_sample_checked": totals["ramanujan_divisor_sum_sample_checked"],
        "ramanujan_divisor_sum_sample_mismatch": totals["ramanujan_divisor_sum_sample_mismatch"],
        "unit_selected": totals["unit_selected"],
        "unit_rejected": totals["unit_rejected"],
        "dynamic_primorial_modulus": W,
        "dynamic_primorial_prime_count": mode_stats["prime_count"],
        "ramanujan_divisor_terms": mode_stats["ramanujan_divisor_terms"],
        "full_additive_character_modes": mode_stats["full_additive_character_modes"],
        "full_additive_mode_l1": mode_stats["full_additive_mode_l1"],
        "selector_cases": dict(sorted(selector_cases.items())),
        "sample_ramanujan_atoms": samples,
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做 Ramanujan 身份审计。"""
    primes = primorial.prime_sieve(2 * max_prime + 10)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}
    records_by_P = {P: primorial.residual_records_for_P(P, primes) for P in P_values}
    mode_by_P = {P: mode_stats_for(P, primes) for P in P_values}

    totals: Counter[str] = Counter()
    selector_cases: Counter[str] = Counter()
    row_count = 0
    active_identity_rows = 0
    sample_rows: list[dict[str, Any]] = []
    max_mode_stats = {
        "max_dynamic_primorial_modulus": 1,
        "max_dynamic_primorial_prime_count": 0,
        "max_ramanujan_divisor_terms_per_candidate": 0,
        "max_full_additive_character_modes_per_candidate": 1,
        "max_full_additive_mode_l1_float": 0.0,
        "max_full_additive_mode_l1": "0",
    }

    for P in P_values:
        mode_stats = mode_by_P[P]
        if mode_stats["W"] > max_mode_stats["max_dynamic_primorial_modulus"]:
            max_mode_stats["max_dynamic_primorial_modulus"] = mode_stats["W"]
        max_mode_stats["max_dynamic_primorial_prime_count"] = max(
            max_mode_stats["max_dynamic_primorial_prime_count"], mode_stats["prime_count"]
        )
        max_mode_stats["max_ramanujan_divisor_terms_per_candidate"] = max(
            max_mode_stats["max_ramanujan_divisor_terms_per_candidate"], mode_stats["ramanujan_divisor_terms"]
        )
        max_mode_stats["max_full_additive_character_modes_per_candidate"] = max(
            max_mode_stats["max_full_additive_character_modes_per_candidate"],
            mode_stats["full_additive_character_modes"],
        )
        if mode_stats["full_additive_mode_l1_float"] > max_mode_stats["max_full_additive_mode_l1_float"]:
            max_mode_stats["max_full_additive_mode_l1_float"] = mode_stats["full_additive_mode_l1_float"]
            max_mode_stats["max_full_additive_mode_l1"] = mode_stats["full_additive_mode_l1"]

        records = records_by_P[P]
        for k in range(1, P):
            row_count += 1
            row = row_audit(P, k, records, primes, mode_stats, (P, k) in interesting)
            active_identity_rows += int(row["ramanujan_product_identity_checked"] > 0)
            for key in (
                "ramanujan_product_identity_checked",
                "ramanujan_product_identity_mismatch",
                "ramanujan_divisor_sum_sample_checked",
                "ramanujan_divisor_sum_sample_mismatch",
                "unit_selected",
                "unit_rejected",
            ):
                totals[key] += row[key]
            selector_cases.update(row["selector_cases"])
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_ramanujan_identity_row_count": active_identity_rows,
        "ramanujan_product_identity_checked_total": totals["ramanujan_product_identity_checked"],
        "ramanujan_product_identity_mismatch_total": totals["ramanujan_product_identity_mismatch"],
        "ramanujan_divisor_sum_sample_checked_total": totals["ramanujan_divisor_sum_sample_checked"],
        "ramanujan_divisor_sum_sample_mismatch_total": totals["ramanujan_divisor_sum_sample_mismatch"],
        "primorial_unit_selected_total": totals["unit_selected"],
        "primorial_unit_rejected_total": totals["unit_rejected"],
        "selector_case_totals": dict(sorted(selector_cases.items())),
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
        **max_mode_stats,
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "dynamic_ramanujan_unit_expansion_closed_usable_kloosterman_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the fastest non-cyclic continuation after the primorial unit selector is the exact Ramanujan additive-character expansion and its mode ledger",
        "current_object": {
            "dynamic_primorial": "W_P=product_{ell prime, ell<=sqrt(P-1)} ell",
            "unit_selector": "1_{gcd(Q_odd,W_P)=1}",
            "ramanujan_expansion": "1_{(n,W)=1}=phi(W)/W * sum_{d|W} mu(d)c_d(n)/phi(d)",
            "local_factor": "for ell|W, local factor is (ell-1)/ell*(1-c_ell(n)/(ell-1))",
            "full_additive_opening": "c_d(n)=sum_{a mod d, (a,d)=1} e(a*n/d), so total modes sum_{d|W}phi(d)=W",
            "phase_after_expansion": "e(h*kP/Q_odd) multiplied by dynamic Ramanujan modes e(a*Q_odd/d)",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "PrimorialUnitRamanujanExpansionIdentity",
                True,
                True,
                "The W_P-unit selector has the exact Ramanujan divisor expansion.",
                "none",
            ),
            gate(
                "RamanujanLocalProductFactorization",
                True,
                True,
                "For squarefree W_P the expansion factors into prime-local tests and equals the gcd selector.",
                "none",
            ),
            gate(
                "FullAdditiveOpeningModeCountLedger",
                True,
                True,
                "Opening all Ramanujan sums gives exactly sum_{d|W_P}phi(d)=W_P additive modes.",
                "none",
            ),
            gate(
                "DynamicRamanujanUnitExpansionToUsableKloostermanCompletionBridge",
                False,
                False,
                "Turn the dynamic Ramanujan-mode expansion into a same-object completed Kloosterman or Type-II family.",
                "new bridge theorem",
            ),
            gate(
                "UniformRamanujanModeCancellationOrTruncation",
                False,
                False,
                "Control or truncate the W_P dynamic additive modes without changing the selector.",
                "mode cancellation/truncation theorem",
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
            "Wright_2026_arXiv_2604_25177": "trilinear Kloosterman fractions do not provide the dynamic Ramanujan-mode completion for W_P unit classes",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "bilinear Kloosterman estimates still need admissible bilinear coefficient families after completion",
            "Pascadi_2025_arXiv_2511_08445": "composite-modulus amplification still needs Type-II organisation, not a raw W_P-mode expansion",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn; not usable as an external input",
        },
        "latest_narrowest_mouth": [
            "DynamicRamanujanUnitExpansionToUsableKloostermanCompletionBridge",
            "AND UniformRamanujanModeCancellationOrTruncation",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "dynamic_ramanujan_unit_expansion_closed": True,
        "ramanujan_product_identity_globally_proved": True,
        "ramanujan_product_identity_finitely_audited": finite_audit["ramanujan_product_identity_mismatch_total"] == 0,
        "ramanujan_divisor_sum_sample_audited": finite_audit["ramanujan_divisor_sum_sample_mismatch_total"] == 0,
        "full_additive_mode_count_ledger_closed": True,
        "usable_kloosterman_completion_bridge_closed": False,
        "uniform_ramanujan_mode_cancellation_closed": False,
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
        "# Prime Matrix Phi-LPF q-support dynamic Ramanujan unit expansion 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"dynamic_primorial={current['dynamic_primorial']}",
        f"unit_selector={current['unit_selector']}",
        f"ramanujan_expansion={current['ramanujan_expansion']}",
        f"local_factor={current['local_factor']}",
        f"full_additive_opening={current['full_additive_opening']}",
        f"phase_after_expansion={current['phase_after_expansion']}",
        "```",
        "",
        "## 2. 有限 Ramanujan 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_ramanujan_identity_row_count={audit['active_ramanujan_identity_row_count']}",
        f"ramanujan_product_identity_checked_total={audit['ramanujan_product_identity_checked_total']}",
        f"ramanujan_product_identity_mismatch_total={audit['ramanujan_product_identity_mismatch_total']}",
        f"ramanujan_divisor_sum_sample_checked_total={audit['ramanujan_divisor_sum_sample_checked_total']}",
        f"ramanujan_divisor_sum_sample_mismatch_total={audit['ramanujan_divisor_sum_sample_mismatch_total']}",
        f"primorial_unit_selected_total={audit['primorial_unit_selected_total']}",
        f"primorial_unit_rejected_total={audit['primorial_unit_rejected_total']}",
        f"max_dynamic_primorial_modulus={audit['max_dynamic_primorial_modulus']}",
        f"max_dynamic_primorial_prime_count={audit['max_dynamic_primorial_prime_count']}",
        f"max_ramanujan_divisor_terms_per_candidate={audit['max_ramanujan_divisor_terms_per_candidate']}",
        f"max_full_additive_character_modes_per_candidate={audit['max_full_additive_character_modes_per_candidate']}",
        f"max_full_additive_mode_l1={audit['max_full_additive_mode_l1']}",
        "```",
        "",
        "代表行：",
        "",
        primorial.table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "ramanujan_product_identity_checked",
                "ramanujan_product_identity_mismatch",
                "ramanujan_divisor_sum_sample_checked",
                "ramanujan_divisor_sum_sample_mismatch",
                "dynamic_primorial_modulus",
                "ramanujan_divisor_terms",
                "full_additive_character_modes",
                "sample_ramanujan_atoms",
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
        "结论：本层把动态 primorial CRT 单位类继续正规化为 Ramanujan 加性字符展开，并精确记录完全打开后的动态模式规模。它没有闭合外部 Kloosterman/Type-II 桥，因为模式数等于 W_P，且 W_P 随 P 增长。",
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
        f"dynamic_ramanujan_unit_expansion_closed={primorial.bool_text(payload['dynamic_ramanujan_unit_expansion_closed'])}",
        f"ramanujan_product_identity_globally_proved={primorial.bool_text(payload['ramanujan_product_identity_globally_proved'])}",
        f"ramanujan_product_identity_finitely_audited={primorial.bool_text(payload['ramanujan_product_identity_finitely_audited'])}",
        f"full_additive_mode_count_ledger_closed={primorial.bool_text(payload['full_additive_mode_count_ledger_closed'])}",
        f"usable_kloosterman_completion_bridge_closed={primorial.bool_text(payload['usable_kloosterman_completion_bridge_closed'])}",
        f"uniform_ramanujan_mode_cancellation_closed={primorial.bool_text(payload['uniform_ramanujan_mode_cancellation_closed'])}",
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
    print("dynamic_ramanujan_unit_expansion_closed=true")
    print("usable_kloosterman_completion_bridge_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
