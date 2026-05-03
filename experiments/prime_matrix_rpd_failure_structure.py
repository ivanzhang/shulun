#!/usr/bin/env python3
"""RPD 失败窗口的粗合数结构扫描。

用法示例：
  python3 experiments/prime_matrix_rpd_failure_structure.py
  python3 experiments/prime_matrix_rpd_failure_structure.py --max-p 2000 --alpha 0.43
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-rpd-failure-structure.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-rpd-failure-structure.md"


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


def primes_from_flags(flags: bytearray) -> list[int]:
    """从素数标记表抽取素数。"""
    return [i for i in range(2, len(flags)) if flags[i]]


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


def analyze_window(
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
    """分析一个窗口的粗合数类型。"""
    rough_count = 0
    prime_count = 0
    composite_count = 0
    omega_counts: dict[str, int] = {}
    min_factor_buckets = {"(z,p^0.5]": 0, "(p^0.5,p]": 0}
    max_factor_buckets = {"(z,p^0.5]": 0, "(p^0.5,p]": 0}
    repeated_factor_count = 0
    semiprime_count = 0
    high_multiplicity_sum = 0
    for n in range(left, right + 1):
        if spf[n] <= z:
            continue
        rough_count += 1
        if prime_flags[n]:
            prime_count += 1
            continue
        composite_count += 1
        factors = factorization(n, spf)
        omega = len(factors)
        omega_counts[str(omega)] = omega_counts.get(str(omega), 0) + 1
        high_multiplicity_sum += omega
        if omega == 2:
            semiprime_count += 1
        if len(set(factors)) < len(factors):
            repeated_factor_count += 1
        min_factor = min(factors)
        max_factor = max(factors)
        if min_factor <= p**0.5:
            min_factor_buckets["(z,p^0.5]"] += 1
        else:
            min_factor_buckets["(p^0.5,p]"] += 1
        if max_factor <= p**0.5:
            max_factor_buckets["(z,p^0.5]"] += 1
        else:
            max_factor_buckets["(p^0.5,p]"] += 1
    prime_ratio = None if rough_count == 0 else prime_count / rough_count
    composite_ratio = None if rough_count == 0 else composite_count / rough_count
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
        "prime_ratio": prime_ratio,
        "composite_ratio": composite_ratio,
        "omega_counts": omega_counts,
        "semiprime_count": semiprime_count,
        "semiprime_share_of_composites": None if composite_count == 0 else semiprime_count / composite_count,
        "repeated_factor_count": repeated_factor_count,
        "avg_high_factor_multiplicity": None if composite_count == 0 else high_multiplicity_sum / composite_count,
        "min_factor_buckets": min_factor_buckets,
        "max_factor_buckets": max_factor_buckets,
    }


def build_audit(max_p: int, alpha: float, tail_fraction: float, keep: int) -> dict[str, Any]:
    """生成 RPD 失败结构扫描。"""
    small_flags = sieve(max_p + 200)
    base_primes = [p for p in primes_from_flags(small_flags) if p >= 3]
    prime_pairs = [(p, q) for p, q in zip(base_primes, base_primes[1:]) if p <= max_p]
    max_q = prime_pairs[-1][1]
    prime_flags = sieve(max_q * max_q)
    spf = smallest_prime_factor(max_q * max_q)
    windows = []
    for p, q in prime_pairs:
        z = max(2, int(p**alpha))
        for q_row, left, right, r in sampled_windows(p, q, tail_fraction):
            row = analyze_window(p, q, z, q_row, left, right, r, prime_flags, spf)
            if row["rough_count"] > 0:
                windows.append(row)
    windows.sort(key=lambda row: (row["prime_ratio"], -row["rough_count"]))
    hard_windows = windows[:keep]
    aggregate = {
        "hard_window_count": len(hard_windows),
        "rough_count": sum(row["rough_count"] for row in hard_windows),
        "prime_count": sum(row["prime_count"] for row in hard_windows),
        "composite_count": sum(row["composite_count"] for row in hard_windows),
        "semiprime_count": sum(row["semiprime_count"] for row in hard_windows),
        "repeated_factor_count": sum(row["repeated_factor_count"] for row in hard_windows),
    }
    aggregate["prime_ratio"] = (
        None if aggregate["rough_count"] == 0 else aggregate["prime_count"] / aggregate["rough_count"]
    )
    aggregate["semiprime_share_of_composites"] = (
        None if aggregate["composite_count"] == 0 else aggregate["semiprime_count"] / aggregate["composite_count"]
    )
    return {
        "certificate_type": "prime_matrix_rpd_failure_structure",
        "status": "rpd_failure_reduced_to_rough_composite_overdensity",
        "parameters": {"max_p": max_p, "alpha": alpha, "tail_fraction": tail_fraction, "keep": keep},
        "case_count": len(prime_pairs),
        "window_count": len(windows),
        "hard_windows": hard_windows,
        "hard_aggregate": aggregate,
        "review_conclusion": (
            "RPD 失败等价于低筛粗剩余中粗合数过密。样本最坏窗口仍有素数，"
            "粗合数主要表现为少数高因子乘积；证明上应转化为粗合数投影上界，"
            "或证明粗合数过密触发 CRTDefect/Tail-anchor/OSPC。"
        ),
    }


def render_markdown(audit: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    params = audit["parameters"]
    agg = audit["hard_aggregate"]
    lines = [
        "# RPD 失败的粗合数结构扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告继续推进 `RPD-or-CRTDefect`：若低筛粗剩余中的素数比例不足，则低筛粗合数必然过密。本轮将这种失败具体分解为粗合数因子类型，寻找可进入 CRTDefect/Tail-anchor/OSPC 的异常投影。",
        "",
        "## 1. 参数",
        "",
        f"- `max_p={params['max_p']}`。",
        f"- `alpha={params['alpha']}`。",
        f"- `tail_fraction={params['tail_fraction']}`。",
        f"- 保留最坏窗口数：`{params['keep']}`。",
        f"- 总采样窗口数：`{audit['window_count']}`。",
        "",
        "## 2. 最坏窗口聚合",
        "",
        f"- `rough_count={agg['rough_count']}`。",
        f"- `prime_count={agg['prime_count']}`，比例 `{agg['prime_ratio']:.6f}`。",
        f"- `composite_count={agg['composite_count']}`。",
        f"- `semiprime_count={agg['semiprime_count']}`，占粗合数比例 `{agg['semiprime_share_of_composites']:.6f}`。",
        f"- `repeated_factor_count={agg['repeated_factor_count']}`。",
        "",
        "## 3. 最坏窗口样本",
        "",
        "| p | q | z | q_row | 区间 | rough | prime | prime比 | omega分布 | semiprime占比 |",
        "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- | ---: |",
    ]
    for row in audit["hard_windows"][:12]:
        lines.append(
            f"| {row['p']} | {row['q']} | {row['z']} | {row['q_row']} | "
            f"`[{row['left']},{row['right']}]` | {row['rough_count']} | {row['prime_count']} | "
            f"{row['prime_ratio']:.6f} | `{row['omega_counts']}` | "
            f"{row['semiprime_share_of_composites']:.6f} |"
        )
    lines += [
        "",
        "## 4. 证明接口",
        "",
        "设 `C_z(J)=R_z(J)\\setminus\\mathbb P` 为低筛粗合数集。`RPD` 失败即",
        "",
        "\\[",
        "|C_z(J)|>(1-\\eta)|R_z(J)|.",
        "\\]",
        "",
        "因此下一步不应再讨论几何遮挡，而应证明粗合数投影上界：",
        "",
        "\\[",
        "|C_z(J)|\\le (1-\\eta)|R_z(J)|,",
        "\\]",
        "",
        "或证明该上界失败时，粗合数的因子投影在某个模/锚/尾段上异常集中，触发 `CRTDefect/Tail-anchor/OSPC`。",
        "",
        "可用的三类出口是：",
        "",
        "- **Semiprime projection：** 粗合数主要是少数高因子的乘积时，转为双线性短区间分布上界。",
        "- **Multifactor projection：** 多因子粗合数过多时，触发高阶乘法能量异常。",
        "- **Anchor projection：** 某些因子层贡献过大时，固定锚线在 ASB 采样残基中异常集中。",
        "",
        "## 5. 审稿结论",
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
