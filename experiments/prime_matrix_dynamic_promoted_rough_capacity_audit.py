#!/usr/bin/env python3
"""审计动态提升轮 Y=P^alpha 后的粗骨架容量。

用法示例：
  python3 experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py \
    --primes 10007,36739,99991 --alphas 0.38,0.40,0.43,0.45,0.49 \
    --out-prefix docs/dynamic_promoted_rough_capacity_audit_20260506

数学接口：
  把所有 q<=Y 的素因子斜线提升进轮底座。轮提升不改变最终幸存集合。
  若剩余 q in (Y,P) 在粗骨架 S_Y 上的总命中 T_Y 已小于 |S_Y|，
  则无需二重重叠，单靠容量就能排除全覆盖。
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


def primes_from_flags(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def row_residue(p: int, q: int, side: str) -> int:
    """返回 q 覆盖平方前/后行时的 k 同余类。"""
    p2 = (p * p) % q
    if side == "plus":
        return (-p2) % q
    if side == "minus":
        return p2 % q
    raise ValueError(f"unknown side: {side}")


def mark_low_skeleton(p: int, low_primes: list[int], side: str) -> bytearray:
    """标记 1<=k<P 中避开所有 low_primes 的粗骨架。"""
    alive = bytearray(b"\x01") * p
    alive[0] = 0
    for q in low_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        if start >= p:
            continue
        alive[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
    return alive


def multiplicity_bound(p: int, high_primes: list[int], side: str) -> dict:
    """用最小剩余高素连乘给出单点标签重数上界。"""
    n_max = p * p + p - 1 if side == "plus" else p * p - 1
    product = 1
    used = []
    for q in high_primes:
        if product * q > n_max:
            break
        product *= q
        used.append(q)
    return {
        "m_bound": len(used),
        "basis_primes": used,
        "basis_product": product,
        "n_max": n_max,
    }


def audit_one(p: int, alpha: float, side: str, all_primes: list[int]) -> dict:
    """审计单个 P,alpha,side。"""
    cutoff = int(p**alpha)
    low_primes = [q for q in all_primes if q <= cutoff]
    high_primes = [q for q in all_primes if cutoff < q < p]
    alive = mark_low_skeleton(p, low_primes, side)
    skeleton_count = sum(alive)
    labels = bytearray(p)
    total_hits = 0
    q_records = []

    for q in high_primes:
        residue = row_residue(p, q, side)
        start = residue if residue > 0 else q
        hits = 0
        for k in range(start, p, q):
            if not alive[k]:
                continue
            labels[k] += 1
            hits += 1
        if hits:
            total_hits += hits
            q_records.append({"q": q, "hit_count": hits})

    covered_count = sum(1 for value in labels if value)
    pair_intersections = sum(value * (value - 1) // 2 for value in labels)
    max_mult = max(labels) if labels else 0
    mult_bound = multiplicity_bound(p, high_primes, side)
    m_bound = max(1, mult_bound["m_bound"])
    forced_union_upper = total_hits - math.ceil(2 * pair_intersections / m_bound)
    harmonic_high = sum(1.0 / q for q in high_primes)
    model_constant = math.log(1.0 / alpha)
    uncovered_count = skeleton_count - covered_count
    capacity_margin = skeleton_count - total_hits
    forced_margin = skeleton_count - forced_union_upper

    return {
        "p": p,
        "alpha": alpha,
        "cutoff": cutoff,
        "side": side,
        "low_prime_count": len(low_primes),
        "high_prime_count": len(high_primes),
        "skeleton_count": skeleton_count,
        "total_hits": total_hits,
        "covered_count": covered_count,
        "uncovered_count": uncovered_count,
        "capacity_margin": capacity_margin,
        "capacity_pass": total_hits < skeleton_count,
        "pair_intersections": pair_intersections,
        "multiplicity_bound": mult_bound,
        "exact_max_multiplicity": int(max_mult),
        "forced_union_upper": forced_union_upper,
        "forced_margin": forced_margin,
        "forced_pass": forced_union_upper < skeleton_count,
        "incidence_ratio": None if skeleton_count == 0 else total_hits / skeleton_count,
        "covered_ratio": None if skeleton_count == 0 else covered_count / skeleton_count,
        "harmonic_high": harmonic_high,
        "model_constant_log_1_over_alpha": model_constant,
        "top_q": sorted(q_records, key=lambda row: -row["hit_count"])[:10],
    }


def audit(primes: list[int], alphas: list[float]) -> dict:
    """执行审计。"""
    all_primes = primes_from_flags(sieve_bool(max(primes)))
    records = []
    for p in primes:
        for alpha in alphas:
            for side in ("minus", "plus"):
                records.append(audit_one(p, alpha, side, all_primes))
    return {"parameters": {"primes": primes, "alphas": alphas}, "records": records}


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 动态提升轮粗骨架容量审计",
        "",
        "**状态：** `dynamic_promoted_rough_capacity_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `primes`: `{params['primes']}`",
        f"- `alphas`: `{params['alphas']}`",
        "",
        "## 总表",
        "",
        "| P | alpha | cutoff | side | S_Y | T_Y | T/S | cap margin | cap pass | I2 | M | forced upper | forced margin | forced pass | uncovered | harmonic | log(1/a) |",
        "|---:|---:|---:|---|---:|---:|---:|---:|---|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for record in result["records"]:
        ratio = record["incidence_ratio"]
        lines.append(
            f"| {record['p']} | {record['alpha']:.3f} | {record['cutoff']} | "
            f"{record['side']} | {record['skeleton_count']} | "
            f"{record['total_hits']} | "
            f"{ratio:.6f} | "
            f"{record['capacity_margin']} | {record['capacity_pass']} | "
            f"{record['pair_intersections']} | "
            f"{record['multiplicity_bound']['m_bound']} | "
            f"{record['forced_union_upper']} | {record['forced_margin']} | "
            f"{record['forced_pass']} | {record['uncovered_count']} | "
            f"{record['harmonic_high']:.6f} | "
            f"{record['model_constant_log_1_over_alpha']:.6f} |"
        )

    lines.extend(["", "## 最强 q 线", ""])
    for record in result["records"]:
        lines.extend(
            [
                f"### P={record['p']}, alpha={record['alpha']:.3f}, side={record['side']}",
                "",
                f"- `basis_primes`: `{record['multiplicity_bound']['basis_primes']}`",
                f"- `low_prime_count`: `{record['low_prime_count']}`",
                f"- `high_prime_count`: `{record['high_prime_count']}`",
                "",
                "| q | hit count |",
                "|---:|---:|",
            ]
        )
        for row in record["top_q"]:
            lines.append(f"| {row['q']} | {row['hit_count']} |")
        lines.append("")

    lines.extend(
        [
            "## 结构解释",
            "",
            "轮提升不变性允许把全部 `q<=Y=P^alpha` 的斜线移入底座。若剩余高素 `q in (Y,P)` 的总命中 `T_Y` 已满足 `T_Y<|S_Y|`，则全覆盖不可能。这是比二重交叉证书更强的一阶容量出口。",
            "",
            "启发式比值是 `sum_{Y<q<P}1/q≈log(1/alpha)`。因此 `alpha>e^{-1}` 时模型常数小于 `1`。审计的目的不是替代证明，而是量化需要证明的短区间粗数分布与高素命中上界余量。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def parse_floats(raw: str) -> list[float]:
    """解析逗号分隔浮点数。"""
    return [float(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="10007,36739,99991")
    parser.add_argument("--alphas", default="0.38,0.40,0.43,0.45,0.49")
    parser.add_argument(
        "--out-prefix",
        default="docs/dynamic_promoted_rough_capacity_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.primes), parse_floats(args.alphas))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
