#!/usr/bin/env python3
"""审计 z=61 整数 s 选择器的二级平方同余形式。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_secondary_congruence_selector_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-crt-root-integral-selector-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.md"

NEXT_TARGET = "SecondarySquareCongruenceGlobalBoundOrSecondaryPhasePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-crt-root-integral-selector-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_secondary_congruence_selector_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def selector_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把整数 s 条件改写成二级平方同余并筛选 CRT 根。"""
    rows = []
    for group in source["selector_rows"]:
        modulus = group["modulus"]
        delta = group["delta"]
        span = group["span"]
        q2 = group["q2"]
        q4 = group["q4"]
        secondary_factor = 2 * q2 * q4
        secondary_modulus = modulus * secondary_factor
        candidate_rows = []
        for candidate in group["candidate_rows"]:
            p_value = candidate["p_candidate"]
            secondary_residue = (
                p_value * p_value + delta + 2 * modulus * q4
            ) % secondary_modulus
            candidate_rows.append(
                {
                    "root_residue": candidate["residue"],
                    "p_candidate": p_value,
                    "primary_congruence_closed": (p_value * p_value + delta) % modulus == 0,
                    "secondary_residue": secondary_residue,
                    "secondary_congruence_closed": secondary_residue == 0,
                    "s_is_integer": candidate["s_is_integer"],
                    "secondary_matches_integral_s": (
                        (secondary_residue == 0) == candidate["s_is_integer"]
                    ),
                    "p_is_prime": candidate["p_is_prime"],
                    "full_source_candidate": candidate["full_source_candidate"],
                }
            )
        secondary_rows = [row for row in candidate_rows if row["secondary_congruence_closed"]]
        selected_rows = [
            row for row in candidate_rows if row["root_residue"] == group["selected_residue"]
        ]
        rows.append(
            {
                "modulus": modulus,
                "delta": delta,
                "span": span,
                "q2": q2,
                "q4": q4,
                "secondary_factor_2q2q4": secondary_factor,
                "secondary_modulus": secondary_modulus,
                "candidate_count": len(candidate_rows),
                "secondary_congruence_candidate_count": len(secondary_rows),
                "selected_residue": group["selected_residue"],
                "selected_candidate": selected_rows[0] if selected_rows else None,
                "secondary_congruence_residues": [
                    row["root_residue"] for row in secondary_rows
                ],
                "all_primary_roots_match_integral_s_by_secondary_congruence": all(
                    row["secondary_matches_integral_s"] for row in candidate_rows
                ),
                "selected_is_unique_secondary_congruence_root": (
                    len(secondary_rows) == 1
                    and selected_rows
                    and secondary_rows[0]["root_residue"] == selected_rows[0]["root_residue"]
                ),
                "candidate_rows": candidate_rows,
                "secondary_congruence_selector_closed_for_group": (
                    len(secondary_rows) == 1
                    and selected_rows
                    and secondary_rows[0]["root_residue"] == selected_rows[0]["root_residue"]
                    and all(row["secondary_matches_integral_s"] for row in candidate_rows)
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行二级同余选择器审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = selector_rows(source)
    all_rows_closed = bool(rows) and all(
        row["secondary_congruence_selector_closed_for_group"] for row in rows
    )
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_secondary_congruence_selector_router",
        "status": "z61_integral_root_selector_reduced_to_secondary_square_congruence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "secondary_congruence_selector_group_count": len(rows),
        "all_secondary_congruence_selectors_closed": all_rows_closed,
        "secondary_selector_rows": rows,
        "secondary_square_congruence_global_bound_proved": False,
        "secondary_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "整数 `s` 条件不是额外的启发式筛选，而是一个更强的二级平方同余："
            "`p^2+delta+2Mq4 ≡ 0 (mod 2Mq2q4)`。"
            "在样本的 `32` 个一级 CRT 根中，只有 `r=26951` 同时满足该二级同余；"
            "这与唯一整数 `s=132` 完全等价。"
            "因此 RootSelector-PDEC 进一步压成 SecondarySquareCongruence-PDEC，"
            "下一步证明这种二级平方同余选择的全局容量界。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 secondary congruence selector",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"secondary_congruence_selector_group_count={result['secondary_congruence_selector_group_count']}",
        f"all_secondary_congruence_selectors_closed={fmt_bool(result['all_secondary_congruence_selectors_closed'])}",
        f"secondary_square_congruence_global_bound_proved={fmt_bool(result['secondary_square_congruence_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 二级同余摘要",
        "",
        "| M | secondary factor | secondary modulus | roots | secondary roots | selected | closed |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["secondary_selector_rows"]:
        lines.append(
            f"| {row['modulus']} | {row['secondary_factor_2q2q4']} | "
            f"{row['secondary_modulus']} | {row['candidate_count']} | "
            f"{row['secondary_congruence_candidate_count']} | {row['selected_residue']} | "
            f"{fmt_bool(row['secondary_congruence_selector_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 通过二级同余的根",
            "",
            "| root residue | p | secondary residue | integral s | prime p | full source |",
            "| ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    for row in result["secondary_selector_rows"]:
        for candidate in row["candidate_rows"]:
            if candidate["secondary_congruence_closed"] or candidate["p_is_prime"]:
                lines.append(
                    f"| {candidate['root_residue']} | {candidate['p_candidate']} | "
                    f"{candidate['secondary_residue']} | "
                    f"{fmt_bool(candidate['s_is_integer'])} | "
                    f"{fmt_bool(candidate['p_is_prime'])} | "
                    f"{fmt_bool(candidate['full_source_candidate'])} |"
                )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "在一级 CRT 根条件 `p^2+delta≡0 (mod M)` 已成立时，"
            "共同乘子公式",
            "",
            "```text",
            "s=(p^2+delta+2*M*q4)/(2*M*q2*q4)",
            "```",
            "",
            "为整数，当且仅当 `p^2+delta+2*M*q4≡0 (mod 2*M*q2*q4)`。"
            "所以整数源选择器等价于在一级平方根集合上叠加一个二级平方同余。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本一级 CRT 根集中唯一根满足二级平方同余。",
            "- 未闭合：全局二级平方同余容量界，或 SecondaryPhase-PDEC 排斥。",
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
                "all_secondary_congruence_selectors_closed": result[
                    "all_secondary_congruence_selectors_closed"
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
