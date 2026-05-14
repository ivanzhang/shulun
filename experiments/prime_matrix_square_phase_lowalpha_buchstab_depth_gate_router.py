#!/usr/bin/env python3
"""审计前驱 Buchstab 区间的因子深度门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_buchstab_depth_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

NEXT_TARGET = "SemiprimePredecessorIntervalConstantOrDeepBuchstabTailPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-buchstab-constant-spike-router.json",
    "prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json",
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


def interval_integer_capacity(p2: int, p: int, d_minus: int) -> int:
    """返回 `P^2/D < u <= (P^2+P-1)/D` 的整数容量。"""
    return max(0, (p2 + p - 1) // d_minus - p2 // d_minus)


def block_omega(d_minus: int, block_primes: list[int]) -> int:
    """计算 `D_-` 中可作为原始块素数 q 的不同因子数。"""
    return sum(1 for q in block_primes if d_minus % q == 0)


def u_depth_bound(p: int, d_minus: int) -> int:
    """固定前驱后，H-rough 的 u 的最大素因子重数上界。"""
    h = p / d_minus
    upper = (p * p + p - 1) / d_minus
    if h <= 1:
        return 99
    depth = 0
    power = 1.0
    while power < upper:
        depth += 1
        power *= h
    return max(0, depth - 1)


def depth_regime(depth: int) -> str:
    """按深度上界命名路线。"""
    if depth <= 1:
        return "prime"
    if depth <= 2:
        return "semiprime"
    return "deep"


def register_regime(regimes: dict[str, dict[str, float]], regime: str, hits: int, weighted: int) -> None:
    """登记 regime 账本。"""
    row = regimes.setdefault(regime, {"hits": 0.0, "weighted_capacity": 0.0, "predecessors": 0.0})
    row["hits"] += hits
    row["weighted_capacity"] += weighted
    row["predecessors"] += 1


def finalize_regimes(regimes: dict[str, dict[str, float]]) -> dict[str, dict[str, float]]:
    """给 regime 补充密度。"""
    result: dict[str, dict[str, float]] = {}
    for key, row in sorted(regimes.items()):
        weighted = row["weighted_capacity"]
        result[key] = {
            "hits": row["hits"],
            "weighted_capacity": weighted,
            "predecessors": row["predecessors"],
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
    """审计一个 low-alpha block 的 u 深度门。"""
    p2 = p * p
    predecessor_hits: dict[int, int] = {}
    predecessor_capacity: dict[int, int] = {}
    predecessor_omega: dict[int, int] = {}
    actual_depth_counts: dict[str, int] = {}
    depth_bound_failures = 0
    for q in block_primes:
        left = p2 // q + 1
        right = (p2 + p - 1) // q
        for m in range(left, right + 1):
            k = q * m - p2
            if not (1 <= k < p and allowed[k]):
                continue
            d_minus, _u, u_factors = crossing_from_factors(p, q, factor_multiset(m, trial_primes))
            predecessor_hits[d_minus] = predecessor_hits.get(d_minus, 0) + 1
            if d_minus not in predecessor_capacity:
                predecessor_capacity[d_minus] = interval_integer_capacity(p2, p, d_minus)
                predecessor_omega[d_minus] = block_omega(d_minus, block_primes)
            actual_depth = len(u_factors)
            actual_depth_counts[str(actual_depth)] = actual_depth_counts.get(str(actual_depth), 0) + 1
            if actual_depth > u_depth_bound(p, d_minus):
                depth_bound_failures += 1
    regimes: dict[str, dict[str, float]] = {}
    max_depth_bound = 0
    top_deep_predecessor = None
    top_semiprime_predecessor = None
    for d_minus, hits in predecessor_hits.items():
        depth = u_depth_bound(p, d_minus)
        max_depth_bound = max(max_depth_bound, depth)
        capacity = predecessor_capacity[d_minus]
        omega = predecessor_omega[d_minus]
        weighted = capacity * omega
        regime = depth_regime(depth)
        register_regime(regimes, regime, hits, weighted)
        row = {
            "d_minus": d_minus,
            "hits": hits,
            "capacity": capacity,
            "omega_block": omega,
            "weighted_capacity": weighted,
            "depth_bound": depth,
            "h": p / d_minus,
            "weighted_density": 0.0 if weighted == 0 else hits / weighted,
        }
        if regime == "deep" and (top_deep_predecessor is None or hits > top_deep_predecessor["hits"]):
            top_deep_predecessor = row
        if regime == "semiprime" and (top_semiprime_predecessor is None or hits > top_semiprime_predecessor["hits"]):
            top_semiprime_predecessor = row
    regime_rows = finalize_regimes(regimes)
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "cofactor_hits": sum(predecessor_hits.values()),
        "active_predecessor_count": len(predecessor_hits),
        "depth_bound_failure_count": depth_bound_failures,
        "actual_u_depth_counts": actual_depth_counts,
        "max_depth_bound": max_depth_bound,
        "regime_rows": regime_rows,
        "top_semiprime_predecessor": top_semiprime_predecessor,
        "top_deep_predecessor": top_deep_predecessor,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 u 深度门。"""
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
        "depth_bound_failure_count": sum(row["depth_bound_failure_count"] for row in low_rows),
        "worst_lowalpha_block": worst,
        "rows": low_rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_buchstab_depth_gate_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def merge_regimes(profiles: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    """合并所有 regime 账本。"""
    merged: dict[str, dict[str, float]] = {}
    for profile in profiles:
        for row in profile["rows"]:
            for regime, values in row["regime_rows"].items():
                target = merged.setdefault(regime, {"hits": 0.0, "weighted_capacity": 0.0, "predecessors": 0.0})
                target["hits"] += values["hits"]
                target["weighted_capacity"] += values["weighted_capacity"]
                target["predecessors"] += values["predecessors"]
    return finalize_regimes(merged)


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行深度门审计。"""
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
    failures = sum(profile["depth_bound_failure_count"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_buchstab_depth_gate_router",
        "status": "buchstab_constant_split_into_semiprime_and_deep_tail_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "u_depth_bound_checked": failures == 0,
        "depth_bound_failure_count": failures,
        "semiprime_gate_closed": True,
        "semiprime_constant_proved": False,
        "deep_buchstab_tail_bound_proved": False,
        "local_density_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "profiles": profiles,
        "global_regime_rows": merge_regimes(profiles),
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Buchstab 常数硬点已按前驱 `D_-` 的 u-因子深度分裂。"
            "若 `D_-<sqrt(P)`，则 `H=P/D_-` 满足 `H^3>P^2/D_-`，"
            "所以 H-rough 的 `u` 至多半素数；其余 `D_->=sqrt(P)` 才是真正 deep Buchstab tail。"
            "本步闭合深度门，不证明半素数常数或 deep tail 上界。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha Buchstab 深度门",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"u_depth_bound_checked={fmt_bool(result['u_depth_bound_checked'])}",
        f"semiprime_gate_closed={fmt_bool(result['semiprime_gate_closed'])}",
        f"semiprime_constant_proved={fmt_bool(result['semiprime_constant_proved'])}",
        f"deep_buchstab_tail_bound_proved={fmt_bool(result['deep_buchstab_tail_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局 regime",
        "",
        "| regime | hits | weighted capacity | predecessors | weighted density |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for regime, values in result["global_regime_rows"].items():
        lines.append(
            f"| `{regime}` | {values['hits']:.0f} | {values['weighted_capacity']:.0f} | "
            f"{values['predecessors']:.0f} | {values['weighted_density']:.6f} |"
        )
    worst = result["worst_lowalpha_block"]
    lines.extend(
        [
            "",
            "## 2. 最坏 low-alpha 块",
            "",
            "| P | block | hits | actual u-depths | regime rows | top semiprime D_- | top deep D_- |",
            "| ---: | --- | ---: | --- | --- | --- | --- |",
        ]
    )
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['cofactor_hits']} | `{worst['actual_u_depth_counts']}` | "
            f"`{worst['regime_rows']}` | `{worst['top_semiprime_predecessor']}` | "
            f"`{worst['top_deep_predecessor']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low blocks | total hits | worst block |",
            "| ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['total_hits']} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：`u` 的 H-rough 因子深度上界。",
            "- 已闭合：`D_-<sqrt(P)` 分支压为 semiprime/prime interval 常数问题。",
            "- 未闭合：semiprime interval 常数上界。",
            "- 未闭合：`D_->=sqrt(P)` 的 deep Buchstab tail 上界或 PDEC。",
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
                "u_depth_bound_checked": result["u_depth_bound_checked"],
                "global_regime_rows": result["global_regime_rows"],
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
