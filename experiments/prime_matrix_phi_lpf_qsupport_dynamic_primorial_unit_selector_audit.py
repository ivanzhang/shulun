#!/usr/bin/env python3
"""审计 q-support 动态 sqrt-sieve selector 的 primorial CRT 单位类正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-audit.json

上一层把 prime-q selector 写成动态 sqrt(P) 小素数排除：

  Q_odd mod ell != 0 for every prime ell<=sqrt(P-1).

本层把这些同时排除合并成一个动态 primorial CRT 单位类条件。令

  W_P = product_{ell prime, ell<=sqrt(P-1)} ell.

则 selector 等价于

  Q_odd exists and gcd(Q_odd, W_P)=1.

这是真推进：它把逐小素数筛改写为一个 CRT 单位类/有限 Mobius 乘积正规形。
但 W_P 随 P 增长，仍是动态素性选择器，不是 completed Kloosterman family。
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-dynamic-sqrt-sieve-selector-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-floor-prime-lpf-selector-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def prime_sieve(n: int) -> list[int]:
    """生成不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def lpf(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return p
    return n


def q_window(P: int, k: int, q: int) -> tuple[int, int]:
    """返回 prime-q 侧 clipped cofactor 窗口。"""
    low = max(q, (k * P) // q + 1)
    high = min(2 * P - 1, (((k + 1) * P) - 1) // q)
    return low, high


def reverse_q_window(P: int, k: int, m: int) -> tuple[int, int]:
    """固定 m 后返回 q 的 clipped reverse product-window。"""
    low = max(P // 2 + 1, (k * P) // m + 1)
    # 中文注释：原 cofactor 窗口含 m>=q，所以反向窗口保留 q<=m。
    high = min(P - 1, m, (((k + 1) * P) - 1) // m)
    return low, high


def unique_odd_candidate(low: int, high: int) -> tuple[int | None, int]:
    """返回整数窗口中的唯一奇候选和奇数个数。"""
    if low > high:
        return None, 0
    q_odd = low if low % 2 else low + 1
    if q_odd > high:
        return None, 0
    count = ((high - q_odd) // 2) + 1
    return (q_odd if count == 1 else None), count


def residual_record(m: int, primes: list[int]) -> dict[str, int] | None:
    """若 m 是 residual rough composite，则返回 LPF 桶记录。"""
    r = lpf(m, primes)
    if r < 7 or r == m:
        return None
    beta = m // r
    if beta < r or lpf(beta, primes) < r:
        return None
    return {"m": m, "r": r, "beta": beta}


def residual_records_for_P(P: int, primes: list[int]) -> list[dict[str, int]]:
    """预先列出 P 尺度的 residual rough cofactors。"""
    records: list[dict[str, int]] = []
    for m in range(P // 2 + 1, 2 * P):
        if m % 2 == 0:
            continue
        record = residual_record(m, primes)
        if record is not None:
            records.append(record)
    return records


def sqrt_sieve_primes(P: int, primes: list[int]) -> list[int]:
    """返回动态 sqrt-sieve 所需的小素数。"""
    limit = int((P - 1) ** 0.5)
    return [ell for ell in primes if ell <= limit]


def primorial_modulus(P: int, primes: list[int]) -> tuple[int, list[int]]:
    """返回 W_P 及其素因子列表。"""
    factors = sqrt_sieve_primes(P, primes)
    W = 1
    for ell in factors:
        W *= ell
    return W, factors


def least_unit_obstruction(n: int, factors: list[int]) -> int:
    """返回使 n 不是 W_P 单位的最小素数；没有则返回 0。"""
    for ell in factors:
        if n % ell == 0:
            return ell
    return 0


def actual_terms_for_row(P: int, k: int, primes: list[int]) -> set[tuple[int, int, int, int]]:
    """从 prime-q 方向直接得到实际支撑项。"""
    terms: set[tuple[int, int, int, int]] = set()
    for q in (p for p in primes if P // 2 < p < P):
        low, high = q_window(P, k, q)
        omega, odd_count = unique_odd_candidate(low, high)
        if odd_count > 1 or omega is None:
            continue
        record = residual_record(omega, primes)
        if record is not None:
            terms.add((q, omega, record["r"], record["beta"]))
    return terms


def unit_selector_atom(P: int, k: int, m: int, W: int, factors: list[int]) -> dict[str, Any]:
    """固定 m 后返回动态 primorial 单位类选择器原子。"""
    low, high = reverse_q_window(P, k, m)
    window_size = max(0, high - low + 1)
    q_odd, odd_count = unique_odd_candidate(low, high)
    gcd_value = math.gcd(q_odd, W) if q_odd is not None else 0
    obstruction = least_unit_obstruction(q_odd, factors) if q_odd is not None else 0
    selected = q_odd if q_odd is not None and gcd_value == 1 else None

    if window_size == 0:
        selector_case = "empty_window"
    elif q_odd is None:
        selector_case = "even_singleton_rejected"
    elif selected is not None:
        selector_case = "primorial_unit_selected"
    else:
        selector_case = f"primorial_nonunit_rejected_by_{obstruction}"

    return {
        "low": low,
        "high": high,
        "window_size": window_size,
        "q_odd": q_odd,
        "odd_count": odd_count,
        "gcd_qodd_W": gcd_value,
        "least_unit_obstruction": obstruction,
        "selected_q": selected,
        "selector_case": selector_case,
        "bad_window_size": int(window_size > 2),
        "bad_odd_count": int(odd_count > 1),
        "bad_gcd_obstruction_mismatch": int((gcd_value > 1) != (obstruction > 0)),
    }


def unit_terms_for_row(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    prime_set: set[int],
) -> tuple[set[tuple[int, int, int, int]], dict[str, Any]]:
    """从动态 primorial unit selector 方向得到支撑项。"""
    terms: set[tuple[int, int, int, int]] = set()
    W, factors = primorial_modulus(P, primes)
    selector_cases: Counter[str] = Counter()
    nonunit_obstruction_counter: Counter[int] = Counter()
    max_window_size = 0
    max_odd_count = 0
    totals: Counter[str] = Counter()
    sample_selectors: list[str] = []

    for record in records:
        atom = unit_selector_atom(P, k, record["m"], W, factors)
        selector_cases[atom["selector_case"]] += 1
        max_window_size = max(max_window_size, atom["window_size"])
        max_odd_count = max(max_odd_count, atom["odd_count"])
        totals["bad_window_size"] += atom["bad_window_size"]
        totals["bad_odd_count"] += atom["bad_odd_count"]
        totals["bad_gcd_obstruction_mismatch"] += atom["bad_gcd_obstruction_mismatch"]
        totals["windows_with_odd_candidate"] += int(atom["q_odd"] is not None)
        if atom["least_unit_obstruction"]:
            nonunit_obstruction_counter[atom["least_unit_obstruction"]] += 1

        selected = atom["selected_q"]
        if selected is not None:
            terms.add((selected, record["m"], record["r"], record["beta"]))
            totals["primorial_unit_selected"] += 1
            totals["bad_unit_survivor_not_prime"] += int(selected not in prime_set)
            if len(sample_selectors) < 5:
                sample_selectors.append(
                    "m={m},r={r},beta={beta},L={low},U={high},Q_odd={q},QmodW={res}".format(
                        m=record["m"],
                        r=record["r"],
                        beta=record["beta"],
                        low=atom["low"],
                        high=atom["high"],
                        q=selected,
                        res=selected % W,
                    )
                )

    return terms, {
        "dynamic_primorial_modulus": W,
        "dynamic_primorial_prime_count": len(factors),
        "formal_mobius_terms_per_candidate": 2 ** len(factors),
        "selector_cases": dict(sorted(selector_cases.items())),
        "nonunit_obstruction_totals": dict(sorted(nonunit_obstruction_counter.items())),
        "max_reverse_window_size": max_window_size,
        "max_odd_count": max_odd_count,
        "bad_window_size": totals["bad_window_size"],
        "bad_odd_count": totals["bad_odd_count"],
        "bad_gcd_obstruction_mismatch": totals["bad_gcd_obstruction_mismatch"],
        "bad_unit_survivor_not_prime": totals["bad_unit_survivor_not_prime"],
        "windows_with_odd_candidate": totals["windows_with_odd_candidate"],
        "primorial_unit_selected": totals["primorial_unit_selected"],
        "sample_selectors": "; ".join(sample_selectors) if sample_selectors else "empty",
    }


def row_audit(P: int, k: int, primes: list[int], prime_set: set[int], records: list[dict[str, int]]) -> dict[str, Any]:
    """审计单行 actual graph 与动态 primorial unit selector graph 是否一致。"""
    actual = actual_terms_for_row(P, k, primes)
    unit_terms, selector_stats = unit_terms_for_row(P, k, records, primes, prime_set)
    missing = actual - unit_terms
    extra = unit_terms - actual
    return {
        "P": P,
        "k": k,
        "actual_support_terms": len(actual),
        "primorial_unit_selector_terms": len(unit_terms),
        "missing_actual_terms": len(missing),
        "extra_primorial_unit_selector_terms": len(extra),
        "dynamic_primorial_modulus": selector_stats["dynamic_primorial_modulus"],
        "dynamic_primorial_prime_count": selector_stats["dynamic_primorial_prime_count"],
        "formal_mobius_terms_per_candidate": selector_stats["formal_mobius_terms_per_candidate"],
        "max_reverse_window_size": selector_stats["max_reverse_window_size"],
        "max_odd_count": selector_stats["max_odd_count"],
        "bad_window_size": selector_stats["bad_window_size"],
        "bad_odd_count": selector_stats["bad_odd_count"],
        "bad_gcd_obstruction_mismatch": selector_stats["bad_gcd_obstruction_mismatch"],
        "bad_unit_survivor_not_prime": selector_stats["bad_unit_survivor_not_prime"],
        "windows_with_odd_candidate": selector_stats["windows_with_odd_candidate"],
        "primorial_unit_selected": selector_stats["primorial_unit_selected"],
        "selector_cases": selector_stats["selector_cases"],
        "nonunit_obstruction_totals": selector_stats["nonunit_obstruction_totals"],
        "sample_selectors": selector_stats["sample_selectors"],
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    prime_set = set(primes)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}
    records_by_P = {P: residual_records_for_P(P, primes) for P in P_values}

    totals: Counter[str] = Counter()
    selector_cases: Counter[str] = Counter()
    nonunit_obstruction_counter: Counter[int] = Counter()
    row_count = 0
    active_rows = 0
    max_reverse_window_size = 0
    max_odd_count = 0
    max_primorial_modulus = 1
    max_primorial_prime_count = 0
    max_formal_mobius_terms = 0
    sample_rows: list[dict[str, Any]] = []

    for P in P_values:
        records = records_by_P[P]
        for k in range(1, P):
            row_count += 1
            row = row_audit(P, k, primes, prime_set, records)
            active_rows += int(row["actual_support_terms"] > 0)
            totals["actual_support_terms"] += row["actual_support_terms"]
            totals["primorial_unit_selector_terms"] += row["primorial_unit_selector_terms"]
            totals["missing_actual_terms"] += row["missing_actual_terms"]
            totals["extra_primorial_unit_selector_terms"] += row["extra_primorial_unit_selector_terms"]
            totals["bad_window_size"] += row["bad_window_size"]
            totals["bad_odd_count"] += row["bad_odd_count"]
            totals["bad_gcd_obstruction_mismatch"] += row["bad_gcd_obstruction_mismatch"]
            totals["bad_unit_survivor_not_prime"] += row["bad_unit_survivor_not_prime"]
            totals["windows_with_odd_candidate"] += row["windows_with_odd_candidate"]
            totals["primorial_unit_selected"] += row["primorial_unit_selected"]
            max_reverse_window_size = max(max_reverse_window_size, row["max_reverse_window_size"])
            max_odd_count = max(max_odd_count, row["max_odd_count"])
            max_primorial_modulus = max(max_primorial_modulus, row["dynamic_primorial_modulus"])
            max_primorial_prime_count = max(max_primorial_prime_count, row["dynamic_primorial_prime_count"])
            max_formal_mobius_terms = max(max_formal_mobius_terms, row["formal_mobius_terms_per_candidate"])
            selector_cases.update(row["selector_cases"])
            nonunit_obstruction_counter.update(row["nonunit_obstruction_totals"])
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_actual_support_terms": totals["actual_support_terms"],
        "total_primorial_unit_selector_terms": totals["primorial_unit_selector_terms"],
        "actual_equals_primorial_unit_selector_terms": totals["actual_support_terms"]
        == totals["primorial_unit_selector_terms"]
        and totals["missing_actual_terms"] == 0
        and totals["extra_primorial_unit_selector_terms"] == 0,
        "missing_actual_terms_total": totals["missing_actual_terms"],
        "extra_primorial_unit_selector_terms_total": totals["extra_primorial_unit_selector_terms"],
        "max_reverse_window_size": max_reverse_window_size,
        "max_odd_count_per_reverse_window": max_odd_count,
        "max_dynamic_primorial_modulus": max_primorial_modulus,
        "max_dynamic_primorial_prime_count": max_primorial_prime_count,
        "max_formal_mobius_terms_per_candidate": max_formal_mobius_terms,
        "windows_with_odd_candidate_total": totals["windows_with_odd_candidate"],
        "primorial_unit_selected_total": totals["primorial_unit_selected"],
        "bad_reverse_window_size_total": totals["bad_window_size"],
        "bad_odd_count_total": totals["bad_odd_count"],
        "bad_gcd_obstruction_mismatch_total": totals["bad_gcd_obstruction_mismatch"],
        "bad_unit_survivor_not_prime_total": totals["bad_unit_survivor_not_prime"],
        "selector_case_totals": dict(sorted(selector_cases.items())),
        "nonunit_obstruction_totals": dict(sorted(nonunit_obstruction_counter.items())),
        "finite_evidence_not_used_as_global_proof": True,
        "sample_rows": sample_rows,
    }


def table(rows: list[dict[str, Any]], fields: list[str]) -> str:
    """生成 Markdown 表格。"""
    header = "| " + " | ".join(fields) + " |"
    sep = "| " + " | ".join("---" for _ in fields) + " |"
    body = []
    for row in rows:
        cells = []
        for field in fields:
            value = row.get(field, "")
            if isinstance(value, bool):
                value = bool_text(value)
            elif isinstance(value, dict):
                value = ", ".join(f"{k}:{value[k]}" for k in sorted(value, key=str))
            elif isinstance(value, list):
                value = " / ".join(str(item) for item in value)
            cells.append(str(value).replace("|", r"\|"))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *body])


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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "dynamic_primorial_unit_selector_normal_form_closed_completion_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after dynamic sqrt-sieve atomization, the fastest non-cyclic continuation is the dynamic primorial CRT unit-class normal form",
        "current_object": {
            "fixed_cofactor": "m=r*beta, with r>=7 prime and beta r-rough",
            "reverse_window": "L=max(P/2+1, floor(kP/m)+1), U=min(P-1, m, floor(((k+1)P-1)/m))",
            "unique_odd_candidate": "Q_odd=L if L is odd, else L+1; valid only when Q_odd<=U",
            "dynamic_primorial": "W_P=product_{ell prime, ell<=sqrt(P-1)} ell",
            "unit_selector": "selected iff Q_odd exists and gcd(Q_odd,W_P)=1",
            "mobius_product": "1_{gcd(Q_odd,W_P)=1}=sum_{d|W_P, d|Q_odd} mu(d)",
            "phase_after_selector": "e(h*kP/Q_odd) on dynamic-primorial unit-class survivors",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "DynamicSqrtSieveEqualsPrimorialUnitClass",
                True,
                True,
                "The simultaneous small-prime exclusions are exactly gcd(Q_odd,W_P)=1.",
                "none",
            ),
            gate(
                "PrimorialMobiusProductIdentity",
                True,
                True,
                "The unit-class indicator equals the finite Mobius sum over squarefree divisors of W_P.",
                "none",
            ),
            gate(
                "ActualQSupportEqualsDynamicPrimorialUnitSelectorGraph",
                True,
                True,
                "The actual support graph equals the graph generated by the dynamic primorial unit selector.",
                "none",
            ),
            gate(
                "StaticModulusCompletionShortcutRejected",
                True,
                True,
                "The modulus W_P grows with P; freezing it would leave rough composite survivors and change the object.",
                "none",
            ),
            gate(
                "DynamicPrimorialUnitSelectorToCompletedKloostermanConvolutionBridge",
                False,
                False,
                "Convert the dynamic unit-class selector over rough cofactors into a same-object completed Kloosterman family.",
                "new bridge theorem",
            ),
            gate(
                "RoughBetaSiegelWalfiszUniformityOrReplacement",
                False,
                False,
                "Supply the equidistribution/SW factor or an object-specific replacement for the rough beta weights.",
                "rough beta uniformity input",
            ),
        ],
        "external_theorem_implication": {
            "Wright_2026_arXiv_2604_25177": "trilinear Kloosterman fractions still require completed/unbalanced convolution; dynamic W_P unit classes are not supplied coefficients",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "bilinear Kloosterman power savings still require bilinear coefficient families, not a growing primorial unit selector",
            "Pascadi_2025_arXiv_2511_08445": "non-abelian amplification still needs Type-II Kloosterman organisation over moduli, not a pointwise dynamic CRT unit test",
            "Dong_Robles_Zeindler_2026_arXiv_2601_00292": "withdrawn; not usable as an external input",
        },
        "latest_narrowest_mouth": [
            "DynamicPrimorialUnitSelectorToCompletedKloostermanConvolutionBridge",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "dynamic_primorial_unit_selector_closed": True,
        "dynamic_sqrt_sieve_equals_primorial_unit_class": True,
        "primorial_mobius_product_identity_closed": True,
        "actual_equals_dynamic_primorial_unit_selector_graph": finite_audit[
            "actual_equals_primorial_unit_selector_terms"
        ],
        "static_modulus_completion_shortcut_valid": False,
        "dynamic_primorial_completion_bridge_closed": False,
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
        "# Prime Matrix Phi-LPF q-support dynamic primorial unit selector 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"fixed_cofactor={current['fixed_cofactor']}",
        f"reverse_window={current['reverse_window']}",
        f"unique_odd_candidate={current['unique_odd_candidate']}",
        f"dynamic_primorial={current['dynamic_primorial']}",
        f"unit_selector={current['unit_selector']}",
        f"mobius_product={current['mobius_product']}",
        f"phase_after_selector={current['phase_after_selector']}",
        "```",
        "",
        "## 2. 有限动态 primorial unit 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_actual_support_terms={audit['total_actual_support_terms']}",
        f"total_primorial_unit_selector_terms={audit['total_primorial_unit_selector_terms']}",
        f"actual_equals_primorial_unit_selector_terms={bool_text(audit['actual_equals_primorial_unit_selector_terms'])}",
        f"missing_actual_terms_total={audit['missing_actual_terms_total']}",
        f"extra_primorial_unit_selector_terms_total={audit['extra_primorial_unit_selector_terms_total']}",
        f"max_reverse_window_size={audit['max_reverse_window_size']}",
        f"max_odd_count_per_reverse_window={audit['max_odd_count_per_reverse_window']}",
        f"max_dynamic_primorial_modulus={audit['max_dynamic_primorial_modulus']}",
        f"max_dynamic_primorial_prime_count={audit['max_dynamic_primorial_prime_count']}",
        f"max_formal_mobius_terms_per_candidate={audit['max_formal_mobius_terms_per_candidate']}",
        f"windows_with_odd_candidate_total={audit['windows_with_odd_candidate_total']}",
        f"primorial_unit_selected_total={audit['primorial_unit_selected_total']}",
        f"bad_gcd_obstruction_mismatch_total={audit['bad_gcd_obstruction_mismatch_total']}",
        f"bad_unit_survivor_not_prime_total={audit['bad_unit_survivor_not_prime_total']}",
        f"selector_case_totals={audit['selector_case_totals']}",
        f"nonunit_obstruction_totals={audit['nonunit_obstruction_totals']}",
        "```",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "actual_support_terms",
                "primorial_unit_selector_terms",
                "missing_actual_terms",
                "extra_primorial_unit_selector_terms",
                "dynamic_primorial_modulus",
                "dynamic_primorial_prime_count",
                "formal_mobius_terms_per_candidate",
                "selector_cases",
                "sample_selectors",
            ],
        ),
        "",
        "## 3. 门控表",
        "",
        table(payload["closed_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 4. 外部 theorem 影响",
        "",
        "```text",
        *[f"{key}={value}" for key, value in payload["external_theorem_implication"].items()],
        "```",
        "",
        "结论：本层把动态 sqrt(P) 小素数筛合并为一个动态 primorial CRT 单位类和有限 Mobius 乘积；但它仍是随 P 增长的逐点 selector，不是 completed Kloosterman family。",
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
        f"dynamic_primorial_unit_selector_closed={bool_text(payload['dynamic_primorial_unit_selector_closed'])}",
        f"dynamic_sqrt_sieve_equals_primorial_unit_class={bool_text(payload['dynamic_sqrt_sieve_equals_primorial_unit_class'])}",
        f"primorial_mobius_product_identity_closed={bool_text(payload['primorial_mobius_product_identity_closed'])}",
        f"actual_equals_dynamic_primorial_unit_selector_graph={bool_text(payload['actual_equals_dynamic_primorial_unit_selector_graph'])}",
        f"static_modulus_completion_shortcut_valid={bool_text(payload['static_modulus_completion_shortcut_valid'])}",
        f"dynamic_primorial_completion_bridge_closed={bool_text(payload['dynamic_primorial_completion_bridge_closed'])}",
        f"rough_beta_siegel_walfisz_factor_extracted={bool_text(payload['rough_beta_siegel_walfisz_factor_extracted'])}",
        f"pointwise_pk_transfer_closed={bool_text(payload['pointwise_pk_transfer_closed'])}",
        f"q_support_phase_saving_closed={bool_text(payload['q_support_phase_saving_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
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
    print("dynamic_primorial_unit_selector_closed=true")
    print("dynamic_primorial_completion_bridge_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
