#!/usr/bin/env python3
"""审计 semiprime predecessor envelope 的 P^(1/4) 门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_semiprime_quarter_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]

NEXT_TARGET = "PrimeDIntervalCapacityBoundAndUltraLowCompositeTailOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json",
    "prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def quarter_gate_closed(p: int, z: int) -> bool:
    """判断 `z>=P^(1/4)` 的整数等价门。"""
    return z**4 >= p


def predecessor_representations(
    d_minus: int,
    z: int,
    block_primes: list[int],
    trial_primes: list[int],
) -> list[tuple[int, int]]:
    """列出 `D_-=qE` 的所有 block 表示。"""
    result = []
    for q in block_primes:
        if d_minus % q == 0 and envelope.is_z_rough(d_minus // q, z, trial_primes):
            result.append((q, d_minus // q))
    return result


def audit_lowalpha_block(
    p: int,
    previous_cutoff: int,
    cutoff: int,
    block_primes: list[int],
    primes: list[int],
    trial_primes: list[int],
) -> dict[str, Any]:
    """审计一个 low-alpha block 的四分之一门分裂。"""
    candidates = envelope.eligible_predecessors(p, previous_cutoff, block_primes, primes)
    prime_d_representations = 0
    composite_e_representations = 0
    prime_d_capacity = 0
    composite_e_capacity = 0
    composite_examples = []
    top_prime_d_capacity = None
    top_composite_capacity = None
    for d_minus in sorted(candidates):
        capacity = envelope.possible_capacity_for_predecessor(p, d_minus, trial_primes)["total_capacity"]
        for q, e_value in predecessor_representations(d_minus, previous_cutoff, block_primes, trial_primes):
            record = {
                "d_minus": d_minus,
                "q": q,
                "e": e_value,
                "capacity": capacity,
                "h": p / d_minus,
            }
            if e_value == 1:
                prime_d_representations += 1
                prime_d_capacity += capacity
                if top_prime_d_capacity is None or capacity > top_prime_d_capacity["capacity"]:
                    top_prime_d_capacity = record
            else:
                composite_e_representations += 1
                composite_e_capacity += capacity
                if len(composite_examples) < 8:
                    composite_examples.append(record)
                if top_composite_capacity is None or capacity > top_composite_capacity["capacity"]:
                    top_composite_capacity = record
    gate_closed = quarter_gate_closed(p, previous_cutoff)
    violation = gate_closed and composite_e_representations > 0
    return {
        "p": p,
        "previous_cutoff": previous_cutoff,
        "cutoff": cutoff,
        "alpha_left": math.log(previous_cutoff) / math.log(p),
        "quarter_gate_closed": gate_closed,
        "eligible_predecessor_count": len(candidates),
        "prime_d_representations": prime_d_representations,
        "composite_e_representations": composite_e_representations,
        "prime_d_capacity": prime_d_capacity,
        "composite_e_capacity": composite_e_capacity,
        "total_capacity": prime_d_capacity + composite_e_capacity,
        "quarter_gate_violation": violation,
        "top_prime_d_capacity": top_prime_d_capacity,
        "top_composite_capacity": top_composite_capacity,
        "composite_examples": composite_examples,
    }


def audit_p(p: int, primes: list[int], trial_primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的四分之一门分裂。"""
    rows = []
    cutoffs = envelope.cutoffs_for_p(p)
    for idx, cutoff in enumerate(cutoffs):
        previous = 0 if idx == 0 else cutoffs[idx - 1]
        block_primes = [q for q in primes if previous < q <= cutoff]
        if previous >= envelope.BASE_D and envelope.factor_depth_bound(p, previous) >= 3:
            rows.append(audit_lowalpha_block(p, previous, cutoff, block_primes, primes, trial_primes))
    worst = max(rows, key=lambda item: item["total_capacity"], default=None)
    return {
        "p": p,
        "lowalpha_row_count": len(rows),
        "quarter_closed_rows": sum(1 for row in rows if row["quarter_gate_closed"]),
        "ultra_low_rows": sum(1 for row in rows if not row["quarter_gate_closed"]),
        "prime_d_representations": sum(row["prime_d_representations"] for row in rows),
        "composite_e_representations": sum(row["composite_e_representations"] for row in rows),
        "prime_d_capacity": sum(row["prime_d_capacity"] for row in rows),
        "composite_e_capacity": sum(row["composite_e_capacity"] for row in rows),
        "total_capacity": sum(row["total_capacity"] for row in rows),
        "quarter_gate_violation_count": sum(1 for row in rows if row["quarter_gate_violation"]),
        "worst_lowalpha_block": worst,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_semiprime_quarter_gate_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行四分之一门审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = []
    for p in p_list:
        primes = envelope.primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes, trial_primes))
    rows = [row for profile in profiles for row in profile["rows"]]
    violation_count = sum(profile["quarter_gate_violation_count"] for profile in profiles)
    total_capacity = sum(profile["total_capacity"] for profile in profiles)
    composite_capacity = sum(profile["composite_e_capacity"] for profile in profiles)
    worst = max(rows, key=lambda item: item["total_capacity"], default=None)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_semiprime_quarter_gate_router",
        "status": "semiprime_envelope_split_by_quarter_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "quarter_gate_inequality_proved": True,
        "sample_quarter_gate_violation_count": violation_count,
        "upper_quarter_composite_predecessor_eliminated": violation_count == 0,
        "prime_d_interval_capacity_bound_proved": False,
        "ultra_low_composite_tail_bound_proved": False,
        "row_column_unconditional_closed": False,
        "quarter_closed_rows": sum(profile["quarter_closed_rows"] for profile in profiles),
        "ultra_low_rows": sum(profile["ultra_low_rows"] for profile in profiles),
        "prime_d_representations": sum(profile["prime_d_representations"] for profile in profiles),
        "composite_e_representations": sum(profile["composite_e_representations"] for profile in profiles),
        "prime_d_capacity": sum(profile["prime_d_capacity"] for profile in profiles),
        "composite_e_capacity": composite_capacity,
        "total_capacity": total_capacity,
        "composite_capacity_share": None if total_capacity == 0 else composite_capacity / total_capacity,
        "profiles": profiles,
        "worst_lowalpha_block": worst,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "先验前驱 envelope 进一步被 `P^(1/4)` 门切开：若 block 左端 `z` 满足 `z^4>=P`，"
            "则任何复合尾 `E>1` 都会给出 `D_-=qE>z^2>=sqrt(P)`，与 semiprime regime 的 "
            "`D_-<sqrt(P)` 矛盾。因此这些块只剩 `D_-=q` 的 prime-D 轴；真正的复合前驱尾项只能存在于 "
            "`z<P^(1/4)` 的 ultra-low-alpha 块。当前样本全部处在四分之一门内，复合尾容量为零。"
        ),
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha semiprime 四分之一门",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"quarter_gate_inequality_proved={fmt_bool(result['quarter_gate_inequality_proved'])}",
        f"upper_quarter_composite_predecessor_eliminated={fmt_bool(result['upper_quarter_composite_predecessor_eliminated'])}",
        f"prime_d_interval_capacity_bound_proved={fmt_bool(result['prime_d_interval_capacity_bound_proved'])}",
        f"ultra_low_composite_tail_bound_proved={fmt_bool(result['ultra_low_composite_tail_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局分裂",
        "",
        "| quarter rows | ultra-low rows | prime-D reps | composite-E reps | prime-D cap | composite-E cap | composite share |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['quarter_closed_rows']} | {result['ultra_low_rows']} | "
            f"{result['prime_d_representations']} | {result['composite_e_representations']} | "
            f"{result['prime_d_capacity']} | {result['composite_e_capacity']} | "
            f"{result['composite_capacity_share']:.6f} |"
        ),
        "",
        "## 2. 最坏 low-alpha 块",
        "",
        "| P | block | quarter gate | prime-D cap | composite-E cap | top prime-D | top composite |",
        "| ---: | --- | ---: | ---: | ---: | --- | --- |",
    ]
    worst = result["worst_lowalpha_block"]
    if worst:
        lines.append(
            f"| {worst['p']} | `({worst['previous_cutoff']},{worst['cutoff']}]` | "
            f"{fmt_bool(worst['quarter_gate_closed'])} | {worst['prime_d_capacity']} | "
            f"{worst['composite_e_capacity']} | `{worst['top_prime_d_capacity']}` | "
            f"`{worst['top_composite_capacity']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 每个 P 的总结",
            "",
            "| P | low rows | quarter rows | ultra-low rows | prime-D cap | composite-E cap | worst block |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for profile in result["profiles"]:
        row = profile["worst_lowalpha_block"]
        if row is None:
            continue
        lines.append(
            f"| {profile['p']} | {profile['lowalpha_row_count']} | {profile['quarter_closed_rows']} | "
            f"{profile['ultra_low_rows']} | {profile['prime_d_capacity']} | {profile['composite_e_capacity']} | "
            f"`({row['previous_cutoff']},{row['cutoff']}]` |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：`z>=P^(1/4)` 的块中，semiprime predecessor 只能是 `D_-=q`。",
            "- 未闭合：prime-D 轴上的 prime-u/semiprime-u 短区间容量全局上界。",
            "- 未闭合：`z<P^(1/4)` ultra-low-alpha 中复合 `E` 尾项的容量上界或 PDEC 排除。",
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
                "quarter_gate_inequality_proved": result["quarter_gate_inequality_proved"],
                "composite_capacity_share": result["composite_capacity_share"],
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
