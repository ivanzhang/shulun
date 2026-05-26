#!/usr/bin/env python3
"""审计 Prime Matrix 行窗口中的 von Mangoldt 素幂尾巴吸收阈值。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_prime_power_tail_absorption_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json

输出：
  data/prime-matrix-phi-lpf-prime-power-tail-absorption-ledger.json
  docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json
  docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.md
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

SLUG = "prime-matrix-phi-lpf-prime-power-tail-absorption"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

SAMPLE_PRIMES = [31, 101, 251, 1009]
ROW_SNAPSHOT_LIMIT = 8

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json",
    DOCS / "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json",
    DOCS / "prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "LPFPurePowerVonMangoldtCompressionClosed "
    "AND PrimePowerTailAbsorptionThresholdClosed "
    "AND NeedPointwisePsiRowLowerBoundBeyondPrimePowerTail "
    "AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen"
)


def sieve(limit: int) -> list[bool]:
    """返回素数布尔表。"""
    is_prime = [False, False] + [True] * max(0, limit - 1)
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            step_start = p * p
            is_prime[step_start : limit + 1 : p] = [False] * (
                ((limit - step_start) // p) + 1
            )
    return is_prime


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


def prime_power_owner(n: int, is_prime: list[bool]) -> tuple[int, int] | None:
    """若 n 是素数幂 p^a 且 a>=2，返回 (p,a)，否则返回 None。"""
    max_a = int(math.log2(n))
    for a in range(2, max_a + 1):
        root = integer_nth_root_floor(n, a)
        if root >= 2 and root**a == n and is_prime[root]:
            # 选择最小素底；素数幂只有一个素底，先遇到的指数不影响 log p。
            return root, a
    return None


def row_prime_power_tail_bound(P: int, k: int) -> dict[str, Any]:
    """用整数根区间给出行内合数素幂尾巴的确定性上界。"""
    upper = (k + 1) * P - 1
    lower = k * P
    max_a = int(math.log2(upper))
    exponent_counts: dict[str, int] = {}
    total_base_count_bound = 0
    for a in range(2, max_a + 1):
        hi = integer_nth_root_floor(upper, a)
        lo = integer_nth_root_floor(lower, a)
        count_bound = max(0, hi - lo)
        if count_bound:
            exponent_counts[str(a)] = count_bound
            total_base_count_bound += count_bound
    return {
        "max_exponent": max_a,
        "integer_base_count_bound": total_base_count_bound,
        "weighted_logP_bound": total_base_count_bound * math.log(P),
        "exponent_base_count_bounds": exponent_counts,
    }


def audit_prime(P: int) -> dict[str, Any]:
    """审计一个 prime P 的所有 strict rows。"""
    limit = P * P - 1
    is_prime = sieve(limit)
    log_values = [0.0] * (limit + 1)
    prime_power_logs = [0.0] * (limit + 1)
    prime_power_tags: list[tuple[int, int] | None] = [None] * (limit + 1)

    for n in range(2, limit + 1):
        if is_prime[n]:
            log_values[n] = math.log(n)
            continue
        pp = prime_power_owner(n, is_prime)
        if pp is not None:
            base, exponent = pp
            prime_power_tags[n] = (base, exponent)
            prime_power_logs[n] = math.log(base)
            log_values[n] = math.log(base)

    row_results: list[dict[str, Any]] = []
    all_identity_ok = True
    all_tail_bound_ok = True
    all_absorption_equiv_ok = True
    rows_with_prime = 0
    rows_where_psi_exceeds_tail = 0

    for k in range(1, P):
        start = k * P + 1
        stop = (k + 1) * P - 1
        theta_mass = 0.0
        psi_mass = 0.0
        tail_mass = 0.0
        prime_count = 0
        tail_count = 0
        tail_items: list[str] = []

        for n in range(start, stop + 1):
            if is_prime[n]:
                prime_count += 1
                theta_mass += math.log(n)
            if prime_power_tags[n] is not None:
                tail_count += 1
                base, exponent = prime_power_tags[n]  # type: ignore[misc]
                tail_mass += math.log(base)
                if len(tail_items) < 6:
                    tail_items.append(f"{n}={base}^{exponent}")
            psi_mass += log_values[n]

        identity_ok = abs(psi_mass - theta_mass - tail_mass) < 1e-9
        tail_bound = row_prime_power_tail_bound(P, k)
        tail_bound_ok = tail_mass <= tail_bound["weighted_logP_bound"] + 1e-9
        has_prime = prime_count > 0
        psi_exceeds_tail = psi_mass > tail_mass + 1e-12
        absorption_equiv_ok = has_prime == psi_exceeds_tail
        all_identity_ok = all_identity_ok and identity_ok
        all_tail_bound_ok = all_tail_bound_ok and tail_bound_ok
        all_absorption_equiv_ok = all_absorption_equiv_ok and absorption_equiv_ok
        rows_with_prime += 1 if has_prime else 0
        rows_where_psi_exceeds_tail += 1 if psi_exceeds_tail else 0

        row_results.append(
            {
                "k": k,
                "interval": f"({k}P,{k + 1}P)",
                "integer_interval": [start, stop],
                "prime_count": prime_count,
                "theta_mass": theta_mass,
                "composite_prime_power_count": tail_count,
                "prime_power_tail_mass": tail_mass,
                "psi_mass": psi_mass,
                "psi_equals_theta_plus_tail": identity_ok,
                "psi_exceeds_tail": psi_exceeds_tail,
                "has_prime": has_prime,
                "absorption_equivalence_holds": absorption_equiv_ok,
                "tail_bound_logP": tail_bound["weighted_logP_bound"],
                "tail_bound_base_count": tail_bound["integer_base_count_bound"],
                "tail_bound_ok": tail_bound_ok,
                "tail_items_sample": tail_items,
                "tail_over_sqrtP_logP": (
                    tail_mass / (math.sqrt(P) * math.log(P)) if P > 1 else 0.0
                ),
            }
        )

    max_tail_row = max(row_results, key=lambda row: row["prime_power_tail_mass"])
    max_bound_row = max(row_results, key=lambda row: row["tail_bound_logP"])
    min_theta_positive_row = min(
        (row for row in row_results if row["has_prime"]),
        key=lambda row: row["theta_mass"],
        default=None,
    )
    empty_rows = [row for row in row_results if not row["has_prime"]]

    return {
        "P": P,
        "strict_row_count": P - 1,
        "rows_with_prime": rows_with_prime,
        "rows_where_psi_exceeds_tail": rows_where_psi_exceeds_tail,
        "empty_rows_in_sample": len(empty_rows),
        "psi_theta_tail_identity_all_rows": all_identity_ok,
        "prime_power_tail_bound_all_rows": all_tail_bound_ok,
        "psi_tail_absorption_equivalent_to_prime_presence_all_rows": all_absorption_equiv_ok,
        "max_prime_power_tail_row": max_tail_row,
        "max_tail_bound_row": max_bound_row,
        "min_positive_theta_row": min_theta_positive_row,
        "empty_row_snapshots": empty_rows[:ROW_SNAPSHOT_LIMIT],
    }


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
        "certificate_type": "prime_matrix_phi_lpf_prime_power_tail_absorption_audit",
        "status": "prime_power_tail_absorption_threshold_reduces_theta_to_pointwise_psi",
        "verified_date": "2026-05-26",
        "sample_primes": SAMPLE_PRIMES,
        "row_interval": "I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P",
        "identity": "psi(I_{P,k})=theta(I_{P,k})+sum_{p^a in I_{P,k}, a>=2} log p",
        "absorption_criterion": "theta(I_{P,k})>0 iff psi(I_{P,k})>prime_power_tail(I_{P,k})",
        "deterministic_tail_bound": (
            "prime_power_tail(I_{P,k}) <= log(P) * sum_{a>=2} "
            "(floor(((k+1)P-1)^(1/a))-floor((kP)^(1/a)))"
        ),
        "psi_theta_tail_identity_all_samples": all(
            audit["psi_theta_tail_identity_all_rows"] for audit in audits
        ),
        "prime_power_tail_bound_all_samples": all(
            audit["prime_power_tail_bound_all_rows"] for audit in audits
        ),
        "psi_tail_absorption_equivalent_to_prime_presence_all_samples": all(
            audit["psi_tail_absorption_equivalent_to_prime_presence_all_rows"]
            for audit in audits
        ),
        "prime_power_tail_absorption_threshold_closed": True,
        "pointwise_psi_row_lower_bound_beyond_tail_proved": False,
        "pointwise_theta_ap_lower_bound_proved": False,
        "admissible_signed_typeii_or_trace_family_constructed": False,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "audits": audits,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "After the LPF pure-power compression, mixed composites contribute zero "
            "to Lambda pointwise. The remaining obstruction between psi and theta is "
            "the composite-prime-power tail. For every strict row, theta positivity is "
            "equivalent to psi mass exceeding this tail, and the tail has a deterministic "
            "integer-root bound. This reduces the prime-extraction target from direct "
            "theta positivity to a pointwise psi lower bound beyond the prime-power tail. "
            "No such pointwise psi lower bound or admissible signed Type-II/trace family "
            "is proved here."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF prime-power tail absorption 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 严格分解",
        "",
        "对 strict row",
        "",
        "```text",
        payload["row_interval"],
        "```",
        "",
        "有精确分解：",
        "",
        "```text",
        payload["identity"],
        "```",
        "",
        "因此素数存在性可改写为素幂尾巴吸收阈值：",
        "",
        "```text",
        payload["absorption_criterion"],
        "```",
        "",
        "尾巴有确定性整数根上界：",
        "",
        "```text",
        payload["deterministic_tail_bound"],
        "```",
        "",
        "## 2. 全局读数",
        "",
        "```text",
        f"psi_theta_tail_identity_all_samples={fmt_bool(payload['psi_theta_tail_identity_all_samples'])}",
        f"prime_power_tail_bound_all_samples={fmt_bool(payload['prime_power_tail_bound_all_samples'])}",
        "psi_tail_absorption_equivalent_to_prime_presence_all_samples="
        f"{fmt_bool(payload['psi_tail_absorption_equivalent_to_prime_presence_all_samples'])}",
        "prime_power_tail_absorption_threshold_closed="
        f"{fmt_bool(payload['prime_power_tail_absorption_threshold_closed'])}",
        "pointwise_psi_row_lower_bound_beyond_tail_proved="
        f"{fmt_bool(payload['pointwise_psi_row_lower_bound_beyond_tail_proved'])}",
        f"pointwise_theta_ap_lower_bound_proved={fmt_bool(payload['pointwise_theta_ap_lower_bound_proved'])}",
        "admissible_signed_typeii_or_trace_family_constructed="
        f"{fmt_bool(payload['admissible_signed_typeii_or_trace_family_constructed'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| P | rows | rows with prime | empty rows | max tail row k | max tail mass | max tail bound | min positive theta row k |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for audit in payload["audits"]:
        min_row = audit["min_positive_theta_row"] or {"k": None}
        lines.append(
            "| {P} | {strict_row_count} | {rows_with_prime} | {empty_rows_in_sample} | "
            "{max_k} | {max_tail:.6f} | {max_bound:.6f} | {min_k} |".format(
                P=audit["P"],
                strict_row_count=audit["strict_row_count"],
                rows_with_prime=audit["rows_with_prime"],
                empty_rows_in_sample=audit["empty_rows_in_sample"],
                max_k=audit["max_prime_power_tail_row"]["k"],
                max_tail=audit["max_prime_power_tail_row"]["prime_power_tail_mass"],
                max_bound=audit["max_tail_bound_row"]["tail_bound_logP"],
                min_k=min_row["k"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最大样本尾巴行",
            "",
        ]
    )
    last = payload["audits"][-1]
    max_row = last["max_prime_power_tail_row"]
    lines.extend(
        [
            f"`P={last['P']}` 的最大素幂尾巴出现在 `k={max_row['k']}`：",
            "",
            "```text",
            f"integer_interval={max_row['integer_interval']}",
            f"prime_count={max_row['prime_count']}",
            f"theta_mass={max_row['theta_mass']:.6f}",
            f"prime_power_tail_count={max_row['composite_prime_power_count']}",
            f"prime_power_tail_mass={max_row['prime_power_tail_mass']:.6f}",
            f"psi_mass={max_row['psi_mass']:.6f}",
            f"tail_bound_logP={max_row['tail_bound_logP']:.6f}",
            f"tail_items_sample={', '.join(max_row['tail_items_sample'])}",
            "```",
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
    print(
        "prime_power_tail_absorption_threshold_closed="
        f"{fmt_bool(payload['prime_power_tail_absorption_threshold_closed'])}"
    )
    print(
        "pointwise_psi_row_lower_bound_beyond_tail_proved="
        f"{fmt_bool(payload['pointwise_psi_row_lower_bound_beyond_tail_proved'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
