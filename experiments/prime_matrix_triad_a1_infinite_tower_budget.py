#!/usr/bin/env python3
"""汇总 Triad-A1 new-layer 塔的删除/熵极限预算。

用法示例：
  python3 experiments/prime_matrix_triad_a1_infinite_tower_budget.py

输出：
  docs/monograph/prime-matrix-triad-a1-infinite-tower-budget.json
  docs/monograph/prime-matrix-triad-a1-infinite-tower-budget.md
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
DEFAULT_AUDITS = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-newlayer-fiber-audit-q30030-q510510.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-infinite-tower-budget.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-infinite-tower-budget.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def safe_neg_log(value: float | None) -> float | None:
    """计算 -log(value)，用于删除势。"""
    if value is None or value <= 0:
        return None
    return -math.log(value)


def layer_rows(path: Path, audit: dict[str, Any]) -> list[dict[str, Any]]:
    """展开单层审计中的 P 级预算行。"""
    rows = []
    for item in audit["prime_results"]:
        support = item["support_accounting"]
        density = item["density_accounting"]
        shape = item["fiber_shape"]
        survival = support["slot_survival_rate"]
        rows.append(
            {
                "audit_path": str(path),
                "q": audit["q"],
                "q_lift": audit["q_lift"],
                "fiber_size": audit["fiber_size"],
                "p": item["p"],
                "old_support_count": item["old_support_count"],
                "lift_support_count": item["lift_support_count"],
                "slot_survival_rate": survival,
                "slot_deletion_rate": support["slot_deletion_rate"],
                "density_drop_factor": density["density_drop_factor"],
                "deletion_potential": safe_neg_log(survival),
                "avg_normalized_entropy_by_lift_mass": shape[
                    "avg_normalized_entropy_by_lift_mass"
                ],
                "avg_normalized_kl_to_uniform_by_lift_mass": shape[
                    "avg_normalized_kl_to_uniform_by_lift_mass"
                ],
                "classification": item["classification"],
            }
        )
    return rows


def summarize_p_path(p: int, rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总单个 P 沿已物化塔的累积预算。"""
    ordered = sorted(rows, key=lambda row: row["q"])
    product_survival = 1.0
    product_drop = 1.0
    deletion_potential_sum = 0.0
    entropy_values = []
    kl_values = []
    complete = True
    previous_q_lift: int | None = None
    for row in ordered:
        if previous_q_lift is not None and row["q"] != previous_q_lift:
            complete = False
        previous_q_lift = row["q_lift"]
        survival = row["slot_survival_rate"]
        drop = row["density_drop_factor"]
        if survival is not None:
            product_survival *= survival
        if drop is not None:
            product_drop *= drop
        if row["deletion_potential"] is not None:
            deletion_potential_sum += row["deletion_potential"]
        if row["avg_normalized_entropy_by_lift_mass"] is not None:
            entropy_values.append(row["avg_normalized_entropy_by_lift_mass"])
        if row["avg_normalized_kl_to_uniform_by_lift_mass"] is not None:
            kl_values.append(row["avg_normalized_kl_to_uniform_by_lift_mass"])

    return {
        "p": p,
        "layer_count": len(ordered),
        "complete_chain_in_input": complete,
        "q_start": ordered[0]["q"] if ordered else None,
        "q_end": ordered[-1]["q_lift"] if ordered else None,
        "product_survival": product_survival if ordered else None,
        "product_density_drop": product_drop if ordered else None,
        "deletion_potential_sum": deletion_potential_sum,
        "max_entropy": max(entropy_values, default=None),
        "min_entropy": min(entropy_values, default=None),
        "max_kl_to_uniform": max(kl_values, default=None),
        "min_kl_to_uniform": min(kl_values, default=None),
        "rows": ordered,
        "finite_reading": (
            "已物化层处于强删除分支；若这种删除势沿无限塔不可求和，支撑密度趋零。"
        ),
    }


