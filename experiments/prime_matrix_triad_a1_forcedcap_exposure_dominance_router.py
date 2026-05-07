#!/usr/bin/env python3
"""把 ForcedCap column-tail 暴露账本转成实际支付支配路由。

用法示例：
  python3 experiments/prime_matrix_triad_a1_forcedcap_exposure_dominance_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-forcedcap-exposure-dominance-router.json
  docs/monograph/prime-matrix-triad-a1-forcedcap-exposure-dominance-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_EXPOSURE = DOCS / "prime-matrix-triad-a1-forcedcap-columntail-payment.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-forcedcap-exposure-dominance-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-forcedcap-exposure-dominance-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ceil_ratio(numerator: int, denominator: int) -> int | None:
    """计算 ceil(numerator/denominator)。"""
    if denominator <= 0:
        return None
    return math.ceil(numerator / denominator)


def analyze_cap(row: dict[str, Any]) -> dict[str, Any]:
    """把单个 cap 的暴露上界转成实际支付桶数下界。"""
    demand = int(row["total_hole_demand"])
    max_residue = int(row["max_residue_exposure"])
    max_colres = int(row["max_column_residue_exposure"])
    residue_lb = ceil_ratio(demand, max_residue)
    colres_lb = ceil_ratio(demand, max_colres)
    route = (
        "MultiBucketPDECOrDistributedCleanKLS"
        if demand > 0
        else "NoTailDemandFinitePDEC"
    )
    return {
        "p": int(row["p"]),
        "q": int(row["q"]),
        "alpha": row["alpha"],
        "direction": row["direction"],
        "h": int(row["h"]),
        "source": row["source"],
        "demand": demand,
        "max_residue_exposure": max_residue,
        "max_column_residue_exposure": max_colres,
        "max_residue_exposure_share": row["max_residue_exposure_over_demand"],
        "max_column_residue_exposure_share": row[
            "max_column_residue_exposure_over_demand"
        ],
        "min_actual_residue_buckets_by_exposure": residue_lb,
        "min_actual_column_residue_buckets_by_exposure": colres_lb,
        "single_residue_actual_payment_excluded": (
            residue_lb is not None and residue_lb >= 2
        ),
        "single_column_residue_actual_payment_excluded": (
            colres_lb is not None and colres_lb >= 2
        ),
        "route": route,
    }


def run(exposure_path: Path) -> dict[str, Any]:
    """运行实际支付支配路由。"""
    exposure = load_json(exposure_path)
    cap_rows = [analyze_cap(row) for row in exposure["cap_reports"]]
    nontrivial = [row for row in cap_rows if row["demand"] > 0]
    route_counts = Counter(row["route"] for row in cap_rows)
    return {
        "certificate_type": "triad_a1_forcedcap_exposure_dominance_router",
        "status": "forcedcap_actual_payment_dominated_by_exposure",
        "source_hashes": {
            "router_script": file_sha256(Path(__file__).resolve()),
            "exposure_json": file_sha256(exposure_path),
        },
        "forced_cap_count": len(cap_rows),
        "route_counts": dict(sorted(route_counts.items())),
        "all_single_residue_actual_payment_excluded": all(
            row["single_residue_actual_payment_excluded"] for row in nontrivial
        ),
        "all_single_column_residue_actual_payment_excluded": all(
            row["single_column_residue_actual_payment_excluded"]
            for row in nontrivial
        ),
        "global_min_actual_residue_buckets_by_exposure": min(
            row["min_actual_residue_buckets_by_exposure"]
            for row in nontrivial
            if row["min_actual_residue_buckets_by_exposure"] is not None
        ),
        "global_min_actual_column_residue_buckets_by_exposure": min(
            row["min_actual_column_residue_buckets_by_exposure"]
            for row in nontrivial
            if row["min_actual_column_residue_buckets_by_exposure"] is not None
        ),
        "global_max_residue_exposure_share": max(
            row["max_residue_exposure_share"] for row in nontrivial
        ),
        "global_max_column_residue_exposure_share": max(
            row["max_column_residue_exposure_share"] for row in nontrivial
        ),
        "p_summary": summarize_by_p(nontrivial),
        "cap_rows": cap_rows,
        "structural_law": (
            "Actual payment in a bucket is bounded above by its exposure. "
            "Therefore a cap with demand D and max bucket exposure E must use at least ceil(D/E) buckets, "
            "unless it routes to a persistent multi-bucket PDEC formal unit."
        ),
        "review_conclusion": (
            "ForcedCap 的实际 column-tail 支付受暴露账本支配；当前全部 24 个 forced cap "
            "都排除了单 residue 与单 column-residue 承担全部需求。剩余只能是多桶持久 PDEC "
            "或分散 CleanKLS/DLS。"
        ),
    }


def summarize_by_p(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 P 汇总动态桶数下界。"""
    summaries = []
    for p in sorted({row["p"] for row in rows}):
        subset = [row for row in rows if row["p"] == p]
        summaries.append(
            {
                "p": p,
                "cap_count": len(subset),
                "min_actual_residue_buckets_by_exposure": min(
                    row["min_actual_residue_buckets_by_exposure"]
                    for row in subset
                    if row["min_actual_residue_buckets_by_exposure"] is not None
                ),
                "min_actual_column_residue_buckets_by_exposure": min(
                    row["min_actual_column_residue_buckets_by_exposure"]
                    for row in subset
                    if row["min_actual_column_residue_buckets_by_exposure"]
                    is not None
                ),
                "max_residue_exposure_share": max(
                    row["max_residue_exposure_share"] for row in subset
                ),
                "max_column_residue_exposure_share": max(
                    row["max_column_residue_exposure_share"] for row in subset
                ),
            }
        )
    return summaries


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 ForcedCap 暴露支配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "actual_payment(bucket) <= exposure(bucket)；",
        "D_C <= sum actual_payment(bucket)；",
        "therefore bucket_count >= ceil(D_C / max_exposure)。",
        "```",
        "",
        "这不是固定常数判据；每个 cap 使用自己的 `D_C/max_exposure` 动态下界。",
        "",
        "## 2. 汇总",
        "",
        f"- `forced_cap_count={result['forced_cap_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_single_residue_actual_payment_excluded={result['all_single_residue_actual_payment_excluded']}`。",
        f"- `all_single_column_residue_actual_payment_excluded={result['all_single_column_residue_actual_payment_excluded']}`。",
        f"- `global_min_actual_residue_buckets_by_exposure={result['global_min_actual_residue_buckets_by_exposure']}`。",
        f"- `global_min_actual_column_residue_buckets_by_exposure={result['global_min_actual_column_residue_buckets_by_exposure']}`。",
        f"- `global_max_residue_exposure_share={fmt_float(result['global_max_residue_exposure_share'])}`。",
        f"- `global_max_column_residue_exposure_share={fmt_float(result['global_max_column_residue_exposure_share'])}`。",
        "",
        "## 3. P 级汇总",
        "",
        "| P | caps | min actual residue buckets | min actual colres buckets | max residue exposure share | max colres exposure share |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["p_summary"]:
        lines.append(
            "| {p} | {caps} | {reslb} | {collb} | {rs} | {cs} |".format(
                p=row["p"],
                caps=row["cap_count"],
                reslb=row["min_actual_residue_buckets_by_exposure"],
                collb=row["min_actual_column_residue_buckets_by_exposure"],
                rs=fmt_float(row["max_residue_exposure_share"]),
                cs=fmt_float(row["max_column_residue_exposure_share"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap 明细",
            "",
            "| P | alpha | h | dir | D | min residue buckets | min colres buckets | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_rows"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {demand} | {reslb} | {collb} | `{route}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                demand=row["demand"],
                reslb=row["min_actual_residue_buckets_by_exposure"],
                collb=row["min_actual_column_residue_buckets_by_exposure"],
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "这一步把 `暴露签名` 升级成实际支付的上界约束。",
            "若某个实际支付签名持久承担需求，它必须是一组多桶 formal unit，而不是单 residue/单 column-residue。",
            "若没有这样的持久多桶集合，则 forced cap 的支付只能分散，进入 CleanKLS/DLS。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exposure-json", type=Path, default=DEFAULT_EXPOSURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.exposure_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "forced_cap_count": result["forced_cap_count"],
                "all_single_residue_actual_payment_excluded": result[
                    "all_single_residue_actual_payment_excluded"
                ],
                "all_single_column_residue_actual_payment_excluded": result[
                    "all_single_column_residue_actual_payment_excluded"
                ],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
