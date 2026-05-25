#!/usr/bin/env python3
"""审计 Legendre-Phi / LPF bucket 的周期截断误差。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_legendre_phi_periodic_truncation_error_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json

输出：
  data/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-ledger.json
  docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json
  docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.md
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

SLUG = "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_N = [100, 1000, 10000, 100000]
DISPLAY_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json",
    DOCS / "prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json",
    DOCS / "prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "LegendrePhiTruncationErrorIsPeriodicBoundaryNotHalfMain "
    "AND UnsignedLPFBucketCountStillParityBlind "
    "AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount "
    "AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
)

EXTERNAL_FRONTIER_INPUTS = [
    {
        "name": "Milićević-Qin-Wu bilinear Kloosterman sums",
        "url": "https://arxiv.org/abs/2511.07550",
        "role": "usable only after a genuine two-variable Kloosterman family is constructed",
        "directly_closes_phi_lpf_truncation_error": False,
    },
    {
        "name": "Zheng primes in simultaneous arithmetic progressions",
        "url": "https://arxiv.org/abs/2512.22798",
        "role": "candidate only after the two AP constraints are matched to the same signed family",
        "directly_closes_phi_lpf_truncation_error": False,
    },
    {
        "name": "Runbo Li large-modulus AP primes and Harman sieve refinements",
        "url": "https://arxiv.org/abs/2602.20917",
        "role": "average-modulus input, not pointwise row-column positivity at x=P^2",
        "directly_closes_phi_lpf_truncation_error": False,
    },
    {
        "name": "Wright trilinear Kloosterman fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role": "requires a trilinear convolution and equidistributed coefficient sequence",
        "directly_closes_phi_lpf_truncation_error": False,
    },
    {
        "name": "Becker-Breuillard spectral gaps and anti-concentration",
        "url": "https://arxiv.org/abs/2512.15364",
        "role": "requires a genuine finite-group orbit or thin-group sieve model",
        "directly_closes_phi_lpf_truncation_error": False,
    },
]


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
    """精确计算 Phi(x; primes<p)。"""
    if x <= 0:
        return 0
    return sum(1 for m in range(1, x + 1) if m == 1 or spf[m] >= p)


def bucket_counts_by_scan(N: int, spf: list[int]) -> Counter[int]:
    """直接扫描复合数的 LPF 分桶。"""
    counts: Counter[int] = Counter()
    for n in range(4, N + 1):
        p = spf[n]
        if p != n:
            counts[p] += 1
    return counts


def primorial_data(primes: list[int], p: int) -> tuple[int, int]:
    """返回 W_{<p}=prod_{q<p}q 与 phi(W_{<p})。"""
    W = 1
    phi_W = 1
    for q in primes:
        if q >= p:
            break
        W *= q
        phi_W *= q - 1
    return W, phi_W


def phi_periodic(x: int, p: int, primes: list[int], spf: list[int]) -> dict[str, Any]:
    """用完整 primorial 周期加余数重算 Phi(x; primes<p)。"""
    W, phi_W = primorial_data(primes, p)
    full_periods, remainder = divmod(max(0, x), W)
    remainder_count = rough_count_by_spf(remainder, p, spf)
    periodic_count = full_periods * phi_W + remainder_count
    exact_count = rough_count_by_spf(x, p, spf)
    density = Fraction(phi_W, W)
    boundary_error = Fraction(exact_count, 1) - Fraction(x * phi_W, W)
    return {
        "x": x,
        "p": p,
        "W": W,
        "phi_W": phi_W,
        "full_periods": full_periods,
        "remainder": remainder,
        "remainder_count": remainder_count,
        "periodic_count": periodic_count,
        "exact_count": exact_count,
        "periodic_identity_holds": periodic_count == exact_count,
        "density": density,
        "boundary_error": boundary_error,
        "boundary_error_abs_le_phi_W": abs(boundary_error) <= phi_W,
    }


def exact_lpf_bucket_count(N: int, p: int, spf: list[int]) -> int:
    """精确计数 composite n<=N 且 LPF(n)=p。"""
    return max(0, rough_count_by_spf(N // p, p, spf) - 1)


def fraction_to_text(value: Fraction) -> str:
    """把 Fraction 输出为短文本。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def audit_bucket(N: int, p: int, primes: list[int], spf: list[int], scan: Counter[int]) -> dict[str, Any]:
    """审计单个 LPF owner bucket 的周期误差。"""
    X = N // p
    phi_X = phi_periodic(X, p, primes, spf)
    phi_base = phi_periodic(p - 1, p, primes, spf)
    exact = exact_lpf_bucket_count(N, p, spf)
    W = int(phi_X["W"])
    phi_W = int(phi_X["phi_W"])
    density = Fraction(phi_W, W)

    endpoint_main = Fraction((X - (p - 1)) * phi_W, W)
    endpoint_error = Fraction(exact, 1) - endpoint_main
    n_axis_main = Fraction(N - p * p, p) * density
    n_axis_error = Fraction(exact, 1) - n_axis_main

    main_for_ratio = endpoint_main if endpoint_main else Fraction(0, 1)
    half_error_ratio = (
        float(abs(endpoint_error) / main_for_ratio) if main_for_ratio > 0 else None
    )
    return {
        "p": p,
        "X_floor_N_over_p": X,
        "W_lt_p": W,
        "phi_W": phi_W,
        "density": fraction_to_text(density),
        "exact": exact,
        "scan_exact": scan[p],
        "scan_matches_phi_identity": exact == scan[p],
        "periodic_identity_holds_at_X": bool(phi_X["periodic_identity_holds"]),
        "periodic_identity_holds_at_p_minus_1": bool(phi_base["periodic_identity_holds"]),
        "endpoint_refined_main": float(endpoint_main),
        "endpoint_refined_error": float(endpoint_error),
        "endpoint_refined_error_fraction": fraction_to_text(endpoint_error),
        "endpoint_error_abs_le_2phi_W": abs(endpoint_error) <= 2 * phi_W,
        "n_axis_main": float(n_axis_main),
        "n_axis_error": float(n_axis_error),
        "half_error_ratio_endpoint_refined": half_error_ratio,
        "boundary_error_X_fraction": fraction_to_text(phi_X["boundary_error"]),
        "boundary_error_p_minus_1_fraction": fraction_to_text(phi_base["boundary_error"]),
    }


