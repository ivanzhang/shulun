#!/usr/bin/env python3
"""把 A1 连续方向弧 DualCap 接到 column-tail 结构二分。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_columntail_bridge.py
  python3 experiments/prime_matrix_triad_a1_continuous_columntail_bridge.py --top-rows-per-p 1

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-columntail-bridge.json
  docs/monograph/prime-matrix-triad-a1-continuous-columntail-bridge.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_CONTINUOUS = DOCS / "prime-matrix-triad-a1-continuous-direction-arc-dual.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-continuous-columntail-bridge.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-columntail-bridge.md"
TAU = 2.0 * math.pi


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


def positive_cap_phases(m_vector: list[int], q: int, h: int, zeta_turn: float) -> list[int]:
    """重建连续半平面 cap 内的相位。"""
    phases = []
    zeta = TAU * zeta_turn
    for phase, mass in enumerate(m_vector):
        if mass <= 0:
            continue
        angle = TAU * ((h * phase) % q) / q
        if math.cos(angle + zeta) > 0.0:
            phases.append(phase)
    return phases


def residue_for_hole(p: int, q: int, phase: int, col: int, prime: int) -> int:
    """给出高素数 prime 支付列 col 所需的 fiber residue y mod prime。"""
    inverse_p = pow(p, -1, prime)
    inverse_q = pow(q % prime, -1, prime)
    target_row_residue = (1 - col * inverse_p) % prime
    return ((target_row_residue - phase) * inverse_q) % prime


def top_counter(counter: Counter[str], limit: int) -> list[dict[str, Any]]:
    """输出 Counter 的 top 项。"""
    return [{"key": key, "count": count} for key, count in counter.most_common(limit)]


def share(value: int, denominator: int) -> float | None:
    """安全比例。"""
    if denominator == 0:
        return None
    return value / denominator


def effective_support(value: int, denominator: int) -> float | None:
    """把最大桶占比转成有效支撑数。"""
    if value == 0:
        return None
    return denominator / value


def bridge_route(total_hole_demand: int, high_primes: list[int]) -> str:
    """给连续 cap 分配结构路由。"""
    if total_hole_demand == 0:
        return "NoTailDemandSparseOrLocalSurvivor"
    if not high_primes:
        return "TailPrimeMissingInconsistentNeedsLocalCheck"
    return "ContinuousCapActualPaymentSelectionDichotomy"


def analyze_continuous_row(
    p: int,
    q: int,
    top_index: int,
    arc_row: dict[str, Any],
    mult_item: dict[str, Any],
    top_limit: int,
) -> dict[str, Any]:
    """分析一个连续方向弧 top row 的 column-tail 暴露账本。"""
    m_vector = [int(value) for value in mult_item["m_vector"]]
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    h = int(arc_row["h"])
    zeta_turn = float(arc_row["best_zeta_turn"])
    phases = positive_cap_phases(m_vector, q, h, zeta_turn)

    cap_mass = sum(m_vector[phase] for phase in phases)
    phase_count_by_holes: Counter[int] = Counter()
    prime_exposure: Counter[str] = Counter()
    residue_exposure: Counter[str] = Counter()
    column_residue_exposure: Counter[str] = Counter()
    payment_signature_exposure: Counter[str] = Counter()
    total_hole_demand = 0
    zero_hole_phase_count = 0

    for phase in phases:
        mass = m_vector[phase]
        holes = low_holes_for_phase(p, q, low_primes, phase)
        phase_count_by_holes[len(holes)] += 1
        if not holes:
            zero_hole_phase_count += 1
            continue
        total_hole_demand += mass * len(holes)
        for col in holes:
            for prime in high_primes:
                residue = residue_for_hole(p, q, phase, col, prime)
                prime_exposure[str(prime)] += mass
                residue_exposure[f"{prime}:{residue}"] += mass
                column_residue_exposure[f"{prime}:{col % prime}"] += mass
                payment_signature_exposure[f"{prime}:{residue}:{col % prime}"] += mass

    max_prime = max(prime_exposure.values(), default=0)
    max_residue = max(residue_exposure.values(), default=0)
    max_colres = max(column_residue_exposure.values(), default=0)
    max_payment_signature = max(payment_signature_exposure.values(), default=0)
    max_signature_share = share(max_payment_signature, total_hole_demand)
    route = bridge_route(total_hole_demand, high_primes)
    reported_phase_count = int(arc_row["cap_phase_count"])
    reported_mass = int(round(float(arc_row["cap_mass"])))

    return {
        "p": p,
        "q": q,
        "top_index": top_index,
        "h": h,
        "zeta_turn": zeta_turn,
        "box_dual_value_over_total_m": arc_row["box_dual_value_over_total_m"],
        "reported_cap_phase_count": reported_phase_count,
        "recomputed_cap_phase_count": len(phases),
        "cap_phase_count_matches": len(phases) == reported_phase_count,
        "reported_cap_mass": reported_mass,
        "recomputed_cap_mass": cap_mass,
        "cap_mass_matches": cap_mass == reported_mass,
        "cap_mass_share": arc_row["cap_mass_share"],
        "low_primes": low_primes,
        "high_primes": high_primes,
        "high_prime_count": len(high_primes),
        "zero_hole_phase_count": zero_hole_phase_count,
        "phase_count_by_holes": dict(sorted(phase_count_by_holes.items())),
        "total_hole_demand": total_hole_demand,
        "max_prime_exposure": max_prime,
        "max_prime_exposure_share": share(max_prime, total_hole_demand),
        "max_residue_exposure": max_residue,
        "max_residue_exposure_share": share(max_residue, total_hole_demand),
        "max_column_residue_exposure": max_colres,
        "max_column_residue_exposure_share": share(max_colres, total_hole_demand),
        "max_payment_signature_exposure": max_payment_signature,
        "max_payment_signature_share": max_signature_share,
        "effective_prime_support": effective_support(max_prime, total_hole_demand),
        "effective_residue_support": effective_support(max_residue, total_hole_demand),
        "effective_column_residue_support": effective_support(max_colres, total_hole_demand),
        "effective_payment_signature_support": effective_support(
            max_payment_signature, total_hole_demand
        ),
        "top_prime_exposure": top_counter(prime_exposure, top_limit),
        "top_residue_exposure": top_counter(residue_exposure, top_limit),
        "top_column_residue_exposure": top_counter(column_residue_exposure, top_limit),
        "top_payment_signature_exposure": top_counter(payment_signature_exposure, top_limit),
        "structural_route": route,
    }


def run(
    continuous_path: Path,
    mult_path: Path,
    top_rows_per_p: int,
    top_limit: int,
) -> dict[str, Any]:
    """运行连续弧 column-tail 桥接。"""
    continuous = load_json(continuous_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    cap_reports = []
    for prime_row in continuous["prime_results"]:
        p = int(prime_row["p"])
        q = int(prime_row["q"])
        for index, arc_row in enumerate(prime_row["top_continuous_arc_rows"][:top_rows_per_p]):
            cap_reports.append(
                analyze_continuous_row(
                    p=p,
                    q=q,
                    top_index=index,
                    arc_row=arc_row,
                    mult_item=mult_by_p[p],
                    top_limit=top_limit,
                )
            )

    route_counts = Counter(row["structural_route"] for row in cap_reports)
    p_level_rows = []
    for p in sorted({int(row["p"]) for row in cap_reports}):
        rows = [row for row in cap_reports if int(row["p"]) == p]
        positive = [row for row in rows if row["total_hole_demand"] > 0]
        p_level_rows.append(
            {
                "p": p,
                "cap_count": len(rows),
                "positive_demand_cap_count": len(positive),
                "max_box_dual_value_over_total_m": max(
                    row["box_dual_value_over_total_m"] or 0.0 for row in rows
                ),
                "max_payment_signature_share": max(
                    (row["max_payment_signature_share"] or 0.0 for row in rows),
                    default=0.0,
                ),
                "min_effective_payment_signature_support": min(
                    (
                        row["effective_payment_signature_support"]
                        for row in positive
                        if row["effective_payment_signature_support"] is not None
                    ),
                    default=None,
                ),
                "routes": dict(Counter(row["structural_route"] for row in rows)),
            }
        )

    return {
        "certificate_type": "triad_a1_continuous_columntail_bridge",
        "status": "continuous_dualcap_columntail_bridge_materialized",
        "q": int(continuous["q"]),
        "parameters": {
            "top_rows_per_p": top_rows_per_p,
            "top_limit": top_limit,
        },
        "source_hashes": {
            "continuous_columntail_bridge_script": file_sha256(Path(__file__).resolve()),
            "continuous_direction_arc_json": file_sha256(continuous_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "cap_report_count": len(cap_reports),
        "all_cap_recomputations_match": all(
            row["cap_phase_count_matches"] and row["cap_mass_matches"]
            for row in cap_reports
        ),
        "route_counts": dict(sorted(route_counts.items())),
        "p_level_rows": p_level_rows,
        "cap_reports": cap_reports,
        "recursive_peeling_law": (
            "对连续方向 persistent cap 的每个低洞，真实反例必须选择某个 tail prime residue 支付。"
            "若某个 payment signature 在无限子族中持久占正比例，则该签名给出 column/tail PDEC 行；"
            "若任意固定签名的比例都被递归剥离到 0，则支付测度扩散，进入 CleanKLS/DLS。"
            "该接口不依赖预设全局常数，而依赖 limsup 正质量或 diffuse 极限二分。"
        ),
        "review_conclusion": (
            "连续方向弧 DualCap 已接到 column-tail 暴露账本。当前步骤仍未证明最终 U_CRT<L_PDEC，"
            "但把下一硬点推进为 ActualPaymentSelection：真实支付若集中则进 PDEC，若不集中则进 CleanKLS/DLS。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 连续弧 ColumnTail 桥接",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 递归剥离律",
        "",
        result["recursive_peeling_law"],
        "",
        "```text",
        "continuous cap C",
        "=> low-hole demand D_C",
        "=> actual tail payment measure mu_C on (prime,residue,column-residue)",
        "=> limsup positive signature -> column/tail PDEC",
        "=> all fixed signatures vanish -> diffuse CleanKLS/DLS。",
        "```",
        "",
        "本文登记的是暴露账本：所有真实支付签名都必须落在这些候选桶中；actual payment 选择仍是下一硬点。",
        "",
        "## 2. 汇总",
        "",
        f"- `cap_report_count={result['cap_report_count']}`。",
        f"- `all_cap_recomputations_match={result['all_cap_recomputations_match']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `parameters={result['parameters']}`。",
        "",
        "## 3. P 级桥接读数",
        "",
        "| P | caps | positive demand caps | max U_box/M | max payment sig share | min effective sig support | routes |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["p_level_rows"]:
        lines.append(
            "| {p} | {caps} | {positive} | {u} | {share} | {support} | `{routes}` |".format(
                p=row["p"],
                caps=row["cap_count"],
                positive=row["positive_demand_cap_count"],
                u=fmt_float(row["max_box_dual_value_over_total_m"]),
                share=fmt_float(row["max_payment_signature_share"]),
                support=fmt_float(row["min_effective_payment_signature_support"]),
                routes=row["routes"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap 明细",
            "",
            "| P | top | h | zeta | phases | mass share | demand | max sig share | eff sig support | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_reports"]:
        lines.append(
            "| {p} | {top} | {h} | {zeta} | {phases} | {mass} | {demand} | {share} | {support} | `{route}` |".format(
                p=row["p"],
                top=row["top_index"],
                h=row["h"],
                zeta=fmt_float(row["zeta_turn"]),
                phases=row["recomputed_cap_phase_count"],
                mass=fmt_float(row["cap_mass_share"]),
                demand=row["total_hole_demand"],
                share=fmt_float(row["max_payment_signature_share"]),
                support=fmt_float(row["effective_payment_signature_support"]),
                route=row["structural_route"],
            )
        )

    lines.extend(["", "## 5. Top 暴露签名", ""])
    for row in result["cap_reports"]:
        lines.extend(
            [
                f"### P={row['p']} top={row['top_index']} h={row['h']} zeta={fmt_float(row['zeta_turn'])}",
                "",
                f"- `phase_count_by_holes={row['phase_count_by_holes']}`。",
                f"- top payment signatures: `{row['top_payment_signature_exposure']}`。",
                f"- top residues: `{row['top_residue_exposure']}`。",
                f"- top column residues: `{row['top_column_residue_exposure']}`。",
                "",
            ]
        )

    lines.extend(
        [
            "## 6. 当前硬点",
            "",
            "这一步关闭的是“连续 cap 与 column-tail 无关”的退路。剩余真正硬点是：",
            "",
            "```text",
            "ActualPaymentSelection:",
            "  从暴露候选桶提升到真实支付测度；",
            "  证明 limsup 正质量签名产生合法 PDEC 行；",
            "  证明所有签名递归剥离为 0 时满足 CleanKLS/DLS 输入条件。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--continuous-json", type=Path, default=DEFAULT_CONTINUOUS)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--top-rows-per-p", type=int, default=1)
    parser.add_argument("--top-limit", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        continuous_path=args.continuous_json,
        mult_path=args.multiplicity_json,
        top_rows_per_p=args.top_rows_per_p,
        top_limit=args.top_limit,
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
                "cap_report_count": result["cap_report_count"],
                "all_cap_recomputations_match": result["all_cap_recomputations_match"],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
