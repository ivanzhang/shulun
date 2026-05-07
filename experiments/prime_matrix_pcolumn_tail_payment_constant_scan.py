#!/usr/bin/env python3
"""扫描第 P 列近截止风险行的远尾付款常数。

用法示例：
  python3 experiments/prime_matrix_pcolumn_tail_payment_constant_scan.py \
    --p-list 5003,10007,20011,50021,100003,200003 \
    --alpha 0.43 \
    --y-factor 4 \
    --tail-factor 10 \
    --top-n 16 \
    --c-tail 1.05 \
    --out-prefix docs/pcolumn_tail_payment_constant_scan_20260506

目标：
  对 y<=4Y 的近截止风险行，先找 T/S 最高的 top-n 行，再把
  T = non_tail + tail 分解，检查
    non_tail + C_tail * model_tail < S
  是否仍有正余量。
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


def prime_prefix(flags: bytearray) -> list[int]:
    """返回 pi(n) 前缀表。"""
    prefix = [0] * len(flags)
    total = 0
    for idx, flag in enumerate(flags):
        if flag:
            total += 1
        prefix[idx] = total
    return prefix


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def ceil_div(a: int, b: int) -> int:
    """整数上取整。"""
    return -(-a // b)


def is_low_rough(value: int, low_primes: list[int]) -> bool:
    """判断 value 是否避开所有低素。"""
    for q in low_primes:
        if value % q == 0:
            return False
    return True


def mark_low_skeleton(p: int, y: int, low_primes: list[int]) -> bytearray:
    """标记 Py-d 避开低素的动态骨架，索引 d。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    anchor = p * y
    for q in low_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def row_capacity(
    p: int,
    y: int,
    low_primes: list[int],
    high_primes: list[int],
) -> dict:
    """计算单行一阶容量。"""
    alive = mark_low_skeleton(p, y, low_primes)
    skeleton = sum(alive)
    anchor = p * y
    total_hits = 0
    covered = bytearray(p)
    for q in high_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        for d in range(start, p, q):
            if not alive[d]:
                continue
            total_hits += 1
            covered[d] = 1
    covered_count = sum(1 for d in range(1, p) if covered[d])
    return {
        "y": y,
        "x": y - 1,
        "skeleton_count": skeleton,
        "total_high_hits": total_hits,
        "capacity_margin": skeleton - total_hits,
        "hit_ratio": total_hits / skeleton if skeleton else 0.0,
        "covered_count": covered_count,
        "prime_holes": skeleton - covered_count,
    }


def tail_model(
    p: int,
    y: int,
    cutoff: int,
    tail_factor: float,
    low_primes: list[int],
    prefix: list[int],
) -> dict:
    """计算远尾实际命中和模型量。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    actual = 0
    model = 0.0
    interval_len_total = 0
    active_m_count = 0
    for m in range(1, m_max + 1):
        if not is_low_rough(m, low_primes):
            continue
        q_min = max(tail_q_min, ceil_div(anchor - (p - 1), m))
        q_max = min(p - 1, (anchor - 1) // m)
        if q_min > q_max:
            continue
        interval_len = q_max - q_min + 1
        count = prefix[q_max] - (prefix[q_min - 1] if q_min > 0 else 0)
        if count:
            active_m_count += 1
        actual += count
        interval_len_total += interval_len
        model += interval_len / math.log(max(q_min, 3))
    return {
        "tail_q_min": tail_q_min,
        "m_max": m_max,
        "active_m_count": active_m_count,
        "interval_len_total": interval_len_total,
        "actual_tail_hits": actual,
        "model_tail": model,
        "actual_over_model": actual / model if model else 0.0,
    }


def audit_p(
    p: int,
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    c_tail: float,
    primes: list[int],
    prefix: list[int],
) -> dict:
    """审计单个 P 的 top 风险行。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    y_limit = min(p + 1, max(2, int(math.ceil(y_factor * cutoff))))
    all_rows = [
        row_capacity(p, y, low_primes, high_primes)
        for y in range(2, y_limit + 1)
    ]
    top_rows = sorted(all_rows, key=lambda row: -row["hit_ratio"])[:top_n]
    enriched = []
    for row in top_rows:
        tail = tail_model(p, row["y"], cutoff, tail_factor, low_primes, prefix)
        non_tail = row["total_high_hits"] - tail["actual_tail_hits"]
        allowable = row["skeleton_count"] - non_tail
        c_allow = allowable / tail["model_tail"] if tail["model_tail"] else 0.0
        c_margin = c_allow - c_tail
        payment_margin = row["skeleton_count"] - non_tail - c_tail * tail["model_tail"]
        enriched.append(
            {
                **row,
                "tail": tail,
                "non_tail_hits": non_tail,
                "allowable_tail_hits": allowable,
                "c_allow": c_allow,
                "c_margin": c_margin,
                "payment_margin": payment_margin,
                "payment_pass": payment_margin > 0,
            }
        )
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "y_limit": y_limit,
        "top_n": top_n,
        "c_tail": c_tail,
        "min_payment_margin": min(row["payment_margin"] for row in enriched),
        "min_c_allow": min(row["c_allow"] for row in enriched),
        "max_actual_over_model": max(
            row["tail"]["actual_over_model"] for row in enriched
        ),
        "payment_fail_count": sum(1 for row in enriched if not row["payment_pass"]),
        "worst_payment_rows": sorted(enriched, key=lambda row: row["payment_margin"])[:8],
        "top_ratio_rows": enriched,
    }


