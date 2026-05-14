#!/usr/bin/env python3
"""审计 crossing 前驱短区间的整数容量与 Buchstab 命中密度。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_predecessor_density_ledger.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json
  docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-density-ledger.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-predecessor-density-ledger.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "BlockMultiplicityAndBuchstabDensityOnPredecessorIntervalsOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json",
    "prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json",
]


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
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def factor_multiset(n: int, trial_primes: list[int]) -> list[int]:
    """返回 n 的素因子重数列表，按从小到大排列。"""
    value = n
    factors: list[int] = []
    for prime in trial_primes:
        if prime * prime > value:
            break
        while value % prime == 0:
            factors.append(prime)
            value //= prime
    if value > 1:
        factors.append(value)
    return factors


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def factor_depth_bound(p: int, z: int) -> int:
    """计算 z-rough cofactor 最大素因子个数上界。"""
    upper = (p * p + p - 1) / z
    depth = 0
    power = 1.0
    while power < upper:
        depth += 1
        power *= z + 1
    return max(0, depth - 1)


def delete_residue(allowed: bytearray, p: int, p2: int, q: int) -> None:
    """从 allowed 中删除 k == -P^2 mod q 的列。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start < p:
        allowed[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)


def crossing_from_factors(p: int, q: int, factors: list[int]) -> tuple[int, int, int]:
    """返回 crossing 记录 `(D_minus, r, tail)`。"""
    prefix = q
    for idx, factor in enumerate(factors):
        before = prefix
        prefix *= factor
        if prefix > p:
            tail = 1
            for rest in factors[idx + 1 :]:
                tail *= rest
            return before, factor, tail
    return prefix, 1, 1


