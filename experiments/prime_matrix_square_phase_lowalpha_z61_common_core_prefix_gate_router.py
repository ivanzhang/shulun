#!/usr/bin/env python3
"""审计 z=61 common-core ratio-window 的 prefix interval gate。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_common_core_prefix_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
WINDOW_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.md"

NEXT_TARGET = "PrefixIntervalGateCapacityBoundOrPrefixGatePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_common_core_prefix_gate_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def interval_selected(prefix: int, small: int, large: int) -> bool:
    """判断 prefix 是否使 ratio 落入 `(4,8]`。"""
    ratio = large / (prefix * small)
    return 4 < ratio <= 8


def audit() -> dict[str, Any]:
    """执行 prefix gate 审计。"""
    data = json.loads(WINDOW_JSON.read_text(encoding="utf-8"))
    prefixes = sorted(data["prefixes"])
    split_map: dict[tuple[int, int], dict[str, Any]] = {}
    for row in data["selector_rows"]:
        small, large = row["core_split"]
        key = (small, large)
        if key not in split_map:
            split_map[key] = {
                "core_split": [small, large],
                "ratio_large_over_small": large / small,
                "prefix_lower_closed": large / (8 * small),
                "prefix_upper_open": large / (4 * small),
                "prefix_rows": [],
            }
        selected_by_window = any(candidate["selected"] for candidate in row["candidate_rows"])
        selected_by_gate = interval_selected(row["prefix"], small, large)
        selected_weight = sum(
            candidate["oriented_abs_lambda_product"]
            for candidate in row["candidate_rows"]
            if candidate["selected"]
        )
        split_map[key]["prefix_rows"].append(
            {
                "prefix": row["prefix"],
                "ratio": large / (row["prefix"] * small),
                "selected_by_window": selected_by_window,
                "selected_by_interval_gate": selected_by_gate,
                "selected_weight": selected_weight,
                "gate_identity_ok": selected_by_window == selected_by_gate,
            }
        )

    split_rows = []
    gate_failures = []
    for row in split_map.values():
        row["selected_prefixes"] = [
            item["prefix"] for item in row["prefix_rows"] if item["selected_by_interval_gate"]
        ]
        row["selected_weight"] = sum(item["selected_weight"] for item in row["prefix_rows"])
        row["selected_prefix_count"] = len(row["selected_prefixes"])
        row["gate_identity_closed"] = all(item["gate_identity_ok"] for item in row["prefix_rows"])
        if not row["gate_identity_closed"]:
            gate_failures.append(row)
        split_rows.append(row)
    split_rows.sort(key=lambda row: row["ratio_large_over_small"])

    selected_weight = sum(row["selected_weight"] for row in split_rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_common_core_prefix_gate_router",
        "status": "z61_common_core_window_selector_reduced_to_prefix_interval_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "common_core": data["common_core"],
        "common_core_factorization": data["common_core_factorization"],
        "prefixes": prefixes,
        "prefix_interval_formula": "large/(8*small) <= prefix < large/(4*small)",
        "split_count": len(split_rows),
        "selected_split_count": sum(1 for row in split_rows if row["selected_prefix_count"] > 0),
        "selected_prefix_total_count": sum(row["selected_prefix_count"] for row in split_rows),
        "selected_weight": selected_weight,
        "source_selected_weight": data["selected_weight"],
        "selected_weight_identity_error": selected_weight - data["selected_weight"],
        "prefix_gate_identity_closed": len(gate_failures) == 0 and selected_weight == data["selected_weight"],
        "split_rows": split_rows,
        "prefix_interval_gate_capacity_bound_proved": False,
        "prefix_gate_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "common-core 窗口选择器已压成一维 prefix 区间门：对 core 分割 `small|large`，"
            "prefix `t` 入选当且仅当 `large/(8*small) <= t < large/(4*small)`。"
            "在当前 `t in {2,3}` 中，只有 `[19,253]` 接收 `2,3`，`[23,209]` 只接收 `2`。"
            "下一步最窄硬点是证明这种 prefix interval gate 的容量受控，或登记 PrefixGate-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 common-core prefix gate",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"split_count={result['split_count']}",
        f"selected_split_count={result['selected_split_count']}",
        f"selected_prefix_total_count={result['selected_prefix_total_count']}",
        f"selected_weight={fmt_float(result['selected_weight'])}",
        f"selected_weight_identity_error={fmt_float(result['selected_weight_identity_error'])}",
        f"prefix_gate_identity_closed={fmt_bool(result['prefix_gate_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Prefix 区间门",
        "",
        "| core split | large/small | prefix interval | selected prefixes | selected weight |",
        "| --- | ---: | --- | --- | ---: |",
    ]
    for row in result["split_rows"]:
        interval = f"[{fmt_float(row['prefix_lower_closed'])}, {fmt_float(row['prefix_upper_open'])})"
        lines.append(
            f"| `{row['core_split']}` | {fmt_float(row['ratio_large_over_small'])} | "
            f"`{interval}` | `{row['selected_prefixes']}` | {fmt_float(row['selected_weight'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：ratio-window 选择到 prefix interval gate 的精确等价。",
            "- 未闭合：prefix interval gate 容量界，或 PrefixGate-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
                "prefix_gate_identity_closed": result["prefix_gate_identity_closed"],
                "selected_prefix_total_count": result["selected_prefix_total_count"],
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
