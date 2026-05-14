#!/usr/bin/env python3
"""审计 occupied-b 跨 q 碰撞的短区间几何。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_occupied_b_collision_geometry_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_occupied_b_sequence_router as occupied


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.md"

DEFAULT_P_LIST = occupied.DEFAULT_P_LIST
NEXT_TARGET = "OccupiedBShortSemiprimeModulusMultiplicityBoundOrPrimeSpikePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-occupied-b-sequence-router.json",
    "prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json",
]

normal = occupied.normal
envelope = normal.envelope
quarter = normal.quarter


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_occupied_b_collision_geometry_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_records_for_p(p: int, flags: bytearray, trial_primes: list[int]) -> list[dict[str, Any]]:
    """复用 occupied-b 路由，收集一个 P 的全部非空单 b 纤维。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    records: list[dict[str, Any]] = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous < envelope.BASE_D:
            continue
        if envelope.factor_depth_bound(p, previous) < 3:
            continue
        if not quarter.quarter_gate_closed(p, previous):
            continue
        for q in block_primes:
            if envelope.is_semiprime_regime(p, q):
                records.extend(occupied.occupied_records_for_q(p, q, primes, flags, trial_primes))
    return records


def decorate_record(p: int, record: dict[str, Any]) -> dict[str, Any]:
    """给 occupied-b 记录补充短区间模数几何字段。"""
    b = int(record["b"])
    q = int(record["q"])
    a = int(record["a"])
    n = q * a
    p2 = p * p
    n_left = p2 // b + 1
    n_right = (p2 + p - 1) // b
    # 固定 (b,q) 后 a 的允许区间长度小于一，这是跨 q 碰撞的一维化核心。
    a_left = p2 // (b * q) + 1
    a_right = (p2 + p - 1) // (b * q)
    return {
        **record,
        "n": n,
        "n_interval": [n_left, n_right],
        "n_interval_capacity": max(0, n_right - n_left + 1),
        "n_interval_width": p / b,
        "n_interval_hit_ok": n_left <= n <= n_right,
        "a_interval_for_fixed_bq": [a_left, a_right],
        "a_interval_capacity_for_fixed_bq": max(0, a_right - a_left + 1),
        "a_interval_width_for_fixed_bq": p / (b * q),
        "a_singleton_for_fixed_bq": a_left == a_right == a,
        "qa_semiprime_modulus": n,
    }


