#!/usr/bin/env python3
"""审计 dyadic 负平方相位一阶负载账本。

用法示例：
  python3 experiments/prime_matrix_square_phase_dyadic_first_moment_ledger.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-dyadic-first-moment-ledger.json

输出：
  docs/monograph/prime-matrix-square-phase-dyadic-first-moment-ledger.json
  docs/monograph/prime-matrix-square-phase-dyadic-first-moment-ledger.md
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
OUT_JSON = DOCS / "prime-matrix-square-phase-dyadic-first-moment-ledger.json"
OUT_MD = DOCS / "prime-matrix-square-phase-dyadic-first-moment-ledger.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

FIRST_MOMENT = "DyadicSquarePhaseFirstMomentLoadPDEC"
OVERLAP_DEFECT = "DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-dyadic-deletion-excess-split-router.json",
    "prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json",
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


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def delete_residue(allowed: bytearray, p: int, p2: int, q: int) -> None:
    """从 allowed 中删除 k == -P^2 mod q 的列。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start < p:
        allowed[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)


def count_hits(allowed: bytearray, p: int, p2: int, q: int) -> int:
    """计数进入块幸存集中被 q 命中的列。"""
    residue = (-p2) % q
    start = residue if residue != 0 else q
    if start >= p:
        return 0
    return sum(allowed[start:p:q])


