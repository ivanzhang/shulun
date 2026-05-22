#!/usr/bin/env python3
"""生成 1<k<P 行内 raw-incidence / LPF-rejection 平衡证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_raw_rejection_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.md
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

SLUG = "prime-matrix-phi-lpf-strict-k-raw-rejection-balance"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json",
    DOCS / "prime-matrix-lowroot-sifted-deficit-frontier-router.json",
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


def raw_rejection_balance_audit(p_len: int, k: int) -> dict[str, Any]:
    """审计一条严格 1<k<P 行的原始命中与 LPF 拒绝平衡。"""
    if not (1 < k < p_len):
        raise ValueError("本证书要求 1<k<P")
    start = k * p_len + 1
    stop = k * p_len + p_len - 1
    length = p_len - 1
    root_bound = isqrt(stop)
    root_primes = primes_upto(root_bound)
    spf = spf_upto(stop)

    raw_counts: Counter[int] = Counter()
    owner_counts: Counter[int] = Counter()
    rejection_counts: Counter[int] = Counter()
    slot_rows: list[dict[str, Any]] = []
    prime_slots: list[int] = []
    composite_slots: list[int] = []
    max_raw_hits = 0

    for slot in range(1, p_len):
        n = k * p_len + slot
        raw_hits = [p for p in root_primes if n % p == 0]
        for p in raw_hits:
            raw_counts[p] += 1
        owner = None if spf[n] == n else spf[n]
        if owner is None:
            prime_slots.append(slot)
        else:
            owner_counts[owner] += 1
            composite_slots.append(slot)
        rejected = [p for p in raw_hits if p != owner]
        for p in rejected:
            rejection_counts[p] += 1
        max_raw_hits = max(max_raw_hits, len(raw_hits))
        if raw_hits or owner is None:
            slot_rows.append(
                {
                    "slot": slot,
                    "n": n,
                    "owner": owner,
                    "raw_hits": raw_hits,
                    "rejected_hits": rejected,
                    "is_prime": owner is None,
                }
            )

    raw_total = sum(raw_counts.values())
    owner_total = sum(owner_counts.values())
    rejection_total = sum(rejection_counts.values())
    prime_count = len(prime_slots)
    raw_surplus_over_row = raw_total - length
    rejection_excess_over_raw_surplus = rejection_total - raw_surplus_over_row

    return {
        "P": p_len,
        "k": k,
        "internal_interval": [start, stop],
        "length": length,
        "root_bound": root_bound,
        "inside_p_square": stop < p_len * p_len,
        "root_prime_count": len(root_primes),
        "raw_incidence_total": raw_total,
        "owner_total": owner_total,
        "rejection_total": rejection_total,
        "raw_surplus_over_row": raw_surplus_over_row,
        "rejection_excess_over_raw_surplus": rejection_excess_over_raw_surplus,
        "prime_count": prime_count,
        "raw_equals_owner_plus_rejection": raw_total == owner_total + rejection_total,
        "prime_equals_rejection_minus_raw_surplus": (
            prime_count == rejection_excess_over_raw_surplus
        ),
        "zero_row_iff_rejection_equals_raw_surplus": (
            (prime_count == 0) == (rejection_total == raw_surplus_over_row)
        ),
        "positive_defect_iff_rejection_strictly_exceeds_raw_surplus": (
            (prime_count > 0) == (rejection_total > raw_surplus_over_row)
        ),
        "raw_counts": {p: raw_counts[p] for p in sorted(raw_counts)},
        "owner_counts": {p: owner_counts[p] for p in sorted(owner_counts)},
        "rejection_counts": {p: rejection_counts[p] for p in sorted(rejection_counts)},
        "prime_slots_sample": prime_slots[:24],
        "composite_slots_sample": composite_slots[:24],
        "max_raw_hits_on_slot": max_raw_hits,
        "slot_rows_sample": slot_rows[:18],
    }


def finite_sweep(max_prime: int = 97) -> dict[str, Any]:
    """有限审计平衡恒等式；不作全局证明。"""
    case_count = 0
    failures: list[dict[str, Any]] = []
    zero_rows_found: list[dict[str, int]] = []
    min_excess: int | None = None
    min_excess_cases: list[dict[str, int]] = []
    max_raw_surplus = 0
    max_raw_surplus_case: dict[str, int] | None = None

    for p_len in [p for p in primes_upto(max_prime) if p >= 3]:
        for k in range(2, p_len):
            case_count += 1
            audit = raw_rejection_balance_audit(p_len, k)
            ok = (
                audit["raw_equals_owner_plus_rejection"]
                and audit["prime_equals_rejection_minus_raw_surplus"]
                and audit["zero_row_iff_rejection_equals_raw_surplus"]
                and audit["positive_defect_iff_rejection_strictly_exceeds_raw_surplus"]
            )
            if not ok:
                failures.append(audit)
            if audit["prime_count"] == 0:
                zero_rows_found.append({"P": p_len, "k": k})
            excess = audit["rejection_excess_over_raw_surplus"]
            if min_excess is None or excess < min_excess:
                min_excess = excess
                min_excess_cases = [{"P": p_len, "k": k, "excess": excess}]
            elif excess == min_excess and len(min_excess_cases) < 12:
                min_excess_cases.append({"P": p_len, "k": k, "excess": excess})
            raw_surplus = audit["raw_surplus_over_row"]
            if raw_surplus > max_raw_surplus:
                max_raw_surplus = raw_surplus
                max_raw_surplus_case = {"P": p_len, "k": k, "raw_surplus": raw_surplus}

    return {
        "max_prime": max_prime,
        "case_count": case_count,
        "all_raw_rejection_balance_identities_verified": not failures,
        "failure_count": len(failures),
        "failure_sample": failures[:3],
        "zero_rows_found_in_finite_sweep": zero_rows_found,
        "minimum_rejection_excess_over_raw_surplus": min_excess,
        "minimum_rejection_excess_cases": min_excess_cases,
        "maximum_raw_surplus_case": max_raw_surplus_case,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "RawIncidenceOwnerRejectionPartition",
            True,
            True,
            "根内原始命中逐项分成 LPF-owner 命中与非 owner 拒绝命中。",
            "raw incidence ledger",
        ),
        row(
            "PrimeCountEqualsRejectionExcess",
            True,
            True,
            "行内素数数目等于 LPF 拒绝量减去原始命中相对行长的超容量。",
            "prime_count = rejection - raw_surplus",
        ),
        row(
            "ZeroRowIffExactRawRejectionBalance",
            True,
            True,
            "零行反例等价于 rejection_total 与 raw_surplus_over_row 精确相等。",
            "zero row exact balance",
        ),
        row(
            "RawCapacityOnlyContradictionRejected",
            True,
            True,
            "原始命中容量通常超过行长；超容量可被非 owner 拒绝吸收，不能单独推出正性。",
            "need strict rejection excess",
        ),
        row(
            "PositiveRejectionExcessProved",
            False,
            False,
            "尚未证明每条严格行都有 rejection_total > raw_surplus_over_row。",
            "same full-root uncovered-slot positivity",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把正缺陷改写为 raw/rejection 失衡；未排除精确平衡。",
            "Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sample_audits = [
        raw_rejection_balance_audit(5, 4),
        raw_rejection_balance_audit(11, 10),
        raw_rejection_balance_audit(17, 16),
        raw_rejection_balance_audit(101, 50),
        raw_rejection_balance_audit(101, 100),
    ]
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_raw_rejection_balance_router",
        "status": "strict_k_raw_rejection_balance_identity_closed_but_strict_excess_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "raw_incidence_owner_rejection_partition_proved": True,
        "prime_count_equals_rejection_excess_proved": True,
        "zero_row_iff_exact_raw_rejection_balance_proved": True,
        "raw_capacity_only_contradiction_rejected": True,
        "positive_rejection_excess_proved": False,
        "row_column_unconditional_closed": False,
        "identity": (
            "RawTotal=OwnerMass+RejectionMass, "
            "row_prime_count=RejectionMass-(RawTotal-(P-1))"
        ),
        "zero_row_condition": (
            "zero row iff RejectionMass=RawTotal-(P-1), "
            "positive row iff RejectionMass>RawTotal-(P-1)"
        ),
        "sample_audits": sample_audits,
        "finite_sweep": finite_sweep(),
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "严格 1<k<P 的内部行中，若先数所有根内素数的原始命中，再把非 LPF-owner 的命中作为"
            "已由更小素因子筛掉的拒绝量，则行内素数数目精确等于拒绝量超过原始超容量的差。"
            "零行反例因此不是普通容量饱和，而是 raw surplus 与 LPF rejection 的精确临界平衡。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k raw rejection balance 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. Raw / rejection 平衡恒等式",
        "",
        "```text",
        result["identity"],
        result["zero_row_condition"],
        "```",
        "",
        "这里 `RawTotal` 是所有 `p<=sqrt(kP+P-1)` 且 `p | kP+a` 的原始命中总数；",
        "`OwnerMass` 是 LPF-owner 总质量；`RejectionMass` 是那些命中里不是最小素因子的部分。",
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
            "| P | k | interval | raw total | owner | rejection | raw surplus | prime count | rejection excess | identities |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for audit in result["sample_audits"]:
        identities = (
            audit["raw_equals_owner_plus_rejection"]
            and audit["prime_equals_rejection_minus_raw_surplus"]
            and audit["zero_row_iff_rejection_equals_raw_surplus"]
        )
        lines.append(
            f"| {audit['P']} | {audit['k']} | {audit['internal_interval']} | "
            f"{audit['raw_incidence_total']} | {audit['owner_total']} | {audit['rejection_total']} | "
            f"{audit['raw_surplus_over_row']} | {audit['prime_count']} | "
            f"{audit['rejection_excess_over_raw_surplus']} | `{fmt_bool(identities)}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 槽位样本",
            "",
            "| P | k | slot | n | owner | raw hits | rejected hits | prime |",
            "| ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
        ]
    )
    for audit in result["sample_audits"][:3]:
        for item in audit["slot_rows_sample"][:10]:
            lines.append(
                f"| {audit['P']} | {audit['k']} | {item['slot']} | {item['n']} | "
                f"{cell(item['owner'])} | `{item['raw_hits']}` | `{item['rejected_hits']}` | "
                f"`{fmt_bool(item['is_prime'])}` |"
            )
    sweep = result["finite_sweep"]
    lines.extend(
        [
            "",
            "## 5. 有限审计边界",
            "",
            "```text",
            f"max_prime={sweep['max_prime']}",
            f"case_count={sweep['case_count']}",
            f"all_raw_rejection_balance_identities_verified={fmt_bool(sweep['all_raw_rejection_balance_identities_verified'])}",
            f"zero_rows_found_in_finite_sweep={sweep['zero_rows_found_in_finite_sweep']}",
            f"minimum_rejection_excess_over_raw_surplus={sweep['minimum_rejection_excess_over_raw_surplus']}",
            f"maximum_raw_surplus_case={sweep['maximum_raw_surplus_case']}",
            "finite_evidence_not_used_as_global_proof=true",
            "```",
            "",
            "最小 rejection excess 样本：",
            "",
            "| P | k | excess |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in sweep["minimum_rejection_excess_cases"]:
        lines.append(f"| {item['P']} | {item['k']} | {item['excess']} |")
    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "本层把 owner 饱和硬点继续拆成两股完全显式的量：raw incidence 的超容量和 LPF rejection。",
            "若要非循环证明 `[kP,kP+P]` 在 `1<k<P` 时有素数，必须证明 LPF rejection 严格大于 raw surplus。",
            "精确相等就是零行反例。因此下一步最窄口是一个 signed/transport 型的严格失衡定理，",
            "不能由 Phi-LPF 恒等式或样本容量本身推出。",
            "",
            "## 7. 依赖哈希",
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
