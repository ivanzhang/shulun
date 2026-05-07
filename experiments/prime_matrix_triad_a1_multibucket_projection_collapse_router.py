#!/usr/bin/env python3
"""判定裸多桶 LP 是否投影坍缩到普通相位容量。

用法示例：
  python3 experiments/prime_matrix_triad_a1_multibucket_projection_collapse_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-multibucket-projection-collapse-router.json
  docs/monograph/prime-matrix-triad-a1-multibucket-projection-collapse-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SKELETON = DOCS / "prime-matrix-triad-a1-multibucket-pdec-skeleton.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-multibucket-projection-collapse-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-multibucket-projection-collapse-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def analyze_row(row: dict[str, Any]) -> dict[str, Any]:
    """分析一个多桶 LP 骨架是否发生裸投影坍缩。"""
    phase_capacity_surplus = (
        bool(row["phase_exposure_identity"])
        and int(row["high_prime_count"]) >= 1
    )
    bare_projection_collapses = phase_capacity_surplus
    route = (
        "NeedsFormalUnitCompatibilityOrCleanKLS"
        if bare_projection_collapses
        else "ExposureCapacityAlreadyRestrictsProjection"
    )
    return {
        "p": int(row["p"]),
        "q": int(row["q"]),
        "alpha": row["alpha"],
        "direction": row["direction"],
        "h": int(row["h"]),
        "source": row["source"],
        "bucket_kind": row["bucket_kind"],
        "active_phase_count": int(row["active_phase_count"]),
        "bucket_count": int(row["bucket_count"]),
        "variable_count": int(row["variable_count"]),
        "high_prime_count": int(row["high_prime_count"]),
        "single_bucket_payment_excluded": bool(
            row["single_bucket_payment_excluded"]
        ),
        "phase_exposure_identity": bool(row["phase_exposure_identity"]),
        "phase_capacity_surplus": phase_capacity_surplus,
        "bare_projection_collapses": bare_projection_collapses,
        "route": route,
    }


def run(skeleton_path: Path) -> dict[str, Any]:
    """运行投影坍缩路由。"""
    skeleton = load_json(skeleton_path)
    rows = [analyze_row(row) for row in skeleton["rows"]]
    route_counts = Counter(row["route"] for row in rows)
    return {
        "certificate_type": "triad_a1_multibucket_projection_collapse_router",
        "status": "bare_multibucket_lp_projection_collapse_routed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "skeleton_json": file_sha256(skeleton_path),
        },
        "matrix_row_count": len(rows),
        "route_counts": dict(sorted(route_counts.items())),
        "all_single_bucket_payments_excluded": all(
            row["single_bucket_payment_excluded"] for row in rows
        ),
        "all_phase_capacity_surplus": all(
            row["phase_capacity_surplus"] for row in rows
        ),
        "all_bare_projection_collapses": all(
            row["bare_projection_collapses"] for row in rows
        ),
        "rows": rows,
        "structural_law": (
            "If only 0<=g_b(t)<=E_b(t), sum_b g_b(t)<=M(t), and the objective "
            "depends on G(t)=sum_b g_b(t), then the feasible projection is exactly "
            "0<=G(t)<=M(t) whenever sum_b E_b(t)>=M(t) for every t. "
            "The current skeleton has sum_b E_b(t)=high_prime_count*M(t), so the bare "
            "multi-bucket LP gives no stronger U_CRT than the phase-mass projection."
        ),
        "review_conclusion": (
            "裸多桶 LP 已全部投影坍缩：单桶支付虽已排除，但若没有 formal-unit 兼容行、"
            "列/尾条件行或实际支付图约束，多桶变量不会自动降低 U_CRT。下一步必须加入"
            "持久多桶签名兼容，或把无兼容情形路由到 CleanKLS/DLS。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 多桶投影坍缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 投影坍缩律",
        "",
        result["structural_law"],
        "",
        "```text",
        "0 <= g_b(t) <= E_b(t)；",
        "G(t)=sum_b g_b(t)；",
        "sum_b g_b(t) <= M(t)；",
        "sum_b E_b(t) >= M(t)",
        "=> 0 <= G(t) <= M(t)。",
        "```",
        "",
        "所以仅有裸暴露上界时，多桶 LP 的 `G(t)` 投影不比普通相位质量上界更强。",
        "",
        "## 2. 汇总",
        "",
        f"- `matrix_row_count={result['matrix_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_single_bucket_payments_excluded={result['all_single_bucket_payments_excluded']}`。",
        f"- `all_phase_capacity_surplus={result['all_phase_capacity_surplus']}`。",
        f"- `all_bare_projection_collapses={result['all_bare_projection_collapses']}`。",
        "",
        "## 3. 路由含义",
        "",
        "这一步不是退回统计估计，而是排除一条无效闭合路径：",
        "",
        "```text",
        "单靠多桶变量数量增加",
        "  不能推出 U_CRT^multi<L_PDEC^multi；",
        "",
        "必须增加 formal-unit compatibility / TailAnchor / ColumnCRT / cofactor 条件行；",
        "否则无持久兼容签名的部分进入 CleanKLS/DLS。",
        "```",
        "",
        "## 4. 明细",
        "",
        "| P | kind | alpha | h | dir | phases | buckets | vars | route |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| {p} | {kind} | {alpha} | {h} | {direction} | {phases} | {buckets} | {vars} | `{route}` |".format(
                p=row["p"],
                kind=row["bucket_kind"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                phases=row["active_phase_count"],
                buckets=row["bucket_count"],
                vars=row["variable_count"],
                route=row["route"],
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skeleton-json", type=Path, default=DEFAULT_SKELETON)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.skeleton_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "matrix_row_count": result["matrix_row_count"],
                "all_bare_projection_collapses": result[
                    "all_bare_projection_collapses"
                ],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
