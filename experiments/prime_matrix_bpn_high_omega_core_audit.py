#!/usr/bin/env python3
"""BPN-B5 高重小素因子核心审计。

用法示例：
  python3 experiments/prime_matrix_bpn_high_omega_core_audit.py

`BPN-B5` 已化为：

  S5(row)=prime_like_count(row)-high_omega_penalty(row).

本脚本专门分析 `high_omega_penalty` 的来源：
- 只统计边界行中含至少 6 个 `<P` 不同小素因子的数；
- 记录六个最小小素因子的乘积 core6；
- 按 core6 与 P 的相对大小分桶。

目标是判断下一步能否走“小核心乘积过密 => Tail-anchor/CRTDefect”路线。
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    value = 2
    while value * value <= limit:
        if sieve[value]:
            start = value * value
            sieve[start : limit + 1 : value] = b"\x00" * (
                ((limit - start) // value) + 1
            )
        value += 1
    return [value for value, ok in enumerate(sieve) if ok]


def small_prime_factors(value: int, primes: list[int]) -> list[int]:
    """列出 value 的不同小素因子。"""
    factors = []
    for prime in primes:
        if prime * prime > value and value < prime * prime:
            pass
        if value % prime == 0:
            factors.append(prime)
    return factors


def s5_weight_from_omega(omega: int) -> int:
    """五阶逐点权重。"""
    if omega == 0:
        return 1
    if omega <= 5:
        return 0
    return -comb(omega - 1, 5)


def classify_core(p: int, core: int) -> str:
    """按 core6 大小分桶。"""
    if core <= p:
        return "<=P"
    if core <= 2 * p:
        return "<=2P"
    if core <= p * p // 4:
        return "<=P^2/4"
    if core <= p * p // 2:
        return "<=P^2/2"
    return "<P^2"


def row_s5_summary(p: int, row: int, primes: list[int]) -> dict:
    """计算一行的 S5 与高重核心画像。"""
    prime_like = 0
    penalty = 0
    omega_hist: dict[int, int] = {}
    core_bins: dict[str, dict] = {}
    samples = []
    for value in range((row - 1) * p + 1, row * p):
        factors = small_prime_factors(value, primes)
        omega = len(factors)
        omega_hist[omega] = omega_hist.get(omega, 0) + 1
        if omega == 0:
            prime_like += 1
        if omega >= 6:
            weight = comb(omega - 1, 5)
            penalty += weight
            core = 1
            for factor in factors[:6]:
                core *= factor
            bucket = classify_core(p, core)
            current = core_bins.setdefault(
                bucket,
                {
                    "count": 0,
                    "penalty": 0,
                    "min_core": core,
                    "max_core": core,
                },
            )
            current["count"] += 1
            current["penalty"] += weight
            current["min_core"] = min(current["min_core"], core)
            current["max_core"] = max(current["max_core"], core)
            if len(samples) < 12:
                samples.append(
                    {
                        "n": value,
                        "omega": omega,
                        "weight": weight,
                        "first_factors": factors[:10],
                        "core6": core,
                        "bucket": bucket,
                    }
                )
    return {
        "row": row,
        "prime_like": prime_like,
        "high_omega_penalty": penalty,
        "s5": prime_like - penalty,
        "omega_hist": dict(sorted(omega_hist.items())),
        "core_bins": dict(sorted(core_bins.items())),
        "samples": samples,
    }


def find_min_s5_row(p: int) -> int:
    """用 omega 筛快速寻找最小 S5 行。"""
    omega = bytearray(p * p)
    for prime in primes_upto(p - 1):
        for multiple in range(prime, p * p, prime):
            omega[multiple] += 1
    min_s5 = None
    min_row = None
    for row in range(2, p + 1):
        row_s5 = 0
        for value in range((row - 1) * p + 1, row * p):
            row_s5 += s5_weight_from_omega(omega[value])
        if min_s5 is None or row_s5 < min_s5:
            min_s5 = row_s5
            min_row = row
    if min_row is None:
        raise ValueError(f"no rows for P={p}")
    return min_row


def audit_prime(p: int) -> dict:
    """审计单个 P。"""
    primes = primes_upto(p - 1)
    min_row = find_min_s5_row(p)
    rows = sorted({min_row, max(2, p // 2), p - 1, p})
    return {
        "p": p,
        "min_s5_row": min_row,
        "row_reports": [row_s5_summary(p, row, primes) for row in rows],
    }


def run_audit() -> dict:
    """运行审计。"""
    results = [audit_prime(p) for p in (503, 1009, 2003, 5003)]
    return {
        "certificate_type": "prime_matrix_bpn_high_omega_core_audit",
        "status": "high_omega_penalty_has_small_core_tail_anchor_structure",
        "results": results,
        "structural_conclusion": (
            "BPN-B5 的负项集中在含至少六个小素因子的数。"
            "这些数都有六小素核心 core6<P^2；样本最薄行的高重惩罚可按 core6 桶分解。"
            "这支持下一步把惩罚过大转化为小核心乘积过密或 Tail-anchor/CRTDefect。"
        ),
        "next_obligations": [
            "证明高重惩罚若超过素数数目，则某个 core6 桶在长度 P 窗口中过密。",
            "将 core6 过密改写为固定小核心 d 的短倍数/尾锚集中。",
            "证明该集中触发 CRTDefect/Tail-anchor，或给出可吸收的统一上界。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# BPN-B5 高重小素因子核心审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        "## 1. 结构恒等式",
        "",
        "五阶下界已经化为",
        "",
        "\\[",
        "S_5(I)=\\#\\{n\\in I:\\omega_P(n)=0\\}",
        "-\\sum_{n\\in I,\\omega_P(n)\\ge6}\\binom{\\omega_P(n)-1}{5}.",
        "\\]",
        "",
        "在边界帽 `n<P^2` 中，第一项就是该行内素数数目。第二项的每个贡献都有六小素核心",
        "",
        "\\[",
        "core_6(n)=q_1q_2q_3q_4q_5q_6<P^2.",
        "\\]",
        "",
        "若第二项过大，则某类 `core_6` 桶必须在短窗中过密。",
        "",
        "## 2. 审计总表",
        "",
        "| P | min S5 row | row | prime_like | penalty | S5 | core bins |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in audit["results"]:
        for report in item["row_reports"]:
            lines.append(
                "| {p} | {minrow} | {row} | {prime} | {penalty} | {s5} | `{bins}` |".format(
                    p=item["p"],
                    minrow=item["min_s5_row"],
                    row=report["row"],
                    prime=report["prime_like"],
                    penalty=report["high_omega_penalty"],
                    s5=report["s5"],
                    bins=report["core_bins"],
                )
            )
    lines.extend(["", "## 3. 最薄行样本", ""])
    for item in audit["results"]:
        report = next(
            row for row in item["row_reports"] if row["row"] == item["min_s5_row"]
        )
        lines.append(f"### P={item['p']}, row={report['row']}")
        lines.append(f"- omega_hist=`{report['omega_hist']}`")
        lines.append(f"- samples=`{report['samples']}`")
        lines.append("")
    lines.extend(["## 4. 后续义务", ""])
    for obligation in audit["next_obligations"]:
        lines.append(f"- {obligation}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-bpn-high-omega-core-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(
        json.dumps(
            {
                item["p"]: {
                    "min_s5_row": item["min_s5_row"],
                    "min_report": next(
                        row
                        for row in item["row_reports"]
                        if row["row"] == item["min_s5_row"]
                    ),
                }
                for item in audit["results"]
            },
            ensure_ascii=False,
            indent=2,
        )[:4000]
    )


if __name__ == "__main__":
    main()
