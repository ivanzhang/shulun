#!/usr/bin/env python3
"""审计 z=61 二级平方同余的商余数门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_secondary_quotient_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.md"

NEXT_TARGET = "QuotientResidueGateGlobalBoundOrQuotientGatePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_secondary_quotient_gate_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def quotient_gate_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把二级平方同余降为商 K 的小模余数门。"""
    rows = []
    for group in source["secondary_selector_rows"]:
        modulus = group["modulus"]
        delta = group["delta"]
        q2 = group["q2"]
        q4 = group["q4"]
        gate_modulus = group["secondary_factor_2q2q4"]
        factor_moduli = [2, q4, q2, 2 * q4, 2 * q2, q2 * q4, gate_modulus]
        candidate_rows = []
        for candidate in group["candidate_rows"]:
            p_value = candidate["p_candidate"]
            quotient_k = (p_value * p_value + delta) // modulus
            gate_residue = (quotient_k + 2 * q4) % gate_modulus
            candidate_rows.append(
                {
                    "root_residue": candidate["root_residue"],
                    "p_candidate": p_value,
                    "quotient_k": quotient_k,
                    "gate_residue_mod_2q2q4": gate_residue,
                    "quotient_gate_closed": gate_residue == 0,
                    "secondary_congruence_closed": candidate["secondary_congruence_closed"],
                    "matches_secondary_congruence": (
                        (gate_residue == 0) == candidate["secondary_congruence_closed"]
                    ),
                    "p_is_prime": candidate["p_is_prime"],
                    "full_source_candidate": candidate["full_source_candidate"],
                }
            )
        factor_gate_rows = []
        for factor_modulus in factor_moduli:
            passed = [
                row
                for row in candidate_rows
                if (row["quotient_k"] + 2 * q4) % factor_modulus == 0
            ]
            factor_gate_rows.append(
                {
                    "factor_modulus": factor_modulus,
                    "pass_count": len(passed),
                    "pass_residues": [row["root_residue"] for row in passed],
                    "selected_passes_uniquely": (
                        len(passed) == 1
                        and passed[0]["root_residue"] == group["selected_residue"]
                    ),
                }
            )
        full_gate_rows = [row for row in candidate_rows if row["quotient_gate_closed"]]
        rows.append(
            {
                "modulus": modulus,
                "delta": delta,
                "q2": q2,
                "q4": q4,
                "gate_modulus_2q2q4": gate_modulus,
                "target_gate_residue": (-2 * q4) % gate_modulus,
                "selected_residue": group["selected_residue"],
                "candidate_count": len(candidate_rows),
                "full_gate_candidate_count": len(full_gate_rows),
                "candidate_rows": candidate_rows,
                "factor_gate_rows": factor_gate_rows,
                "q4_gate_already_unique": next(
                    row for row in factor_gate_rows if row["factor_modulus"] == q4
                )["selected_passes_uniquely"],
                "q2_gate_already_unique": next(
                    row for row in factor_gate_rows if row["factor_modulus"] == q2
                )["selected_passes_uniquely"],
                "all_candidates_match_secondary_congruence": all(
                    row["matches_secondary_congruence"] for row in candidate_rows
                ),
                "quotient_gate_closed_for_group": (
                    len(full_gate_rows) == 1
                    and full_gate_rows[0]["root_residue"] == group["selected_residue"]
                    and all(row["matches_secondary_congruence"] for row in candidate_rows)
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行商余数门审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = quotient_gate_rows(source)
    all_rows_closed = bool(rows) and all(row["quotient_gate_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_secondary_quotient_gate_router",
        "status": "z61_secondary_square_congruence_reduced_to_quotient_residue_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "secondary_quotient_gate_group_count": len(rows),
        "all_secondary_quotient_gates_closed": all_rows_closed,
        "quotient_gate_rows": rows,
        "quotient_residue_gate_global_bound_proved": False,
        "quotient_gate_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "二级平方同余可消去大模数 `M`：由一级条件 `p^2+delta=M*K`，"
            "二级条件等价于 `K+2q4≡0 (mod 2q2q4)`。"
            "样本中 `2q2q4=5254`，而在 32 个一级 CRT 根上，"
            "`mod 37` 门和 `mod 71` 门各自已经单独唯一选中 `r=26951`。"
            "因此最新硬点压成 quotient-residue gate 的全局容量界，"
            "或登记 QuotientGate-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 secondary quotient gate",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"secondary_quotient_gate_group_count={result['secondary_quotient_gate_group_count']}",
        f"all_secondary_quotient_gates_closed={fmt_bool(result['all_secondary_quotient_gates_closed'])}",
        f"quotient_residue_gate_global_bound_proved={fmt_bool(result['quotient_residue_gate_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 商余数门摘要",
        "",
        "| M | delta | gate modulus | target residue | roots | full gate roots | selected | q4 unique | q2 unique |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["quotient_gate_rows"]:
        lines.append(
            f"| {row['modulus']} | {row['delta']} | {row['gate_modulus_2q2q4']} | "
            f"{row['target_gate_residue']} | {row['candidate_count']} | "
            f"{row['full_gate_candidate_count']} | {row['selected_residue']} | "
            f"{fmt_bool(row['q4_gate_already_unique'])} | "
            f"{fmt_bool(row['q2_gate_already_unique'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 因子门",
            "",
            "| factor modulus | pass count | pass residues | uniquely selected |",
            "| ---: | ---: | --- | --- |",
        ]
    )
    for row in result["quotient_gate_rows"]:
        for factor_row in row["factor_gate_rows"]:
            lines.append(
                f"| {factor_row['factor_modulus']} | {factor_row['pass_count']} | "
                f"`{factor_row['pass_residues']}` | "
                f"{fmt_bool(factor_row['selected_passes_uniquely'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 素数候选的 K 余数",
            "",
            "| root | p | K | K+2q4 mod 5254 | prime p | full source |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["quotient_gate_rows"]:
        for candidate in row["candidate_rows"]:
            if candidate["p_is_prime"] or candidate["quotient_gate_closed"]:
                lines.append(
                    f"| {candidate['root_residue']} | {candidate['p_candidate']} | "
                    f"{candidate['quotient_k']} | {candidate['gate_residue_mod_2q2q4']} | "
                    f"{fmt_bool(candidate['p_is_prime'])} | "
                    f"{fmt_bool(candidate['full_source_candidate'])} |"
                )
    lines.extend(
        [
            "",
            "## 4. 自足小引理",
            "",
            "一级平方同余给出 `p^2+delta=M*K`。于是",
            "",
            "```text",
            "p^2+delta+2*M*q4 ≡ 0 (mod 2*M*q2*q4)",
            "```",
            "",
            "等价于 `K+2*q4≡0 (mod 2*q2*q4)`。"
            "因此二级平方同余可降为一级根集合上的小模商余数门。",
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：样本二级同余等价于 quotient `K` 的小模余数门，且 q2/q4 因子门各自唯一选中同一根。",
            "- 未闭合：全局 quotient-residue gate 容量界，或 QuotientGate-PDEC 排斥。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_secondary_quotient_gates_closed": result[
                    "all_secondary_quotient_gates_closed"
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
