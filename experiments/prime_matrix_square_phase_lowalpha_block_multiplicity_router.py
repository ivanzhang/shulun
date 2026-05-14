#!/usr/bin/env python3
"""审计 crossing 前驱短区间中的块素数重数乘子。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_block_multiplicity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-block-multiplicity-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-block-multiplicity-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-block-multiplicity-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-block-multiplicity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-block-multiplicity-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "OmegaBlockWeightedBuchstabDensityBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-predecessor-density-ledger.json",
    "prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json",
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


def crossing_from_factors(p: int, q: int, factors: list[int]) -> tuple[int, int]:
    """返回 crossing 前驱 `D_-` 与剩余 `u`。"""
    prefix = q
    for idx, factor in enumerate(factors):
        before = prefix
        prefix *= factor
        if prefix > p:
            tail = 1
            for rest in factors[idx:]:
                tail *= rest
            return before, tail
    return prefix, 1


def interval_integer_capacity(p2: int, p: int, d_minus: int) -> int:
    """返回 `P^2/D < u <= (P^2+P-1)/D` 的整数容量。"""
    return max(0, (p2 + p - 1) // d_minus - p2 // d_minus)


def block_omega(d_minus: int, block_primes: list[int]) -> int:
    """计算 `D_-` 中可作为原始块素数 q 的不同因子数。"""
    return sum(1 for q in block_primes if d_minus % q == 0)


def omega_bucket(omega: int) -> str:
    """按块素数因子数分桶。"""
    if omega <= 0:
        return "O0"
    if omega == 1:
        return "O1"
    if omega == 2:
        return "O2"
    if omega == 3:
        return "O3"
    return "O4+"


def register_bucket(buckets: dict[str, dict[str, float]], key: str, hits: int, capacity: int, weighted: int) -> None:
    """登记桶的命中、容量和加权容量。"""
    row = buckets.setdefault(key, {"hits": 0.0, "capacity": 0.0, "weighted_capacity": 0.0, "predecessors": 0.0})
    row["hits"] += hits
    row["capacity"] += capacity
    row["weighted_capacity"] += weighted
    row["predecessors"] += 1


def finalize_buckets(buckets: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    """给桶补充密度。"""
    result: dict[str, dict[str, float]] = {}
    for key, row in sorted(buckets.items()):
        capacity = row["capacity"]
        weighted = row["weighted_capacity"]
        result[key] = {
            "hits": row["hits"],
            "capacity": capacity,
            "weighted_capacity": weighted,
            "predecessors": row["predecessors"],
            "density": 0.0 if capacity == 0 else row["hits"] / capacity,
            "weighted_density": 0.0 if weighted == 0 else row["hits"] / weighted,
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
    """审计一个 low-alpha block 的块素数重数。"""
    p2 = p * p
    key_qs: dict[tuple[int, int], set[int]] = {}
    predecessor_hits: dict[int, int] = {}
    predecessor_capacity: dict[int, int] = {}
    predecessor_omega: dict[int, int] = {}
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            d_minus, u = crossing_from_factors(p, q, factor_multiset(m, trial_primes))
            key_qs.setdefault((d_minus, u), set()).add(q)
            predecessor_hits[d_minus] = predecessor_hits.get(d_minus, 0) + 1
            if d_minus not in predecessor_capacity:
                predecessor_capacity[d_minus] = interval_integer_capacity(p2, p, d_minus)
                predecessor_omega[d_minus] = block_omega(d_minus, block_primes)
    multiplicity_failures = 0
    max_actual_multiplicity = 0
    top_multiplicity_key = None
    for (d_minus, u), qs in key_qs.items():
        multiplicity = len(qs)
        omega = predecessor_omega[d_minus]
        if multiplicity > omega:
            multiplicity_failures += 1
        if multiplicity > max_actual_multiplicity:
            max_actual_multiplicity = multiplicity
            top_multiplicity_key = {
                "d_minus": d_minus,
                "u": u,
                "multiplicity": multiplicity,
                "omega_block": omega,
                "q_values": sorted(qs),
            }
    buckets: dict[str, dict[str, float]] = {}
    total_hits = 0
    total_capacity = 0
    total_weighted_capacity = 0
    max_omega = 0
    top_hit_predecessor = None
    top_weighted_density_predecessor = None
    for d_minus, hits in predecessor_hits.items():
        capacity = predecessor_capacity[d_minus]
        omega = predecessor_omega[d_minus]
        weighted = capacity * omega
        total_hits += hits
        total_capacity += capacity
        total_weighted_capacity += weighted
        max_omega = max(max_omega, omega)
        density = 0.0 if capacity == 0 else hits / capacity
        weighted_density = 0.0 if weighted == 0 else hits / weighted
        row = {
            "d_minus": d_minus,
            "hits": hits,
            "capacity": capacity,
            "omega_block": omega,
            "weighted_capacity": weighted,
            "density": density,
            "weighted_density": weighted_density,
        }
        if top_hit_predecessor is None or hits > top_hit_predecessor["hits"]:
            top_hit_predecessor = row
        if top_weighted_density_predecessor is None or weighted_density > top_weighted_density_predecessor["weighted_density"]:
            top_weighted_density_predecessor = row
        register_bucket(buckets, omega_bucket(omega), hits, capacity, weighted)
    bucket_rows = finalize_buckets(buckets)
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "cofactor_hits": total_hits,
        "unique_du_key_count": len(key_qs),
        "active_predecessor_count": len(predecessor_hits),
        "integer_capacity_sum": total_capacity,
        "omega_weighted_capacity_sum": total_weighted_capacity,
        "hits_per_integer_capacity": None if total_capacity == 0 else total_hits / total_capacity,
        "hits_per_omega_weighted_capacity": None if total_weighted_capacity == 0 else total_hits / total_weighted_capacity,
        "multiplicity_bound_failure_count": multiplicity_failures,
        "max_actual_multiplicity": max_actual_multiplicity,
        "max_omega_block": max_omega,
        "top_multiplicity_key": top_multiplicity_key,
        "top_hit_predecessor": top_hit_predecessor,
        "top_weighted_density_predecessor": top_weighted_density_predecessor,
        "omega_bucket_rows": bucket_rows,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的块素数重数。"""
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
        "omega_weighted_capacity_sum": sum(row["omega_weighted_capacity_sum"] for row in low_rows),
        "multiplicity_bound_failure_count": sum(row["multiplicity_bound_failure_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_block_multiplicity_router.py": file_sha256(
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
    failures = sum(profile["multiplicity_bound_failure_count"] for profile in profiles)
    total_hits = sum(profile["total_hits"] for profile in profiles)
    total_capacity = sum(profile["integer_capacity_sum"] for profile in profiles)
    total_weighted = sum(profile["omega_weighted_capacity_sum"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_block_multiplicity_router",
        "status": "block_multiplicity_reduced_to_omega_block_weighted_density_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "block_multiplicity_bound_closed": failures == 0,
        "multiplicity_bound_failure_count": failures,
        "total_lowalpha_hits": total_hits,
        "total_integer_capacity": total_capacity,
        "total_omega_weighted_capacity": total_weighted,
        "total_hits_per_integer_capacity": None if total_capacity == 0 else total_hits / total_capacity,
        "total_hits_per_omega_weighted_capacity": None if total_weighted == 0 else total_hits / total_weighted,
        "omega_weighted_density_bound_proved": False,
        "row_column_unconditional_closed": False,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "固定 `(D_-,u)` 后，一阶负载的重复命中只能来自 `D_-` 中属于当前 dyadic 块的原始素数因子。"
            "因此实际 multiplicity 被 `omega_B(D_-)` 控制；样本中该上界无失败。"
            "剩余硬点从无结构重复计数压成 `omega_B(D_-)` 加权的 Buchstab 短区间密度上界，"
            "或失败形成块素数因子 PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha block multiplicity 路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"block_multiplicity_bound_closed={fmt_bool(result['block_multiplicity_bound_closed'])}",
        f"multiplicity_bound_failure_count={result['multiplicity_bound_failure_count']}",
        f"omega_weighted_density_bound_proved={fmt_bool(result['omega_weighted_density_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总体容量",
        "",
        "| hits | u capacity | hits/u capacity | omega weighted capacity | hits/weighted |",
        "| ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['total_lowalpha_hits']} | {result['total_integer_capacity']} | "
            f"{result['total_hits_per_integer_capacity']:.6f} | {result['total_omega_weighted_capacity']} | "
            f"{result['total_hits_per_omega_weighted_capacity']:.6f} |"
        ),
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | hits | unique (D,u) | active D | weighted capacity | weighted density | max mult | max omega | top mult key |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | {worst['unique_du_key_count']} | "
            f"{worst['active_predecessor_count']} | {worst['omega_weighted_capacity_sum']} | "
            f"{worst['hits_per_omega_weighted_capacity']:.6f} | "
            f"{worst['max_actual_multiplicity']} | {worst['max_omega_block']} | "
            f"`{worst['top_multiplicity_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | hits | weighted capacity | hits/weighted | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        density = 0.0 if profile["omega_weighted_capacity_sum"] == 0 else profile["total_hits"] / profile["omega_weighted_capacity_sum"]
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"{profile['omega_weighted_capacity_sum']} | {density:.6f} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：固定 `(D_-,u)` 的重复命中数不超过 `omega_B(D_-)`。",
            "- 未闭合：需要证明 `omega_B(D_-)` 加权后的 Buchstab 短区间密度上界。",
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
                "block_multiplicity_bound_closed": result["block_multiplicity_bound_closed"],
                "total_hits_per_omega_weighted_capacity": result["total_hits_per_omega_weighted_capacity"],
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
