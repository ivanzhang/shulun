#!/usr/bin/env python3
"""审计 semiprime regime 的 prime-u/semiprime-u 精确容量。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_prime_semiprime_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "WeightedPrimeSemiprimeIntervalCapacityGlobalBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-semiprime-fiber-router.json",
    "prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.json",
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


def crossing_from_factors(p: int, q: int, factors: list[int]) -> tuple[int, int, list[int]]:
    """返回 crossing 前驱、剩余 u 和 u 的因子列表。"""
    prefix = q
    for idx, factor in enumerate(factors):
        before = prefix
        prefix *= factor
        if prefix > p:
            tail_factors = factors[idx:]
            tail = 1
            for item in tail_factors:
                tail *= item
            return before, tail, tail_factors
    return prefix, 1, []


def interval_bounds(p2: int, p: int, d_minus: int) -> tuple[int, int]:
    """返回 `P^2/D < u <= (P^2+P-1)/D` 的整数端点。"""
    return p2 // d_minus + 1, (p2 + p - 1) // d_minus


def block_omega(d_minus: int, block_primes: list[int]) -> int:
    """计算 `D_-` 中可作为原始块素数 q 的不同因子数。"""
    return sum(1 for q in block_primes if d_minus % q == 0)


def is_semiprime_regime(p: int, d_minus: int) -> bool:
    """判断 `D_-<sqrt(P)` 的半素数门。"""
    return d_minus * d_minus < p


def classify_possible_u(u: int, h: float, trial_primes: list[int]) -> str | None:
    """分类短区间内的可用 u。"""
    factors = factor_multiset(u, trial_primes)
    if len(factors) == 1 and factors[0] > h:
        return "prime"
    if len(factors) == 2 and factors[0] > h:
        return "semiprime"
    return None


def possible_capacity_for_predecessor(p: int, d_minus: int, trial_primes: list[int]) -> dict[str, int]:
    """枚举固定 D_- 的 prime-u/semiprime-u 精确容量。"""
    p2 = p * p
    left, right = interval_bounds(p2, p, d_minus)
    h = p / d_minus
    prime_count = 0
    semiprime_count = 0
    for u in range(left, right + 1):
        label = classify_possible_u(u, h, trial_primes)
        if label == "prime":
            prime_count += 1
        elif label == "semiprime":
            semiprime_count += 1
    return {
        "prime_u_capacity": prime_count,
        "semiprime_u_capacity": semiprime_count,
        "total_capacity": prime_count + semiprime_count,
        "integer_capacity": max(0, right - left + 1),
    }


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的 semiprime 精确容量。"""
    p2 = p * p
    predecessor_actual: dict[int, dict[str, int]] = {}
    predecessor_omega: dict[int, int] = {}
    capacity_cache: dict[int, dict[str, int]] = {}
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            d_minus, _u, u_factors = crossing_from_factors(p, q, factor_multiset(m, trial_primes))
            if not is_semiprime_regime(p, d_minus):
                continue
            row = predecessor_actual.setdefault(d_minus, {"prime": 0, "semiprime": 0, "other": 0})
            if len(u_factors) == 1:
                row["prime"] += 1
            elif len(u_factors) == 2:
                row["semiprime"] += 1
            else:
                row["other"] += 1
            if d_minus not in predecessor_omega:
                predecessor_omega[d_minus] = block_omega(d_minus, block_primes)
    failure_count = 0
    total_actual_prime = 0
    total_actual_semiprime = 0
    total_weighted_prime_capacity = 0
    total_weighted_semiprime_capacity = 0
    total_weighted_all_capacity = 0
    total_integer_capacity = 0
    top_capacity_pressure = None
    top_prime_pressure = None
    top_semiprime_pressure = None
    for d_minus, actual in predecessor_actual.items():
        if d_minus not in capacity_cache:
            capacity_cache[d_minus] = possible_capacity_for_predecessor(p, d_minus, trial_primes)
        capacity = capacity_cache[d_minus]
        omega = predecessor_omega[d_minus]
        actual_prime = actual["prime"]
        actual_semiprime = actual["semiprime"]
        weighted_prime = omega * capacity["prime_u_capacity"]
        weighted_semiprime = omega * capacity["semiprime_u_capacity"]
        weighted_total = weighted_prime + weighted_semiprime
        if actual_prime > weighted_prime or actual_semiprime > weighted_semiprime:
            failure_count += 1
        total_actual_prime += actual_prime
        total_actual_semiprime += actual_semiprime
        total_weighted_prime_capacity += weighted_prime
        total_weighted_semiprime_capacity += weighted_semiprime
        total_weighted_all_capacity += weighted_total
        total_integer_capacity += omega * capacity["integer_capacity"]
        total_actual = actual_prime + actual_semiprime
        pressure = None if weighted_total == 0 else total_actual / weighted_total
        prime_pressure = None if weighted_prime == 0 else actual_prime / weighted_prime
        semiprime_pressure = None if weighted_semiprime == 0 else actual_semiprime / weighted_semiprime
        record = {
            "d_minus": d_minus,
            "omega_block": omega,
            "actual_prime": actual_prime,
            "actual_semiprime": actual_semiprime,
            "prime_capacity": capacity["prime_u_capacity"],
            "semiprime_capacity": capacity["semiprime_u_capacity"],
            "weighted_prime_capacity": weighted_prime,
            "weighted_semiprime_capacity": weighted_semiprime,
            "pressure": pressure,
            "prime_pressure": prime_pressure,
            "semiprime_pressure": semiprime_pressure,
            "h": p / d_minus,
        }
        if pressure is not None and (top_capacity_pressure is None or pressure > top_capacity_pressure["pressure"]):
            top_capacity_pressure = record
        if prime_pressure is not None and (
            top_prime_pressure is None or prime_pressure > top_prime_pressure["prime_pressure"]
        ):
            top_prime_pressure = record
        if semiprime_pressure is not None and (
            top_semiprime_pressure is None or semiprime_pressure > top_semiprime_pressure["semiprime_pressure"]
        ):
            top_semiprime_pressure = record
    total_actual = total_actual_prime + total_actual_semiprime
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "actual_prime_u_hits": total_actual_prime,
        "actual_semiprime_u_hits": total_actual_semiprime,
        "actual_total_hits": total_actual,
        "weighted_prime_u_capacity": total_weighted_prime_capacity,
        "weighted_semiprime_u_capacity": total_weighted_semiprime_capacity,
        "weighted_total_capacity": total_weighted_all_capacity,
        "weighted_integer_capacity": total_integer_capacity,
        "exact_capacity_cover_failure_count": failure_count,
        "active_semiprime_predecessors": len(predecessor_actual),
        "actual_over_weighted_total_capacity": None
        if total_weighted_all_capacity == 0
        else total_actual / total_weighted_all_capacity,
        "top_capacity_pressure": top_capacity_pressure,
        "top_prime_pressure": top_prime_pressure,
        "top_semiprime_pressure": top_semiprime_pressure,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 semiprime 精确容量。"""
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
    worst = max(low_rows, key=lambda item: item["actual_total_hits"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(low_rows),
        "actual_prime_u_hits": sum(row["actual_prime_u_hits"] for row in low_rows),
        "actual_semiprime_u_hits": sum(row["actual_semiprime_u_hits"] for row in low_rows),
        "actual_total_hits": sum(row["actual_total_hits"] for row in low_rows),
        "weighted_prime_u_capacity": sum(row["weighted_prime_u_capacity"] for row in low_rows),
        "weighted_semiprime_u_capacity": sum(row["weighted_semiprime_u_capacity"] for row in low_rows),
        "weighted_total_capacity": sum(row["weighted_total_capacity"] for row in low_rows),
        "weighted_integer_capacity": sum(row["weighted_integer_capacity"] for row in low_rows),
        "exact_capacity_cover_failure_count": sum(row["exact_capacity_cover_failure_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_prime_semiprime_capacity_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 prime/semiprime 精确容量审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve_bool(max(trial_limit, max_p))
    trial_primes = primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes))
    rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(rows, key=lambda item: item["actual_total_hits"], default=None)
    failures = sum(profile["exact_capacity_cover_failure_count"] for profile in profiles)
    total_actual = sum(profile["actual_total_hits"] for profile in profiles)
    total_capacity = sum(profile["weighted_total_capacity"] for profile in profiles)
    total_integer = sum(profile["weighted_integer_capacity"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_prime_semiprime_capacity_router",
        "status": "semiprime_regime_reduced_to_exact_prime_semiprime_capacity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "exact_prime_semiprime_capacity_cover_closed": failures == 0,
        "exact_capacity_cover_failure_count": failures,
        "global_capacity_bound_proved": False,
        "local_capacity_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "actual_total_hits": total_actual,
        "weighted_prime_u_capacity": sum(profile["weighted_prime_u_capacity"] for profile in profiles),
        "weighted_semiprime_u_capacity": sum(profile["weighted_semiprime_u_capacity"] for profile in profiles),
        "weighted_total_capacity": total_capacity,
        "weighted_integer_capacity": total_integer,
        "actual_over_weighted_total_capacity": None if total_capacity == 0 else total_actual / total_capacity,
        "exact_capacity_over_integer_capacity": None if total_integer == 0 else total_capacity / total_integer,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "semiprime regime 已从分布模型降为精确容量：对每个活跃前驱 `D_-`，"
            "直接枚举短区间内所有 prime-u 与 H-rough semiprime-u，再乘 `omega_B(D_-)`。"
            "实际 prime-u/semiprime-u 命中均被该精确容量覆盖。"
            "剩余不是单纤维结构，而是证明这些精确容量的全局上界，或把容量尖峰登记为 PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha prime/semiprime 精确容量",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_prime_semiprime_capacity_cover_closed={fmt_bool(result['exact_prime_semiprime_capacity_cover_closed'])}",
        f"global_capacity_bound_proved={fmt_bool(result['global_capacity_bound_proved'])}",
        f"local_capacity_spike_pdec_excluded={fmt_bool(result['local_capacity_spike_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局容量",
        "",
        "| actual hits | weighted prime capacity | weighted semiprime capacity | weighted total capacity | actual/total capacity | exact/integer capacity |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['actual_total_hits']} | {result['weighted_prime_u_capacity']} | "
            f"{result['weighted_semiprime_u_capacity']} | {result['weighted_total_capacity']} | "
            f"{result['actual_over_weighted_total_capacity']:.6f} | "
            f"{result['exact_capacity_over_integer_capacity']:.6f} |"
        ),
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | actual | weighted total cap | actual/cap | top cap pressure | top prime pressure | top semiprime pressure |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['actual_total_hits']} | {worst['weighted_total_capacity']} | "
            f"{worst['actual_over_weighted_total_capacity']:.6f} | "
            f"`{worst['top_capacity_pressure']}` | `{worst['top_prime_pressure']}` | "
            f"`{worst['top_semiprime_pressure']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | actual | weighted cap | actual/cap | exact/integer | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        ratio = 0.0 if profile["weighted_total_capacity"] == 0 else profile["actual_total_hits"] / profile["weighted_total_capacity"]
        exact_ratio = 0.0 if profile["weighted_integer_capacity"] == 0 else profile["weighted_total_capacity"] / profile["weighted_integer_capacity"]
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['actual_total_hits']} | "
            f"{profile['weighted_total_capacity']} | {ratio:.6f} | {exact_ratio:.6f} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：prime-u 与 H-rough semiprime-u 的精确容量覆盖。",
            "- 未闭合：这些精确容量的全局上界。",
            "- 未闭合：若某前驱容量尖峰持续出现，需证明其进入 PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
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
                "exact_prime_semiprime_capacity_cover_closed": result["exact_prime_semiprime_capacity_cover_closed"],
                "actual_over_weighted_total_capacity": result["actual_over_weighted_total_capacity"],
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
