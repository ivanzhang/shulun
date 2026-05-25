#!/usr/bin/env python3
"""审计 LPF 分桶的 inclusive survival 修正版公式。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_lpf_bucket_inclusive_survival_formula_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json

输出：
  data/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-ledger.json
  docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json
  docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.md
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

SLUG = "prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_N = [100, 1000, 10000, 100000]
DISPLAY_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json",
    DOCS / "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "PrimeDivisibilityClassIsOneOverPNotOneMinusOneOverP "
    "AND ExactLPFBucketCountIsLegendrePhiNotInclusiveSurvivalProduct "
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
    """精确计算 Phi(x; primes<p)。"""
    if x <= 0:
        return 0
    return sum(1 for m in range(1, x + 1) if m == 1 or spf[m] >= p)


def exact_lpf_bucket_count(N: int, p: int, spf: list[int]) -> int:
    """精确计数 composite n<=N 且 LPF(n)=p。"""
    return max(0, rough_count_by_spf(N // p, p, spf) - 1)


def bucket_counts_by_scan(N: int, spf: list[int]) -> Counter[int]:
    """直接扫描复合数的 LPF 分桶。"""
    counts: Counter[int] = Counter()
    for n in range(4, N + 1):
        p = spf[n]
        if p != n:
            counts[p] += 1
    return counts


def density_less_than_p(primes: list[int], p: int) -> Fraction:
    """避开所有 q<p 的零类密度。"""
    density = Fraction(1, 1)
    for q in primes:
        if q >= p:
            break
        density *= Fraction(q - 1, q)
    return density


def correct_n_axis_main(N: int, p: int, primes: list[int]) -> float:
    """n 轴正确主项: (N-p^2)*(1/p)*prod_{q<p}(1-1/q)。"""
    if p * p > N:
        return 0.0
    return float(Fraction(N - p * p, p) * density_less_than_p(primes, p))


def user_inclusive_survival_main(N: int, p: int, primes: list[int]) -> float:
    """用户修正版: (N-p^2)*prod_{q<=p}(1-1/q)。"""
    if p * p > N:
        return 0.0
    density = density_less_than_p(primes, p) * Fraction(p - 1, p)
    return float(Fraction(N - p * p) * density)


def correct_density_factor(primes: list[int], p: int) -> str:
    """正确 n 轴密度因子。"""
    factor = Fraction(1, p) * density_less_than_p(primes, p)
    return f"{factor.numerator}/{factor.denominator}"


def user_density_factor(primes: list[int], p: int) -> str:
    """用户修正版密度因子。"""
    factor = Fraction(p - 1, p) * density_less_than_p(primes, p)
    return f"{factor.numerator}/{factor.denominator}"


def audit_N(N: int) -> dict[str, Any]:
    """审计单个 N。"""
    spf = spf_table(N)
    primes = primes_upto_from_spf(spf)
    scan = bucket_counts_by_scan(N, spf)
    bucket_primes = [p for p in primes if p * p <= N]

    exact_total = 0
    correct_total = 0.0
    user_total = 0.0
    mismatch_count = 0
    first_user_wrong_prime = None
    rows = []

    for p in bucket_primes:
        exact = exact_lpf_bucket_count(N, p, spf)
        if exact != scan[p]:
            mismatch_count += 1
        correct = correct_n_axis_main(N, p, primes)
        user = user_inclusive_survival_main(N, p, primes)
        exact_total += exact
        correct_total += correct
        user_total += user
        if p >= 3 and first_user_wrong_prime is None and abs(user - correct) > 1e-12:
            first_user_wrong_prime = p
        if p in DISPLAY_PRIMES:
            rows.append(
                {
                    "p": p,
                    "exact": exact,
                    "correct_density": correct_density_factor(primes, p),
                    "correct_main": correct,
                    "user_density": user_density_factor(primes, p),
                    "user_main": user,
                    "user_over_correct_main": user / correct if correct else None,
                    "user_over_exact": user / exact if exact else None,
                }
            )

    composite_count = sum(1 for n in range(4, N + 1) if spf[n] != n)
    return {
        "N": N,
        "sqrt_prime_bucket_count": len(bucket_primes),
        "composite_count": composite_count,
        "exact_lpf_bucket_total": exact_total,
        "exact_lpf_buckets_sum_to_composites": exact_total == composite_count,
        "exact_phi_formula_mismatch_count": mismatch_count,
        "correct_n_axis_total": correct_total,
        "user_inclusive_survival_total": user_total,
        "correct_total_over_exact": correct_total / exact_total if exact_total else 0.0,
        "user_total_over_exact": user_total / exact_total if exact_total else 0.0,
        "first_user_formula_wrong_prime": first_user_wrong_prime,
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
        "certificate_type": "prime_matrix_phi_lpf_lpf_bucket_inclusive_survival_formula_audit",
        "status": "prime_divisibility_class_is_one_over_p_not_one_minus_one_over_p",
        "verified_date": "2026-05-25",
        "sample_N": SAMPLE_N,
        "exact_formula": "C_p(N)=Phi(floor(N/p); primes<p)-1",
        "correct_n_axis_main": "(N-p^2)*(1/p)*prod_{q<p}(1-1/q)",
        "user_inclusive_survival_formula": "(N-p^2)*prod_{q<=p}(1-1/q)",
        "first_structural_wrong_prime": 3,
        "reason_user_formula_fails": (
            "For q<p the LPF bucket survives nonzero classes. For p itself the "
            "bucket requires the zero class n=0 mod p, whose density is 1/p, "
            "not the nonzero-class density 1-1/p."
        ),
        "exact_lpf_bucket_identity_closed": all(
            audit["exact_lpf_buckets_sum_to_composites"]
            and audit["exact_phi_formula_mismatch_count"] == 0
            for audit in audits
        ),
        "inclusive_survival_formula_supported": False,
        "correct_n_axis_main_supported_as_continuous_main": True,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "audits": audits,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The revised formula fixes the survival factors for primes q<p, but "
            "it treats p itself as another survival prime. LPF(n)=p instead "
            "requires divisibility by p. Thus the p-factor is 1/p, not 1-1/p. "
            "The exact identity remains a Legendre-Phi rough-number count and "
            "stays parity-blind without a signed divisor payload."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF LPF bucket inclusive survival formula 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 结论",
        "",
        "修正版已经把小素数 `q<p` 的生存密度改为 `1-1/q`，这是正确方向。",
        "但 `p` 本身不能继续乘 `1-1/p`。在 `LPF(n)=p` 的 bucket 中，",
        "`n` 必须满足 `n=0 mod p`，所以 `p` 这一层的密度是 `1/p`。",
        "",
        "精确公式仍是：",
        "",
        "```text",
        "C_p(N)=#{n<=N composite : LPF(n)=p}",
        "      =Phi(floor(N/p); primes<p)-1.",
        "```",
        "",
        "正确的 n 轴连续主项是：",
        "",
        "```text",
        "(N-p^2)*(1/p)*prod_{q<p}(1-1/q).",
        "```",
        "",
        "用户修正版为：",
        "",
        "```text",
        "(N-p^2)*prod_{q<=p}(1-1/q),",
        "```",
        "",
        "二者相差因子 `p-1`。因此只在 `p=2` 偶然相同，从 `p=3` 起系统性高估。",
        "",
        "## 2. 全局读数",
        "",
        "```text",
        f"exact_lpf_bucket_identity_closed={fmt_bool(payload['exact_lpf_bucket_identity_closed'])}",
        f"inclusive_survival_formula_supported={fmt_bool(payload['inclusive_survival_formula_supported'])}",
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| N | exact total | composite count | correct total/exact | user total/exact | first wrong p |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| {N} | {exact_lpf_bucket_total} | {composite_count} | "
            "{correct_total_over_exact:.6f} | {user_total_over_exact:.6f} | "
            "{first_user_formula_wrong_prime} |".format(**audit)
        )
    lines.extend(["", "## 3. 样本 bucket", ""])
    for audit in payload["audits"]:
        lines.extend(
            [
                f"### N={audit['N']}",
                "",
                "| p | exact | correct density | correct main | user density | user main | user/correct |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in audit["display_rows"]:
            lines.append(
                "| {p} | {exact} | {correct_density} | {correct_main:.6f} | "
                "{user_density} | {user_main:.6f} | {user_over_correct_main:.6f} |".format(**row)
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
    print(f"inclusive_survival_formula_supported={fmt_bool(payload['inclusive_survival_formula_supported'])}")
    print(
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
