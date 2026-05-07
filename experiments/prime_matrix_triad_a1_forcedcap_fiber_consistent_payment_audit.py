#!/usr/bin/env python3
"""审计 ForcedCap 的 fiber-consistent actual-payment incidence。

用法示例：
  python3 experiments/prime_matrix_triad_a1_forcedcap_fiber_consistent_payment_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.json
  docs/monograph/prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any

from prime_matrix_triad_a1_forcedcap_columntail_payment_audit import (
    file_sha256,
    forced_caps_from_dualcap,
    load_json,
    parse_p_values,
)
from prime_matrix_triad_a1_pdec_dualcap_extractor import cap_phases
from prime_matrix_triad_a1_persistent_columntail_payment_audit import (
    bit_positions,
    residue_options,
    top_counter,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.md"


def superset_sums(counts: dict[int, int], bit_count: int) -> list[int]:
    """计算每个 mask 的所有超集计数和。"""
    size = 1 << bit_count
    values = [0] * size
    for mask, count in counts.items():
        values[mask] = count
    for bit in range(bit_count):
        step = 1 << bit
        for mask in range(size):
            if (mask & step) == 0:
                values[mask] += values[mask | step]
    return values


def fast_phase_payment_signature(
    p: int,
    q: int,
    phase: int,
    low_primes: list[int],
    high_primes: list[int],
) -> dict[str, Any]:
    """快速计算单相位的 fiber-consistent cover incidence。"""
    from math import prod

    from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase

    holes = low_holes_for_phase(p, q, low_primes, phase)
    high_period = prod(high_primes) if high_primes else 1
    if not holes:
        return {
            "phase": phase,
            "holes": holes,
            "completion_count": high_period,
            "hole_demand": 0,
            "cover_incidence": 0,
            "prime_cover": {},
            "residue_cover": {},
            "column_residue_cover": {},
            "active_prime": {},
            "max_dp_state_count": 1,
        }

    full_mask = (1 << len(holes)) - 1
    options_by_prime = [
        (prime, residue_options(p, q, phase, holes, prime))
        for prime in high_primes
    ]

    prefix: list[dict[int, int]] = [{0: 1}]
    for _prime, options in options_by_prime:
        option_counter = Counter(mask for _residue, mask in options)
        next_dp: dict[int, int] = {}
        for old_mask, old_count in prefix[-1].items():
            for option_mask, multiplicity in option_counter.items():
                new_mask = old_mask | option_mask
                next_dp[new_mask] = next_dp.get(new_mask, 0) + old_count * multiplicity
        prefix.append(next_dp)

    suffix: list[dict[int, int]] = [{} for _ in range(len(options_by_prime) + 1)]
    suffix[-1] = {0: 1}
    for idx in range(len(options_by_prime) - 1, -1, -1):
        _prime, options = options_by_prime[idx]
        option_counter = Counter(mask for _residue, mask in options)
        next_dp: dict[int, int] = {}
        for old_mask, old_count in suffix[idx + 1].items():
            for option_mask, multiplicity in option_counter.items():
                new_mask = old_mask | option_mask
                next_dp[new_mask] = next_dp.get(new_mask, 0) + old_count * multiplicity
        suffix[idx] = next_dp

    suffix_supersets = [
        superset_sums(row, len(holes))
        for row in suffix
    ]
    completion_count = prefix[-1].get(full_mask, 0)
    prime_cover: Counter[str] = Counter()
    residue_cover: Counter[str] = Counter()
    column_residue_cover: Counter[str] = Counter()
    active_prime: Counter[str] = Counter()

    for idx, (prime, options) in enumerate(options_by_prime):
        suffix_sum = suffix_supersets[idx + 1]
        for residue, option_mask in options:
            if option_mask == 0:
                continue
            use_count = 0
            for left_mask, left_count in prefix[idx].items():
                missing = full_mask & ~(left_mask | option_mask)
                use_count += left_count * suffix_sum[missing]
            if use_count == 0:
                continue
            key_prime = str(prime)
            key_residue = f"{prime}:{residue}"
            active_prime[key_prime] += use_count
            covered_cols = bit_positions(option_mask, holes)
            for col in covered_cols:
                prime_cover[key_prime] += use_count
                residue_cover[key_residue] += use_count
                column_residue_cover[f"{prime}:{col % prime}"] += use_count

    cover_incidence = sum(prime_cover.values())
    return {
        "phase": phase,
        "holes": holes,
        "completion_count": completion_count,
        "hole_demand": completion_count * len(holes),
        "cover_incidence": cover_incidence,
        "prime_cover": dict(prime_cover),
        "residue_cover": dict(residue_cover),
        "column_residue_cover": dict(column_residue_cover),
        "active_prime": dict(active_prime),
        "max_dp_state_count": max(len(row) for row in [*prefix, *suffix]),
    }


def analyze_cap(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    phase_cache: dict[tuple[int, int], dict[str, Any]],
    top_limit: int,
) -> dict[str, Any]:
    """聚合一个 ForcedCap 的 fiber-consistent 支付 incidence。"""
    p = int(cap["p"])
    q = int(cap["q"])
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    m_vector = [int(value) for value in mult_item["m_vector"]]
    support = {idx for idx, value in enumerate(m_vector) if value > 0}
    phases = [
        phase
        for phase in cap_phases(q, cap["alpha"], cap["direction"], cap["h"])
        if phase in support
    ]

    prime_cover: Counter[str] = Counter()
    residue_cover: Counter[str] = Counter()
    column_residue_cover: Counter[str] = Counter()
    active_prime: Counter[str] = Counter()
    total_completion_mass = 0
    total_hole_demand = 0
    total_cover_incidence = 0
    max_dp_state_count = 0
    phase_count_by_holes: Counter[int] = Counter()
    mismatch_count = 0

    for phase in phases:
        key = (p, phase)
        if key not in phase_cache:
            phase_cache[key] = fast_phase_payment_signature(
                p=p,
                q=q,
                phase=phase,
                low_primes=low_primes,
                high_primes=high_primes,
            )
        row = phase_cache[key]
        completion_count = int(row["completion_count"])
        if completion_count != m_vector[phase]:
            mismatch_count += 1
        total_completion_mass += completion_count
        total_hole_demand += int(row["hole_demand"])
        total_cover_incidence += int(row["cover_incidence"])
        max_dp_state_count = max(max_dp_state_count, int(row["max_dp_state_count"]))
        phase_count_by_holes[len(row["holes"])] += 1
        prime_cover.update({key: int(value) for key, value in row["prime_cover"].items()})
        residue_cover.update({key: int(value) for key, value in row["residue_cover"].items()})
        column_residue_cover.update(
            {key: int(value) for key, value in row["column_residue_cover"].items()}
        )
        active_prime.update({key: int(value) for key, value in row["active_prime"].items()})

    max_prime_cover = max(prime_cover.values(), default=0)
    max_residue_cover = max(residue_cover.values(), default=0)
    max_column_residue_cover = max(column_residue_cover.values(), default=0)
    max_active_prime = max(active_prime.values(), default=0)
    return {
        **cap,
        "intersection_size_recomputed": len(phases),
        "intersection_size_matches": len(phases) == cap["reported_intersection_size"],
        "intersection_mass_recomputed": total_completion_mass,
        "intersection_mass_matches": total_completion_mass == cap["reported_intersection_mass"],
        "mismatch_count": mismatch_count,
        "high_primes": high_primes,
        "high_prime_count": len(high_primes),
        "phase_count_by_holes": dict(sorted(phase_count_by_holes.items())),
        "total_hole_demand": total_hole_demand,
        "total_cover_incidence": total_cover_incidence,
        "cover_over_demand": (
            total_cover_incidence / total_hole_demand if total_hole_demand else None
        ),
        "max_prime_cover": max_prime_cover,
        "max_prime_cover_over_demand": (
            max_prime_cover / total_hole_demand if total_hole_demand else None
        ),
        "max_residue_cover": max_residue_cover,
        "max_residue_cover_over_demand": (
            max_residue_cover / total_hole_demand if total_hole_demand else None
        ),
        "max_column_residue_cover": max_column_residue_cover,
        "max_column_residue_cover_over_demand": (
            max_column_residue_cover / total_hole_demand if total_hole_demand else None
        ),
        "max_active_prime": max_active_prime,
        "max_active_prime_over_completion_mass": (
            max_active_prime / total_completion_mass if total_completion_mass else None
        ),
        "top_prime_cover": top_counter(prime_cover, top_limit),
        "top_residue_cover": top_counter(residue_cover, top_limit),
        "top_column_residue_cover": top_counter(column_residue_cover, top_limit),
        "top_active_prime": top_counter(active_prime, top_limit),
        "max_dp_state_count": max_dp_state_count,
        "structural_route": (
            "FiberConsistentPaymentMFUOrDistributedCleanKLS"
            if total_hole_demand > 0
            else "NoTailDemandFinitePDEC"
        ),
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    p_filter: set[int] | None,
    top_limit: int,
) -> dict[str, Any]:
    """运行 ForcedCap fiber-consistent 支付审计。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    caps = forced_caps_from_dualcap(dualcap, p_filter)
    phase_cache: dict[tuple[int, int], dict[str, Any]] = {}
    cap_reports = [
        analyze_cap(
            cap=cap,
            mult_item=mult_by_p[int(cap["p"])],
            phase_cache=phase_cache,
            top_limit=top_limit,
        )
        for cap in caps
    ]
    route_counts = Counter(row["structural_route"] for row in cap_reports)
    p_summary = []
    for p in sorted({int(row["p"]) for row in cap_reports}):
        subset = [
            row for row in cap_reports
            if int(row["p"]) == p and int(row["total_hole_demand"]) > 0
        ]
        if not subset:
            continue
        p_summary.append(
            {
                "p": p,
                "cap_count": len(subset),
                "max_cover_over_demand": max(
                    row["cover_over_demand"] or 0.0 for row in subset
                ),
                "max_residue_cover_over_demand": max(
                    row["max_residue_cover_over_demand"] or 0.0 for row in subset
                ),
                "max_column_residue_cover_over_demand": max(
                    row["max_column_residue_cover_over_demand"] or 0.0
                    for row in subset
                ),
                "max_active_prime_over_completion_mass": max(
                    row["max_active_prime_over_completion_mass"] or 0.0
                    for row in subset
                ),
                "max_dp_state_count": max(row["max_dp_state_count"] for row in subset),
            }
        )
    return {
        "certificate_type": "triad_a1_forcedcap_fiber_consistent_payment_audit",
        "status": "forcedcap_fiber_consistent_payment_incidence_materialized",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_json": file_sha256(mult_path),
        },
        "forced_cap_count": len(cap_reports),
        "all_intersections_recomputed": all(
            row["intersection_size_matches"] and row["intersection_mass_matches"]
            for row in cap_reports
        ),
        "all_completion_counts_match_m_vector": all(
            row["mismatch_count"] == 0 for row in cap_reports
        ),
        "route_counts": dict(sorted(route_counts.items())),
        "unique_phase_cache_count": len(phase_cache),
        "p_summary": p_summary,
        "cap_reports": cap_reports,
        "review_conclusion": (
            "ForcedCap 的 actual-payment incidence 已加入 fiber 一致性：同一 phase 的所有低洞必须来自同一个 "
            "CRT fiber y 的完成态。该账本仍是 incidence 上界，不等同于最小支付选择 Gamma；但它比裸 exposure "
            "更接近 ActualPaymentStitching，下一步可在此基础上做持久 MFU 或 CleanKLS 二分。"
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
        "# Triad-A1 ForcedCap Fiber-Consistent 支付审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构语义",
        "",
        "这一步把 APS 中的 `Gamma` 约束推进一层：实际完成态不是任意选择暴露边，而是由同一个 fiber 参数 `y` 同时决定所有高素数 residue。",
        "",
        "```text",
        "phase t 固定；",
        "row = t + Qy；",
        "同一个 y mod high_period 必须覆盖该 phase 的全部低洞。",
        "```",
        "",
        "因此本报告统计的是所有完成 `y` 诱导出的 fiber-consistent cover incidence。",
        "",
        "## 2. 汇总",
        "",
        f"- `forced_cap_count={result['forced_cap_count']}`。",
        f"- `unique_phase_cache_count={result['unique_phase_cache_count']}`。",
        f"- `all_intersections_recomputed={result['all_intersections_recomputed']}`。",
        f"- `all_completion_counts_match_m_vector={result['all_completion_counts_match_m_vector']}`。",
        f"- `route_counts={result['route_counts']}`。",
        "",
        "## 3. P 级汇总",
        "",
        "| P | caps | max cover/demand | max residue/demand | max colres/demand | max active-prime/completion | max DP states |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["p_summary"]:
        lines.append(
            "| {p} | {caps} | {cover} | {res} | {colres} | {active} | {states} |".format(
                p=row["p"],
                caps=row["cap_count"],
                cover=fmt_float(row["max_cover_over_demand"]),
                res=fmt_float(row["max_residue_cover_over_demand"]),
                colres=fmt_float(row["max_column_residue_cover_over_demand"]),
                active=fmt_float(row["max_active_prime_over_completion_mass"]),
                states=row["max_dp_state_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap 明细",
            "",
            "| P | alpha | h | dir | mass | demand | cover/demand | max residue/demand | max colres/demand | max active-prime/completion | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_reports"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {mass} | {demand} | {cover} | {res} | {colres} | {active} | `{route}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                mass=row["intersection_mass_recomputed"],
                demand=row["total_hole_demand"],
                cover=fmt_float(row["cover_over_demand"]),
                res=fmt_float(row["max_residue_cover_over_demand"]),
                colres=fmt_float(row["max_column_residue_cover_over_demand"]),
                active=fmt_float(row["max_active_prime_over_completion_mass"]),
                route=row["structural_route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "如果某个 fiber-consistent 签名持久承担实际支付，它就是 MFU/PDEC 输入。",
            "如果实际支付在这些 fiber-consistent 签名之间持续分散，则进入 CleanKLS/DLS。",
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
    parser.add_argument("--top-limit", type=int, default=8)
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
                "all_completion_counts_match_m_vector": result[
                    "all_completion_counts_match_m_vector"
                ],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
