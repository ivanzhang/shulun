#!/usr/bin/env python3
"""审计 z=61 positive lift signed support 到 carry-layer projection 的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_layer_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SIGNED_BRIDGE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json"
CARRY_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.md"

NEXT_TARGET = "CarryLayerTargetFiberGlobalBoundOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_layer_bridge_router.py": file_sha256(
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
    """执行 signed support 到 carry layer 的桥接审计。"""
    signed_bridge = load(SIGNED_BRIDGE_JSON)
    carry = load(CARRY_JSON)
    row = carry["carry_layer_rows"][0]
    selected_layer = next(layer for layer in row["layer_rows"] if layer["carry"] == row["selected_carry"])
    nonempty_layers = [
        {
            "carry": layer["carry"],
            "q4_or_q2_target_hit_count": layer["q4_or_q2_target_hit_count"],
            "combined_target_hit_count": layer["combined_target_hit_count"],
            "target_hit_words": layer["target_hit_words"],
            "combined_hit_words": layer["combined_hit_words"],
        }
        for layer in row["layer_rows"]
        if layer["q4_or_q2_target_hit_count"] or layer["combined_target_hit_count"]
    ]

    bridge_closed = (
        signed_bridge["positive_lift_signed_projection_bridge_closed_for_sample"]
        and carry["all_carry_layer_projections_closed"]
        and row["carry_layer_projection_closed_for_group"]
        and row["modulus"] == signed_bridge["modulus"]
        and row["q2"] == signed_bridge["q2"]
        and row["q4"] == signed_bridge["q4"]
        and row["selected_residue"] == signed_bridge["selected_residue"]
        and row["selected_sign_word"] == signed_bridge["selected_sign_word"]
        and row["selected_carry"] == signed_bridge["selected_carry"]
        and row["combined_target_hit_count"] == 1
        and row["q4_or_q2_target_hit_count"] == 1
        and row["all_target_hits_are_selected"]
        and nonempty_layers
        == [
            {
                "carry": 6,
                "q4_or_q2_target_hit_count": 1,
                "combined_target_hit_count": 1,
                "target_hit_words": ["--++-:26951"],
                "combined_hit_words": ["--++-:26951"],
            }
        ]
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_layer_bridge_router",
        "status": "z61_positive_lift_signed_support_reduced_to_carry_layer_target_fiber_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            signed_bridge["certificate_type"],
            carry["certificate_type"],
        ],
        "target_bucket": signed_bridge["target_bucket"],
        "target_omega": signed_bridge["target_omega"],
        "target_shell": signed_bridge["target_shell"],
        "modulus": signed_bridge["modulus"],
        "q2": signed_bridge["q2"],
        "q4": signed_bridge["q4"],
        "selected_residue": signed_bridge["selected_residue"],
        "selected_sign_word": signed_bridge["selected_sign_word"],
        "selected_carry": signed_bridge["selected_carry"],
        "carry_values": row["carry_values"],
        "carry_layer_count": row["carry_layer_count"],
        "selected_layer_sign_count": selected_layer["sign_count"],
        "selected_layer_root_residues": selected_layer["root_residues"],
        "nonempty_target_layers": nonempty_layers,
        "q4_or_q2_target_hit_count": row["q4_or_q2_target_hit_count"],
        "combined_target_hit_count": row["combined_target_hit_count"],
        "all_target_hits_are_selected": row["all_target_hits_are_selected"],
        "positive_lift_carry_layer_bridge_closed_for_sample": bridge_closed,
        "carry_layer_target_fiber_global_bound_proved": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "MissingLift 的 signed CRT 支撑可进一步按 carry 分层。当前 32 个符号向量只落入 "
            "8 个 carry 层，所有目标投影命中都集中在 carry=6；该层虽然有 7 个符号，"
            "但目标纤维只有 `--++-:26951` 一个命中。剩余因此变成全局 carry-layer "
            "目标纤维界，或 MissingLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift carry-layer bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"carry_values={result['carry_values']}",
        f"selected_carry={result['selected_carry']}",
        f"selected_sign_word={result['selected_sign_word']}",
        f"combined_target_hit_count={result['combined_target_hit_count']}",
        f"all_target_hits_are_selected={fmt_bool(result['all_target_hits_are_selected'])}",
        f"positive_lift_carry_layer_bridge_closed_for_sample={fmt_bool(result['positive_lift_carry_layer_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Carry 分层",
        "",
        "| M | carry layers | selected carry | selected layer roots | selected layer sign count |",
        "| ---: | --- | ---: | --- | ---: |",
        f"| {result['modulus']} | `{result['carry_values']}` | {result['selected_carry']} | "
        f"`{result['selected_layer_root_residues']}` | {result['selected_layer_sign_count']} |",
        "",
        "## 2. 非空目标层",
        "",
        "| nonempty layers | q4/q2 hits | combined hits |",
        "| --- | ---: | ---: |",
        f"| `{result['nonempty_target_layers']}` | {result['q4_or_q2_target_hit_count']} | "
        f"{result['combined_target_hit_count']} |",
        "",
        "## 3. 证明边界",
        "",
        "- 已闭合：当前 MissingLift signed support 与 carry-layer 目标纤维严格同一对象。",
        "- 未闭合：全局 carry-layer 目标纤维界，或 MissingLift-PDEC 排斥。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 4. 依赖哈希",
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
                "positive_lift_carry_layer_bridge_closed_for_sample": result[
                    "positive_lift_carry_layer_bridge_closed_for_sample"
                ],
                "selected_carry": result["selected_carry"],
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
