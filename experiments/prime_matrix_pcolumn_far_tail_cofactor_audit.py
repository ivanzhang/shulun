#!/usr/bin/env python3
"""审计第 P 列近截止强行中的远尾互补因子反演。

用法示例：
  python3 experiments/prime_matrix_pcolumn_far_tail_cofactor_audit.py \
    --p-list 5003,10007,20011,50021,100003 \
    --alpha 0.43 \
    --y-factor 4 \
    --tail-factor 10 \
    --out-prefix docs/pcolumn_far_tail_cofactor_audit_20260506

目标：
  对近截止区域最强 T/S 行，把 q>tail_factor*P^alpha 的远尾命中
  精确反演为低互补因子 m 上的短素数区间计数。
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
    """计算单行容量并集和 top q。"""
    alive = mark_low_skeleton(p, y, low_primes)
    skeleton = sum(alive)
    anchor = p * y
    total_hits = 0
    covered = bytearray(p)
    top_q = []
    for q in high_primes:
        residue = anchor % q
        start = residue if residue > 0 else q
        hits = 0
        if start < p:
            for d in range(start, p, q):
                if not alive[d]:
                    continue
                hits += 1
                covered[d] = 1
        if hits:
            top_q.append({"q": q, "hit_count": hits})
        total_hits += hits
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
        "top_q": sorted(top_q, key=lambda row: -row["hit_count"])[:8],
    }


def find_best_near_row(
    p: int,
    cutoff: int,
    low_primes: list[int],
    high_primes: list[int],
    y_factor: float,
) -> dict:
    """找近截止区域 T/S 最大行。"""
    y_limit = min(p + 1, max(2, int(math.ceil(y_factor * cutoff))))
    rows = [
        row_capacity(p, y, low_primes, high_primes)
        for y in range(2, y_limit + 1)
    ]
    best = max(rows, key=lambda row: row["hit_ratio"])
    best["y_limit"] = y_limit
    return best


def direct_tail_hits(
    p: int,
    y: int,
    tail_q_min: int,
    low_primes: list[int],
    high_primes: list[int],
) -> int:
    """直接按 q 统计远尾命中，作为反演校验。"""
    alive = mark_low_skeleton(p, y, low_primes)
    anchor = p * y
    total = 0
    for q in high_primes:
        if q < tail_q_min:
            continue
        residue = anchor % q
        start = residue if residue > 0 else q
        if start >= p:
            continue
        for d in range(start, p, q):
            if alive[d]:
                total += 1
    return total


def m_band_key(m: int, y: int) -> str:
    """按 m/y 比例给互补因子分桶。"""
    ratio = m / y
    if ratio <= 2:
        return "(1,2]y"
    if ratio <= 5:
        return "(2,5]y"
    if ratio <= 10:
        return "(5,10]y"
    if ratio <= 25:
        return "(10,25]y"
    if ratio <= 50:
        return "(25,50]y"
    return ">50y"


def audit_tail_cofactors(
    p: int,
    y: int,
    cutoff: int,
    tail_factor: float,
    low_primes: list[int],
    flags: bytearray,
    prefix: list[int],
) -> dict:
    """把 q 远尾命中精确反演到 m 短素数区间。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    total = 0
    rough_m_count = 0
    active_m_count = 0
    min_active_m = None
    max_active_m = None
    top_m = []
    bands: dict[str, dict] = {}

    for m in range(1, m_max + 1):
        if not is_low_rough(m, low_primes):
            continue
        rough_m_count += 1
        q_min = max(tail_q_min, ceil_div(anchor - (p - 1), m))
        q_max = min(p - 1, (anchor - 1) // m)
        if q_min > q_max:
            continue
        count = prefix[q_max] - (prefix[q_min - 1] if q_min > 0 else 0)
        if not count:
            continue
        active_m_count += 1
        total += count
        min_active_m = m if min_active_m is None else min(min_active_m, m)
        max_active_m = m if max_active_m is None else max(max_active_m, m)
        interval_len = q_max - q_min + 1
        key = m_band_key(m, y)
        bucket = bands.setdefault(
            key,
            {
                "m_count": 0,
                "prime_hits": 0,
                "interval_len": 0,
                "min_m": m,
                "max_m": m,
            },
        )
        bucket["m_count"] += 1
        bucket["prime_hits"] += count
        bucket["interval_len"] += interval_len
        bucket["min_m"] = min(bucket["min_m"], m)
        bucket["max_m"] = max(bucket["max_m"], m)
        top_m.append(
            {
                "m": m,
                "prime_hits": count,
                "q_min": q_min,
                "q_max": q_max,
                "interval_len": interval_len,
                "m_over_y": m / y,
                "m_over_p": m / p,
            }
        )

    band_rows = [
        {"band": key, **value}
        for key, value in sorted(
            bands.items(), key=lambda item: -item[1]["prime_hits"]
        )
    ]
    return {
        "tail_factor": tail_factor,
        "tail_q_min": tail_q_min,
        "m_max": m_max,
        "rough_m_count": rough_m_count,
        "active_m_count": active_m_count,
        "tail_hits_by_cofactor": total,
        "min_active_m": min_active_m,
        "max_active_m": max_active_m,
        "top_m": sorted(top_m, key=lambda row: -row["prime_hits"])[:12],
        "m_bands": band_rows,
    }


def audit_p(
    p: int,
    alpha: float,
    y_factor: float,
    tail_factor: float,
    primes: list[int],
    flags: bytearray,
    prefix: list[int],
) -> dict:
    """审计单个 P。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    best = find_best_near_row(p, cutoff, low_primes, high_primes, y_factor)
    cofactor = audit_tail_cofactors(
        p,
        best["y"],
        cutoff,
        tail_factor,
        low_primes,
        flags,
        prefix,
    )
    direct = direct_tail_hits(
        p,
        best["y"],
        cofactor["tail_q_min"],
        low_primes,
        high_primes,
    )
    cofactor["tail_hits_direct"] = direct
    cofactor["identity_delta"] = direct - cofactor["tail_hits_by_cofactor"]
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "y_factor": y_factor,
        "tail_factor": tail_factor,
        "best_near_row": best,
        "cofactor_tail": cofactor,
    }


def audit(
    p_list: list[int],
    alpha: float,
    y_factor: float,
    tail_factor: float,
) -> dict:
    """执行审计。"""
    flags = sieve_bool(max(p_list))
    prefix = prime_prefix(flags)
    primes = primes_from_flags(flags)
    return {
        "parameters": {
            "p_list": p_list,
            "alpha": alpha,
            "y_factor": y_factor,
            "tail_factor": tail_factor,
        },
        "records": [
            audit_p(p, alpha, y_factor, tail_factor, primes, flags, prefix)
            for p in p_list
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 第P列远尾互补因子反演审计",
        "",
        "**状态：** `far_tail_cofactor_identity_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `p_list`: `{params['p_list']}`",
        f"- `alpha`: `{params['alpha']}`",
        f"- `y_factor`: `{params['y_factor']}`",
        f"- `tail_factor`: `{params['tail_factor']}`",
        "",
        "## 总表",
        "",
        "| P | cutoff | y | T/S | tail q min | tail hits | direct | delta | active m | m range | top m |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for record in result["records"]:
        row = record["best_near_row"]
        tail = record["cofactor_tail"]
        top_m = ",".join(str(item["m"]) for item in tail["top_m"][:4])
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {row['y']} | "
            f"{row['hit_ratio']:.6f} | {tail['tail_q_min']} | "
            f"{tail['tail_hits_by_cofactor']} | {tail['tail_hits_direct']} | "
            f"{tail['identity_delta']} | {tail['active_m_count']} | "
            f"`{tail['min_active_m']}..{tail['max_active_m']}` | `{top_m}` |"
        )

    for record in result["records"]:
        row = record["best_near_row"]
        tail = record["cofactor_tail"]
        lines.extend(
            [
                "",
                f"## P={record['p']}",
                "",
                f"- `cutoff`: `{record['cutoff']}`",
                f"- `best y`: `{row['y']}`",
                f"- `S,T,margin,T/S`: `{row['skeleton_count']}, {row['total_high_hits']}, {row['capacity_margin']}, {row['hit_ratio']:.6f}`",
                f"- `tail_q_min`: `{tail['tail_q_min']}`",
                f"- `tail_hits_by_cofactor`: `{tail['tail_hits_by_cofactor']}`",
                f"- `identity_delta`: `{tail['identity_delta']}`",
                "",
                "互补因子分桶：",
                "",
                "| band | m count | prime hits | interval length | m range |",
                "|---|---:|---:|---:|---|",
            ]
        )
        for band in tail["m_bands"]:
            lines.append(
                f"| `{band['band']}` | {band['m_count']} | "
                f"{band['prime_hits']} | {band['interval_len']} | "
                f"`{band['min_m']}..{band['max_m']}` |"
            )
        lines.extend(["", "top m：", ""])
        for item in tail["top_m"]:
            lines.append(
                f"- `m={item['m']}, hits={item['prime_hits']}, "
                f"q=[{item['q_min']},{item['q_max']}], "
                f"len={item['interval_len']}, m/y={item['m_over_y']:.3f}`"
            )

    lines.extend(
        [
            "",
            "## 结构解释",
            "",
            "对远尾 `q>tail_factor*Y`，命中 `Py-d=qm` 且 `1<=d<P` 等价于",
            "",
            "```text",
            "ceil((Py-P+1)/m) <= q <= floor((Py-1)/m),",
            "q prime, q>tail_factor*Y, q<P,",
            "m 避开所有 ell<=Y。",
            "```",
            "",
            "因此远尾正偏差不再是任意高素斜线噪声，而是低互补因子 `m` 上的短素数区间计数问题。`identity_delta=0` 表示按 q 直接计数与按 m 反演计数完全一致。",
            "",
            "下一步若要证明 `PColumn Dynamic Capacity`，可把远尾分支改写成这些 `Y`-rough 互补因子短区间的总上界；若某些 `m` 带长期超额，则它们给出 cofactor-anchor / ColumnCRT / SAE 入口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default="5003,10007,20011,50021,100003")
    parser.add_argument("--alpha", type=float, default=0.43)
    parser.add_argument("--y-factor", type=float, default=4.0)
    parser.add_argument("--tail-factor", type=float, default=10.0)
    parser.add_argument(
        "--out-prefix",
        default="docs/pcolumn_far_tail_cofactor_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(
        parse_ints(args.p_list),
        args.alpha,
        args.y_factor,
        args.tail_factor,
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
