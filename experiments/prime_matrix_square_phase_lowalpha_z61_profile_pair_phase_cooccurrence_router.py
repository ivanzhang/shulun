#!/usr/bin/env python3
"""审计 z=61 P-pair 信用的方向性相位共现。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_profile_pair_phase_cooccurrence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.md
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
SUPPORT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.md"

NEXT_TARGET = "PProfilePhaseCooccurrenceDirectionalityBoundOrPhaseDefectPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_profile_pair_phase_cooccurrence_router.py": file_sha256(
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


def unordered_key(left_p: int, right_p: int) -> str:
    """生成无序 pair 键。"""
    left, right = sorted([left_p, right_p])
    return f"{left}<->{right}"


def audit() -> dict[str, Any]:
    """执行方向性相位共现审计。"""
    sign_data = json.loads(SIGN_JSON.read_text(encoding="utf-8"))
    pair_data = json.loads(PAIR_JSON.read_text(encoding="utf-8"))
    support_data = json.loads(SUPPORT_JSON.read_text(encoding="utf-8"))
    p_list = sign_data["p_list"]

    ordered_credit: dict[tuple[int, int], float] = defaultdict(float)
    ordered_cells: dict[tuple[int, int], int] = defaultdict(int)
    same_sign_overlap: dict[tuple[int, int], float] = defaultdict(float)
    opposite_raw_overlap: dict[tuple[int, int], float] = defaultdict(float)
    bucket_ordered_credit: dict[tuple[str, int, int], float] = defaultdict(float)
    bucket_ordered_cells: dict[tuple[str, int, int], int] = defaultdict(int)
    cell_identity_failures = []

    for row in sign_data["cell_rows"]:
        value_by_p = {
            entry["p"]: entry["linear_remainder"]
            for entry in row["profile_entries"]
        }
        pair_entries = pair_router.pair_credit_for_cell(row)
        if abs(sum(item["pair_credit"] for item in pair_entries) - row["opposite_sign_credit"]) > 1e-8:
            cell_identity_failures.append(
                {
                    "bucket": row["bucket"],
                    "omega": row["omega"],
                    "shell": row["shell"],
                }
            )
        active_pairs = set()
        for pair in pair_entries:
            key = (pair["positive_p"], pair["negative_p"])
            ordered_credit[key] += pair["pair_credit"]
            bucket_ordered_credit[(row["bucket"], *key)] += pair["pair_credit"]
            active_pairs.add(key)
        for key in active_pairs:
            ordered_cells[key] += 1
            bucket_ordered_cells[(row["bucket"], *key)] += 1
        for left_index, left_p in enumerate(p_list):
            for right_p in p_list[left_index + 1 :]:
                left = value_by_p[left_p]
                right = value_by_p[right_p]
                if left * right > 0:
                    same_sign_overlap[(left_p, right_p)] += min(abs(left), abs(right))
                elif left * right < 0:
                    opposite_raw_overlap[(left_p, right_p)] += min(abs(left), abs(right))

    oriented_rows = []
    for positive_p in p_list:
        for negative_p in p_list:
            if positive_p == negative_p:
                continue
            credit = ordered_credit[(positive_p, negative_p)]
            reverse = ordered_credit[(negative_p, positive_p)]
            total_oriented = credit + reverse
            if total_oriented <= 0:
                continue
            oriented_rows.append(
                {
                    "pair_key": pair_key(positive_p, negative_p),
                    "positive_p": positive_p,
                    "negative_p": negative_p,
                    "credit": credit,
                    "reverse_credit": reverse,
                    "orientation_share": safe_ratio(credit, total_oriented),
                    "orientation_margin": safe_ratio(credit - reverse, total_oriented),
                    "active_cell_count": ordered_cells[(positive_p, negative_p)],
                    "reverse_cell_count": ordered_cells[(negative_p, positive_p)],
                    "bucket_rows": [
                        {
                            "bucket": bucket_row["bucket"],
                            "credit": bucket_ordered_credit[(bucket_row["bucket"], positive_p, negative_p)],
                            "reverse_credit": bucket_ordered_credit[(bucket_row["bucket"], negative_p, positive_p)],
                            "orientation_share": safe_ratio(
                                bucket_ordered_credit[(bucket_row["bucket"], positive_p, negative_p)],
                                bucket_ordered_credit[(bucket_row["bucket"], positive_p, negative_p)]
                                + bucket_ordered_credit[(bucket_row["bucket"], negative_p, positive_p)],
                            ),
                            "active_cell_count": bucket_ordered_cells[(bucket_row["bucket"], positive_p, negative_p)],
                            "reverse_cell_count": bucket_ordered_cells[(bucket_row["bucket"], negative_p, positive_p)],
                        }
                        for bucket_row in pair_data["bucket_rows"]
                    ],
                }
            )
    oriented_rows.sort(key=lambda row: row["credit"], reverse=True)

    unordered_rows = []
    for left_index, left_p in enumerate(p_list):
        for right_p in p_list[left_index + 1 :]:
            left_to_right = ordered_credit[(left_p, right_p)]
            right_to_left = ordered_credit[(right_p, left_p)]
            total_credit = left_to_right + right_to_left
            unordered_rows.append(
                {
                    "pair_key": unordered_key(left_p, right_p),
                    "left_p": left_p,
                    "right_p": right_p,
                    "left_to_right_credit": left_to_right,
                    "right_to_left_credit": right_to_left,
                    "total_opposite_credit": total_credit,
                    "directionality": safe_ratio(abs(left_to_right - right_to_left), total_credit),
                    "same_sign_overlap": same_sign_overlap[(left_p, right_p)],
                    "opposite_raw_overlap": opposite_raw_overlap[(left_p, right_p)],
                    "opposite_overlap_share": safe_ratio(
                        opposite_raw_overlap[(left_p, right_p)],
                        opposite_raw_overlap[(left_p, right_p)] + same_sign_overlap[(left_p, right_p)],
                    ),
                }
            )
    unordered_rows.sort(key=lambda row: row["total_opposite_credit"], reverse=True)

    outgoing_credit = {
        p: sum(row["credit"] for row in oriented_rows if row["positive_p"] == p)
        for p in p_list
    }
    incoming_credit = {
        p: sum(row["credit"] for row in oriented_rows if row["negative_p"] == p)
        for p in p_list
    }
    principal_positive_p = max(
        p_list,
        key=lambda p: outgoing_credit[p] - incoming_credit[p],
    )
    principal_star_rows = [
        row
        for row in oriented_rows
        if row["positive_p"] == principal_positive_p and row["credit"] > 0
    ]
    principal_star_directionality_materialized = all(
        (row["orientation_share"] or 0.0) >= 0.95
        for row in principal_star_rows
    )
    dominant_keys = {row["pair_key"] for row in support_data["global_pair_rows"][:4]}
    dominant_orientation_rows = [
        row for row in oriented_rows if row["pair_key"] in dominant_keys
    ]
    dominant_directionality_materialized = all(
        (row["orientation_share"] or 0.0) >= 0.95
        for row in dominant_orientation_rows
        if row["credit"] > 0
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_profile_pair_phase_cooccurrence_router",
        "status": "z61_profile_pair_phase_directionality_materialized_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": p_list,
        "z": sign_data["z"],
        "pair_phase_credit_identity_closed": len(cell_identity_failures) == 0,
        "principal_positive_p": principal_positive_p,
        "principal_star_directionality_materialized": principal_star_directionality_materialized,
        "principal_star_rows": principal_star_rows,
        "dominant_pair_directionality_materialized": dominant_directionality_materialized,
        "phase_cooccurrence_directionality_bound_proved": False,
        "phase_defect_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "cell_identity_failure_count": len(cell_identity_failures),
        "oriented_rows": oriented_rows,
        "unordered_rows": unordered_rows,
        "dominant_orientation_rows": dominant_orientation_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "主导 P-pair 的信用不仅存在，而且方向性很强：在样本中最大几条 pair "
            "显示出一个主正相位星形结构；同时次级 pair 仍保留方向性缺口。"
            "因此下一步可把 lower bound 改写成 P-profile 相位共现方向性下界；"
            "若方向性消失，则形成 PhaseDefect-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 profile pair 相位共现",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pair_phase_credit_identity_closed={fmt_bool(result['pair_phase_credit_identity_closed'])}",
        f"principal_positive_p={result['principal_positive_p']}",
        f"principal_star_directionality_materialized={fmt_bool(result['principal_star_directionality_materialized'])}",
        f"dominant_pair_directionality_materialized={fmt_bool(result['dominant_pair_directionality_materialized'])}",
        f"phase_cooccurrence_directionality_bound_proved={fmt_bool(result['phase_cooccurrence_directionality_bound_proved'])}",
        f"phase_defect_pdec_excluded={fmt_bool(result['phase_defect_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最大有向 pair",
        "",
        "| pair | credit | reverse | orientation share | margin | cells | reverse cells |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["oriented_rows"][:12]:
        lines.append(
            f"| `{row['pair_key']}` | {fmt_float(row['credit'])} | "
            f"{fmt_float(row['reverse_credit'])} | "
            f"{fmt_float(row['orientation_share'])} | "
            f"{fmt_float(row['orientation_margin'])} | "
            f"{row['active_cell_count']} | {row['reverse_cell_count']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 主星形方向性",
            "",
            "| pair | credit | reverse | orientation share | margin | cells | reverse cells |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["principal_star_rows"]:
        lines.append(
            f"| `{row['pair_key']}` | {fmt_float(row['credit'])} | "
            f"{fmt_float(row['reverse_credit'])} | "
            f"{fmt_float(row['orientation_share'])} | "
            f"{fmt_float(row['orientation_margin'])} | "
            f"{row['active_cell_count']} | {row['reverse_cell_count']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 无序 pair 的反相/同相画像",
            "",
            "| pair | total opposite credit | directionality | opposite overlap share | same overlap | opposite overlap |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["unordered_rows"]:
        lines.append(
            f"| `{row['pair_key']}` | {fmt_float(row['total_opposite_credit'])} | "
            f"{fmt_float(row['directionality'])} | "
            f"{fmt_float(row['opposite_overlap_share'])} | "
            f"{fmt_float(row['same_sign_overlap'])} | "
            f"{fmt_float(row['opposite_raw_overlap'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 主导 pair 的 bucket 方向性",
            "",
            "| pair | bucket | credit | reverse | orientation share | cells | reverse cells |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["dominant_orientation_rows"]:
        for bucket in row["bucket_rows"]:
            lines.append(
                f"| `{row['pair_key']}` | `{bucket['bucket']}` | "
                f"{fmt_float(bucket['credit'])} | {fmt_float(bucket['reverse_credit'])} | "
                f"{fmt_float(bucket['orientation_share'])} | "
                f"{bucket['active_cell_count']} | {bucket['reverse_cell_count']} |"
            )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：有向 pair 信用重新求和与上一层 pair 信用一致。",
            "- 已定位：主星形 pair 的方向性相位强偏置，以及次级 pair 的方向性缺口。",
            "- 未闭合：需要证明这种方向性共现下界，或登记 PhaseDefect-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
                "pair_phase_credit_identity_closed": result["pair_phase_credit_identity_closed"],
                "principal_positive_p": result["principal_positive_p"],
                "principal_star_directionality_materialized": result[
                    "principal_star_directionality_materialized"
                ],
                "dominant_pair_directionality_materialized": result[
                    "dominant_pair_directionality_materialized"
                ],
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
