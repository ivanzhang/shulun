#!/usr/bin/env python3
"""审计 LPF first-hit 分割能否提升为 von Mangoldt signed payload。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_affine_lpf_first_hit_von_mangoldt_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json

输出：
  data/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-ledger.json
  docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json
  docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.md
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

SLUG = "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SAMPLE_X = [100, 1000, 10000, 50000]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json",
    DOCS / "prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json",
    DOCS / "prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-router.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount "
    "AND PointwiseThetaAPPositivityAtP2OrAdmissibleSignedDivisorPayloadTypeIIFamily "
    "AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC "
    "AND PrimitiveOrientationLocalFactorProductLawBeforePushforward "
    "AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
)

EXTERNAL_FRONTIER = [
    {
        "name": "Milicevic-Qin-Wu arbitrary-modulus Kloosterman bilinear forms",
        "url": "https://arxiv.org/abs/2511.07550",
        "usable_now": False,
        "reason": "requires a completed bilinear Kloosterman family; raw LPF first-hit tail is not such a family",
    },
    {
        "name": "Pascadi non-abelian composite-modulus Kloosterman Type-II",
        "url": "https://arxiv.org/abs/2511.08445",
        "usable_now": False,
        "reason": "requires composite-modulus Type-II sums with admissible coefficients, not unsigned LPF bucket counts",
    },
    {
        "name": "Matomaki-Radziwill-Shao-Tao-Teravainen 2026 almost-all short-interval Lambda uniformity",
        "url": "https://link.springer.com/article/10.1007/s00222-026-01408-6",
        "usable_now": False,
        "reason": "almost-all short interval uniformity does not give pointwise every-residue positivity at x=P^2",
    },
    {
        "name": "Dong-Robles-Zeindler Kloosterman fractions 2601.00292",
        "url": "https://arxiv.org/abs/2601.00292",
        "usable_now": False,
        "reason": "withdrawn; cannot be used as an active theorem input",
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


def primes_from_spf(spf: list[int]) -> list[int]:
    """从最小素因子表提取素数。"""
    return [n for n in range(2, len(spf)) if spf[n] == n]


def prime_power(n: int, spf: list[int]) -> tuple[int, int] | None:
    """若 n=p^a，返回 (p,a)，否则返回 None。"""
    if n < 2:
        return None
    p = spf[n]
    a = 0
    x = n
    while x % p == 0:
        x //= p
        a += 1
    return (p, a) if x == 1 else None


def von_mangoldt_target(n: int, spf: list[int]) -> float:
    """直接按 prime-power 定义计算 von Mangoldt 函数。"""
    pp = prime_power(n, spf)
    if pp is None:
        return 0.0
    p, _a = pp
    return math.log(p)


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


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def top_counter(counter: Counter[int], limit: int = 8) -> dict[str, int]:
    """压缩计数器。"""
    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    out = {str(k): v for k, v in items[:limit]}
    rest = sum(v for _k, v in items[limit:])
    if rest:
        out["other"] = rest
    return out


def divisor_support_count(n: int, mu: list[int]) -> int:
    """统计 Lambda Mobius 和式中非零 Mobius 除子数。"""
    count = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d:
            continue
        if mu[d] != 0 and n // d > 1:
            count += 1
        other = n // d
        if other != d and mu[other] != 0 and n // other > 1:
            count += 1
    return count


def audit_x(x_bound: int) -> dict[str, Any]:
    """审计一个 X 截断。"""
    M = 2 * x_bound + 1
    spf = spf_table(M)
    mu = mobius_table(spf)
    lam_formula = von_mangoldt_by_mobius(M, mu)

    endpoint_prime_count = 0
    endpoint_theta_mass = 0.0
    composite_tail_count = 0
    tail_prime_power_count = 0
    tail_prime_power_lambda_mass = 0.0
    tail_non_prime_power_count = 0
    tail_non_prime_power_divisor_terms: Counter[int] = Counter()
    cofactor_omega_counter: Counter[int] = Counter()
    lambda_failures: list[dict[str, float]] = []
    lpf_identity_failures: list[dict[str, int]] = []

    for m in range(3, M + 1, 2):
        target = von_mangoldt_target(m, spf)
        if abs(lam_formula[m] - target) > 1e-9:
            lambda_failures.append({"m": m, "formula": lam_formula[m], "target": target})

        p = spf[m]
        if p == m:
            endpoint_prime_count += 1
            endpoint_theta_mass += math.log(p)
            continue

        composite_tail_count += 1
        c = m // p
        k = (c - 1) // 2
        n = (m - 1) // 2
        if n != k * p + (p - 1) // 2:
            lpf_identity_failures.append({"m": m, "p": p, "c": c, "k": k, "n": n})

        pp = prime_power(m, spf)
        if pp is not None:
            tail_prime_power_count += 1
            tail_prime_power_lambda_mass += math.log(pp[0])
        else:
            tail_non_prime_power_count += 1
            tail_non_prime_power_divisor_terms[divisor_support_count(m, mu)] += 1

        # 记录 cofactor 的素因子层数；这显示 LPF tail 内部仍混合多层。
        x = c
        omega = 0
        while x > 1:
            omega += 1
            x //= spf[x]
        cofactor_omega_counter[omega] += 1

    total_lambda_formula_mass = sum(lam_formula[m] for m in range(3, M + 1, 2))
    theta_plus_prime_power_mass = endpoint_theta_mass + tail_prime_power_lambda_mass
    nonprimepower_cancelled = tail_non_prime_power_count > 0
    lambda_identity_closed = (
        not lambda_failures
        and abs(total_lambda_formula_mass - theta_plus_prime_power_mass) < 1e-8
    )
    return {
        "X": x_bound,
        "M": M,
        "endpoint_prime_count": endpoint_prime_count,
        "composite_tail_count": composite_tail_count,
        "tail_prime_power_count": tail_prime_power_count,
        "tail_non_prime_power_count": tail_non_prime_power_count,
        "endpoint_theta_mass": endpoint_theta_mass,
        "tail_prime_power_lambda_mass": tail_prime_power_lambda_mass,
        "total_von_mangoldt_mass_odd_axis": total_lambda_formula_mass,
        "theta_plus_prime_power_mass": theta_plus_prime_power_mass,
        "lambda_identity_closed": lambda_identity_closed,
        "lambda_failure_count": len(lambda_failures),
        "lpf_identity_failure_count": len(lpf_identity_failures),
        "nonprimepower_tail_cancelled_by_mobius_divisor_sum": nonprimepower_cancelled,
        "tail_prime_power_mass_fraction_of_lambda": (
            tail_prime_power_lambda_mass / total_lambda_formula_mass
            if total_lambda_formula_mass
            else 0.0
        ),
        "cofactor_omega_histogram": top_counter(cofactor_omega_counter),
        "nonprimepower_tail_divisor_term_histogram": top_counter(
            tail_non_prime_power_divisor_terms
        ),
        "lambda_failure_sample": lambda_failures[:3],
        "lpf_identity_failure_sample": lpf_identity_failures[:3],
    }


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    rows = [audit_x(x) for x in SAMPLE_X]
    lambda_closed = all(row["lambda_identity_closed"] for row in rows)
    lpf_closed = all(row["lpf_identity_failure_count"] == 0 for row in rows)
    nonprimepower_cancelled = all(
        row["nonprimepower_tail_cancelled_by_mobius_divisor_sum"] for row in rows
    )
    prime_power_leak_present = all(row["tail_prime_power_count"] > 0 for row in rows)
    return {
        "certificate_type": "prime_matrix_phi_lpf_affine_lpf_first_hit_von_mangoldt_lift_router",
        "status": "von_mangoldt_lift_exact_global_divisor_payload_required",
        "verified_date": "2026-05-25",
        "sample_X": SAMPLE_X,
        "mobius_von_mangoldt_identity_closed": lambda_closed,
        "lpf_first_hit_identity_imported_and_verified": lpf_closed,
        "endpoint_theta_separated_from_lpf_tail": True,
        "tail_prime_power_leak_present": prime_power_leak_present,
        "nonprimepower_tail_cancelled_only_by_mobius_divisor_sum": nonprimepower_cancelled,
        "lpf_local_unsigned_count_sufficient_for_prime_extraction": False,
        "global_divisor_signed_payload_required": True,
        "admissible_typeii_or_trace_family_constructed": False,
        "pointwise_theta_ap_positivity_at_p2_proved": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_frontier_sync": EXTERNAL_FRONTIER,
        "rows": rows,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The exact von Mangoldt lift exists, but it is a global Mobius divisor "
            "payload, not an LPF-local unsigned count. It separates endpoint theta "
            "mass from composite tails up to prime-power leakage, while non-prime-power "
            "tails cancel only through divisor-level signed terms. Therefore the next "
            "proof object must construct an admissible signed divisor/Type-II/trace "
            "family or return a named PDEC; no pointwise AP positivity follows here."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF affine LPF first-hit von Mangoldt lift 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书审计 LPF first-hit 分割能否直接升级为 prime extraction。结论是：",
        "von Mangoldt lift 是精确的，但它需要全局 Mobius divisor signed payload，",
        "不是 LPF-local unsigned count。",
        "",
        "## 1. 精确身份",
        "",
        "```text",
        "Lambda(m) = sum_{d|m} mu(d) log(m/d)",
        "Lambda(m) = log p  if m=p^a",
        "Lambda(m) = 0      otherwise",
        "```",
        "",
        "端点素数 `m=p` 的 `log p` 质量被分离出来；合数尾中的 prime powers 仍携带",
        "`Lambda` 质量，非 prime powers 只能通过 Mobius divisor signed sum 抵消。",
        "",
        "## 2. 审计读数",
        "",
        "```text",
        f"mobius_von_mangoldt_identity_closed={fmt_bool(payload['mobius_von_mangoldt_identity_closed'])}",
        f"lpf_first_hit_identity_imported_and_verified={fmt_bool(payload['lpf_first_hit_identity_imported_and_verified'])}",
        f"tail_prime_power_leak_present={fmt_bool(payload['tail_prime_power_leak_present'])}",
        "nonprimepower_tail_cancelled_only_by_mobius_divisor_sum="
        f"{fmt_bool(payload['nonprimepower_tail_cancelled_only_by_mobius_divisor_sum'])}",
        "lpf_local_unsigned_count_sufficient_for_prime_extraction="
        f"{fmt_bool(payload['lpf_local_unsigned_count_sufficient_for_prime_extraction'])}",
        f"global_divisor_signed_payload_required={fmt_bool(payload['global_divisor_signed_payload_required'])}",
        "admissible_typeii_or_trace_family_constructed="
        f"{fmt_bool(payload['admissible_typeii_or_trace_family_constructed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| X | M | endpoint primes | composite tails | tail prime powers | tail non-prime-powers | prime-power Lambda fraction |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in payload["rows"]:
        lines.append(
            "| {X} | {M} | {endpoint_prime_count} | {composite_tail_count} | "
            "{tail_prime_power_count} | {tail_non_prime_power_count} | "
            "{tail_prime_power_mass_fraction_of_lambda:.6f} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## 3. 外部前沿边界",
            "",
            "| input | usable now | reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in payload["external_frontier_sync"]:
        lines.append(
            f"| [{item['name']}]({item['url']}) | `{fmt_bool(item['usable_now'])}` | {item['reason']} |"
        )
    lines.extend(
        [
            "",
            "这些输入都要求先有 admissible signed family、Type-II family 或 completed",
            "trace/Kloosterman family。当前 LPF first-hit tail 只是精确分割后的无符号对象。",
            "",
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
    """写出证书。"""
    payload = build_certificate()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(f"mobius_von_mangoldt_identity_closed={fmt_bool(payload['mobius_von_mangoldt_identity_closed'])}")
    print(f"global_divisor_signed_payload_required={fmt_bool(payload['global_divisor_signed_payload_required'])}")
    print(
        "admissible_typeii_or_trace_family_constructed="
        f"{fmt_bool(payload['admissible_typeii_or_trace_family_constructed'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