def interval_integer_capacity(p2: int, p: int, d_minus: int) -> int:
    """返回 `P^2/D < u <= (P^2+P-1)/D` 的整数容量。"""
    return max(0, (p2 + p - 1) // d_minus - p2 // d_minus)


def width_bucket_from_capacity(capacity: int) -> str:
    """按整数容量分桶。"""
    if capacity <= 1:
        return "C0:<=1"
    if capacity <= 3:
        return "C1:2-3"
    if capacity <= 7:
        return "C2:4-7"
    if capacity <= 15:
        return "C3:8-15"
    if capacity <= 31:
        return "C4:16-31"
    if capacity <= 63:
        return "C5:32-63"
    if capacity <= 127:
        return "C6:64-127"
    return "C7:>=128"


def register_bucket(buckets: dict[str, dict[str, float]], key: str, hits: int, capacity: int) -> None:
    """登记桶的命中和容量。"""
    row = buckets.setdefault(key, {"hits": 0.0, "capacity": 0.0, "predecessors": 0.0})
    row["hits"] += hits
    row["capacity"] += capacity
    row["predecessors"] += 1


def finalize_buckets(buckets: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    """给桶补充密度。"""
    result: dict[str, dict[str, float]] = {}
    for key, row in sorted(buckets.items()):
        capacity = row["capacity"]
        result[key] = {
            "hits": row["hits"],
            "capacity": capacity,
            "predecessors": row["predecessors"],
            "density": 0.0 if capacity == 0 else row["hits"] / capacity,
        }
    return result


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的前驱密度。"""
    p2 = p * p
    predecessor_hits: dict[int, int] = {}
    predecessor_capacity: dict[int, int] = {}
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            d_minus, _crossing_prime, _tail = crossing_from_factors(p, q, factor_multiset(m, trial_primes))
            predecessor_hits[d_minus] = predecessor_hits.get(d_minus, 0) + 1
            if d_minus not in predecessor_capacity:
                predecessor_capacity[d_minus] = interval_integer_capacity(p2, p, d_minus)
    buckets: dict[str, dict[str, float]] = {}
    over_capacity_count = 0
    total_hits = 0
    total_capacity = 0
    max_density = 0.0
    top_density_predecessor = None
    top_hit_predecessor = None
    for d_minus, hits in predecessor_hits.items():
        capacity = predecessor_capacity[d_minus]
        total_hits += hits
        total_capacity += capacity
        if hits > capacity:
            over_capacity_count += 1
        density = 0.0 if capacity == 0 else hits / capacity
        if density > max_density:
            max_density = density
            top_density_predecessor = {
                "d_minus": d_minus,
                "hits": hits,
                "capacity": capacity,
                "density": density,
            }
        if top_hit_predecessor is None or hits > top_hit_predecessor["hits"]:
            top_hit_predecessor = {
                "d_minus": d_minus,
                "hits": hits,
                "capacity": capacity,
                "density": density,
            }
        register_bucket(buckets, width_bucket_from_capacity(capacity), hits, capacity)
    bucket_rows = finalize_buckets(buckets)
    high_capacity = sum(row["capacity"] for key, row in bucket_rows.items() if key >= "C7")
    high_capacity_hits = sum(row["hits"] for key, row in bucket_rows.items() if key >= "C7")
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "cofactor_hits": total_hits,
        "active_predecessor_count": len(predecessor_hits),
        "integer_capacity_sum": total_capacity,
        "hits_per_integer_capacity": None if total_capacity == 0 else total_hits / total_capacity,
        "over_capacity_predecessor_count": over_capacity_count,
        "max_predecessor_density": max_density,
        "top_density_predecessor": top_density_predecessor,
        "top_hit_predecessor": top_hit_predecessor,
        "capacity_bucket_rows": bucket_rows,
        "large_capacity_bucket_hits": high_capacity_hits,
        "large_capacity_bucket_capacity": high_capacity,
        "large_capacity_bucket_density": 0.0 if high_capacity == 0 else high_capacity_hits / high_capacity,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的前驱密度。"""
    p2 = p * p
    cutoffs = cutoffs_for_p(p)
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    prime_index = 0
    rows = []
    for cutoff in cutoffs:
        previous = 0 if not rows else rows[-1].get("cutoff", 0)
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= BASE_D and factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, allowed, block_primes, trial_primes))
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            delete_residue(allowed, p, p2, primes[prime_index])
            prime_index += 1
        if not rows or rows[-1].get("cutoff") != cutoff:
            rows.append({"p": p, "previous_cutoff": previous, "cutoff": cutoff, "skipped": True})
    low_rows = [row for row in rows if not row.get("skipped")]
    worst = max(low_rows, key=lambda item: item["cofactor_hits"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(low_rows),
        "total_hits": sum(row["cofactor_hits"] for row in low_rows),
        "integer_capacity_sum": sum(row["integer_capacity_sum"] for row in low_rows),
        "over_capacity_predecessor_count": sum(row["over_capacity_predecessor_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_predecessor_density_ledger.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve_bool(max(trial_limit, max_p))
    trial_primes = primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes))
    rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(rows, key=lambda item: item["cofactor_hits"], default=None)
    total_hits = sum(profile["total_hits"] for profile in profiles)
    total_capacity = sum(profile["integer_capacity_sum"] for profile in profiles)
    over_capacity = sum(profile["over_capacity_predecessor_count"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_predecessor_density_ledger",
        "status": "predecessor_u_capacity_multiplicity_density_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "predecessor_integer_capacity_bound_closed": over_capacity == 0,
        "over_capacity_predecessor_count": over_capacity,
        "total_lowalpha_hits": total_hits,
        "total_integer_capacity": total_capacity,
        "total_hits_per_integer_capacity": None if total_capacity == 0 else total_hits / total_capacity,
        "u_capacity_alone_sufficient_for_first_moment_bound": False,
        "block_multiplicity_bound_proved": False,
        "buchstab_density_bound_proved": False,
        "row_column_unconditional_closed": False,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "固定 crossing 前驱 `D_-` 后，`u=r*t` 落在整数短区间 "
            "`P^2/D_- < u <= (P^2+P-1)/D_-`。这给出 `u` 值容量，"
            "但一阶负载可因同一 `u` 被块内多个 `q` 命中而超过该容量。"
            "因此剩余必须同时控制 block-multiplicity 与 prime/rough Buchstab 密度，"
            "或把异常登记为 PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 前驱密度账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"predecessor_u_capacity_bound_closed={fmt_bool(result['predecessor_integer_capacity_bound_closed'])}",
        f"over_capacity_predecessor_count={result['over_capacity_predecessor_count']}",
        f"u_capacity_alone_sufficient_for_first_moment_bound={fmt_bool(result['u_capacity_alone_sufficient_for_first_moment_bound'])}",
        f"block_multiplicity_bound_proved={fmt_bool(result['block_multiplicity_bound_proved'])}",
        f"buchstab_density_bound_proved={fmt_bool(result['buchstab_density_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总体容量",
        "",
        "| total hits | integer capacity | hits/capacity |",
        "| ---: | ---: | ---: |",
        f"| {result['total_lowalpha_hits']} | {result['total_integer_capacity']} | {result['total_hits_per_integer_capacity']:.6f} |",
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | hits | active D_- | capacity | hits/capacity | top-hit D_- | top-density D_- | large-cap density |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- | --- | ---: |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | {worst['active_predecessor_count']} | "
            f"{worst['integer_capacity_sum']} | {worst['hits_per_integer_capacity']:.6f} | "
            f"`{worst['top_hit_predecessor']}` | `{worst['top_density_predecessor']}` | "
            f"{worst['large_capacity_bucket_density']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | total hits | integer capacity | hits/capacity | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        density = 0.0 if profile["integer_capacity_sum"] == 0 else profile["total_hits"] / profile["integer_capacity_sum"]
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"{profile['integer_capacity_sum']} | {density:.6f} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：逐前驱 `u` 短区间公式和整数容量账本。",
            "- 未闭合：一阶负载允许同一 `u` 被多个块内 `q` 重复命中，故单纯 `u` 容量不能闭合。",
            "- 未闭合：即使剥离 multiplicity，容量总和仍过宽，还需 Buchstab rough/prime 密度上界。",
            f"- 下一目标：`{NEXT_TARGET}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "predecessor_integer_capacity_bound_closed": result["predecessor_integer_capacity_bound_closed"],
                "total_hits_per_integer_capacity": result["total_hits_per_integer_capacity"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
