#!/usr/bin/env python3
"""审计 LPF 最小素因子分桶计数公式。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_lpf_bucket_count_formula_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json

输出：
  data/prime-matrix-phi-lpf-lpf-bucket-count-formula-ledger.json
  docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json
  docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.md
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-lpf-bucket-count-formula"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_N = [100, 1000, 10000, 100000]
DISPLAY_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json",
    DOCS / "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json",
    DOCS / "prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
]

LATEST_OPEN_GATE = (
    "ExactLPFBucketCountIsLegendrePhiNotReciprocalDensity "
    "AND UnsignedLPFBucketCountStillParityBlind "
    "AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount "
    "AND PointwiseThetaAPPositivityAtP2OrAdmissibleSignedDivisorPayloadTypeIIFamily"
)


def spf_table(limit: int) -> list[int]:
    """返回最小素因子表。"""
    spf = list(range(limit + 1))
    if limit >= 0:
        spf[0] = 0
    if limit >= 1:
        spf[1] = 1
    for p in range(2, int(limit**0.5) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def primes_upto_from_spf(spf: list[int]) -> list[int]:
    """从最小素因子表提取素数。"""
    return [n for n in range(2, len(spf)) if spf[n] == n]


def rough_count_by_spf(x: int, p: int, spf: list[int]) -> int:
    """精确计算 Phi(x; p^-): 计数 m=1 或 SPF(m)>=p。"""
    if x <= 0:
        return 0
    return sum(1 for m in range(1, x + 1) if m == 1 or spf[m] >= p)


def exact_lpf_bucket_count(N: int, p: int, spf: list[int]) -> int:
    """精确计数 composite n<=N 且 LPF(n)=p。"""
    x = N // p
    # m=1 对应 n=p，是端点素数，不属于 composite bucket；m<p 的其余数不会存活。
    return max(0, rough_count_by_spf(x, p, spf) - 1)


def corrected_continuous_main(N: int, p: int, primes: list[int]) -> float:
    """正确连续主项: (N/p-p)*prod_{q<p}(1-1/q)。"""
    if p * p > N:
        return 0.0
    density = Fraction(1, 1)
    for q in primes:
        if q >= p:
            break
        density *= Fraction(q - 1, q)
    return float(Fraction(N - p * p, p) * density)


def user_reciprocal_main(N: int, p: int, primes: list[int]) -> float:
    """用户草式: (N-p^2)*prod_{q<=p} 1/q。"""
    if p * p > N:
        return 0.0
    denom = 1
    for q in primes:
        denom *= q
        if q == p:
            break
    return (N - p * p) / denom


def survival_density_factor(p: int, primes: list[int]) -> str:
    """渲染正确密度因子。"""
    factor = Fraction(1, p)
    for q in primes:
        if q >= p:
            break
        factor *= Fraction(q - 1, q)
    return f"{factor.numerator}/{factor.denominator}"


def reciprocal_density_factor(p: int, primes: list[int]) -> str:
    """渲染用户草式密度因子。"""
    denom = 1
    for q in primes:
        denom *= q
        if q == p:
            break
    return f"1/{denom}"


def bucket_counts_by_scan(N: int, spf: list[int]) -> Counter[int]:
    """直接扫描复合数的 LPF 分桶。"""
    counts: Counter[int] = Counter()
    for n in range(4, N + 1):
        p = spf[n]
        if p != n:
            counts[p] += 1
    return counts


def audit_N(N: int) -> dict[str, Any]:
    """审计单个 N。"""
    spf = spf_table(N)
    primes = primes_upto_from_spf(spf)
    buckets_scan = bucket_counts_by_scan(N, spf)
    primes_to_sqrt = [p for p in primes if p * p <= N]

    rows = []
    exact_total = 0
    corrected_total = 0.0
    user_total = 0.0
    exact_formula_mismatches = []
    first_user_bad_prime = None

    for p in primes_to_sqrt:
        exact = exact_lpf_bucket_count(N, p, spf)
        scanned = buckets_scan[p]
        if exact != scanned:
            exact_formula_mismatches.append({"p": p, "exact": exact, "scan": scanned})
        corrected = corrected_continuous_main(N, p, primes)
        user = user_reciprocal_main(N, p, primes)
        exact_total += exact
        corrected_total += corrected
        user_total += user
        if p >= 5 and first_user_bad_prime is None and abs(corrected - user) > 1e-12:
            first_user_bad_prime = p
        if p in DISPLAY_PRIMES:
            rows.append(
                {
                    "p": p,
                    "exact": exact,
                    "corrected_main": corrected,
                    "user_reciprocal_main": user,
                    "correct_density_factor": survival_density_factor(p, primes),
                    "user_density_factor": reciprocal_density_factor(p, primes),
                    "corrected_over_exact": corrected / exact if exact else None,
                    "user_over_exact": user / exact if exact else None,
                }
            )

    composite_count = sum(1 for n in range(4, N + 1) if spf[n] != n)
    return {
        "N": N,
        "sqrt_prime_bucket_count": len(primes_to_sqrt),
        "composite_count": composite_count,
        "exact_lpf_bucket_total": exact_total,
        "exact_lpf_buckets_sum_to_composites": exact_total == composite_count,
        "exact_phi_formula_mismatch_count": len(exact_formula_mismatches),
        "exact_phi_formula_mismatch_sample": exact_formula_mismatches[:3],
        "corrected_continuous_total": corrected_total,
        "user_reciprocal_total": user_total,
        "corrected_total_over_exact": corrected_total / exact_total if exact_total else 0.0,
        "user_total_over_exact": user_total / exact_total if exact_total else 0.0,
        "first_user_formula_wrong_prime": first_user_bad_prime,
        "display_rows": rows,
    }


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    audits = [audit_N(N) for N in SAMPLE_N]
    return {
        "certificate_type": "prime_matrix_phi_lpf_lpf_bucket_count_formula_audit",
        "status": "exact_lpf_bucket_count_is_legendre_phi_not_reciprocal_density",
        "verified_date": "2026-05-25",
        "sample_N": SAMPLE_N,
        "exact_formula": "C_p(N)=Phi(floor(N/p); primes< p)-1",
        "correct_continuous_main": "(N/p-p)*prod_{q<p}(1-1/q)",
        "user_formula": "(N-p^2)*prod_{q<=p}1/q",
        "user_formula_correct_for_p2_p3_only_as_density_accident": True,
        "first_structural_wrong_prime": 5,
        "reason_user_formula_fails": (
            "For q<p one must survive the forbidden residue 0 mod q, with "
            "density 1-1/q. Multiplying by 1/q counts one residue class instead "
            "of all nonzero residue classes."
        ),
        "exact_lpf_bucket_identity_closed": all(
            row["exact_lpf_buckets_sum_to_composites"]
            and row["exact_phi_formula_mismatch_count"] == 0
            for row in audits
        ),
        "corrected_main_is_only_continuous_not_exact": True,
        "user_reciprocal_density_formula_supported": False,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "audits": audits,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The exact LPF bucket count is a Legendre-Phi rough-number count. "
            "The corrected main term uses survival densities (1-1/q), not "
            "reciprocal densities 1/q. This closes the bucket-count arithmetic "
            "diagnosis but remains an unsigned sieve identity, so it does not "
            "extract primes or break parity without a signed divisor payload."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF LPF bucket count formula 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 结论",
        "",
        "对 composite bucket，精确公式不是用户草式的全 reciprocal product，而是",
        "Legendre-`Phi` 粗数计数：",
        "",
        "```text",
        "C_p(N) = #{n<=N composite : LPF(n)=p}",
        "       = Phi(floor(N/p); primes < p) - 1",
        "```",
        "",
        "`-1` 去掉的是 `m=1`，即端点素数 `n=p`。连续主项应为：",
        "",
        "```text",
        "(N/p - p) * prod_{q<p}(1-1/q)",
        "  = (N-p^2)/p * prod_{q<p}(1-1/q).",
        "```",
        "",
        "用户草式",
        "",
        "```text",
        "(N-p^2) * prod_{q<=p} 1/q",
        "```",
        "",
        "在 `p=2,3` 因低阶偶然相同；从 `p=5` 起把“避开 0 类”的生存密度",
        "`1-1/q` 误写成了单类密度 `1/q`。",
        "",
        "## 2. 全局读数",
        "",
        "```text",
        f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}",
        f"user_reciprocal_density_formula_supported={fmt_bool(payload['user_reciprocal_density_formula_supported'])}",
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| N | exact total | composite count | corrected total/exact | user total/exact | first wrong p |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| {N} | {exact_lpf_bucket_total} | {composite_count} | "
            "{corrected_total_over_exact:.6f} | {user_total_over_exact:.6f} | "
            "{first_user_formula_wrong_prime} |".format(**audit)
        )
    lines.extend(["", "## 3. 样本 bucket", ""])
    for audit in payload["audits"]:
        lines.extend(
            [
                f"### N={audit['N']}",
                "",
                "| p | exact | correct density | corrected main | user density | user main |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in audit["display_rows"]:
            lines.append(
                "| {p} | {exact} | {correct_density_factor} | "
                "{corrected_main:.6f} | {user_density_factor} | "
                "{user_reciprocal_main:.6f} |".format(**row)
            )
        lines.append("")
    lines.extend(
        [
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in payload["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出审计证书。"""
    payload = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}")
    print(f"user_reciprocal_density_formula_supported={fmt_bool(payload['user_reciprocal_density_formula_supported'])}")
    print(
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
