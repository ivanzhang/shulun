#!/usr/bin/env python3
"""边界相位非覆盖引理审计。

用法示例：
  python3 experiments/prime_matrix_boundary_phase_noncoverage_audit.py

目标：审计前 P 行，即 x=1,...,P-1 中是否存在完整覆盖相位。
若 x<P 且 xP+c 避开所有小于 P 的素数，则 xP+c<P^2 自动为素数。
因此边界相位非覆盖等价于每个边界行至少有一个真实素数幸存者。
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, ok in enumerate(sieve) if ok]


def is_prime(value: int) -> bool:
    """朴素素性测试；本审计只处理小样本。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def uncovered_columns(p: int, base_primes: list[int], x: int) -> list[dict]:
    """列出边界相位 x 的未覆盖列。"""
    holes = []
    for col in range(1, p):
        value = x * p + col
        if any(value % prime == 0 for prime in base_primes):
            continue
        holes.append({"col": col, "value": value, "is_prime": is_prime(value)})
    return holes


def prefix_holes(p: int, prefix_primes: list[int], x: int) -> list[int]:
    """列出只用低素数前缀筛后仍未覆盖的列。"""
    holes = []
    for col in range(1, p):
        value = x * p + col
        if not any(value % prime == 0 for prime in prefix_primes):
            holes.append(col)
    return holes


def audit_prime(p: int) -> dict:
    """审计单个 P 的前窗口。"""
    base_primes = primes_upto(p - 1)
    best_rows: list[dict] = []
    min_holes = p
    zero_rows = []
    low_prefix = [prime for prime in (2, 3, 5, 7) if prime < p]
    for x in range(1, p):
        holes = uncovered_columns(p, base_primes, x)
        if not holes:
            zero_rows.append(x + 1)
        if len(holes) < min_holes:
            min_holes = len(holes)
            best_rows = [
                {
                    "x": x,
                    "row": x + 1,
                    "holes": holes,
                    "prefix_holes_2_3_5_7": prefix_holes(p, low_prefix, x),
                }
            ]
        elif len(holes) == min_holes and len(best_rows) < 8:
            best_rows.append(
                {
                    "x": x,
                    "row": x + 1,
                    "holes": holes,
                    "prefix_holes_2_3_5_7": prefix_holes(p, low_prefix, x),
                }
            )
    return {
        "p": p,
        "base_prime_count": len(base_primes),
        "min_boundary_survivors": min_holes,
        "boundary_zero_rows": zero_rows,
        "bpn_holds_in_scan": not zero_rows and min_holes > 0,
        "best_rows": best_rows,
    }


def run_audit(max_p: int = 199) -> dict:
    """运行边界相位审计。"""
    p_values = [prime for prime in primes_upto(max_p) if prime >= 5]
    results = [audit_prime(p) for p in p_values]
    return {
        "certificate_type": "prime_matrix_boundary_phase_noncoverage_audit",
        "status": "boundary_window_verified_in_scan_but_theorem_reduces_to_short_prime_gap_grid",
        "max_p": max_p,
        "results": results,
        "summary": {
            "checked_prime_count": len(results),
            "failures": [item for item in results if not item["bpn_holds_in_scan"]],
            "minimum_survivor_count_seen": min(
                item["min_boundary_survivors"] for item in results
            ),
        },
        "structural_conclusion": (
            "扫描内所有前 P 行均有旧筛幸存者；由于 x<P 时幸存者自动为素数，"
            "这正是边界相位非覆盖。最薄边界行通常只有少数素数幸存者，"
            "说明证明必须处理最后残洞核与高素数补洞标签的 CRT 最小代表。"
        ),
        "proof_boundary": (
            "该实验不能替代证明。一般 BPN 等价于在每个网格区间 "
            "[xP+1,xP+P-1], 1<=x<P, 存在素数；这是强短素数间隔型输入。"
        ),
        "next_obligations": [
            "把 BPN 写成完整覆盖方案最小 CRT 代表 x_S>=P 的定理。",
            "证明前窗口最后残洞核不能由高素数标签在 x<P 内同时补齐且保持旧覆盖不释放。",
            "若无法自足闭合，应明确标注需要一个网格短素数间隔输入，而不能宣称无条件完成。",
        ],
    }


def write_markdown(audit: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# 边界相位非覆盖审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        audit["structural_conclusion"],
        "",
        audit["proof_boundary"],
        "",
        "## 总表",
        "",
        "| P | base primes | min survivors | BPN holds? | best rows |",
        "| ---: | ---: | ---: | --- | --- |",
    ]
    for item in audit["results"]:
        best = [
            {
                "x": row["x"],
                "row": row["row"],
                "holes": [
                    (hole["col"], hole["value"]) for hole in row["holes"]
                ],
                "prefix_holes_2_3_5_7": row["prefix_holes_2_3_5_7"],
            }
            for row in item["best_rows"][:3]
        ]
        lines.append(
            "| {p} | {base_count} | {min_holes} | {holds} | `{best}` |".format(
                p=item["p"],
                base_count=item["base_prime_count"],
                min_holes=item["min_boundary_survivors"],
                holds=item["bpn_holds_in_scan"],
                best=best,
            )
        )
    lines.extend(
        [
            "",
            "## 形式化压缩",
            "",
            "令 `x=r-1`。边界相位非覆盖引理可写为：对每个奇素数 `P` 与每个 `1<=x<P`，存在 `1<=c<P` 使",
            "",
            "\\[",
            "\\gcd(xP+c,\\prod_{\\ell<P}\\ell)=1.",
            "\\]",
            "",
            "由于 `xP+c<P^2`，该幸存者自动是素数。因此 BPN 等价于每个网格区间 `[xP+1,xP+P-1]` 中有素数。",
            "",
            "换成相位覆盖语言：不存在 `x<P` 使列集 `1,...,P-1` 被禁类族",
            "",
            "\\[",
            "c\\equiv -xP\\pmod \\ell,\\qquad \\ell<P",
            "\\]",
            "",
            "完全覆盖。若把一个完整覆盖证书记为 `S`，其 CRT 最小代表为 `x_S`，则目标等价于",
            "",
            "\\[",
            "x_S\\ge P\\quad\\text{for every complete cover certificate }S.",
            "\\]",
            "",
            "## 当前硬点",
            "",
            "已有实验显示低素数骨架在前窗口总留洞；局部补洞约束可有小 CRT 代表，但一旦要求保持全部列覆盖，首个完整代表回到 `x>=P`。缺口是把这种“残洞迁移守恒”从实验现象提升为定理。",
            "",
            "## 下一证明义务",
            "",
        ]
    )
    for item in audit["next_obligations"]:
        lines.append(f"- {item}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    audit = run_audit()
    prefix = DOCS / "prime-matrix-boundary-phase-noncoverage-audit"
    prefix.with_suffix(".json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(audit, prefix.with_suffix(".md"))
    print(json.dumps(audit["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
