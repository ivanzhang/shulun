#!/usr/bin/env python3
"""定位 z=61 主导 P-pair 信用的深度格支撑。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_profile_pair_support_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_z61_profile_pair_credit_router as pair_router


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SIGN_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json"
PAIR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.md"

NEXT_TARGET = "DominantPairCellSupportInvariantOrPairSupportDefectPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_profile_pair_support_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def pair_key(positive_p: int, negative_p: int) -> str:
    """生成 pair 键。"""
    return f"{positive_p}->{negative_p}"


def normalized_hhi(values: list[float]) -> float | None:
    """计算归一化集中度；越接近 1 越集中。"""
    total = sum(values)
    if total <= 0:
        return None
    return sum((value / total) ** 2 for value in values)


def audit() -> dict[str, Any]:
    """执行 pair 支撑审计。"""
    sign_data = json.loads(SIGN_JSON.read_text(encoding="utf-8"))
    pair_data = json.loads(PAIR_JSON.read_text(encoding="utf-8"))
    bucket_abs = {
        row["bucket"]: row["opposite_sign_credit"] / row["pair_credit_ratio"]
        for row in pair_data["bucket_rows"]
        if row["pair_credit_ratio"]
    }
    required_by_bucket = {
        row["bucket"]: row["required_credit_to_meet_cap"]
        for row in pair_data["bucket_rows"]
    }
    cover_pair_keys = {
        row["bucket"]: {pair["pair_key"] for pair in row["greedy_cover_pairs"]}
        for row in pair_data["bucket_rows"]
    }

    support: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    global_support: dict[str, list[dict[str, Any]]] = defaultdict(list)
    cell_identity_failures = []
    for row in sign_data["cell_rows"]:
        pairs = pair_router.pair_credit_for_cell(row)
        pair_sum = sum(pair["pair_credit"] for pair in pairs)
        if abs(pair_sum - row["opposite_sign_credit"]) > 1e-8:
            cell_identity_failures.append(
                {
                    "bucket": row["bucket"],
                    "omega": row["omega"],
                    "shell": row["shell"],
                    "error": pair_sum - row["opposite_sign_credit"],
                }
            )
        for pair in pairs:
            key = pair_key(pair["positive_p"], pair["negative_p"])
            item = {
                "bucket": row["bucket"],
                "omega": row["omega"],
                "shell": row["shell"],
                "sign_word": row["sign_word"],
                "pair_key": key,
                "positive_p": pair["positive_p"],
                "negative_p": pair["negative_p"],
                "pair_credit": pair["pair_credit"],
                "bucket_abs_share": safe_ratio(pair["pair_credit"], bucket_abs[row["bucket"]]),
                "required_credit_share": safe_ratio(pair["pair_credit"], required_by_bucket[row["bucket"]]),
                "cell_total_credit": row["opposite_sign_credit"],
                "cell_credit_share_from_pair": safe_ratio(pair["pair_credit"], row["opposite_sign_credit"]),
            }
            support[(row["bucket"], key)].append(item)
            global_support[key].append(item)

    bucket_rows = []
    for bucket_row in pair_data["bucket_rows"]:
        bucket = bucket_row["bucket"]
        pair_support_rows = []
        for pair in bucket_row["pair_rows"]:
            key = pair["pair_key"]
            cells = sorted(
                support[(bucket, key)],
                key=lambda item: item["pair_credit"],
                reverse=True,
            )
            top_cells = cells[:8]
            pair_support_rows.append(
                {
                    **pair,
                    "is_greedy_cover_pair": key in cover_pair_keys[bucket],
                    "support_cell_count": len(cells),
                    "top_cell_credit_share_of_pair": safe_ratio(
                        top_cells[0]["pair_credit"] if top_cells else 0.0,
                        pair["pair_credit"],
                    ),
                    "top_three_credit_share_of_pair": safe_ratio(
                        sum(item["pair_credit"] for item in top_cells[:3]),
                        pair["pair_credit"],
                    ),
                    "support_hhi": normalized_hhi([item["pair_credit"] for item in cells]),
                    "top_cells": top_cells,
                }
            )
        cover_support = [
            row for row in pair_support_rows if row["is_greedy_cover_pair"]
        ]
        bucket_rows.append(
            {
                "bucket": bucket,
                "required_credit_ratio": bucket_row["required_credit_ratio"],
                "pair_credit_ratio": bucket_row["pair_credit_ratio"],
                "greedy_cover_pair_count": bucket_row["greedy_cover_pair_count"],
                "cover_support_cell_count": sum(row["support_cell_count"] for row in cover_support),
                "max_cover_pair_top_three_share": max(
                    (row["top_three_credit_share_of_pair"] or 0.0 for row in cover_support),
                    default=0.0,
                ),
                "pair_support_rows": pair_support_rows,
            }
        )

    global_pair_rows = []
    for key, cells in global_support.items():
        total_credit = sum(item["pair_credit"] for item in cells)
        buckets = sorted({item["bucket"] for item in cells})
        top_cells = sorted(cells, key=lambda item: item["pair_credit"], reverse=True)[:10]
        global_pair_rows.append(
            {
                "pair_key": key,
                "positive_p": int(key.split("->")[0]),
                "negative_p": int(key.split("->")[1]),
                "total_credit": total_credit,
                "bucket_count": len(buckets),
                "buckets": buckets,
                "support_cell_count": len(cells),
                "top_cell_credit_share_of_pair": safe_ratio(
                    top_cells[0]["pair_credit"] if top_cells else 0.0,
                    total_credit,
                ),
                "top_three_credit_share_of_pair": safe_ratio(
                    sum(item["pair_credit"] for item in top_cells[:3]),
                    total_credit,
                ),
                "support_hhi": normalized_hhi([item["pair_credit"] for item in cells]),
                "top_cells": top_cells,
            }
        )
    global_pair_rows.sort(key=lambda row: row["total_credit"], reverse=True)

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_profile_pair_support_router",
        "status": "z61_dominant_profile_pair_credit_support_materialized_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": sign_data["p_list"],
        "z": sign_data["z"],
        "pair_cell_support_identity_closed": len(cell_identity_failures) == 0,
        "dominant_pair_support_materialized": True,
        "dominant_pair_cell_support_invariant_proved": False,
        "pair_support_defect_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cell_identity_failure_count": len(cell_identity_failures),
        "bucket_rows": bucket_rows,
        "global_pair_rows": global_pair_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "主导 P-pair 信用已经落到具体 `(bucket, omega, shell)` 支撑。"
            "这一步区分两种后续打法：若信用集中在少数深度格，就攻局部格相位；"
            "若信用跨多个深度格稳定分布，就攻 pair 相位不变量。"
            "若主导 pair 的支撑消失，则形成 PairSupportDefect-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 profile pair 支撑路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pair_cell_support_identity_closed={fmt_bool(result['pair_cell_support_identity_closed'])}",
        f"dominant_pair_support_materialized={fmt_bool(result['dominant_pair_support_materialized'])}",
        f"dominant_pair_cell_support_invariant_proved={fmt_bool(result['dominant_pair_cell_support_invariant_proved'])}",
        f"pair_support_defect_pdec_excluded={fmt_bool(result['pair_support_defect_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. bucket 覆盖支撑",
        "",
        "| bucket | need | pair credit | cover pairs | cover support cells | max cover top3 share |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['required_credit_ratio'])} | "
            f"{fmt_float(row['pair_credit_ratio'])} | {row['greedy_cover_pair_count']} | "
            f"{row['cover_support_cell_count']} | {fmt_float(row['max_cover_pair_top_three_share'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 全局主导 pair 支撑",
            "",
            "| pair | credit | buckets | cells | top1 share | top3 share | hhi |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["global_pair_rows"][:12]:
        lines.append(
            f"| `{row['pair_key']}` | {fmt_float(row['total_credit'])} | "
            f"{row['bucket_count']} | {row['support_cell_count']} | "
            f"{fmt_float(row['top_cell_credit_share_of_pair'])} | "
            f"{fmt_float(row['top_three_credit_share_of_pair'])} | "
            f"{fmt_float(row['support_hhi'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 覆盖 pair 的最大支撑格",
            "",
            "| bucket | pair | cells | top1 | top3 | top cell |",
            "| --- | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for bucket in result["bucket_rows"]:
        for row in bucket["pair_support_rows"]:
            if not row["is_greedy_cover_pair"]:
                continue
            top_cell = row["top_cells"][0] if row["top_cells"] else None
            if top_cell:
                cell_text = (
                    f"{top_cell['omega']},{top_cell['shell']},"
                    f"{top_cell['sign_word']}:{fmt_float(top_cell['bucket_abs_share'])}"
                )
            else:
                cell_text = "n/a"
            lines.append(
                f"| `{bucket['bucket']}` | `{row['pair_key']}` | {row['support_cell_count']} | "
                f"{fmt_float(row['top_cell_credit_share_of_pair'])} | "
                f"{fmt_float(row['top_three_credit_share_of_pair'])} | `{cell_text}` |"
            )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：pair 信用逐格支撑重新求和等于上一层 pair 信用。",
            "- 已定位：每个 bucket 的覆盖 pair 由哪些深度格支撑。",
            "- 未闭合：需要证明主导 pair 的支撑不变量，或登记 PairSupportDefect-PDEC。",
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
                "pair_cell_support_identity_closed": result["pair_cell_support_identity_closed"],
                "top_global_pair": result["global_pair_rows"][0]["pair_key"] if result["global_pair_rows"] else None,
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
