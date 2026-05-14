#!/usr/bin/env python3
"""审计 low-alpha Buchstab 因子前缀跨 P 后的单位容量账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_buchstab_crossing_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "CrossingPrefixDistributionBoundOrPDEC"
PRIME_TARGET = "PrimeAnchorRFPOrSelbergDistributionLedger"

SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json",
    "prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json",
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


def residual_interval_capacity(p2: int, p: int, modulus: int) -> int:
    """固定前缀模数 D 后，剩余 cofactor 的整数区间容量。"""
    left = p2 // modulus + 1
    right = (p2 + p - 1) // modulus
    return max(0, right - left + 1)


def dyadic_power_bucket(value: int, p: int) -> str:
    """按相对 P 的 dyadic 尺度分桶。"""
    ratio = value / p
    if ratio <= 0:
        return "invalid"
    level = math.floor(math.log(ratio, 2))
    return f"C{level}:({2**level}P,{2**(level + 1)}P]"


def register(mapping: dict[str, int], key: str) -> None:
    """登记计数。"""
    mapping[key] = mapping.get(key, 0) + 1


def crossing_record(p: int, q: int, m: int, factors: list[int]) -> dict[str, Any]:
    """计算 q*m 因子前缀第一次跨过 P 的记录。"""
    prefix = q
    before = q
    crossing_depth = 0
    crossing_prime = None
    crossing_factors: list[int] = []
    for factor in factors:
        before = prefix
        prefix *= factor
        crossing_factors.append(factor)
        crossing_depth += 1
        if prefix > p:
            crossing_prime = factor
            break
    return {
        "before_product": before,
        "crossing_product": prefix,
        "crossing_depth": crossing_depth,
        "crossing_prime": crossing_prime,
        "crossing_factors": crossing_factors,
        "is_prime_anchor": len(factors) == 1,
    }


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的跨 P 单位容量。"""
    p2 = p * p
    hits = 0
    composite_hits = 0
    prime_anchor_hits = 0
    crossing_failures = 0
    unit_capacity_failures = 0
    exact_key_hits: dict[str, int] = {}
    crossing_depth_counts: dict[str, int] = {}
    composite_depth_counts: dict[str, int] = {}
    crossing_bucket_counts: dict[str, int] = {}
    top_examples = []
    max_capacity_after_crossing = 0
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            factors = factor_multiset(m, trial_primes)
            record = crossing_record(p, q, m, factors)
            hits += 1
            if record["is_prime_anchor"]:
                prime_anchor_hits += 1
            else:
                composite_hits += 1
            if not (record["before_product"] <= p < record["crossing_product"]):
                crossing_failures += 1
            cap = residual_interval_capacity(p2, p, record["crossing_product"])
            max_capacity_after_crossing = max(max_capacity_after_crossing, cap)
            if cap > 1:
                unit_capacity_failures += 1
            key = f"{q}:{'*'.join(str(item) for item in record['crossing_factors'])}"
            exact_key_hits[key] = exact_key_hits.get(key, 0) + 1
            register(crossing_depth_counts, str(record["crossing_depth"]))
            if not record["is_prime_anchor"]:
                register(composite_depth_counts, str(record["crossing_depth"]))
            register(crossing_bucket_counts, dyadic_power_bucket(record["crossing_product"], p))
            if len(top_examples) < 8:
                top_examples.append(
                    {
                        "q": q,
                        "m": m,
                        "factors_prefix": record["crossing_factors"],
                        "before_product": record["before_product"],
                        "crossing_product": record["crossing_product"],
                        "capacity_after_crossing": cap,
                    }
                )
    collision_keys = {key: count for key, count in exact_key_hits.items() if count > 1}
    top_key = max(exact_key_hits.items(), key=lambda item: item[1], default=(None, 0))
    top_bucket = max(crossing_bucket_counts.items(), key=lambda item: item[1], default=(None, 0))
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "cofactor_hits": hits,
        "prime_anchor_hits": prime_anchor_hits,
        "composite_anchor_hits": composite_hits,
        "crossing_failure_count": crossing_failures,
        "unit_capacity_failure_count": unit_capacity_failures,
        "max_capacity_after_crossing": max_capacity_after_crossing,
        "exact_crossing_key_count": len(exact_key_hits),
        "exact_crossing_key_collision_count": len(collision_keys),
        "max_exact_crossing_key_multiplicity": top_key[1],
        "top_exact_crossing_key": top_key[0],
        "crossing_depth_counts": crossing_depth_counts,
        "composite_crossing_depth_counts": composite_depth_counts,
        "crossing_bucket_counts": crossing_bucket_counts,
        "top_crossing_bucket": top_bucket[0],
        "top_crossing_bucket_count": top_bucket[1],
        "sample_crossing_examples": top_examples,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 low-alpha 跨 P 单位容量。"""
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
        "prime_anchor_hits": sum(row["prime_anchor_hits"] for row in low_rows),
        "composite_anchor_hits": sum(row["composite_anchor_hits"] for row in low_rows),
        "crossing_failure_count": sum(row["crossing_failure_count"] for row in low_rows),
        "unit_capacity_failure_count": sum(row["unit_capacity_failure_count"] for row in low_rows),
        "exact_crossing_key_collision_count": sum(row["exact_crossing_key_collision_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_buchstab_crossing_capacity_router.py": file_sha256(
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
    crossing_failures = sum(profile["crossing_failure_count"] for profile in profiles)
    unit_failures = sum(profile["unit_capacity_failure_count"] for profile in profiles)
    collision_count = sum(profile["exact_crossing_key_collision_count"] for profile in profiles)
    total_hits = sum(profile["total_hits"] for profile in profiles)
    prime_hits = sum(profile["prime_anchor_hits"] for profile in profiles)
    composite_hits = sum(profile["composite_anchor_hits"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_buchstab_crossing_capacity_router",
        "status": "lowalpha_buchstab_crossing_unit_capacity_reduction_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "crossing_prefix_exists_and_brackets_p": crossing_failures == 0,
        "post_crossing_unit_capacity_checked": unit_failures == 0,
        "exact_crossing_key_collision_free": collision_count == 0,
        "crossing_failure_count": crossing_failures,
        "unit_capacity_failure_count": unit_failures,
        "exact_crossing_key_collision_count": collision_count,
        "total_lowalpha_hits": total_hits,
        "prime_anchor_hits": prime_hits,
        "composite_anchor_hits": composite_hits,
        "crossing_distribution_bound_proved": False,
        "row_column_unconditional_closed": False,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "parallel_attack_target": PRIME_TARGET,
        "plain_conclusion": (
            "low-alpha Buchstab 命中沿 `q` 加互补因子素因子前缀继续展开，"
            "每条路径唯一存在第一次跨过 `P` 的前缀 `D_-<=P<D_+`。"
            "固定精确 crossing 前缀 `D_+` 后，剩余 cofactor 区间长度小于一，"
            "所以局部多重容量已经消失；若仍有反例负载，只能来自 crossing 前缀集合的全局分布过密或 PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Buchstab crossing 容量路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"crossing_prefix_exists_and_brackets_p={fmt_bool(result['crossing_prefix_exists_and_brackets_p'])}",
        f"post_crossing_unit_capacity_checked={fmt_bool(result['post_crossing_unit_capacity_checked'])}",
        f"exact_crossing_key_collision_free={fmt_bool(result['exact_crossing_key_collision_free'])}",
        f"crossing_distribution_bound_proved={fmt_bool(result['crossing_distribution_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总体账本",
        "",
        "| total hits | prime anchor | composite anchor | crossing failures | unit failures | key collisions |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['total_lowalpha_hits']} | {result['prime_anchor_hits']} | "
            f"{result['composite_anchor_hits']} | {result['crossing_failure_count']} | "
            f"{result['unit_capacity_failure_count']} | {result['exact_crossing_key_collision_count']} |"
        ),
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | hits | composite | max post-cross capacity | top key | max key multiplicity | depth counts | top crossing bucket |",
        "| ---: | --- | ---: | ---: | ---: | --- | ---: | --- | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | {worst['composite_anchor_hits']} | "
            f"{worst['max_capacity_after_crossing']} | `{worst['top_exact_crossing_key']}` | "
            f"{worst['max_exact_crossing_key_multiplicity']} | "
            f"`{worst['crossing_depth_counts']}` | `{worst['top_crossing_bucket']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | total hits | prime | composite | worst block | worst depth counts |",
            "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"{profile['prime_anchor_hits']} | {profile['composite_anchor_hits']} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` | `{row['crossing_depth_counts']}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：每条 Buchstab 因子路径存在唯一 crossing edge `D_-<=P<D_+`。",
            "- 已闭合：crossing 后的剩余整数区间容量至多一；精确 crossing key 无重复命中。",
            f"- 未闭合：`{NEXT_TARGET}`，即 crossing 前缀集合的全局分布上界或 PDEC 排斥。",
            f"- 并行保留：`{PRIME_TARGET}`，处理 `m` 本身为素数的 prime-anchor 分支。",
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
                "crossing_prefix_exists_and_brackets_p": result["crossing_prefix_exists_and_brackets_p"],
                "post_crossing_unit_capacity_checked": result["post_crossing_unit_capacity_checked"],
                "exact_crossing_key_collision_free": result["exact_crossing_key_collision_free"],
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
