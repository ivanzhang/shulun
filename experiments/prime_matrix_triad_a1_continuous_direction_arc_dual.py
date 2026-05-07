#!/usr/bin/env python3
"""精确审计 Triad-A1 LHB 分支的连续方向弧 box-dual 前沿。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_direction_arc_dual.py
  python3 experiments/prime_matrix_triad_a1_continuous_direction_arc_dual.py --top-limit 8

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-direction-arc-dual.json
  docs/monograph/prime-matrix-triad-a1-continuous-direction-arc-dual.md
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
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-continuous-direction-arc-dual.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-direction-arc-dual.md"
TAU = 2.0 * math.pi


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析可选 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def angle_for_residue(residue: int, q: int) -> float:
    """把 q 周期 residue 转成角度。"""
    return TAU * residue / q


def endpoint_value(vector: complex, zeta: float) -> float:
    """计算 Re(e^{i zeta} vector)。"""
    return (complex(math.cos(zeta), math.sin(zeta)) * vector).real


def interval_best(vector: complex, left: float, right: float) -> tuple[float, float]:
    """在一个 active set 不变区间上求最大值与方向。"""
    if abs(vector) <= 1e-18:
        return 0.0, left
    candidates = [(endpoint_value(vector, left), left), (endpoint_value(vector, right), right)]
    zeta0 = (-math.atan2(vector.imag, vector.real)) % TAU
    if left <= zeta0 <= right:
        candidates.append((abs(vector), zeta0))
    return max(candidates, key=lambda item: item[0])


def aggregate_frequency_weights(m_vector: list[int], q: int, h: int) -> dict[int, int]:
    """聚合 h*t mod q 上的 M(t)。"""
    weights: dict[int, int] = {}
    for phase, value in enumerate(m_vector):
        if value <= 0:
            continue
        residue = (h * phase) % q
        weights[residue] = weights.get(residue, 0) + int(value)
    return weights


def best_continuous_arc_for_frequency(
    weights: dict[int, int],
    q: int,
) -> dict[str, Any]:
    """对固定 h 的聚合权重精确求连续方向半平面 box-dual 上界。"""
    events: list[tuple[float, complex, int]] = []
    active_vector = 0j
    active_mass = 0
    total_mass = sum(weights.values())

    # 对每个相位点，cos(theta+zeta)>0 时该点可被 box-dual 取满。
    for residue, weight in weights.items():
        theta = angle_for_residue(residue, q)
        point = complex(math.cos(theta), math.sin(theta)) * weight
        if math.cos(theta) > 0.0:
            active_vector += point
            active_mass += weight
        remove_at = (math.pi / 2.0 - theta) % TAU
        add_at = (3.0 * math.pi / 2.0 - theta) % TAU
        events.append((remove_at, -point, -weight))
        events.append((add_at, point, weight))

    events.sort(key=lambda item: item[0])
    best_value = -1.0
    best_zeta = 0.0
    best_active_mass = active_mass
    best_interval = (0.0, 0.0)
    left = 0.0
    idx = 0
    while idx < len(events):
        right = events[idx][0]
        if right > left:
            value, zeta = interval_best(active_vector, left, right)
            if value > best_value:
                best_value = value
                best_zeta = zeta
                best_active_mass = active_mass
                best_interval = (left, right)
        same_at = right
        while idx < len(events) and events[idx][0] == same_at:
            delta = events[idx][1]
            delta_mass = events[idx][2]
            active_vector += delta
            active_mass += delta_mass
            idx += 1
        left = right

    if left < TAU:
        value, zeta = interval_best(active_vector, left, TAU)
        if value > best_value:
            best_value = value
            best_zeta = zeta % TAU
            best_active_mass = active_mass
            best_interval = (left, TAU)

    # active_mass 只用于提示；最终 cap 质量会用 best_zeta 重算。
    return {
        "box_dual_value": best_value,
        "best_zeta_turn": best_zeta / TAU,
        "best_interval_turn": [best_interval[0] / TAU, best_interval[1] / TAU],
        "active_mass_hint": best_active_mass,
        "total_mass": total_mass,
    }


def cap_stats_for_zeta(m_vector: list[int], q: int, h: int, zeta_turn: float) -> dict[str, Any]:
    """按最优 zeta 重算实际正半平面 cap 的相位与质量。"""
    zeta = TAU * zeta_turn
    phases: list[int] = []
    mass = 0
    projection = 0.0
    for phase, value in enumerate(m_vector):
        if value <= 0:
            continue
        angle = TAU * ((h * phase) % q) / q
        c = math.cos(angle + zeta)
        if c > 0.0:
            phases.append(phase)
            mass += int(value)
            projection += int(value) * c
    return {
        "cap_phase_count": len(phases),
        "cap_mass": mass,
        "cap_phase_sample": phases[:20],
        "projection_recomputed": projection,
    }


def analyze_prime(item: dict[str, Any], top_limit: int, sparse_threshold: int) -> dict[str, Any]:
    """分析单个 P 的连续方向弧 box-dual。"""
    p = int(item["p"])
    q = int(item["q"])
    m_vector = [int(value) for value in item["m_vector"]]
    total_mass = sum(m_vector)
    rows: list[dict[str, Any]] = []
    for h in range(1, q):
        weights = aggregate_frequency_weights(m_vector, q, h)
        dual = best_continuous_arc_for_frequency(weights, q)
        cap = cap_stats_for_zeta(m_vector, q, h, dual["best_zeta_turn"])
        value = float(dual["box_dual_value"])
        rows.append(
            {
                "h": h,
                "box_dual_value": value,
                "box_dual_value_over_total_m": value / total_mass if total_mass else None,
                "best_zeta_turn": dual["best_zeta_turn"],
                "best_interval_turn": dual["best_interval_turn"],
                "cap_phase_count": cap["cap_phase_count"],
                "cap_mass": cap["cap_mass"],
                "cap_mass_share": cap["cap_mass"] / total_mass if total_mass else None,
                "projection_recomputed": cap["projection_recomputed"],
                "cap_phase_sample": cap["cap_phase_sample"],
                "route": (
                    "SparseContinuousDualCapToLocalSurvivor"
                    if cap["cap_phase_count"] <= sparse_threshold
                    else "PersistentContinuousDualCapNeedsColumnTailOrCleanKLS"
                ),
            }
        )
    rows.sort(key=lambda row: row["box_dual_value_over_total_m"] or 0.0, reverse=True)
    top_rows = rows[:top_limit]
    return {
        "p": p,
        "q": q,
        "total_m": total_mass,
        "nonzero_m_phase_count": sum(1 for value in m_vector if value > 0),
        "top_continuous_arc_rows": top_rows,
        "best_box_dual_value_over_total_m": top_rows[0]["box_dual_value_over_total_m"],
        "best_cap_mass_share": top_rows[0]["cap_mass_share"],
        "best_cap_phase_count": top_rows[0]["cap_phase_count"],
        "best_route": top_rows[0]["route"],
    }


def run(
    multiplicity_path: Path,
    p_filter: set[int] | None,
    top_limit: int,
    sparse_threshold: int,
) -> dict[str, Any]:
    """运行连续方向弧审计。"""
    data = load_json(multiplicity_path)
    prime_results = []
    for item in data["prime_results"]:
        p = int(item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        prime_results.append(analyze_prime(item, top_limit, sparse_threshold))
    return {
        "certificate_type": "triad_a1_continuous_direction_arc_dual",
        "status": "continuous_direction_arc_box_dual_materialized_not_closed",
        "q": int(data["q"]),
        "sparse_threshold": sparse_threshold,
        "top_limit": top_limit,
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "multiplicity_cap_json": file_sha256(multiplicity_path),
        },
        "prime_results": prime_results,
        "global_max_box_dual_value_over_total_m": max(
            row["best_box_dual_value_over_total_m"] for row in prime_results
        ),
        "global_min_best_cap_phase_count": min(
            row["best_cap_phase_count"] for row in prime_results
        ),
        "route_counts": {
            route: sum(1 for row in prime_results if row["best_route"] == route)
            for route in sorted({row["best_route"] for row in prime_results})
        },
        "structural_law": (
            "在仅有 0<=g(t)<=M(t) 的同集容量行下，固定 h 与方向 zeta 的最优解会取满 "
            "Re(e^{i zeta}e(ht))>0 的全部相位。因此连续方向弧上界可由半平面支持函数精确计算。"
            "若该上界仍大，失败对象就是连续方向 DualCap，必须加入 column/tail/cofactor 行或转 CleanKLS。"
        ),
        "review_conclusion": (
            "连续方向弧 box-dual 已物化：当前合法 box 行不能给出 U_CRT<L_PDEC。"
            "它把 ContinuousDirectionArcDual 缺口转成具体的 persistent continuous DualCap 输入。"
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
        "# Triad-A1 连续方向弧 Box-Dual 审计",
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
        "U_box(h,zeta)=sum_t M(t) max(0, Re(e^{i zeta}e(ht)))；",
        "U_box(h)=max_zeta U_box(h,zeta)。",
        "```",
        "",
        "这是当前合法 box 行的精确连续方向弧上界，不是离散方向采样。",
        "",
        "## 2. 汇总",
        "",
        f"- `Q={result['q']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `global_max_box_dual_value_over_total_m={fmt_float(result['global_max_box_dual_value_over_total_m'])}`。",
        f"- `global_min_best_cap_phase_count={result['global_min_best_cap_phase_count']}`。",
        "",
        "## 3. P 级最强连续弧",
        "",
        "| P | total M | nonzero phases | best h | zeta | U_box/M | cap mass share | cap phases | route |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["prime_results"]:
        top = row["top_continuous_arc_rows"][0]
        lines.append(
            "| {p} | {total} | {nonzero} | {h} | {zeta} | {u} | {share} | {phases} | `{route}` |".format(
                p=row["p"],
                total=row["total_m"],
                nonzero=row["nonzero_m_phase_count"],
                h=top["h"],
                zeta=fmt_float(top["best_zeta_turn"]),
                u=fmt_float(top["box_dual_value_over_total_m"]),
                share=fmt_float(top["cap_mass_share"]),
                phases=top["cap_phase_count"],
                route=top["route"],
            )
        )
    lines.extend(
        [
            "",
            "## 4. 读法",
            "",
            "如果目标是证明 `U_CRT<L_PDEC`，当前 box 行已经不够：连续方向上仍有 persistent cap。",
            "因此下一步不应继续增加方向采样密度，而应补入同集合法的结构行：",
            "",
            "```text",
            "column/displacement compatibility；",
            "tail/cofactor nonreuse；",
            "actual Gamma forced-signature constraints；",
            "或 flat residual CleanKLS/DLS。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--p-values", default=None)
    parser.add_argument("--top-limit", type=int, default=5)
    parser.add_argument("--sparse-threshold", type=int, default=16)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        multiplicity_path=args.multiplicity_json,
        p_filter=parse_p_values(args.p_values),
        top_limit=args.top_limit,
        sparse_threshold=args.sparse_threshold,
    )
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
                "global_max_box_dual_value_over_total_m": result[
                    "global_max_box_dual_value_over_total_m"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
