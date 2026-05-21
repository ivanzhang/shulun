#!/usr/bin/env python3
"""生成 1<k<P 闭区间端点 LPF 桶抵消证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_endpoint_bucket_cancellation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.md
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-endpoint-interval-difference-router.json",
    DOCS / "prime-matrix-short-interval-rough-residue-barrier-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def spf_upto(n: int) -> list[int]:
    """返回最小素因子表；spf[1]=1。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def phi_count(x: int, p: int, spf: list[int]) -> int:
    """计算 Phi(x,p)：1<=n<=x 且所有素因子都不小于 p 的个数。"""
    if x <= 0:
        return 0
    return sum(1 for n in range(1, x + 1) if n == 1 or spf[n] >= p)


def bucket_deltas(a: int, b: int) -> dict[int, int]:
    """计算闭区间 [a,b] 的 LPF 桶端点差分。"""
    spf = spf_upto(b)
    deltas: dict[int, int] = {}
    for p in primes_upto(isqrt(b)):
        delta = phi_count(b // p, p, spf) - phi_count((a - 1) // p, p, spf)
        if delta:
            deltas[p] = delta
    return deltas


def prime_count_direct(a: int, b: int) -> int:
    """直接数闭区间 [a,b] 内素数。"""
    spf = spf_upto(b)
    return sum(1 for n in range(max(2, a), b + 1) if spf[n] == n)


def endpoint_owner_counter(p_len: int, k: int) -> Counter[int]:
    """返回两个端点合数所属的 LPF owner 桶。"""
    spf = spf_upto(p_len)
    return Counter([spf[k], spf[k + 1]])


def signed_bucket_difference(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    """计算两个桶字典的差 left-right，保留非零项。"""
    keys = set(left) | set(right)
    return {p: left.get(p, 0) - right.get(p, 0) for p in sorted(keys) if left.get(p, 0) != right.get(p, 0)}


def strict_k_endpoint_audit(p_len: int, k: int) -> dict[str, Any]:
    """审计 1<k<P 的闭区间端点桶付款。"""
    if not (1 < k < p_len):
        raise ValueError("本证书要求 1<k<P")
    closed_a = k * p_len
    closed_b = k * p_len + p_len
    internal_a = closed_a + 1
    internal_b = closed_b - 1
    closed = bucket_deltas(closed_a, closed_b)
    internal = bucket_deltas(internal_a, internal_b)
    diff = signed_bucket_difference(closed, internal)
    owners = endpoint_owner_counter(p_len, k)
    owner_dict = {p: owners[p] for p in sorted(owners)}
    endpoint_values = [
        {
            "name": "left",
            "n": closed_a,
            "cofactor": k,
            "lpf_owner": spf_upto(p_len)[k],
        },
        {
            "name": "right",
            "n": closed_b,
            "cofactor": k + 1,
            "lpf_owner": spf_upto(p_len)[k + 1],
        },
    ]
    return {
        "P": p_len,
        "k": k,
        "closed_interval": [closed_a, closed_b],
        "internal_interval": [internal_a, internal_b],
        "closed_length": closed_b - closed_a + 1,
        "internal_length": internal_b - internal_a + 1,
        "closed_prime_count": prime_count_direct(closed_a, closed_b),
        "internal_prime_count": prime_count_direct(internal_a, internal_b),
        "closed_prime_count_equals_internal": (
            prime_count_direct(closed_a, closed_b) == prime_count_direct(internal_a, internal_b)
        ),
        "closed_composite_delta_total": sum(closed.values()),
        "internal_composite_delta_total": sum(internal.values()),
        "closed_minus_internal_composite_delta_total": sum(closed.values()) - sum(internal.values()),
        "closed_bucket_deltas": closed,
        "internal_bucket_deltas": internal,
        "closed_minus_internal_bucket_deltas": diff,
        "endpoint_owner_bucket_counts": owner_dict,
        "endpoint_bucket_difference_matches_owner_counts": diff == owner_dict,
        "endpoint_values": endpoint_values,
    }


def finite_sweep(max_prime: int = 97) -> dict[str, Any]:
    """有限审计端点桶抵消；只用于验证证书实现。"""
    case_count = 0
    failures: list[dict[str, Any]] = []
    twin_owner_cases = 0
    distinct_owner_cases = 0
    for p_len in [p for p in primes_upto(max_prime) if p >= 3]:
        for k in range(2, p_len):
            case_count += 1
            audit = strict_k_endpoint_audit(p_len, k)
            if len(audit["endpoint_owner_bucket_counts"]) == 1:
                twin_owner_cases += 1
            else:
                distinct_owner_cases += 1
            if not (
                audit["closed_prime_count_equals_internal"]
                and audit["closed_minus_internal_composite_delta_total"] == 2
                and audit["endpoint_bucket_difference_matches_owner_counts"]
            ):
                failures.append(audit)
    return {
        "max_prime": max_prime,
        "case_count": case_count,
        "all_endpoint_bucket_cancellations_verified": not failures,
        "failure_count": len(failures),
        "failure_sample": failures[:3],
        "same_owner_endpoint_cases": twin_owner_cases,
        "distinct_owner_endpoint_cases": distinct_owner_cases,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "StrictKEndpointCompositeMassTwo",
            True,
            True,
            "当 1<k<P 时，闭区间 [kP,kP+P] 比内部行多出的两个端点都是合数。",
            "endpoint composite mass is exactly two",
        ),
        row(
            "EndpointLPFOwnerBucketsPinned",
            True,
            True,
            "左端点归入 LPF(k) 桶，右端点归入 LPF(k+1) 桶；若 k+1=P，则右端点归入 P 桶。",
            "owner multiset {LPF(k), LPF(k+1)}",
        ),
        row(
            "ClosedMinusInternalBucketDeltaEqualsEndpointOwners",
            True,
            True,
            "闭区间 LPF 桶端点增量减去内部行增量，逐桶等于两个端点 owner 的计数。",
            "bucket-level cancellation identity",
        ),
        row(
            "NoEndpointSlackForRowPositivity",
            True,
            True,
            "闭区间多出的长度 2 被两个端点合数桶精确吃掉，不能产生额外素数正性余量。",
            "strict-k endpoint shortcut removed",
        ),
        row(
            "InternalRowCompositeDeltaInequalityStillNeeded",
            False,
            False,
            "要证明行内有素数，仍需内部行合数桶增量和小于 P-1。",
            "same full-root uncovered-slot positivity",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层排除了端点余量捷径，但未证明内部行正性。",
            "Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sample_audits = [
        strict_k_endpoint_audit(5, 4),
        strict_k_endpoint_audit(11, 10),
        strict_k_endpoint_audit(17, 16),
        strict_k_endpoint_audit(101, 50),
        strict_k_endpoint_audit(101, 100),
    ]
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_endpoint_bucket_cancellation_router",
        "status": "strict_k_endpoint_bucket_cancellation_closed_but_internal_row_positivity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "strict_k_endpoint_composite_mass_two_proved": True,
        "endpoint_lpf_owner_buckets_pinned": True,
        "closed_minus_internal_bucket_delta_equals_endpoint_owners_proved": True,
        "no_endpoint_slack_for_row_positivity_proved": True,
        "internal_row_composite_delta_inequality_proved": False,
        "full_root_uncovered_slot_positive_proved": False,
        "row_column_unconditional_closed": False,
        "identity": (
            "Delta_closed_p-Delta_internal_p = 1_{p=LPF(k)} + 1_{p=LPF(k+1)} "
            "for [kP,kP+P], 1<k<P"
        ),
        "prime_count_identity": "pi(kP+P)-pi(kP-1)=pi(kP+P-1)-pi(kP)",
        "sample_audits": sample_audits,
        "finite_sweep": finite_sweep(),
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "严格 1<k<P 时，闭区间 [kP,kP+P] 比内部行只多两个合数端点。"
            "Phi-LPF 桶差分逐桶显示，这两个端点分别支付给 LPF(k) 与 LPF(k+1) owner 桶；"
            "闭区间多出的长度 2 被合数桶增量精确抵消。"
            "因此端点差分没有隐藏正性余量，剩余仍是内部行 LPF 合数桶增量和小于 P-1。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k endpoint bucket cancellation 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. 桶抵消恒等式",
        "",
        "```text",
        result["prime_count_identity"],
        result["identity"],
        "```",
        "",
        "这里 `Delta_closed_p` 是 `[kP,kP+P]` 的第 `p` 个 LPF 桶端点增量，",
        "`Delta_internal_p` 是 `[kP+1,kP+P-1]` 的第 `p` 个 LPF 桶端点增量。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 样本审计",
            "",
            "| P | k | closed | internal | closed primes | internal primes | delta total | bucket diff | endpoint owners | ok |",
            "| ---: | ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    for audit in result["sample_audits"]:
        lines.append(
            f"| {audit['P']} | {audit['k']} | {audit['closed_interval']} | {audit['internal_interval']} | "
            f"{audit['closed_prime_count']} | {audit['internal_prime_count']} | "
            f"{audit['closed_minus_internal_composite_delta_total']} | "
            f"`{cell(audit['closed_minus_internal_bucket_deltas'])}` | "
            f"`{cell(audit['endpoint_owner_bucket_counts'])}` | "
            f"`{fmt_bool(audit['endpoint_bucket_difference_matches_owner_counts'])}` |"
        )
    sweep = result["finite_sweep"]
    lines.extend(
        [
            "",
            "## 4. 有限审计边界",
            "",
            "```text",
            f"max_prime={sweep['max_prime']}",
            f"case_count={sweep['case_count']}",
            f"all_endpoint_bucket_cancellations_verified={fmt_bool(sweep['all_endpoint_bucket_cancellations_verified'])}",
            f"same_owner_endpoint_cases={sweep['same_owner_endpoint_cases']}",
            f"distinct_owner_endpoint_cases={sweep['distinct_owner_endpoint_cases']}",
            "finite_evidence_not_used_as_global_proof=true",
            "```",
            "",
            "## 5. 结论",
            "",
            "闭区间端点没有给出新的正性来源：多出的两个位置被两个端点合数的 LPF owner 桶精确抵消。",
            "因此 `[kP,kP+P]` 的 Phi-LPF 端点差分路线已经完全回到内部行不等式",
            "`sum Delta_internal_p < P-1`。该不等式仍等价于 full-root 未覆盖槽存在，不能作为内部黑箱。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
