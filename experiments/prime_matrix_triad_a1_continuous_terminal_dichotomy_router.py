#!/usr/bin/env python3
"""路由 A1 连续 actual-payment 的终端二分。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_terminal_dichotomy_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json
  docs/monograph/prime-matrix-triad-a1-continuous-terminal-dichotomy-router.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_ACTUAL = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.md"


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


def route_cap(row: dict[str, Any]) -> dict[str, Any]:
    """把单个 cap 路由到终端二分接口。"""
    if int(row["total_hole_demand"]) == 0:
        route = "NoTailDemandSparseOrLocalSurvivor"
        terminal_obligations: list[str] = []
    else:
        route = "PositiveLimsupPDECOrDiffuseCleanKLSDichotomy"
        terminal_obligations = [
            "PLS-PDEC: positive-limsup finite payment signature gives a legal column-tail PDEC row",
            "DIF-KLS: all finite payment signatures vanish gives L2-flat CleanKLS/DLS admission",
        ]
    return {
        "p": int(row["p"]),
        "q": int(row["q"]),
        "h": int(row["h"]),
        "zeta_turn": float(row["zeta_turn"]),
        "total_hole_demand": int(row["total_hole_demand"]),
        "total_payment_count": int(row["total_payment_count"]),
        "payment_count_matches_demand": bool(row["payment_count_matches_demand"]),
        "max_payment_signature_share": row["max_payment_signature_share"],
        "effective_payment_signature_support": row[
            "effective_payment_signature_support"
        ],
        "payment_signature_l2_energy": row["payment_signature_l2_energy"],
        "inverse_l2_payment_signature_support": row[
            "inverse_l2_payment_signature_support"
        ],
        "distinct_payment_signature_count": int(row["distinct_payment_signature_count"]),
        "top_payment_signature": row["top_payment_signature"],
        "route": route,
        "terminal_obligations": terminal_obligations,
    }


def run(actual_path: Path) -> dict[str, Any]:
    """运行终端二分路由。"""
    actual = load_json(actual_path)
    cap_routes = [route_cap(row) for row in actual["cap_reports"]]
    positive = [row for row in cap_routes if row["total_hole_demand"] > 0]
    route_counts = Counter(row["route"] for row in cap_routes)
    return {
        "certificate_type": "triad_a1_continuous_terminal_dichotomy_router",
        "status": "continuous_terminal_dichotomy_admission_closed_capacity_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "continuous_actual_payment_selection_json": file_sha256(actual_path),
        },
        "all_actual_payment_measures_constructed": bool(
            actual["all_payment_counts_match_demand"]
        ),
        "cap_route_count": len(cap_routes),
        "positive_demand_route_count": len(positive),
        "route_counts": dict(sorted(route_counts.items())),
        "global_max_actual_signature_share": max(
            (row["max_payment_signature_share"] or 0.0 for row in positive),
            default=0.0,
        ),
        "global_min_effective_signature_support": min(
            (
                row["effective_payment_signature_support"]
                for row in positive
                if row["effective_payment_signature_support"] is not None
            ),
            default=None,
        ),
        "global_min_inverse_l2_signature_support": min(
            (
                row["inverse_l2_payment_signature_support"]
                for row in positive
                if row["inverse_l2_payment_signature_support"] is not None
            ),
            default=None,
        ),
        "cap_routes": cap_routes,
        "terminal_dichotomy_law": (
            "对任意无限反例塔的 canonical payment probability measures mu_i，"
            "固定有限层的 payment-signature 空间是有限的。因此要么某个有限签名有正 limsup 质量，"
            "要么每个固定有限签名质量都趋零。前者是 column-tail PDEC formal row 的合法输入；"
            "后者给出所有有限投影的 max atom 和 L2 能量趋零，即 CleanKLS/DLS admission。"
        ),
        "closed_subclaims": [
            "canonical actual payment measure constructed",
            "payment_count equals low-hole demand",
            "no third terminal route in the finite-projection dichotomy",
            "diffuse branch supplies L2-flat admission language",
            "positive-limsup branch supplies legal finite column-tail PDEC row input",
        ],
        "open_terminal_obligations": [
            "PDEC-CAP: prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC",
            "KLS-EXT: prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures",
        ],
        "review_conclusion": (
            "连续 actual-payment 分支的终端二分已经闭合到两个外部终端义务："
            "正 limsup 有限签名不是新出口，而是合法 column-tail PDEC 输入；"
            "全部有限签名消散不是新出口，而是 L2-flat CleanKLS/DLS 输入。"
            "剩余未闭合的是 PDEC 容量不等式和 CleanKLS 大筛估计本身。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 连续 actual-payment 终端二分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 终端二分律",
        "",
        result["terminal_dichotomy_law"],
        "",
        "```text",
        "canonical payment measures mu_i on finite projection B_i；",
        "either exists b in B_i with limsup mu_i(b)>0",
        "  => positive-limsup finite signature => column-tail PDEC；",
        "or for every fixed finite projection atom b, mu_i(b)->0",
        "  => max atom -> 0 and L2 -> 0 on finite projections => CleanKLS/DLS admission。",
        "```",
        "",
        "这一步关闭的是二分逻辑，不声称已经证明 PDEC 容量或 KLS 大筛终端估计。",
        "",
        "## 2. 汇总",
        "",
        f"- `all_actual_payment_measures_constructed={result['all_actual_payment_measures_constructed']}`。",
        f"- `cap_route_count={result['cap_route_count']}`。",
        f"- `positive_demand_route_count={result['positive_demand_route_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `global_max_actual_signature_share={fmt_float(result['global_max_actual_signature_share'])}`。",
        f"- `global_min_effective_signature_support={fmt_float(result['global_min_effective_signature_support'])}`。",
        f"- `global_min_inverse_l2_signature_support={fmt_float(result['global_min_inverse_l2_signature_support'])}`。",
        "",
        "## 3. 已闭合子命题",
        "",
    ]
    for item in result["closed_subclaims"]:
        lines.append(f"- `{item}`。")
    lines.extend(["", "## 4. 剩余终端义务", ""])
    for item in result["open_terminal_obligations"]:
        lines.append(f"- `{item}`。")

    lines.extend(
        [
            "",
            "## 5. Cap 路由",
            "",
            "| P | demand | max sig share | eff sig support | L2 sig support | distinct sigs | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_routes"]:
        lines.append(
            "| {p} | {demand} | {share} | {support} | {l2support} | {distinct} | `{route}` |".format(
                p=row["p"],
                demand=row["total_hole_demand"],
                share=fmt_float(row["max_payment_signature_share"]),
                support=fmt_float(row["effective_payment_signature_support"]),
                l2support=fmt_float(row["inverse_l2_payment_signature_support"]),
                distinct=row["distinct_payment_signature_count"],
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 6. 读法",
            "",
            "当前样本的 actual payment 已经高度分散；但全局证明不能依赖这些有限数值。",
            "真正可用的是投影塔二分：集中则命名为 PDEC，完全不集中则满足 CleanKLS 的 L2-flat 输入。",
            "所以下一步必须直接攻 `PDEC-CAP` 或 `KLS-EXT`，不能再把 actual payment 当作未定义缺口。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actual-json", type=Path, default=DEFAULT_ACTUAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.actual_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "route_counts": result["route_counts"],
                "open_terminal_obligations": result["open_terminal_obligations"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
