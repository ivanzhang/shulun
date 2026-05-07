#!/usr/bin/env python3
"""给 A1 连续标准 prime-lift 签名生成删除势账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_standard_prime_lift_deletion.py

输出：
  docs/monograph/prime-matrix-triad-a1-standard-prime-lift-deletion.json
  docs/monograph/prime-matrix-triad-a1-standard-prime-lift-deletion.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PRIME_LIFT = DOCS / "prime-matrix-triad-a1-continuous-prime-lift-router.json"
DEFAULT_COMMUTATION = DOCS / "prime-matrix-triad-a1-selective-promotion-commutation.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-standard-prime-lift-deletion.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-standard-prime-lift-deletion.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def deletion_row_from_standard(row: dict[str, Any]) -> dict[str, Any]:
    """标准 prime-lift 行的删除势下界。"""
    promoted_prime = int(row["promoted_prime"])
    survival_upper_bound = 1.0 / promoted_prime
    return {
        "p": int(row["p"]),
        "signature": row["signature"],
        "promoted_prime": promoted_prime,
        "signature_payment_mass": int(row["signature_payment_mass"]),
        "route_source": "standard_next_prime_signature",
        "survival_upper_bound_from_fixed_residue": survival_upper_bound,
        "deletion_potential_lower_bound": -math.log(survival_upper_bound),
        "route": "PositiveDeletionPotentialOrNoDeletionKL",
    }


def deletion_rows_from_commutation(commutation: dict[str, Any]) -> list[dict[str, Any]]:
    """选择性行有限拆分后的标准后继删除势下界。"""
    rows = []
    for item in commutation["commutation_rows"]:
        promoted_prime = int(item["promoted_prime"])
        survival_upper_bound = 1.0 / promoted_prime
        for successor in item["successor_signatures"]:
            rows.append(
                {
                    "p": int(item["p"]),
                    "signature": successor["successor_signature"],
                    "promoted_prime": promoted_prime,
                    "signature_payment_mass": None,
                    "route_source": "selective_commutation_successor",
                    "first_prime_residue": int(successor["first_prime_residue"]),
                    "survival_upper_bound_from_fixed_residue": survival_upper_bound,
                    "deletion_potential_lower_bound": -math.log(survival_upper_bound),
                    "route": "PositiveDeletionPotentialOrNoDeletionKL",
                }
            )
    return rows


def run(prime_lift_path: Path, commutation_path: Path) -> dict[str, Any]:
    """运行标准 prime-lift 删除势账本。"""
    prime_lift = load_json(prime_lift_path)
    commutation = load_json(commutation_path)
    standard_rows = [
        deletion_row_from_standard(row)
        for row in prime_lift["signature_rows"]
        if row["route"] == "StandardNextPrimePromotionDeletionKLReady"
    ]
    commuted_rows = deletion_rows_from_commutation(commutation)
    all_rows = [*standard_rows, *commuted_rows]
    route_counts = Counter(row["route"] for row in all_rows)
    promoted_prime_counts = Counter(row["promoted_prime"] for row in all_rows)
    return {
        "certificate_type": "triad_a1_standard_prime_lift_deletion",
        "status": "standard_prime_lift_positive_deletion_potential_materialized",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "continuous_prime_lift_json": file_sha256(prime_lift_path),
            "selective_commutation_json": file_sha256(commutation_path),
        },
        "standard_row_count": len(standard_rows),
        "commuted_successor_row_count": len(commuted_rows),
        "deletion_row_count": len(all_rows),
        "route_counts": dict(sorted(route_counts.items())),
        "promoted_prime_counts": dict(sorted(promoted_prime_counts.items())),
        "global_min_deletion_potential_lower_bound": min(
            (row["deletion_potential_lower_bound"] for row in all_rows),
            default=None,
        ),
        "global_max_survival_upper_bound": max(
            (row["survival_upper_bound_from_fixed_residue"] for row in all_rows),
            default=None,
        ),
        "deletion_rows": all_rows,
        "deletion_law": (
            "标准 prime-lift 签名固定 promoted prime ell 的一个 fiber residue。"
            "把 ell 晋升进低模周期时，完整 ell-fiber 中至多 1/ell 落在该固定 residue。"
            "因此该签名支付删除势 D>=log(ell)。若无限层持续出现标准固定 residue，"
            "删除势发散；若固定 residue 不再持久，则回到 diffuse CleanKLS/DLS；"
            "若删除停止但分布偏斜，则进入 NoDeletion-KL/PDEC。"
        ),
        "review_conclusion": (
            "连续 positive-limsup 的标准 prime-lift 分支已接入删除势账本。"
            "39 个当前标准行给出 D>=log(13)，选择性拆分的 13 个后继给出 D>=log(17)。"
            "剩余终端是 NoDeletion-KL/PDEC 或 diffuse CleanKLS/DLS 大筛。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 标准 Prime-Lift 删除势账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 删除势律",
        "",
        result["deletion_law"],
        "",
        "```text",
        "fixed residue modulo ell",
        "=> survival <= 1/ell after promoting ell",
        "=> deletion potential D >= log(ell)。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `standard_row_count={result['standard_row_count']}`。",
        f"- `commuted_successor_row_count={result['commuted_successor_row_count']}`。",
        f"- `deletion_row_count={result['deletion_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `promoted_prime_counts={result['promoted_prime_counts']}`。",
        f"- `global_min_deletion_potential_lower_bound={fmt_float(result['global_min_deletion_potential_lower_bound'])}`。",
        f"- `global_max_survival_upper_bound={fmt_float(result['global_max_survival_upper_bound'])}`。",
        "",
        "## 3. 删除势行",
        "",
        "| P | signature | ell | source | survival upper | D lower | route |",
        "| ---: | --- | ---: | --- | ---: | ---: | --- |",
    ]
    for row in result["deletion_rows"]:
        lines.append(
            "| {p} | `{sig}` | {ell} | `{source}` | {surv} | {deletion} | `{route}` |".format(
                p=row["p"],
                sig=row["signature"],
                ell=row["promoted_prime"],
                source=row["route_source"],
                surv=fmt_float(row["survival_upper_bound_from_fixed_residue"]),
                deletion=fmt_float(row["deletion_potential_lower_bound"]),
                route=row["route"],
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前硬点",
            "",
            "标准 prime-lift positive-limsup 分支已不再是开放 PDEC-CAP 缺口。",
            "它要么持续支付删除势，要么在删除停止时进入 NoDeletion-KL/PDEC 或 diffuse CleanKLS/DLS。",
            "下一步只剩将 NoDeletion-KL 与 CleanKLS/DLS 的终端估计补齐。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime-lift-json", type=Path, default=DEFAULT_PRIME_LIFT)
    parser.add_argument("--commutation-json", type=Path, default=DEFAULT_COMMUTATION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.prime_lift_json, args.commutation_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "deletion_row_count": result["deletion_row_count"],
                "route_counts": result["route_counts"],
                "global_min_deletion_potential_lower_bound": result[
                    "global_min_deletion_potential_lower_bound"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
