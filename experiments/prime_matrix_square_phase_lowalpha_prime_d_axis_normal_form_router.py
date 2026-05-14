#!/usr/bin/env python3
"""审计 quarter-gate 内 `D_-=q` 轴的 prime/semiprime normal form。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_prime_d_axis_normal_form_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_predecessor_envelope_router as envelope
import prime_matrix_square_phase_lowalpha_semiprime_quarter_gate_router as quarter


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]

NEXT_TARGET = "PrimeDTwoPrimeStripBoundAndSemiprimeSingleFiberBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json",
    "prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def is_prime_with_flags(value: int, flags: bytearray, trial_primes: list[int]) -> bool:
    """判断整数是否为素数。"""
    if value < len(flags):
        return bool(flags[value])
    if value < 2:
        return False
    for prime in trial_primes:
        if prime * prime > value:
            break
        if value % prime == 0:
            return False
    return True


def factor_pair_if_semiprime(value: int, h: float, trial_primes: list[int]) -> tuple[int, int] | None:
    """若 value 是 H-rough 半素数，返回 `(a,b)`。"""
    factors = envelope.factor_multiset(value, trial_primes)
    if len(factors) == 2 and factors[0] > h:
        return factors[0], factors[1]
    return None


def b_interval_for_qa(p: int, q: int, a: int) -> tuple[int, int, float]:
    """返回固定 `(q,a)` 后 `b` 的整数区间。"""
    p2 = p * p
    left = p2 // (q * a) + 1
    right = (p2 + p - 1) // (q * a)
    width = p / (q * a)
    return left, right, width


def audit_prime_d_q(
    p: int,
    q: int,
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计单个 prime-D 轴 `D_-=q`。"""
    p2 = p * p
    left, right = envelope.interval_bounds(p2, p, q)
    h = p / q
    prime_u_capacity = 0
    semiprime_u_capacity = 0
    semiprime_a_fiber_capacity = 0
    semiprime_width_failures = 0
    semiprime_b_interval_failures = 0
    semiprime_a_values: set[int] = set()
    top_semiprime_sample = None
    for u in range(left, right + 1):
        if is_prime_with_flags(u, flags, trial_primes) and u > h:
            prime_u_capacity += 1
            continue
        pair = factor_pair_if_semiprime(u, h, trial_primes)
        if pair is None:
            continue
        a, b = pair
        b_left, b_right, b_width = b_interval_for_qa(p, q, a)
        semiprime_u_capacity += 1
        semiprime_a_values.add(a)
        if b_right - b_left + 1 > 1 or not b_width < 1:
            semiprime_width_failures += 1
        if not (b_left <= b <= b_right):
            semiprime_b_interval_failures += 1
        semiprime_a_fiber_capacity += max(0, b_right - b_left + 1)
        sample = {
            "u": u,
            "a": a,
            "b": b,
            "b_interval": [b_left, b_right],
            "b_width": b_width,
        }
        if top_semiprime_sample is None or b_width > top_semiprime_sample["b_width"]:
            top_semiprime_sample = sample
    return {
        "q": q,
        "left_u": left,
        "right_u": right,
        "h": h,
        "u_interval_capacity": max(0, right - left + 1),
        "prime_u_capacity": prime_u_capacity,
        "semiprime_u_capacity": semiprime_u_capacity,
        "total_capacity": prime_u_capacity + semiprime_u_capacity,
        "semiprime_a_count": len(semiprime_a_values),
        "semiprime_a_fiber_capacity": semiprime_a_fiber_capacity,
        "semiprime_single_b_fiber_closed": semiprime_width_failures == 0 and semiprime_b_interval_failures == 0,
        "semiprime_width_failure_count": semiprime_width_failures,
        "semiprime_b_interval_failure_count": semiprime_b_interval_failures,
        "top_semiprime_sample": top_semiprime_sample,
    }


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    block_primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 quarter-gate low-alpha block 的 `D_-=q` normal form。"""
    if not quarter.quarter_gate_closed(p, previous_cutoff):
        return {
            "p": p,
            "previous_cutoff": previous_cutoff,
            "cutoff": cutoff,
            "alpha_left": math.log(previous_cutoff) / math.log(p),
            "skipped_ultra_low": True,
        }
    q_rows = [
        audit_prime_d_q(p, q, flags, trial_primes)
        for q in block_primes
        if envelope.is_semiprime_regime(p, q)
    ]
    prime_u_capacity = sum(row["prime_u_capacity"] for row in q_rows)
    semiprime_u_capacity = sum(row["semiprime_u_capacity"] for row in q_rows)
    total_capacity = prime_u_capacity + semiprime_u_capacity
    fiber_failures = sum(row["semiprime_width_failure_count"] + row["semiprime_b_interval_failure_count"] for row in q_rows)
    top_q = max(q_rows, key=lambda item: item["total_capacity"], default=None)
    top_semiprime_q = max(q_rows, key=lambda item: item["semiprime_u_capacity"], default=None)
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "skipped_ultra_low": False,
        "q_axis_count": len(q_rows),
        "prime_u_capacity": prime_u_capacity,
        "semiprime_u_capacity": semiprime_u_capacity,
        "total_capacity": total_capacity,
        "u_interval_capacity": sum(row["u_interval_capacity"] for row in q_rows),
        "semiprime_a_count": sum(row["semiprime_a_count"] for row in q_rows),
        "semiprime_a_fiber_capacity": sum(row["semiprime_a_fiber_capacity"] for row in q_rows),
        "semiprime_single_b_fiber_failure_count": fiber_failures,
        "prime_u_to_two_prime_strip_closed": True,
        "semiprime_single_b_fiber_closed": fiber_failures == 0,
        "top_q_capacity": top_q,
        "top_semiprime_q": top_semiprime_q,
        "q_rows": q_rows,
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 prime-D normal form。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, block_primes, flags, trial_primes))
    active_rows = [row for row in rows if not row.get("skipped_ultra_low")]
    skipped_rows = [row for row in rows if row.get("skipped_ultra_low")]
    worst = max(active_rows, key=lambda item: item["total_capacity"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(rows),
        "quarter_gate_row_count": len(active_rows),
        "ultra_low_skipped_row_count": len(skipped_rows),
        "prime_u_capacity": sum(row["prime_u_capacity"] for row in active_rows),
        "semiprime_u_capacity": sum(row["semiprime_u_capacity"] for row in active_rows),
        "total_capacity": sum(row["total_capacity"] for row in active_rows),
        "u_interval_capacity": sum(row["u_interval_capacity"] for row in active_rows),
        "semiprime_a_count": sum(row["semiprime_a_count"] for row in active_rows),
        "semiprime_a_fiber_capacity": sum(row["semiprime_a_fiber_capacity"] for row in active_rows),
        "semiprime_single_b_fiber_failure_count": sum(
            row["semiprime_single_b_fiber_failure_count"] for row in active_rows
        ),
        "worst_quarter_gate_block": worst,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_prime_d_axis_normal_form_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 prime-D normal form 审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]
    rows = [row for profile in profiles for row in profile["rows"] if not row.get("skipped_ultra_low")]
    worst = max(rows, key=lambda item: item["total_capacity"], default=None)
    total_capacity = sum(profile["total_capacity"] for profile in profiles)
    prime_capacity = sum(profile["prime_u_capacity"] for profile in profiles)
    semiprime_capacity = sum(profile["semiprime_u_capacity"] for profile in profiles)
    fiber_failures = sum(profile["semiprime_single_b_fiber_failure_count"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_prime_d_axis_normal_form_router",
        "status": "quarter_gate_prime_d_axis_reduced_to_two_prime_strip_and_single_b_fibers_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "prime_d_axis_normal_form_closed": fiber_failures == 0,
        "prime_u_to_two_prime_strip_closed": True,
        "semiprime_single_b_fiber_closed": fiber_failures == 0,
        "semiprime_single_b_fiber_failure_count": fiber_failures,
        "prime_d_two_prime_strip_bound_proved": False,
        "semiprime_single_fiber_global_bound_proved": False,
        "ultra_low_composite_tail_bound_proved": False,
        "row_column_unconditional_closed": False,
        "quarter_gate_row_count": sum(profile["quarter_gate_row_count"] for profile in profiles),
        "ultra_low_skipped_row_count": sum(profile["ultra_low_skipped_row_count"] for profile in profiles),
        "prime_u_capacity": prime_capacity,
        "semiprime_u_capacity": semiprime_capacity,
        "total_capacity": total_capacity,
        "prime_capacity_share": None if total_capacity == 0 else prime_capacity / total_capacity,
        "semiprime_capacity_share": None if total_capacity == 0 else semiprime_capacity / total_capacity,
        "u_interval_capacity": sum(profile["u_interval_capacity"] for profile in profiles),
        "semiprime_a_count": sum(profile["semiprime_a_count"] for profile in profiles),
        "semiprime_a_fiber_capacity": sum(profile["semiprime_a_fiber_capacity"] for profile in profiles),
        "profiles": profiles,
        "worst_quarter_gate_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "在 `z>=P^(1/4)` 的 quarter-gate 内，semiprime predecessor 已退化为 `D_-=q`。"
            "于是 prime-u 分支就是双素数窄带 `P^2<q*u<=P^2+P-1`；"
            "semiprime-u 分支写成 `u=a*b` 且 `a>P/q`，固定 `(q,a)` 后 "
            "`b` 落在长度 `P/(q*a)<1` 的整数区间，因此是单点纤维。"
            "剩余不再是一般 Buchstab 分布，而是双素数窄带上界、半素数单纤维全局求和，"
            "以及 `z<P^(1/4)` ultra-low 复合尾项。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha prime-D 轴 normal form",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prime_d_axis_normal_form_closed={fmt_bool(result['prime_d_axis_normal_form_closed'])}",
        f"prime_u_to_two_prime_strip_closed={fmt_bool(result['prime_u_to_two_prime_strip_closed'])}",
        f"semiprime_single_b_fiber_closed={fmt_bool(result['semiprime_single_b_fiber_closed'])}",
        f"prime_d_two_prime_strip_bound_proved={fmt_bool(result['prime_d_two_prime_strip_bound_proved'])}",
        f"semiprime_single_fiber_global_bound_proved={fmt_bool(result['semiprime_single_fiber_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局分支容量",
        "",
        "| quarter rows | ultra-low skipped | prime-u cap | semiprime-u cap | total cap | prime share | semiprime share |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['quarter_gate_row_count']} | {result['ultra_low_skipped_row_count']} | "
            f"{result['prime_u_capacity']} | {result['semiprime_u_capacity']} | "
            f"{result['total_capacity']} | {result['prime_capacity_share']:.6f} | "
            f"{result['semiprime_capacity_share']:.6f} |"
        ),
        "",
        "## 2. 最坏 quarter-gate 块",
        "",
        "| P | block | prime-u | semiprime-u | total | top q | top semiprime q |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- |",
    ]
    worst = result["worst_quarter_gate_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['prime_u_capacity']} | {worst['semiprime_u_capacity']} | "
            f"{worst['total_capacity']} | `{worst['top_q_capacity']}` | "
            f"`{worst['top_semiprime_q']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | quarter rows | ultra-low skipped | prime-u | semiprime-u | total | semiprime a-fibers | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_quarter_gate_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['quarter_gate_row_count']} | {profile['ultra_low_skipped_row_count']} | "
            f"{profile['prime_u_capacity']} | {profile['semiprime_u_capacity']} | {profile['total_capacity']} | "
            f"{profile['semiprime_a_fiber_capacity']} | `({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：quarter-gate 内 `D_-=q` 轴的 normal form。",
            "- 已闭合：prime-u 分支等价于双素数窄带点 `P^2<q*u<=P^2+P-1`。",
            "- 已闭合：semiprime-u 分支固定 `(q,a)` 后 `b` 的整数区间长度小于一。",
            "- 未闭合：双素数窄带的全局上筛常数与相位缺陷排除。",
            "- 未闭合：半素数单纤维在所有 `(q,a)` 上的全局求和上界。",
            "- 未闭合：`z<P^(1/4)` ultra-low 复合尾项。",
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
                "prime_d_axis_normal_form_closed": result["prime_d_axis_normal_form_closed"],
                "prime_u_capacity": result["prime_u_capacity"],
                "semiprime_u_capacity": result["semiprime_u_capacity"],
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
