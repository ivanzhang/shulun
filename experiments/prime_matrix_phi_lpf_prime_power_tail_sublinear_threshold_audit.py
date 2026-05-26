#!/usr/bin/env python3
"""审计 Prime Matrix strict row 中素幂尾巴的次线性阈值。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_prime_power_tail_sublinear_threshold_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json

输出：
  data/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-ledger.json
  docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json
  docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_PRIMES = [31, 101, 251, 1009, 3001, 10007]
ASYMPTOTIC_CHECK_POINTS = [10**3, 10**4, 10**6, 10**8, 10**12]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json",
    DOCS / "prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json",
    DOCS / "prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json",
    DOCS / "prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "LPFPurePowerVonMangoldtCompressionClosed "
    "AND PrimePowerTailAbsorptionThresholdClosed "
    "AND PrimePowerTailSublinearThresholdClosed "
    "AND NeedPointwisePsiRowPositiveProportionAtSqrtScale "
    "AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def sieve_primes(limit: int) -> list[int]:
    """返回不超过 limit 的素数列表。"""
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [n for n in range(2, limit + 1) if is_prime[n]]


def is_prime(n: int) -> bool:
    """小规模确定性素性测试。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def integer_nth_root_floor(n: int, a: int) -> int:
    """返回 floor(n^(1/a))，用整数校正避免浮点边界误差。"""
    if n < 0:
        raise ValueError("n must be nonnegative")
    if n <= 1:
        return n
    guess = int(round(n ** (1.0 / a)))
    while (guess + 1) ** a <= n:
        guess += 1
    while guess**a > n:
        guess -= 1
    return guess


def row_integer_root_count_bound(P: int, k: int) -> int:
    """上一层整数根上界中的未加权 base-count。"""
    upper = (k + 1) * P - 1
    lower = k * P
    max_a = int(math.log2(upper))
    total = 0
    for a in range(2, max_a + 1):
        hi = integer_nth_root_floor(upper, a)
        lo = integer_nth_root_floor(lower, a)
        total += max(0, hi - lo)
    return total


def global_sublinear_count_bound(P: int) -> float:
    """对所有 strict rows 统一有效的解析 base-count 上界。

    对 a=2 用最左行的平方根差；对 a>=3 用凹函数差分在最左行最大这一事实。
    这里保留每个指数的 floor 误差 +1，得到完全显式的 o(P) 口径。
    """
    max_a = int(math.log2(P * P - 1))
    square_shell = (math.sqrt(2.0) - 1.0) * math.sqrt(P) + 1.0
    if max_a <= 2:
        return square_shell
    high_power_shell = (2.0 ** (1.0 / 3.0) - 1.0) * (P ** (1.0 / 3.0)) + 1.0
    return square_shell + (max_a - 2) * high_power_shell


def generate_prime_power_tail_by_row(P: int) -> list[dict[str, Any]]:
    """生成每行合数素幂尾巴的实际质量。"""
    rows: list[dict[str, Any]] = [
        {
            "k": k,
            "prime_power_tail_count": 0,
            "prime_power_tail_mass": 0.0,
            "prime_power_items_sample": [],
        }
        for k in range(1, P)
    ]
    primes = sieve_primes(P - 1)
    upper_limit = P * P
    for p in primes:
        value = p * p
        exponent = 2
        while value < upper_limit:
            k = value // P
            if 1 <= k < P and value % P != 0:
                row = rows[k - 1]
                row["prime_power_tail_count"] += 1
                row["prime_power_tail_mass"] += math.log(p)
                if len(row["prime_power_items_sample"]) < 6:
                    row["prime_power_items_sample"].append(f"{value}={p}^{exponent}")
            value *= p
            exponent += 1
    return rows


