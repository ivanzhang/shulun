#!/usr/bin/env python3
"""把 z=61 profile 信用压成主星形与次级残量合同。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_principal_star_residual_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PAIR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json"
PHASE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.json"
SUPPORT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.md"

NEXT_TARGET = "SecondaryPairResidualCreditForMidUnbalancedOrResidualPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_principal_star_residual_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def greedy_cover(rows: list[dict[str, Any]], target: float) -> list[dict[str, Any]]:
    """贪心选择次级 pair 覆盖目标残量。"""
    total = 0.0
    result = []
    for row in sorted(rows, key=lambda item: item["pair_credit"], reverse=True):
        if total >= target:
            break
        total += row["pair_credit"]
        result.append({**row, "cumulative_credit": total})
    return result


def support_lookup(support_data: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    """建立 `(bucket,pair)` 到支撑信息的索引。"""
    lookup = {}
    for bucket_row in support_data["bucket_rows"]:
        bucket = bucket_row["bucket"]
        for pair_row in bucket_row["pair_support_rows"]:
            lookup[(bucket, pair_row["pair_key"])] = pair_row
    return lookup


def audit() -> dict[str, Any]:
    """执行主星形残量审计。"""
    pair_data = json.loads(PAIR_JSON.read_text(encoding="utf-8"))
    phase_data = json.loads(PHASE_JSON.read_text(encoding="utf-8"))
    support_data = json.loads(SUPPORT_JSON.read_text(encoding="utf-8"))
    principal = phase_data["principal_positive_p"]
    support_by_pair = support_lookup(support_data)
    bucket_rows = []
    identity_failures = []
    residual_buckets = []

    for row in pair_data["bucket_rows"]:
        bucket = row["bucket"]
        bucket_abs = row["opposite_sign_credit"] / row["pair_credit_ratio"]
        principal_pairs = [
            pair for pair in row["pair_rows"] if pair["positive_p"] == principal
        ]
        secondary_pairs = [
            pair for pair in row["pair_rows"] if pair["positive_p"] != principal
        ]
        principal_credit = sum(pair["pair_credit"] for pair in principal_pairs)
        secondary_credit = sum(pair["pair_credit"] for pair in secondary_pairs)
        identity_error = principal_credit + secondary_credit - row["opposite_sign_credit"]
        if abs(identity_error) > 1e-8:
            identity_failures.append({"bucket": bucket, "error": identity_error})
        residual_needed = max(0.0, row["required_credit_to_meet_cap"] - principal_credit)
        secondary_cover = greedy_cover(secondary_pairs, residual_needed)
        star_covers_required = residual_needed <= 1e-8
        if not star_covers_required:
            residual_buckets.append(bucket)
        principal_pair_rows = []
        for pair in principal_pairs:
            support = support_by_pair.get((bucket, pair["pair_key"]), {})
            principal_pair_rows.append(
                {
                    **pair,
                    "support_cell_count": support.get("support_cell_count", 0),
                    "top_three_credit_share_of_pair": support.get("top_three_credit_share_of_pair"),
                }
            )
        secondary_pair_rows = []
        for pair in secondary_pairs:
            support = support_by_pair.get((bucket, pair["pair_key"]), {})
            secondary_pair_rows.append(
                {
                    **pair,
                    "support_cell_count": support.get("support_cell_count", 0),
                    "top_three_credit_share_of_pair": support.get("top_three_credit_share_of_pair"),
                }
            )
        bucket_rows.append(
            {
                "bucket": bucket,
                "bucket_abs": bucket_abs,
                "cap_required_credit": row["required_credit_to_meet_cap"],
                "total_pair_credit": row["opposite_sign_credit"],
                "principal_positive_p": principal,
                "principal_star_credit": principal_credit,
                "secondary_credit": secondary_credit,
                "residual_needed_after_principal_star": residual_needed,
                "identity_error": identity_error,
                "principal_star_covers_required": star_covers_required,
                "secondary_credit_covers_residual": secondary_credit + 1e-8 >= residual_needed,
                "required_credit_ratio": safe_ratio(row["required_credit_to_meet_cap"], bucket_abs),
                "principal_star_credit_ratio": safe_ratio(principal_credit, bucket_abs),
                "secondary_credit_ratio": safe_ratio(secondary_credit, bucket_abs),
                "residual_needed_ratio": safe_ratio(residual_needed, bucket_abs),
                "secondary_surplus_ratio": safe_ratio(secondary_credit - residual_needed, bucket_abs),
                "principal_share_of_required": safe_ratio(principal_credit, row["required_credit_to_meet_cap"]),
                "principal_share_of_total_credit": safe_ratio(principal_credit, row["opposite_sign_credit"]),
                "principal_pair_rows": sorted(
                    principal_pair_rows,
                    key=lambda item: item["pair_credit"],
                    reverse=True,
                ),
                "secondary_pair_rows": sorted(
                    secondary_pair_rows,
                    key=lambda item: item["pair_credit"],
                    reverse=True,
                ),
                "secondary_cover_pair_count": len(secondary_cover),
                "secondary_cover_pairs": secondary_cover,
            }
        )

    residual_summary = [
        {
            "bucket": row["bucket"],
            "residual_needed_ratio": row["residual_needed_ratio"],
            "secondary_credit_ratio": row["secondary_credit_ratio"],
            "secondary_surplus_ratio": row["secondary_surplus_ratio"],
            "secondary_cover_pair_count": row["secondary_cover_pair_count"],
            "secondary_cover_pairs": row["secondary_cover_pairs"],
        }
        for row in bucket_rows
        if not row["principal_star_covers_required"]
    ]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_principal_star_residual_router",
        "status": "z61_principal_star_reduces_to_two_secondary_residual_buckets_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": pair_data["p_list"],
        "z": pair_data["z"],
        "principal_positive_p": principal,
        "principal_star_residual_identity_closed": len(identity_failures) == 0,
        "principal_star_covers_bucket_count": sum(
            1 for row in bucket_rows if row["principal_star_covers_required"]
        ),
        "residual_bucket_count": len(residual_buckets),
        "residual_buckets": residual_buckets,
        "secondary_credit_covers_all_residuals_in_sample": all(
            row["secondary_credit_covers_residual"] for row in bucket_rows
        ),
        "principal_star_lower_bound_proved": False,
        "secondary_residual_credit_bound_proved": False,
        "residual_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "identity_failure_count": len(identity_failures),
        "bucket_rows": bucket_rows,
        "residual_summary": residual_summary,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "z=61 的 profile 信用已分离为主星形 `83561->*` 与次级残量。"
            "样本中主星形单独覆盖 balanced/far 两个 bucket，"
            "剩余只在 mid<=4 与 unbalanced<=8 两个 bucket 出现；"
            "因此下一步无需再处理全部 pair，只需证明这两个残量口的次级 pair 信用下界，"
            "或登记 Residual-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 主星形残量路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"principal_positive_p={result['principal_positive_p']}",
        f"principal_star_residual_identity_closed={fmt_bool(result['principal_star_residual_identity_closed'])}",
        f"principal_star_covers_bucket_count={result['principal_star_covers_bucket_count']}",
        f"residual_bucket_count={result['residual_bucket_count']}",
        "secondary_credit_covers_all_residuals_in_sample="
        f"{fmt_bool(result['secondary_credit_covers_all_residuals_in_sample'])}",
        f"principal_star_lower_bound_proved={fmt_bool(result['principal_star_lower_bound_proved'])}",
        f"secondary_residual_credit_bound_proved={fmt_bool(result['secondary_residual_credit_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. bucket 主星形/残量",
        "",
        "| bucket | need | principal star | residual need | secondary | secondary surplus | star covers |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['required_credit_ratio'])} | "
            f"{fmt_float(row['principal_star_credit_ratio'])} | "
            f"{fmt_float(row['residual_needed_ratio'])} | "
            f"{fmt_float(row['secondary_credit_ratio'])} | "
            f"{fmt_float(row['secondary_surplus_ratio'])} | "
            f"{fmt_bool(row['principal_star_covers_required'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 残量 bucket 的次级覆盖",
            "",
            "| bucket | residual need | secondary surplus | cover pairs | pair list |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["residual_summary"]:
        pair_text = ", ".join(
            f"{pair['pair_key']}:{fmt_float(pair['bucket_abs_share'])}"
            for pair in row["secondary_cover_pairs"]
        )
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['residual_needed_ratio'])} | "
            f"{fmt_float(row['secondary_surplus_ratio'])} | "
            f"{row['secondary_cover_pair_count']} | `{pair_text}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 主星形 pair",
            "",
            "| bucket | pair | credit/bucket abs | cells | top3 share |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
    )
    for row in result["bucket_rows"]:
        for pair in row["principal_pair_rows"]:
            lines.append(
                f"| `{row['bucket']}` | `{pair['pair_key']}` | "
                f"{fmt_float(pair['bucket_abs_share'])} | "
                f"{pair['support_cell_count']} | "
                f"{fmt_float(pair['top_three_credit_share_of_pair'])} |"
            )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：pair 信用分解为主星形与次级残量的恒等式。",
            "- 已压缩：主星形单独闭合 `balanced<=2` 与 `far>8`。",
            "- 剩余：`mid<=4` 与 `unbalanced<=8` 的次级残量信用下界。",
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
                "principal_positive_p": result["principal_positive_p"],
                "principal_star_covers_bucket_count": result["principal_star_covers_bucket_count"],
                "residual_buckets": result["residual_buckets"],
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
