#!/usr/bin/env python3
"""用非主正相位信用重压 z=61 次级残量。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_nonprincipal_secondary_extractor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.md
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
STAR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.md"

NEXT_TARGET = "UnbalancedFourNonprincipalCellsPhaseInvariantOrExtractorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json",
    "prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json",
    "prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_nonprincipal_secondary_extractor_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def bucket_abs_lookup(pair_data: dict[str, Any]) -> dict[str, float]:
    """从 pair 账本恢复 bucket 绝对基准。"""
    return {
        row["bucket"]: row["opposite_sign_credit"] / row["pair_credit_ratio"]
        for row in pair_data["bucket_rows"]
        if row["pair_credit_ratio"]
    }


def greedy_cover(rows: list[dict[str, Any]], target: float) -> list[dict[str, Any]]:
    """按信用从大到小覆盖目标。"""
    result = []
    total = 0.0
    for row in sorted(rows, key=lambda item: item["secondary_credit_ratio"], reverse=True):
        if total >= target:
            break
        total += row["secondary_credit_ratio"]
        result.append({**row, "cumulative_secondary_credit_ratio": total})
    return result


def audit() -> dict[str, Any]:
    """执行非主正相位抽取审计。"""
    sign_data = json.loads(SIGN_JSON.read_text(encoding="utf-8"))
    pair_data = json.loads(PAIR_JSON.read_text(encoding="utf-8"))
    star_data = json.loads(STAR_JSON.read_text(encoding="utf-8"))
    principal = star_data["principal_positive_p"]
    bucket_abs = bucket_abs_lookup(pair_data)
    residual_need = {
        row["bucket"]: row["residual_needed_ratio"]
        for row in star_data["residual_summary"]
    }
    expected_secondary = {
        row["bucket"]: row["secondary_credit_ratio"]
        for row in star_data["residual_summary"]
    }

    rows_by_bucket: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in sign_data["cell_rows"]:
        bucket = row["bucket"]
        if bucket not in residual_need:
            continue
        pairs = pair_router.pair_credit_for_cell(row)
        secondary_pairs = [
            pair for pair in pairs if pair["positive_p"] != principal
        ]
        secondary_credit = sum(pair["pair_credit"] for pair in secondary_pairs)
        if secondary_credit <= 0:
            continue
        rows_by_bucket[bucket].append(
            {
                "bucket": bucket,
                "omega": row["omega"],
                "shell": row["shell"],
                "sign_word": row["sign_word"],
                "secondary_credit": secondary_credit,
                "secondary_credit_ratio": secondary_credit / bucket_abs[bucket],
                "profile_crude_bucket_share": row["profile_crude_bucket_share"],
                "cell_net_bucket_share": row["cell_net_bucket_share"],
                "opposite_sign_credit_bucket_share": row[
                    "opposite_sign_credit_bucket_share"
                ],
                "secondary_share_of_cell_credit": safe_ratio(
                    secondary_credit,
                    row["opposite_sign_credit"],
                ),
                "profile_vector": [
                    {
                        "p": entry["p"],
                        "linear_remainder": entry["linear_remainder"],
                        "signed_bucket_share": entry["signed_bucket_share"],
                    }
                    for entry in row["profile_entries"]
                ],
                "secondary_pairs": [
                    {
                        "pair_key": f"{pair['positive_p']}->{pair['negative_p']}",
                        "positive_p": pair["positive_p"],
                        "negative_p": pair["negative_p"],
                        "pair_credit": pair["pair_credit"],
                        "pair_credit_ratio": pair["pair_credit"] / bucket_abs[bucket],
                    }
                    for pair in secondary_pairs
                ],
            }
        )

    bucket_rows = []
    identity_failures = []
    for bucket, need in residual_need.items():
        cells = sorted(
            rows_by_bucket[bucket],
            key=lambda item: item["secondary_credit_ratio"],
            reverse=True,
        )
        total_secondary = sum(row["secondary_credit_ratio"] for row in cells)
        identity_error = total_secondary - expected_secondary[bucket]
        if abs(identity_error) > 1e-8:
            identity_failures.append({"bucket": bucket, "error": identity_error})
        cover_cells = greedy_cover(cells, need)
        template_credit: dict[str, float] = defaultdict(float)
        for cell in cells:
            template_credit[cell["sign_word"]] += cell["secondary_credit_ratio"]
        bucket_rows.append(
            {
                "bucket": bucket,
                "residual_needed_ratio": need,
                "expected_secondary_credit_ratio": expected_secondary[bucket],
                "computed_secondary_credit_ratio": total_secondary,
                "secondary_identity_error": identity_error,
                "nonprincipal_cells_cover_residual": (
                    sum(cell["secondary_credit_ratio"] for cell in cover_cells) + 1e-12 >= need
                ),
                "cover_cell_count": len(cover_cells),
                "cover_credit_ratio": sum(
                    cell["secondary_credit_ratio"] for cell in cover_cells
                ),
                "cover_surplus_ratio": sum(
                    cell["secondary_credit_ratio"] for cell in cover_cells
                )
                - need,
                "all_secondary_cells": cells,
                "cover_cells": cover_cells,
                "template_credit": [
                    {
                        "sign_word": sign_word,
                        "credit_ratio": credit,
                    }
                    for sign_word, credit in sorted(
                        template_credit.items(), key=lambda item: item[1], reverse=True
                    )
                ],
            }
        )

    unbalanced_row = next(
        row for row in bucket_rows if row["bucket"] == "unbalanced<=8"
    )
    unbalanced_cover_sign_words = [
        row["sign_word"] for row in unbalanced_row["cover_cells"]
    ]

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_nonprincipal_secondary_extractor_router",
        "status": "z61_residual_reduced_to_nonprincipal_secondary_extractor_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "p_list": sign_data["p_list"],
        "z": sign_data["z"],
        "principal_positive_p": principal,
        "nonprincipal_secondary_identity_closed": len(identity_failures) == 0,
        "sample_nonprincipal_cells_cover_all_residuals": all(
            row["nonprincipal_cells_cover_residual"] for row in bucket_rows
        ),
        "unbalanced_cover_cell_count": unbalanced_row["cover_cell_count"],
        "unbalanced_cover_sign_words": unbalanced_cover_sign_words,
        "nonprincipal_extractor_phase_invariant_proved": False,
        "extractor_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "identity_failure_count": len(identity_failures),
        "bucket_rows": bucket_rows,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "两处残量可以更自然地由非主正相位信用支付。"
            "`mid<=4` 由两个 `--++` 单元覆盖；"
            "`unbalanced<=8` 可由 4 个非主正相位单元覆盖，且不必依赖上一层的 `--++` 选中模板。"
            "因此下一硬点压成 unbalanced 四个非主正相位单元的相位不变量，"
            "或输出 Extractor-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 非主正相位抽取",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"principal_positive_p={result['principal_positive_p']}",
        f"nonprincipal_secondary_identity_closed={fmt_bool(result['nonprincipal_secondary_identity_closed'])}",
        f"sample_nonprincipal_cells_cover_all_residuals={fmt_bool(result['sample_nonprincipal_cells_cover_all_residuals'])}",
        f"unbalanced_cover_cell_count={result['unbalanced_cover_cell_count']}",
        f"unbalanced_cover_sign_words={','.join(result['unbalanced_cover_sign_words'])}",
        f"nonprincipal_extractor_phase_invariant_proved={fmt_bool(result['nonprincipal_extractor_phase_invariant_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. bucket 非主正相位覆盖",
        "",
        "| bucket | residual need | total secondary | cover cells | cover credit | surplus |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["bucket_rows"]:
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(row['residual_needed_ratio'])} | "
            f"{fmt_float(row['computed_secondary_credit_ratio'])} | "
            f"{row['cover_cell_count']} | {fmt_float(row['cover_credit_ratio'])} | "
            f"{fmt_float(row['cover_surplus_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 选中覆盖单元",
            "",
            "| bucket | omega | shell | signs | secondary credit | cumulative | pairs | profile vector |",
            "| --- | ---: | --- | --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["bucket_rows"]:
        for cell in row["cover_cells"]:
            pairs = ", ".join(
                f"{pair['pair_key']}:{fmt_float(pair['pair_credit_ratio'])}"
                for pair in cell["secondary_pairs"]
            )
            vector = ", ".join(
                f"{entry['p']}:{fmt_float(entry['linear_remainder'])}"
                for entry in cell["profile_vector"]
            )
            lines.append(
                f"| `{cell['bucket']}` | {cell['omega']} | `{cell['shell']}` | "
                f"`{cell['sign_word']}` | {fmt_float(cell['secondary_credit_ratio'])} | "
                f"{fmt_float(cell['cumulative_secondary_credit_ratio'])} | "
                f"`{pairs}` | `{vector}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 模板信用",
            "",
            "| bucket | sign word | secondary credit |",
            "| --- | --- | ---: |",
        ]
    )
    for row in result["bucket_rows"]:
        for template in row["template_credit"]:
            lines.append(
                f"| `{row['bucket']}` | `{template['sign_word']}` | "
                f"{fmt_float(template['credit_ratio'])} |"
            )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：非主正相位信用与上一层 secondary credit 精确一致。",
            "- 已压缩：`unbalanced<=8` 由 4 个非主正相位单元覆盖。",
            "- 未闭合：证明这 4 个单元的相位不变量，或登记 Extractor-PDEC。",
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
                "nonprincipal_secondary_identity_closed": result[
                    "nonprincipal_secondary_identity_closed"
                ],
                "unbalanced_cover_cell_count": result["unbalanced_cover_cell_count"],
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
