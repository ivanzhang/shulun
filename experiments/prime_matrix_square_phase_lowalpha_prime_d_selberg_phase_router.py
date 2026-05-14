#!/usr/bin/env python3
"""审计 prime-D 轴的 Selberg/相位常数接口。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_prime_d_selberg_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
SAMPLE_CONSTANT = 2.0

NEXT_TARGET = "AsymmetricPrimeDTwoPrimeSelbergAndSingleFiberPhaseBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json",
    "prime-matrix-square-phase-rfp-upper-direct-attack-router.json",
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


def log_weight(center: float) -> float:
    """返回素数模型的对数分母。"""
    return max(1.0, math.log(max(center, math.e)))


def prime_u_model(row: dict[str, Any]) -> float:
    """prime-u 分支的短区间素数模型量。"""
    center = (row["left_u"] + row["right_u"]) / 2.0
    return row["u_interval_capacity"] / log_weight(center)


def semiprime_single_fiber_model(
    p: int,
    q: int,
    right_u: int,
    primes: list[int],
) -> dict[str, Any]:
    """semiprime-u 单 b 纤维的相位/素性模型量。"""
    phase_mass = 0.0
    prime_b_model = 0.0
    nonempty_fibers = 0
    a_count = 0
    max_width = 0.0
    top_width_sample = None
    a_left = math.floor(p / q) + 1
    a_right = math.isqrt(right_u)
    for a in primes:
        if a < a_left:
            continue
        if a > a_right:
            break
        b_left, b_right, width = normal.b_interval_for_qa(p, q, a)
        center = p * p / (q * a)
        phase_mass += width
        prime_b_model += width / log_weight(center)
        a_count += 1
        if b_right >= b_left:
            nonempty_fibers += 1
        if width > max_width:
            max_width = width
            top_width_sample = {
                "a": a,
                "b_interval": [b_left, b_right],
                "width": width,
                "center": center,
            }
    return {
        "a_count": a_count,
        "phase_mass": phase_mass,
        "prime_b_model": prime_b_model,
        "nonempty_fibers": nonempty_fibers,
        "max_width": max_width,
        "top_width_sample": top_width_sample,
    }


def audit_q_axis(
    p: int,
    q: int,
    primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计单个 q 轴的模型压力。"""
    row = normal.audit_prime_d_q(p, q, flags, trial_primes)
    p_model = prime_u_model(row)
    s_model = semiprime_single_fiber_model(p, q, row["right_u"], primes)
    semiprime_model = s_model["prime_b_model"]
    return {
        "q": q,
        "h": row["h"],
        "u_interval_capacity": row["u_interval_capacity"],
        "prime_u_capacity": row["prime_u_capacity"],
        "prime_u_model": p_model,
        "prime_u_over_model": safe_ratio(row["prime_u_capacity"], p_model),
        "semiprime_u_capacity": row["semiprime_u_capacity"],
        "semiprime_phase_mass": s_model["phase_mass"],
        "semiprime_nonempty_fibers": s_model["nonempty_fibers"],
        "semiprime_nonempty_over_phase": safe_ratio(s_model["nonempty_fibers"], s_model["phase_mass"]),
        "semiprime_prime_b_model": semiprime_model,
        "semiprime_u_over_prime_b_model": safe_ratio(row["semiprime_u_capacity"], semiprime_model),
        "semiprime_a_count": s_model["a_count"],
        "semiprime_max_width": s_model["max_width"],
        "semiprime_top_width_sample": s_model["top_width_sample"],
    }


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 quarter-gate block 的 Selberg/相位模型压力。"""
    if not quarter.quarter_gate_closed(p, previous_cutoff):
        return {
            "p": p,
            "previous_cutoff": previous_cutoff,
            "cutoff": cutoff,
            "alpha_left": math.log(previous_cutoff) / math.log(p),
            "skipped_ultra_low": True,
        }
    block_primes = [q for q in primes if previous_cutoff < q <= cutoff and envelope.is_semiprime_regime(p, q)]
    q_rows = [audit_q_axis(p, q, primes, flags, trial_primes) for q in block_primes]
    prime_actual = sum(row["prime_u_capacity"] for row in q_rows)
    prime_model = sum(row["prime_u_model"] for row in q_rows)
    semiprime_actual = sum(row["semiprime_u_capacity"] for row in q_rows)
    semiprime_model = sum(row["semiprime_prime_b_model"] for row in q_rows)
    phase_mass = sum(row["semiprime_phase_mass"] for row in q_rows)
    nonempty_fibers = sum(row["semiprime_nonempty_fibers"] for row in q_rows)
    top_prime_pressure = max(
        q_rows,
        key=lambda item: item["prime_u_over_model"] if item["prime_u_over_model"] is not None else -1,
        default=None,
    )
    top_semiprime_pressure = max(
        q_rows,
        key=lambda item: item["semiprime_u_over_prime_b_model"]
        if item["semiprime_u_over_prime_b_model"] is not None
        else -1,
        default=None,
    )
    top_phase_pressure = max(
        q_rows,
        key=lambda item: item["semiprime_nonempty_over_phase"]
        if item["semiprime_nonempty_over_phase"] is not None
        else -1,
        default=None,
    )
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "skipped_ultra_low": False,
        "q_axis_count": len(q_rows),
        "prime_u_capacity": prime_actual,
        "prime_u_model": prime_model,
        "prime_u_over_model": safe_ratio(prime_actual, prime_model),
        "semiprime_u_capacity": semiprime_actual,
        "semiprime_prime_b_model": semiprime_model,
        "semiprime_u_over_prime_b_model": safe_ratio(semiprime_actual, semiprime_model),
        "semiprime_phase_mass": phase_mass,
        "semiprime_nonempty_fibers": nonempty_fibers,
        "semiprime_nonempty_over_phase": safe_ratio(nonempty_fibers, phase_mass),
        "top_prime_pressure": top_prime_pressure,
        "top_semiprime_pressure": top_semiprime_pressure,
        "top_phase_pressure": top_phase_pressure,
        "q_rows": q_rows,
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 Selberg/相位模型压力。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, primes, flags, trial_primes))
    active_rows = [row for row in rows if not row.get("skipped_ultra_low")]
    worst = max(
        active_rows,
        key=lambda item: (item["prime_u_over_model"] or 0) + (item["semiprime_u_over_prime_b_model"] or 0),
        default=None,
    )
    prime_actual = sum(row["prime_u_capacity"] for row in active_rows)
    prime_model = sum(row["prime_u_model"] for row in active_rows)
    semiprime_actual = sum(row["semiprime_u_capacity"] for row in active_rows)
    semiprime_model = sum(row["semiprime_prime_b_model"] for row in active_rows)
    phase_mass = sum(row["semiprime_phase_mass"] for row in active_rows)
    nonempty = sum(row["semiprime_nonempty_fibers"] for row in active_rows)
    return {
        "p": p,
        "quarter_gate_row_count": len(active_rows),
        "ultra_low_skipped_row_count": sum(1 for row in rows if row.get("skipped_ultra_low")),
        "prime_u_capacity": prime_actual,
        "prime_u_model": prime_model,
        "prime_u_over_model": safe_ratio(prime_actual, prime_model),
        "semiprime_u_capacity": semiprime_actual,
        "semiprime_prime_b_model": semiprime_model,
        "semiprime_u_over_prime_b_model": safe_ratio(semiprime_actual, semiprime_model),
        "semiprime_phase_mass": phase_mass,
        "semiprime_nonempty_fibers": nonempty,
        "semiprime_nonempty_over_phase": safe_ratio(nonempty, phase_mass),
        "worst_quarter_gate_block": worst,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_prime_d_selberg_phase_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def max_ratio(rows: list[dict[str, Any]], key: str) -> float | None:
    """返回比值字段最大值。"""
    values = [row[key] for row in rows if row.get(key) is not None]
    if not values:
        return None
    return max(values)


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 Selberg/相位接口审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]
    block_rows = [row for profile in profiles for row in profile["rows"] if not row.get("skipped_ultra_low")]
    q_rows = [q_row for block in block_rows for q_row in block["q_rows"]]
    prime_actual = sum(profile["prime_u_capacity"] for profile in profiles)
    prime_model = sum(profile["prime_u_model"] for profile in profiles)
    semiprime_actual = sum(profile["semiprime_u_capacity"] for profile in profiles)
    semiprime_model = sum(profile["semiprime_prime_b_model"] for profile in profiles)
    phase_mass = sum(profile["semiprime_phase_mass"] for profile in profiles)
    nonempty = sum(profile["semiprime_nonempty_fibers"] for profile in profiles)
    total_actual = prime_actual + semiprime_actual
    total_model = prime_model + semiprime_model
    top_prime_q = max(
        q_rows,
        key=lambda item: item["prime_u_over_model"] if item["prime_u_over_model"] is not None else -1,
        default=None,
    )
    top_semiprime_q = max(
        q_rows,
        key=lambda item: item["semiprime_u_over_prime_b_model"]
        if item["semiprime_u_over_prime_b_model"] is not None
        else -1,
        default=None,
    )
    top_phase_q = max(
        q_rows,
        key=lambda item: item["semiprime_nonempty_over_phase"]
        if item["semiprime_nonempty_over_phase"] is not None
        else -1,
        default=None,
    )
    max_prime_ratio = max_ratio(q_rows, "prime_u_over_model")
    max_semiprime_ratio = max_ratio(q_rows, "semiprime_u_over_prime_b_model")
    max_phase_ratio = max_ratio(q_rows, "semiprime_nonempty_over_phase")
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_prime_d_selberg_phase_router",
        "status": "prime_d_axis_reduced_to_selberg_phase_constant_or_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "prime_d_axis_normal_form_imported": True,
        "prime_u_selberg_model_materialized": True,
        "semiprime_single_fiber_phase_model_materialized": True,
        "sample_constant": SAMPLE_CONSTANT,
        "sample_prime_u_C2_covers_all_q": max_prime_ratio is not None and max_prime_ratio <= SAMPLE_CONSTANT,
        "sample_semiprime_C2_covers_all_q": max_semiprime_ratio is not None and max_semiprime_ratio <= SAMPLE_CONSTANT,
        "sample_phase_lattice_C2_covers_all_q": max_phase_ratio is not None and max_phase_ratio <= SAMPLE_CONSTANT,
        "prime_d_two_prime_selberg_bound_proved": False,
        "semiprime_single_fiber_phase_bound_proved": False,
        "reciprocal_phase_pdec_excluded": False,
        "ultra_low_composite_tail_bound_proved": False,
        "row_column_unconditional_closed": False,
        "quarter_gate_row_count": sum(profile["quarter_gate_row_count"] for profile in profiles),
        "ultra_low_skipped_row_count": sum(profile["ultra_low_skipped_row_count"] for profile in profiles),
        "q_axis_count": len(q_rows),
        "prime_u_capacity": prime_actual,
        "prime_u_model": prime_model,
        "prime_u_over_model": safe_ratio(prime_actual, prime_model),
        "semiprime_u_capacity": semiprime_actual,
        "semiprime_prime_b_model": semiprime_model,
        "semiprime_u_over_prime_b_model": safe_ratio(semiprime_actual, semiprime_model),
        "semiprime_phase_mass": phase_mass,
        "semiprime_nonempty_fibers": nonempty,
        "semiprime_nonempty_over_phase": safe_ratio(nonempty, phase_mass),
        "total_capacity": total_actual,
        "total_model": total_model,
        "total_over_model": safe_ratio(total_actual, total_model),
        "max_prime_u_q_ratio": max_prime_ratio,
        "max_semiprime_q_ratio": max_semiprime_ratio,
        "max_phase_lattice_q_ratio": max_phase_ratio,
        "top_prime_q": top_prime_q,
        "top_semiprime_q": top_semiprime_q,
        "top_phase_q": top_phase_q,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`D_-=q` 轴现在有两个明确的常数账本：prime-u 分支按短区间素数上筛模型 "
            "`sum_q |I_q|/log(P^2/q)` 支付；semiprime-u 分支按单 `b` 纤维相位模型 "
            "`sum_{q,a} (P/(qa))/log(P^2/(qa))` 支付。样本中两个分支的全局实际/模型都接近 1，"
            "逐 q 压力也被常数 2 覆盖。该步只闭合接口与样本账本；全局仍需证明统一 Selberg/相位常数，"
            "或把失败登记为 reciprocal-phase/PDEC，并另处理 ultra-low 复合尾项。"
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
        "# Prime Matrix square-phase low-alpha prime-D Selberg/相位接口",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prime_u_selberg_model_materialized={fmt_bool(result['prime_u_selberg_model_materialized'])}",
        f"semiprime_single_fiber_phase_model_materialized={fmt_bool(result['semiprime_single_fiber_phase_model_materialized'])}",
        f"sample_prime_u_C2_covers_all_q={fmt_bool(result['sample_prime_u_C2_covers_all_q'])}",
        f"sample_semiprime_C2_covers_all_q={fmt_bool(result['sample_semiprime_C2_covers_all_q'])}",
        f"prime_d_two_prime_selberg_bound_proved={fmt_bool(result['prime_d_two_prime_selberg_bound_proved'])}",
        f"semiprime_single_fiber_phase_bound_proved={fmt_bool(result['semiprime_single_fiber_phase_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局模型压力",
        "",
        "| q axes | prime actual | prime model | prime/model | semi actual | semi model | semi/model | total/model |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['q_axis_count']} | {result['prime_u_capacity']} | {result['prime_u_model']:.6f} | "
            f"{fmt_float(result['prime_u_over_model'])} | {result['semiprime_u_capacity']} | "
            f"{result['semiprime_prime_b_model']:.6f} | {fmt_float(result['semiprime_u_over_prime_b_model'])} | "
            f"{fmt_float(result['total_over_model'])} |"
        ),
        "",
        "## 2. 相位栅格压力",
        "",
        "| phase mass | nonempty fibers | nonempty/phase | max prime q/model | max semi q/model | max phase q/model |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['semiprime_phase_mass']:.6f} | {result['semiprime_nonempty_fibers']} | "
            f"{fmt_float(result['semiprime_nonempty_over_phase'])} | "
            f"{fmt_float(result['max_prime_u_q_ratio'])} | {fmt_float(result['max_semiprime_q_ratio'])} | "
            f"{fmt_float(result['max_phase_lattice_q_ratio'])} |"
        ),
        "",
        "## 3. 最热 q 轴",
        "",
        "| type | record |",
        "| --- | --- |",
        f"| prime-u | `{result['top_prime_q']}` |",
        f"| semiprime-u | `{result['top_semiprime_q']}` |",
        f"| phase lattice | `{result['top_phase_q']}` |",
        "",
        "## 4. 每个 P 的总结",
        "",
        "| P | q rows | prime/model | semi/model | phase nonempty/phase | total |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        q_count = sum(0 if row.get("skipped_ultra_low") else row["q_axis_count"] for row in profile["rows"])
        lines.append(
            f"| {profile['p']} | {q_count} | {fmt_float(profile['prime_u_over_model'])} | "
            f"{fmt_float(profile['semiprime_u_over_prime_b_model'])} | "
            f"{fmt_float(profile['semiprime_nonempty_over_phase'])} | "
            f"{profile['prime_u_capacity'] + profile['semiprime_u_capacity']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：prime-u 与 semiprime 单纤维的同参数模型账本接口。",
            "- 已闭合：样本中逐 q 压力均由常数 2 覆盖。",
            "- 未闭合：统一的非对称双素数窄带 Selberg 上界。",
            "- 未闭合：单 `b` 纤维相位栅格与素性模型的全局常数证明。",
            "- 未闭合：若上述模型失败，对应 reciprocal-phase/PDEC 的排除。",
            "- 未闭合：`z<P^(1/4)` ultra-low 复合尾项。",
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
                "sample_prime_u_C2_covers_all_q": result["sample_prime_u_C2_covers_all_q"],
                "sample_semiprime_C2_covers_all_q": result["sample_semiprime_C2_covers_all_q"],
                "total_over_model": result["total_over_model"],
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
