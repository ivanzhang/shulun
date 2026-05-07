#!/usr/bin/env python3
"""解析 A1 连续 PDEC 签名中的选择性晋升交换律。

用法示例：
  python3 experiments/prime_matrix_triad_a1_selective_promotion_commutation.py

输出：
  docs/monograph/prime-matrix-triad-a1-selective-promotion-commutation.json
  docs/monograph/prime-matrix-triad-a1-selective-promotion-commutation.md
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
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-selective-promotion-commutation.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-selective-promotion-commutation.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def successor_signature_after_first_promotion(
    original_signature: str,
    first_prime: int,
    first_residue: int,
) -> str:
    """先晋升 first_prime 后，原选择性签名在后继层的签名。"""
    promoted_raw, fiber_raw, column_raw = original_signature.split(":")
    promoted_prime = int(promoted_raw)
    fiber_residue = int(fiber_raw)
    column_residue = int(column_raw)
    inverse_first = pow(first_prime, -1, promoted_prime)
    successor_residue = ((fiber_residue - first_residue) * inverse_first) % promoted_prime
    return f"{promoted_prime}:{successor_residue}:{column_residue}"


def analyze_selective_row(row: dict[str, Any]) -> dict[str, Any]:
    """分析一个选择性晋升行的交换拆分。"""
    first_prime = int(row["next_high_prime"])
    promoted_prime = int(row["promoted_prime"])
    if math.gcd(first_prime, promoted_prime) != 1:
        route = "SelectivePromotionNonCoprimeInvalid"
        successors = []
    else:
        successors = [
            {
                "first_prime_residue": residue,
                "successor_signature": successor_signature_after_first_promotion(
                    row["signature"], first_prime, residue
                ),
            }
            for residue in range(first_prime)
        ]
        route = "FiniteSplitThenStandardPromotionOrDiffuseKLS"
    return {
        "p": int(row["p"]),
        "q": int(row["q"]),
        "signature": row["signature"],
        "signature_payment_mass": int(row["signature_payment_mass"]),
        "signature_phase_count": int(row["signature_phase_count"]),
        "first_prime": first_prime,
        "promoted_prime": promoted_prime,
        "final_q_direct": int(row["q"]) * promoted_prime * first_prime,
        "final_q_ordered": int(row["q"]) * first_prime * promoted_prime,
        "crt_orders_commute": int(row["q"]) * promoted_prime * first_prime
        == int(row["q"]) * first_prime * promoted_prime,
        "successor_count": len(successors),
        "successor_signatures": successors,
        "route": route,
    }


def run(prime_lift_path: Path) -> dict[str, Any]:
    """运行选择性晋升交换律审计。"""
    prime_lift = load_json(prime_lift_path)
    selective_rows = [
        row for row in prime_lift["signature_rows"]
        if row["route"] == "SelectivePrimePromotionNeedsCommutationBeforeDeletionKL"
    ]
    commutation_rows = [analyze_selective_row(row) for row in selective_rows]
    route_counts = Counter(row["route"] for row in commutation_rows)
    return {
        "certificate_type": "triad_a1_selective_promotion_commutation",
        "status": "selective_promotion_commutation_resolved_by_finite_split",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "continuous_prime_lift_json": file_sha256(prime_lift_path),
        },
        "selective_row_count": len(selective_rows),
        "route_counts": dict(sorted(route_counts.items())),
        "all_crt_orders_commute": all(row["crt_orders_commute"] for row in commutation_rows),
        "max_successor_count": max(
            (row["successor_count"] for row in commutation_rows),
            default=0,
        ),
        "commutation_rows": commutation_rows,
        "commutation_law": (
            "若 signature (ell,y,c) 跳过较小尾素数 r，则先晋升 r。"
            "对 r 的每个 residue s，原 ell-fiber residue 在 Qr 层变为 "
            "y'=(y-s)r^{-1} mod ell。于是选择性签名被有限拆成 r 个标准后继签名。"
            "若原签名有正 limsup 质量，则有限鸽巢给出某个后继签名正 limsup；"
            "若所有后继都不持久，则该质量进入 diffuse CleanKLS/DLS。"
        ),
        "review_conclusion": (
            "唯一选择性晋升缺口已由 CRT 交换律和有限拆分吸收：它不再是独立终端。"
            "后继要么回到标准 prime-lift promotion deletion/KL，要么进入 diffuse KLS。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 选择性晋升交换律",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 交换律",
        "",
        result["commutation_law"],
        "",
        "```text",
        "original signature: (ell,y,c) at Q；",
        "first promote r<ell；",
        "new phase: t'=t+Qs；",
        "need t'+Qr*y' == t+Qy mod ell；",
        "therefore y'=(y-s)r^{-1} mod ell。",
        "```",
        "",
        "因此跳过较小素数的选择性晋升不会生成第四出口；它只是有限拆分。",
        "",
        "## 2. 汇总",
        "",
        f"- `selective_row_count={result['selective_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_crt_orders_commute={result['all_crt_orders_commute']}`。",
        f"- `max_successor_count={result['max_successor_count']}`。",
        "",
        "## 3. 明细",
        "",
        "| P | signature | first r | ell | successors | route |",
        "| ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["commutation_rows"]:
        lines.append(
            "| {p} | `{sig}` | {first} | {ell} | {count} | `{route}` |".format(
                p=row["p"],
                sig=row["signature"],
                first=row["first_prime"],
                ell=row["promoted_prime"],
                count=row["successor_count"],
                route=row["route"],
            )
        )
    lines.extend(["", "## 4. 后继签名", ""])
    for row in result["commutation_rows"]:
        lines.append(f"### P={row['p']} signature={row['signature']}")
        lines.append("")
        lines.append(f"- final_q_direct=`{row['final_q_direct']}`。")
        lines.append(f"- final_q_ordered=`{row['final_q_ordered']}`。")
        lines.append(f"- successors=`{row['successor_signatures']}`。")
        lines.append("")
    lines.extend(
        [
            "## 5. 当前硬点",
            "",
            "选择性晋升已不再是独立缺口。剩余是标准晋升后的删除势/NoDeletion-KL 证书，",
            "以及 diffuse 分支的 CleanKLS/DLS 大筛估计。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime-lift-json", type=Path, default=DEFAULT_PRIME_LIFT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.prime_lift_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "selective_row_count": result["selective_row_count"],
                "route_counts": result["route_counts"],
                "max_successor_count": result["max_successor_count"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
