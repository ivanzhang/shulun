#!/usr/bin/env python3
"""审计 z=61 positive lift root selector 到素因子提升门的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_factor_gate_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
ROOT_BRIDGE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json"
SECONDARY_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json"
QUOTIENT_GATE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json"
FACTOR_LIFT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.md"

NEXT_TARGET = "PrimeFactorLiftGateGlobalBoundOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-secondary-congruence-selector-router.json",
    "prime-matrix-square-phase-lowalpha-z61-secondary-quotient-gate-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_factor_gate_bridge_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def audit() -> dict[str, Any]:
    """执行 root selector 到素因子提升门的桥接审计。"""
    root_bridge = load(ROOT_BRIDGE_JSON)
    secondary = load(SECONDARY_JSON)
    quotient_gate = load(QUOTIENT_GATE_JSON)
    factor_lift = load(FACTOR_LIFT_JSON)

    sec_row = secondary["secondary_selector_rows"][0]
    gate_row = quotient_gate["quotient_gate_rows"][0]
    lift_row = factor_lift["factor_lift_rows"][0]
    selected = sec_row["selected_candidate"]
    factor_gate_rows = gate_row["factor_gate_rows"]
    factor_lift_rows = lift_row["lift_rows"]
    q4_gate = next(row for row in factor_gate_rows if row["factor_modulus"] == root_bridge["q4"])
    q2_gate = next(row for row in factor_gate_rows if row["factor_modulus"] == root_bridge["q2"])
    q4_lift = next(row for row in factor_lift_rows if row["name"] == "q4_plain_square_lift")
    q2_lift = next(row for row in factor_lift_rows if row["name"] == "q2_shifted_square_lift")
    combined_lift = next(row for row in factor_lift_rows if row["name"] == "q2q4_combined_lift")

    bridge_closed = (
        root_bridge["positive_lift_root_selector_bridge_closed_for_sample"]
        and secondary["all_secondary_congruence_selectors_closed"]
        and quotient_gate["all_secondary_quotient_gates_closed"]
        and factor_lift["all_quotient_factor_lift_gates_closed"]
        and sec_row["modulus"] == gate_row["modulus"] == lift_row["modulus"] == root_bridge["modulus"]
        and sec_row["delta"] == gate_row["delta"] == lift_row["delta"] == root_bridge["delta"]
        and sec_row["q2"] == gate_row["q2"] == lift_row["q2"] == root_bridge["q2"]
        and sec_row["q4"] == gate_row["q4"] == lift_row["q4"] == root_bridge["q4"]
        and sec_row["selected_residue"] == gate_row["selected_residue"] == lift_row["selected_residue"] == root_bridge["selected_residue"]
        and selected["p_candidate"] == root_bridge["selected_p"]
        and selected["s_is_integer"]
        and selected["full_source_candidate"]
        and sec_row["selected_is_unique_secondary_congruence_root"]
        and gate_row["full_gate_candidate_count"] == 1
        and gate_row["q4_gate_already_unique"]
        and gate_row["q2_gate_already_unique"]
        and lift_row["q4_lift_unique"]
        and lift_row["q2_lift_unique"]
        and lift_row["combined_lift_unique"]
        and q4_gate["pass_residues"] == [root_bridge["selected_residue"]]
        and q2_gate["pass_residues"] == [root_bridge["selected_residue"]]
        and q4_lift["pass_residues"] == [root_bridge["selected_residue"]]
        and q2_lift["pass_residues"] == [root_bridge["selected_residue"]]
        and combined_lift["pass_residues"] == [root_bridge["selected_residue"]]
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_factor_gate_bridge_router",
        "status": "z61_positive_lift_root_selector_reduced_to_prime_factor_lift_gates_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            root_bridge["certificate_type"],
            secondary["certificate_type"],
            quotient_gate["certificate_type"],
            factor_lift["certificate_type"],
        ],
        "target_bucket": root_bridge["target_bucket"],
        "target_omega": root_bridge["target_omega"],
        "target_shell": root_bridge["target_shell"],
        "modulus": root_bridge["modulus"],
        "delta": root_bridge["delta"],
        "q2": root_bridge["q2"],
        "q4": root_bridge["q4"],
        "selected_residue": root_bridge["selected_residue"],
        "selected_p": root_bridge["selected_p"],
        "secondary_factor_2q2q4": sec_row["secondary_factor_2q2q4"],
        "secondary_modulus": sec_row["secondary_modulus"],
        "secondary_congruence_candidate_count": sec_row["secondary_congruence_candidate_count"],
        "gate_modulus_2q2q4": gate_row["gate_modulus_2q2q4"],
        "target_gate_residue": gate_row["target_gate_residue"],
        "full_gate_candidate_count": gate_row["full_gate_candidate_count"],
        "q4_gate_already_unique": gate_row["q4_gate_already_unique"],
        "q2_gate_already_unique": gate_row["q2_gate_already_unique"],
        "q4_factor_gate_pass_residues": q4_gate["pass_residues"],
        "q2_factor_gate_pass_residues": q2_gate["pass_residues"],
        "q4_plain_lift_modulus": q4_lift["lift_modulus"],
        "q2_shifted_lift_modulus": q2_lift["lift_modulus"],
        "combined_lift_modulus": combined_lift["lift_modulus"],
        "q4_lift_unique": lift_row["q4_lift_unique"],
        "q2_lift_unique": lift_row["q2_lift_unique"],
        "combined_lift_unique": lift_row["combined_lift_unique"],
        "positive_lift_factor_gate_bridge_closed_for_sample": bridge_closed,
        "prime_factor_lift_gate_global_bound_proved": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "MissingLift 的唯一根选择可进一步压成两个素因子提升门：q4=37 门是普通平方根"
            "从 M 提升到 M*q4，q2=71 门是带偏移项 `2Mq4` 的平方根提升到 M*q2。"
            "在当前 32 个一级 CRT 根上，这两个门各自单独唯一选中同一根 r=26951，"
            "合并提升门也唯一。剩余因此变成素因子提升门的全局容量界，或 MissingLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift factor gate bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"secondary_congruence_candidate_count={result['secondary_congruence_candidate_count']}",
        f"full_gate_candidate_count={result['full_gate_candidate_count']}",
        f"q4_gate_already_unique={fmt_bool(result['q4_gate_already_unique'])}",
        f"q2_gate_already_unique={fmt_bool(result['q2_gate_already_unique'])}",
        f"combined_lift_unique={fmt_bool(result['combined_lift_unique'])}",
        f"positive_lift_factor_gate_bridge_closed_for_sample={fmt_bool(result['positive_lift_factor_gate_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 二级同余与商门",
        "",
        "| M | delta | selected r | secondary factor | gate modulus | target gate | full gate roots |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        f"| {result['modulus']} | {result['delta']} | {result['selected_residue']} | "
        f"{result['secondary_factor_2q2q4']} | {result['gate_modulus_2q2q4']} | "
        f"{result['target_gate_residue']} | {result['full_gate_candidate_count']} |",
        "",
        "## 2. 素因子门",
        "",
        "| gate | pass residues | unique |",
        "| --- | --- | --- |",
        f"| q4={result['q4']} | `{result['q4_factor_gate_pass_residues']}` | {fmt_bool(result['q4_gate_already_unique'])} |",
        f"| q2={result['q2']} | `{result['q2_factor_gate_pass_residues']}` | {fmt_bool(result['q2_gate_already_unique'])} |",
        "",
        "## 3. 提升模数",
        "",
        "| lift | modulus | unique |",
        "| --- | ---: | --- |",
        f"| q4 plain | {result['q4_plain_lift_modulus']} | {fmt_bool(result['q4_lift_unique'])} |",
        f"| q2 shifted | {result['q2_shifted_lift_modulus']} | {fmt_bool(result['q2_lift_unique'])} |",
        f"| combined | {result['combined_lift_modulus']} | {fmt_bool(result['combined_lift_unique'])} |",
        "",
        "## 4. 证明边界",
        "",
        "- 已闭合：当前 MissingLift 根选择器与素因子提升门严格同一对象。",
        "- 未闭合：全局素因子提升门容量界，或 MissingLift-PDEC 排斥。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
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
                "positive_lift_factor_gate_bridge_closed_for_sample": result[
                    "positive_lift_factor_gate_bridge_closed_for_sample"
                ],
                "selected_residue": result["selected_residue"],
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