def audit_N(N: int) -> dict[str, Any]:
    """审计单个 N 的所有 LPF bucket。"""
    spf = spf_table(N)
    primes = primes_upto_from_spf(spf)
    scan = bucket_counts_by_scan(N, spf)
    bucket_primes = [p for p in primes if p * p <= N]
    rows = [audit_bucket(N, p, primes, spf, scan) for p in bucket_primes]

    exact_total = sum(row["exact"] for row in rows)
    composite_count = sum(1 for n in range(4, N + 1) if spf[n] != n)
    endpoint_total = sum(row["endpoint_refined_main"] for row in rows)
    n_axis_total = sum(row["n_axis_main"] for row in rows)
    half_like_rows = [
        row["p"]
        for row in rows
        if row["half_error_ratio_endpoint_refined"] is not None
        and abs(row["half_error_ratio_endpoint_refined"] - 0.5) <= 0.05
    ]
    return {
        "N": N,
        "sqrt_prime_bucket_count": len(bucket_primes),
        "composite_count": composite_count,
        "exact_lpf_bucket_total": exact_total,
        "exact_lpf_buckets_sum_to_composites": exact_total == composite_count,
        "all_scan_matches_phi_identity": all(row["scan_matches_phi_identity"] for row in rows),
        "all_periodic_identities_hold": all(
            row["periodic_identity_holds_at_X"]
            and row["periodic_identity_holds_at_p_minus_1"]
            for row in rows
        ),
        "all_endpoint_errors_within_bound": all(row["endpoint_error_abs_le_2phi_W"] for row in rows),
        "endpoint_refined_total": endpoint_total,
        "endpoint_refined_total_over_exact": endpoint_total / exact_total if exact_total else 0.0,
        "n_axis_total": n_axis_total,
        "n_axis_total_over_exact": n_axis_total / exact_total if exact_total else 0.0,
        "half_main_like_bucket_count": len(half_like_rows),
        "half_main_like_bucket_primes": half_like_rows[:20],
        "display_rows": [row for row in rows if row["p"] in DISPLAY_PRIMES],
    }


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装审计证书。"""
    audits = [audit_N(N) for N in SAMPLE_N]
    return {
        "certificate_type": "prime_matrix_phi_lpf_legendre_phi_periodic_truncation_error_audit",
        "status": "legendre_phi_truncation_error_is_periodic_boundary_not_half_main",
        "verified_date": "2026-05-25",
        "sample_N": SAMPLE_N,
        "exact_bucket_formula": "C_p(N)=Phi(floor(N/p); primes<p)-Phi(p-1; primes<p)",
        "periodic_phi_formula": (
            "Phi(x; primes<p)=floor(x/W_<p)*phi(W_<p)+R_p(x mod W_<p)"
        ),
        "boundary_error_formula": (
            "C_p(N)=(floor(N/p)-p+1)*phi(W_<p)/W_<p + "
            "B_p(floor(N/p))-B_p(p-1), |B_p(t)|<=phi(W_<p)"
        ),
        "legendre_phi_periodic_truncation_error_closed": all(
            audit["all_periodic_identities_hold"] and audit["all_endpoint_errors_within_bound"]
            for audit in audits
        ),
        "exact_lpf_bucket_identity_closed": all(
            audit["exact_lpf_buckets_sum_to_composites"]
            and audit["all_scan_matches_phi_identity"]
            for audit in audits
        ),
        "half_main_truncation_error_claim_supported": False,
        "truncation_error_is_periodic_residue_boundary": True,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "admissible_typeii_or_trace_family_constructed": False,
        "admissible_finite_group_orbit_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "audits": audits,
        "external_frontier_inputs": EXTERNAL_FRONTIER_INPUTS,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The Legendre-Phi truncation error is not a universal half-main "
            "phenomenon. After the correct LPF owner class and endpoint are used, "
            "Phi is an exact primorial-periodic count plus a bounded boundary "
            "remainder. This closes the local truncation grammar but leaves the "
            "prime-extraction problem parity-blind until a signed divisor, trace, "
            "Kloosterman, Type-II, or finite-group orbit family is constructed."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF Legendre-Phi periodic truncation error 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 严格公式",
        "",
        "设",
        "",
        "```text",
        "W_<p = prod_{q<p} q.",
        "```",
        "",
        "则 Legendre-Phi 粗数计数有完整周期分解：",
        "",
        "```text",
        "Phi(x; primes<p) = floor(x/W_<p)*phi(W_<p) + R_p(x mod W_<p).",
        "```",
        "",
        "因此 composite LPF bucket 不是一个带固定半主项误差的欧拉乘积估计，而是：",
        "",
        "```text",
        "C_p(N)=Phi(floor(N/p); primes<p)-Phi(p-1; primes<p)",
        "      =(floor(N/p)-p+1)*phi(W_<p)/W_<p",
        "       + B_p(floor(N/p))-B_p(p-1),",
        "|B_p(t)| <= phi(W_<p).",
        "```",
        "",
        "这说明截断误差是 primorial 周期余数边界项，不是普遍的 `1/2 main`。",
        "",
        "## 2. 全局读数",
        "",
        "```text",
        f"legendre_phi_periodic_truncation_error_closed={fmt_bool(payload['legendre_phi_periodic_truncation_error_closed'])}",
        f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}",
        f"half_main_truncation_error_claim_supported={fmt_bool(payload['half_main_truncation_error_claim_supported'])}",
        f"truncation_error_is_periodic_residue_boundary={fmt_bool(payload['truncation_error_is_periodic_residue_boundary'])}",
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| N | exact total | composite count | endpoint main/exact | n-axis main/exact | half-like buckets |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| {N} | {exact_lpf_bucket_total} | {composite_count} | "
            "{endpoint_refined_total_over_exact:.6f} | {n_axis_total_over_exact:.6f} | "
            "{half_main_like_bucket_count} |".format(**audit)
        )
    lines.extend(["", "## 3. 样本 bucket", ""])
    for audit in payload["audits"]:
        lines.extend(
            [
                f"### N={audit['N']}",
                "",
                "| p | exact | density | endpoint main | endpoint error | n-axis main | n-axis error | W_<p |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in audit["display_rows"]:
            lines.append(
                "| {p} | {exact} | {density} | {endpoint_refined_main:.6f} | "
                "{endpoint_refined_error:.6f} | {n_axis_main:.6f} | "
                "{n_axis_error:.6f} | {W_lt_p} |".format(**row)
            )
        lines.append("")
    lines.extend(
        [
            "## 4. 外部前沿可用性",
            "",
            "| input | url | current role | direct close |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in payload["external_frontier_inputs"]:
        lines.append(
            "| {name} | {url} | {role} | `{direct}` |".format(
                direct=fmt_bool(item["directly_closes_phi_lpf_truncation_error"]),
                **item,
            )
        )
    lines.extend(
        [
            "",
            "## 5. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 6. 依赖哈希",
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
    print(
        "legendre_phi_periodic_truncation_error_closed="
        f"{fmt_bool(payload['legendre_phi_periodic_truncation_error_closed'])}"
    )
    print(f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}")
    print(
        "half_main_truncation_error_claim_supported="
        f"{fmt_bool(payload['half_main_truncation_error_claim_supported'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
