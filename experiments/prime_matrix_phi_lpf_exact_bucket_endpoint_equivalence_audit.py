#!/usr/bin/env python3
"""审计 LPF 精确分桶公式的端点等价与连续主项边界。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_exact_bucket_endpoint_equivalence_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json

输出：
  data/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-ledger.json
  docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json
  docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.md
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_N = [30, 100, 1000, 10000, 100000]
DISPLAY_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json",
    DOCS / "prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json",
    DOCS / "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "ExactLPFBucketEndpointSingletonFixed "
    "AND FloorEndpointAndPeriodicBoundaryRetained "
    "AND ContinuousEulerMainNotExactCount "
    "AND UnsignedLPFBucketCountStillParityBlind "
    "AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount"
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
    """精确计算 Phi(x; primes<p)，其中 1 计入。"""
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
    """返回 W_<p 与 phi(W_<p)。"""
    W = 1
    phi_W = 1
    for q in primes:
        if q >= p:
            break
        W *= q
        phi_W *= q - 1
    return W, phi_W


def density_less_than_p(primes: list[int], p: int) -> Fraction:
    """避开所有 q<p 的零类密度。"""
    W, phi_W = primorial_data(primes, p)
    return Fraction(phi_W, W)


def exact_lpf_bucket_count(N: int, p: int, spf: list[int]) -> int:
    """精确计数 composite n<=N 且 LPF(n)=p。"""
    return max(0, rough_count_by_spf(N // p, p, spf) - 1)


def fraction_to_text(value: Fraction) -> str:
    """把 Fraction 输出为短文本。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def audit_bucket(N: int, p: int, primes: list[int], spf: list[int], scan: Counter[int]) -> dict[str, Any]:
    """审计单个 LPF bucket 的精确式与连续主项差别。"""
    X = N // p
    phi_X = rough_count_by_spf(X, p, spf)
    phi_endpoint = rough_count_by_spf(p - 1, p, spf)
    exact_scan = scan[p]
    exact_minus_one = phi_X - 1
    exact_endpoint = phi_X - phi_endpoint
    density = density_less_than_p(primes, p)
    floor_endpoint_main = Fraction(X - p + 1, 1) * density
    continuous_n_axis_main = Fraction(N - p * p, p) * density
    return {
        "p": p,
        "X_floor_N_over_p": X,
        "phi_X": phi_X,
        "phi_p_minus_1": phi_endpoint,
        "endpoint_singleton_holds": phi_endpoint == 1,
        "scan_exact": exact_scan,
        "exact_minus_one": exact_minus_one,
        "exact_endpoint": exact_endpoint,
        "minus_one_matches_scan": exact_minus_one == exact_scan,
        "endpoint_matches_scan": exact_endpoint == exact_scan,
        "minus_one_and_endpoint_equivalent": exact_minus_one == exact_endpoint,
        "density": fraction_to_text(density),
        "floor_endpoint_main": float(floor_endpoint_main),
        "floor_endpoint_error": float(Fraction(exact_scan, 1) - floor_endpoint_main),
        "continuous_n_axis_main": float(continuous_n_axis_main),
        "continuous_n_axis_error": float(Fraction(exact_scan, 1) - continuous_n_axis_main),
        "continuous_n_axis_equals_exact": Fraction(exact_scan, 1) == continuous_n_axis_main,
    }


