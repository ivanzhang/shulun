#!/usr/bin/env python3
"""审计 Runbo Li 短区间定理对 Prime Matrix 低行带的桥接范围。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_runbo_li_low_row_band_bridge_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json

输出：
  data/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-ledger.json
  docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json
  docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.md
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

SLUG = "prime-matrix-phi-lpf-runbo-li-low-row-band-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_PRIMES = [31, 101, 251, 1009, 3001, 10007, 100003, 1000003]
ASYMPTOTIC_POINTS = [10**3, 10**6, 10**9, 10**12, 10**18]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json",
    DOCS / "prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "RunboLiLowRowBandClosedForKPlusOneLessThanPTo12Over13 "
    "AND TopBandKPlusOneAtLeastPTo12Over13StillRequiresSqrtScalePointwisePsi "
    "AND PrimePowerTailSublinearThresholdClosed "
    "AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def is_probable_prime(n: int) -> bool:
    """对本脚本样本范围足够的确定性 Miller-Rabin 素性测试。"""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
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


def max_li_closed_k(P: int) -> int:
    """最大 k，使得 ((k+1)P)^(13/25)<P。

    等价整数条件为 (k+1)^13 < P^12。
    """
    n_max = integer_nth_root_floor(P**12 - 1, 13)
    return max(0, min(P - 1, n_max - 1))


def first_prime_in_row(P: int, k: int) -> int | None:
    """仅用于小样本展示，寻找 strict row 中第一个素数。"""
    start = k * P + 1
    stop = (k + 1) * P
    for n in range(start, stop):
        if is_probable_prime(n):
            return n
    return None


def audit_prime(P: int) -> dict[str, Any]:
    """审计一个 prime P 的低行带桥接规模。"""
    if not is_probable_prime(P):
        raise ValueError(f"sample P must be prime: {P}")
    k_max = max_li_closed_k(P)
    closed_rows = k_max
    top_band_rows = (P - 1) - closed_rows
    boundary_k = max(1, k_max)
    boundary_prime = first_prime_in_row(P, boundary_k) if P <= 10007 and boundary_k else None
    next_k = k_max + 1 if k_max + 1 < P else None
    return {
        "P": P,
        "strict_row_count": P - 1,
        "li_closed_k_max": k_max,
        "li_closed_rows": closed_rows,
        "li_closed_rows_over_all_rows": closed_rows / (P - 1),
        "top_band_rows_remaining": top_band_rows,
        "top_band_rows_over_all_rows": top_band_rows / (P - 1),
        "exact_integer_condition_for_closed_rows": "(k+1)^13 < P^12",
        "boundary_row_k": boundary_k,
        "boundary_row_first_prime_sample": boundary_prime,
        "next_uncovered_k": next_k,
        "next_uncovered_condition_value": (
            f"{next_k + 1}^13 >= {P}^12" if next_k is not None else None
        ),
    }


def asymptotic_table() -> list[dict[str, Any]]:
    """记录低行带占比的渐近行为。"""
    rows = []
    for P in ASYMPTOTIC_POINTS:
        approx_closed = P ** (12.0 / 13.0)
        rows.append(
            {
                "P": P,
                "approx_closed_rows": approx_closed,
                "approx_closed_fraction": approx_closed / P,
                "approx_top_band_fraction": 1.0 - approx_closed / P,
            }
        )
    return rows


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    audits = [audit_prime(P) for P in SAMPLE_PRIMES]
    return {
        "certificate_type": "prime_matrix_phi_lpf_runbo_li_low_row_band_bridge_audit",
        "status": "runbo_li_short_interval_closes_low_row_band_but_not_top_band",
        "verified_date": "2026-05-26",
        "external_input": {
            "name": "Runbo Li primes in short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            "exponent": "13/25 = 0.52",
            "form_used": "for sufficiently large X, (X-X^(13/25), X] contains a prime",
        },
        "row_interval": "I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P",
        "right_endpoint_match": "X=(k+1)P",
        "embedding_condition": "X^(13/25)<P iff (k+1)^13<P^12",
        "low_row_band_closed_asymptotically": "1<=k<=P^(12/13)-1, up to integer floor",
        "top_band_remaining_asymptotically": "k+1>=P^(12/13)",
        "runbo_li_low_row_band_closed": True,
        "top_band_sqrt_scale_gap_remains": True,
        "closes_all_strict_rows": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "audits": audits,
        "asymptotic_table": asymptotic_table(),
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "Runbo Li's 13/25 short-interval theorem gives a genuine external "
            "unconditional bridge for the low-row band: if (k+1)^13<P^12, the "
            "short interval ending at (k+1)P fits inside the strict row and "
            "contains a prime. This closes a growing but zero-density set of "
            "rows. The dominant top band k+1>=P^(12/13), including k comparable "
            "to P, still requires a square-root-scale pointwise psi/theta lower "
            "bound or an admissible signed Type-II/trace family."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF Runbo Li low-row band bridge 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 外部定理嵌入",
        "",
        "使用外部输入：",
        "",
        "```text",
        f"name={payload['external_input']['name']}",
        f"source={payload['external_input']['source']}",
        f"exponent={payload['external_input']['exponent']}",
        f"form_used={payload['external_input']['form_used']}",
        "```",
        "",
        "对 strict row 取右端点：",
        "",
        "```text",
        payload["row_interval"],
        payload["right_endpoint_match"],
        payload["embedding_condition"],
        "```",
        "",
        "因此低行带无条件外部闭合为：",
        "",
        "```text",
        payload["low_row_band_closed_asymptotically"],
        "```",
        "",
        "但剩余 top band 为：",
        "",
        "```text",
        payload["top_band_remaining_asymptotically"],
        "```",
        "",
        "## 2. 样本审计",
        "",
        "```text",
        f"runbo_li_low_row_band_closed={fmt_bool(payload['runbo_li_low_row_band_closed'])}",
        f"top_band_sqrt_scale_gap_remains={fmt_bool(payload['top_band_sqrt_scale_gap_remains'])}",
        f"closes_all_strict_rows={fmt_bool(payload['closes_all_strict_rows'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| P | rows | Li-closed k max | closed rows | closed fraction | top-band rows | next uncovered k |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| {P} | {rows} | {kmax} | {closed} | {closed_frac:.6f} | {top} | {next_k} |".format(
                P=audit["P"],
                rows=audit["strict_row_count"],
                kmax=audit["li_closed_k_max"],
                closed=audit["li_closed_rows"],
                closed_frac=audit["li_closed_rows_over_all_rows"],
                top=audit["top_band_rows_remaining"],
                next_k=audit["next_uncovered_k"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 渐近占比",
            "",
            "| P | approx closed rows | approx closed fraction | approx top-band fraction |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for row in payload["asymptotic_table"]:
        lines.append(
            "| {P} | {closed:.3f} | {closed_frac:.9f} | {top_frac:.9f} |".format(
                P=row["P"],
                closed=row["approx_closed_rows"],
                closed_frac=row["approx_closed_fraction"],
                top_frac=row["approx_top_band_fraction"],
            )
        )

    lines.extend(
        [
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
    """生成证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(f"runbo_li_low_row_band_closed={fmt_bool(payload['runbo_li_low_row_band_closed'])}")
    print(f"closes_all_strict_rows={fmt_bool(payload['closes_all_strict_rows'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
