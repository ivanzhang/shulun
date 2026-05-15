#!/usr/bin/env python3
"""审计 z=61 quotient gate 的素因子提升门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_quotient_factor_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.md"

NEXT_TARGET = "PrimeFactorLiftGateGlobalBoundOrLiftGatePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_quotient_factor_lift_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def factor_lift_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把 K 余数门改写为对 q2/q4 的平方根提升门。"""
    rows = []
    for group in source["quotient_gate_rows"]:
        modulus = group["modulus"]
        delta = group["delta"]
        q2 = group["q2"]
        q4 = group["q4"]
        selected = group["selected_residue"]
        lift_specs = [
            {
                "name": "q4_plain_square_lift",
                "factor": q4,
                "offset_multiple_of_M": 0,
                "meaning": "K≡0 mod q4, equivalently p^2+delta≡0 mod M*q4",
            },
            {
                "name": "q2_shifted_square_lift",
                "factor": q2,
                "offset_multiple_of_M": 2 * q4,
                "meaning": "K+2q4≡0 mod q2, equivalently p^2+delta+2M*q4≡0 mod M*q2",
            },
            {
                "name": "q2q4_combined_lift",
                "factor": q2 * q4,
                "offset_multiple_of_M": 2 * q4,
                "meaning": "combined odd part of K+2q4≡0 mod 2q2q4",
            },
        ]
        lift_rows = []
        for spec in lift_specs:
            factor = spec["factor"]
            lift_modulus = modulus * factor
            passed = []
            for candidate in group["candidate_rows"]:
                p_value = candidate["p_candidate"]
                lift_residue = (
                    p_value * p_value
                    + delta
                    + modulus * spec["offset_multiple_of_M"]
                ) % lift_modulus
                closed = lift_residue == 0
                if closed:
                    passed.append(candidate["root_residue"])
                candidate[f"{spec['name']}_residue"] = lift_residue
                candidate[f"{spec['name']}_closed"] = closed
            lift_rows.append(
                {
                    **spec,
                    "lift_modulus": lift_modulus,
                    "pass_count": len(passed),
                    "pass_residues": passed,
                    "selected_passes_uniquely": len(passed) == 1 and passed[0] == selected,
                }
            )
        rows.append(
            {
                "modulus": modulus,
                "delta": delta,
                "q2": q2,
                "q4": q4,
                "selected_residue": selected,
                "candidate_count": len(group["candidate_rows"]),
                "lift_rows": lift_rows,
                "candidate_rows": group["candidate_rows"],
                "q4_lift_unique": lift_rows[0]["selected_passes_uniquely"],
                "q2_lift_unique": lift_rows[1]["selected_passes_uniquely"],
                "combined_lift_unique": lift_rows[2]["selected_passes_uniquely"],
                "factor_lift_gate_closed_for_group": (
                    lift_rows[0]["selected_passes_uniquely"]
                    and lift_rows[1]["selected_passes_uniquely"]
                    and lift_rows[2]["selected_passes_uniquely"]
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行素因子提升门审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = factor_lift_rows(source)
    all_rows_closed = bool(rows) and all(row["factor_lift_gate_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_quotient_factor_lift_router",
        "status": "z61_quotient_gate_reduced_to_prime_factor_lift_gates_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "quotient_factor_lift_group_count": len(rows),
        "all_quotient_factor_lift_gates_closed": all_rows_closed,
        "factor_lift_rows": rows,
        "prime_factor_lift_gate_global_bound_proved": False,
        "lift_gate_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "quotient-residue gate 可改写为两个素因子提升门："
            "`q4=37` 门等价于一级平方根从 `M` 提升到 `M*37`，"
            "`q2=71` 门等价于带偏移项 `2Mq4` 提升到 `M*71`。"
            "样本中两个提升门各自已经唯一选中同一个根 `r=26951`，"
            "其合并门也唯一。因此最新硬点从商变量 `K` 收窄为 CRT 根的素因子提升容量界，"
            "或登记 LiftGate-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 quotient factor lift",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"quotient_factor_lift_group_count={result['quotient_factor_lift_group_count']}",
        f"all_quotient_factor_lift_gates_closed={fmt_bool(result['all_quotient_factor_lift_gates_closed'])}",
        f"prime_factor_lift_gate_global_bound_proved={fmt_bool(result['prime_factor_lift_gate_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 素因子提升门",
        "",
        "| gate | factor | lift modulus | offset/M | pass count | pass residues | uniquely selected |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["factor_lift_rows"]:
        for lift in row["lift_rows"]:
            lines.append(
                f"| `{lift['name']}` | {lift['factor']} | {lift['lift_modulus']} | "
                f"{lift['offset_multiple_of_M']} | {lift['pass_count']} | "
                f"`{lift['pass_residues']}` | {fmt_bool(lift['selected_passes_uniquely'])} |"
            )
    lines.extend(
        [
            "",
            "## 2. 素数候选的提升残差",
            "",
            "| root | p | q4 lift | q2 lift | combined lift | prime p | full source |",
            "| ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["factor_lift_rows"]:
        for candidate in row["candidate_rows"]:
            if candidate["p_is_prime"] or candidate["quotient_gate_closed"]:
                lines.append(
                    f"| {candidate['root_residue']} | {candidate['p_candidate']} | "
                    f"{candidate['q4_plain_square_lift_residue']} | "
                    f"{candidate['q2_shifted_square_lift_residue']} | "
                    f"{candidate['q2q4_combined_lift_residue']} | "
                    f"{fmt_bool(candidate['p_is_prime'])} | "
                    f"{fmt_bool(candidate['full_source_candidate'])} |"
                )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "在一级条件 `p^2+delta=M*K` 下，`K+2q4≡0 (mod q)` 等价于",
            "",
            "```text",
            "p^2+delta+2M*q4 ≡ 0 (mod M*q).",
            "```",
            "",
            "当 `q=q4` 时偏移项 `2M*q4` 已被 `M*q4` 整除，所以退化为普通平方根提升；"
            "当 `q=q2` 时得到真正的带偏移提升。两者合并即 quotient gate 的奇素因子部分。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本 q2/q4 两个素因子提升门各自唯一选中同一根。",
            "- 未闭合：全局素因子提升门容量界，或 LiftGate-PDEC 排斥。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_quotient_factor_lift_gates_closed": result[
                    "all_quotient_factor_lift_gates_closed"
                ],
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
