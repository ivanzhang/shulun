#!/usr/bin/env python3
"""审计 q-support LPF 桶的反向 prime-q 选择器与 completion bridge 剩余门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_reverse_prime_selector_completion_bridge_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge-audit.json

上一层已经把支撑项压成 sparse product-window triples:

  kP < q*r*beta < (k+1)P,
  q prime in (P/2,P), r prime >= 7, beta r-rough.

本层固定粗余因子 m=r*beta。因为 m>P/2，反向 q-window 长度 P/m<2，
所以最多两个连续整数，最多一个奇素数 q。于是实际 q-support 等价于
一个 floor-defined reverse prime selector，而不是 completed dense
Kloosterman convolution。这个正规形继续压窄 completion bridge，但不宣称
Phi-LPF 奇偶障碍已经突破。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge-audit.json",
    DOCS / "prime-matrix-phi-lpf-qsupport-external-theorem-match-audit.json",
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


def unique_odd_candidate(low: int, high: int) -> tuple[int | None, int]:
    """返回整数窗口中的唯一奇候选和奇数个数。"""
    if low > high:
        return None, 0
    odd_low = low if low % 2 else low + 1
    if odd_low > high:
        return None, 0
    count = ((high - odd_low) // 2) + 1
    return (odd_low if count == 1 else None), count


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


def reverse_q_window(P: int, k: int, m: int) -> tuple[int, int]:
    """固定 m 后返回 q 的 clipped reverse product-window。"""
    low = max(P // 2 + 1, (k * P) // m + 1)
    # 中文注释：q_window 中 m>=q，所以反向窗口也要保留 q<=m。
    high = min(P - 1, m, (((k + 1) * P) - 1) // m)
    return low, high


def reverse_prime_selector(P: int, k: int, m: int, prime_set: set[int]) -> dict[str, Any]:
    """固定 m 后选择反向窗口中的唯一奇素数 q。"""
    low, high = reverse_q_window(P, k, m)
    window_size = max(0, high - low + 1)
    odd_candidate, odd_count = unique_odd_candidate(low, high)
    prime_candidates = [q for q in range(low, high + 1) if q in prime_set]
    selected = odd_candidate if odd_candidate in prime_set else None
    if window_size == 0:
        selector_case = "empty"
    elif window_size == 1:
        selector_case = "singleton_prime" if selected is not None else "singleton_nonprime"
    elif selected == low:
        selector_case = "two_point_first_odd_prime"
    elif selected == high:
        selector_case = "two_point_second_odd_prime"
    elif odd_candidate is None:
        selector_case = "two_point_no_odd"
    else:
        selector_case = "two_point_odd_nonprime"
    return {
        "low": low,
        "high": high,
        "window_size": window_size,
        "odd_candidate": odd_candidate,
        "odd_count": odd_count,
        "prime_candidates": prime_candidates,
        "selected_q": selected,
        "selector_case": selector_case,
    }


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


def reverse_terms_for_row(
    P: int,
    k: int,
    records: list[dict[str, int]],
    prime_set: set[int],
) -> tuple[set[tuple[int, int, int, int]], dict[str, Any]]:
    """从 fixed m=r*beta 方向得到反向 prime selector 支撑项。"""
    terms: set[tuple[int, int, int, int]] = set()
    selector_cases: Counter[str] = Counter()
    max_window_size = 0
    max_odd_count = 0
    max_prime_count = 0
    bad_window_size = 0
    bad_prime_multiplicity = 0
    bad_selected_not_odd = 0
    sample_selectors: list[str] = []

    for record in records:
        m = record["m"]
        selector = reverse_prime_selector(P, k, m, prime_set)
        selector_cases[selector["selector_case"]] += 1
        max_window_size = max(max_window_size, selector["window_size"])
        max_odd_count = max(max_odd_count, selector["odd_count"])
        max_prime_count = max(max_prime_count, len(selector["prime_candidates"]))
        bad_window_size += int(selector["window_size"] > 2)
        bad_prime_multiplicity += int(len(selector["prime_candidates"]) > 1)
        selected = selector["selected_q"]
        if selected is not None:
            bad_selected_not_odd += int(selected % 2 == 0)
            terms.add((selected, m, record["r"], record["beta"]))
            if len(sample_selectors) < 5:
                sample_selectors.append(
                    "m={m},r={r},beta={beta},L={low},U={high},q={q},case={case}".format(
                        m=m,
                        r=record["r"],
                        beta=record["beta"],
                        low=selector["low"],
                        high=selector["high"],
                        q=selected,
                        case=selector["selector_case"],
                    )
                )

    return terms, {
        "selector_cases": dict(sorted(selector_cases.items())),
        "max_reverse_window_size": max_window_size,
        "max_odd_count": max_odd_count,
        "max_prime_count": max_prime_count,
        "bad_window_size": bad_window_size,
        "bad_prime_multiplicity": bad_prime_multiplicity,
        "bad_selected_not_odd": bad_selected_not_odd,
        "sample_selectors": "; ".join(sample_selectors) if sample_selectors else "empty",
    }


def row_audit(P: int, k: int, primes: list[int], prime_set: set[int], records: list[dict[str, int]]) -> dict[str, Any]:
    """审计单行 actual graph 与 reverse selector graph 是否一致。"""
    actual = actual_terms_for_row(P, k, primes)
    reverse, selector_stats = reverse_terms_for_row(P, k, records, prime_set)
    missing = actual - reverse
    extra = reverse - actual
    return {
        "P": P,
        "k": k,
        "actual_support_terms": len(actual),
        "reverse_selector_terms": len(reverse),
        "missing_actual_terms": len(missing),
        "extra_reverse_terms": len(extra),
        "max_reverse_window_size": selector_stats["max_reverse_window_size"],
        "max_odd_count": selector_stats["max_odd_count"],
        "max_prime_count": selector_stats["max_prime_count"],
        "bad_window_size": selector_stats["bad_window_size"],
        "bad_prime_multiplicity": selector_stats["bad_prime_multiplicity"],
        "bad_selected_not_odd": selector_stats["bad_selected_not_odd"],
        "selector_cases": selector_stats["selector_cases"],
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
    row_count = 0
    active_rows = 0
    max_reverse_window_size = 0
    max_odd_count = 0
    max_prime_count = 0
    sample_rows: list[dict[str, Any]] = []

    for P in P_values:
        records = records_by_P[P]
        for k in range(1, P):
            row_count += 1
            row = row_audit(P, k, primes, prime_set, records)
            active_rows += int(row["actual_support_terms"] > 0)
            totals["actual_support_terms"] += row["actual_support_terms"]
            totals["reverse_selector_terms"] += row["reverse_selector_terms"]
            totals["missing_actual_terms"] += row["missing_actual_terms"]
            totals["extra_reverse_terms"] += row["extra_reverse_terms"]
            totals["bad_window_size"] += row["bad_window_size"]
            totals["bad_prime_multiplicity"] += row["bad_prime_multiplicity"]
            totals["bad_selected_not_odd"] += row["bad_selected_not_odd"]
            max_reverse_window_size = max(max_reverse_window_size, row["max_reverse_window_size"])
            max_odd_count = max(max_odd_count, row["max_odd_count"])
            max_prime_count = max(max_prime_count, row["max_prime_count"])
            selector_cases.update(row["selector_cases"])
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_actual_support_terms": totals["actual_support_terms"],
        "total_reverse_selector_terms": totals["reverse_selector_terms"],
        "actual_equals_reverse_selector_terms": totals["actual_support_terms"]
        == totals["reverse_selector_terms"]
        and totals["missing_actual_terms"] == 0
        and totals["extra_reverse_terms"] == 0,
        "missing_actual_terms_total": totals["missing_actual_terms"],
        "extra_reverse_terms_total": totals["extra_reverse_terms"],
        "max_reverse_window_size": max_reverse_window_size,
        "max_odd_count_per_reverse_window": max_odd_count,
        "max_prime_count_per_reverse_window": max_prime_count,
        "bad_reverse_window_size_total": totals["bad_window_size"],
        "bad_prime_multiplicity_total": totals["bad_prime_multiplicity"],
        "bad_selected_not_odd_total": totals["bad_selected_not_odd"],
        "selector_case_totals": dict(sorted(selector_cases.items())),
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_reverse_prime_selector_completion_bridge_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "reverse_prime_selector_normal_form_closed_completion_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after LPF bucket normal form, the fastest non-cyclic continuation is the fixed-cofactor reverse prime selector",
        "current_object": {
            "previous_product_window": "kP < q*r*beta < (k+1)P with q prime and beta r-rough",
            "fixed_cofactor": "m=r*beta",
            "reverse_window": "max(P/2+1, floor(kP/m)+1) <= q <= min(P-1, m, floor(((k+1)P-1)/m))",
            "two_point_bound": "window length is <2 because m>P/2",
            "selector": "q is the unique odd prime in this reverse window, if it exists",
            "phase_after_selector": "e(h*kP/Q_{P,k}(r*beta))",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "FixedRoughCofactorReverseQWindowTwoPointBound",
                True,
                True,
                "For fixed m=r*beta>P/2, the reverse q-window contains at most two consecutive integers.",
                "none",
            ),
            gate(
                "UniqueOddPrimeQSelectorForFixedRoughCofactor",
                True,
                True,
                "Since q>P/2>2 is prime, a nonempty reverse window contains at most one admissible odd prime q.",
                "none",
            ),
            gate(
                "ActualQSupportEqualsReversePrimeSelectorGraph",
                True,
                True,
                "The actual q-support graph equals the graph generated by the fixed-cofactor reverse prime selector.",
                "none",
            ),
            gate(
                "DenseCompletionByAddingAllReverseWindowIntegersRejected",
                True,
                True,
                "Adding the nonselected integer in a two-point reverse window would change the object and destroy pointwise equivalence.",
                "none",
            ),
            gate(
                "FloorPrimeSelectorToCompletedKloostermanConvolutionBridge",
                False,
                False,
                "Convert the floor-defined prime selector over rough cofactors into a same-object completed Kloosterman family.",
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
            "Wright_2026_arXiv_2604_25177": "still needs completed trilinear convolution and SW/equidistribution factor",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "still needs bilinear Kloosterman coefficients rather than a floor-prime selector",
            "Pascadi_2025_arXiv_2511_08445": "still needs Type-II Kloosterman organisation over moduli, not a two-point selector graph",
            "Ford_Maynard_2024_arXiv_2407_14368": "still needs object-specific Type-I/II hypotheses before positivity",
        },
        "latest_narrowest_mouth": [
            "FloorPrimeSelectorToCompletedKloostermanConvolutionBridge",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "reverse_prime_selector_normal_form_closed": True,
        "actual_equals_reverse_selector_graph": finite_audit["actual_equals_reverse_selector_terms"],
        "dense_completion_by_filling_window_rejected": True,
        "floor_prime_selector_completion_bridge_closed": False,
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
        "# Prime Matrix Phi-LPF q-support reverse prime selector completion bridge 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"previous_product_window={current['previous_product_window']}",
        f"fixed_cofactor={current['fixed_cofactor']}",
        f"reverse_window={current['reverse_window']}",
        f"two_point_bound={current['two_point_bound']}",
        f"selector={current['selector']}",
        f"phase_after_selector={current['phase_after_selector']}",
        "```",
        "",
        "## 2. 有限反向选择器审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_actual_support_terms={audit['total_actual_support_terms']}",
        f"total_reverse_selector_terms={audit['total_reverse_selector_terms']}",
        f"actual_equals_reverse_selector_terms={bool_text(audit['actual_equals_reverse_selector_terms'])}",
        f"missing_actual_terms_total={audit['missing_actual_terms_total']}",
        f"extra_reverse_terms_total={audit['extra_reverse_terms_total']}",
        f"max_reverse_window_size={audit['max_reverse_window_size']}",
        f"max_odd_count_per_reverse_window={audit['max_odd_count_per_reverse_window']}",
        f"max_prime_count_per_reverse_window={audit['max_prime_count_per_reverse_window']}",
        f"bad_reverse_window_size_total={audit['bad_reverse_window_size_total']}",
        f"bad_prime_multiplicity_total={audit['bad_prime_multiplicity_total']}",
        f"bad_selected_not_odd_total={audit['bad_selected_not_odd_total']}",
        f"selector_case_totals={audit['selector_case_totals']}",
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
                "reverse_selector_terms",
                "missing_actual_terms",
                "extra_reverse_terms",
                "max_reverse_window_size",
                "max_prime_count",
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
        "结论：本层真推进是把 sparse product-window graph 压成 fixed-cofactor reverse prime selector graph；但相位现在是 floor-prime selector 上的 e(h*kP/q)，仍不是外部定理的 completed Kloosterman family。",
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
        f"reverse_prime_selector_normal_form_closed={bool_text(payload['reverse_prime_selector_normal_form_closed'])}",
        f"actual_equals_reverse_selector_graph={bool_text(payload['actual_equals_reverse_selector_graph'])}",
        f"dense_completion_by_filling_window_rejected={bool_text(payload['dense_completion_by_filling_window_rejected'])}",
        f"floor_prime_selector_completion_bridge_closed={bool_text(payload['floor_prime_selector_completion_bridge_closed'])}",
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
    print("reverse_prime_selector_normal_form_closed=true")
    print("floor_prime_selector_completion_bridge_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