def audit(
    p_list: list[int],
    alpha: float,
    y_factor: float,
    tail_factor: float,
    top_n: int,
    c_tail: float,
) -> dict:
    """执行扫描。"""
    flags = sieve_bool(max(p_list))
    prefix = prime_prefix(flags)
    primes = primes_from_flags(flags)
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "y_factor": y_factor,
            "tail_factor": tail_factor,
            "top_n": top_n,
            "c_tail": c_tail,
        },
        "records": [
            audit_p(
                p,
                alpha,
                y_factor,
                tail_factor,
                top_n,
                c_tail,
                primes,
                prefix,
            )
            for p in p_list
        ],
    }


def row_text(row: dict) -> str:
    """压缩展示风险行。"""
    return (
        f"y={row['y']}, S={row['skeleton_count']}, T={row['total_high_hits']}, "
        f"tail={row['tail']['actual_tail_hits']}, non_tail={row['non_tail_hits']}, "
        f"T/S={row['hit_ratio']:.6f}, c_allow={row['c_allow']:.6f}, "
        f"actual/model={row['tail']['actual_over_model']:.6f}, "
        f"pay_margin={row['payment_margin']:.3f}"
    )


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 第P列远尾付款常数扫描",
        "",
        "**状态：** `tail_payment_constant_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `y_factor`: `{params['y_factor']}`",
        f"- `tail_factor`: `{params['tail_factor']}`",
        f"- `top_n`: `{params['top_n']}`",
        f"- `c_tail`: `{params['c_tail']}`",
        "",
        "## 总表",
        "",
        "| P | cutoff | y_limit | min pay margin | min C allow | max actual/model | fails |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {record['y_limit']} | "
            f"{record['min_payment_margin']:.3f} | "
            f"{record['min_c_allow']:.6f} | "
            f"{record['max_actual_over_model']:.6f} | "
            f"{record['payment_fail_count']} |"
        )

    for record in result["records"]:
        lines.extend(
            [
                "",
                f"## P={record['p']}",
                "",
                "付款余量最紧行：",
                "",
            ]
        )
        for row in record["worst_payment_rows"]:
            lines.append(f"- `{row_text(row)}`")

    lines.extend(
        [
            "",
            "## 结构解释",
            "",
            "该扫描检验一个条件付款命题：若远尾满足 `tail<=C_tail*model_tail`，则 top 风险行是否已推出 `T<S`。这里 `model_tail=sum |I_m|/log(q_min)`，`C_allow=(S-non_tail)/model_tail` 是该行允许的最大远尾常数。",
            "",
            "若 `C_tail < min C_allow` 且实际 `actual/model_tail` 也明显低于 `C_tail`，则远尾分支可被压成证明统一短素数区间上界。若某行 `C_allow` 接近实际比例，则进入 `cofactor-anchor / SAE / PDEC / ColumnCRT`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="5003,10007,20011,50021,100003,200003")
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--y-factor", type=float, default=4.0)
    parser.add_argument("--tail-factor", type=float, default=10.0)
    parser.add_argument("--top-n", type=int, default=16)
    parser.add_argument("--c-tail", type=float, default=1.05)
    parser.add_argument(
        "--out-prefix",
        default="docs/pcolumn_tail_payment_constant_scan_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_ints(args.p_list),
        args.alpha,
        args.y_factor,
        args.tail_factor,
        args.top_n,
        args.c_tail,
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
