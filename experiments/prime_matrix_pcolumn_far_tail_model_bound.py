#!/usr/bin/env python3
"""审计第 P 列远尾互补因子的模型付款常数。

用法示例：
  python3 experiments/prime_matrix_pcolumn_far_tail_model_bound.py \
    --p-list 5003,10007,20011,50021,100003,200003 \
    --alpha 0.43 \
    --y-factor 4 \
    --tail-factor 10 \
    --out-prefix docs/pcolumn_far_tail_model_bound_20260506

目标：
  在远尾反演
    Py-d=qm, q>tail_factor*Y
  后，对每个 Y-rough 互补因子 m 的短素数区间 I_m 计算
    model_m = |I_m|/log(q_min)
  并统计实际命中 / 模型量，以及闭合 T<S 所允许的常数。
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
    """计算单行容量。"""
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
        "skeleton_count": skeleton,
        "total_high_hits": total_hits,
        "capacity_margin": skeleton - total_hits,
        "hit_ratio": total_hits / skeleton if skeleton else 0.0,
        "covered_count": covered_count,
        "prime_holes": skeleton - covered_count,
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


def m_band_key(m: int, y: int) -> str:
    """按 m/y 比例分桶。"""
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


def empty_bucket() -> dict:
    """创建分桶累计对象。"""
    return {
        "m_count": 0,
        "actual_hits": 0,
        "interval_len": 0,
        "model_len_log": 0.0,
        "model_li_local": 0.0,
        "min_m": None,
        "max_m": None,
    }


def local_li_model(q_min: int, q_max: int) -> float:
    """用端点对数平均给短区间素数模型量。"""
    if q_min > q_max:
        return 0.0
    left = max(q_min, 3)
    right = max(q_max, left)
    # 只作为审计模型，不作为严格数值积分。
    return (right - left + 1) / ((math.log(left) + math.log(right)) / 2.0)


def tail_model(
    p: int,
    y: int,
    cutoff: int,
    tail_factor: float,
    low_primes: list[int],
    prefix: list[int],
) -> dict:
    """计算远尾互补因子模型付款账本。"""
    anchor = p * y
    tail_q_min = max(cutoff + 1, int(math.floor(tail_factor * cutoff)) + 1)
    m_max = (anchor - 1) // tail_q_min
    actual = 0
    model_len_log = 0.0
    model_li_local = 0.0
    interval_len_total = 0
    rough_m_count = 0
    active_m_count = 0
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
        interval_len = q_max - q_min + 1
        count = prefix[q_max] - (prefix[q_min - 1] if q_min > 0 else 0)
        if interval_len <= 0:
            continue
        len_log = interval_len / math.log(max(q_min, 3))
        li_local = local_li_model(q_min, q_max)
        interval_len_total += interval_len
        model_len_log += len_log
        model_li_local += li_local
        if count:
            active_m_count += 1
        actual += count
        key = m_band_key(m, y)
        bucket = bands.setdefault(key, empty_bucket())
        bucket["m_count"] += 1
        bucket["actual_hits"] += count
        bucket["interval_len"] += interval_len
        bucket["model_len_log"] += len_log
        bucket["model_li_local"] += li_local
        bucket["min_m"] = m if bucket["min_m"] is None else min(bucket["min_m"], m)
        bucket["max_m"] = m if bucket["max_m"] is None else max(bucket["max_m"], m)
        if count:
            top_m.append(
                {
                    "m": m,
                    "actual_hits": count,
                    "interval_len": interval_len,
                    "model_len_log": len_log,
                    "actual_over_model": count / len_log if len_log else 0.0,
                    "q_min": q_min,
                    "q_max": q_max,
                    "m_over_y": m / y,
                }
            )

    band_rows = []
    for key, bucket in bands.items():
        band_rows.append(
            {
                "band": key,
                **bucket,
                "actual_over_len_log": (
                    bucket["actual_hits"] / bucket["model_len_log"]
                    if bucket["model_len_log"]
                    else 0.0
                ),
                "actual_over_li_local": (
                    bucket["actual_hits"] / bucket["model_li_local"]
                    if bucket["model_li_local"]
                    else 0.0
                ),
            }
        )
    band_rows.sort(key=lambda row: -row["actual_hits"])
    return {
        "tail_q_min": tail_q_min,
        "m_max": m_max,
        "rough_m_count": rough_m_count,
        "active_m_count": active_m_count,
        "interval_len_total": interval_len_total,
        "actual_tail_hits": actual,
        "model_len_log": model_len_log,
        "model_li_local": model_li_local,
        "actual_over_len_log": actual / model_len_log if model_len_log else 0.0,
        "actual_over_li_local": actual / model_li_local if model_li_local else 0.0,
        "bands": band_rows,
        "top_m": sorted(top_m, key=lambda row: -row["actual_hits"])[:12],
    }


def audit_p(
    p: int,
    alpha: float,
    y_factor: float,
    tail_factor: float,
    primes: list[int],
    prefix: list[int],
) -> dict:
    """审计单个 P。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in primes if q <= cutoff]
    high_primes = [q for q in primes if cutoff < q < p]
    best = find_best_near_row(p, cutoff, low_primes, high_primes, y_factor)
    tail = tail_model(p, best["y"], cutoff, tail_factor, low_primes, prefix)
    non_tail_hits = best["total_high_hits"] - tail["actual_tail_hits"]
    allowable_tail_hits = best["skeleton_count"] - non_tail_hits
    tail["non_tail_hits"] = non_tail_hits
    tail["allowable_tail_hits"] = allowable_tail_hits
    tail["allowable_over_len_log"] = (
        allowable_tail_hits / tail["model_len_log"]
        if tail["model_len_log"]
        else 0.0
    )
    tail["allowable_over_li_local"] = (
        allowable_tail_hits / tail["model_li_local"]
        if tail["model_li_local"]
        else 0.0
    )
    tail["constant_slack_len_log"] = (
        tail["allowable_over_len_log"] - tail["actual_over_len_log"]
    )
    tail["constant_slack_li_local"] = (
        tail["allowable_over_li_local"] - tail["actual_over_li_local"]
    )
    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "best_near_row": best,
        "tail_model": tail,
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
            audit_p(p, alpha, y_factor, tail_factor, primes, prefix)
            for p in p_list
        ],
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 第P列远尾模型付款审计",
        "",
        "**状态：** `far_tail_model_payment_audit_not_a_proof`",
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
        "| P | cutoff | y | S | T | tail | non-tail | margin | model | actual/model | allow/model | C slack |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in result["records"]:
        row = record["best_near_row"]
        tail = record["tail_model"]
        lines.append(
            f"| {record['p']} | {record['cutoff']} | {row['y']} | "
            f"{row['skeleton_count']} | {row['total_high_hits']} | "
            f"{tail['actual_tail_hits']} | {tail['non_tail_hits']} | "
            f"{row['capacity_margin']} | {tail['model_len_log']:.3f} | "
            f"{tail['actual_over_len_log']:.6f} | "
            f"{tail['allowable_over_len_log']:.6f} | "
            f"{tail['constant_slack_len_log']:.6f} |"
        )

    for record in result["records"]:
        row = record["best_near_row"]
        tail = record["tail_model"]
        lines.extend(
            [
                "",
                f"## P={record['p']}",
                "",
                f"- `best y`: `{row['y']}`",
                f"- `S,T,margin`: `{row['skeleton_count']}, {row['total_high_hits']}, {row['capacity_margin']}`",
                f"- `tail actual/model`: `{tail['actual_tail_hits']} / {tail['model_len_log']:.3f}`",
                f"- `actual_over_model`: `{tail['actual_over_len_log']:.6f}`",
                f"- `allowable_over_model`: `{tail['allowable_over_len_log']:.6f}`",
                f"- `constant_slack`: `{tail['constant_slack_len_log']:.6f}`",
                "",
                "m/y 分桶：",
                "",
                "| band | m count | actual | model | actual/model | interval len | m range |",
                "|---|---:|---:|---:|---:|---:|---|",
            ]
        )
        for band in tail["bands"]:
            lines.append(
                f"| `{band['band']}` | {band['m_count']} | "
                f"{band['actual_hits']} | {band['model_len_log']:.3f} | "
                f"{band['actual_over_len_log']:.6f} | "
                f"{band['interval_len']} | "
                f"`{band['min_m']}..{band['max_m']}` |"
            )
        lines.extend(["", "top m：", ""])
        for item in tail["top_m"]:
            lines.append(
                f"- `m={item['m']}, actual={item['actual_hits']}, "
                f"model={item['model_len_log']:.3f}, "
                f"ratio={item['actual_over_model']:.6f}, "
                f"q=[{item['q_min']},{item['q_max']}], "
                f"m/y={item['m_over_y']:.3f}`"
            )

    lines.extend(
        [
            "",
            "## 结构解释",
            "",
            "`model=sum |I_m|/log(q_min)` 是远尾互补因子短素数区间的基础模型量。`allow/model=(S-non_tail)/model` 表示若远尾有统一上界 `tail<=C*model`，闭合 `T<S` 所允许的最大常数。",
            "",
            "若存在全局常数 `C` 满足 `actual/model <= C < allow/model`，则远尾分支可付款。若某个层的 `actual/model` 长期超过可付款常数，则它不是随机波动，应进入 `cofactor-anchor / SAE / PDEC / ColumnCRT`。",
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
        default="docs/pcolumn_far_tail_model_bound_20260506",
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