def collision_group_summary(p: int, b: int, records: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总同一 b 的碰撞组。"""
    sorted_records = sorted(records, key=lambda item: (item["n"], item["q"], item["a"]))
    q_counter = Counter(record["q"] for record in sorted_records)
    n_values = [record["n"] for record in sorted_records]
    adjacent_n_gaps = [right - left for left, right in zip(n_values, n_values[1:])]
    first = sorted_records[0]
    return {
        "p": p,
        "b": b,
        "multiplicity": len(sorted_records),
        "prime_b": bool(first["prime_b"]),
        "n_interval": first["n_interval"],
        "n_interval_capacity": first["n_interval_capacity"],
        "n_interval_width": first["n_interval_width"],
        "n_span": n_values[-1] - n_values[0] if n_values else 0,
        "min_adjacent_n_gap": min(adjacent_n_gaps) if adjacent_n_gaps else None,
        "max_adjacent_n_gap": max(adjacent_n_gaps) if adjacent_n_gaps else None,
        "q_values": [record["q"] for record in sorted_records],
        "a_values": [record["a"] for record in sorted_records],
        "n_values": n_values,
        "repeated_q_count": sum(1 for count in q_counter.values() if count > 1),
        "sample_records": sorted_records[:8],
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的 occupied-b 碰撞几何。"""
    raw_records = collect_records_for_p(p, flags, trial_primes)
    records = [decorate_record(p, record) for record in raw_records]
    by_b: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_b[int(record["b"])].append(record)

    collision_groups = [
        collision_group_summary(p, b, group)
        for b, group in by_b.items()
        if len(group) > 1
    ]
    prime_collision_groups = [group for group in collision_groups if group["prime_b"]]
    collision_fibers = sum(group["multiplicity"] for group in collision_groups)
    prime_collision_fibers = sum(group["multiplicity"] for group in prime_collision_groups)
    fixed_bq_failures = [
        record for record in records
        if not record["a_singleton_for_fixed_bq"] or record["a_interval_capacity_for_fixed_bq"] != 1
    ]
    interval_failures = [record for record in records if not record["n_interval_hit_ok"]]
    same_q_failures = [group for group in collision_groups if group["repeated_q_count"] > 0]
    top_collision = max(collision_groups, key=lambda item: item["multiplicity"], default=None)
    densest_collision = max(
        collision_groups,
        key=lambda item: safe_ratio(item["multiplicity"], item["n_interval_capacity"]) or 0.0,
        default=None,
    )
    max_fixed_bq_width = max((record["a_interval_width_for_fixed_bq"] for record in records), default=0.0)
    return {
        "p": p,
        "occupied_fibers": len(records),
        "distinct_b_values": len(by_b),
        "collision_value_count": len(collision_groups),
        "collision_fibers": collision_fibers,
        "duplicate_excess": collision_fibers - len(collision_groups),
        "prime_collision_value_count": len(prime_collision_groups),
        "prime_collision_fibers": prime_collision_fibers,
        "prime_duplicate_excess": prime_collision_fibers - len(prime_collision_groups),
        "max_b_multiplicity": max((group["multiplicity"] for group in collision_groups), default=1 if records else 0),
        "max_prime_b_multiplicity": max(
            (group["multiplicity"] for group in prime_collision_groups),
            default=1 if any(record["prime_b"] for record in records) else 0,
        ),
        "max_n_interval_capacity_on_collisions": max(
            (group["n_interval_capacity"] for group in collision_groups),
            default=0,
        ),
        "max_n_interval_width_on_collisions": max(
            (group["n_interval_width"] for group in collision_groups),
            default=0.0,
        ),
        "max_fixed_bq_a_interval_width": max_fixed_bq_width,
        "fixed_bq_single_a_failure_count": len(fixed_bq_failures),
        "short_modulus_interval_failure_count": len(interval_failures),
        "same_q_collision_failure_count": len(same_q_failures),
        "top_collision": top_collision,
        "densest_collision": densest_collision,
        "collision_groups_sample": sorted(
            collision_groups,
            key=lambda item: (-item["multiplicity"], item["b"]),
        )[:10],
    }


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 occupied-b 碰撞几何审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]

    occupied_fibers = sum(profile["occupied_fibers"] for profile in profiles)
    distinct_b_values = sum(profile["distinct_b_values"] for profile in profiles)
    collision_fibers = sum(profile["collision_fibers"] for profile in profiles)
    collision_values = sum(profile["collision_value_count"] for profile in profiles)
    prime_collision_fibers = sum(profile["prime_collision_fibers"] for profile in profiles)
    prime_collision_values = sum(profile["prime_collision_value_count"] for profile in profiles)
    top_collision = max(
        (profile["top_collision"] for profile in profiles if profile["top_collision"] is not None),
        key=lambda item: item["multiplicity"],
        default=None,
    )
    densest_collision = max(
        (profile["densest_collision"] for profile in profiles if profile["densest_collision"] is not None),
        key=lambda item: safe_ratio(item["multiplicity"], item["n_interval_capacity"]) or 0.0,
        default=None,
    )
    fixed_bq_failures = sum(profile["fixed_bq_single_a_failure_count"] for profile in profiles)
    interval_failures = sum(profile["short_modulus_interval_failure_count"] for profile in profiles)
    same_q_failures = sum(profile["same_q_collision_failure_count"] for profile in profiles)

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_occupied_b_collision_geometry_router",
        "status": "occupied_b_collisions_reduced_to_short_semiprime_modulus_intervals_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "imports_occupied_b_sequence_router": True,
        "short_semiprime_modulus_interval_identity_closed": interval_failures == 0,
        "fixed_bq_single_a_fiber_closed": fixed_bq_failures == 0,
        "same_q_collision_excluded_by_imported_injection": same_q_failures == 0,
        "global_low_multiplicity_bound_proved": False,
        "one_dimensional_selberg_prime_bound_proved": False,
        "prime_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "occupied_fibers": occupied_fibers,
        "distinct_b_values": distinct_b_values,
        "collision_value_count": collision_values,
        "collision_fibers": collision_fibers,
        "duplicate_excess": collision_fibers - collision_values,
        "prime_collision_value_count": prime_collision_values,
        "prime_collision_fibers": prime_collision_fibers,
        "prime_duplicate_excess": prime_collision_fibers - prime_collision_values,
        "global_duplicate_ratio": safe_ratio(occupied_fibers, distinct_b_values),
        "max_b_multiplicity": max((profile["max_b_multiplicity"] for profile in profiles), default=0),
        "max_prime_b_multiplicity": max((profile["max_prime_b_multiplicity"] for profile in profiles), default=0),
        "max_n_interval_capacity_on_collisions": max(
            (profile["max_n_interval_capacity_on_collisions"] for profile in profiles),
            default=0,
        ),
        "max_n_interval_width_on_collisions": max(
            (profile["max_n_interval_width_on_collisions"] for profile in profiles),
            default=0.0,
        ),
        "max_fixed_bq_a_interval_width": max(
            (profile["max_fixed_bq_a_interval_width"] for profile in profiles),
            default=0.0,
        ),
        "fixed_bq_single_a_failure_count": fixed_bq_failures,
        "short_modulus_interval_failure_count": interval_failures,
        "same_q_collision_failure_count": same_q_failures,
        "top_collision": top_collision,
        "densest_collision": densest_collision,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "同一 occupied-b 的跨 q 重复不再是二维纤维问题。"
            "固定 b 后，每条记录的半素数模数 n=q*a 都必须落入短区间 "
            "(P^2/b,(P^2+P-1)/b]；固定 (b,q) 后 a 的允许区间长度为 P/(bq)<1，"
            "所以每个 q 至多贡献一个 a。样本中该短区间恒等式、固定 (b,q) 单 a 纤维、"
            "以及同 q 碰撞排除均无失败；剩余被压成一维 q 扫描上的低重数/素性上筛，"
            "或素性尖峰 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha occupied-b 碰撞几何路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"short_semiprime_modulus_interval_identity_closed={fmt_bool(result['short_semiprime_modulus_interval_identity_closed'])}",
        f"fixed_bq_single_a_fiber_closed={fmt_bool(result['fixed_bq_single_a_fiber_closed'])}",
        f"same_q_collision_excluded_by_imported_injection={fmt_bool(result['same_q_collision_excluded_by_imported_injection'])}",
        f"global_low_multiplicity_bound_proved={fmt_bool(result['global_low_multiplicity_bound_proved'])}",
        f"one_dimensional_selberg_prime_bound_proved={fmt_bool(result['one_dimensional_selberg_prime_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 碰撞账本",
        "",
        "| occupied fibers | distinct b | collision b | collision fibers | duplicate excess | max b mult | prime collision b | prime collision fibers | max prime mult |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['occupied_fibers']} | {result['distinct_b_values']} | "
            f"{result['collision_value_count']} | {result['collision_fibers']} | "
            f"{result['duplicate_excess']} | {result['max_b_multiplicity']} | "
            f"{result['prime_collision_value_count']} | {result['prime_collision_fibers']} | "
            f"{result['max_prime_b_multiplicity']} |"
        ),
        "",
        "## 2. 短区间几何",
        "",
        "| interval failures | fixed (b,q) failures | same q failures | max n-capacity on collisions | max n-width | max a-width for fixed (b,q) |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['short_modulus_interval_failure_count']} | "
            f"{result['fixed_bq_single_a_failure_count']} | "
            f"{result['same_q_collision_failure_count']} | "
            f"{result['max_n_interval_capacity_on_collisions']} | "
            f"{fmt_float(result['max_n_interval_width_on_collisions'])} | "
            f"{fmt_float(result['max_fixed_bq_a_interval_width'])} |"
        ),
        "",
        "## 3. 典型碰撞",
        "",
        "| kind | data |",
        "| --- | --- |",
        f"| top multiplicity | `{result['top_collision']}` |",
        f"| densest interval | `{result['densest_collision']}` |",
        "",
        "## 4. 每个 P 的总结",
        "",
        "| P | collision b | dup excess | max mult | prime collision b | prime dup excess | max n-cap | max fixed-bq a-width |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['collision_value_count']} | "
            f"{profile['duplicate_excess']} | {profile['max_b_multiplicity']} | "
            f"{profile['prime_collision_value_count']} | {profile['prime_duplicate_excess']} | "
            f"{profile['max_n_interval_capacity_on_collisions']} | "
            f"{fmt_float(profile['max_fixed_bq_a_interval_width'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：同一 `b` 的每个记录等价于 `q*a` 落入短区间 `(P^2/b,(P^2+P-1)/b]`。",
            "- 已闭合：固定 `(b,q)` 时 `a` 的允许区间长度小于一，所以每个 `q` 至多一个 `a`。",
            "- 已继承：固定 `q` 的 `a->b` 注入排除同 `q` 碰撞。",
            "- 未闭合：固定 `b` 的全局低重数上界，即一维 `q` 扫描中有多少个 `q` 使唯一候选 `a_q` 为素数且相位非空。",
            "- 未闭合：该稀疏 occupied-b 序列上的素性上筛，或持续素性尖峰的 PDEC 排除。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
                "short_semiprime_modulus_interval_identity_closed": result[
                    "short_semiprime_modulus_interval_identity_closed"
                ],
                "fixed_bq_single_a_fiber_closed": result["fixed_bq_single_a_fiber_closed"],
                "max_b_multiplicity": result["max_b_multiplicity"],
                "max_prime_b_multiplicity": result["max_prime_b_multiplicity"],
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
