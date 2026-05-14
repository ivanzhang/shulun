#!/usr/bin/env python3
"""审计 ultra-low-alpha 复合前驱尾项的出生门与容量包络。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_ultralow_composite_tail_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-ultralow-composite-tail-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-ultralow-composite-tail-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-ultralow-composite-tail-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_predecessor_envelope_router as envelope


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-ultralow-composite-tail-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-ultralow-composite-tail-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003, 1000003, 1874177]

NEXT_TARGET = "UltraLowCompositeTailRankinSelbergBoundOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json",
    "prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def next_prime_after(z: int, primes: list[int]) -> int | None:
    """返回大于 z 的最小素数。"""
    for prime in primes:
        if prime > z:
            return prime
    return None


def next_prime_quarter_gate_closed(p: int, z: int, primes: list[int]) -> bool:
    """判断下一素数四分之一门是否关闭复合尾。"""
    next_prime = next_prime_after(z, primes)
    if next_prime is None:
        return False
    return next_prime**4 >= p


def composite_tail_representations(
    p: int,
    z: int,
    block_primes: list[int],
    primes: list[int],
) -> list[tuple[int, int, int]]:
    """枚举复合前驱表示 `(q,E,D_-)`。"""
    limit_d = math.isqrt(p - 1)
    rows = []
    for q in block_primes:
        max_tail = limit_d // q
        if max_tail <= 1:
            continue
        for e_value in envelope.rough_products_above(z, max_tail, primes):
            if e_value <= 1:
                continue
            d_minus = q * e_value
            if envelope.is_semiprime_regime(p, d_minus):
                rows.append((q, e_value, d_minus))
    return rows


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的 ultra-low 复合尾项。"""
    block_primes = [q for q in primes if previous_cutoff < q <= cutoff]
    next_prime = next_prime_after(previous_cutoff, primes)
    gate_closed = next_prime_quarter_gate_closed(p, previous_cutoff, primes)
    reps = composite_tail_representations(p, previous_cutoff, block_primes, primes)
    weighted_exact_capacity = 0
    weighted_integer_capacity = 0
    top_rep = None
    for q, e_value, d_minus in reps:
        capacity = envelope.possible_capacity_for_predecessor(p, d_minus, trial_primes)
        exact = capacity["total_capacity"]
        integer_capacity = capacity["integer_capacity"]
        weighted_exact_capacity += exact
        weighted_integer_capacity += integer_capacity
        record = {
            "q": q,
            "e": e_value,
            "d_minus": d_minus,
            "prime_u_capacity": capacity["prime_u_capacity"],
            "semiprime_u_capacity": capacity["semiprime_u_capacity"],
            "exact_capacity": exact,
            "integer_capacity": integer_capacity,
            "h": p / d_minus,
        }
        if top_rep is None or exact > top_rep["exact_capacity"]:
            top_rep = record
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "next_prime_after_left": next_prime,
        "next_prime_quarter_gate_closed": gate_closed,
        "composite_representation_count": len(reps),
        "weighted_exact_capacity": weighted_exact_capacity,
        "weighted_integer_capacity": weighted_integer_capacity,
        "exact_over_integer_capacity": None
        if weighted_integer_capacity == 0
        else weighted_exact_capacity / weighted_integer_capacity,
        "top_composite_representation": top_rep,
        "sample_representations": [
            {"q": q, "e": e_value, "d_minus": d_minus} for q, e_value, d_minus in reps[:12]
        ],
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 ultra-low 复合尾项。"""
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, primes, trial_primes))
    worst = max(rows, key=lambda item: item["weighted_exact_capacity"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(rows),
        "next_prime_gate_closed_rows": sum(1 for row in rows if row["next_prime_quarter_gate_closed"]),
        "open_ultralow_rows": sum(1 for row in rows if not row["next_prime_quarter_gate_closed"]),
        "composite_representation_count": sum(row["composite_representation_count"] for row in rows),
        "weighted_exact_capacity": sum(row["weighted_exact_capacity"] for row in rows),
        "weighted_integer_capacity": sum(row["weighted_integer_capacity"] for row in rows),
        "worst_ultralow_block": worst,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_ultralow_composite_tail_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 ultra-low 复合尾项审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes))
    rows = [row for profile in profiles for row in profile["rows"]]
    worst = max(rows, key=lambda item: item["weighted_exact_capacity"], default=None)
    exact = sum(profile["weighted_exact_capacity"] for profile in profiles)
    integer_capacity = sum(profile["weighted_integer_capacity"] for profile in profiles)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_ultralow_composite_tail_router",
        "status": "ultralow_composite_tail_reduced_to_next_prime_birth_and_rankin_selberg_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "next_prime_quarter_gate_proved": True,
        "composite_tail_birth_materialized": True,
        "composite_tail_rankin_selberg_bound_proved": False,
        "composite_tail_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "next_prime_gate_closed_rows": sum(profile["next_prime_gate_closed_rows"] for profile in profiles),
        "open_ultralow_rows": sum(profile["open_ultralow_rows"] for profile in profiles),
        "composite_representation_count": sum(profile["composite_representation_count"] for profile in profiles),
        "weighted_exact_capacity": exact,
        "weighted_integer_capacity": integer_capacity,
        "exact_over_integer_capacity": None if integer_capacity == 0 else exact / integer_capacity,
        "profiles": profiles,
        "worst_ultralow_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "ultra-low 复合前驱尾项有更精确的出生门：设 `p_+(z)` 为大于 block 左端 `z` 的最小素数。"
            "若 `p_+(z)^4>=P`，则任意复合 `E>1` 与 block 素数 `q` 都满足 "
            "`D_-=qE>=p_+(z)^2>=sqrt(P)`，不可能进入 semiprime regime。"
            "因此复合尾项只在 `p_+(z)^4<P` 后出生；出生后其候选为 `D_-=qE<sqrt(P)`、"
            "`E` 为 `z`-rough。样本第一次出生在 `P=1874177` 的 `(31,62]` 块，"
            "唯一表示为 `37*37`，精确 prime/semiprime 容量为 102，整数容量为 1369。"
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
        "# Prime Matrix square-phase low-alpha ultra-low 复合尾项",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"next_prime_quarter_gate_proved={fmt_bool(result['next_prime_quarter_gate_proved'])}",
        f"composite_tail_birth_materialized={fmt_bool(result['composite_tail_birth_materialized'])}",
        f"composite_tail_rankin_selberg_bound_proved={fmt_bool(result['composite_tail_rankin_selberg_bound_proved'])}",
        f"composite_tail_pdec_excluded={fmt_bool(result['composite_tail_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局尾项容量",
        "",
        "| closed rows | open ultra-low rows | composite reps | exact cap | integer cap | exact/integer |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['next_prime_gate_closed_rows']} | {result['open_ultralow_rows']} | "
            f"{result['composite_representation_count']} | {result['weighted_exact_capacity']} | "
            f"{result['weighted_integer_capacity']} | {fmt_float(result['exact_over_integer_capacity'])} |"
        ),
        "",
        "## 2. 最坏 ultra-low 块",
        "",
        "| P | block | next prime | open | reps | exact cap | integer cap | top representation |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    worst = result["worst_ultralow_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{worst['next_prime_after_left']} | {fmt_bool(not worst['next_prime_quarter_gate_closed'])} | "
            f"{worst['composite_representation_count']} | {worst['weighted_exact_capacity']} | "
            f"{worst['weighted_integer_capacity']} | `{worst['top_composite_representation']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low rows | gate-closed rows | open ultra-low rows | composite reps | exact cap | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_ultralow_block"]
        block = "none" if row is None else f"({row['previous_cutoff']},{row['cutoff']}]"
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['next_prime_gate_closed_rows']} | "
            f"{profile['open_ultralow_rows']} | {profile['composite_representation_count']} | "
            f"{profile['weighted_exact_capacity']} | `{block}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：下一素数四分之一门 `p_+(z)^4>=P` 排除复合尾。",
            "- 已闭合：复合尾出生后的候选 envelope 为 `D_-=qE<sqrt(P)`、`E` 为 `z`-rough。",
            "- 未闭合：出生后复合尾的 Rankin/Selberg 全局容量上界。",
            "- 未闭合：若复合尾容量尖峰持续出现，对应 PDEC 的排除。",
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
                "next_prime_quarter_gate_proved": result["next_prime_quarter_gate_proved"],
                "composite_representation_count": result["composite_representation_count"],
                "weighted_exact_capacity": result["weighted_exact_capacity"],
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