def audit_prime(P: int) -> dict[str, Any]:
    """审计一个 prime P 的素幂尾巴次线性阈值。"""
    if not is_prime(P):
        raise ValueError(f"sample P must be prime: {P}")

    row_payloads = generate_prime_power_tail_by_row(P)
    sublinear_count = global_sublinear_count_bound(P)
    sublinear_mass = sublinear_count * math.log(P)
    all_root_bounds_ok = True
    all_sublinear_bounds_ok = True

    for row in row_payloads:
        k = row["k"]
        root_count = row_integer_root_count_bound(P, k)
        root_mass = root_count * math.log(P)
        row["integer_root_count_bound"] = root_count
        row["integer_root_mass_bound"] = root_mass
        row["global_sublinear_mass_bound"] = sublinear_mass
        row["tail_over_P"] = row["prime_power_tail_mass"] / P
        row["integer_root_bound_over_P"] = root_mass / P
        row["global_sublinear_bound_over_P"] = sublinear_mass / P
        row["root_bound_ok"] = row["prime_power_tail_mass"] <= root_mass + 1e-12
        row["sublinear_bound_ok"] = row["prime_power_tail_mass"] <= sublinear_mass + 1e-12
        all_root_bounds_ok = all_root_bounds_ok and row["root_bound_ok"]
        all_sublinear_bounds_ok = all_sublinear_bounds_ok and row["sublinear_bound_ok"]

    max_tail_row = max(row_payloads, key=lambda row: row["prime_power_tail_mass"])
    max_root_bound_row = max(row_payloads, key=lambda row: row["integer_root_mass_bound"])
    return {
        "P": P,
        "strict_row_count": P - 1,
        "global_sublinear_count_bound": sublinear_count,
        "global_sublinear_mass_bound": sublinear_mass,
        "global_sublinear_bound_over_P": sublinear_mass / P,
        "max_actual_tail_row": max_tail_row,
        "max_integer_root_bound_row": max_root_bound_row,
        "actual_tail_bound_all_rows": all_root_bounds_ok,
        "sublinear_tail_bound_all_rows": all_sublinear_bounds_ok,
        "positive_proportion_needed_by_global_bound": sublinear_mass / P,
    }


def asymptotic_bound_table() -> list[dict[str, Any]]:
    """记录解析阈值随 P 增长下降到 0 的数值趋势。"""
    rows = []
    for P in ASYMPTOTIC_CHECK_POINTS:
        count_bound = global_sublinear_count_bound(P)
        mass_bound = count_bound * math.log(P)
        rows.append(
            {
                "P": P,
                "global_sublinear_count_bound": count_bound,
                "global_sublinear_mass_bound": mass_bound,
                "global_sublinear_bound_over_P": mass_bound / P,
            }
        )
    return rows


