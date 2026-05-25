#!/usr/bin/env python3
"""审计 2n+1 仿射轴上的 endpoint-prime leak 与 LPF first-hit 分割。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_affine_endpoint_lpf_first_hit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json

输出：
  data/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-ledger.json
  docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json
  docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.md
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SAMPLE_X = [100, 1000, 10000, 50000]

SOURCE_FILES = [
    Path(__file__).resolve(),
    DOCS / "prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json",
    DOCS / "prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "EndpointPrimeLeakSeparatedFromLPFTailButPrimeExtractionStillParityBlocked "
    "AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC "
    "AND PrimitiveOrientationLocalFactorProductLawBeforePushforward "
    "AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving "
    "AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
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


def primes_from_spf(spf: list[int]) -> list[int]:
    """从最小素因子表提取素数。"""
    return [n for n in range(2, len(spf)) if spf[n] == n]


def omega(n: int, spf: list[int]) -> int:
    """计算带重数的素因子个数。"""
    count = 0
    while n > 1:
        p = spf[n]
        n //= p
        count += 1
    return count


def rough_to_p(n: int, p: int, primes: list[int]) -> bool:
    """判断 n 没有小于 p 的素因子。"""
    for q in primes:
        if q >= p:
            break
        if n % q == 0:
            return False
    return True


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def zero_class_event_count(M: int, odd_primes: list[int]) -> int:
    """统计所有奇素数零类命中次数，允许一个 m 被多个素因子重复命中。"""
    total = 0
    for p in odd_primes:
        # p*c <= M 且 c 为奇数。
        total += (M // p + 1) // 2
    return total


def top_counter(counter: Counter[int], limit: int = 8) -> dict[str, int]:
    """压缩计数器。"""
    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    out = {str(key): value for key, value in items[:limit]}
    rest = sum(value for _key, value in items[limit:])
    if rest:
        out["other"] = rest
    return out


def audit_x(x_bound: int) -> dict[str, Any]:
    """审计一个 X 截断。"""
    M = 2 * x_bound + 1
    spf = spf_table(M)
    primes = primes_from_spf(spf)
    odd_primes = [p for p in primes if p != 2]

    odd_count = 0
    endpoint_prime_count = 0
    composite_tail_count = 0
    semiprime_tail_count = 0
    higher_composite_tail_count = 0
    lpf_bucket_counter: Counter[int] = Counter()
    cofactor_omega_counter: Counter[int] = Counter()
    identity_failures: list[dict[str, int]] = []
    rough_failures: list[dict[str, int]] = []

    for m in range(3, M + 1, 2):
        odd_count += 1
        p = spf[m]
        if p == m:
            endpoint_prime_count += 1
            n = (m - 1) // 2
            if n != (p - 1) // 2:
                identity_failures.append({"m": m, "p": p, "n": n})
            continue

        composite_tail_count += 1
        c = m // p
        k = (c - 1) // 2
        n = (m - 1) // 2
        lpf_bucket_counter[p] += 1
        cofactor_omega_counter[omega(c, spf)] += 1

        if spf[c] == c:
            semiprime_tail_count += 1
        else:
            higher_composite_tail_count += 1
        if n != k * p + (p - 1) // 2:
            identity_failures.append({"m": m, "p": p, "c": c, "k": k, "n": n})
        if not rough_to_p(c, p, primes):
            rough_failures.append({"m": m, "p": p, "c": c})

    zero_events = zero_class_event_count(M, odd_primes)
    first_hit_total = endpoint_prime_count + composite_tail_count
    lpf_partition_closed = (
        first_hit_total == odd_count
        and not identity_failures
        and not rough_failures
        and sum(lpf_bucket_counter.values()) == composite_tail_count
    )
    tail_count_for_small_lpf = sum(
        count for p, count in lpf_bucket_counter.items() if p * p <= M
    )
    tail_count_for_large_lpf = composite_tail_count - tail_count_for_small_lpf

    return {
        "X": x_bound,
        "M": M,
        "odd_axis_count_m_3_to_M": odd_count,
        "odd_prime_endpoint_count": endpoint_prime_count,
        "composite_lpf_tail_count": composite_tail_count,
        "first_hit_partition_total": first_hit_total,
        "lpf_first_hit_partition_closed": lpf_partition_closed,
        "zero_class_event_count_with_duplicates": zero_events,
        "zero_class_duplicate_overcount": zero_events - odd_count,
        "endpoint_prime_fraction_of_first_hits": endpoint_prime_count / first_hit_total,
        "composite_tail_fraction_of_first_hits": composite_tail_count / first_hit_total,
        "semiprime_tail_count": semiprime_tail_count,
        "higher_composite_tail_count": higher_composite_tail_count,
        "cofactor_prime_fraction_inside_tail": (
            semiprime_tail_count / composite_tail_count if composite_tail_count else 0.0
        ),
        "tail_count_with_lpf_le_sqrt_M": tail_count_for_small_lpf,
        "tail_count_with_lpf_gt_sqrt_M": tail_count_for_large_lpf,
        "top_lpf_buckets": top_counter(lpf_bucket_counter),
        "cofactor_omega_histogram": top_counter(cofactor_omega_counter),
        "identity_failure_count": len(identity_failures),
        "rough_failure_count": len(rough_failures),
        "identity_failure_sample": identity_failures[:3],
        "rough_failure_sample": rough_failures[:3],
    }


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    rows = [audit_x(x) for x in SAMPLE_X]
    partition_closed = all(row["lpf_first_hit_partition_closed"] for row in rows)
    duplicate_overcount_positive = all(row["zero_class_duplicate_overcount"] > 0 for row in rows)
    parity_mixture_present = all(
        row["semiprime_tail_count"] > 0 and row["higher_composite_tail_count"] > 0
        for row in rows
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_affine_endpoint_lpf_first_hit_router",
        "status": "endpoint_prime_leak_lpf_first_hit_partition_closed_prime_extraction_open",
        "verified_date": "2026-05-25",
        "sample_X": SAMPLE_X,
        "first_hit_partition_identity": (
            "odd m>=3 is hit first at p=LPF(m); if m=p this is an endpoint prime, "
            "otherwise m=p(2k+1) with 2k+1 rough to p"
        ),
        "endpoint_prime_leak_separated": partition_closed,
        "lpf_tail_composite_partition_closed": partition_closed,
        "zero_class_duplicate_overcount_positive": duplicate_overcount_positive,
        "cofactor_parity_mixture_present_in_tail": parity_mixture_present,
        "prime_extraction_from_lpf_tail_proved": False,
        "signed_payload_or_von_mangoldt_weight_constructed": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The increasing LPF peel gives an exact first-hit partition on the "
            "affine odd axis: endpoint primes m=p are separated from composite tails "
            "m=p(2k+1). This repairs the k=0 leak in the Phi-LPF recursion. However, "
            "the composite tail still contains semiprime and higher-composite "
            "cofactors, and zero-class events overcount unless assigned by LPF. "
            "Thus the next proof object must be a signed payload, von-Mangoldt-like "
            "cofactor weight, admissible Type-II/trace family, or a named PDEC."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF affine endpoint LPF first-hit 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 `m=2n+1` 轴上的奇素数零类按最小素因子第一次命中精确分割。",
        "",
        "## 1. 核心身份",
        "",
        "```text",
        "m=p           -> endpoint prime leak, k=0",
        "m=p(2k+1)     -> composite LPF tail, k>=1",
        "2n+1=p(2k+1)  -> n=kp+(p-1)/2",
        "LPF(2k+1)>=p  -> LPF(2n+1)=p",
        "```",
        "",
        "这给 Phi-LPF 递推提供了从小到大剥离素因子的精确 first-hit 账本：",
        "端点素数 `m=p` 必须单独作为 prime leak 发射；合数尾才进入 LPF bucket。",
        "",
        "## 2. 审计读数",
        "",
        "```text",
        f"endpoint_prime_leak_separated={fmt_bool(payload['endpoint_prime_leak_separated'])}",
        f"lpf_tail_composite_partition_closed={fmt_bool(payload['lpf_tail_composite_partition_closed'])}",
        f"zero_class_duplicate_overcount_positive={fmt_bool(payload['zero_class_duplicate_overcount_positive'])}",
        f"cofactor_parity_mixture_present_in_tail={fmt_bool(payload['cofactor_parity_mixture_present_in_tail'])}",
        f"prime_extraction_from_lpf_tail_proved={fmt_bool(payload['prime_extraction_from_lpf_tail_proved'])}",
        f"signed_payload_or_von_mangoldt_weight_constructed={fmt_bool(payload['signed_payload_or_von_mangoldt_weight_constructed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "| X | M=2X+1 | odd m | endpoint primes | composite tails | zero-class duplicate overcount | semiprime tails | higher tails |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in payload["rows"]:
        lines.append(
            "| {X} | {M} | {odd_axis_count_m_3_to_M} | {odd_prime_endpoint_count} | "
            "{composite_lpf_tail_count} | {zero_class_duplicate_overcount} | "
            "{semiprime_tail_count} | {higher_composite_tail_count} |".format(**row)
        )
    lines.extend(
        [
            "",
            "`zero-class duplicate overcount` 为正说明：所有零类命中不能直接相加，必须按",
            "`LPF(m)` first-hit 分配，否则同一个合数会被多个素因子重复计算。",
            "",
            "## 3. 尾部仍是奇偶性障碍",
            "",
            "合数尾中同时存在 cofactor 为素数的半素数层和更高合数层。仅靠 Euler product、",
            "forbidden residue、Phi 递推或 LPF 桶计数，不会自动生成区分这些层的符号权重。",
            "因此本层闭合的是 first-hit partition，不是 prime extraction。",
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
    print(f"endpoint_prime_leak_separated={fmt_bool(payload['endpoint_prime_leak_separated'])}")
    print(f"lpf_tail_composite_partition_closed={fmt_bool(payload['lpf_tail_composite_partition_closed'])}")
    print(
        "cofactor_parity_mixture_present_in_tail="
        f"{fmt_bool(payload['cofactor_parity_mixture_present_in_tail'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