def run(audit_paths: list[Path]) -> dict[str, Any]:
    """运行塔预算汇总。"""
    audits = [(path, load_json(path)) for path in audit_paths]
    rows = [row for path, audit in audits for row in layer_rows(path, audit)]
    by_p: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        by_p.setdefault(row["p"], []).append(row)
    p_paths = [summarize_p_path(p, p_rows) for p, p_rows in sorted(by_p.items())]

    return {
        "certificate_type": "triad_a1_infinite_tower_deletion_entropy_budget",
        "status": "finite_budget_for_infinite_tower_dichotomy",
        "source_hashes": {
            "budget_script": file_sha256(Path(__file__).resolve()),
            **{
                f"audit_{idx}": file_sha256(path)
                for idx, (path, _audit) in enumerate(audits, start=1)
            },
        },
        "layer_count": len(audits),
        "row_count": len(rows),
        "p_paths": p_paths,
        "dichotomy_law": (
            "沿同一 C_P 投影塔，若删除势 sum_n -log a_n(P) 发散，则支撑密度趋零；"
            "若删除势可求和，则 a_n(P)->1，必须进入 fiber 条件分布的 KL/PDEC 或 CleanKLS 二分。"
        ),
        "review_conclusion": (
            "有限审计显示 P=19,23 已连续两层强删除，product_survival 很小。"
            "该文件的证明价值在于把后续无限塔硬点压成 deletion-potential divergence "
            "versus NoDeletion entropy dichotomy。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点值。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 无限塔删除/熵预算",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 极限二分律",
        "",
        result["dichotomy_law"],
        "",
        "设第 `n` 层平均支撑幸存率为 `a_n(P)`。投影单调性给出：",
        "",
        "```text",
        "density(A_{Q_N}) = density(A_{Q_0}) * product_{n<N} a_n(P)。",
        "```",
        "",
        "因此：",
        "",
        "```text",
        "sum -log a_n(P)=infinity  => density(A_{Q_N}) -> 0；",
        "sum -log a_n(P)<infinity  => a_n(P)->1，进入 NoDeletion。",
        "```",
        "",
        "`NoDeletion` 不能无名停留：若 fiber 条件分布持续偏斜，则进入 new-layer PDEC；若偏斜趋零，则进入 CleanKLS/DLS。",
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
            "## 3. P 路径预算",
            "",
            "| P | layers | Q start | Q end | product survival | product drop | deletion potential | entropy range | KL range |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for path_row in result["p_paths"]:
        entropy_range = (
            f"{fmt_float(path_row['min_entropy'])}..{fmt_float(path_row['max_entropy'])}"
        )
        kl_range = (
            f"{fmt_float(path_row['min_kl_to_uniform'])}..{fmt_float(path_row['max_kl_to_uniform'])}"
        )
        lines.append(
            "| {p} | {layers} | {qs} | {qe} | {surv} | {drop} | {pot} | `{ent}` | `{kl}` |".format(
                p=path_row["p"],
                layers=path_row["layer_count"],
                qs=path_row["q_start"],
                qe=path_row["q_end"],
                surv=fmt_float(path_row["product_survival"]),
                drop=fmt_float(path_row["product_density_drop"]),
                pot=fmt_float(path_row["deletion_potential_sum"]),
                ent=entropy_range,
                kl=kl_range,
            )
        )

    lines.extend(["", "## 4. 层级明细", ""])
    for path_row in result["p_paths"]:
        lines.extend(
            [
                f"### P={path_row['p']}",
                "",
                "| layer | survival | deletion | drop | deletion potential | entropy | KL | class |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for row in path_row["rows"]:
            lines.append(
                "| Q={q}->{ql} | {surv} | {dele} | {drop} | {pot} | {ent} | {kl} | `{cls}` |".format(
                    q=row["q"],
                    ql=row["q_lift"],
                    surv=fmt_float(row["slot_survival_rate"]),
                    dele=fmt_float(row["slot_deletion_rate"]),
                    drop=fmt_float(row["density_drop_factor"]),
                    pot=fmt_float(row["deletion_potential"]),
                    ent=fmt_float(row["avg_normalized_entropy_by_lift_mass"]),
                    kl=fmt_float(row["avg_normalized_kl_to_uniform_by_lift_mass"]),
                    cls=row["classification"],
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. 闭合边界",
            "",
            "本文给出无限塔的结构预算公式与有限层读数。它还没有证明 `sum -log a_n(P)` 必然发散，",
            "也没有完成 NoDeletion 分支的最终 PDEC/CleanKLS 排斥。下一步应攻：",
            "",
            "```text",
            "NoDeletion => KL 偏斜不可长期隐藏；",
            "若 KL 偏斜隐藏，则高维平坦大筛吸收。",
            "```",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audits", default=DEFAULT_AUDITS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(parse_paths(args.audits))
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "layer_count": result["layer_count"],
                "p_count": len(result["p_paths"]),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
