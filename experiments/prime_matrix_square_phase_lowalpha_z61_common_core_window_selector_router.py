#!/usr/bin/env python3
"""审计 z=61 common-core overlap 的 bucket ratio-window 选择器。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_common_core_window_selector_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router as bilinear
import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution
import prime_matrix_square_phase_lowalpha_z61_overlap_common_core_router as common_core_router
import prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router as profile_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
COMMON_CORE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.md"

NEXT_TARGET = "CommonCoreRatioWindowPartitionBoundOrWindowPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json",
]
TOL = 1e-10


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_common_core_window_selector_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def product(values: list[int]) -> int:
    """计算整数列表乘积。"""
    result = 1
    for value in values:
        result *= value
    return result


def unordered_core_splits(core_factors: list[int]) -> list[tuple[int, int]]:
    """列出 core 因子的无序二分乘积。"""
    splits = set()
    factors = list(core_factors)
    for size in range(len(factors) + 1):
        for subset in itertools.combinations(factors, size):
            left = product(list(subset))
            right = product([factor for factor in factors if factor not in subset])
            splits.add(tuple(sorted((left, right))))
    return sorted(splits)


def selector_rows_for_prefix(
    prefix: int,
    core_factors: list[int],
    weights: dict[int, float],
    target_bucket: str,
) -> list[dict[str, Any]]:
    """列出一个 prefix 下所有 core 分割的 bucket 选择结果。"""
    rows = []
    for left, right in unordered_core_splits(core_factors):
        oriented_candidates = [(prefix * left, right), (prefix * right, left)]
        candidate_rows = []
        for d_value, e_value in oriented_candidates:
            if d_value not in weights or e_value not in weights:
                continue
            ratio = max(d_value, e_value) / min(d_value, e_value)
            bucket = bilinear.balance_bucket(d_value, e_value)
            ordered_symmetry = 1 if d_value == e_value else 2
            candidate_rows.append(
                {
                    "d": d_value,
                    "e": e_value,
                    "ratio": ratio,
                    "bucket": bucket,
                    "abs_lambda_product": abs(weights[d_value] * weights[e_value]),
                    "ordered_symmetry": ordered_symmetry,
                    "oriented_abs_lambda_product": ordered_symmetry * abs(weights[d_value] * weights[e_value]),
                    "selected": bucket == target_bucket,
                }
            )
        rows.append(
            {
                "prefix": prefix,
                "core_split": [left, right],
                "selected_candidate_count": sum(1 for row in candidate_rows if row["selected"]),
                "selected_weight_with_oriented_symmetry": sum(
                    row["oriented_abs_lambda_product"] for row in candidate_rows if row["selected"]
                ),
                "candidate_rows": candidate_rows,
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行 ratio-window 选择器审计。"""
    data = json.loads(COMMON_CORE_JSON.read_text(encoding="utf-8"))
    _, primes = profile_router.collect_value_profiles([data["overlap_p"]])
    weights = attribution.selberg.selberg_weights(61, attribution.DEFAULT_D_LEVEL, primes)
    core_factors = data["common_core_factorization"]
    target_bucket = data["target_bucket"]
    prefixes = data["prefixes"]

    selector_rows = []
    for prefix in prefixes:
        selector_rows.extend(selector_rows_for_prefix(prefix, core_factors, weights, target_bucket))

    selected_edges = [
        {
            "prefix": row["prefix"],
            "core_split": row["core_split"],
            **candidate,
        }
        for row in selector_rows
        for candidate in row["candidate_rows"]
        if candidate["selected"]
    ]
    selected_weight = sum(edge["oriented_abs_lambda_product"] for edge in selected_edges)
    source_weight = data["overlap_contribution_from_moduli"]
    selected_unordered_splits = [
        {"prefix": row["prefix"], "core_split": row["core_split"]}
        for row in selector_rows
        if row["selected_candidate_count"] > 0
    ]
    bucket_counts: dict[str, int] = {}
    for row in selector_rows:
        for candidate in row["candidate_rows"]:
            bucket_counts[candidate["bucket"]] = bucket_counts.get(candidate["bucket"], 0) + 1

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_common_core_window_selector_router",
        "status": "z61_two_three_common_core_overlap_reduced_to_ratio_window_selector_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "common_core": data["common_core"],
        "common_core_factorization": core_factors,
        "prefixes": prefixes,
        "target_bucket": target_bucket,
        "target_ratio_window": "(4,8]",
        "selector_row_count": len(selector_rows),
        "selected_oriented_edge_count": sum(edge["ordered_symmetry"] for edge in selected_edges),
        "selected_unordered_split_count": len(selected_unordered_splits),
        "selected_unordered_splits": selected_unordered_splits,
        "candidate_bucket_counts": bucket_counts,
        "selected_edges": selected_edges,
        "selector_rows": selector_rows,
        "selected_weight": selected_weight,
        "source_overlap_weight": source_weight,
        "selector_weight_identity_error": selected_weight - source_weight,
        "ratio_window_selector_identity_closed": abs(selected_weight - source_weight) <= TOL,
        "common_core_ratio_window_partition_bound_proved": False,
        "window_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "`2C/3C` common-core overlap 的目标权重完全由 bucket 比例窗口选择决定："
            "把 `C=11*19*23` 二分后，只保留使 `max(d,e)/min(d,e)` 落在 `(4,8]` 的分割。"
            "样本中被选中的无序分割只有 `prefix=2` 的两个分割和 `prefix=3` 的一个分割；"
            "其有向对称权重和精确等于 overlap 权重。下一步应证明这类窗口分割容量受控，"
            "或登记 Window-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 common-core 窗口选择器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selector_row_count={result['selector_row_count']}",
        f"selected_oriented_edge_count={result['selected_oriented_edge_count']}",
        f"selected_unordered_split_count={result['selected_unordered_split_count']}",
        f"selected_weight={fmt_float(result['selected_weight'])}",
        f"selector_weight_identity_error={fmt_float(result['selector_weight_identity_error'])}",
        f"ratio_window_selector_identity_closed={fmt_bool(result['ratio_window_selector_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 入选有向边",
        "",
        "| prefix | core split | d | e | ratio | weight |",
        "| ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for edge in result["selected_edges"]:
        lines.append(
            f"| {edge['prefix']} | `{edge['core_split']}` | {edge['d']} | {edge['e']} | "
            f"{fmt_float(edge['ratio'])} | {fmt_float(edge['oriented_abs_lambda_product'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 候选 bucket 计数",
            "",
            "| bucket | oriented candidates |",
            "| --- | ---: |",
        ]
    )
    for bucket, count in sorted(result["candidate_bucket_counts"].items()):
        lines.append(f"| `{bucket}` | {count} |")
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：`2C/3C` common-core 权重到 ratio-window 选择器的精确等价。",
            "- 未闭合：窗口分割容量全局界，或 Window-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
                "ratio_window_selector_identity_closed": result["ratio_window_selector_identity_closed"],
                "selected_unordered_split_count": result["selected_unordered_split_count"],
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
