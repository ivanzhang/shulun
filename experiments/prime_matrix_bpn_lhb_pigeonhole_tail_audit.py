#!/usr/bin/env python3
"""BPN low-hole bucket 鸽巢尾段审计。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_pigeonhole_tail_audit.py
  python3 experiments/prime_matrix_bpn_lhb_pigeonhole_tail_audit.py --max-p 100000

目标：
- 用 `Q=2310` 的周期前缀和精确计算低洞数最大值；
- 用纯鸽巢递推检验固定升序高素数梯是否必然覆盖任意同大小洞集；
- 把 `LHB-7` 的真正剩余压缩到鸽巢递推失败的窄带。
"""

from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import primes_upto


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def coprime_prefix(q: int) -> list[int]:
    """返回两个周期长度上的互素指示前缀和。"""
    period = [1 if gcd(residue, q) == 1 else 0 for residue in range(q)]
    prefix = [0]
    for value in period + period:
        prefix.append(prefix[-1] + value)
    return prefix


def max_low_holes_from_prefix(prefix: list[int], q: int, length: int) -> int:
    """计算任意连续 length 个残基中最多有多少个 Q-互素残基。"""
    full_periods, rest = divmod(length, q)
    period_mass = prefix[q]
    if rest == 0:
        return full_periods * period_mass
    local_max = max(prefix[start + rest] - prefix[start] for start in range(q))
    return full_periods * period_mass + local_max


def pigeonhole_residual(hole_count: int, high_primes: list[int]) -> tuple[int, list[dict[str, int]]]:
    """用最大残基块至少为 ceil(S/ell) 的鸽巢递推得到剩余上界。"""
    residual = hole_count
    steps: list[dict[str, int]] = []
    for prime in high_primes:
        if residual <= 0:
            break
        hit = (residual + prime - 1) // prime
        before = residual
        residual -= hit
        steps.append({"prime": prime, "before": before, "hit": hit, "after": residual})
    return residual, steps


def pigeonhole_residual_until(
    hole_count: int,
    high_primes: list[int],
    upper_prime_bound: int,
) -> tuple[int, int, list[dict[str, int]]]:
    """只使用 `ell<=upper_prime_bound` 的高素数做鸽巢递推。"""
    residual = hole_count
    used = 0
    steps: list[dict[str, int]] = []
    for prime in high_primes:
        if prime > upper_prime_bound or residual <= 0:
            break
        hit = (residual + prime - 1) // prime
        before = residual
        residual -= hit
        used += 1
        steps.append({"prime": prime, "before": before, "hit": hit, "after": residual})
    return residual, used, steps