def audit_N(N: int) -> dict[str, Any]:
    """审计单个 N。"""
    spf = spf_table(N)
    primes = primes_upto_from_spf(spf)
    scan = bucket_counts_by_scan(N, spf)
    bucket_primes = [p for p in primes if p * p <= N]
    rows = [audit_bucket(N, p, primes, spf, scan) for p in bucket_primes]
    composite_count = sum(1 for n in range(4, N + 1) if spf[n] != n)
    exact_total = sum(row["scan_exact"] for row in rows)
    continuous_mismatch = [row["p"] for row in rows if not row["continuous_n_axis_equals_exact"]]
    return {
        "N": N,
        "sqrt_prime_bucket_count": len(bucket_primes),
        "composite_count": composite_count,
        "exact_lpf_bucket_total": exact_total,
        "exact_lpf_buckets_sum_to_composites": exact_total == composite_count,
        "all_endpoint_singletons_hold": all(row["endpoint_singleton_holds"] for row in rows),
        "all_minus_one_formulas_match_scan": all(row["minus_one_matches_scan"] for row in rows),
        "all_endpoint_formulas_match_scan": all(row["endpoint_matches_scan"] for row in rows),
        "all_minus_one_and_endpoint_forms_equivalent": all(
            row["minus_one_and_endpoint_equivalent"] for row in rows
        ),
        "continuous_n_axis_exact_for_all_buckets": all(
            row["continuous_n_axis_equals_exact"] for row in rows
        ),
        "first_continuous_n_axis_mismatch_prime": continuous_mismatch[0] if continuous_mismatch else None,
        "display_rows": [row for row in rows if row["p"] in DISPLAY_PRIMES],
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
        "certificate_type": "prime_matrix_phi_lpf_exact_bucket_endpoint_equivalence_audit",
        "status": "exact_lpf_bucket_endpoint_singleton_and_floor_boundary_fixed",
        "verified_date": "2026-05-25",
        "sample_N": SAMPLE_N,
        "correct_exact_formula_minus_one": "C_p(N)=Phi(floor(N/p); primes<p)-1",
        "correct_exact_formula_endpoint": "C_p(N)=Phi(floor(N/p); primes<p)-Phi(p-1; primes<p)",
        "endpoint_singleton_identity": "Phi(p-1; primes<p)=1",
        "continuous_main_not_exact_formula": "(N-p^2)*(1/p)*prod_{q<p}(1-1/q)",
        "exact_endpoint_singleton_fixed": all(audit["all_endpoint_singletons_hold"] for audit in audits),
        "minus_one_and_endpoint_forms_equivalent": all(
            audit["all_minus_one_and_endpoint_forms_equivalent"] for audit in audits
        ),
        "exact_lpf_bucket_identity_closed": all(
            audit["exact_lpf_buckets_sum_to_composites"]
            and audit["all_minus_one_formulas_match_scan"]
            and audit["all_endpoint_formulas_match_scan"]
            for audit in audits
        ),
        "continuous_euler_main_is_exact_count": all(
            audit["continuous_n_axis_exact_for_all_buckets"] for audit in audits
        ),
        "floor_endpoint_and_periodic_boundary_required": True,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "audits": audits,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "There is no conflict between the '-1' and '-Phi(p-1)' exact LPF bucket "
            "forms, because Phi(p-1; primes<p)=1. The real correction is to keep "
            "the floor, the endpoint singleton, and the primorial-periodic boundary "
            "term separate from the continuous Euler-product main. None of these "
            "unsigned identities supplies prime extraction across the parity barrier."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF exact bucket endpoint equivalence 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 修正后的精确公式层级",
        "",
        "两种精确写法完全等价：",
        "",
        "```text",
        "C_p(N)=Phi(floor(N/p); primes<p)-1",
        "      =Phi(floor(N/p); primes<p)-Phi(p-1; primes<p),",
        "Phi(p-1; primes<p)=1.",
        "```",
        "",
        "真正需要修正的是：不能把连续欧拉乘积主项当作精确计数。下面只是连续主项：",
        "",
        "```text",
        "(N-p^2)*(1/p)*prod_{q<p}(1-1/q).",
        "```",
        "",
        "精确计算必须保留 `floor(N/p)`、端点 singleton，以及上一轮证书中的 primorial 周期边界项。",
        "",
        "## 2. 全局读数",
        "",
        "```text",
        f"exact_endpoint_singleton_fixed={fmt_bool(payload['exact_endpoint_singleton_fixed'])}",
        f"minus_one_and_endpoint_forms_equivalent={fmt_bool(payload['minus_one_and_endpoint_forms_equivalent'])}",
        f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}",
        f"continuous_euler_main_is_exact_count={fmt_bool(payload['continuous_euler_main_is_exact_count'])}",
        f"floor_endpoint_and_periodic_boundary_required={fmt_bool(payload['floor_endpoint_and_periodic_boundary_required'])}",
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| N | exact total | composite count | endpoint singleton | endpoint formula | first continuous mismatch p |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| {N} | {exact_lpf_bucket_total} | {composite_count} | `{singleton}` | "
            "`{endpoint}` | {mismatch} |".format(
                singleton=fmt_bool(audit["all_endpoint_singletons_hold"]),
                endpoint=fmt_bool(audit["all_endpoint_formulas_match_scan"]),
                mismatch=audit["first_continuous_n_axis_mismatch_prime"],
                **audit,
            )
        )
    lines.extend(["", "## 3. 样本 bucket", ""])
    for audit in payload["audits"]:
        lines.extend(
            [
                f"### N={audit['N']}",
                "",
                "| p | scan exact | Phi(X)-1 | Phi(X)-Phi(p-1) | Phi(p-1) | continuous main | continuous error |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in audit["display_rows"]:
            lines.append(
                "| {p} | {scan_exact} | {exact_minus_one} | {exact_endpoint} | "
                "{phi_p_minus_1} | {continuous_n_axis_main:.6f} | "
                "{continuous_n_axis_error:.6f} |".format(**row)
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
    print(f"exact_endpoint_singleton_fixed={fmt_bool(payload['exact_endpoint_singleton_fixed'])}")
    print(
        "minus_one_and_endpoint_forms_equivalent="
        f"{fmt_bool(payload['minus_one_and_endpoint_forms_equivalent'])}"
    )
    print(f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}")
    print(
        "continuous_euler_main_is_exact_count="
        f"{fmt_bool(payload['continuous_euler_main_is_exact_count'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
