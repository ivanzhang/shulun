#!/usr/bin/env python3
"""审计 z=61 positive lift projection gate 到 signed projection support 的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_signed_projection_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PROJECTION_BRIDGE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json"
SIGNED_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.md"

NEXT_TARGET = "SignedCRTSupportCarryBoundOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_signed_projection_bridge_router.py": file_sha256(
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


def gate_fiber_summary(row: dict[str, Any]) -> list[dict[str, Any]]:
    """提取单投影目标纤维摘要。"""
    out = []
    for gate in row["gate_fibers"]:
        out.append(
            {
                "gate_name": gate["gate_name"],
                "ell": gate["ell"],
                "total_target_fiber_size": gate["total_target_fiber_size"],
                "selected_singleton": gate["selected_singleton"],
                "targets": [
                    {
                        "target_residue": target["target_residue"],
                        "fiber_size": target["fiber_size"],
                        "fiber": [
                            f"{item['sign_word']}:{item['root_residue']}"
                            for item in target["fiber"]
                        ],
                    }
                    for target in gate["target_fibers"]
                ],
            }
        )
    return out


def audit() -> dict[str, Any]:
    """执行投影门到符号支撑的桥接审计。"""
    projection = load(PROJECTION_BRIDGE_JSON)
    signed = load(SIGNED_JSON)
    row = signed["signed_projection_rows"][0]
    selected = row["selected_sign_rows"][0]
    combined_classes = [item["target_class"] for item in row["combined_fibers"]]
    combined_nonempty = [
        {
            "target_class": item["target_class"],
            "fiber": [f"{entry['sign_word']}:{entry['root_residue']}" for entry in item["fiber"]],
            "fiber_size": item["fiber_size"],
        }
        for item in row["combined_fibers"]
        if item["fiber_size"] > 0
    ]

    bridge_closed = (
        projection["positive_lift_projection_gate_bridge_closed_for_sample"]
        and signed["all_signed_projection_supports_closed"]
        and row["signed_projection_support_closed_for_group"]
        and row["modulus"] == projection["modulus"]
        and row["q2"] == projection["q2"]
        and row["q4"] == projection["q4"]
        and row["selected_residue"] == projection["selected_residue"]
        and row["sign_vector_count"] == 32
        and row["source_root_count"] == 32
        and row["signed_support_matches_source_roots"]
        and row["pairwise_two_roots"]
        and row["all_local_roots_pm_pairs"]
        and selected["sign_word"] == row["selected_sign_word"] == "--++-"
        and selected["root_residue"] == projection["selected_residue"]
        and selected["least_residue_carry"] == row["selected_carry"] == 6
        and row["combined_selected_singleton"]
        and row["combined_total_target_fiber_size"] == 1
        and combined_classes == projection["combined_projection_classes"]
        and combined_nonempty == [{"target_class": 681, "fiber": ["--++-:26951"], "fiber_size": 1}]
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_signed_projection_bridge_router",
        "status": "z61_positive_lift_projection_gate_reduced_to_signed_crt_support_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            projection["certificate_type"],
            signed["certificate_type"],
        ],
        "target_bucket": projection["target_bucket"],
        "target_omega": projection["target_omega"],
        "target_shell": projection["target_shell"],
        "modulus": projection["modulus"],
        "q2": projection["q2"],
        "q4": projection["q4"],
        "selected_residue": projection["selected_residue"],
        "local_moduli": row["local_moduli"],
        "sign_vector_count": row["sign_vector_count"],
        "source_root_count": row["source_root_count"],
        "signed_support_matches_source_roots": row["signed_support_matches_source_roots"],
        "selected_sign_word": row["selected_sign_word"],
        "selected_carry": row["selected_carry"],
        "carry_correction_needed_for_external_projection": row[
            "carry_correction_needed_for_external_projection"
        ],
        "all_carry_corrected_projections_match_roots": row[
            "all_carry_corrected_projections_match_roots"
        ],
        "gate_fiber_summary": gate_fiber_summary(row),
        "combined_projection_classes": combined_classes,
        "combined_nonempty_fibers": combined_nonempty,
        "combined_total_target_fiber_size": row["combined_total_target_fiber_size"],
        "combined_selected_singleton": row["combined_selected_singleton"],
        "positive_lift_signed_projection_bridge_closed_for_sample": bridge_closed,
        "signed_crt_support_carry_bound_proved": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "MissingLift 的 root projection gate 可展开为五维 CRT 符号支撑："
            "`M=4*3*11*19*23` 的 32 个一级根正好对应 32 个符号向量。"
            "外部小模投影必须使用最小代表 carry 修正；修正后 q4/q2 以及合并模 "
            "`2627` 的目标纤维都只命中 `--++-`，即 `r=26951`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift signed projection bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sign_vector_count={result['sign_vector_count']}",
        f"source_root_count={result['source_root_count']}",
        f"signed_support_matches_source_roots={fmt_bool(result['signed_support_matches_source_roots'])}",
        f"selected_sign_word={result['selected_sign_word']}",
        f"selected_carry={result['selected_carry']}",
        f"combined_selected_singleton={fmt_bool(result['combined_selected_singleton'])}",
        f"positive_lift_signed_projection_bridge_closed_for_sample={fmt_bool(result['positive_lift_signed_projection_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 符号支撑",
        "",
        "| M | local moduli | sign vectors | source roots | selected sign | carry | selected r |",
        "| ---: | --- | ---: | ---: | --- | ---: | ---: |",
        f"| {result['modulus']} | `{result['local_moduli']}` | {result['sign_vector_count']} | "
        f"{result['source_root_count']} | `{result['selected_sign_word']}` | "
        f"{result['selected_carry']} | {result['selected_residue']} |",
        "",
        "## 2. 单投影目标纤维",
        "",
        "| gate | ell | total target fiber | selected singleton | targets |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for gate in result["gate_fiber_summary"]:
        lines.append(
            f"| `{gate['gate_name']}` | {gate['ell']} | {gate['total_target_fiber_size']} | "
            f"{fmt_bool(gate['selected_singleton'])} | `{gate['targets']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 合并投影",
            "",
            "| classes | nonempty fibers | total fiber | singleton |",
            "| --- | --- | ---: | --- |",
            f"| `{result['combined_projection_classes']}` | `{result['combined_nonempty_fibers']}` | "
            f"{result['combined_total_target_fiber_size']} | "
            f"{fmt_bool(result['combined_selected_singleton'])} |",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：当前 MissingLift root projection gate 与带 carry 的 signed CRT 支撑严格同一对象。",
            "- 未闭合：全局 signed CRT carry 支撑界，或 MissingLift-PDEC 排斥。",
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
                "positive_lift_signed_projection_bridge_closed_for_sample": result[
                    "positive_lift_signed_projection_bridge_closed_for_sample"
                ],
                "selected_sign_word": result["selected_sign_word"],
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