def scan(max_p: int, q: int, split_denominator: int) -> dict[str, Any]:
    """扫描 `61<=P<=max_p` 的素数。"""
    all_primes = primes_upto(max_p)
    prefix = coprime_prefix(q)
    product_prefix = [1.0] * (max_p + 1)
    product_value = 1.0
    prime_set = set(all_primes)
    for value in range(1, max_p + 1):
        if value in prime_set and q % value != 0:
            product_value *= 1 - 1 / value
        product_prefix[value] = product_value
    rows: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    split_failures: list[dict[str, Any]] = []
    split_tail_failures: list[dict[str, Any]] = []
    product_failures: list[dict[str, Any]] = []
    first_tail_pass: int | None = None

    for p in all_primes:
        if p < 61:
            continue
        high_primes = [prime for prime in all_primes if prime < p and q % prime != 0]
        max_holes = max_low_holes_from_prefix(prefix, q, p - 1)
        residual, steps = pigeonhole_residual(max_holes, high_primes)
        split_bound = p // split_denominator
        split_residual, split_used, split_steps = pigeonhole_residual_until(
            max_holes,
            high_primes,
            split_bound,
        )
        split_remaining_primes = len(high_primes) - split_used
        split_margin = split_remaining_primes - split_residual
        product_lhs = max_holes * product_prefix[split_bound]
        product_rhs = split_remaining_primes
        product_margin = product_rhs - product_lhs
        row = {
            "p": p,
            "max_holes": max_holes,
            "high_prime_count": len(high_primes),
            "pigeonhole_residual": residual,
            "initial_steps": steps[:8],
            "split_denominator": split_denominator,
            "split_bound": split_bound,
            "split_residual": split_residual,
            "split_remaining_primes": split_remaining_primes,
            "split_margin": split_margin,
            "product_lhs": product_lhs,
            "product_rhs": product_rhs,
            "product_margin": product_margin,
            "split_initial_steps": split_steps[:8],
        }
        rows.append(row)
        if residual > 0:
            failures.append(row)
        if split_margin < 0:
            split_failures.append(row)
            if p >= 107:
                split_tail_failures.append(row)
        if product_margin < 0:
            product_failures.append(row)
        elif first_tail_pass is None:
            first_tail_pass = p

    last_failure = failures[-1]["p"] if failures else None
    stable_tail_from = None
    if last_failure is not None:
        for row in rows:
            if row["p"] > last_failure:
                stable_tail_from = row["p"]
                break
    elif rows:
        stable_tail_from = rows[0]["p"]
    last_product_failure = product_failures[-1]["p"] if product_failures else None
    product_stable_from = None
    if last_product_failure is not None:
        for row in rows:
            if row["p"] > last_product_failure:
                product_stable_from = row["p"]
                break
    elif rows:
        product_stable_from = rows[0]["p"]

    return {
        "certificate_type": "prime_matrix_bpn_lhb_pigeonhole_tail",
        "q": q,
        "max_p": max_p,
        "first_tail_pass": first_tail_pass,
        "last_failure": last_failure,
        "stable_tail_from_in_scan": stable_tail_from,
        "failure_count": len(failures),
        "failures": failures,
        "split_denominator": split_denominator,
        "split_failure_count": len(split_failures),
        "split_tail_failure_count": len(split_tail_failures),
        "split_failures": split_failures,
        "split_tail_failures": split_tail_failures,
        "split_min_margin": min((row["split_margin"] for row in rows), default=None),
        "split_tail_min_margin": min(
            (row["split_margin"] for row in rows if row["p"] >= 107),
            default=None,
        ),
        "product_failure_count": len(product_failures),
        "last_product_failure": last_product_failure,
        "product_stable_from_in_scan": product_stable_from,
        "product_failures": product_failures,
        "product_tail_min_margin": min(
            (row["product_margin"] for row in rows if row["p"] >= 233),
            default=None,
        ),
        "finite_tail_rows": [
            row for row in rows if 107 <= row["p"] <= 229
        ],
        "tail_samples": rows[-10:],
        "review_conclusion": (
            "纯鸽巢递推已把 LHB-7 的结构硬点压到低素数窄带："
            "在扫描范围内，最后失败为 P=103，P=107 起鸽巢尾段闭合。"
            "进一步的 P/5 分割判据在 P>=107 的尾段扫描中无失败；"
            "连续乘积上界从 P=233 起在扫描中无失败。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计报告。"""
    lines = [
        "# BPN low-hole bucket 鸽巢尾段审计",
        "",
        result["review_conclusion"],
        "",
        "## 1. 判据",
        "",
        "令 `Hmax(P)` 为长度 `P-1` 的任意 `Q=2310` 连续残基段中最多的互素残基数。",
        "对高素数升序 `ell_1,ell_2,...` 定义递推：",
        "",
        "```text",
        "U_0=Hmax(P)",
        "U_j=U_{j-1}-ceil(U_{j-1}/ell_j)",
        "```",
        "",
        "若最终 `U_j=0`，则任意同大小洞集都被固定升序梯覆盖；这是纯鸽巢充分条件。",
        "",
        "## 2. 总结",
        "",
        f"- `max_p`: `{result['max_p']}`",
        f"- `last_failure`: `{result['last_failure']}`",
        f"- `stable_tail_from_in_scan`: `{result['stable_tail_from_in_scan']}`",
        f"- `failure_count`: `{result['failure_count']}`",
        f"- `split_denominator`: `{result['split_denominator']}`",
        f"- `split_failure_count`: `{result['split_failure_count']}`",
        f"- `split_tail_failure_count(P>=107)`: `{result['split_tail_failure_count']}`",
        f"- `split_min_margin`: `{result['split_min_margin']}`",
        f"- `split_tail_min_margin(P>=107)`: `{result['split_tail_min_margin']}`",
        f"- `product_failure_count`: `{result['product_failure_count']}`",
        f"- `last_product_failure`: `{result['last_product_failure']}`",
        f"- `product_stable_from_in_scan`: `{result['product_stable_from_in_scan']}`",
        f"- `product_tail_min_margin(P>=233)`: `{result['product_tail_min_margin']}`",
        "",
        "## 3. 失败窄带",
        "",
        "| P | Hmax | high # | residual | first steps |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["failures"]:
        lines.append(
            f"| {row['p']} | {row['max_holes']} | {row['high_prime_count']} | "
            f"{row['pigeonhole_residual']} | `{row['initial_steps']}` |"
        )
    lines.extend(
        [
            "",
            "## 4. P/5 分割判据",
            "",
            "先用 `ell<=floor(P/5)` 的高素数执行鸽巢递推，得到残量 `V`；",
            "若剩余高素数个数不少于 `V`，则每个剩余高素数至少再删除一个洞，从而闭合。",
            "该判据在 `P>=107` 的尾段扫描中无失败；低素数窄带仍需真实碰撞能量处理。",
            "",
            "| P | Hmax | split bound | split residual | remaining primes | margin |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tail_samples"]:
        lines.append(
            f"| {row['p']} | {row['max_holes']} | {row['split_bound']} | "
            f"{row['split_residual']} | {row['split_remaining_primes']} | "
            f"{row['split_margin']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 有限尾段证书",
            "",
            "`107<=P<=229` 由精确 `P/5` 分割递推闭合；该段不能直接用连续乘积上界替代。",
            "",
            "| P | Hmax | split residual | remaining primes | margin |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["finite_tail_rows"]:
        lines.append(
            f"| {row['p']} | {row['max_holes']} | {row['split_residual']} | "
            f"{row['split_remaining_primes']} | {row['split_margin']} |"
        )
    lines.extend(
        [
            "",
            "## 6. 连续乘积上界",
            "",
            "`Hmax(P) * product_{13<=ell<=P/5}(1-1/ell)` 是分割残量的连续上界。",
            "该上界在低尾段偏保守，最后失败为 `P=229`；从 `P=233` 起扫描无失败。",
            "",
            "| P | Hmax | split bound | product lhs | remaining primes | margin |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["product_failures"][-10:]:
        lines.append(
            f"| {row['p']} | {row['max_holes']} | {row['split_bound']} | "
            f"{row['product_lhs']:.6f} | {row['product_rhs']} | {row['product_margin']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 7. 尾段样本",
            "",
            "| P | Hmax | high # | residual |",
            "| ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tail_samples"]:
        lines.append(
            f"| {row['p']} | {row['max_holes']} | {row['high_prime_count']} | "
            f"{row['pigeonhole_residual']} |"
        )
    lines.extend(
        [
            "",
            "## 8. 审稿结论",
            "",
            "该审计给出两层正式接口：",
            "`107<=P<=229` 可用精确分割递推作为有限尾段证书；",
            "`P>=233` 可尝试用显式素数计数和 Mertens 乘积界证明连续乘积不等式。",
            "更低的 `61<=P<=103` 十个素数进入有限碰撞能量窄带。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument("--split-denominator", type=int, default=5)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-pigeonhole-tail-audit.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "prime-matrix-bpn-lhb-pigeonhole-tail-audit.md",
    )
    args = parser.parse_args()
    result = scan(args.max_p, args.q, args.split_denominator)
    args.json_output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
