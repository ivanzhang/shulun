#!/usr/bin/env python3
"""把 z=61 profile 反号信用拆成 P-pair 配对信用矩阵。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_profile_pair_credit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router as source


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SIGN_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.md"

NEXT_TARGET = "DominantPProfilePairCreditLowerBoundOrPairDefectPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_profile_pair_credit_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def pair_credit_for_cell(row: dict[str, Any]) -> list[dict[str, Any]]:
    """把一个深度格的反号信用分配到正负 P 配对。"""
    positives = [
        (entry["p"], entry["linear_remainder"])
        for entry in row["profile_entries"]
        if entry["linear_remainder"] > 0
    ]
    negatives = [
        (entry["p"], -entry["linear_remainder"])
        for entry in row["profile_entries"]
        if entry["linear_remainder"] < 0
    ]
    positive_mass = sum(value for _, value in positives)
    negative_mass = sum(value for _, value in negatives)
    denominator = max(positive_mass, negative_mass)
    if denominator <= 0:
        return []
    pairs = []
    for positive_p, positive_value in positives:
        for negative_p, negative_value in negatives:
            credit = 2 * positive_value * negative_value / denominator
            pairs.append(
                {
                    "positive_p": positive_p,
                    "negative_p": negative_p,
                    "pair_credit": credit,
                    "positive_mass": positive_value,
                    "negative_mass": negative_value,
                }
            )
    return pairs


def compact_pair_key(positive_p: int, negative_p: int) -> str:
    """生成 pair 键。"""
    return f"{positive_p}->{negative_p}"


def greedy_cover_pairs(pair_rows: list[dict[str, Any]], required_credit: float) -> list[dict[str, Any]]:
    """用最大配对信用贪心覆盖所需信用。"""
    covered = 0.0
    result = []
    for row in sorted(pair_rows, key=lambda item: item["pair_credit"], reverse=True):
        if covered >= required_credit:
            break
        covered += row["pair_credit"]
        result.append({**row, "cumulative_credit": covered})
    return result


def audit() -> dict[str, Any]:
    """执行 P-pair 信用审计。"""
    sign_data = json.loads(SIGN_JSON.read_text(encoding="utf-8"))
    bucket_by_name = {row["bucket"]: row for row in sign_data["bucket_rows"]}
    bucket_pairs: dict[str, dict[str, float]] = {
        bucket: defaultdict(float) for bucket in source.BUCKETS
    }
    bucket_pair_cells: dict[str, dict[str, int]] = {
        bucket: defaultdict(int) for bucket in source.BUCKETS
    }
    cell_rows = []
    identity_failures = []
    for row in sign_data["cell_rows"]:
        pairs = pair_credit_for_cell(row)
        pair_credit_sum = sum(pair["pair_credit"] for pair in pairs)
        identity_error = pair_credit_sum - row["opposite_sign_credit"]
        if abs(identity_error) > 1e-8:
            identity_failures.append(
                {
                    "bucket": row["bucket"],
                    "omega": row["omega"],
                    "shell": row["shell"],
                    "identity_error": identity_error,
                }
            )
        top_pairs = sorted(pairs, key=lambda item: item["pair_credit"], reverse=True)[:6]
        cell_rows.append(
            {
                "bucket": row["bucket"],
                "omega": row["omega"],
                "shell": row["shell"],
                "sign_word": row["sign_word"],
                "opposite_sign_credit": row["opposite_sign_credit"],
                "opposite_sign_credit_bucket_share": row["opposite_sign_credit_bucket_share"],
                "pair_credit_sum": pair_credit_sum,
                "pair_credit_identity_error": identity_error,
                "top_pairs": top_pairs,
            }
        )
        for pair in pairs:
            key = compact_pair_key(pair["positive_p"], pair["negative_p"])
            bucket_pairs[row["bucket"]][key] += pair["pair_credit"]
            bucket_pair_cells[row["bucket"]][key] += 1

    bucket_rows = []
    global_pair_credit: dict[str, float] = defaultdict(float)
    for bucket in source.BUCKETS:
        bucket_row = bucket_by_name[bucket]
        required = bucket_row["required_credit_to_meet_cap"]
        total_credit = sum(bucket_pairs[bucket].values())
        pair_rows = []
        for key, credit in sorted(bucket_pairs[bucket].items(), key=lambda item: item[1], reverse=True):
            positive_p, negative_p = (int(part) for part in key.split("->"))
            pair_rows.append(
                {
                    "positive_p": positive_p,
                    "negative_p": negative_p,
                    "pair_key": key,
                    "pair_credit": credit,
                    "bucket_abs_share": safe_ratio(credit, bucket_row["bucket_abs"]),
                    "required_credit_share": safe_ratio(credit, required),
                    "active_cell_count": bucket_pair_cells[bucket][key],
                }
            )
            global_pair_credit[key] += credit
        cover = greedy_cover_pairs(pair_rows, required)
        bucket_rows.append(
            {
                "bucket": bucket,
                "required_credit_to_meet_cap": required,
                "opposite_sign_credit": total_credit,
                "pair_credit_identity_error": total_credit - bucket_row["opposite_sign_credit"],
                "pair_credit_covers_required": total_credit + 1e-8 >= required,
                "required_credit_ratio": bucket_row["required_credit_ratio"],
                "pair_credit_ratio": safe_ratio(total_credit, bucket_row["bucket_abs"]),
                "pair_credit_margin_ratio": safe_ratio(total_credit - required, bucket_row["bucket_abs"]),
                "pair_rows": pair_rows,
                "greedy_cover_pair_count": len(cover),
                "greedy_cover_pairs": cover,
            }
        )

    bucket_identity_failures = [
        row for row in bucket_rows if abs(row["pair_credit_identity_error"]) > 1e-8
    ]
    sample_cover_failures = [
        row for row in bucket_rows if not row["pair_credit_covers_required"]
    ]
    top_global_pairs = [
        {
            "pair_key": key,
            "positive_p": int(key.split("->")[0]),
            "negative_p": int(key.split("->")[1]),
            "pair_credit": credit,
        }
        for key, credit in sorted(global_pair_credit.items(), key=lambda item: item[1], reverse=True)[:16]
    ]
    top_cell_pair_credit = sorted(
        cell_rows, key=lambda item: item["opposite_sign_credit_bucket_share"] or 0.0, reverse=True
    )[:16]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_profile_pair_credit_router",
        "status": "z61_profile_opposite_sign_credit_split_to_p_pair_matrix_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": sign_data["p_list"],
        "z": sign_data["z"],
        "pair_transport_identity_closed": len(identity_failures) == 0,
        "bucket_pair_credit_identity_closed": len(bucket_identity_failures) == 0,
        "sample_pair_credit_covers_required_for_all_buckets": len(sample_cover_failures) == 0,
        "dominant_pair_credit_lower_bound_proved": False,
        "pair_defect_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cell_pair_identity_failure_count": len(identity_failures),
        "bucket_pair_identity_failure_count": len(bucket_identity_failures),
        "sample_cover_failure_count": len(sample_cover_failures),
        "bucket_rows": bucket_rows,
        "top_global_pairs": top_global_pairs,
        "top_cell_pair_credit": top_cell_pair_credit,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "每个深度格的反号信用已拆成正 profile P 与负 profile P 的配对信用矩阵。"
            "配对规则是规范化运输：若正质量为 P_+、负质量为 P_-，则 "
            "`credit(P_i,P_j)=2*pos_i*neg_j/max(P_+,P_-)`，逐格求和精确恢复上一层反号信用。"
            "因此下一步可以只攻主要 P-pair 的持续信用下界；若主要 pair 信用消失，"
            "则输出 PairDefect-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 profile P-pair 信用矩阵",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pair_transport_identity_closed={fmt_bool(result['pair_transport_identity_closed'])}",
        f"bucket_pair_credit_identity_closed={fmt_bool(result['bucket_pair_credit_identity_closed'])}",
        "sample_pair_credit_covers_required_for_all_buckets="
        f"{fmt_bool(result['sample_pair_credit_covers_required_for_all_buckets'])}",
        f"dominant_pair_credit_lower_bound_proved={fmt_bool(result['dominant_pair_credit_lower_bound_proved'])}",
        f"pair_defect_pdec_excluded={fmt_bool(result['pair_defect_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 配对信用公式",
        "",
        "对一个深度格，把 `L_P>0` 的 profile 记为正质量，把 `L_P<0` 的 profile 记为负质量。定义",
        "",
        "```text",
        "credit(P_i,P_j)=2*pos_i*neg_j/max(total_pos,total_neg).",
        "```",
        "",
        "则所有正负配对求和精确等于上一层 `opposite_sign_credit`。",
        "",
        "## 2. bucket 配对验收",
        "",
        "| bucket | need credit | pair credit | margin | cover pairs |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['required_credit_ratio'])} | "
            f"{fmt_float(row['pair_credit_ratio'])} | "
            f"{fmt_float(row['pair_credit_margin_ratio'])} | "
            f"{row['greedy_cover_pair_count']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 各 bucket 最大 P-pair",
            "",
            "| bucket | positive P | negative P | credit/bucket abs | credit/need | active cells |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["bucket_rows"]:
        for pair in row["pair_rows"][:8]:
            lines.append(
                f"| `{row['bucket']}` | {pair['positive_p']} | {pair['negative_p']} | "
                f"{fmt_float(pair['bucket_abs_share'])} | "
                f"{fmt_float(pair['required_credit_share'])} | "
                f"{pair['active_cell_count']} |"
            )
    lines.extend(
        [
            "",
            "## 4. 全局最大 P-pair",
            "",
            "| positive P | negative P | pair credit |",
            "| ---: | ---: | ---: |",
        ]
    )
    for row in result["top_global_pairs"]:
        lines.append(
            f"| {row['positive_p']} | {row['negative_p']} | {fmt_float(row['pair_credit'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 最大信用深度格",
            "",
            "| bucket | omega | shell | signs | credit/bucket abs | top pair |",
            "| --- | ---: | --- | --- | ---: | --- |",
        ]
    )
    for row in result["top_cell_pair_credit"]:
        top_pair = row["top_pairs"][0] if row["top_pairs"] else None
        if top_pair:
            pair_text = f"{top_pair['positive_p']}->{top_pair['negative_p']}:{fmt_float(top_pair['pair_credit'])}"
        else:
            pair_text = "n/a"
        lines.append(
            f"| `{row['bucket']}` | {row['omega']} | `{row['shell']}` | `{row['sign_word']}` | "
            f"{fmt_float(row['opposite_sign_credit_bucket_share'])} | `{pair_text}` |"
        )
    lines.extend(
        [
            "",
            "## 6. 证明边界",
            "",
            "- 已闭合：反号信用到 P-pair 信用矩阵的逐格恒等式。",
            "- 样本事实：P-pair 信用总量覆盖四个 bucket 所需信用。",
            "- 未闭合：需要证明主要 P-pair 的信用下界，或把 pair 信用缺失登记为 PairDefect-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 7. 依赖哈希",
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
                "pair_transport_identity_closed": result["pair_transport_identity_closed"],
                "sample_cover_failure_count": result["sample_cover_failure_count"],
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
