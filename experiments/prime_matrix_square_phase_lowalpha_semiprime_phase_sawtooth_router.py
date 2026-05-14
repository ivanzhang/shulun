#!/usr/bin/env python3
"""审计 semiprime carry 偏差的 sawtooth 恒等式。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_semiprime_phase_sawtooth_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]

NEXT_TARGET = "ReciprocalSawtoothDiscrepancyBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.json",
    "prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md",
]

envelope = normal.envelope
quarter = normal.quarter


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def frac(numerator: int, denominator: int) -> float:
    """返回有理数分数部。"""
    return (numerator % denominator) / denominator


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def audit_q_axis(
    p: int,
    q: int,
    primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计固定 q 轴的 sawtooth 恒等式。"""
    row = normal.audit_prime_d_q(p, q, flags, trial_primes)
    p2 = p * p
    carry_count = 0
    phase_p = 0.0
    phase_p_minus_1 = 0.0
    saw_exact_sum = 0.0
    saw_p_sum = 0.0
    identity_failures = 0
    top_abs_sample = None
    a_left = math.floor(p / q) + 1
    a_right = math.isqrt(row["right_u"])
    for a in primes:
        if a < a_left:
            continue
        if a > a_right:
            break
        modulus = q * a
        carry = (p2 + p - 1) // modulus - p2 // modulus
        exact_phase = (p - 1) / modulus
        p_phase = p / modulus
        saw_exact = frac(p2, modulus) - frac(p2 + p - 1, modulus)
        saw_p = saw_exact - 1.0 / modulus
        if abs((carry - exact_phase) - saw_exact) > 1e-12:
            identity_failures += 1
        if abs((carry - p_phase) - saw_p) > 1e-12:
            identity_failures += 1
        carry_count += carry
        phase_p += p_phase
        phase_p_minus_1 += exact_phase
        saw_exact_sum += saw_exact
        saw_p_sum += saw_p
        sample = {
            "a": a,
            "modulus": modulus,
            "carry": carry,
            "phase_p": p_phase,
            "saw_p": saw_p,
            "residue_left": p2 % modulus,
            "residue_right": (p2 + p - 1) % modulus,
        }
        if top_abs_sample is None or abs(saw_p) > abs(top_abs_sample["saw_p"]):
            top_abs_sample = sample
    return {
        "q": q,
        "a_interval": [a_left, a_right],
        "carry_count": carry_count,
        "phase_p": phase_p,
        "phase_p_minus_1": phase_p_minus_1,
        "signed_discrepancy_vs_p_phase": carry_count - phase_p,
        "signed_discrepancy_vs_exact_phase": carry_count - phase_p_minus_1,
        "saw_p_sum": saw_p_sum,
        "saw_exact_sum": saw_exact_sum,
        "identity_failure_count": identity_failures,
        "top_abs_saw_sample": top_abs_sample,
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
    """审计一个 quarter-gate block 的 sawtooth 恒等式。"""
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
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "skipped_ultra_low": False,
        "q_axis_count": len(q_rows),
        "carry_count": sum(row["carry_count"] for row in q_rows),
        "phase_p": sum(row["phase_p"] for row in q_rows),
        "phase_p_minus_1": sum(row["phase_p_minus_1"] for row in q_rows),
        "saw_p_sum": sum(row["saw_p_sum"] for row in q_rows),
        "saw_exact_sum": sum(row["saw_exact_sum"] for row in q_rows),
        "identity_failure_count": sum(row["identity_failure_count"] for row in q_rows),
        "q_rows": q_rows,
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 sawtooth 恒等式。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, block_primes, primes, flags, trial_primes))
    active_rows = [row for row in rows if not row.get("skipped_ultra_low")]
    carry_count = sum(row["carry_count"] for row in active_rows)
    phase_p = sum(row["phase_p"] for row in active_rows)
    phase_exact = sum(row["phase_p_minus_1"] for row in active_rows)
    return {
        "p": p,
        "quarter_gate_row_count": len(active_rows),
        "ultra_low_skipped_row_count": sum(1 for row in rows if row.get("skipped_ultra_low")),
        "carry_count": carry_count,
        "phase_p": phase_p,
        "phase_p_minus_1": phase_exact,
        "signed_discrepancy_vs_p_phase": carry_count - phase_p,
        "signed_discrepancy_vs_exact_phase": carry_count - phase_exact,
        "saw_p_sum": sum(row["saw_p_sum"] for row in active_rows),
        "saw_exact_sum": sum(row["saw_exact_sum"] for row in active_rows),
        "identity_failure_count": sum(row["identity_failure_count"] for row in active_rows),
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_semiprime_phase_sawtooth_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 sawtooth 恒等式审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]
    rows = [row for profile in profiles for row in profile["rows"] if not row.get("skipped_ultra_low")]
    q_rows = [q_row for row in rows for q_row in row["q_rows"]]
    carry_count = sum(profile["carry_count"] for profile in profiles)
    phase_p = sum(profile["phase_p"] for profile in profiles)
    phase_exact = sum(profile["phase_p_minus_1"] for profile in profiles)
    saw_p_sum = sum(profile["saw_p_sum"] for profile in profiles)
    saw_exact_sum = sum(profile["saw_exact_sum"] for profile in profiles)
    top_abs_q = max(
        q_rows,
        key=lambda item: abs(item["saw_p_sum"]),
        default=None,
    )
    identity_failures = sum(profile["identity_failure_count"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_semiprime_phase_sawtooth_router",
        "status": "reciprocal_carry_discrepancy_reduced_to_sawtooth_sum_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "sawtooth_identity_closed": identity_failures == 0,
        "identity_failure_count": identity_failures,
        "reciprocal_sawtooth_bound_proved": False,
        "reciprocal_sawtooth_pdec_excluded": False,
        "occupied_b_selberg_prime_bound_proved": False,
        "row_column_unconditional_closed": False,
        "q_axis_count": len(q_rows),
        "carry_count": carry_count,
        "phase_p": phase_p,
        "phase_p_minus_1": phase_exact,
        "carry_over_phase_p": safe_ratio(carry_count, phase_p),
        "signed_discrepancy_vs_p_phase": carry_count - phase_p,
        "signed_discrepancy_vs_exact_phase": carry_count - phase_exact,
        "saw_p_sum": saw_p_sum,
        "saw_exact_sum": saw_exact_sum,
        "top_abs_saw_q": top_abs_q,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "semiprime fiber 的 carry 偏差已化为精确 sawtooth 恒等式。"
            "对 `m=qa`，有 `carry-(P-1)/m={P^2/m}-{(P^2+P-1)/m}`，"
            "同时 `carry-P/m` 只多一个 `-1/m` 校正。"
            "因此相位异常必须表现为倒数端点分数部差的低频或局部集中；"
            "样本恒等式零失败。剩余是证明这些 sawtooth 和的统一界，或登记为 reciprocal-sawtooth/PDEC。"
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
        "# Prime Matrix square-phase low-alpha semiprime phase sawtooth 路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sawtooth_identity_closed={fmt_bool(result['sawtooth_identity_closed'])}",
        f"identity_failure_count={result['identity_failure_count']}",
        f"reciprocal_sawtooth_bound_proved={fmt_bool(result['reciprocal_sawtooth_bound_proved'])}",
        f"reciprocal_sawtooth_pdec_excluded={fmt_bool(result['reciprocal_sawtooth_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局 sawtooth 账本",
        "",
        "| q axes | carry | phase P/m | carry/phase | saw P sum | saw exact sum |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['q_axis_count']} | {result['carry_count']} | {result['phase_p']:.6f} | "
            f"{fmt_float(result['carry_over_phase_p'])} | {result['saw_p_sum']:.6f} | "
            f"{result['saw_exact_sum']:.6f} |"
        ),
        "",
        "## 2. 最热 q 轴",
        "",
        "| record |",
        "| --- |",
        f"| `{result['top_abs_saw_q']}` |",
        "",
        "## 3. 每个 P 的总结",
        "",
        "| P | carry | phase P/m | saw P sum | saw exact sum |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['carry_count']} | {profile['phase_p']:.6f} | "
            f"{profile['saw_p_sum']:.6f} | {profile['saw_exact_sum']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：carry 偏差与端点分数部 sawtooth 差完全等价。",
            "- 未闭合：sawtooth 和的统一界。",
            "- 未闭合：若 sawtooth 异常集中，对应 PDEC 的排除。",
            "- 未闭合：occupied-b 序列的一维 Selberg 素性上界。",
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
                "sawtooth_identity_closed": result["sawtooth_identity_closed"],
                "saw_p_sum": result["saw_p_sum"],
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
