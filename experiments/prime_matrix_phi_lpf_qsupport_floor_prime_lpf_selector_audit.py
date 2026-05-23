#!/usr/bin/env python3
"""审计 q-support fixed-cofactor floor-prime selector 的 LPF 素性原子化门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_floor_prime_lpf_selector_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-floor-prime-lpf-selector-audit.json

上一层已经把支撑项压成 fixed-cofactor reverse prime selector：

  max(P/2+1, floor(kP/m)+1) <= q <= min(P-1, m, floor(((k+1)P-1)/m)).

本层不再把 ``prime q`` 当作黑箱选择器，而是写出唯一奇候选

  Q_odd = smallest odd integer in [L,U], if it exists,

并把素性选择器原子化为 ``LPF(Q_odd)=Q_odd``。这关闭 floor-prime
selector 的确定性表达门；但它仍是 pointwise LPF-prime selector，不是
completed Kloosterman family，也不证明 Phi-LPF 总目标。
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

SLUG = "prime-matrix-phi-lpf-qsupport-floor-prime-lpf-selector"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge-audit.json",
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


def selector_atom(P: int, k: int, m: int, primes: list[int], prime_set: set[int]) -> dict[str, Any]:
    """固定 m 后返回唯一奇候选与 LPF 素性选择器。"""
    low, high = reverse_q_window(P, k, m)
    window_size = max(0, high - low + 1)
    q_odd, odd_count = unique_odd_candidate(low, high)
    prime_candidates = [q for q in range(low, high + 1) if q in prime_set]
    q_lpf = lpf(q_odd, primes) if q_odd is not None else 0
    selected = q_odd if q_odd is not None and q_lpf == q_odd else None

    if window_size == 0:
        selector_case = "empty_window"
    elif q_odd is None:
        selector_case = "even_singleton_rejected"
    elif selected is not None:
        selector_case = "odd_prime_selected"
    else:
        selector_case = "odd_composite_lpf_rejected"

    direct_selected = prime_candidates[0] if len(prime_candidates) == 1 else None
    return {
        "low": low,
        "high": high,
        "window_size": window_size,
        "q_odd": q_odd,
        "odd_count": odd_count,
        "q_lpf": q_lpf,
        "selected_q": selected,
        "prime_candidates": prime_candidates,
        "direct_selected_q": direct_selected,
        "selector_case": selector_case,
        "bad_window_size": int(window_size > 2),
        "bad_odd_count": int(odd_count > 1),
        "bad_lpf_prime_test": int(selected != direct_selected),
        "bad_prime_multiplicity": int(len(prime_candidates) > 1),
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


def atomized_terms_for_row(
    P: int,
    k: int,
    records: list[dict[str, int]],
    primes: list[int],
    prime_set: set[int],
) -> tuple[set[tuple[int, int, int, int]], dict[str, Any]]:
    """从 unique-odd LPF-prime selector 方向得到支撑项。"""
    terms: set[tuple[int, int, int, int]] = set()
    selector_cases: Counter[str] = Counter()
    rejected_lpf: Counter[int] = Counter()
    max_window_size = 0
    max_odd_count = 0
    max_prime_count = 0
    totals: Counter[str] = Counter()
    sample_selectors: list[str] = []

    for record in records:
        atom = selector_atom(P, k, record["m"], primes, prime_set)
        selector_cases[atom["selector_case"]] += 1
        max_window_size = max(max_window_size, atom["window_size"])
        max_odd_count = max(max_odd_count, atom["odd_count"])
        max_prime_count = max(max_prime_count, len(atom["prime_candidates"]))
        totals["bad_window_size"] += atom["bad_window_size"]
        totals["bad_odd_count"] += atom["bad_odd_count"]
        totals["bad_lpf_prime_test"] += atom["bad_lpf_prime_test"]
        totals["bad_prime_multiplicity"] += atom["bad_prime_multiplicity"]
        totals["windows_with_odd_candidate"] += int(atom["q_odd"] is not None)
        totals["odd_prime_selected"] += int(atom["selected_q"] is not None)
        if atom["q_odd"] is not None and atom["selected_q"] is None:
            rejected_lpf[atom["q_lpf"]] += 1

        selected = atom["selected_q"]
        if selected is not None:
            terms.add((selected, record["m"], record["r"], record["beta"]))
            if len(sample_selectors) < 5:
                sample_selectors.append(
                    "m={m},r={r},beta={beta},L={low},U={high},Q_odd={q},LPF={lpf}".format(
                        m=record["m"],
                        r=record["r"],
                        beta=record["beta"],
                        low=atom["low"],
                        high=atom["high"],
                        q=selected,
                        lpf=atom["q_lpf"],
                    )
                )

    return terms, {
        "selector_cases": dict(sorted(selector_cases.items())),
        "rejected_odd_candidate_lpf_totals": dict(sorted(rejected_lpf.items())),
        "max_reverse_window_size": max_window_size,
        "max_odd_count": max_odd_count,
        "max_prime_count": max_prime_count,
        "bad_window_size": totals["bad_window_size"],
        "bad_odd_count": totals["bad_odd_count"],
        "bad_lpf_prime_test": totals["bad_lpf_prime_test"],
        "bad_prime_multiplicity": totals["bad_prime_multiplicity"],
        "windows_with_odd_candidate": totals["windows_with_odd_candidate"],
        "odd_prime_selected": totals["odd_prime_selected"],
        "sample_selectors": "; ".join(sample_selectors) if sample_selectors else "empty",
    }


def row_audit(P: int, k: int, primes: list[int], prime_set: set[int], records: list[dict[str, int]]) -> dict[str, Any]:
    """审计单行 actual graph 与 LPF-prime selector graph 是否一致。"""
    actual = actual_terms_for_row(P, k, primes)
    atomized, selector_stats = atomized_terms_for_row(P, k, records, primes, prime_set)
    missing = actual - atomized
    extra = atomized - actual
    return {
        "P": P,
        "k": k,
        "actual_support_terms": len(actual),
        "lpf_prime_selector_terms": len(atomized),
        "missing_actual_terms": len(missing),
        "extra_lpf_prime_selector_terms": len(extra),
        "max_reverse_window_size": selector_stats["max_reverse_window_size"],
        "max_odd_count": selector_stats["max_odd_count"],
        "max_prime_count": selector_stats["max_prime_count"],
        "bad_window_size": selector_stats["bad_window_size"],
        "bad_odd_count": selector_stats["bad_odd_count"],
        "bad_lpf_prime_test": selector_stats["bad_lpf_prime_test"],
        "bad_prime_multiplicity": selector_stats["bad_prime_multiplicity"],
        "windows_with_odd_candidate": selector_stats["windows_with_odd_candidate"],
        "odd_prime_selected": selector_stats["odd_prime_selected"],
        "selector_cases": selector_stats["selector_cases"],
        "rejected_odd_candidate_lpf_totals": selector_stats["rejected_odd_candidate_lpf_totals"],
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
    rejected_lpf: Counter[int] = Counter()
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
            totals["lpf_prime_selector_terms"] += row["lpf_prime_selector_terms"]
            totals["missing_actual_terms"] += row["missing_actual_terms"]
            totals["extra_lpf_prime_selector_terms"] += row["extra_lpf_prime_selector_terms"]
            totals["bad_window_size"] += row["bad_window_size"]
            totals["bad_odd_count"] += row["bad_odd_count"]
            totals["bad_lpf_prime_test"] += row["bad_lpf_prime_test"]
            totals["bad_prime_multiplicity"] += row["bad_prime_multiplicity"]
            totals["windows_with_odd_candidate"] += row["windows_with_odd_candidate"]
            totals["odd_prime_selected"] += row["odd_prime_selected"]
            max_reverse_window_size = max(max_reverse_window_size, row["max_reverse_window_size"])
            max_odd_count = max(max_odd_count, row["max_odd_count"])
            max_prime_count = max(max_prime_count, row["max_prime_count"])
            selector_cases.update(row["selector_cases"])
            rejected_lpf.update(row["rejected_odd_candidate_lpf_totals"])
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_actual_support_terms": totals["actual_support_terms"],
        "total_lpf_prime_selector_terms": totals["lpf_prime_selector_terms"],
        "actual_equals_lpf_prime_selector_terms": totals["actual_support_terms"]
        == totals["lpf_prime_selector_terms"]
        and totals["missing_actual_terms"] == 0
        and totals["extra_lpf_prime_selector_terms"] == 0,
        "missing_actual_terms_total": totals["missing_actual_terms"],
        "extra_lpf_prime_selector_terms_total": totals["extra_lpf_prime_selector_terms"],
        "max_reverse_window_size": max_reverse_window_size,
        "max_odd_count_per_reverse_window": max_odd_count,
        "max_prime_count_per_reverse_window": max_prime_count,
        "windows_with_odd_candidate_total": totals["windows_with_odd_candidate"],
        "odd_prime_selected_total": totals["odd_prime_selected"],
        "bad_reverse_window_size_total": totals["bad_window_size"],
        "bad_odd_count_total": totals["bad_odd_count"],
        "bad_lpf_prime_test_total": totals["bad_lpf_prime_test"],
        "bad_prime_multiplicity_total": totals["bad_prime_multiplicity"],
        "selector_case_totals": dict(sorted(selector_cases.items())),
        "rejected_odd_candidate_lpf_totals": dict(sorted(rejected_lpf.items())),
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_floor_prime_lpf_selector_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "floor_prime_lpf_selector_atomized_completion_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "after reverse prime selector, the fastest non-cyclic continuation is the unique-odd LPF primality atom",
        "current_object": {
            "fixed_cofactor": "m=r*beta, with r>=7 prime and beta r-rough",
            "reverse_window": "L=max(P/2+1, floor(kP/m)+1), U=min(P-1, m, floor(((k+1)P-1)/m))",
            "unique_odd_candidate": "Q_odd=L if L is odd, else L+1; valid only when Q_odd<=U",
            "prime_lpf_selector": "selected iff Q_odd exists and LPF(Q_odd)=Q_odd",
            "phase_after_selector": "e(h*kP/Q_odd) on selected atoms",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "ReverseWindowUniqueOddCandidateFormula",
                True,
                True,
                "The two-point reverse window has a closed formula for its only possible odd integer.",
                "none",
            ),
            gate(
                "PrimeSelectorEquivalentToLPFIdentity",
                True,
                True,
                "The prime-q selector is exactly the LPF test LPF(Q_odd)=Q_odd.",
                "none",
            ),
            gate(
                "ActualQSupportEqualsFloorOddLPFPrimeSelectorGraph",
                True,
                True,
                "The actual support graph equals the graph generated by the unique odd LPF-prime selector.",
                "none",
            ),
            gate(
                "MobiusShortcutWithoutLPFGuardRejected",
                True,
                True,
                "No standalone Mobius divisor-sum formula is used as a prime indicator without the LPF/primality guard.",
                "none",
            ),
            gate(
                "OddCandidateLPFPrimeSelectorToCompletedKloostermanConvolutionBridge",
                False,
                False,
                "Convert the pointwise LPF-prime selector over rough cofactors into a same-object completed Kloosterman family.",
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
            "Wright_2026_arXiv_2604_25177": "still needs a completed trilinear/unbalanced convolution with admissible beta equidistribution",
            "Milicevic_Qin_Wu_2025_arXiv_2511_07550": "still needs bilinear Kloosterman coefficients, not a pointwise LPF-prime selector",
            "Pascadi_2025_arXiv_2511_08445": "still needs Type-II Kloosterman organisation over moduli, not a two-point selector graph",
            "Ford_Maynard_2024_arXiv_2407_14368": "still needs object-specific Type-I/II hypotheses before positivity",
        },
        "latest_narrowest_mouth": [
            "OddCandidateLPFPrimeSelectorToCompletedKloostermanConvolutionBridge",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "floor_prime_selector_atomized": True,
        "unique_odd_candidate_formula_closed": True,
        "prime_lpf_test_atomized": True,
        "actual_equals_lpf_prime_selector_graph": finite_audit["actual_equals_lpf_prime_selector_terms"],
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
        "# Prime Matrix Phi-LPF q-support floor prime LPF selector 审计",
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
        f"prime_lpf_selector={current['prime_lpf_selector']}",
        f"phase_after_selector={current['phase_after_selector']}",
        "```",
        "",
        "## 2. 有限 LPF-prime selector 审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_actual_support_terms={audit['total_actual_support_terms']}",
        f"total_lpf_prime_selector_terms={audit['total_lpf_prime_selector_terms']}",
        f"actual_equals_lpf_prime_selector_terms={bool_text(audit['actual_equals_lpf_prime_selector_terms'])}",
        f"missing_actual_terms_total={audit['missing_actual_terms_total']}",
        f"extra_lpf_prime_selector_terms_total={audit['extra_lpf_prime_selector_terms_total']}",
        f"max_reverse_window_size={audit['max_reverse_window_size']}",
        f"max_odd_count_per_reverse_window={audit['max_odd_count_per_reverse_window']}",
        f"max_prime_count_per_reverse_window={audit['max_prime_count_per_reverse_window']}",
        f"windows_with_odd_candidate_total={audit['windows_with_odd_candidate_total']}",
        f"odd_prime_selected_total={audit['odd_prime_selected_total']}",
        f"bad_reverse_window_size_total={audit['bad_reverse_window_size_total']}",
        f"bad_odd_count_total={audit['bad_odd_count_total']}",
        f"bad_lpf_prime_test_total={audit['bad_lpf_prime_test_total']}",
        f"bad_prime_multiplicity_total={audit['bad_prime_multiplicity_total']}",
        f"selector_case_totals={audit['selector_case_totals']}",
        f"rejected_odd_candidate_lpf_totals={audit['rejected_odd_candidate_lpf_totals']}",
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
                "lpf_prime_selector_terms",
                "missing_actual_terms",
                "extra_lpf_prime_selector_terms",
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
        "结论：本层真推进是把 floor-defined prime selector 进一步写成唯一奇候选加 LPF 素性测试；但它仍是逐点选择器，不是 completed Kloosterman family。",
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
        f"floor_prime_selector_atomized={bool_text(payload['floor_prime_selector_atomized'])}",
        f"unique_odd_candidate_formula_closed={bool_text(payload['unique_odd_candidate_formula_closed'])}",
        f"prime_lpf_test_atomized={bool_text(payload['prime_lpf_test_atomized'])}",
        f"actual_equals_lpf_prime_selector_graph={bool_text(payload['actual_equals_lpf_prime_selector_graph'])}",
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
    print("floor_prime_selector_atomized=true")
    print("floor_prime_selector_completion_bridge_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
