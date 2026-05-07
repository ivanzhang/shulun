#!/usr/bin/env python3
"""审计 Triad-A1 PersistentCap 的 column-tail 支付签名。

用法示例：
  python3 experiments/prime_matrix_triad_a1_persistent_columntail_payment_audit.py
  python3 experiments/prime_matrix_triad_a1_persistent_columntail_payment_audit.py --p-values 19,23,29,31,37

输出：
  docs/monograph/prime-matrix-triad-a1-persistent-columntail-payment.json
  docs/monograph/prime-matrix-triad-a1-persistent-columntail-payment.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import low_holes_for_phase
from prime_matrix_triad_a1_pdec_dualcap_extractor import cap_phases


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-persistent-columntail-payment.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-persistent-columntail-payment.md"


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析逗号分隔 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def bit_positions(mask: int, holes: list[int]) -> list[int]:
    """把覆盖掩码转回列号。"""
    return [col for idx, col in enumerate(holes) if (mask >> idx) & 1]


def residue_options(
    p: int,
    q: int,
    phase: int,
    holes: list[int],
    prime: int,
) -> list[tuple[int, int]]:
    """返回给定高素数的 `(residue, cover_mask)` 选项。"""
    if not holes:
        return [(residue, 0) for residue in range(prime)]
    inverse_p = pow(p, -1, prime)
    inverse_q = pow(q % prime, -1, prime)
    hole_index = {col: index for index, col in enumerate(holes)}
    table = [0] * prime
    for col in holes:
        target_row_residue = (1 - col * inverse_p) % prime
        y_residue = ((target_row_residue - phase) * inverse_q) % prime
        table[y_residue] |= 1 << hole_index[col]
    return list(enumerate(table))


def phase_payment_signature(
    p: int,
    q: int,
    phase: int,
    low_primes: list[int],
    high_primes: list[int],
) -> dict[str, Any]:
    """计算单相位的 completion 数和 column-tail 支付签名。"""
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
        next_dp: dict[int, int] = {}
        option_counter = Counter(mask for _residue, mask in options)
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
        next_dp = {}
        for old_mask, old_count in suffix[idx + 1].items():
            for option_mask, multiplicity in option_counter.items():
                new_mask = old_mask | option_mask
                next_dp[new_mask] = next_dp.get(new_mask, 0) + old_count * multiplicity
        suffix[idx] = next_dp

    completion_count = prefix[-1].get(full_mask, 0)
    prime_cover: Counter[str] = Counter()
    residue_cover: Counter[str] = Counter()
    column_residue_cover: Counter[str] = Counter()
    active_prime: Counter[str] = Counter()

    for idx, (prime, options) in enumerate(options_by_prime):
        for residue, option_mask in options:
            if option_mask == 0:
                continue
            use_count = 0
            for left_mask, left_count in prefix[idx].items():
                joined = left_mask | option_mask
                for right_mask, right_count in suffix[idx + 1].items():
                    if (joined | right_mask) == full_mask:
                        use_count += left_count * right_count
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


def persistent_caps_from_dualcap(
    dualcap: dict[str, Any],
    p_filter: set[int] | None,
) -> list[dict[str, Any]]:
    """抽取 PersistentCap 描述符；保留 source 区分，以便回指原始账本。"""
    caps = []
    seen: set[tuple[int, float, float, int, str]] = set()
    for prime_item in dualcap["prime_results"]:
        p = int(prime_item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        for cap in prime_item["top_caps"]:
            if cap["classification"] != "PersistentCap":
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
                }
            )
    return caps


def top_counter(counter: Counter[str], limit: int) -> list[dict[str, Any]]:
    """输出 Counter 的 top 项。"""
    return [
        {"key": key, "count": count}
        for key, count in counter.most_common(limit)
    ]


def analyze_cap(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    phase_cache: dict[tuple[int, int], dict[str, Any]],
    top_limit: int,
) -> dict[str, Any]:
    """聚合一个 PersistentCap 的 column-tail 支付账本。"""
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

    prime_cover: Counter[str] = Counter()
    residue_cover: Counter[str] = Counter()
    column_residue_cover: Counter[str] = Counter()
    active_prime: Counter[str] = Counter()
    total_completion_mass = 0
    total_hole_demand = 0
    total_cover_incidence = 0
    max_dp_state_count = 0
    phase_count_by_holes: Counter[int] = Counter()
    zero_hole_phase_count = 0
    mismatches = []

    for phase in phases:
        key = (p, phase)
        if key not in phase_cache:
            phase_cache[key] = phase_payment_signature(
                p=p,
                q=q,
                phase=phase,
                low_primes=low_primes,
                high_primes=high_primes,
            )
        row = phase_cache[key]
        completion_count = int(row["completion_count"])
        if completion_count != m_vector[phase]:
            mismatches.append(
                {
                    "phase": phase,
                    "m_vector": m_vector[phase],
                    "completion_count": completion_count,
                }
            )
        total_completion_mass += completion_count
        total_hole_demand += int(row["hole_demand"])
        total_cover_incidence += int(row["cover_incidence"])
        max_dp_state_count = max(max_dp_state_count, int(row["max_dp_state_count"]))
        phase_count_by_holes[len(row["holes"])] += 1
        if not row["holes"]:
            zero_hole_phase_count += 1
        prime_cover.update({key: int(value) for key, value in row["prime_cover"].items()})
        residue_cover.update({key: int(value) for key, value in row["residue_cover"].items()})
        column_residue_cover.update(
            {key: int(value) for key, value in row["column_residue_cover"].items()}
        )
        active_prime.update({key: int(value) for key, value in row["active_prime"].items()})

    high_prime_count = len(high_primes)
    high_residue_count = sum(high_primes)
    max_prime_cover = max(prime_cover.values(), default=0)
    max_residue_cover = max(residue_cover.values(), default=0)
    max_column_residue_cover = max(column_residue_cover.values(), default=0)
    prime_pigeonhole_floor = (
        total_hole_demand / high_prime_count if high_prime_count else None
    )
    residue_pigeonhole_floor = (
        total_hole_demand / high_residue_count if high_residue_count else None
    )
    column_residue_pigeonhole_floor = residue_pigeonhole_floor
    return {
        **cap,
        "intersection_size_recomputed": len(phases),
        "intersection_size_matches": len(phases) == cap["reported_intersection_size"],
        "intersection_mass_recomputed": total_completion_mass,
        "intersection_mass_matches": total_completion_mass == cap["reported_intersection_mass"],
        "mismatch_count": len(mismatches),
        "mismatches": mismatches[:8],
        "high_primes": high_primes,
        "high_prime_count": high_prime_count,
        "high_residue_count": high_residue_count,
        "zero_hole_phase_count": zero_hole_phase_count,
        "phase_count_by_holes": dict(sorted(phase_count_by_holes.items())),
        "total_hole_demand": total_hole_demand,
        "total_cover_incidence": total_cover_incidence,
        "cover_over_demand": (
            total_cover_incidence / total_hole_demand if total_hole_demand else None
        ),
        "prime_pigeonhole_floor": prime_pigeonhole_floor,
        "residue_pigeonhole_floor": residue_pigeonhole_floor,
        "column_residue_pigeonhole_floor": column_residue_pigeonhole_floor,
        "max_prime_cover": max_prime_cover,
        "max_prime_cover_over_demand": (
            max_prime_cover / total_hole_demand if total_hole_demand else None
        ),
        "max_prime_cover_over_floor": (
            max_prime_cover / prime_pigeonhole_floor
            if prime_pigeonhole_floor
            else None
        ),
        "max_residue_cover": max_residue_cover,
        "max_residue_cover_over_demand": (
            max_residue_cover / total_hole_demand if total_hole_demand else None
        ),
        "max_residue_cover_over_floor": (
            max_residue_cover / residue_pigeonhole_floor
            if residue_pigeonhole_floor
            else None
        ),
        "max_column_residue_cover": max_column_residue_cover,
        "max_column_residue_cover_over_demand": (
            max_column_residue_cover / total_hole_demand if total_hole_demand else None
        ),
        "max_column_residue_cover_over_floor": (
            max_column_residue_cover / column_residue_pigeonhole_floor
            if column_residue_pigeonhole_floor
            else None
        ),
        "top_prime_cover": top_counter(prime_cover, top_limit),
        "top_residue_cover": top_counter(residue_cover, top_limit),
        "top_column_residue_cover": top_counter(column_residue_cover, top_limit),
        "top_active_prime": top_counter(active_prime, top_limit),
        "max_dp_state_count": max_dp_state_count,
        "structural_route": (
            "NoTailDemandFinitePDEC"
            if total_hole_demand == 0
            else "ColumnTailPigeonholeRowOrDistributedCleanKLS"
        ),
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    p_filter: set[int] | None,
    top_limit: int,
) -> dict[str, Any]:
    """运行 PersistentCap column-tail 支付审计。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    caps = persistent_caps_from_dualcap(dualcap, p_filter)
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
                "min_effective_prime_support": min(
                    row["total_hole_demand"] / row["max_prime_cover"]
                    for row in rows
                    if row["max_prime_cover"] > 0
                ),
                "min_effective_residue_support": min(
                    row["total_hole_demand"] / row["max_residue_cover"]
                    for row in rows
                    if row["max_residue_cover"] > 0
                ),
                "min_effective_column_residue_support": min(
                    row["total_hole_demand"] / row["max_column_residue_cover"]
                    for row in rows
                    if row["max_column_residue_cover"] > 0
                ),
                "max_residue_cover_share": max(
                    row["max_residue_cover_over_demand"] or 0.0
                    for row in rows
                ),
                "max_column_residue_cover_share": max(
                    row["max_column_residue_cover_over_demand"] or 0.0
                    for row in rows
                ),
            }
        )
    return {
        "certificate_type": "triad_a1_persistent_columntail_payment_audit",
        "status": "persistent_caps_columntail_payment_materialized",
        "q": int(dualcap["q"]),
        "source_hashes": {
            "persistent_columntail_payment_script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "p_values": sorted({int(row["p"]) for row in cap_reports}),
        "persistent_cap_count": len(cap_reports),
        "unique_phase_signature_count": len(phase_cache),
        "all_intersections_recomputed": all(
            row["intersection_size_matches"] and row["intersection_mass_matches"]
            for row in cap_reports
        ),
        "all_phase_m_counts_match": all(row["mismatch_count"] == 0 for row in cap_reports),
        "route_counts": dict(sorted(route_counts.items())),
        "p_level_effective_support": p_level_effective_support,
        "cap_reports": cap_reports,
        "review_conclusion": (
            "PersistentCap 的质量已经被拆成 column-tail 支付账本。每个低洞完成都必须由"
            "某个高素数 residue 支付；因此持久分支只能二分为固定 tail/column residue 过载"
            "的 PDEC，或支付分散的 CleanKLS/DLS。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审稿摘要。"""
    lines = [
        "# Triad-A1 PersistentCap ColumnTail 支付审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构语义",
        "",
        "对每个 `PersistentCap`，低模骨架留下的洞必须由不在 `Q` 中的高素数 residue 支付。",
        "设 cap 内总完成质量为 `M_C`，低洞需求为：",
        "",
        "```text",
        "D_C = sum_{phase in C} M(phase) * |H_low(phase)|。",
        "```",
        "",
        "每个完成态至少支付这些洞；于是无需猜全局常数，直接得到结构二分：",
        "",
        "```text",
        "某个 tail/column residue 持久过载 => TailAnchor / ColumnCRT displacement PDEC；",
        "所有 residue 都分散支付           => CleanKLS / DLS 型大筛入口。",
        "```",
        "",
        "本文登记的是这套二分的机器可读输入，不声称已完成 `U_CRT<L_PDEC`。",
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
            f"- `persistent_cap_count={result['persistent_cap_count']}`。",
            f"- `unique_phase_signature_count={result['unique_phase_signature_count']}`。",
            f"- `all_intersections_recomputed={result['all_intersections_recomputed']}`。",
            f"- `all_phase_m_counts_match={result['all_phase_m_counts_match']}`。",
            f"- `route_counts={result['route_counts']}`。",
            "",
            "## 4. P 级有效支撑",
            "",
            "`effective support = total_hole_demand / max_single_bucket_payment`。它不是固定阈值，而是本层实际需要的分散桶数下界。",
            "",
            "| P | caps | min eff prime | min eff residue | min eff column residue | max residue share | max colres share |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["p_level_effective_support"]:
        lines.append(
            "| {p} | {caps} | {ep} | {er} | {ec} | {rs} | {cs} |".format(
                p=row["p"],
                caps=row["cap_count"],
                ep=fmt_float(row["min_effective_prime_support"]),
                er=fmt_float(row["min_effective_residue_support"]),
                ec=fmt_float(row["min_effective_column_residue_support"]),
                rs=fmt_float(row["max_residue_cover_share"]),
                cs=fmt_float(row["max_column_residue_cover_share"]),
            )
        )

    lines.extend(
        [
            "",
            "## 5. Cap 明细",
            "",
            "| P | alpha | h | dir | mass | demand | cover/demand | max prime/demand | max residue/demand | max colres/demand | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_reports"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {mass} | {demand} | {cod} | {mpd} | {mrd} | {mcd} | `{route}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                mass=row["intersection_mass_recomputed"],
                demand=row["total_hole_demand"],
                cod=fmt_float(row["cover_over_demand"]),
                mpd=fmt_float(row["max_prime_cover_over_demand"]),
                mrd=fmt_float(row["max_residue_cover_over_demand"]),
                mcd=fmt_float(row["max_column_residue_cover_over_demand"]),
                route=row["structural_route"],
            )
        )

    lines.extend(["", "## 6. Top 支付签名", ""])
    for row in result["cap_reports"]:
        lines.extend(
            [
                f"### P={row['p']} alpha={fmt_float(row['alpha'])} h={row['h']} dir={fmt_float(row['direction'])} source={row['source']}",
                "",
                f"- `phase_count_by_holes={row['phase_count_by_holes']}`。",
                f"- `prime_pigeonhole_floor={fmt_float(row['prime_pigeonhole_floor'])}`。",
                f"- `residue_pigeonhole_floor={fmt_float(row['residue_pigeonhole_floor'])}`。",
                f"- `max_prime_cover_over_floor={fmt_float(row['max_prime_cover_over_floor'])}`。",
                f"- `max_residue_cover_over_floor={fmt_float(row['max_residue_cover_over_floor'])}`。",
                f"- `max_column_residue_cover_over_floor={fmt_float(row['max_column_residue_cover_over_floor'])}`。",
                f"- top prime cover: `{row['top_prime_cover']}`。",
                f"- top residue cover: `{row['top_residue_cover']}`。",
                f"- top column-residue cover: `{row['top_column_residue_cover']}`。",
                "",
            ]
        )

    lines.extend(
        [
            "## 7. 结构读数",
            "",
            "这一步把 `PersistentCap => refined PDEC / column-tail rows` 从口头路由推进为支付方程：",
            "",
            "```text",
            "PersistentCap mass + low-hole demand",
            "=> tail residue / column residue payment ledger",
            "=> fixed overload PDEC or distributed CleanKLS/DLS。",
            "```",
            "",
            "下一硬点不再是寻找某个固定全局常数，而是证明：沿正式反例族，top 支付签名若持久复现则可提交同一 formal unit 的 PDEC；若不复现，则支付必须跨多壳分散，进入大筛型 CleanKLS/DLS。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--p-values", type=str, default="17,19,23,29,31,37")
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
                "persistent_cap_count": result["persistent_cap_count"],
                "unique_phase_signature_count": result["unique_phase_signature_count"],
                "all_intersections_recomputed": result["all_intersections_recomputed"],
                "all_phase_m_counts_match": result["all_phase_m_counts_match"],
                "route_counts": result["route_counts"],
                "p_level_effective_support": result["p_level_effective_support"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
