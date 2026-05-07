#!/usr/bin/env python3
"""审计提升轮骨架上的强制重叠证书。

用法示例：
  python3 experiments/prime_matrix_promoted_wheel_forced_overlap_audit.py \
    --primes 10007,36739 --wheels 510510,9699690 \
    --out-prefix docs/promoted_wheel_forced_overlap_audit_20260506

证明接口：
  对轮骨架 S 上的剩余 q 斜线，令
    T  = 总命中次数；
    U  = 被命中的不同偏移数；
    I2 = sum_k binom(m_k,2)，其中 m_k 是偏移 k 的 q 标签数；
    M  = 任一点最大可能 q 标签数。

  因 binom(m,2) <= M(m-1)/2，可得强制重叠下界
    T-U >= 2*I2/M。
  若 T - ceil(2*I2/M) < |S|，则即使不逐点枚举未覆盖点，
  也能由二重交叉和重数上界推出不可能全覆盖。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from itertools import combinations
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


def in_wheel_skeleton(p: int, k: int, modulus: int, side: str) -> bool:
    """判断偏移 k 是否落在 W 轮骨架。"""
    if side == "plus":
        value = p * p + k
    elif side == "minus":
        value = p * p - k
    else:
        raise ValueError(f"unknown side: {side}")
    return math.gcd(value, modulus) == 1


def m_interval_for_q(p: int, q: int, side: str) -> tuple[int, int]:
    """返回 q*m 落入平方前/后行时的 m 区间。"""
    if side == "plus":
        low = p * p + 1
        high = p * p + p - 1
    elif side == "minus":
        low = p * p - p + 1
        high = p * p - 1
    else:
        raise ValueError(f"unknown side: {side}")
    return (low + q - 1) // q, high // q


def k_from_qm(p: int, q: int, m: int, side: str) -> int:
    """由 q*m 还原行内偏移。"""
    if side == "plus":
        return q * m - p * p
    if side == "minus":
        return p * p - q * m
    raise ValueError(f"unknown side: {side}")


def multiplicity_bound_by_primorial(
    p: int, modulus: int, primes: list[int], side: str
) -> dict:
    """用最小剩余素数连乘给出单点 q 标签数上界。"""
    if side == "plus":
        n_max = p * p + p - 1
    elif side == "minus":
        n_max = p * p - 1
    else:
        raise ValueError(f"unknown side: {side}")

    product = 1
    used = []
    for q in primes:
        if q >= p:
            break
        if math.gcd(q, modulus) != 1:
            continue
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


def audit_one(p: int, modulus: int, side: str, primes: list[int]) -> dict:
    """审计单个 P,W,side 的强制重叠证书。"""
    skeleton = {
        k for k in range(1, p) if in_wheel_skeleton(p, k, modulus, side)
    }
    labels: dict[int, list[int]] = {}
    q_hit_counts = []

    for q in primes:
        if q >= p:
            break
        if math.gcd(q, modulus) != 1:
            continue
        m_min, m_max = m_interval_for_q(p, q, side)
        hits = 0
        for m in range(m_min, m_max + 1):
            if math.gcd(m, modulus) != 1:
                continue
            k = k_from_qm(p, q, m, side)
            if 1 <= k < p:
                labels.setdefault(k, []).append(q)
                hits += 1
        if hits:
            q_hit_counts.append({"q": q, "hit_count": hits})

    multiplicities = [len(items) for items in labels.values()]
    pair_counter: Counter[tuple[int, int]] = Counter()
    for items in labels.values():
        if len(items) < 2:
            continue
        pair_counter.update(combinations(sorted(items), 2))
    total_hits = sum(multiplicities)
    covered_count = len(labels)
    overlap_excess = total_hits - covered_count
    pair_intersections = sum(m * (m - 1) // 2 for m in multiplicities)
    exact_max_multiplicity = max(multiplicities, default=0)
    mult_bound = multiplicity_bound_by_primorial(p, modulus, primes, side)
    m_bound = max(1, mult_bound["m_bound"])
    forced_overlap_lower = math.ceil(2 * pair_intersections / m_bound)
    forced_union_upper = total_hits - forced_overlap_lower
    skeleton_count = len(skeleton)
    pair_certificate_margin = skeleton_count - forced_union_upper
    uncovered = sorted(skeleton - set(labels))
    multiplicity_hist = dict(sorted(Counter(multiplicities).items()))
    top_q = sorted(q_hit_counts, key=lambda item: -item["hit_count"])[:12]
    top_pairs = [
        {"q1": pair[0], "q2": pair[1], "intersection_count": count}
        for pair, count in pair_counter.most_common(12)
    ]

    return {
        "p": p,
        "modulus": modulus,
        "side": side,
        "wheel_factors": factor_distinct(modulus),
        "skeleton_count": skeleton_count,
        "covered_count": covered_count,
        "uncovered_count": len(uncovered),
        "uncovered_first": uncovered[:20],
        "total_hits": total_hits,
        "overlap_excess": overlap_excess,
        "pair_intersections": pair_intersections,
        "exact_max_multiplicity": exact_max_multiplicity,
        "multiplicity_bound": mult_bound,
        "forced_overlap_lower": forced_overlap_lower,
        "forced_union_upper": forced_union_upper,
        "pair_certificate_margin": pair_certificate_margin,
        "pair_certificate_pass": forced_union_upper < skeleton_count,
        "multiplicity_hist": multiplicity_hist,
        "top_q": top_q,
        "top_pairs": top_pairs,
    }


def audit(primes: list[int], wheels: list[int]) -> dict:
    """执行审计。"""
    prime_table = primes_from_table(sieve_bool(max(primes)))
    records = []
    for p in primes:
        for modulus in wheels:
            for side in ("minus", "plus"):
                records.append(audit_one(p, modulus, side, prime_table))
    return {"parameters": {"primes": primes, "wheels": wheels}, "records": records}


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# 提升轮强制重叠证书审计",
        "",
        "**状态：** `forced_overlap_certificate_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `primes`: `{params['primes']}`",
        f"- `wheels`: `{params['wheels']}`",
        "",
        "## 总表",
        "",
        "| P | W | side | skeleton | covered | uncovered | T | I2 | M_bound | forced union upper | margin | pass | max mult |",
        "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|",
    ]
    for record in result["records"]:
        lines.append(
            f"| {record['p']} | {record['modulus']} | {record['side']} | "
            f"{record['skeleton_count']} | {record['covered_count']} | "
            f"{record['uncovered_count']} | {record['total_hits']} | "
            f"{record['pair_intersections']} | "
            f"{record['multiplicity_bound']['m_bound']} | "
            f"{record['forced_union_upper']} | "
            f"{record['pair_certificate_margin']} | "
            f"{record['pair_certificate_pass']} | "
            f"{record['exact_max_multiplicity']} |"
        )

    lines.extend(["", "## 明细", ""])
    for record in result["records"]:
        bound = record["multiplicity_bound"]
        lines.extend(
            [
                f"### P={record['p']}, W={record['modulus']}, side={record['side']}",
                "",
                f"- `basis_primes`: `{bound['basis_primes']}`",
                f"- `basis_product`: `{bound['basis_product']}`",
                f"- `n_max`: `{bound['n_max']}`",
                f"- `multiplicity_hist`: `{record['multiplicity_hist']}`",
                f"- `uncovered_first`: `{record['uncovered_first']}`",
                "",
                "| q | hit count |",
                "|---:|---:|",
            ]
        )
        for row in record["top_q"]:
            lines.append(f"| {row['q']} | {row['hit_count']} |")
        lines.extend(
            [
                "",
                "Top q-pair intersections:",
                "",
                "| q1 | q2 | intersection count |",
                "|---:|---:|---:|",
            ]
        )
        for row in record["top_pairs"]:
            lines.append(
                f"| {row['q1']} | {row['q2']} | {row['intersection_count']} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 结构解释",
            "",
            "这份证书把集合覆盖失败从逐点幸存改写为强制重叠：剩余 q 斜线的总容量 `T` 不能直接当作可用覆盖，因为同一偏移会被多条 q 线同时命中。若任一点最多带 `M` 个剩余 q 标签，则",
            "",
            "\\[",
            "T-U\\ge {2I_2\\over M},",
            "\\]",
            "",
            "其中 `I2=sum_k binom(m_k,2)`。因此 `T-ceil(2I2/M)<|S|` 时，轮骨架 `S` 不可能被盖满。`M_bound` 由最小剩余素数连乘给出，不依赖随机模型。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析逗号分隔整数。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="10007,36739")
    parser.add_argument("--wheels", default="510510,9699690")
    parser.add_argument(
        "--out-prefix",
        default="docs/promoted_wheel_forced_overlap_audit_20260506",
    )
    args = parser.parse_args()
    result = audit(parse_ints(args.primes), parse_ints(args.wheels))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["parameters"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
