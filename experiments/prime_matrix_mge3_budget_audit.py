#!/usr/bin/env python3
"""M_{>=3} 多粗因子预算审计。

用法示例：
  python3 experiments/prime_matrix_mge3_budget_audit.py
  python3 experiments/prime_matrix_mge3_budget_audit.py --max-p 2000 --alpha 0.43
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-mge3-budget-audit.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-mge3-budget-audit.md"


def sieve(n: int) -> bytearray:
    """返回不超过 n 的素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    p = 2
    while p * p <= n:
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return flags


def primes_from_flags(flags: bytearray) -> list[int]:
    """从素数标记表抽取素数。"""
    return [i for i in range(2, len(flags)) if flags[i]]


def smallest_prime_factor(n: int) -> list[int]:
    """构造最小素因子表。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
        p += 1
    return spf


def factorization(n: int, spf: list[int]) -> list[int]:
    """返回带重数素因子分解。"""
    factors: list[int] = []
    while n > 1:
        p = spf[n]
        factors.append(p)
        n //= p
    return factors


def row_interval(width: int, row: int) -> tuple[int, int]:
    """返回方阵第 row 行对应的闭区间。"""
    return (row - 1) * width + 1, row * width


def contains_full_p_row(p: int, left: int, right: int) -> bool:
    """判断区间是否含完整旧 p 行。"""
    first_t = (left - 1 + p - 1) // p
    block_left = first_t * p + 1
    block_right = (first_t + 1) * p
    return block_left >= left and block_right <= right


def sampled_windows(p: int, q: int, tail_fraction: float) -> list[tuple[int, int, int, int]]:
    """列出后排 ASB 采样窗口。"""
    g = q - p
    last_full_q_row = (p * p) // q
    tail_start = max(1, int((1.0 - tail_fraction) * last_full_q_row))
    windows = []
    for s in range(tail_start, last_full_q_row + 1):
        left, right = row_interval(q, s)
        if contains_full_p_row(p, left, right):
            continue
        r = (left - 1) % p
        if r <= g:
            continue
        windows.append((s, left, right, r))
    return windows


def ceil_div(a: int, b: int) -> int:
    """整数上取整除法。"""
    return -(-a // b)


def beta_bucket(anchor: int, p: int, alpha: float) -> str:
    """按 anchor≈p^beta 分桶。"""
    beta = math.log(anchor) / math.log(p)
    edges = [alpha, 0.50, 0.60, 2.0 / 3.0, 0.80, 1.01]
    labels = ["[α,0.50)", "[0.50,0.60)", "[0.60,2/3)", "[2/3,0.80)", "[0.80,1.01)"]
    for label, lo, hi in zip(labels, edges, edges[1:]):
        if lo <= beta < hi:
            return label
    return "outside"


def classify_window(
    p: int,
    q: int,
    z: int,
    q_row: int,
    left: int,
    right: int,
    r: int,
    prime_flags: bytearray,
    spf: list[int],
) -> dict[str, Any]:
    """分类一个 ASB 窗口中的低筛粗剩余。"""
    rough_count = 0
    prime_count = 0
    semiprime_count = 0
    mge3_count = 0
    repeated_mge3_count = 0
    omega_counts: dict[str, int] = {}
    max_anchor_beta = 0.0
    max_anchor = None
    examples = []
    identity_violations = 0

    for n in range(left, right + 1):
        if spf[n] <= z:
            continue
        rough_count += 1
        if prime_flags[n]:
            prime_count += 1
            continue
        factors = factorization(n, spf)
        omega = len(factors)
        omega_counts[str(omega)] = omega_counts.get(str(omega), 0) + 1
        if omega == 2:
            semiprime_count += 1
            continue
        mge3_count += 1
        anchor = factors[0]
        cofactor = n // anchor
        anchor_beta = math.log(anchor) / math.log(p)
        if anchor_beta > max_anchor_beta:
            max_anchor_beta = anchor_beta
            max_anchor = anchor
        if len(set(factors)) < len(factors):
            repeated_mge3_count += 1
        if not (cofactor > 1 and not prime_flags[cofactor] and spf[cofactor] >= anchor):
            identity_violations += 1
        if len(examples) < 8:
            examples.append({"n": n, "factors": factors, "anchor": anchor, "cofactor": cofactor})

    composite_count = rough_count - prime_count
    return {
        "p": p,
        "q": q,
        "z": z,
        "q_row": q_row,
        "left": left,
        "right": right,
        "r": r,
        "rough_count": rough_count,
        "prime_count": prime_count,
        "composite_count": composite_count,
        "semiprime_count": semiprime_count,
        "mge3_count": mge3_count,
        "other_check": composite_count - semiprime_count - mge3_count,
        "prime_ratio": None if rough_count == 0 else prime_count / rough_count,
        "mge3_share_of_rough": None if rough_count == 0 else mge3_count / rough_count,
        "mge3_share_of_composites": None if composite_count == 0 else mge3_count / composite_count,
        "semiprime_share_of_composites": None if composite_count == 0 else semiprime_count / composite_count,
        "repeated_mge3_count": repeated_mge3_count,
        "omega_counts": omega_counts,
        "max_anchor": max_anchor,
        "max_anchor_beta": max_anchor_beta,
        "identity_violations": identity_violations,
        "examples": examples,
    }


def collect_hard_windows(
    max_p: int,
    alpha: float,
    tail_fraction: float,
    keep: int,
    prime_flags: bytearray,
    spf: list[int],
) -> list[dict[str, Any]]:
    """收集 RPD 压力最大的窗口。"""
    small_flags = sieve(max_p + 200)
    base_primes = [p for p in primes_from_flags(small_flags) if p >= 3]
    rows = []
    for p, q in zip(base_primes, base_primes[1:]):
        if p > max_p:
            break
        z = max(2, int(p**alpha))
        for q_row, left, right, r in sampled_windows(p, q, tail_fraction):
            row = classify_window(p, q, z, q_row, left, right, r, prime_flags, spf)
            if row["rough_count"]:
                rows.append(row)
    rows.sort(key=lambda row: (row["prime_ratio"], -row["rough_count"]))
    return rows[:keep]


def audit_mge3_identity(
    hard_windows: list[dict[str, Any]],
    primes: list[int],
    prime_flags: bytearray,
    spf: list[int],
    alpha: float,
) -> dict[str, Any]:
    """用最小锚恒等式审计 M_{>=3}。"""
    buckets: dict[str, dict[str, Any]] = {}
    identity_total = 0
    integer_capacity_total = 0
    for window in hard_windows:
        p = window["p"]
        z = window["z"]
        left = window["left"]
        right = window["right"]
        max_anchor = int(round(right ** (1.0 / 3.0))) + 2
        for anchor in primes:
            if anchor <= z:
                continue
            if anchor > max_anchor:
                break
            co_left = max(anchor * anchor, ceil_div(left, anchor))
            co_right = right // anchor
            capacity = max(0, co_right - co_left + 1)
            if capacity == 0:
                continue
            bucket = beta_bucket(anchor, p, alpha)
            entry = buckets.setdefault(
                bucket,
                {
                    "anchor_interval_count": 0,
                    "integer_capacity": 0,
                    "mge3_count": 0,
                    "distinct_anchors": set(),
                    "max_anchor": 0,
                    "max_beta": 0.0,
                },
            )
            entry["anchor_interval_count"] += 1
            entry["integer_capacity"] += capacity
            entry["distinct_anchors"].add(anchor)
            entry["max_anchor"] = max(entry["max_anchor"], anchor)
            entry["max_beta"] = max(entry["max_beta"], math.log(anchor) / math.log(p))
            integer_capacity_total += capacity
            for cofactor in range(co_left, co_right + 1):
                if prime_flags[cofactor]:
                    continue
                if spf[cofactor] < anchor:
                    continue
                entry["mge3_count"] += 1
                identity_total += 1

    rendered = []
    for name, entry in sorted(buckets.items()):
        rendered.append(
            {
                "bucket": name,
                "anchor_interval_count": entry["anchor_interval_count"],
                "integer_capacity": entry["integer_capacity"],
                "mge3_count": entry["mge3_count"],
                "capacity_efficiency": None
                if entry["integer_capacity"] == 0
                else entry["mge3_count"] / entry["integer_capacity"],
                "distinct_anchor_count": len(entry["distinct_anchors"]),
                "max_anchor": entry["max_anchor"],
                "max_beta": entry["max_beta"],
            }
        )

    classified_total = sum(row["mge3_count"] for row in hard_windows)
    return {
        "classified_mge3_total": classified_total,
        "identity_mge3_total": identity_total,
        "identity_gap": identity_total - classified_total,
        "integer_capacity_total": integer_capacity_total,
        "capacity_efficiency": None
        if integer_capacity_total == 0
        else identity_total / integer_capacity_total,
        "buckets": rendered,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成 M_{>=3} 多粗因子预算审计。"""
    small_flags = sieve(max_p + 200)
    max_q = max(primes_from_flags(small_flags))
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    primes = primes_from_flags(prime_flags)
    hard_windows = collect_hard_windows(max_p, alpha, tail_fraction, keep, prime_flags, spf)
    aggregate = {
        "hard_window_count": len(hard_windows),
        "rough_count": sum(row["rough_count"] for row in hard_windows),
        "prime_count": sum(row["prime_count"] for row in hard_windows),
        "composite_count": sum(row["composite_count"] for row in hard_windows),
        "semiprime_count": sum(row["semiprime_count"] for row in hard_windows),
        "mge3_count": sum(row["mge3_count"] for row in hard_windows),
        "identity_violations": sum(row["identity_violations"] for row in hard_windows),
        "other_check": sum(row["other_check"] for row in hard_windows),
    }
    aggregate["mge3_share_of_rough"] = (
        None if aggregate["rough_count"] == 0 else aggregate["mge3_count"] / aggregate["rough_count"]
    )
    aggregate["mge3_share_of_composites"] = (
        None if aggregate["composite_count"] == 0 else aggregate["mge3_count"] / aggregate["composite_count"]
    )
    aggregate["semiprime_share_of_composites"] = (
        None if aggregate["composite_count"] == 0 else aggregate["semiprime_count"] / aggregate["composite_count"]
    )
    identity = audit_mge3_identity(hard_windows, primes, prime_flags, spf, alpha)
    return {
        "certificate_type": "prime_matrix_mge3_budget_audit",
        "status": "mge3_reduced_to_low_anchor_composite_cofactor_budget",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "hard_aggregate": aggregate,
        "identity_audit": identity,
        "worst_mge3_windows": sorted(
            hard_windows, key=lambda row: (row["mge3_share_of_composites"], row["mge3_count"]), reverse=True
        )[:12],
        "review_conclusion": (
            "M_{>=3} 项有精确最小锚恒等式，锚必落在 z<a<=R^{1/3}。"
            "因此它不是高锚层压力，而是低锚-复合互补因子预算；"
            "若该预算失败，就必须表现为低锚复合互补因子密度异常。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    aggregate = audit["hard_aggregate"]
    identity = audit["identity_audit"]
    lines = [
        "# M_{>=3} 多粗因子预算审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告处理互补素数短区间接口之外的剩余项 `M_{>=3}(J)`：低筛粗剩余中至少含三个粗素因子的合数。",
        "",
        "## 1. 精确最小锚恒等式",
        "",
        "若 `n in R_z(J)` 且 `n` 至少有三个素因子，取最小素因子 `a=P^-(n)`，写 `n=a c`。则 `c` 必为合数且 `P^-(c)>=a`。反过来，任何这样的 `(a,c)` 都给出一个 `M_{>=3}` 点。因此",
        "",
        "\\[",
        "M_{\\ge3}(J)=\\sum_{z<a\\le R^{1/3}}",
        "\\#\\{c:\\lceil L/a\\rceil\\le c\\le\\lfloor R/a\\rfloor,\\ c\\ \\text{composite},\\ P^-(c)\\ge a\\}.",
        "\\]",
        "",
        "这一步是恒等式，不是启发式。它把剩余预算从高锚层压力转为低锚复合互补因子计数。",
        "",
        "## 2. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 最坏窗口数：`{params['keep']}`。",
        "",
        "## 3. 总体账本",
        "",
        f"- 低筛粗剩余：`{aggregate['rough_count']}`。",
        f"- 粗剩余素数：`{aggregate['prime_count']}`。",
        f"- 粗合数：`{aggregate['composite_count']}`。",
        f"- 粗半素数：`{aggregate['semiprime_count']}`，占粗合数 `{aggregate['semiprime_share_of_composites']:.6f}`。",
        f"- `M_{{>=3}}`：`{aggregate['mge3_count']}`，占粗合数 `{aggregate['mge3_share_of_composites']:.6f}`，占粗剩余 `{aggregate['mge3_share_of_rough']:.6f}`。",
        f"- 恒等式校验差：`{identity['identity_gap']}`。",
        f"- 分解异常数：`{aggregate['identity_violations']}`。",
        "",
        "## 4. 最小锚容量分层",
        "",
        "| 锚层 | 锚-窗口数 | 整数容量 | M>=3数 | 容量效率 | 不同锚数 | 最大锚 | 最大beta |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in identity["buckets"]:
        lines.append(
            f"| `{row['bucket']}` | {row['anchor_interval_count']} | {row['integer_capacity']} | "
            f"{row['mge3_count']} | {row['capacity_efficiency']:.6f} | "
            f"{row['distinct_anchor_count']} | {row['max_anchor']} | {row['max_beta']:.6f} |"
        )
    lines += [
        "",
        "## 5. M>=3 压力最高窗口",
        "",
        "| p | q行 | J | rough | prime | semiprime | M>=3 | M>=3/composite | 最大锚beta |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in audit["worst_mge3_windows"]:
        lines.append(
            f"| {row['p']} | {row['q_row']} | `[{row['left']},{row['right']}]` | "
            f"{row['rough_count']} | {row['prime_count']} | {row['semiprime_count']} | "
            f"{row['mge3_count']} | {row['mge3_share_of_composites']:.6f} | "
            f"{row['max_anchor_beta']:.6f} |"
        )
    lines += [
        "",
        "## 6. 新接口",
        "",
        "`M_{>=3}` 已不应再作为黑箱项保留。它的最小可审稿接口是：",
        "",
        "```text",
        "Low-anchor composite-cofactor bound",
        "or low-anchor cofactor density spike => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "与互补素数短区间接口合并后，ASB/RPD 的剩余证明义务变为：",
        "",
        "```text",
        "prime-cofactor interval bound",
        "+ low-anchor composite-cofactor bound",
        "or corresponding density spikes => CRTDefect/Tail-anchor/OSPC.",
        "```",
        "",
        "## 7. 审稿结论",
        "",
        audit["review_conclusion"],
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--tail-fraction", type=float, default=0.25)
    parser.add_argument("--keep", type=int, default=40)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    audit = build_audit(args.max_p, args.alpha, args.tail_fraction, args.keep)
    args.json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    args.md_out.write_text(render_markdown(audit) + "\n")
    print(args.json_out)
    print(args.md_out)


if __name__ == "__main__":
    main()
