#!/usr/bin/env python3
"""审计 z=61 素因子提升门的仿射根选择器。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_affine_lift_selector_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.md"

NEXT_TARGET = "AffineRootLiftSelectorGlobalBoundOrAffineLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_affine_lift_selector_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def affine_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """把提升门改写为根 r 上的仿射 K 选择器。"""
    rows = []
    for group in source["factor_lift_rows"]:
        modulus = group["modulus"]
        delta = group["delta"]
        q2 = group["q2"]
        q4 = group["q4"]
        selected = group["selected_residue"]
        candidate_rows = []
        for candidate in group["candidate_rows"]:
            root = candidate["root_residue"]
            p_value = candidate["p_candidate"]
            span_h = (p_value - root) // modulus
            local_k0 = (root * root + delta) // modulus
            affine_k = local_k0 + 2 * span_h * root + span_h * span_h * modulus
            q4_residue = affine_k % q4
            q2_residue = (affine_k + 2 * q4) % q2
            combined_residue = (affine_k + 2 * q4) % (q2 * q4)
            candidate_rows.append(
                {
                    "root_residue": root,
                    "p_candidate": p_value,
                    "span_h": span_h,
                    "local_k0": local_k0,
                    "quotient_k": candidate["quotient_k"],
                    "affine_k": affine_k,
                    "affine_formula_matches_quotient_k": affine_k == candidate["quotient_k"],
                    "q4_affine_residue": q4_residue,
                    "q2_shifted_affine_residue": q2_residue,
                    "combined_affine_residue": combined_residue,
                    "q4_affine_gate_closed": q4_residue == 0,
                    "q2_shifted_affine_gate_closed": q2_residue == 0,
                    "combined_affine_gate_closed": combined_residue == 0,
                    "p_is_prime": candidate["p_is_prime"],
                    "full_source_candidate": candidate["full_source_candidate"],
                }
            )
        q4_pass = [row["root_residue"] for row in candidate_rows if row["q4_affine_gate_closed"]]
        q2_pass = [
            row["root_residue"] for row in candidate_rows if row["q2_shifted_affine_gate_closed"]
        ]
        combined_pass = [
            row["root_residue"] for row in candidate_rows if row["combined_affine_gate_closed"]
        ]
        span_values = sorted({row["span_h"] for row in candidate_rows})
        rows.append(
            {
                "modulus": modulus,
                "delta": delta,
                "q2": q2,
                "q4": q4,
                "selected_residue": selected,
                "candidate_count": len(candidate_rows),
                "span_values": span_values,
                "single_span_locked": len(span_values) == 1,
                "q4_affine_pass_count": len(q4_pass),
                "q4_affine_pass_residues": q4_pass,
                "q2_affine_pass_count": len(q2_pass),
                "q2_affine_pass_residues": q2_pass,
                "combined_affine_pass_count": len(combined_pass),
                "combined_affine_pass_residues": combined_pass,
                "candidate_rows": candidate_rows,
                "all_affine_formulae_match_quotient_k": all(
                    row["affine_formula_matches_quotient_k"] for row in candidate_rows
                ),
                "q4_affine_gate_unique": len(q4_pass) == 1 and q4_pass[0] == selected,
                "q2_affine_gate_unique": len(q2_pass) == 1 and q2_pass[0] == selected,
                "combined_affine_gate_unique": len(combined_pass) == 1 and combined_pass[0] == selected,
                "affine_lift_selector_closed_for_group": (
                    len(span_values) == 1
                    and all(row["affine_formula_matches_quotient_k"] for row in candidate_rows)
                    and len(q4_pass) == 1
                    and q4_pass[0] == selected
                    and len(q2_pass) == 1
                    and q2_pass[0] == selected
                    and len(combined_pass) == 1
                    and combined_pass[0] == selected
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行仿射根选择器审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = affine_rows(source)
    all_rows_closed = bool(rows) and all(row["affine_lift_selector_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_affine_lift_selector_router",
        "status": "z61_prime_factor_lifts_reduced_to_affine_root_selector_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "affine_lift_selector_group_count": len(rows),
        "all_affine_lift_selectors_closed": all_rows_closed,
        "affine_selector_rows": rows,
        "affine_root_lift_selector_global_bound_proved": False,
        "affine_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "素因子提升门可完全消去大平方：一级根 `r` 满足 `r^2+delta=M*k0`，"
            "而固定商 `h=floor(p/M)` 后，`K=(p^2+delta)/M` 等于 "
            "`k0+2hr+h^2M`。样本中所有候选根都有同一 `h=3`，"
            "`K mod 37` 与 `K+74 mod 71` 两个仿射门各自唯一选中 `r=26951`。"
            "因此最新硬点从提升同余进一步收窄为一级 CRT 根上的仿射选择器容量界，"
            "或登记 AffineLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 affine lift selector",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"affine_lift_selector_group_count={result['affine_lift_selector_group_count']}",
        f"all_affine_lift_selectors_closed={fmt_bool(result['all_affine_lift_selectors_closed'])}",
        f"affine_root_lift_selector_global_bound_proved={fmt_bool(result['affine_root_lift_selector_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 仿射门摘要",
        "",
        "| M | h values | roots | q4 pass | q2 pass | combined pass | selected | closed |",
        "| ---: | --- | ---: | --- | --- | --- | ---: | --- |",
    ]
    for row in result["affine_selector_rows"]:
        lines.append(
            f"| {row['modulus']} | `{row['span_values']}` | {row['candidate_count']} | "
            f"`{row['q4_affine_pass_residues']}` | `{row['q2_affine_pass_residues']}` | "
            f"`{row['combined_affine_pass_residues']}` | {row['selected_residue']} | "
            f"{fmt_bool(row['affine_lift_selector_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 素数候选的仿射残差",
            "",
            "| root | p | k0 | K | K mod 37 | K+74 mod 71 | combined | prime p | full source |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["affine_selector_rows"]:
        for candidate in row["candidate_rows"]:
            if candidate["p_is_prime"] or candidate["combined_affine_gate_closed"]:
                lines.append(
                    f"| {candidate['root_residue']} | {candidate['p_candidate']} | "
                    f"{candidate['local_k0']} | {candidate['affine_k']} | "
                    f"{candidate['q4_affine_residue']} | "
                    f"{candidate['q2_shifted_affine_residue']} | "
                    f"{candidate['combined_affine_residue']} | "
                    f"{fmt_bool(candidate['p_is_prime'])} | "
                    f"{fmt_bool(candidate['full_source_candidate'])} |"
                )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "若 `p=hM+r` 且 `r^2+delta=M*k0`，则",
            "",
            "```text",
            "(p^2+delta)/M = k0 + 2*h*r + h^2*M.",
            "```",
            "",
            "所以 `K mod q4` 与 `K+2q4 mod q2` 都是一级根 `r` 上的仿射选择条件，"
            "无需再处理大平方或大提升模数。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本 q2/q4 提升门等价于一级根上的两个仿射门，且二者各自唯一选中同一根。",
            "- 未闭合：全局仿射根选择器容量界，或 AffineLift-PDEC 排斥。",
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
                "all_affine_lift_selectors_closed": result["all_affine_lift_selectors_closed"],
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
