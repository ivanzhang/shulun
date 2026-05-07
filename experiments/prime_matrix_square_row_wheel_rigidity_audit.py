#!/usr/bin/env python3
"""审计 P^2 前后两行的轮筛刚性。

用法示例：
  python3 experiments/prime_matrix_square_row_wheel_rigidity_audit.py \
    --max-p 100000 --wheels 6,30,210,2310 \
    --out-prefix docs/square_row_wheel_rigidity_audit_p100000_20260506

该脚本只研究结构性低模轮骨架，不把实验当作证明。
核心恒等式：
  P^2+k 避开 W 的素因子 <=> k mod W in U_W - P^2
  P^2-k 避开 W 的素因子 <=> k mod W in P^2 - U_W
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return flags


def primes_from_table(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def factor_distinct(value: int) -> list[int]:
    """返回 value 的不同素因子。"""
    factors = []
    n = value
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            factors.append(factor)
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def units(modulus: int) -> list[int]:
    """返回模 modulus 的单位剩余类。"""
    return [residue for residue in range(modulus) if math.gcd(residue, modulus) == 1]


def count_residues_in_range(residues: set[int], modulus: int, length: int) -> int:
    """计数 1<=k<=length 中 k mod modulus 属于 residues 的个数。"""
    full, rem = divmod(length, modulus)
    total = full * len(residues)
    total += sum(1 for k in range(1, rem + 1) if k % modulus in residues)
    return total


def residue_table_for_square(modulus: int, p2: int) -> dict:
    """生成给定 P^2 residue 的前后行轮骨架。"""
    unit_set = set(units(modulus))
    plus = {(u - p2) % modulus for u in unit_set}
    minus = {(p2 - u) % modulus for u in unit_set}
    both = plus & minus
    return {
        "p2": p2,
        "plus_allowed": sorted(plus),
        "minus_allowed": sorted(minus),
        "both_allowed": sorted(both),
        "plus_count_mod_w": len(plus),
        "minus_count_mod_w": len(minus),
        "both_count_mod_w": len(both),
        "mirror_ok": sorted((-r) % modulus for r in plus) == sorted(minus),
    }


def audit_wheel(max_p: int, modulus: int, tail_min_p: int) -> dict:
    """审计单个轮模数。"""
    factors = factor_distinct(modulus)
    flags = sieve_bool(max_p)
    primes = [p for p in primes_from_table(flags) if p > max(factors)]
    unit_set = set(units(modulus))
    square_residues = sorted({(u * u) % modulus for u in unit_set})
    residue_tables = {
        str(p2): residue_table_for_square(modulus, p2) for p2 in square_residues
    }

    records = []
    for p in primes:
        p2 = (p * p) % modulus
        table = residue_tables[str(p2)]
        length = p - 1
        plus_count = count_residues_in_range(
            set(table["plus_allowed"]), modulus, length
        )
        minus_count = count_residues_in_range(
            set(table["minus_allowed"]), modulus, length
        )
        both_count = count_residues_in_range(
            set(table["both_allowed"]), modulus, length
        )
        expected_full_density = length * len(unit_set) / modulus
        records.append(
            {
                "p": p,
                "p_mod_w": p % modulus,
                "p2_mod_w": p2,
                "length": length,
                "plus_count": plus_count,
                "minus_count": minus_count,
                "both_count": both_count,
                "plus_error_from_density": plus_count - expected_full_density,
                "minus_error_from_density": minus_count - expected_full_density,
            }
        )

    min_plus = min(records, key=lambda item: item["plus_count"], default=None)
    min_minus = min(records, key=lambda item: item["minus_count"], default=None)
    min_both = min(records, key=lambda item: item["both_count"], default=None)
    tail_records = [record for record in records if record["p"] >= tail_min_p]
    tail_min_plus = min(
        tail_records, key=lambda item: item["plus_count"], default=None
    )
    tail_min_minus = min(
        tail_records, key=lambda item: item["minus_count"], default=None
    )
    tail_min_both = min(
        tail_records, key=lambda item: item["both_count"], default=None
    )
    max_plus_error = max(
        records, key=lambda item: abs(item["plus_error_from_density"]), default=None
    )
    max_minus_error = max(
        records, key=lambda item: abs(item["minus_error_from_density"]), default=None
    )
    p2_classes_seen = sorted({record["p2_mod_w"] for record in records})
    return {
        "modulus": modulus,
        "factors": factors,
        "phi": len(unit_set),
        "unit_density": len(unit_set) / modulus,
        "square_residues": square_residues,
        "square_residue_count": len(square_residues),
        "p2_classes_seen": p2_classes_seen,
        "residue_tables": residue_tables,
        "summary": {
            "prime_count": len(records),
            "min_plus_record": min_plus,
            "min_minus_record": min_minus,
            "min_both_record": min_both,
            "tail_min_p": tail_min_p,
            "tail_prime_count": len(tail_records),
            "tail_min_plus_record": tail_min_plus,
            "tail_min_minus_record": tail_min_minus,
            "tail_min_both_record": tail_min_both,
            "max_plus_error_record": max_plus_error,
            "max_minus_error_record": max_minus_error,
            "both_count_mod_w_by_p2": {
                p2: residue_tables[str(p2)]["both_count_mod_w"]
                for p2 in map(str, square_residues)
            },
            "all_mirror_ok": all(
                table["mirror_ok"] for table in residue_tables.values()
            ),
        },
    }


def audit(max_p: int, wheels: list[int], tail_min_p: int) -> dict:
    """审计多个轮模数。"""
    return {
        "parameters": {"max_p": max_p, "wheels": wheels, "tail_min_p": tail_min_p},
        "wheels": {
            str(wheel): audit_wheel(max_p, wheel, tail_min_p) for wheel in wheels
        },
    }


def compact_residue_list(values: list[int], limit: int = 24) -> str:
    """压缩长剩余类列表。"""
    if len(values) <= limit:
        return ", ".join(str(value) for value in values)
    head = ", ".join(str(value) for value in values[: limit // 2])
    tail = ", ".join(str(value) for value in values[-limit // 2 :])
    return f"{head}, ..., {tail}"


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# P^2 前后两行的轮筛刚性审计",
        "",
        "**状态：** `wheel_rigidity_structural_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `tail_min_p`: `{params['tail_min_p']}`",
        f"- `wheels`: `{params['wheels']}`",
        "",
        "## 核心恒等式",
        "",
        "对 `W` 的单位剩余类集合 `U_W`，若 `gcd(P,W)=1`，则",
        "",
        "```text",
        "P^2+k 避开 W 的素因子 <=> k mod W in U_W - P^2",
        "P^2-k 避开 W 的素因子 <=> k mod W in P^2 - U_W",
        "```",
        "",
        "因此平方前后两行的低模骨架不是随机对象，而是同一个轮单位集合的平移与镜像。",
        "",
        "## 汇总",
        "",
        "| W | factors | phi(W) | square residues | both residues/W | mirror | primes | min plus | min minus | min both |",
        "|---:|---|---:|---:|---:|---|---:|---:|---:|---:|",
    ]
    for wheel_key, wheel in result["wheels"].items():
        summary = wheel["summary"]
        both_counts = sorted(set(summary["both_count_mod_w_by_p2"].values()))
        lines.append(
            f"| {wheel_key} | {wheel['factors']} | {wheel['phi']} | "
            f"{wheel['square_residue_count']} | {both_counts} | "
            f"{summary['all_mirror_ok']} | {summary['prime_count']} | "
            f"{summary['min_plus_record']['plus_count']} | "
            f"{summary['min_minus_record']['minus_count']} | "
            f"{summary['min_both_record']['both_count']} |"
        )

    lines.extend(
        [
            "## 尾段窗口计数",
            "",
            "| W | tail primes | min plus | min minus | min both | min plus/P | min minus/P | min both/P |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for wheel_key, wheel in result["wheels"].items():
        summary = wheel["summary"]
        tail_plus = summary["tail_min_plus_record"]
        tail_minus = summary["tail_min_minus_record"]
        tail_both = summary["tail_min_both_record"]
        lines.append(
            f"| {wheel_key} | {summary['tail_prime_count']} | "
            f"{tail_plus['plus_count']} | {tail_minus['minus_count']} | {tail_both['both_count']} | "
            f"{tail_plus['plus_count'] / tail_plus['p']:.6f} | "
            f"{tail_minus['minus_count'] / tail_minus['p']:.6f} | "
            f"{tail_both['both_count'] / tail_both['p']:.6f} |"
        )
    lines.append("")

    lines.extend(["", "## 平方残基与允许偏移", ""])
    for wheel_key, wheel in result["wheels"].items():
        lines.extend(
            [
                f"### W={wheel_key}",
                "",
                f"- `factors`: `{wheel['factors']}`",
                f"- `phi(W)`: `{wheel['phi']}`",
                f"- `square_residues`: `{compact_residue_list(wheel['square_residues'])}`",
                "",
                "| P^2 mod W | plus allowed count | minus allowed count | both count | plus allowed residues |",
                "|---:|---:|---:|---:|---|",
            ]
        )
        for p2 in wheel["square_residues"]:
            table = wheel["residue_tables"][str(p2)]
            lines.append(
                f"| {p2} | {table['plus_count_mod_w']} | "
                f"{table['minus_count_mod_w']} | {table['both_count_mod_w']} | "
                f"{compact_residue_list(table['plus_allowed'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 审稿解释",
            "",
            "该审计只固定低模轮骨架。它不能证明平方前后窗口中必有素数；真正需要证明的是：在这个确定性轮骨架上，所有 `W` 以上的已激活斜线不能完成全覆盖。好处是后续高素补洞不再面对原始列集合，而是面对 `U_W ± P^2` 的刚性平移骨架。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_wheels(raw: str) -> list[int]:
    """解析轮模数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=100000)
    parser.add_argument("--tail-min-p", type=int, default=10007)
    parser.add_argument("--wheels", default="6,30,210,2310")
    parser.add_argument(
        "--out-prefix",
        default="docs/square_row_wheel_rigidity_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(args.max_p, parse_wheels(args.wheels), args.tail_min_p)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