def external_thresholds() -> list[dict[str, Any]]:
    """把外部前沿输入翻译成 strict-row 所需尺度。"""
    return [
        {
            "name": "Runbo Li short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            "input_shape": "every sufficiently large interval of length x^0.52 contains primes",
            "at_x_equals_P_squared": "requires length P^1.04",
            "row_length": "P = x^0.5",
            "closes_strict_row": False,
            "reason": "exponent 0.52 remains above the square-root row exponent 0.5",
        },
        {
            "name": "Runbo Li large-modulus AP/Harman",
            "source": "https://arxiv.org/abs/2602.20917",
            "input_shape": "Bombieri--Vinogradov type mean values for large moduli",
            "at_x_equals_P_squared": "averaged moduli/residue information",
            "row_length": "single fixed row and residue load",
            "closes_strict_row": False,
            "reason": "average large-modulus information is not a zero-exception rowwise psi lower bound",
        },
        {
            "name": "Milicevic-Qin-Wu bilinear Kloosterman",
            "source": "https://arxiv.org/abs/2511.07550",
            "input_shape": "power-saving bilinear Kloosterman forms modulo arbitrary q",
            "at_x_equals_P_squared": "usable after constructing a true bilinear trace family",
            "row_length": "not directly a psi interval lower bound",
            "closes_strict_row": False,
            "reason": "the project still lacks an admissible signed Type-II/trace family",
        },
        {
            "name": "Pascadi composite-modulus Type-II Kloosterman",
            "source": "https://arxiv.org/abs/2511.08445",
            "input_shape": "non-abelian amplification for composite-modulus Kloosterman Type-II sums",
            "at_x_equals_P_squared": "candidate once a composite-modulus coefficient family exists",
            "row_length": "not directly a psi interval lower bound",
            "closes_strict_row": False,
            "reason": "coefficient family and return-to-row load are not constructed",
        },
        {
            "name": "Wright trilinear Kloosterman fractions",
            "source": "https://arxiv.org/abs/2604.25177",
            "input_shape": "unbalanced convolution estimates with equidistributed beta sequence",
            "at_x_equals_P_squared": "candidate for trilinear trace routing",
            "row_length": "not directly a psi interval lower bound",
            "closes_strict_row": False,
            "reason": "requires a trilinear convolution with the paper's distribution hypotheses",
        },
    ]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    audits = [audit_prime(P) for P in SAMPLE_PRIMES]
    asymptotic_rows = asymptotic_bound_table()
    return {
        "certificate_type": "prime_matrix_phi_lpf_prime_power_tail_sublinear_threshold_audit",
        "status": "prime_power_tail_is_sublinear_but_pointwise_psi_sqrt_window_still_open",
        "verified_date": "2026-05-26",
        "sample_primes": SAMPLE_PRIMES,
        "row_interval": "I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P",
        "sublinear_tail_bound": (
            "prime_power_tail(I_{P,k}) <= log(P)*((sqrt(2)-1)*sqrt(P)+1+"
            "(floor(log2(P^2-1))-2)*((2^(1/3)-1)*P^(1/3)+1))"
        ),
        "asymptotic_tail_statement": (
            "prime_power_tail(I_{P,k}) = O(sqrt(P)*log(P)+P^(1/3)*log(P)^2)=o(P)"
        ),
        "positive_proportion_closure_contract": (
            "Any rowwise lower bound psi(I_{P,k}) >= eta*P for fixed eta>0 "
            "would exceed the prime-power tail for all sufficiently large P."
        ),
        "actual_tail_bound_all_samples": all(audit["actual_tail_bound_all_rows"] for audit in audits),
        "sublinear_tail_bound_all_samples": all(
            audit["sublinear_tail_bound_all_rows"] for audit in audits
        ),
        "prime_power_tail_sublinear_threshold_closed": True,
        "positive_proportion_psi_would_close_rows_eventually": True,
        "known_short_interval_input_reaches_sqrt_window": False,
        "pointwise_psi_row_positive_proportion_proved": False,
        "admissible_signed_typeii_or_trace_family_constructed": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "audits": audits,
        "asymptotic_bound_table": asymptotic_rows,
        "external_thresholds": external_thresholds(),
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The LPF exact-count corrections leave no half-main Euler-product error to exploit. "
            "After the von Mangoldt pure-power compression, the only difference between psi "
            "and theta in a strict row is a composite prime-power tail. This certificate "
            "shows that the tail is uniformly o(P), so any fixed positive-proportion "
            "rowwise psi lower bound would absorb it. Current short-interval, AP-average, "
            "Kloosterman, and spectral inputs still do not supply that pointwise square-root "
            "scale lower bound or an admissible signed Type-II/trace family."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF prime-power tail sublinear threshold 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 解析压缩",
        "",
        "对 strict row",
        "",
        "```text",
        payload["row_interval"],
        "```",
        "",
        "上一层已证明：",
        "",
        "```text",
        "theta(I_{P,k})>0 iff psi(I_{P,k})>prime_power_tail(I_{P,k})",
        "```",
        "",
        "本层把尾巴进一步压成统一次线性阈值：",
        "",
        "```text",
        payload["sublinear_tail_bound"],
        payload["asymptotic_tail_statement"],
        "```",
        "",
        "因此新的闭合合同是：",
        "",
        "```text",
        payload["positive_proportion_closure_contract"],
        "```",
        "",
        "## 2. 样本审计",
        "",
        "```text",
        f"actual_tail_bound_all_samples={fmt_bool(payload['actual_tail_bound_all_samples'])}",
        f"sublinear_tail_bound_all_samples={fmt_bool(payload['sublinear_tail_bound_all_samples'])}",
        "prime_power_tail_sublinear_threshold_closed="
        f"{fmt_bool(payload['prime_power_tail_sublinear_threshold_closed'])}",
        "positive_proportion_psi_would_close_rows_eventually="
        f"{fmt_bool(payload['positive_proportion_psi_would_close_rows_eventually'])}",
        "known_short_interval_input_reaches_sqrt_window="
        f"{fmt_bool(payload['known_short_interval_input_reaches_sqrt_window'])}",
        "pointwise_psi_row_positive_proportion_proved="
        f"{fmt_bool(payload['pointwise_psi_row_positive_proportion_proved'])}",
        "admissible_signed_typeii_or_trace_family_constructed="
        f"{fmt_bool(payload['admissible_signed_typeii_or_trace_family_constructed'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| P | rows | max tail k | max actual tail | actual tail / P | global sublinear bound / P | max root-bound k |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for audit in payload["audits"]:
        max_tail = audit["max_actual_tail_row"]
        max_root = audit["max_integer_root_bound_row"]
        lines.append(
            "| {P} | {rows} | {max_k} | {max_tail:.6f} | {tail_ratio:.6f} | "
            "{sub_ratio:.6f} | {root_k} |".format(
                P=audit["P"],
                rows=audit["strict_row_count"],
                max_k=max_tail["k"],
                max_tail=max_tail["prime_power_tail_mass"],
                tail_ratio=max_tail["tail_over_P"],
                sub_ratio=audit["global_sublinear_bound_over_P"],
                root_k=max_root["k"],
            )
        )

    last = payload["audits"][-1]
    max_tail = last["max_actual_tail_row"]
    lines.extend(
        [
            "",
            "最大样本行快照：",
            "",
            "```text",
            f"P={last['P']}, k={max_tail['k']}",
            f"prime_power_tail_count={max_tail['prime_power_tail_count']}",
            f"prime_power_tail_mass={max_tail['prime_power_tail_mass']:.6f}",
            f"integer_root_mass_bound={max_tail['integer_root_mass_bound']:.6f}",
            f"global_sublinear_mass_bound={max_tail['global_sublinear_mass_bound']:.6f}",
            f"prime_power_items_sample={', '.join(max_tail['prime_power_items_sample'])}",
            "```",
            "",
            "## 3. 解析阈值趋势",
            "",
            "| P | sublinear mass bound | bound / P |",
            "| ---: | ---: | ---: |",
        ]
    )
    for row in payload["asymptotic_bound_table"]:
        lines.append(
            "| {P} | {mass:.6f} | {ratio:.9f} |".format(
                P=row["P"],
                mass=row["global_sublinear_mass_bound"],
                ratio=row["global_sublinear_bound_over_P"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 外部前沿阈值",
            "",
            "| 外部输入 | 源 | strict-row 结论 |",
            "| --- | --- | --- |",
        ]
    )
    for item in payload["external_thresholds"]:
        lines.append(
            f"| {item['name']} | {item['source']} | closes_strict_row="
            f"{fmt_bool(item['closes_strict_row'])}; {item['reason']} |"
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
        "prime_power_tail_sublinear_threshold_closed="
        f"{fmt_bool(payload['prime_power_tail_sublinear_threshold_closed'])}"
    )
    print(
        "pointwise_psi_row_positive_proportion_proved="
        f"{fmt_bool(payload['pointwise_psi_row_positive_proportion_proved'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
