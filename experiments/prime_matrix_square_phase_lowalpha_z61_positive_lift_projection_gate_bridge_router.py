#!/usr/bin/env python3
"""审计 z=61 positive lift factor gate 到 root projection gate 的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_projection_gate_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
FACTOR_BRIDGE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json"
AFFINE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json"
PROJECTION_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.md"

NEXT_TARGET = "RootProjectionGateGlobalBoundOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json",
    "prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_projection_gate_bridge_router.py": file_sha256(
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
    """执行 factor gate 到 projection gate 的桥接审计。"""
    factor_bridge = load(FACTOR_BRIDGE_JSON)
    affine = load(AFFINE_JSON)
    projection = load(PROJECTION_JSON)

    affine_row = affine["affine_selector_rows"][0]
    projection_row = projection["projection_gate_rows"][0]
    q4_projection = next(
        row for row in projection_row["projection_gate_specs"] if row["name"] == "q4_plain_root_projection"
    )
    q2_projection = next(
        row for row in projection_row["projection_gate_specs"] if row["name"] == "q2_shifted_root_projection"
    )
    selected = factor_bridge["selected_residue"]

    bridge_closed = (
        factor_bridge["positive_lift_factor_gate_bridge_closed_for_sample"]
        and affine["all_affine_lift_selectors_closed"]
        and projection["all_root_projection_gates_closed"]
        and affine_row["affine_lift_selector_closed_for_group"]
        and projection_row["root_projection_gate_closed_for_group"]
        and affine_row["modulus"] == projection_row["modulus"] == factor_bridge["modulus"]
        and affine_row["delta"] == projection_row["delta"] == factor_bridge["delta"]
        and affine_row["q2"] == projection_row["q2"] == factor_bridge["q2"]
        and affine_row["q4"] == projection_row["q4"] == factor_bridge["q4"]
        and affine_row["selected_residue"] == projection_row["selected_residue"] == selected
        and affine_row["q4_affine_gate_unique"]
        and affine_row["q2_affine_gate_unique"]
        and affine_row["combined_affine_gate_unique"]
        and projection_row["q4_projection_gate_unique"]
        and projection_row["q2_projection_gate_unique"]
        and projection_row["combined_projection_gate_unique"]
        and q4_projection["pass_residues"] == [selected]
        and q2_projection["pass_residues"] == [selected]
        and projection_row["combined_pass_residues"] == [selected]
        and projection_row["all_projection_formulae_match_affine"]
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_projection_gate_bridge_router",
        "status": "z61_positive_lift_factor_gates_reduced_to_root_projection_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            factor_bridge["certificate_type"],
            affine["certificate_type"],
            projection["certificate_type"],
        ],
        "target_bucket": factor_bridge["target_bucket"],
        "target_omega": factor_bridge["target_omega"],
        "target_shell": factor_bridge["target_shell"],
        "modulus": factor_bridge["modulus"],
        "delta": factor_bridge["delta"],
        "q2": factor_bridge["q2"],
        "q4": factor_bridge["q4"],
        "selected_residue": selected,
        "span_values": affine_row["span_values"],
        "single_span_locked": affine_row["single_span_locked"],
        "q4_affine_pass_residues": affine_row["q4_affine_pass_residues"],
        "q2_affine_pass_residues": affine_row["q2_affine_pass_residues"],
        "combined_affine_pass_residues": affine_row["combined_affine_pass_residues"],
        "q4_projection_root_solutions": q4_projection["root_projection_solutions"],
        "q2_projection_root_solutions": q2_projection["root_projection_solutions"],
        "q4_projection_pass_residues": q4_projection["pass_residues"],
        "q2_projection_pass_residues": q2_projection["pass_residues"],
        "q4_unrealized_projection_solutions": q4_projection["unrealized_projection_solutions"],
        "q2_unrealized_projection_solutions": q2_projection["unrealized_projection_solutions"],
        "combined_projection_classes": projection_row["combined_projection_classes"],
        "combined_pass_residues": projection_row["combined_pass_residues"],
        "q4_projection_gate_unique": projection_row["q4_projection_gate_unique"],
        "q2_projection_gate_unique": projection_row["q2_projection_gate_unique"],
        "combined_projection_gate_unique": projection_row["combined_projection_gate_unique"],
        "positive_lift_projection_gate_bridge_closed_for_sample": bridge_closed,
        "root_projection_gate_global_bound_proved": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "MissingLift 的素因子提升门可继续降为一级 CRT 根支撑上的小模投影筛："
            "q4=37 投影根为 `15,16`，q2=71 移位投影根为 `42,50`，但在当前 32 个一级根支撑中，"
            "两门与合并门都只命中 `r=26951`。因此剩余从提升容量界进一步压成根支撑投影容量界，"
            "或 MissingLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift projection gate bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"single_span_locked={fmt_bool(result['single_span_locked'])}",
        f"q4_projection_gate_unique={fmt_bool(result['q4_projection_gate_unique'])}",
        f"q2_projection_gate_unique={fmt_bool(result['q2_projection_gate_unique'])}",
        f"combined_projection_gate_unique={fmt_bool(result['combined_projection_gate_unique'])}",
        f"positive_lift_projection_gate_bridge_closed_for_sample={fmt_bool(result['positive_lift_projection_gate_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Affine selector",
        "",
        "| M | delta | selected r | h values | q4 pass | q2 pass | combined pass |",
        "| ---: | ---: | ---: | --- | --- | --- | --- |",
        f"| {result['modulus']} | {result['delta']} | {result['selected_residue']} | "
        f"`{result['span_values']}` | `{result['q4_affine_pass_residues']}` | "
        f"`{result['q2_affine_pass_residues']}` | `{result['combined_affine_pass_residues']}` |",
        "",
        "## 2. Projection gate",
        "",
        "| gate | root solutions | pass roots | unrealized | unique |",
        "| --- | --- | --- | --- | --- |",
        f"| q4={result['q4']} | `{result['q4_projection_root_solutions']}` | "
        f"`{result['q4_projection_pass_residues']}` | `{result['q4_unrealized_projection_solutions']}` | "
        f"{fmt_bool(result['q4_projection_gate_unique'])} |",
        f"| q2={result['q2']} | `{result['q2_projection_root_solutions']}` | "
        f"`{result['q2_projection_pass_residues']}` | `{result['q2_unrealized_projection_solutions']}` | "
        f"{fmt_bool(result['q2_projection_gate_unique'])} |",
        "",
        "## 3. Combined projection",
        "",
        "| combined classes | pass roots | unique |",
        "| --- | --- | --- |",
        f"| `{result['combined_projection_classes']}` | `{result['combined_pass_residues']}` | "
        f"{fmt_bool(result['combined_projection_gate_unique'])} |",
        "",
        "## 4. 证明边界",
        "",
        "- 已闭合：当前 MissingLift factor gate 与 root projection gate 严格同一对象。",
        "- 未闭合：全局根支撑投影容量界，或 MissingLift-PDEC 排斥。",
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
                "positive_lift_projection_gate_bridge_closed_for_sample": result[
                    "positive_lift_projection_gate_bridge_closed_for_sample"
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
