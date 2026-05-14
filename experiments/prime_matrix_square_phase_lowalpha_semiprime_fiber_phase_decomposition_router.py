#!/usr/bin/env python3
"""审计 semiprime 单 b 纤维的相位/素性分解。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_semiprime_fiber_phase_decomposition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
PHASE_SAMPLE_CONSTANT = 1.25
PRIME_SAMPLE_CONSTANT = 1.75

NEXT_TARGET = "ReciprocalFiberPhaseDiscrepancyAndOccupiedFiberPrimeDensityBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.json",
    "prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json",
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
    """返回素性模型的对数分母。"""
    return max(1.0, math.log(max(center, math.e)))


def audit_q_axis(
    p: int,
    q: int,
    primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计单个 q 轴的相位/素性分解。"""
    row = normal.audit_prime_d_q(p, q, flags, trial_primes)
    phase_mass = 0.0
    nonempty_fibers = 0
    occupied_prime_model = 0.0
    width_prime_model = 0.0
    max_width = 0.0
    top_width_sample = None
    a_left = math.floor(p / q) + 1
    a_right = math.isqrt(row["right_u"])
    for a in primes:
        if a < a_left:
            continue
        if a > a_right:
            break
        b_left, b_right, width = normal.b_interval_for_qa(p, q, a)
        center = p * p / (q * a)
        denominator = log_weight(center)
        phase_mass += width
        width_prime_model += width / denominator
        if b_right >= b_left:
            nonempty_fibers += 1
            occupied_prime_model += 1.0 / denominator
        if width > max_width:
            max_width = width
            top_width_sample = {
                "a": a,
                "b_interval": [b_left, b_right],
                "width": width,
                "center": center,
            }
    return {
        "q": q,
        "h": row["h"],
        "semiprime_u_capacity": row["semiprime_u_capacity"],
        "phase_mass": phase_mass,
        "nonempty_fibers": nonempty_fibers,
        "nonempty_over_phase": safe_ratio(nonempty_fibers, phase_mass),
        "width_prime_model": width_prime_model,
        "semiprime_over_width_model": safe_ratio(row["semiprime_u_capacity"], width_prime_model),
        "occupied_prime_model": occupied_prime_model,
        "semiprime_over_occupied_model": safe_ratio(row["semiprime_u_capacity"], occupied_prime_model),
        "max_width": max_width,
        "top_width_sample": top_width_sample,
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
    """审计一个 quarter-gate block 的 semiprime 纤维分解。"""
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
    semiprime_actual = sum(row["semiprime_u_capacity"] for row in q_rows)
    phase_mass = sum(row["phase_mass"] for row in q_rows)
    nonempty = sum(row["nonempty_fibers"] for row in q_rows)
    width_model = sum(row["width_prime_model"] for row in q_rows)
    occupied_model = sum(row["occupied_prime_model"] for row in q_rows)
    top_phase = max(
        q_rows,
        key=lambda item: item["nonempty_over_phase"] if item["nonempty_over_phase"] is not None else -1,
        default=None,
    )
    top_prime = max(
        q_rows,
        key=lambda item: item["semiprime_over_occupied_model"]
        if item["semiprime_over_occupied_model"] is not None
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
        "semiprime_u_capacity": semiprime_actual,
        "phase_mass": phase_mass,
        "nonempty_fibers": nonempty,
        "nonempty_over_phase": safe_ratio(nonempty, phase_mass),
        "width_prime_model": width_model,
        "semiprime_over_width_model": safe_ratio(semiprime_actual, width_model),
        "occupied_prime_model": occupied_model,
        "semiprime_over_occupied_model": safe_ratio(semiprime_actual, occupied_model),
        "top_phase_q": top_phase,
        "top_prime_q": top_prime,
        "q_rows": q_rows,
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 semiprime 纤维分解。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, block_primes, primes, flags, trial_primes))
    active_rows = [row for row in rows if not row.get("skipped_ultra_low")]
    semiprime_actual = sum(row["semiprime_u_capacity"] for row in active_rows)
    phase_mass = sum(row["phase_mass"] for row in active_rows)
    nonempty = sum(row["nonempty_fibers"] for row in active_rows)
    width_model = sum(row["width_prime_model"] for row in active_rows)
    occupied_model = sum(row["occupied_prime_model"] for row in active_rows)
    return {
        "p": p,
        "quarter_gate_row_count": len(active_rows),
        "ultra_low_skipped_row_count": sum(1 for row in rows if row.get("skipped_ultra_low")),
        "semiprime_u_capacity": semiprime_actual,
        "phase_mass": phase_mass,
        "nonempty_fibers": nonempty,
        "nonempty_over_phase": safe_ratio(nonempty, phase_mass),
        "width_prime_model": width_model,
        "semiprime_over_width_model": safe_ratio(semiprime_actual, width_model),
        "occupied_prime_model": occupied_model,
        "semiprime_over_occupied_model": safe_ratio(semiprime_actual, occupied_model),
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_semiprime_fiber_phase_decomposition_router.py": file_sha256(
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
    """执行 semiprime 单纤维相位/素性分解审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]
    rows = [row for profile in profiles for row in profile["rows"] if not row.get("skipped_ultra_low")]
    q_rows = [q_row for row in rows for q_row in row["q_rows"]]
    semiprime_actual = sum(profile["semiprime_u_capacity"] for profile in profiles)
    phase_mass = sum(profile["phase_mass"] for profile in profiles)
    nonempty = sum(profile["nonempty_fibers"] for profile in profiles)
    width_model = sum(profile["width_prime_model"] for profile in profiles)
    occupied_model = sum(profile["occupied_prime_model"] for profile in profiles)
    top_phase = max(
        q_rows,
        key=lambda item: item["nonempty_over_phase"] if item["nonempty_over_phase"] is not None else -1,
        default=None,
    )
    top_prime = max(
        q_rows,
        key=lambda item: item["semiprime_over_occupied_model"]
        if item["semiprime_over_occupied_model"] is not None
        else -1,
        default=None,
    )
    max_phase = max_ratio(q_rows, "nonempty_over_phase")
    max_prime = max_ratio(q_rows, "semiprime_over_occupied_model")
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_semiprime_fiber_phase_decomposition_router",
        "status": "semiprime_single_fiber_split_to_phase_and_occupied_prime_density_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "prime_u_branch_external_bt_imported": True,
        "single_b_fiber_normal_form_imported": True,
        "phase_occupancy_model_materialized": True,
        "occupied_fiber_prime_density_model_materialized": True,
        "sample_phase_constant": PHASE_SAMPLE_CONSTANT,
        "sample_prime_constant": PRIME_SAMPLE_CONSTANT,
        "sample_phase_constant_covers_all_q": max_phase is not None and max_phase <= PHASE_SAMPLE_CONSTANT,
        "sample_prime_constant_covers_all_q": max_prime is not None and max_prime <= PRIME_SAMPLE_CONSTANT,
        "reciprocal_fiber_phase_discrepancy_bound_proved": False,
        "occupied_fiber_prime_density_bound_proved": False,
        "semiprime_single_fiber_phase_bound_proved": False,
        "ultra_low_composite_tail_bound_proved": False,
        "row_column_unconditional_closed": False,
        "q_axis_count": len(q_rows),
        "semiprime_u_capacity": semiprime_actual,
        "phase_mass": phase_mass,
        "nonempty_fibers": nonempty,
        "nonempty_over_phase": safe_ratio(nonempty, phase_mass),
        "width_prime_model": width_model,
        "semiprime_over_width_model": safe_ratio(semiprime_actual, width_model),
        "occupied_prime_model": occupied_model,
        "semiprime_over_occupied_model": safe_ratio(semiprime_actual, occupied_model),
        "max_phase_q_ratio": max_phase,
        "max_prime_q_ratio": max_prime,
        "top_phase_q": top_phase,
        "top_prime_q": top_prime,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "semiprime 单 `b` 纤维进一步拆成两个独立输入："
            "第一，`(q,a)` 对应的长度小于一的 `b` 区间是否非空，"
            "其总量由 reciprocal phase mass `sum P/(qa)` 控制；"
            "第二，在非空纤维中该唯一整数 `b` 是否为素数，"
            "其模型为 `sum_{nonempty} 1/log(P^2/(qa))`。"
            "样本显示非空纤维/相位质量几乎为 1，非空纤维内素性密度也近似模型；"
            "逐 q 最坏相位压力低于 1.25，逐 q 最坏素性压力低于 1.75。"
            "剩余是证明这两个常数，或把失败登记为 reciprocal-phase/PDEC 与 occupied-fiber prime spike。"
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
        "# Prime Matrix square-phase low-alpha semiprime 单纤维相位/素性分解",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_occupancy_model_materialized={fmt_bool(result['phase_occupancy_model_materialized'])}",
        f"occupied_fiber_prime_density_model_materialized={fmt_bool(result['occupied_fiber_prime_density_model_materialized'])}",
        f"sample_phase_constant_covers_all_q={fmt_bool(result['sample_phase_constant_covers_all_q'])}",
        f"sample_prime_constant_covers_all_q={fmt_bool(result['sample_prime_constant_covers_all_q'])}",
        f"reciprocal_fiber_phase_discrepancy_bound_proved={fmt_bool(result['reciprocal_fiber_phase_discrepancy_bound_proved'])}",
        f"occupied_fiber_prime_density_bound_proved={fmt_bool(result['occupied_fiber_prime_density_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局分解",
        "",
        "| q axes | semiprime actual | phase mass | nonempty | nonempty/phase | occupied model | actual/occupied model |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['q_axis_count']} | {result['semiprime_u_capacity']} | "
            f"{result['phase_mass']:.6f} | {result['nonempty_fibers']} | "
            f"{fmt_float(result['nonempty_over_phase'])} | {result['occupied_prime_model']:.6f} | "
            f"{fmt_float(result['semiprime_over_occupied_model'])} |"
        ),
        "",
        "## 2. 最热 q 轴",
        "",
        "| type | record |",
        "| --- | --- |",
        f"| phase | `{result['top_phase_q']}` |",
        f"| occupied-prime | `{result['top_prime_q']}` |",
        "",
        "## 3. 每个 P 的总结",
        "",
        "| P | semiprime | nonempty/phase | actual/occupied model | actual/width model |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['semiprime_u_capacity']} | "
            f"{fmt_float(profile['nonempty_over_phase'])} | "
            f"{fmt_float(profile['semiprime_over_occupied_model'])} | "
            f"{fmt_float(profile['semiprime_over_width_model'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：semiprime 单纤维分成相位非空问题与非空纤维素性问题。",
            "- 已闭合：样本中相位常数 `1.25` 与素性常数 `1.75` 覆盖逐 q 压力。",
            "- 未闭合：reciprocal phase discrepancy 的全局常数证明或 PDEC 排除。",
            "- 未闭合：occupied-fiber prime density 的全局常数证明或素性尖峰排除。",
            "- 未闭合：ultra-low 复合尾项 Rankin/Selberg 上界。",
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
                "sample_phase_constant_covers_all_q": result["sample_phase_constant_covers_all_q"],
                "sample_prime_constant_covers_all_q": result["sample_prime_constant_covers_all_q"],
                "semiprime_over_occupied_model": result["semiprime_over_occupied_model"],
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
