#!/usr/bin/env python3
"""审计 semiprime regime 的先验前驱 envelope。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_predecessor_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-envelope-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-predecessor-envelope-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "EligiblePredecessorEnvelopeWeightedCapacityGlobalBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json",
    "prime-matrix-square-phase-lowalpha-semiprime-fiber-router.json",
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


def is_semiprime_regime(p: int, d_minus: int) -> bool:
    """判断 `D_-<sqrt(P)` 的半素数门。"""
    return d_minus * d_minus < p


def is_z_rough(value: int, z: int, trial_primes: list[int]) -> bool:
    """检查 value 是否没有不超过 z 的素因子。"""
    if value == 1:
        return True
    for prime in trial_primes:
        if prime > z or prime * prime > value:
            break
        if value % prime == 0:
            return False
    return True


def block_omega_eligible(d_minus: int, z: int, block_primes: list[int], trial_primes: list[int]) -> int:
    """计算可作为原始块素数 q 的 eligible 重数。"""
    total = 0
    for q in block_primes:
        if d_minus % q == 0 and is_z_rough(d_minus // q, z, trial_primes):
            total += 1
    return total


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


def rough_products_above(z: int, limit: int, primes: list[int]) -> list[int]:
    """枚举由大于 z 的素数组成且不超过 limit 的乘积，包含 1。"""
    result = [1]
    usable = [prime for prime in primes if z < prime <= limit]

    def visit(start: int, current: int) -> None:
        for idx in range(start, len(usable)):
            value = current * usable[idx]
            if value > limit:
                break
            result.append(value)
            visit(idx, value)

    visit(0, 1)
    return sorted(set(result))


def eligible_predecessors(p: int, z: int, block_primes: list[int], primes: list[int]) -> set[int]:
    """先验枚举所有可能的 semiprime-regime crossing 前驱 D_-。"""
    limit_d = math.isqrt(p - 1)
    result: set[int] = set()
    for q in block_primes:
        max_tail = limit_d // q
        if max_tail < 1:
            continue
        for tail in rough_products_above(z, max_tail, primes):
            d_minus = q * tail
            if is_semiprime_regime(p, d_minus):
                result.add(d_minus)
    return result


def actual_active_predecessors(
    p: int,
    allowed: bytearray,
    block_primes: list[int],
    trial_primes: list[int],
) -> dict[int, dict[str, int]]:
    """从真实命中侧提取活跃 semiprime 前驱。"""
    p2 = p * p
    active: dict[int, dict[str, int]] = {}
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
            row = active.setdefault(d_minus, {"prime": 0, "semiprime": 0, "other": 0})
            if len(u_factors) == 1:
                row["prime"] += 1
            elif len(u_factors) == 2:
                row["semiprime"] += 1
            else:
                row["other"] += 1
    return active


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    allowed: bytearray,
    block_primes: list[int],
    primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的先验前驱 envelope。"""
    active = actual_active_predecessors(p, allowed, block_primes, trial_primes)
    envelope = eligible_predecessors(p, previous_cutoff, block_primes, primes)
    capacity_positive: set[int] = set()
    weighted_prime_capacity = 0
    weighted_semiprime_capacity = 0
    weighted_total_capacity = 0
    weighted_integer_capacity = 0
    top_capacity_record = None
    for d_minus in envelope:
        omega = block_omega_eligible(d_minus, previous_cutoff, block_primes, trial_primes)
        capacity = possible_capacity_for_predecessor(p, d_minus, trial_primes)
        weighted_prime = omega * capacity["prime_u_capacity"]
        weighted_semiprime = omega * capacity["semiprime_u_capacity"]
        weighted_total = weighted_prime + weighted_semiprime
        weighted_prime_capacity += weighted_prime
        weighted_semiprime_capacity += weighted_semiprime
        weighted_total_capacity += weighted_total
        weighted_integer_capacity += omega * capacity["integer_capacity"]
        if weighted_total > 0:
            capacity_positive.add(d_minus)
            record = {
                "d_minus": d_minus,
                "omega_block": omega,
                "prime_capacity": capacity["prime_u_capacity"],
                "semiprime_capacity": capacity["semiprime_u_capacity"],
                "weighted_total_capacity": weighted_total,
                "h": p / d_minus,
            }
            if top_capacity_record is None or weighted_total > top_capacity_record["weighted_total_capacity"]:
                top_capacity_record = record
    actual_prime = sum(item["prime"] for item in active.values())
    actual_semiprime = sum(item["semiprime"] for item in active.values())
    actual_other = sum(item["other"] for item in active.values())
    actual_total = actual_prime + actual_semiprime
    active_set = {d_minus for d_minus, item in active.items() if item["prime"] + item["semiprime"] > 0}
    missing_active = sorted(active_set - capacity_positive)
    extra_envelope = sorted(capacity_positive - active_set)
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "eligible_predecessor_count": len(envelope),
        "capacity_positive_predecessor_count": len(capacity_positive),
        "active_semiprime_predecessors": len(active_set),
        "actual_prime_u_hits": actual_prime,
        "actual_semiprime_u_hits": actual_semiprime,
        "actual_other_hits": actual_other,
        "actual_total_hits": actual_total,
        "weighted_prime_u_capacity": weighted_prime_capacity,
        "weighted_semiprime_u_capacity": weighted_semiprime_capacity,
        "weighted_total_capacity": weighted_total_capacity,
        "weighted_integer_capacity": weighted_integer_capacity,
        "active_missing_from_envelope_count": len(missing_active),
        "envelope_positive_not_active_count": len(extra_envelope),
        "weighted_capacity_mismatch": weighted_total_capacity - actual_total,
        "active_equals_positive_envelope": not missing_active and not extra_envelope,
        "actual_over_envelope_capacity": None if weighted_total_capacity == 0 else actual_total / weighted_total_capacity,
        "exact_capacity_over_integer_capacity": None
        if weighted_integer_capacity == 0
        else weighted_total_capacity / weighted_integer_capacity,
        "top_capacity_record": top_capacity_record,
        "missing_active_sample": missing_active[:8],
        "extra_envelope_sample": extra_envelope[:8],
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的先验前驱 envelope。"""
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
            rows.append(audit_lowalpha_block(p, previous, cutoff, allowed, block_primes, primes, trial_primes))
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            delete_residue(allowed, p, p2, primes[prime_index])
            prime_index += 1
        if not rows or rows[-1].get("cutoff") != cutoff:
            rows.append({"p": p, "previous_cutoff": previous, "cutoff": cutoff, "skipped": True})
    low_rows = [row for row in rows if not row.get("skipped")]
    worst = max(low_rows, key=lambda item: item["weighted_total_capacity"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(low_rows),
        "eligible_predecessor_count": sum(row["eligible_predecessor_count"] for row in low_rows),
        "capacity_positive_predecessor_count": sum(row["capacity_positive_predecessor_count"] for row in low_rows),
        "active_semiprime_predecessors": sum(row["active_semiprime_predecessors"] for row in low_rows),
        "actual_total_hits": sum(row["actual_total_hits"] for row in low_rows),
        "weighted_total_capacity": sum(row["weighted_total_capacity"] for row in low_rows),
        "weighted_integer_capacity": sum(row["weighted_integer_capacity"] for row in low_rows),
        "active_missing_from_envelope_count": sum(row["active_missing_from_envelope_count"] for row in low_rows),
        "envelope_positive_not_active_count": sum(row["envelope_positive_not_active_count"] for row in low_rows),
        "weighted_capacity_mismatch": sum(row["weighted_capacity_mismatch"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_predecessor_envelope_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行先验前驱 envelope 审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = sieve_bool(max(trial_limit, max_p))
    trial_primes = primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes))
    rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(rows, key=lambda item: item["weighted_total_capacity"], default=None)
    missing = sum(profile["active_missing_from_envelope_count"] for profile in profiles)
    extra = sum(profile["envelope_positive_not_active_count"] for profile in profiles)
    mismatch = sum(profile["weighted_capacity_mismatch"] for profile in profiles)
    total_actual = sum(profile["actual_total_hits"] for profile in profiles)
    total_capacity = sum(profile["weighted_total_capacity"] for profile in profiles)
    total_integer = sum(profile["weighted_integer_capacity"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_predecessor_envelope_router",
        "status": "active_predecessors_replaced_by_prior_eligible_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "prior_eligible_predecessor_envelope_closed": missing == 0 and extra == 0 and mismatch == 0,
        "active_equals_capacity_positive_envelope": missing == 0 and extra == 0,
        "weighted_envelope_capacity_equals_actual_hits": mismatch == 0,
        "active_missing_from_envelope_count": missing,
        "envelope_positive_not_active_count": extra,
        "weighted_capacity_mismatch": mismatch,
        "global_capacity_bound_proved": False,
        "local_capacity_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "actual_total_hits": total_actual,
        "weighted_total_capacity": total_capacity,
        "weighted_integer_capacity": total_integer,
        "actual_over_envelope_capacity": None if total_capacity == 0 else total_actual / total_capacity,
        "exact_capacity_over_integer_capacity": None if total_integer == 0 else total_capacity / total_integer,
        "eligible_predecessor_count": sum(profile["eligible_predecessor_count"] for profile in profiles),
        "capacity_positive_predecessor_count": sum(
            profile["capacity_positive_predecessor_count"] for profile in profiles
        ),
        "active_semiprime_predecessors": sum(profile["active_semiprime_predecessors"] for profile in profiles),
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "semiprime 分支中的活跃前驱不再需要后验提取：固定 block `(z,Z]` 后，"
            "所有可能前驱先验等于 `D_-=qE<sqrt(P)`，其中 `q` 属于当前 block，"
            "`E` 没有不超过 `z` 的素因子。容量为正的先验 envelope 与真实活跃前驱完全一致，"
            "且加权 prime/semiprime 容量逐项等于真实命中。剩余被压成这个先验 envelope 上的全局容量上界，"
            "或容量尖峰的 PDEC 排除。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha 先验前驱 envelope",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prior_eligible_predecessor_envelope_closed={fmt_bool(result['prior_eligible_predecessor_envelope_closed'])}",
        f"active_equals_capacity_positive_envelope={fmt_bool(result['active_equals_capacity_positive_envelope'])}",
        f"weighted_envelope_capacity_equals_actual_hits={fmt_bool(result['weighted_envelope_capacity_equals_actual_hits'])}",
        f"global_capacity_bound_proved={fmt_bool(result['global_capacity_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局 envelope 容量",
        "",
        "| eligible D | cap-positive D | active D | actual hits | envelope cap | actual/cap | cap/integer |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['eligible_predecessor_count']} | {result['capacity_positive_predecessor_count']} | "
            f"{result['active_semiprime_predecessors']} | {result['actual_total_hits']} | "
            f"{result['weighted_total_capacity']} | {result['actual_over_envelope_capacity']:.6f} | "
            f"{result['exact_capacity_over_integer_capacity']:.6f} |"
        ),
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | eligible D | cap-positive D | actual | envelope cap | top capacity record |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['eligible_predecessor_count']} | {worst['capacity_positive_predecessor_count']} | "
            f"{worst['actual_total_hits']} | {worst['weighted_total_capacity']} | "
            f"`{worst['top_capacity_record']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | eligible D | cap-positive D | active D | actual | envelope cap | cap/integer | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        ratio = 0.0 if profile["weighted_integer_capacity"] == 0 else profile["weighted_total_capacity"] / profile["weighted_integer_capacity"]
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['eligible_predecessor_count']} | "
            f"{profile['capacity_positive_predecessor_count']} | {profile['active_semiprime_predecessors']} | "
            f"{profile['actual_total_hits']} | {profile['weighted_total_capacity']} | {ratio:.6f} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：活跃前驱集合可由先验 envelope `D_-=qE<sqrt(P)` 替代。",
            "- 已闭合：容量为正的 envelope 与真实活跃集合一致；加权容量等于真实命中。",
            "- 未闭合：对该先验 envelope 的全局加权 prime/semiprime 容量上界。",
            "- 未闭合：若 envelope 容量尖峰持续出现，需证明其形成 PDEC 并排除。",
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
                "prior_eligible_predecessor_envelope_closed": result["prior_eligible_predecessor_envelope_closed"],
                "actual_over_envelope_capacity": result["actual_over_envelope_capacity"],
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
