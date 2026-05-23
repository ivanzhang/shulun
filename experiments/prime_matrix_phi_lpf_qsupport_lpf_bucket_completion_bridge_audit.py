#!/usr/bin/env python3
"""审计 q-support 谓词的 LPF 桶展开与 completion bridge 剩余门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_qsupport_lpf_bucket_completion_bridge_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge-audit.json

上一层已经把完整叶子相位压成

  sum_{q in S(P,k)} e(h*kP/q).

本层继续下钻 S(P,k)。对每个 prime q in (P/2,P)，q 侧窗口至多给出
一个 odd candidate omega。残余 q-support 谓词等价于

  omega is composite and LPF(omega)>=7.

本脚本验证这个谓词的唯一 LPF 桶/rough-Mobius 展开，并记录为什么它仍然
不是 Wright/MQW/Pascadi/Ford--Maynard 等外部 theorem 所需的 completed
bilinear/trilinear Kloosterman convolution。真正未闭合的是 sparse product-window
graph 到 completed Kloosterman family 的同对象桥。
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-qsupport-external-theorem-match-audit.json",
    DOCS / "prime-matrix-phi-lpf-complete-leaf-phase-collapse-audit.json",
    DOCS / "prime-matrix-phi-lpf-complete-rough-factor-tree-closure-audit.json",
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


def unique_odd_candidate(P: int, k: int, q: int) -> tuple[int | None, int]:
    """返回窗口中的唯一奇候选及奇候选数量。"""
    low, high = q_window(P, k, q)
    if low > high:
        return None, 0
    odd_low = low if low % 2 else low + 1
    if odd_low > high:
        return None, 0
    count = ((high - odd_low) // 2) + 1
    return (odd_low if count == 1 else None), count


def reverse_q_window(P: int, k: int, m: int) -> tuple[int, int]:
    """固定 m 后返回满足 kP<qm<(k+1)P 的 q 整数窗口。"""
    low = max(P // 2 + 1, (k * P) // m + 1)
    high = min(P - 1, (((k + 1) * P) - 1) // m)
    return low, high


def lpf_bucket_terms(n: int, primes: list[int]) -> list[dict[str, int]]:
    """用 rough-Mobius/LPF 桶公式列出 residual terms。

    对每个 prime r>=7, r<=sqrt(n)，项为

      1_{r|n} * sum_{d|n, P^+(d)<r} mu(d).

    内层和为 1 当且仅当 n 没有小于 r 的素因子，否则为 0。
    """
    terms: list[dict[str, int]] = []
    for r in primes:
        if r < 7:
            continue
        if r * r > n:
            break
        if n % r != 0:
            continue
        # 中文注释：rough-Mobius 内层和只检测是否存在更小素因子。
        smaller_factor = any(n % p == 0 for p in primes if p < r)
        if smaller_factor:
            mobius_inner_sum = 0
        else:
            mobius_inner_sum = 1
        beta = n // r
        if mobius_inner_sum == 1 and beta >= r:
            terms.append({"r": r, "beta": beta, "mobius_inner_sum": mobius_inner_sum})
    return terms


def direct_residual_indicator(n: int, primes: list[int]) -> bool:
    """直接判定 residual cofactor：合数且 LPF>=7。"""
    r = lpf(n, primes)
    return r >= 7 and r != n


def row_audit(P: int, k: int, primes: list[int], prime_set: set[int]) -> dict[str, Any]:
    """审计单行的 q-support LPF 桶展开。"""
    q_values = [q for q in primes if P // 2 < q < P]
    odd_candidates = 0
    residual_support = 0
    bucket_terms_total = 0
    bad_candidate_count = 0
    bad_bucket_formula = 0
    bad_reverse_window = 0
    max_terms_per_candidate = 0
    max_reverse_prime_count = 0
    r_counter: Counter[int] = Counter()
    samples: list[str] = []

    for q in q_values:
        omega, odd_count = unique_odd_candidate(P, k, q)
        if odd_count > 1:
            bad_candidate_count += 1
        if omega is None:
            continue
        odd_candidates += 1
        terms = lpf_bucket_terms(omega, primes)
        direct = direct_residual_indicator(omega, primes)
        residual_support += int(direct)
        bucket_terms_total += len(terms)
        max_terms_per_candidate = max(max_terms_per_candidate, len(terms))
        if direct != (len(terms) == 1):
            bad_bucket_formula += 1
        if len(terms) == 1:
            r = terms[0]["r"]
            beta = terms[0]["beta"]
            r_counter[r] += 1
            rev_low, rev_high = reverse_q_window(P, k, omega)
            reverse_primes = [v for v in range(rev_low, rev_high + 1) if v in prime_set]
            max_reverse_prime_count = max(max_reverse_prime_count, len(reverse_primes))
            if q not in reverse_primes:
                bad_reverse_window += 1
            if len(samples) < 5:
                samples.append(
                    f"q={q},omega={omega},r={r},beta={beta},reverse_prime_count={len(reverse_primes)}"
                )

    return {
        "P": P,
        "k": k,
        "prime_q_count": len(q_values),
        "odd_candidate_count": odd_candidates,
        "residual_support_count": residual_support,
        "lpf_bucket_terms_total": bucket_terms_total,
        "max_terms_per_candidate": max_terms_per_candidate,
        "max_reverse_prime_count": max_reverse_prime_count,
        "bad_candidate_count": bad_candidate_count,
        "bad_bucket_formula": bad_bucket_formula,
        "bad_reverse_window": bad_reverse_window,
        "r_bucket_totals": dict(sorted(r_counter.items())),
        "sample_terms": "; ".join(samples) if samples else "empty",
    }


def audit_rows(max_prime: int = 1009) -> dict[str, Any]:
    """对 P<=max_prime 的全部 1<=k<P 行做有限一致性审计。"""
    primes = prime_sieve(2 * max_prime + 10)
    prime_set = set(primes)
    P_values = [p for p in primes if 11 <= p <= max_prime]
    interesting = {(101, 100), (257, 256), (971, 936), (1009, 1008)}

    totals: Counter[str] = Counter()
    global_r_counter: Counter[int] = Counter()
    max_terms_per_candidate = 0
    max_reverse_prime_count = 0
    sample_rows: list[dict[str, Any]] = []
    row_count = 0
    active_rows = 0
    reverse_multiplicity_by_row: defaultdict[int, int] = defaultdict(int)

    for P in P_values:
        for k in range(1, P):
            row_count += 1
            row = row_audit(P, k, primes, prime_set)
            active_rows += int(row["residual_support_count"] > 0)
            totals["prime_q_instances"] += row["prime_q_count"]
            totals["odd_candidate_instances"] += row["odd_candidate_count"]
            totals["residual_support_instances"] += row["residual_support_count"]
            totals["lpf_bucket_terms_total"] += row["lpf_bucket_terms_total"]
            totals["bad_candidate_count"] += row["bad_candidate_count"]
            totals["bad_bucket_formula"] += row["bad_bucket_formula"]
            totals["bad_reverse_window"] += row["bad_reverse_window"]
            max_terms_per_candidate = max(max_terms_per_candidate, row["max_terms_per_candidate"])
            max_reverse_prime_count = max(max_reverse_prime_count, row["max_reverse_prime_count"])
            reverse_multiplicity_by_row[row["max_reverse_prime_count"]] += 1
            for r_key, value in row["r_bucket_totals"].items():
                global_r_counter[int(r_key)] += value
            if (P, k) in interesting:
                sample_rows.append(row)

    return {
        "max_prime": max_prime,
        "k_range": "1<=k<P in this implementation audit",
        "row_count": row_count,
        "active_residual_row_count": active_rows,
        "total_prime_q_instances": totals["prime_q_instances"],
        "total_odd_candidate_instances": totals["odd_candidate_instances"],
        "total_residual_support_instances": totals["residual_support_instances"],
        "total_lpf_bucket_terms": totals["lpf_bucket_terms_total"],
        "actual_support_equals_lpf_bucket_terms": totals["residual_support_instances"]
        == totals["lpf_bucket_terms_total"],
        "max_terms_per_candidate": max_terms_per_candidate,
        "max_reverse_prime_count_per_lpf_bucket": max_reverse_prime_count,
        "bad_candidate_count": totals["bad_candidate_count"],
        "bad_bucket_formula_total": totals["bad_bucket_formula"],
        "bad_reverse_window_total": totals["bad_reverse_window"],
        "reverse_prime_multiplicity_row_histogram": dict(sorted(reverse_multiplicity_by_row.items())),
        "r_bucket_totals": dict(sorted(global_r_counter.items())),
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
                value = ", ".join(f"{k}:{value[k]}" for k in sorted(value, key=lambda x: int(x)))
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
        "certificate_type": "prime_matrix_phi_lpf_qsupport_lpf_bucket_completion_bridge_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "lpf_bucket_normal_form_closed_completion_bridge_open",
        "chosen_claim": "Prime Matrix row/column Phi-LPF",
        "reason_chosen": "the q-support completion bridge is the narrowest non-cyclic continuation after external theorem matching",
        "current_object": {
            "phase_sum": "sum_{q in S(P,k)} e(h*kP/q)",
            "support_predicate": "q in S(P,k) iff the unique odd candidate omega_{P,k}(q) is composite with LPF(omega)>=7",
            "lpf_bucket_formula": "1_S(q)=sum_{7<=r<=sqrt(omega), r prime, r|omega} 1_{P^-(omega)>=r} 1_{omega/r>=r}",
            "rough_mobius_inner_sum": "1_{P^-(omega)>=r}=sum_{d|omega, P^+(d)<r} mu(d)",
            "product_window_shape": "kP < q*r*beta < (k+1)P with beta=omega/r and P^-(beta)>=r",
        },
        "finite_audit": finite_audit,
        "closed_gates": [
            gate(
                "QSupportUniqueOddCandidateLPFBucketNormalForm",
                True,
                True,
                "The actual q-support predicate is exactly a unique LPF bucket over the odd candidate omega_{P,k}(q).",
                "none",
            ),
            gate(
                "RoughMobiusLPFBucketIdentityForQSupport",
                True,
                True,
                "The LPF bucket can be written as a rough-Mobius inner sum over primes below r.",
                "none",
            ),
            gate(
                "SparseProductWindowGraphNormalForm",
                True,
                True,
                "Every support term is a sparse product-window triple (q,r,beta) with max reverse prime multiplicity one.",
                "none",
            ),
            gate(
                "NaiveDenseDyadicConvolutionCompletionRejected",
                True,
                True,
                "The product-window graph is sparse and pointwise; treating it as a dense completed convolution would add non-object terms.",
                "none",
            ),
            gate(
                "SparseLPFBucketProductWindowGraphToCompletedKloostermanConvolutionBridge",
                False,
                False,
                "Construct a same-object bridge from sparse product-window triples to a completed bilinear/trilinear Kloosterman family.",
                "new bridge theorem",
            ),
            gate(
                "RoughBetaSiegelWalfiszUniformityOrReplacement",
                False,
                False,
                "Provide the SW/equidistribution factor required by external trilinear theorems, or replace it by an object-specific theorem.",
                "rough beta uniformity input",
            ),
        ],
        "external_theorem_implication": {
            "Wright_2026": "still requires completed convolution plus equidistributed/SW factor",
            "Milicevic_Qin_Wu_2025": "still requires admissible bilinear Kloosterman coefficients",
            "Pascadi_2025": "still requires Type-II organisation over the target modulus family",
            "Ford_Maynard_2024": "still requires object-specific Type-I/II inputs before sieve positivity",
        },
        "latest_narrowest_mouth": [
            "SparseLPFBucketProductWindowGraphToCompletedKloostermanConvolutionBridge",
            "AND RoughBetaSiegelWalfiszUniformityOrReplacement",
            "AND PointwisePKUniformTransferFromExternalAverageEstimate",
            "AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity",
        ],
        "lpf_bucket_normal_form_closed": True,
        "rough_mobius_identity_closed": True,
        "sparse_product_window_normal_form_closed": True,
        "dense_completed_convolution_available": False,
        "siegel_walfisz_factor_extracted": False,
        "same_object_kloosterman_bridge_closed": False,
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
        "# Prime Matrix Phi-LPF q-support LPF bucket completion bridge 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 当前对象",
        "",
        "```text",
        f"phase_sum={current['phase_sum']}",
        f"support_predicate={current['support_predicate']}",
        f"lpf_bucket_formula={current['lpf_bucket_formula']}",
        f"rough_mobius_inner_sum={current['rough_mobius_inner_sum']}",
        f"product_window_shape={current['product_window_shape']}",
        "```",
        "",
        "## 2. 有限 LPF 桶审计",
        "",
        "```text",
        f"max_prime={audit['max_prime']}",
        f"k_range={audit['k_range']}",
        f"row_count={audit['row_count']}",
        f"active_residual_row_count={audit['active_residual_row_count']}",
        f"total_prime_q_instances={audit['total_prime_q_instances']}",
        f"total_odd_candidate_instances={audit['total_odd_candidate_instances']}",
        f"total_residual_support_instances={audit['total_residual_support_instances']}",
        f"total_lpf_bucket_terms={audit['total_lpf_bucket_terms']}",
        f"actual_support_equals_lpf_bucket_terms={bool_text(audit['actual_support_equals_lpf_bucket_terms'])}",
        f"max_terms_per_candidate={audit['max_terms_per_candidate']}",
        f"max_reverse_prime_count_per_lpf_bucket={audit['max_reverse_prime_count_per_lpf_bucket']}",
        f"bad_candidate_count={audit['bad_candidate_count']}",
        f"bad_bucket_formula_total={audit['bad_bucket_formula_total']}",
        f"bad_reverse_window_total={audit['bad_reverse_window_total']}",
        f"r_bucket_totals={audit['r_bucket_totals']}",
        "```",
        "",
        "代表行：",
        "",
        table(
            audit["sample_rows"],
            [
                "P",
                "k",
                "prime_q_count",
                "odd_candidate_count",
                "residual_support_count",
                "lpf_bucket_terms_total",
                "max_reverse_prime_count",
                "r_bucket_totals",
                "sample_terms",
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
        "结论：本层真推进是把 q-support 谓词压成唯一 LPF 桶和 sparse product-window graph；但这仍不是 completed Kloosterman convolution。直接把稀疏图填充成密集 dyadic convolution 会加入非同对象项。",
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
        f"lpf_bucket_normal_form_closed={bool_text(payload['lpf_bucket_normal_form_closed'])}",
        f"rough_mobius_identity_closed={bool_text(payload['rough_mobius_identity_closed'])}",
        f"sparse_product_window_normal_form_closed={bool_text(payload['sparse_product_window_normal_form_closed'])}",
        f"dense_completed_convolution_available={bool_text(payload['dense_completed_convolution_available'])}",
        f"siegel_walfisz_factor_extracted={bool_text(payload['siegel_walfisz_factor_extracted'])}",
        f"same_object_kloosterman_bridge_closed={bool_text(payload['same_object_kloosterman_bridge_closed'])}",
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
    print("lpf_bucket_normal_form_closed=true")
    print("same_object_kloosterman_bridge_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
