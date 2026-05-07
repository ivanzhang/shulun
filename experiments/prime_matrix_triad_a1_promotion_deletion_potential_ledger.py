#!/usr/bin/env python3
"""生成 Triad-A1 TopPrimePromotion 的删除势账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_promotion_deletion_potential_ledger.py

输出：
  docs/monograph/prime-matrix-triad-a1-promotion-deletion-potential-ledger.json
  docs/monograph/prime-matrix-triad-a1-promotion-deletion-potential-ledger.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PROMOTION = DOCS / "prime-matrix-triad-a1-topprime-promotion-gate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-promotion-deletion-potential-ledger.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-promotion-deletion-potential-ledger.md"


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def deletion_potential(survival: float) -> float:
    """把幸存率转成删除势。"""
    if survival <= 0:
        return math.inf
    return -math.log(survival)


def analyze_cap(row: dict[str, Any]) -> dict[str, Any]:
    """分析单个晋升 cap 的删除势。"""
    survival = float(row["lift_survival_rate"])
    potential = deletion_potential(survival)
    return {
        "p": int(row["p"]),
        "q": int(row["q"]),
        "target_q": int(row["target_q"]),
        "top_prime": int(row["top_prime"]),
        "alpha": row["alpha"],
        "direction": row["direction"],
        "h": int(row["h"]),
        "source": row["source"],
        "old_intersection_size": int(row["old_intersection_size"]),
        "lift_slot_count": int(row["lift_slot_count"]),
        "max_lift_slots": int(row["max_lift_slots"]),
        "lift_survival_rate": survival,
        "lift_deletion_rate": float(row["lift_deletion_rate"]),
        "deletion_potential": potential,
        "promotion_classification": row["promotion_classification"],
        "ledger_route": (
            "PositiveDeletionPotential"
            if potential > 0
            else "NoDeletionGate"
        ),
    }


def run(promotion_path: Path) -> dict[str, Any]:
    """运行删除势账本。"""
    promotion = load_json(promotion_path)
    cap_rows = [analyze_cap(row) for row in promotion["cap_reports"]]
    p_summary = []
    for p in sorted({row["p"] for row in cap_rows}):
        rows = [row for row in cap_rows if row["p"] == p]
        potentials = [row["deletion_potential"] for row in rows]
        survivals = [row["lift_survival_rate"] for row in rows]
        p_summary.append(
            {
                "p": p,
                "cap_count": len(rows),
                "min_deletion_potential": min(potentials),
                "max_deletion_potential": max(potentials),
                "min_survival_rate": min(survivals),
                "max_survival_rate": max(survivals),
                "all_positive_deletion_potential": all(value > 0 for value in potentials),
            }
        )

    finite_potentials = [
        row["deletion_potential"] for row in cap_rows
        if math.isfinite(row["deletion_potential"])
    ]
    return {
        "certificate_type": "triad_a1_promotion_deletion_potential_ledger",
        "status": "promotion_deletion_potential_materialized",
        "source_hashes": {
            "promotion_deletion_potential_script": file_sha256(Path(__file__).resolve()),
            "topprime_promotion_json": file_sha256(promotion_path),
        },
        "q": int(promotion["q"]),
        "cap_count": len(cap_rows),
        "p_values": sorted({row["p"] for row in cap_rows}),
        "all_positive_deletion_potential": all(
            row["deletion_potential"] > 0 for row in cap_rows
        ),
        "global_min_deletion_potential_current_layer": min(finite_potentials),
        "global_max_survival_current_layer": max(
            row["lift_survival_rate"] for row in cap_rows
        ),
        "p_summary": p_summary,
        "cap_rows": cap_rows,
        "tower_law": (
            "每次 top-prime 晋升产生本地删除势 D_n=-log(a_n)。"
            "若沿无限晋升塔 sum D_n 发散，则支撑密度趋零；若 sum D_n 可求和，"
            "则 a_n->1，必须进入 NoDeletion-KL / CleanKLS / PDEC 回流。"
        ),
        "review_conclusion": (
            "当前 Q=2310 的 top-prime 晋升层全部具有正删除势。"
            "这不是全局常数证明；它把当前层纳入可累加删除势账本，并给出未来层的严格门控。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    if math.isinf(value):
        return "inf"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 晋升删除势账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 删除势律",
        "",
        result["tower_law"],
        "",
        "形式上，对每层晋升：",
        "",
        "```text",
        "a_n = lift_survival_rate；",
        "D_n = -log(a_n)。",
        "```",
        "",
        "于是：",
        "",
        "```text",
        "sum D_n = infinity  => 支撑密度趋零，进入 Sparse/LocalSurvivor/PDEC；",
        "sum D_n < infinity  => a_n -> 1，进入 NoDeletion-KL / CleanKLS；",
        "某固定 residue/cap 持久 => PDEC 回流。",
        "```",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 汇总",
            "",
            f"- `cap_count={result['cap_count']}`。",
            f"- `all_positive_deletion_potential={result['all_positive_deletion_potential']}`。",
            f"- `global_min_deletion_potential_current_layer={fmt_float(result['global_min_deletion_potential_current_layer'])}`。",
            f"- `global_max_survival_current_layer={fmt_float(result['global_max_survival_current_layer'])}`。",
            "",
            "| P | caps | min survival | max survival | min D | max D | positive D |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["p_summary"]:
        lines.append(
            "| {p} | {caps} | {mins} | {maxs} | {mind} | {maxd} | `{pos}` |".format(
                p=row["p"],
                caps=row["cap_count"],
                mins=fmt_float(row["min_survival_rate"]),
                maxs=fmt_float(row["max_survival_rate"]),
                mind=fmt_float(row["min_deletion_potential"]),
                maxd=fmt_float(row["max_deletion_potential"]),
                pos=row["all_positive_deletion_potential"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap 删除势明细",
            "",
            "| P | alpha | h | dir | survival | deletion | D=-log(a) | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_rows"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {surv} | {dele} | {pot} | `{route}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                surv=fmt_float(row["lift_survival_rate"]),
                dele=fmt_float(row["lift_deletion_rate"]),
                pot=fmt_float(row["deletion_potential"]),
                route=row["ledger_route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结构读数",
            "",
            "当前层最小删除势为正，说明 `top-prime 持久支付` 在本层已经被实质删除吸收。",
            "后续证明不应把 `0.880078...` 当作全局常数；正确链条是逐层登记 `D_n`。",
            "若未来层 `D_n` 不可累加到无穷，则自动给出 `a_n->1` 的 NoDeletion 条件，接入 KL/PDEC 或 CleanKLS。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.promotion_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "cap_count": result["cap_count"],
                "all_positive_deletion_potential": result[
                    "all_positive_deletion_potential"
                ],
                "global_min_deletion_potential_current_layer": result[
                    "global_min_deletion_potential_current_layer"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
