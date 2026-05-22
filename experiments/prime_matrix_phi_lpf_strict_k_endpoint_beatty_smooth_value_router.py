#!/usr/bin/env python3
"""生成 strict 行 Phi-LPF 端点差分的 Beatty/smooth 精确值证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_endpoint_beatty_smooth_value_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.md
"""

from __future__ import annotations

from array import array
from bisect import bisect_right
from collections import Counter
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
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


def prime_sieve(n: int) -> bytearray:
    """返回素数标记表。"""
    if n < 2:
        return bytearray(n + 1)
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def spf_upto(n: int) -> array:
    """返回最小素因子表；spf[1]=1。"""
    spf = array("I", range(n + 1))
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


def primes_from_flags(flags: bytearray) -> list[int]:
    """从标记表抽取素数。"""
    return [i for i, is_prime in enumerate(flags) if is_prime]


def prime_prefix(flags: bytearray) -> array:
    """构造 pi(x) 前缀表。"""
    prefix = array("I", [0]) * len(flags)
    count = 0
    for i, is_prime in enumerate(flags):
        if is_prime:
            count += 1
        prefix[i] = count
    return prefix


def pi_between(prefix: array, lower_exclusive: int, upper_inclusive: int) -> int:
    """计算 lower < prime <= upper 的素数个数。"""
    if upper_inclusive <= lower_exclusive:
        return 0
    return int(prefix[upper_inclusive]) - int(prefix[lower_exclusive])


def factor_primes(n: int, spf: array) -> list[int]:
    """返回 n 的不同素因子。"""
    factors: list[int] = []
    while n > 1:
        p = int(spf[n])
        factors.append(p)
        while n % p == 0:
            n //= p
    return factors


