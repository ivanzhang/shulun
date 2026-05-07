#!/usr/bin/env python3
"""审计 Triad-A1 ForcedCap 的 column-tail 需求暴露签名。

用法示例：
  python3 experiments/prime_matrix_triad_a1_forcedcap_columntail_payment_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-forcedcap-columntail-payment.json
  docs/monograph/prime-matrix-triad-a1-forcedcap-columntail-payment.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase
from prime_matrix_triad_a1_pdec_dualcap_extractor import cap_phases


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-forcedcap-columntail-payment.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-forcedcap-columntail-payment.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析逗号分隔 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def forced_caps_from_dualcap(
    dualcap: dict[str, Any],
    p_filter: set[int] | None,
) -> list[dict[str, Any]]:
    """抽取 ForcedPersistentByDensityBarrier cap 描述符。"""
    caps = []
    seen: set[tuple[int, float, float, int, str]] = set()
    for prime_item in dualcap["prime_results"]:
        p = int(prime_item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        for cap in prime_item["top_caps"]:
            if cap["classification"] != "ForcedPersistentByDensityBarrier":
                continue
            key = (
                p,
                float(cap["alpha"]),
                float(cap["direction"]),
                int(cap["h"]),
                str(cap["source"]),
            )
            if key in seen:
                continue
            seen.add(key)
            caps.append(
                {
                    "p": p,
                    "q": int(cap["q"]),
                    "alpha": float(cap["alpha"]),
                    "direction": float(cap["direction"]),
                    "h": int(cap["h"]),
                    "source": cap["source"],
                    "reported_intersection_size": int(cap["intersection_size"]),
                    "reported_intersection_mass": int(cap["intersection_mass"]),
                    "reported_mass_share": cap["mass_share_of_total_m"],
                    "density_barrier_lower_bound": int(
                        cap["density_barrier_lower_bound"]
                    ),
                }
            )
    return caps


def residue_for_hole(p: int, q: int, phase: int, col: int, prime: int) -> int:
    """给出高素数 prime 覆盖列 col 所需的 fiber residue y mod prime。"""
    inverse_p = pow(p, -1, prime)
    inverse_q = pow(q % prime, -1, prime)
    target_row_residue = (1 - col * inverse_p) % prime
    return ((target_row_residue - phase) * inverse_q) % prime


def analyze_cap_exposure(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    top_limit: int,
) -> dict[str, Any]:
    """聚合一个 ForcedCap 的 column-tail 需求暴露账本。

    这是轻量账本：它统计每个低洞可由哪些高素数 residue 支付的需求暴露，
    不枚举所有完成态的实际支付选择。
    """
    p = int(cap["p"])
    q = int(cap["q"])
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    m_vector = [int(value) for value in mult_item["m_vector"]]
    support = {idx for idx, value in enumerate(m_vector) if value > 0}
    phases = [
        phase for phase in cap_phases(q, cap["alpha"], cap["direction"], cap["h"])
        if phase in support
    ]

    prime_exposure: Counter[str] = Counter()
    residue_exposure: Counter[str] = Counter()
    column_residue_exposure: Counter[str] = Counter()
    phase_count_by_holes: Counter[int] = Counter()
    zero_hole_phase_count = 0
    total_mass = 0
    total_hole_demand = 0
    total_exposure_incidence = 0

    for phase in phases:
        mass = m_vector[phase]
        total_mass += mass
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
                total_exposure_incidence += mass

    max_prime = max(prime_exposure.values(), default=0)
    max_residue = max(residue_exposure.values(), default=0)
    max_column_residue = max(column_residue_exposure.values(), default=0)
    return {
        **cap,
        "intersection_size_recomputed": len(phases),
        "intersection_size_matches": len(phases) == cap["reported_intersection_size"],
        "intersection_mass_recomputed": total_mass,
        "intersection_mass_matches": total_mass == cap["reported_intersection_mass"],
        "high_primes": high_primes,
        "high_prime_count": len(high_primes),
        "zero_hole_phase_count": zero_hole_phase_count,
        "phase_count_by_holes": dict(sorted(phase_count_by_holes.items())),
        "total_hole_demand": total_hole_demand,
        "total_exposure_incidence": total_exposure_incidence,
        "exposure_over_demand": (
            total_exposure_incidence / total_hole_demand if total_hole_demand else None
        ),
        "max_prime_exposure": max_prime,
        "max_prime_exposure_over_demand": (
            max_prime / total_hole_demand if total_hole_demand else None
        ),
        "max_residue_exposure": max_residue,
        "max_residue_exposure_over_demand": (
            max_residue / total_hole_demand if total_hole_demand else None
        ),
        "max_column_residue_exposure": max_column_residue,
        "max_column_residue_exposure_over_demand": (
            max_column_residue / total_hole_demand if total_hole_demand else None
        ),
        "top_prime_exposure": [
            {"key": key, "count": count}
            for key, count in prime_exposure.most_common(top_limit)
        ],
        "top_residue_exposure": [
            {"key": key, "count": count}
            for key, count in residue_exposure.most_common(top_limit)
        ],
        "top_column_residue_exposure": [
            {"key": key, "count": count}
            for key, count in column_residue_exposure.most_common(top_limit)
        ],
        "structural_route": (
            "NoTailDemandFinitePDEC"
            if total_hole_demand == 0
            else "ForcedColumnTailExposurePDECOrDistributedCleanKLS"
        ),
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    p_filter: set[int] | None,
    top_limit: int,
) -> dict[str, Any]:
    """运行 ForcedCap column-tail 暴露审计。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    caps = forced_caps_from_dualcap(dualcap, p_filter)
    cap_reports = [
        analyze_cap_exposure(
            cap=cap,
            mult_item=mult_by_p[int(cap["p"])],
            top_limit=top_limit,
        )
        for cap in caps
    ]
    route_counts = Counter(row["structural_route"] for row in cap_reports)
    p_level_effective_support = []
    for p in sorted({int(row["p"]) for row in cap_reports}):
        rows = [
            row for row in cap_reports
            if int(row["p"]) == p and row["total_hole_demand"] > 0
        ]
        if not rows:
            continue
        p_level_effective_support.append(
            {
                "p": p,
                "cap_count": len(rows),
                "min_effective_prime_exposure_support": min(
                    row["total_hole_demand"] / row["max_prime_exposure"]
                    for row in rows
                    if row["max_prime_exposure"] > 0
                ),
                "min_effective_residue_exposure_support": min(
                    row["total_hole_demand"] / row["max_residue_exposure"]
                    for row in rows
                    if row["max_residue_exposure"] > 0
                ),
                "min_effective_column_residue_exposure_support": min(
                    row["total_hole_demand"] / row["max_column_residue_exposure"]
                    for row in rows
                    if row["max_column_residue_exposure"] > 0
                ),
                "max_residue_exposure_share": max(
                    row["max_residue_exposure_over_demand"] or 0.0
                    for row in rows
                ),
                "max_column_residue_exposure_share": max(
                    row["max_column_residue_exposure_over_demand"] or 0.0
                    for row in rows
                ),
            }
        )
    return {
        "certificate_type": "triad_a1_forcedcap_columntail_payment_audit",
        "status": "forced_caps_columntail_exposure_materialized",
        "q": int(dualcap["q"]),
        "source_hashes": {
            "forcedcap_columntail_exposure_script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "p_values": sorted({int(row["p"]) for row in cap_reports}),
        "forced_cap_count": len(cap_reports),
        "all_intersections_recomputed": all(
            row["intersection_size_matches"] and row["intersection_mass_matches"]
            for row in cap_reports
        ),
        "route_counts": dict(sorted(route_counts.items())),
        "p_level_effective_support": p_level_effective_support,
        "cap_reports": cap_reports,
        "review_conclusion": (
            "ForcedCap 的旧层低洞需求暴露已物化为 column-tail 签名账本。"
            "这是轻量 exposure ledger，不声称已经枚举完成态实际支付选择；"
            "它把 forced cap 的下一终端输入压成固定签名 PDEC 或分散 CleanKLS/DLS。"
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
        "# Triad-A1 ForcedCap ColumnTail 暴露审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构语义",
        "",
        "对 `ForcedPersistentByDensityBarrier`，固定 `Q` 同层 cap 已由密度屏障判定不能闭合；但 cap 内低洞仍必须由高素数 residue 支付。",
        "本文先登记轻量暴露账本：对每个低洞列和每个高素数，计算可覆盖该洞的唯一 fiber residue，并按 `M(phase)` 加权。",
        "",
        "```text",
        "D_C = sum_{phase in C} M(phase) * |H_low(phase)|；",
        "exposure(prime,residue,column) += M(phase)。",
        "```",
        "",
        "暴露账本不是完整支付选择枚举；它给出 forced cap 后续 PDEC/ColumnTail 证书必须面对的候选签名。",
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
            f"- `forced_cap_count={result['forced_cap_count']}`。",
            f"- `all_intersections_recomputed={result['all_intersections_recomputed']}`。",
            f"- `route_counts={result['route_counts']}`。",
            "",
            "## 4. P 级有效暴露支撑",
            "",
            "| P | caps | min eff prime exposure | min eff residue exposure | min eff column-residue exposure | max residue exposure share | max colres exposure share |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["p_level_effective_support"]:
        lines.append(
            "| {p} | {caps} | {ep} | {er} | {ec} | {rs} | {cs} |".format(
                p=row["p"],
                caps=row["cap_count"],
                ep=fmt_float(row["min_effective_prime_exposure_support"]),
                er=fmt_float(row["min_effective_residue_exposure_support"]),
                ec=fmt_float(row["min_effective_column_residue_exposure_support"]),
                rs=fmt_float(row["max_residue_exposure_share"]),
                cs=fmt_float(row["max_column_residue_exposure_share"]),
            )
        )

    lines.extend(
        [
            "",
            "## 5. Cap 明细",
            "",
            "| P | alpha | h | dir | mass | demand | exposure/demand | max residue exposure/demand | max colres exposure/demand | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_reports"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {mass} | {demand} | {eod} | {mrd} | {mcd} | `{route}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                mass=row["intersection_mass_recomputed"],
                demand=row["total_hole_demand"],
                eod=fmt_float(row["exposure_over_demand"]),
                mrd=fmt_float(row["max_residue_exposure_over_demand"]),
                mcd=fmt_float(row["max_column_residue_exposure_over_demand"]),
                route=row["structural_route"],
            )
        )

    lines.extend(["", "## 6. Top 暴露签名", ""])
    for row in result["cap_reports"]:
        lines.extend(
            [
                f"### P={row['p']} alpha={fmt_float(row['alpha'])} h={row['h']} dir={fmt_float(row['direction'])} source={row['source']}",
                "",
                f"- `phase_count_by_holes={row['phase_count_by_holes']}`。",
                f"- top prime exposure: `{row['top_prime_exposure']}`。",
                f"- top residue exposure: `{row['top_residue_exposure']}`。",
                f"- top column-residue exposure: `{row['top_column_residue_exposure']}`。",
                "",
            ]
        )

    lines.extend(
        [
            "## 7. 读法",
            "",
            "这一步没有排除 forced cap；它把 forced cap 的 column-tail 终端义务物化为轻量签名账本。",
            "若某个暴露签名在正式反例族中持久承担实际支付，就进入 TailAnchor/ColumnCRT PDEC。",
            "若实际支付不能固定在这些 top 签名上，则 forced cap 只能继续升层或进入分散 CleanKLS/DLS。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--p-values", type=str, default="43,47")
    parser.add_argument("--top-limit", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        dualcap_path=args.dualcap_json,
        mult_path=args.multiplicity_json,
        p_filter=parse_p_values(args.p_values),
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
                "forced_cap_count": result["forced_cap_count"],
                "all_intersections_recomputed": result["all_intersections_recomputed"],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
