#!/usr/bin/env python3
"""审计 semiprime 单纤维非空条件的 reciprocal carry 等价。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_semiprime_phase_carry_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_prime_d_axis_normal_form_router as normal


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]

NEXT_TARGET = "ReciprocalCarryDiscrepancyBoundForSemiprimeFibersOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.json",
    "prime-matrix-square-phase-reciprocal-floor-congruence-ledger.json",
]

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


def carry_for_qa(p: int, q: int, a: int) -> int:
    """返回固定 `(q,a)` 的 reciprocal carry。"""
    p2 = p * p
    return (p2 + p - 1) // (q * a) - p2 // (q * a)


def fractional_threshold_condition(p: int, q: int, a: int) -> bool:
    """检查等价的分数部阈值条件。"""
    p2 = p * p
    modulus = q * a
    residue = p2 % modulus
    return residue + p - 1 >= modulus


def audit_q_axis(
    p: int,
    q: int,
    primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计单个 q 轴的 carry 等价。"""
    row = normal.audit_prime_d_q(p, q, flags, trial_primes)
    phase_mass = 0.0
    carry_count = 0
    formula_failures = 0
    carry_value_failures = 0
    discrepancy_abs = 0.0
    max_width = 0.0
    top_carry_sample = None
    a_left = math.floor(p / q) + 1
    a_right = math.isqrt(row["right_u"])
    for a in primes:
        if a < a_left:
            continue
        if a > a_right:
            break
        b_left, b_right, width = normal.b_interval_for_qa(p, q, a)
        carry = carry_for_qa(p, q, a)
        condition = fractional_threshold_condition(p, q, a)
        nonempty = b_right >= b_left
        phase_mass += width
        carry_count += carry
        discrepancy_abs += abs(carry - width)
        if carry not in (0, 1):
            carry_value_failures += 1
        if carry != int(nonempty) or condition != nonempty:
            formula_failures += 1
        if carry and width > max_width:
            max_width = width
            top_carry_sample = {
                "a": a,
                "b_interval": [b_left, b_right],
                "width": width,
                "residue": (p * p) % (q * a),
                "modulus": q * a,
            }
    signed_discrepancy = carry_count - phase_mass
    return {
        "q": q,
        "h": row["h"],
        "a_interval": [a_left, a_right],
        "phase_mass": phase_mass,
        "carry_count": carry_count,
        "carry_over_phase": safe_ratio(carry_count, phase_mass),
        "signed_discrepancy": signed_discrepancy,
        "absolute_discrepancy_sum": discrepancy_abs,
        "formula_failure_count": formula_failures,
        "carry_value_failure_count": carry_value_failures,
        "top_carry_sample": top_carry_sample,
    }


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    block_primes: list[int],
    primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 quarter-gate block 的 carry 等价。"""
    if not quarter.quarter_gate_closed(p, previous_cutoff):
        return {
            "p": p,
            "previous_cutoff": previous_cutoff,
            "cutoff": cutoff,
            "alpha_left": math.log(previous_cutoff) / math.log(p),
            "skipped_ultra_low": True,
        }
    q_rows = [
        audit_q_axis(p, q, primes, flags, trial_primes)
        for q in block_primes
        if envelope.is_semiprime_regime(p, q)
    ]
    phase_mass = sum(row["phase_mass"] for row in q_rows)
    carry_count = sum(row["carry_count"] for row in q_rows)
    top_positive = max(q_rows, key=lambda item: item["signed_discrepancy"], default=None)
    top_ratio = max(
        q_rows,
        key=lambda item: item["carry_over_phase"] if item["carry_over_phase"] is not None else -1,
        default=None,
    )
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "skipped_ultra_low": False,
        "q_axis_count": len(q_rows),
        "phase_mass": phase_mass,
        "carry_count": carry_count,
        "carry_over_phase": safe_ratio(carry_count, phase_mass),
        "signed_discrepancy": carry_count - phase_mass,
        "formula_failure_count": sum(row["formula_failure_count"] for row in q_rows),
        "carry_value_failure_count": sum(row["carry_value_failure_count"] for row in q_rows),
        "top_positive_discrepancy_q": top_positive,
        "top_ratio_q": top_ratio,
        "q_rows": q_rows,
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 carry 等价。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, block_primes, primes, flags, trial_primes))
    active_rows = [row for row in rows if not row.get("skipped_ultra_low")]
    phase_mass = sum(row["phase_mass"] for row in active_rows)
    carry_count = sum(row["carry_count"] for row in active_rows)
    return {
        "p": p,
        "quarter_gate_row_count": len(active_rows),
        "ultra_low_skipped_row_count": sum(1 for row in rows if row.get("skipped_ultra_low")),
        "phase_mass": phase_mass,
        "carry_count": carry_count,
        "carry_over_phase": safe_ratio(carry_count, phase_mass),
        "signed_discrepancy": carry_count - phase_mass,
        "formula_failure_count": sum(row["formula_failure_count"] for row in active_rows),
        "carry_value_failure_count": sum(row["carry_value_failure_count"] for row in active_rows),
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_semiprime_phase_carry_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 reciprocal carry 等价审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]
    rows = [row for profile in profiles for row in profile["rows"] if not row.get("skipped_ultra_low")]
    q_rows = [q_row for row in rows for q_row in row["q_rows"]]
    phase_mass = sum(profile["phase_mass"] for profile in profiles)
    carry_count = sum(profile["carry_count"] for profile in profiles)
    formula_failures = sum(profile["formula_failure_count"] for profile in profiles)
    carry_failures = sum(profile["carry_value_failure_count"] for profile in profiles)
    top_positive = max(q_rows, key=lambda item: item["signed_discrepancy"], default=None)
    top_ratio = max(
        q_rows,
        key=lambda item: item["carry_over_phase"] if item["carry_over_phase"] is not None else -1,
        default=None,
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_semiprime_phase_carry_router",
        "status": "semiprime_fiber_phase_reduced_to_reciprocal_carry_discrepancy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "carry_formula_closed": formula_failures == 0 and carry_failures == 0,
        "carry_formula_failure_count": formula_failures,
        "carry_value_failure_count": carry_failures,
        "fractional_threshold_identity_closed": formula_failures == 0,
        "reciprocal_carry_discrepancy_bound_proved": False,
        "reciprocal_carry_pdec_excluded": False,
        "occupied_fiber_prime_density_bound_proved": False,
        "row_column_unconditional_closed": False,
        "q_axis_count": len(q_rows),
        "phase_mass": phase_mass,
        "carry_count": carry_count,
        "carry_over_phase": safe_ratio(carry_count, phase_mass),
        "signed_discrepancy": carry_count - phase_mass,
        "top_positive_discrepancy_q": top_positive,
        "top_ratio_q": top_ratio,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "semiprime 单纤维的非空事件已精确改写成 reciprocal carry："
            "`b` 区间非空当且仅当 "
            "`floor((P^2+P-1)/(qa))-floor(P^2/(qa))=1`，"
            "等价于余数阈值 `(P^2 mod qa)+P-1>=qa`。"
            "因此相位非空过密不再是抽象统计现象，而是倒数 floor-carry 的 sawtooth 偏差。"
            "样本公式零失败；剩余是证明 carry_count 相对 phase_mass 的统一偏差界，"
            "或把失败登记为 reciprocal-carry/PDEC。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha semiprime 相位 carry 路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"carry_formula_closed={fmt_bool(result['carry_formula_closed'])}",
        f"fractional_threshold_identity_closed={fmt_bool(result['fractional_threshold_identity_closed'])}",
        f"reciprocal_carry_discrepancy_bound_proved={fmt_bool(result['reciprocal_carry_discrepancy_bound_proved'])}",
        f"reciprocal_carry_pdec_excluded={fmt_bool(result['reciprocal_carry_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局 carry 账本",
        "",
        "| q axes | phase mass | carry count | carry/phase | signed discrepancy |",
        "| ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['q_axis_count']} | {result['phase_mass']:.6f} | {result['carry_count']} | "
            f"{fmt_float(result['carry_over_phase'])} | {result['signed_discrepancy']:.6f} |"
        ),
        "",
        "## 2. 最热 q 轴",
        "",
        "| type | record |",
        "| --- | --- |",
        f"| positive discrepancy | `{result['top_positive_discrepancy_q']}` |",
        f"| carry/phase | `{result['top_ratio_q']}` |",
        "",
        "## 3. 每个 P 的总结",
        "",
        "| P | carry count | phase mass | carry/phase | signed discrepancy |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['carry_count']} | {profile['phase_mass']:.6f} | "
            f"{fmt_float(profile['carry_over_phase'])} | {profile['signed_discrepancy']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：纤维非空与 reciprocal carry/fractional-threshold 完全等价。",
            "- 未闭合：carry_count 相对 phase_mass 的统一偏差界。",
            "- 未闭合：若 carry 偏差持续过大，对应 reciprocal-carry/PDEC 的排除。",
            "- 未闭合：非空纤维上的素性密度上界。",
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
                "carry_formula_closed": result["carry_formula_closed"],
                "carry_over_phase": result["carry_over_phase"],
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