def phi_delta_for_owner(p_owner: int, p_len: int, k: int, spf: array) -> int:
    """用 LPF 条件直接读出单个桶的 Phi 端点增量。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    left = lower // p_owner
    right = upper // p_owner
    total = 0
    for q in range(left + 1, right + 1):
        if q == 1 or spf[q] >= p_owner:
            total += 1
    return total


def beatty_slots(primes: list[int], p_len: int, k: int) -> dict[int, dict[str, int]]:
    """计算 Beatty 近倍数源像，键为行内槽位。"""
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    source_upper = upper // 2
    slots: dict[int, dict[str, int]] = {}
    start = bisect_right(primes, p_len)
    stop = bisect_right(primes, source_upper)
    for r in primes[start:stop]:
        residue = lower % r
        # 在 1<k<P 且 r>P 时，r 不整除 kP；slot 是下一倍数距离。
        slot = r - residue
        if 1 <= slot <= p_len - 1:
            n = lower + slot
            m = n // r
            if 2 <= m <= k and m * r == n:
                slots[slot] = {
                    "slot": slot,
                    "n": n,
                    "r": r,
                    "m": m,
                    "source_row": r // p_len,
                    "residue_kp_mod_r": residue,
                }
    return slots


def row_value(primes: list[int], flags: bytearray, prefix: array, spf: array, p_len: int, k: int) -> dict[str, Any]:
    """计算一条 strict 行的端点差分与 Beatty/smooth 分解。"""
    if not (1 < k < p_len):
        raise ValueError("本证书要求 1<k<P")
    lower = k * p_len
    upper = (k + 1) * p_len - 1
    length = p_len - 1
    prime_slots: list[int] = []
    smooth_slots: list[int] = []
    high_payment_slots: list[int] = []
    owner_counts: Counter[int] = Counter()

    for slot in range(1, p_len):
        n = lower + slot
        if flags[n]:
            prime_slots.append(slot)
            continue
        factors = factor_primes(n, spf)
        owner_counts[min(factors)] += 1
        if any(q > p_len for q in factors):
            high_payment_slots.append(slot)
        else:
            smooth_slots.append(slot)

    beatty = beatty_slots(primes, p_len, k)
    beatty_slot_list = sorted(beatty)
    high_payment_slot_list = sorted(high_payment_slots)
    endpoint_prime_count = pi_between(prefix, lower, upper)
    composite_delta = sum(owner_counts.values())
    beatty_count = len(beatty_slot_list)
    smooth_count = len(smooth_slots)
    prime_count = len(prime_slots)
    positive_condition_holds = beatty_count + smooth_count <= p_len - 2
    bucket_rows = [
        {
            "p": p,
            "owner_delta": owner_counts[p],
            "phi_delta_by_lpf_condition": phi_delta_for_owner(p, p_len, k, spf),
        }
        for p in sorted(owner_counts)
    ]
    return {
        "P": p_len,
        "k": k,
        "internal_interval": [lower + 1, upper],
        "length": length,
        "endpoint_prime_count": endpoint_prime_count,
        "direct_prime_count": prime_count,
        "phi_lpf_composite_delta": composite_delta,
        "beatty_payment_count": beatty_count,
        "p_smooth_count": smooth_count,
        "beatty_plus_smooth": beatty_count + smooth_count,
        "exact_value_formula_count": length - beatty_count - smooth_count,
        "endpoint_equals_direct": endpoint_prime_count == prime_count,
        "composite_delta_equals_beatty_plus_smooth": composite_delta == beatty_count + smooth_count,
        "beatty_slots_equal_high_payment_slots": beatty_slot_list == high_payment_slot_list,
        "partition_identity_holds": length == prime_count + beatty_count + smooth_count,
        "positive_iff_beatty_smooth_below_full": (prime_count > 0) == positive_condition_holds,
        "positive_condition": f"{beatty_count}+{smooth_count}<={p_len - 2}",
        "prime_slots_sample": prime_slots[:20],
        "smooth_slots_sample": smooth_slots[:20],
        "beatty_slots_sample": [
            beatty[slot] for slot in beatty_slot_list[:8]
        ],
        "owner_bucket_sample": bucket_rows[:12],
        "all_owner_phi_deltas_match": all(
            item["owner_delta"] == item["phi_delta_by_lpf_condition"] for item in bucket_rows
        ),
    }


def finite_sweep(max_prime: int = 257) -> dict[str, Any]:
    """有限审计精确值公式；不作为全局证明。"""
    sample_pairs = [(11, 10), (101, 50), (101, 100), (257, 244), (571, 438), (1009, 1008)]
    sieve_prime = max(max_prime, max(p for p, _k in sample_pairs))
    flags = prime_sieve(sieve_prime * sieve_prime)
    prefix = prime_prefix(flags)
    spf = spf_upto(sieve_prime * sieve_prime)
    primes = primes_from_flags(flags)
    strict_primes = [p for p in primes if 5 <= p <= max_prime]

    row_count = 0
    identity_failures: list[dict[str, Any]] = []
    zero_rows_found: list[dict[str, int]] = []
    min_prime_count: int | None = None
    min_prime_cases: list[dict[str, int]] = []
    max_composite_fill = {"value": -1.0, "cases": []}
    max_beatty = {"value": -1.0, "cases": []}
    max_smooth = {"value": -1.0, "cases": []}

    for p_len in strict_primes:
        for k in range(2, p_len):
            row_count += 1
            value = row_value(primes, flags, prefix, spf, p_len, k)
            ok = (
                value["endpoint_equals_direct"]
                and value["composite_delta_equals_beatty_plus_smooth"]
                and value["beatty_slots_equal_high_payment_slots"]
                and value["partition_identity_holds"]
                and value["positive_iff_beatty_smooth_below_full"]
                and value["all_owner_phi_deltas_match"]
            )
            if not ok and len(identity_failures) < 8:
                identity_failures.append(value)
            prime_count = value["direct_prime_count"]
            if prime_count == 0 and len(zero_rows_found) < 32:
                zero_rows_found.append({"P": p_len, "k": k})
            if min_prime_count is None or prime_count < min_prime_count:
                min_prime_count = prime_count
                min_prime_cases = [{"P": p_len, "k": k, "prime_count": prime_count}]
            elif prime_count == min_prime_count and len(min_prime_cases) < 16:
                min_prime_cases.append({"P": p_len, "k": k, "prime_count": prime_count})

            case = {
                "P": p_len,
                "k": k,
                "prime_count": prime_count,
                "beatty": value["beatty_payment_count"],
                "smooth": value["p_smooth_count"],
                "fill": value["beatty_plus_smooth"] / value["length"],
            }
            fill = value["beatty_plus_smooth"] / value["length"]
            beatty_ratio = value["beatty_payment_count"] / value["length"]
            smooth_ratio = value["p_smooth_count"] / value["length"]
            for bucket, ratio in (
                (max_composite_fill, fill),
                (max_beatty, beatty_ratio),
                (max_smooth, smooth_ratio),
            ):
                if ratio > bucket["value"]:
                    bucket["value"] = ratio
                    bucket["cases"] = [case]
                elif ratio == bucket["value"] and len(bucket["cases"]) < 8:
                    bucket["cases"].append(case)

    sample_rows = [row_value(primes, flags, prefix, spf, p, k) for p, k in sample_pairs]
    return {
        "max_prime": max_prime,
        "sieve_prime_for_large_samples": sieve_prime,
        "strict_row_count": row_count,
        "all_endpoint_beatty_smooth_value_identities_hold": not identity_failures,
        "identity_failures": identity_failures,
        "zero_rows_found_in_finite_sweep": zero_rows_found,
        "all_rows_positive_in_finite_sweep": not zero_rows_found,
        "minimum_prime_count": min_prime_count,
        "minimum_prime_cases": min_prime_cases,
        "max_composite_fill": max_composite_fill,
        "max_beatty_ratio": max_beatty,
        "max_smooth_ratio": max_smooth,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "EndpointDifferenceExactValueClosed",
            True,
            True,
            "Phi-LPF 端点差分给出 N_P(k)=pi((k+1)P-1)-pi(kP) 的精确值。",
            "exact interval value",
        ),
        row(
            "BeattySmoothCompositeSplitClosed",
            True,
            True,
            "在 1<k<P 时，每个合数槽唯一落入 P-smooth 槽或 Beatty high-prime payment 槽。",
            "composite split",
        ),
        row(
            "ExactValueAsPMinusBeattyMinusSmoothClosed",
            True,
            True,
            "N_P(k)=(P-1)-B_P(k)-S_P(k)，其中 B_P(k) 是 Beatty 源像，S_P(k) 是 P-smooth 槽。",
            "row prime count value",
        ),
        row(
            "PositivityEquivalentToBeattySmoothAntiTilingClosed",
            True,
            True,
            "N_P(k)>=1 等价于 B_P(k)+S_P(k)<=P-2。",
            "same positivity target",
        ),
        row(
            "BeattySmoothAntiTilingInequalityProved",
            False,
            False,
            "当前层没有证明 B_P(k)+S_P(k)<=P-2 对所有 1<k<P 成立。",
            "global anti-tiling inequality",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层给出精确值坐标，不给出 strict 行正性的无条件证明。",
            "anti-tiling, rejection excess, or sqrt-scale input",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def sample_rows_markdown(sample_rows: list[dict[str, Any]]) -> str:
    """输出样本行 Markdown。"""
    lines = [
        "| P | k | N_P(k) | B Beatty | S smooth | B+S | P-1 | formula ok | first prime slots |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for item in sample_rows:
        lines.append(
            "| {P} | {k} | {n} | {b} | {s} | {bs} | {length} | `{ok}` | {slots} |".format(
                P=item["P"],
                k=item["k"],
                n=item["direct_prime_count"],
                b=item["beatty_payment_count"],
                s=item["p_smooth_count"],
                bs=item["beatty_plus_smooth"],
                length=item["length"],
                ok=fmt_bool(item["exact_value_formula_count"] == item["direct_prime_count"]),
                slots=", ".join(map(str, item["prime_slots_sample"][:8])),
            )
        )
    return "\n".join(lines)


def cases_markdown(cases: list[dict[str, Any]]) -> str:
    """压缩输出若干极值样本。"""
    if not cases:
        return "无"
    return "; ".join(
        f"P={case['P']}, k={case['k']}, prime={case['prime_count']}, "
        f"B={case['beatty']}, S={case['smooth']}, fill={case['fill']:.6f}"
        for case in cases
    )


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    sweep = finite_sweep()
    rows = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    payload = {
        "status": "strict_k_endpoint_difference_rewritten_as_beatty_smooth_exact_value",
        "formula": {
            "N_P(k)": "pi((k+1)P-1)-pi(kP)",
            "Phi_LPF": "N_P(k)=(P-1)-sum_{p<=sqrt((k+1)P-1)}[Phi(floor(((k+1)P-1)/p),p)-Phi(floor(kP/p),p)]",
            "Beatty_smooth": "N_P(k)=(P-1)-B_P(k)-S_P(k)",
            "Beatty_B": "#{prime r>P: r-(kP mod r) in [1,P-1]}",
            "positivity": "N_P(k)>=1 iff B_P(k)+S_P(k)<=P-2",
        },
        "finite_sweep": sweep,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "Phi-LPF 端点差分能给出 [kP,kP+P] 内部行素数个数的精确值；"
            "结合 Beatty 源表后，该值等于 (P-1)-B_P(k)-S_P(k)。"
            "正性剩余不是计数恒等式问题，而是 Beatty 源像与 P-smooth 槽不能铺满全部槽的全局不等式。"
        ),
    }
    return payload


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    sweep = payload["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k endpoint Beatty-smooth exact value 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "本层把用户要求的 `[kP,kP+P]` 端点差计数同最新 Beatty payment 源表合并。结论是：",
        "",
        "```text",
        "N_P(k)=pi((k+1)P-1)-pi(kP)",
        "      =(P-1)-sum_{p<=sqrt((k+1)P-1)}[Phi(floor(((k+1)P-1)/p),p)-Phi(floor(kP/p),p)]",
        "      =(P-1)-B_P(k)-S_P(k).",
        "```",
        "",
        "其中 `B_P(k)` 是 Beatty 近倍数 high-prime payment 源像，`S_P(k)` 是行内 `P`-smooth 合数槽。",
        "因此正性精确等价于：",
        "",
        "```text",
        "N_P(k)>=1  iff  B_P(k)+S_P(k)<=P-2.",
        "```",
        "",
        "这一步给出精确值坐标，但不自动证明该不等式；未证部分正是 Beatty/smooth 反铺满硬点。",
        "",
        "## 1. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"strict_row_count={sweep['strict_row_count']}",
        f"all_endpoint_beatty_smooth_value_identities_hold={fmt_bool(sweep['all_endpoint_beatty_smooth_value_identities_hold'])}",
        f"all_rows_positive_in_finite_sweep={fmt_bool(sweep['all_rows_positive_in_finite_sweep'])}",
        f"minimum_prime_count={sweep['minimum_prime_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "最接近铺满的有限样本：",
        "",
        "```text",
        f"max_composite_fill={sweep['max_composite_fill']['value']:.6f}",
        cases_markdown(sweep["max_composite_fill"]["cases"]),
        "```",
        "",
        "## 2. 样本行",
        "",
        sample_rows_markdown(sweep["sample_rows"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前层关闭的是端点差精确值与 Beatty/smooth 分解，不是 strict 行正性的无条件证明。",
        "下一步最窄接口仍是 `BeattySmoothAntiTilingInequality`、",
        "`PositiveRejectionExcessForStrictKRawLPFIncidence` 或真正的 `SqrtGapInputAfterX`。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