def audit_p(p: int, primes: list[int]) -> dict[str, Any]:
    """审计一个 P 的 dyadic 一阶负载。"""
    p2 = p * p
    y = max(2, math.floor(p / math.e))
    cutoffs = cutoffs_for_p(p)
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    prime_index = 0
    rows = []
    for cutoff in cutoffs:
        previous_cutoff = 0 if not rows else rows[-1]["cutoff"]
        block_primes = [q for q in primes if previous_cutoff < q <= cutoff]
        enter_count = sum(allowed)
        linear_weight = sum(1.0 / q for q in block_primes)
        independent_keep = 1.0
        for q in block_primes:
            independent_keep *= 1.0 - 1.0 / q
        independent_delete = enter_count * (1.0 - independent_keep)
        first_moment = sum(count_hits(allowed, p, p2, q) for q in block_primes)
        after = bytearray(allowed)
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            delete_residue(after, p, p2, primes[prime_index])
            prime_index += 1
        exit_count = sum(after)
        union_delete = enter_count - exit_count
        overlap_mass = first_moment - union_delete
        expected_first = enter_count * linear_weight
        rows.append(
            {
                "p": p,
                "previous_cutoff": previous_cutoff,
                "cutoff": cutoff,
                "block_prime_count": len(block_primes),
                "enter_count": enter_count,
                "exit_count": exit_count,
                "union_delete": union_delete,
                "independent_delete": independent_delete,
                "union_excess": union_delete - independent_delete,
                "first_moment": first_moment,
                "expected_first": expected_first,
                "first_excess": first_moment - expected_first,
                "overlap_mass": overlap_mass,
                "expected_overlap_gap": expected_first - independent_delete,
                "overlap_deficit": (expected_first - independent_delete) - overlap_mass,
                "linear_weight": linear_weight,
                "independent_keep": independent_keep,
                "first_excess_over_sqrt_p": (first_moment - expected_first) / math.sqrt(p),
                "union_excess_over_sqrt_p": (union_delete - independent_delete) / math.sqrt(p),
                "overlap_deficit_over_sqrt_p": ((expected_first - independent_delete) - overlap_mass)
                / math.sqrt(p),
            }
        )
        allowed = after
    worst_union = max(rows, key=lambda item: item["union_excess_over_sqrt_p"])
    worst_first = max(rows, key=lambda item: item["first_excess_over_sqrt_p"])
    worst_overlap_deficit = max(rows, key=lambda item: item["overlap_deficit_over_sqrt_p"])
    return {
        "p": p,
        "y": y,
        "row_count": len(rows),
        "worst_union_excess": worst_union,
        "worst_first_excess": worst_first,
        "worst_overlap_deficit": worst_overlap_deficit,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_dyadic_first_moment_ledger.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行审计。"""
    limit = max(max(p_list), 2)
    flags = sieve_bool(limit)
    profiles = []
    for p in p_list:
        primes = primes_from_flags(flags, max(2, math.floor(p / math.e)))
        profiles.append(audit_p(p, primes))
    all_rows = [row for profile in profiles for row in profile["rows"]]
    worst_union = max(all_rows, key=lambda item: item["union_excess_over_sqrt_p"])
    worst_first = max(all_rows, key=lambda item: item["first_excess_over_sqrt_p"])
    worst_overlap = max(all_rows, key=lambda item: item["overlap_deficit_over_sqrt_p"])
    return {
        "certificate_type": "prime_matrix_square_phase_dyadic_first_moment_ledger",
        "status": "dyadic_first_moment_and_overlap_ledger_materialized_defect_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "first_moment_ledger_materialized": True,
        "first_moment_load_pdec_excluded": False,
        "overlap_deficit_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "p_list": p_list,
        "profiles": profiles,
        "worst_union_excess": worst_union,
        "worst_first_excess": worst_first,
        "worst_overlap_deficit": worst_overlap,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": FIRST_MOMENT,
        "parallel_attack_target": OVERLAP_DEFECT,
        "plain_conclusion": (
            "本账本在同一进入块幸存集 `S_z` 上同时物化 union 删除量、"
            "一阶负载和重叠质量。它显示每个 dyadic 过删都可以被精确分摊到"
            "一阶负载超额或重叠不足。当前仍是审计与对象固定，不是全局排斥证明。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase dyadic 一阶负载账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"first_moment_ledger_materialized={fmt_bool(result['first_moment_ledger_materialized'])}",
        f"first_moment_load_pdec_excluded={fmt_bool(result['first_moment_load_pdec_excluded'])}",
        f"overlap_deficit_pdec_excluded={fmt_bool(result['overlap_deficit_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局极值",
        "",
        "| item | P | block | union excess/sqrtP | first excess/sqrtP | overlap deficit/sqrtP |",
        "| --- | ---: | --- | ---: | ---: | ---: |",
    ]
    for label, key in [
        ("worst_union", "worst_union_excess"),
        ("worst_first", "worst_first_excess"),
        ("worst_overlap", "worst_overlap_deficit"),
    ]:
        row = result[key]
        lines.append(
            f"| `{label}` | {row['p']} | `({row['previous_cutoff']},{row['cutoff']}]` | "
            f"{row['union_excess_over_sqrt_p']:.6f} | "
            f"{row['first_excess_over_sqrt_p']:.6f} | "
            f"{row['overlap_deficit_over_sqrt_p']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 2. 每个 P 的最坏行",
            "",
            "| P | y | worst union block | union excess/sqrtP | worst first block | first excess/sqrtP | worst overlap block | overlap deficit/sqrtP |",
            "| ---: | ---: | --- | ---: | --- | ---: | --- | ---: |",
        ]
    )
    for profile in result["profiles"]:
        wu = profile["worst_union_excess"]
        wf = profile["worst_first_excess"]
        wo = profile["worst_overlap_deficit"]
        lines.append(
            f"| {profile['p']} | {profile['y']} | `({wu['previous_cutoff']},{wu['cutoff']}]` | "
            f"{wu['union_excess_over_sqrt_p']:.6f} | `({wf['previous_cutoff']},{wf['cutoff']}]` | "
            f"{wf['first_excess_over_sqrt_p']:.6f} | `({wo['previous_cutoff']},{wo['cutoff']}]` | "
            f"{wo['overlap_deficit_over_sqrt_p']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "已物化：",
            "",
            "```text",
            "U_B = union_delete(S_z,B)",
            "H_B = sum_{q in B} |S_z cap {-P^2 mod q}|",
            "overlap_mass = H_B-U_B",
            "union_excess = first_excess + overlap_deficit",
            "```",
            "",
            "未闭合：",
            "",
            f"- `{FIRST_MOMENT}`：一阶负载超额的 Fourier/PDEC 排斥。",
            f"- `{OVERLAP_DEFECT}`：重叠不足或 pair-correlation 缺陷排斥。",
            "",
            "## 4. 依赖哈希",
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
                "next_direct_attack_target": result["next_direct_attack_target"],
                "parallel_attack_target": result["parallel_attack_target"],
                "first_moment_load_pdec_excluded": result["first_moment_load_pdec_excluded"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
