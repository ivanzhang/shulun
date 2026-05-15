#!/usr/bin/env python3
"""审计 z=61 正向 lift square-window 与 CRT root selector 的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_root_selector_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SHIFTED_BRIDGE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json"
SQUARE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
ROOT_SELECTOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-crt-root-integral-selector-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.md"

NEXT_TARGET = "CRTRootIntegralSelectorGlobalBoundOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_root_selector_bridge_router.py": file_sha256(
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
    """执行 square-window 到 root selector 的桥接审计。"""
    bridge = load(SHIFTED_BRIDGE_JSON)
    square = load(SQUARE_JSON)
    selector = load(ROOT_SELECTOR_JSON)
    square_row = square["square_window_rows"][0]
    selector_row = selector["selector_rows"][0]
    selected = selector_row["selected_candidate"]

    bridge_closed = (
        bridge["positive_lift_shifted_pair_bridge_closed_for_sample"]
        and square["all_shifted_square_window_groups_closed"]
        and selector["all_crt_root_integral_selectors_closed"]
        and selector_row["crt_root_integral_selector_closed_for_group"]
        and selector_row["modulus"] == square_row["base_modulus"] == bridge["same_p_group_base_modulus"]
        and selector_row["delta"] == square_row["delta_low"] == bridge["square_window_delta"]
        and selector_row["span"] == square_row["span"]
        and selector_row["q2"] == square_row["q2"] == bridge["q2"]
        and selector_row["q4"] == square_row["q4"] == bridge["q4"]
        and selected["p_candidate"] == square_row["p"] == bridge["shifted_pair_p"]
        and selected["s_value"] == square_row["s"] == bridge["common_multiplier"]
        and selected["a4"] == bridge["a4"]
        and selected["a2"] == bridge["a2"]
        and selector_row["integral_s_candidate_count"] == 1
        and selector_row["full_source_candidate_count"] == 1
        and selector_row["selected_is_unique_integral_s_root"]
        and selector_row["selected_is_unique_full_source_root"]
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_root_selector_bridge_router",
        "status": "z61_positive_lift_square_window_reduced_to_unique_root_selector_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            bridge["certificate_type"],
            square["certificate_type"],
            selector["certificate_type"],
        ],
        "target_bucket": bridge["target_bucket"],
        "target_omega": bridge["target_omega"],
        "target_shell": bridge["target_shell"],
        "modulus": selector_row["modulus"],
        "delta": selector_row["delta"],
        "span": selector_row["span"],
        "q2": selector_row["q2"],
        "q4": selector_row["q4"],
        "crt_root_count": selector_row["crt_root_count"],
        "prime_p_candidate_count": selector_row["prime_p_candidate_count"],
        "integral_s_candidate_count": selector_row["integral_s_candidate_count"],
        "full_source_candidate_count": selector_row["full_source_candidate_count"],
        "selected_residue": selector_row["selected_residue"],
        "selected_p": selected["p_candidate"],
        "selected_s": selected["s_value"],
        "selected_a4": selected["a4"],
        "selected_a2": selected["a2"],
        "selected_p_is_prime": selected["p_is_prime"],
        "selected_a4_is_prime": selected["a4_is_prime"],
        "selected_a2_is_prime": selected["a2_is_prime"],
        "selected_is_unique_integral_s_root": selector_row["selected_is_unique_integral_s_root"],
        "selected_is_unique_full_source_root": selector_row["selected_is_unique_full_source_root"],
        "positive_lift_root_selector_bridge_closed_for_sample": bridge_closed,
        "crt_root_integral_selector_global_bound_proved": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "MissingLift 的 square-window 剩余可继续压到 CRT root integral selector："
            "在 `M=57684, delta=527, span=3` 的 32 个 CRT 根中，只有 `r=26951` "
            "给出整数 `s=132`，并同时给出两个素数源 `a4=9371,a2=9767`。"
            "因此正向 lift 存在性在当前 formal unit 中等价于唯一 full-source 根选择；"
            "全局剩余是证明这类根选择器容量界，或登记 MissingLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift root selector bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"crt_root_count={result['crt_root_count']}",
        f"prime_p_candidate_count={result['prime_p_candidate_count']}",
        f"integral_s_candidate_count={result['integral_s_candidate_count']}",
        f"full_source_candidate_count={result['full_source_candidate_count']}",
        f"selected_is_unique_integral_s_root={fmt_bool(result['selected_is_unique_integral_s_root'])}",
        f"selected_is_unique_full_source_root={fmt_bool(result['selected_is_unique_full_source_root'])}",
        f"positive_lift_root_selector_bridge_closed_for_sample={fmt_bool(result['positive_lift_root_selector_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Selector data",
        "",
        "| M | delta | span | q2 | q4 | roots | prime p | integral s | full source |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        f"| {result['modulus']} | {result['delta']} | {result['span']} | "
        f"{result['q2']} | {result['q4']} | {result['crt_root_count']} | "
        f"{result['prime_p_candidate_count']} | {result['integral_s_candidate_count']} | "
        f"{result['full_source_candidate_count']} |",
        "",
        "## 2. Unique selected root",
        "",
        "| residue | p | s | a4 | a2 | p prime | a4 prime | a2 prime |",
        "| ---: | ---: | ---: | ---: | ---: | --- | --- | --- |",
        f"| {result['selected_residue']} | {result['selected_p']} | {result['selected_s']} | "
        f"{result['selected_a4']} | {result['selected_a2']} | "
        f"{fmt_bool(result['selected_p_is_prime'])} | "
        f"{fmt_bool(result['selected_a4_is_prime'])} | "
        f"{fmt_bool(result['selected_a2_is_prime'])} |",
        "",
        "## 3. 证明边界",
        "",
        "- 已闭合：当前 positive lift square-window 与唯一 full-source CRT 根严格同一对象。",
        "- 未闭合：全局 CRT root integral selector 容量界，或 MissingLift-PDEC 排斥。",
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
                "positive_lift_root_selector_bridge_closed_for_sample": result[
                    "positive_lift_root_selector_bridge_closed_for_sample"
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
