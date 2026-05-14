#!/usr/bin/env python3
"""审计 prime-D 轴 prime-u 分支的 Brun-Titchmarsh 外部闭合接口。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_prime_u_brun_titchmarsh_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BT_MODEL_CONSTANT = 6.0

NEXT_TARGET = "SemiprimeSingleFiberSelbergPhaseBoundAndUltraLowCompositeTailOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json",
    "prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json",
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


def interval_model(row: dict[str, Any]) -> float:
    """返回 `|I_q|/log(P^2/q)` 模型。"""
    center = (row["left_u"] + row["right_u"]) / 2.0
    return row["u_interval_capacity"] / max(1.0, math.log(center))


def brun_titchmarsh_budget(row: dict[str, Any]) -> float:
    """返回 BT 预算 `2H/log H`。"""
    h = row["u_interval_capacity"]
    return 2.0 * h / max(1.0, math.log(h))


def symbolic_bt_factor_bound(p: int, q: int) -> float:
    """给出 BT 相对 `H/log(P^2/q)` 模型的符号常数上界。"""
    alpha = math.log(q) / math.log(p)
    if alpha >= 1:
        return float("inf")
    return 2.0 * (2.0 - alpha) / (1.0 - alpha)


def audit_q_axis(p: int, q: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计单个 q 轴的 prime-u BT 预算。"""
    row = normal.audit_prime_d_q(p, q, flags, trial_primes)
    model = interval_model(row)
    bt = brun_titchmarsh_budget(row)
    factor = symbolic_bt_factor_bound(p, q)
    return {
        "q": q,
        "alpha": math.log(q) / math.log(p),
        "h": row["h"],
        "u_interval_capacity": row["u_interval_capacity"],
        "prime_u_capacity": row["prime_u_capacity"],
        "model": model,
        "brun_titchmarsh_budget": bt,
        "actual_over_model": safe_ratio(row["prime_u_capacity"], model),
        "actual_over_bt": safe_ratio(row["prime_u_capacity"], bt),
        "bt_over_model": safe_ratio(bt, model),
        "symbolic_bt_factor_bound": factor,
        "bt_model_constant_6_covers": factor <= BT_MODEL_CONSTANT,
    }


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    block_primes: list[int],
    flags: bytearray,
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 quarter-gate block 的 prime-u BT 预算。"""
    if not quarter.quarter_gate_closed(p, previous_cutoff):
        return {
            "p": p,
            "previous_cutoff": previous_cutoff,
            "cutoff": cutoff,
            "alpha_left": math.log(previous_cutoff) / math.log(p),
            "skipped_ultra_low": True,
        }
    q_rows = [
        audit_q_axis(p, q, flags, trial_primes)
        for q in block_primes
        if envelope.is_semiprime_regime(p, q)
    ]
    actual = sum(row["prime_u_capacity"] for row in q_rows)
    model = sum(row["model"] for row in q_rows)
    bt = sum(row["brun_titchmarsh_budget"] for row in q_rows)
    top_actual_model = max(
        q_rows,
        key=lambda item: item["actual_over_model"] if item["actual_over_model"] is not None else -1,
        default=None,
    )
    top_bt_model = max(
        q_rows,
        key=lambda item: item["bt_over_model"] if item["bt_over_model"] is not None else -1,
        default=None,
    )
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "skipped_ultra_low": False,
        "q_axis_count": len(q_rows),
        "prime_u_capacity": actual,
        "model": model,
        "brun_titchmarsh_budget": bt,
        "actual_over_model": safe_ratio(actual, model),
        "actual_over_bt": safe_ratio(actual, bt),
        "bt_over_model": safe_ratio(bt, model),
        "max_symbolic_bt_factor_bound": max(
            (row["symbolic_bt_factor_bound"] for row in q_rows),
            default=None,
        ),
        "bt_model_constant_6_covers_all_q": all(row["bt_model_constant_6_covers"] for row in q_rows),
        "top_actual_model_q": top_actual_model,
        "top_bt_model_q": top_bt_model,
        "q_rows": q_rows,
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 prime-u BT 预算。"""
    primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, block_primes, flags, trial_primes))
    active_rows = [row for row in rows if not row.get("skipped_ultra_low")]
    actual = sum(row["prime_u_capacity"] for row in active_rows)
    model = sum(row["model"] for row in active_rows)
    bt = sum(row["brun_titchmarsh_budget"] for row in active_rows)
    worst = max(
        active_rows,
        key=lambda item: item["actual_over_bt"] if item["actual_over_bt"] is not None else -1,
        default=None,
    )
    return {
        "p": p,
        "quarter_gate_row_count": len(active_rows),
        "ultra_low_skipped_row_count": sum(1 for row in rows if row.get("skipped_ultra_low")),
        "prime_u_capacity": actual,
        "model": model,
        "brun_titchmarsh_budget": bt,
        "actual_over_model": safe_ratio(actual, model),
        "actual_over_bt": safe_ratio(actual, bt),
        "bt_over_model": safe_ratio(bt, model),
        "bt_model_constant_6_covers_all_q": all(row["bt_model_constant_6_covers_all_q"] for row in active_rows),
        "worst_block": worst,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_prime_u_brun_titchmarsh_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 prime-u Brun-Titchmarsh 接口审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]
    rows = [row for profile in profiles for row in profile["rows"] if not row.get("skipped_ultra_low")]
    q_rows = [q_row for row in rows for q_row in row["q_rows"]]
    actual = sum(profile["prime_u_capacity"] for profile in profiles)
    model = sum(profile["model"] for profile in profiles)
    bt = sum(profile["brun_titchmarsh_budget"] for profile in profiles)
    top_actual_model = max(
        q_rows,
        key=lambda item: item["actual_over_model"] if item["actual_over_model"] is not None else -1,
        default=None,
    )
    top_bt_model = max(
        q_rows,
        key=lambda item: item["bt_over_model"] if item["bt_over_model"] is not None else -1,
        default=None,
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_prime_u_brun_titchmarsh_router",
        "status": "prime_u_branch_closed_by_external_brun_titchmarsh_constant_open_self_contained",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "prime_d_axis_normal_form_imported": True,
        "brun_titchmarsh_external_input_registered": True,
        "brun_titchmarsh_statement": "pi(x+y)-pi(x) <= 2y/log(y) for 1<y<x",
        "prime_u_bt_model_constant_bound_proved_from_external_input": True,
        "prime_u_bt_model_constant": BT_MODEL_CONSTANT,
        "prime_u_self_contained_proved": False,
        "semiprime_single_fiber_phase_bound_proved": False,
        "ultra_low_composite_tail_bound_proved": False,
        "row_column_unconditional_closed": False,
        "q_axis_count": len(q_rows),
        "quarter_gate_row_count": sum(profile["quarter_gate_row_count"] for profile in profiles),
        "ultra_low_skipped_row_count": sum(profile["ultra_low_skipped_row_count"] for profile in profiles),
        "prime_u_capacity": actual,
        "model": model,
        "brun_titchmarsh_budget": bt,
        "actual_over_model": safe_ratio(actual, model),
        "actual_over_bt": safe_ratio(actual, bt),
        "bt_over_model": safe_ratio(bt, model),
        "all_q_symbolic_bt_factor_le_6": all(row["bt_model_constant_6_covers"] for row in q_rows),
        "max_symbolic_bt_factor_bound": max(
            (row["symbolic_bt_factor_bound"] for row in q_rows),
            default=None,
        ),
        "top_actual_model_q": top_actual_model,
        "top_bt_model_q": top_bt_model,
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "prime-u 分支可由外部 Brun-Titchmarsh 型短区间素数上界支付。"
            "对 `D_-=q<sqrt(P)`，区间长度 `H≈P/q`，BT 给 `prime_u(q)<=2H/logH`；"
            "相对先前模型 `H/log(P^2/q)` 的符号常数为 `2(2-alpha)/(1-alpha)`，"
            "`alpha=log q/log P<1/2` 时不超过 6。"
            "因此在接受该外部输入后，prime-u 子分支从开放硬点中剥离；"
            "自足版本仍需内联 Brun-Titchmarsh，剩余为 semiprime 单纤维相位上界与 ultra-low 复合尾项。"
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
        "# Prime Matrix square-phase low-alpha prime-u Brun-Titchmarsh 接口",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"brun_titchmarsh_external_input_registered={fmt_bool(result['brun_titchmarsh_external_input_registered'])}",
        f"prime_u_bt_model_constant_bound_proved_from_external_input={fmt_bool(result['prime_u_bt_model_constant_bound_proved_from_external_input'])}",
        f"prime_u_self_contained_proved={fmt_bool(result['prime_u_self_contained_proved'])}",
        f"semiprime_single_fiber_phase_bound_proved={fmt_bool(result['semiprime_single_fiber_phase_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局 BT 预算",
        "",
        "| q axes | prime actual | model | BT budget | actual/model | actual/BT | BT/model | max symbolic factor |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['q_axis_count']} | {result['prime_u_capacity']} | {result['model']:.6f} | "
            f"{result['brun_titchmarsh_budget']:.6f} | {fmt_float(result['actual_over_model'])} | "
            f"{fmt_float(result['actual_over_bt'])} | {fmt_float(result['bt_over_model'])} | "
            f"{fmt_float(result['max_symbolic_bt_factor_bound'])} |"
        ),
        "",
        "## 2. 最热 q 轴",
        "",
        "| type | record |",
        "| --- | --- |",
        f"| actual/model | `{result['top_actual_model_q']}` |",
        f"| BT/model | `{result['top_bt_model_q']}` |",
        "",
        "## 3. 每个 P 的总结",
        "",
        "| P | quarter rows | prime actual | actual/model | actual/BT | BT/model |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['quarter_gate_row_count']} | {profile['prime_u_capacity']} | "
            f"{fmt_float(profile['actual_over_model'])} | {fmt_float(profile['actual_over_bt'])} | "
            f"{fmt_float(profile['bt_over_model'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 外部闭合：接受 Brun-Titchmarsh 后，prime-u 分支有统一模型常数 `6`。",
            "- 未自足：本文作者侧尚未内联 Brun-Titchmarsh 证明。",
            "- 未闭合：semiprime 单 `b` 纤维相位/素性上界。",
            "- 未闭合：ultra-low 复合尾项 Rankin/Selberg 上界或 PDEC 排除。",
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
                "prime_u_bt_model_constant": result["prime_u_bt_model_constant"],
                "actual_over_bt": result["actual_over_bt"],
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
