#!/usr/bin/env python3
"""审计 von Mangoldt lift 的 LPF 纯素幂压缩口径。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_von_mangoldt_pure_power_compression_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json

输出：
  data/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-ledger.json
  docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json
  docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.md
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

SLUG = "prime-matrix-phi-lpf-von-mangoldt-pure-power-compression"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_X = [100, 1000, 10000, 50000, 100000]
DISPLAY_X = [100, 1000, 10000, 100000]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json",
    DOCS / "prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json",
    DOCS / "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json",
    DOCS / "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "LPFPurePowerVonMangoldtCompressionClosed "
    "AND PrimePowerTailSeparated "
    "AND PurePowerSelectorNotAnAdditiveSignedDistributionFamily "
    "AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen"
)

EXTERNAL_FRONTIER = [
    {
        "name": "Milicevic-Qin-Wu arbitrary-modulus Kloosterman bilinear forms",
        "url": "https://arxiv.org/abs/2511.07550",
        "role_after_this_audit": (
            "power-saving bilinear Kloosterman input; it becomes relevant only after "
            "the LPF layer supplies an actual bilinear trace family"
        ),
        "direct_close": False,
    },
    {
        "name": "Zheng simultaneous arithmetic progressions",
        "url": "https://arxiv.org/abs/2512.22798",
        "role_after_this_audit": (
            "mean-value input for two simultaneous AP constraints only after the "
            "LPF pure-power selector has been replaced by an admissible signed family"
        ),
        "direct_close": False,
    },
    {
        "name": "Runbo Li large-modulus AP primes and Harman sieve refinements",
        "url": "https://arxiv.org/abs/2602.20917",
        "role_after_this_audit": (
            "average-modulus prime distribution input; does not give pointwise every-row "
            "theta positivity at the P^2 scale"
        ),
        "direct_close": False,
    },
    {
        "name": "Wright trilinear Kloosterman fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "role_after_this_audit": (
            "usable only after a trilinear convolution with equidistributed coefficients "
            "is constructed"
        ),
        "direct_close": False,
    },
    {
        "name": "Pascadi non-abelian composite-modulus Kloosterman Type-II",
        "url": "https://arxiv.org/abs/2511.08445",
        "role_after_this_audit": (
            "requires a genuine Type-II Kloosterman family over composite moduli, not "
            "a nonlinear pure-power selector"
        ),
        "direct_close": False,
    },
    {
        "name": "Becker-Breuillard spectral gaps and anti-concentration",
        "url": "https://arxiv.org/abs/2512.15364",
        "role_after_this_audit": (
            "requires a finite-group orbit or random-walk model before spectral gap "
            "anti-concentration can be applied"
        ),
        "direct_close": False,
    },
    {
        "name": "Matomaki-Radziwill-Shao-Tao-Teravainen almost-all short-interval uniformity",
        "url": "https://link.springer.com/article/10.1007/s00222-026-01408-6",
        "role_after_this_audit": (
            "almost-all short-interval Lambda uniformity; not a pointwise AP positivity "
            "theorem for each prime-matrix row"
        ),
        "direct_close": False,
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


def mobius_table(spf: list[int]) -> list[int]:
    """由最小素因子表计算 Mobius 函数。"""
    mu = [0] * len(spf)
    if len(mu) > 1:
        mu[1] = 1
    for n in range(2, len(spf)):
        x = n
        last = 0
        omega = 0
        squarefree = True
        while x > 1:
            p = spf[x]
            x //= p
            if p == last:
                squarefree = False
                break
            last = p
            omega += 1
        mu[n] = 0 if not squarefree else (-1 if omega % 2 else 1)
    return mu


def von_mangoldt_by_mobius(limit: int, mu: list[int]) -> list[float]:
    """用 Lambda(n)=sum_{d|n} mu(d) log(n/d) 计算。"""
    lam = [0.0] * (limit + 1)
    for d in range(1, limit + 1):
        if mu[d] == 0:
            continue
        coeff = mu[d]
        for n in range(d, limit + 1, d):
            q = n // d
            if q > 1:
                lam[n] += coeff * math.log(q)
    return lam


def strip_lpf_power(n: int, spf: list[int]) -> tuple[int, int, int]:
    """剥离最小素因子 p 的全部幂，返回 p、指数和剩余 cofactor。"""
    if n < 2:
        return (0, 0, n)
    p = spf[n]
    exponent = 0
    rest = n
    while rest % p == 0:
        rest //= p
        exponent += 1
    return p, exponent, rest


def lambda_by_lpf_pure_power(n: int, spf: list[int]) -> float:
    """LPF 纯素幂压缩：剩余 cofactor 为 1 时给 log(p)，否则为 0。"""
    p, _exponent, rest = strip_lpf_power(n, spf)
    return math.log(p) if rest == 1 else 0.0


def prime_power_kind(n: int, spf: list[int]) -> str:
    """给出 LPF 纯素幂分类。"""
    p, exponent, rest = strip_lpf_power(n, spf)
    if rest != 1:
        return "mixed_composite"
    if exponent == 1 and p == n:
        return "prime_endpoint"
    return "composite_prime_power"


def top_counter(counter: Counter[int], limit: int = 8) -> dict[str, int]:
    """压缩计数器，保留最大若干项。"""
    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    shown = {str(key): value for key, value in items[:limit]}
    rest = sum(value for _key, value in items[limit:])
    if rest:
        shown["other"] = rest
    return shown


def audit_x(x_bound: int) -> dict[str, Any]:
    """审计 odd axis m<=2X+1 上的 LPF 纯素幂压缩。"""
    M = 2 * x_bound + 1
    spf = spf_table(M)
    mu = mobius_table(spf)
    lam_mobius = von_mangoldt_by_mobius(M, mu)

    counts: Counter[str] = Counter()
    owner_prime_power_counter: Counter[int] = Counter()
    owner_mixed_counter: Counter[int] = Counter()
    exponent_counter: Counter[int] = Counter()
    failures: list[dict[str, Any]] = []
    endpoint_theta_mass = 0.0
    composite_prime_power_mass = 0.0
    mixed_abs_mobius_residual = 0.0

    for m in range(3, M + 1, 2):
        kind = prime_power_kind(m, spf)
        counts[kind] += 1
        p, exponent, rest = strip_lpf_power(m, spf)
        compressed = lambda_by_lpf_pure_power(m, spf)
        if abs(compressed - lam_mobius[m]) > 1e-9:
            failures.append(
                {
                    "m": m,
                    "mobius_lambda": lam_mobius[m],
                    "lpf_pure_power_lambda": compressed,
                    "owner_p": p,
                    "owner_exponent": exponent,
                    "residual_after_owner_power": rest,
                }
            )

        if kind == "prime_endpoint":
            endpoint_theta_mass += compressed
        elif kind == "composite_prime_power":
            composite_prime_power_mass += compressed
            owner_prime_power_counter[p] += 1
            exponent_counter[exponent] += 1
        else:
            owner_mixed_counter[p] += 1
            mixed_abs_mobius_residual += abs(lam_mobius[m])

    total_lambda_mass = sum(lam_mobius[m] for m in range(3, M + 1, 2))
    reconstructed_mass = endpoint_theta_mass + composite_prime_power_mass
    tail_fraction = (
        composite_prime_power_mass / total_lambda_mass if total_lambda_mass else 0.0
    )
    mixed_count = counts["mixed_composite"]
    return {
        "X": x_bound,
        "M": M,
        "odd_axis_count": x_bound,
        "prime_endpoint_count": counts["prime_endpoint"],
        "composite_prime_power_count": counts["composite_prime_power"],
        "mixed_composite_count": mixed_count,
        "endpoint_theta_mass": endpoint_theta_mass,
        "composite_prime_power_lambda_mass": composite_prime_power_mass,
        "total_lambda_mass_odd_axis": total_lambda_mass,
        "reconstructed_lambda_mass": reconstructed_mass,
        "prime_power_tail_mass_fraction": tail_fraction,
        "mixed_composite_mobius_residual_abs_sum": mixed_abs_mobius_residual,
        "lpf_pure_power_matches_mobius_lambda": not failures,
        "lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail": (
            abs(total_lambda_mass - reconstructed_mass) < 1e-8
        ),
        "mixed_composites_cancel_to_zero_pointwise": mixed_abs_mobius_residual < 1e-8,
        "top_composite_prime_power_owners": top_counter(owner_prime_power_counter),
        "top_mixed_composite_owners": top_counter(owner_mixed_counter),
        "composite_prime_power_exponents": top_counter(exponent_counter),
        "sample_failures": failures[:5],
    }


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    audits = [audit_x(x_bound) for x_bound in SAMPLE_X]
    return {
        "certificate_type": "prime_matrix_phi_lpf_von_mangoldt_pure_power_compression_audit",
        "status": "lpf_pure_power_von_mangoldt_compression_closed_but_not_distribution_family",
        "verified_date": "2026-05-26",
        "sample_X": SAMPLE_X,
        "exact_identity": "Lambda(m)=log(LPF(m)) if m is a power of LPF(m), else 0",
        "mobius_identity": "Lambda(m)=sum_{d|m} mu(d) log(m/d)",
        "lpf_pure_power_compression_closed": all(
            audit["lpf_pure_power_matches_mobius_lambda"] for audit in audits
        ),
        "lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail": all(
            audit["lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail"]
            for audit in audits
        ),
        "mixed_composites_cancel_to_zero_pointwise": all(
            audit["mixed_composites_cancel_to_zero_pointwise"] for audit in audits
        ),
        "prime_power_tail_separated": True,
        "pure_power_selector_is_nonlinear_factorization_predicate": True,
        "pure_power_selector_supplies_additive_signed_distribution_family": False,
        "pointwise_ap_theta_lower_bound_proved": False,
        "admissible_typeii_or_trace_family_constructed": False,
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "audits": audits,
        "external_frontier_checked_date": "2026-05-26",
        "external_frontier": EXTERNAL_FRONTIER,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The pointwise von Mangoldt lift can be compressed from the full Mobius "
            "divisor cube to the LPF pure-power selector: strip all powers of the "
            "owner prime p=LPF(m); Lambda(m) is log p exactly when the residual is 1. "
            "This corrects an over-strong reading that the pointwise identity must "
            "always be kept as a global divisor sum. However, the pure-power selector "
            "is a nonlinear factorization predicate and not an additive signed "
            "Type-II, trace, or AP distribution family. Therefore it does not by "
            "itself close prime extraction or the Phi-LPF parity barrier."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF von Mangoldt pure-power compression 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 修正后的 lift 口径",
        "",
        "全局 Mobius 除子和式仍是可线性平均的标准形式：",
        "",
        "```text",
        payload["mobius_identity"],
        "```",
        "",
        "但点态恒等式可以被 LPF 剥离压缩为：",
        "",
        "```text",
        payload["exact_identity"],
        "```",
        "",
        "也就是说，令 `p=LPF(m)`，把 `p` 的全部幂从 `m` 中剥掉；若剩余为 `1`，",
        "则 `m=p^a` 且 `Lambda(m)=log p`，否则 `Lambda(m)=0`。",
        "",
        "这修正了“点态 lift 必须保持完整全局 divisor cube”的过强表述；真正不能省略的是",
        "可平均的 signed distribution family。LPF 纯素幂选择器是非线性因子分解谓词，不是",
        "Type-II/trace/AP 平均可直接调用的加性有符号族。",
        "",
        "## 2. 全局读数",
        "",
        "```text",
        f"lpf_pure_power_compression_closed={fmt_bool(payload['lpf_pure_power_compression_closed'])}",
        "lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail="
        f"{fmt_bool(payload['lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail'])}",
        f"mixed_composites_cancel_to_zero_pointwise={fmt_bool(payload['mixed_composites_cancel_to_zero_pointwise'])}",
        f"prime_power_tail_separated={fmt_bool(payload['prime_power_tail_separated'])}",
        "pure_power_selector_supplies_additive_signed_distribution_family="
        f"{fmt_bool(payload['pure_power_selector_supplies_additive_signed_distribution_family'])}",
        f"pointwise_ap_theta_lower_bound_proved={fmt_bool(payload['pointwise_ap_theta_lower_bound_proved'])}",
        "admissible_typeii_or_trace_family_constructed="
        f"{fmt_bool(payload['admissible_typeii_or_trace_family_constructed'])}",
        "unsigned_lpf_bucket_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['unsigned_lpf_bucket_count_sufficient_for_prime_extraction'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| X | M=2X+1 | endpoint primes | composite prime powers | mixed composites | prime-power Lambda fraction |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for audit in payload["audits"]:
        if audit["X"] not in DISPLAY_X:
            continue
        lines.append(
            "| {X} | {M} | {prime_endpoint_count} | {composite_prime_power_count} | "
            "{mixed_composite_count} | {prime_power_tail_mass_fraction:.6f} |".format(
                **audit
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最大样本局部结构",
            "",
        ]
    )
    last = payload["audits"][-1]
    lines.extend(
        [
            f"`X={last['X']}` 的 composite prime-power owner：",
            "",
            "```text",
            ", ".join(f"{k}:{v}" for k, v in last["top_composite_prime_power_owners"].items()),
            "```",
            "",
            "对应 exponent 分布：",
            "",
            "```text",
            ", ".join(f"{k}:{v}" for k, v in last["composite_prime_power_exponents"].items()),
            "```",
            "",
            "mixed composite 的主要 owner bucket：",
            "",
            "```text",
            ", ".join(f"{k}:{v}" for k, v in last["top_mixed_composite_owners"].items()),
            "```",
            "",
            "## 4. 外部前沿重新定位",
            "",
            "| input | direct close | role after this audit |",
            "| --- | --- | --- |",
        ]
    )
    for item in payload["external_frontier"]:
        lines.append(
            f"| [{item['name']}]({item['url']}) | `{fmt_bool(item['direct_close'])}` | "
            f"{item['role_after_this_audit']} |"
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
    """生成证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(
        "lpf_pure_power_compression_closed="
        f"{fmt_bool(payload['lpf_pure_power_compression_closed'])}"
    )
    print(
        "pure_power_selector_supplies_additive_signed_distribution_family="
        f"{fmt_bool(payload['pure_power_selector_supplies_additive_signed_distribution_family'])}"
    )
    print(
        "pointwise_ap_theta_lower_bound_proved="
        f"{fmt_bool(payload['pointwise_ap_theta_lower_bound_proved'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
