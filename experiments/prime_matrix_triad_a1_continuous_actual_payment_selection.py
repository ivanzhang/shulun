#!/usr/bin/env python3
"""精确构造 A1 连续方向弧 cap 的 canonical actual payment measure。

用法示例：
  python3 experiments/prime_matrix_triad_a1_continuous_actual_payment_selection.py
  python3 experiments/prime_matrix_triad_a1_continuous_actual_payment_selection.py --p-values 17,19,23

输出：
  docs/monograph/prime-matrix-triad-a1-continuous-actual-payment-selection.json
  docs/monograph/prime-matrix-triad-a1-continuous-actual-payment-selection.md
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
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.md"
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


def residue_options(
    p: int,
    q: int,
    phase: int,
    holes: list[int],
    prime: int,
) -> list[tuple[int, int]]:
    """返回 `(residue, cover_mask)` 选项。"""
    hole_index = {col: index for index, col in enumerate(holes)}
    table = [0] * prime
    for col in holes:
        residue = residue_for_hole(p, q, phase, col, prime)
        table[residue] |= 1 << hole_index[col]
    return list(enumerate(table))


def combine_dp(left: dict[int, int], option_counter: Counter[int]) -> dict[int, int]:
    """按 OR 覆盖合并 DP。"""
    result: dict[int, int] = {}
    for old_mask, old_count in left.items():
        for option_mask, multiplicity in option_counter.items():
            new_mask = old_mask | option_mask
            result[new_mask] = result.get(new_mask, 0) + old_count * multiplicity
    return result


def superset_sums(counter: dict[int, int], bit_count: int) -> list[int]:
    """对 mask 计数表做超集求和。"""
    size = 1 << bit_count
    sums = [0] * size
    for mask, count in counter.items():
        sums[mask] = count
    for bit in range(bit_count):
        step = 1 << bit
        for mask in range(size):
            if (mask & step) == 0:
                sums[mask] += sums[mask | step]
    return sums


def canonical_phase_payments(
    p: int,
    q: int,
    phase: int,
    low_primes: list[int],
    high_primes: list[int],
) -> dict[str, Any]:
    """精确统计单相位 canonical actual payment。

    规则：对每个完成态和每个低洞，选择第一个覆盖该洞的 high prime residue。
    这给出确定的真实支付测度，避免暴露账本的多重计数。
    """
    holes = low_holes_for_phase(p, q, low_primes, phase)
    if not holes:
        high_period = math.prod(high_primes) if high_primes else 1
        return {
            "holes": holes,
            "completion_count": high_period,
            "payment_count": 0,
            "max_dp_state_count": 1,
            "prime_payment": {},
            "residue_payment": {},
            "column_residue_payment": {},
            "payment_signature": {},
        }

    full_mask = (1 << len(holes)) - 1
    options_by_prime = [
        (prime, residue_options(p, q, phase, holes, prime))
        for prime in high_primes
    ]

    suffix: list[dict[int, int]] = [{} for _ in range(len(options_by_prime) + 1)]
    suffix[-1] = {0: 1}
    for idx in range(len(options_by_prime) - 1, -1, -1):
        _prime, options = options_by_prime[idx]
        suffix[idx] = combine_dp(
            suffix[idx + 1],
            Counter(mask for _residue, mask in options),
        )
    suffix_super = [superset_sums(row, len(holes)) for row in suffix]
    completion_count = suffix[0].get(full_mask, 0)

    prime_payment: Counter[str] = Counter()
    residue_payment: Counter[str] = Counter()
    column_residue_payment: Counter[str] = Counter()
    payment_signature: Counter[str] = Counter()

    for hole_index, col in enumerate(holes):
        bit = 1 << hole_index
        prefix_no_cover: dict[int, int] = {0: 1}
        for idx, (prime, options) in enumerate(options_by_prime):
            for residue, option_mask in options:
                if (option_mask & bit) == 0:
                    continue
                for left_mask, left_count in prefix_no_cover.items():
                    joined = left_mask | option_mask
                    need = full_mask ^ joined
                    right_count = suffix_super[idx + 1][need]
                    if right_count == 0:
                        continue
                    count = left_count * right_count
                    prime_payment[str(prime)] += count
                    residue_payment[f"{prime}:{residue}"] += count
                    column_residue_payment[f"{prime}:{col % prime}"] += count
                    payment_signature[f"{prime}:{residue}:{col % prime}"] += count

            prefix_no_cover = combine_dp(
                prefix_no_cover,
                Counter(mask for _residue, mask in options if (mask & bit) == 0),
            )

    return {
        "holes": holes,
        "completion_count": completion_count,
        "payment_count": sum(payment_signature.values()),
        "max_dp_state_count": max(len(row) for row in suffix),
        "prime_payment": dict(prime_payment),
        "residue_payment": dict(residue_payment),
        "column_residue_payment": dict(column_residue_payment),
        "payment_signature": dict(payment_signature),
    }


def top_counter(counter: Counter[str], limit: int) -> list[dict[str, Any]]:
    """输出 Counter 的 top 项。"""
    return [{"key": key, "count": count} for key, count in counter.most_common(limit)]


def ratio(numerator: int, denominator: int) -> float | None:
    """安全比例。"""
    if denominator == 0:
        return None
    return numerator / denominator


def effective_support(value: int, denominator: int) -> float | None:
    """最大桶占比的倒数形式。"""
    if value == 0:
        return None
    return denominator / value


def analyze_continuous_cap(
    prime_row: dict[str, Any],
    mult_item: dict[str, Any],
    top_index: int,
    top_limit: int,
) -> dict[str, Any]:
    """分析一个连续 cap 的 canonical actual payment。"""
    p = int(prime_row["p"])
    q = int(prime_row["q"])
    arc_row = prime_row["top_continuous_arc_rows"][top_index]
    h = int(arc_row["h"])
    zeta_turn = float(arc_row["best_zeta_turn"])
    m_vector = [int(value) for value in mult_item["m_vector"]]
    low_primes = [int(value) for value in mult_item["low_primes"]]
    high_primes = [int(value) for value in mult_item["high_primes"]]
    phases = positive_cap_phases(m_vector, q, h, zeta_turn)

    phase_count_by_holes: Counter[int] = Counter()
    prime_payment: Counter[str] = Counter()
    residue_payment: Counter[str] = Counter()
    column_residue_payment: Counter[str] = Counter()
    payment_signature: Counter[str] = Counter()
    total_completion_mass = 0
    total_hole_demand = 0
    total_payment_count = 0
    max_dp_state_count = 0
    mismatches: list[dict[str, Any]] = []

    for phase in phases:
        row = canonical_phase_payments(p, q, phase, low_primes, high_primes)
        mass = int(row["completion_count"])
        expected_mass = m_vector[phase]
        holes = row["holes"]
        phase_count_by_holes[len(holes)] += 1
        total_completion_mass += mass
        total_hole_demand += mass * len(holes)
        total_payment_count += int(row["payment_count"])
        max_dp_state_count = max(max_dp_state_count, int(row["max_dp_state_count"]))
        if mass != expected_mass or int(row["payment_count"]) != mass * len(holes):
            mismatches.append(
                {
                    "phase": phase,
                    "expected_mass": expected_mass,
                    "completion_count": mass,
                    "hole_count": len(holes),
                    "payment_count": row["payment_count"],
                }
            )
        prime_payment.update({key: int(value) for key, value in row["prime_payment"].items()})
        residue_payment.update(
            {key: int(value) for key, value in row["residue_payment"].items()}
        )
        column_residue_payment.update(
            {key: int(value) for key, value in row["column_residue_payment"].items()}
        )
        payment_signature.update(
            {key: int(value) for key, value in row["payment_signature"].items()}
        )

    max_prime = max(prime_payment.values(), default=0)
    max_residue = max(residue_payment.values(), default=0)
    max_colres = max(column_residue_payment.values(), default=0)
    max_signature = max(payment_signature.values(), default=0)
    reported_phase_count = int(arc_row["cap_phase_count"])
    reported_mass = int(round(float(arc_row["cap_mass"])))
    route = (
        "NoTailDemandSparseOrLocalSurvivor"
        if total_hole_demand == 0
        else "ActualPaymentMeasureDichotomySubmitted"
    )

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
        "recomputed_cap_mass": total_completion_mass,
        "cap_mass_matches": total_completion_mass == reported_mass,
        "cap_mass_share": arc_row["cap_mass_share"],
        "low_primes": low_primes,
        "high_primes": high_primes,
        "phase_count_by_holes": dict(sorted(phase_count_by_holes.items())),
        "total_hole_demand": total_hole_demand,
        "total_payment_count": total_payment_count,
        "payment_count_matches_demand": total_payment_count == total_hole_demand,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches[:8],
        "max_dp_state_count": max_dp_state_count,
        "max_prime_payment": max_prime,
        "max_prime_payment_share": ratio(max_prime, total_hole_demand),
        "max_residue_payment": max_residue,
        "max_residue_payment_share": ratio(max_residue, total_hole_demand),
        "max_column_residue_payment": max_colres,
        "max_column_residue_payment_share": ratio(max_colres, total_hole_demand),
        "max_payment_signature": max_signature,
        "max_payment_signature_share": ratio(max_signature, total_hole_demand),
        "effective_prime_support": effective_support(max_prime, total_hole_demand),
        "effective_residue_support": effective_support(max_residue, total_hole_demand),
        "effective_column_residue_support": effective_support(max_colres, total_hole_demand),
        "effective_payment_signature_support": effective_support(
            max_signature, total_hole_demand
        ),
        "top_prime_payment": top_counter(prime_payment, top_limit),
        "top_residue_payment": top_counter(residue_payment, top_limit),
        "top_column_residue_payment": top_counter(column_residue_payment, top_limit),
        "top_payment_signature": top_counter(payment_signature, top_limit),
        "structural_route": route,
    }


def run(
    continuous_path: Path,
    mult_path: Path,
    p_filter: set[int] | None,
    top_rows_per_p: int,
    top_limit: int,
) -> dict[str, Any]:
    """运行 canonical actual payment 审计。"""
    continuous = load_json(continuous_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    cap_reports = []
    for prime_row in continuous["prime_results"]:
        p = int(prime_row["p"])
        if p_filter is not None and p not in p_filter:
            continue
        for top_index in range(min(top_rows_per_p, len(prime_row["top_continuous_arc_rows"]))):
            cap_reports.append(
                analyze_continuous_cap(
                    prime_row=prime_row,
                    mult_item=mult_by_p[p],
                    top_index=top_index,
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
        "certificate_type": "triad_a1_continuous_actual_payment_selection",
        "status": "continuous_actual_payment_measure_constructed",
        "q": int(continuous["q"]),
        "parameters": {
            "top_rows_per_p": top_rows_per_p,
            "top_limit": top_limit,
            "p_filter": None if p_filter is None else sorted(p_filter),
        },
        "source_hashes": {
            "continuous_actual_payment_selection_script": file_sha256(Path(__file__).resolve()),
            "continuous_direction_arc_json": file_sha256(continuous_path),
            "multiplicity_cap_json": file_sha256(mult_path),
        },
        "cap_report_count": len(cap_reports),
        "all_cap_recomputations_match": all(
            row["cap_phase_count_matches"] and row["cap_mass_matches"]
            for row in cap_reports
        ),
        "all_payment_counts_match_demand": all(
            row["payment_count_matches_demand"] and row["mismatch_count"] == 0
            for row in cap_reports
        ),
        "route_counts": dict(sorted(route_counts.items())),
        "p_level_rows": p_level_rows,
        "cap_reports": cap_reports,
        "selection_law": (
            "对每个完成态和每个低洞，按 high prime 的固定顺序选择第一个覆盖该洞的 residue。"
            "这把暴露候选桶提升为真实支付测度；总质量恒等式为 "
            "payment_count=sum_phase M(phase)*|H_low(phase)|。"
        ),
        "recursive_dichotomy": (
            "若 canonical payment measure 的某个有限签名在无限反例子族中具有正 limsup 质量，"
            "该签名进入 column/tail PDEC；若所有固定签名的质量递归趋零，"
            "则支付测度扩散，进入 CleanKLS/DLS admission。"
        ),
        "review_conclusion": (
            "连续方向弧 cap 的 actual payment measure 已精确构造；暴露账本不再只是候选集合。"
            "剩余硬点被压成两个终端引理：limsup 正签名 => PDEC；全部签名递归消散 => CleanKLS/DLS。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 连续弧 ActualPaymentSelection 审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 选择律",
        "",
        result["selection_law"],
        "",
        "```text",
        "completion y=(y_ell)_ell；",
        "hole c in H_low(t)；",
        "pay(c,y)=first ell such that ell covers c under y_ell；",
        "mu_C(bucket)=# canonical payments in bucket。",
        "```",
        "",
        "## 2. 递归二分",
        "",
        result["recursive_dichotomy"],
        "",
        "这一步不依赖固定全局常数；它依赖无限子族上的 `limsup > 0` 或所有固定签名趋零。",
        "",
        "## 3. 汇总",
        "",
        f"- `cap_report_count={result['cap_report_count']}`。",
        f"- `all_cap_recomputations_match={result['all_cap_recomputations_match']}`。",
        f"- `all_payment_counts_match_demand={result['all_payment_counts_match_demand']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `parameters={result['parameters']}`。",
        "",
        "## 4. P 级 actual payment 读数",
        "",
        "| P | caps | positive demand caps | max actual sig share | min effective sig support | routes |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["p_level_rows"]:
        lines.append(
            "| {p} | {caps} | {positive} | {share} | {support} | `{routes}` |".format(
                p=row["p"],
                caps=row["cap_count"],
                positive=row["positive_demand_cap_count"],
                share=fmt_float(row["max_payment_signature_share"]),
                support=fmt_float(row["min_effective_payment_signature_support"]),
                routes=row["routes"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. Cap 明细",
            "",
            "| P | h | phases | mass share | demand | payment count | max sig share | eff sig support | route |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["cap_reports"]:
        lines.append(
            "| {p} | {h} | {phases} | {mass} | {demand} | {payments} | {share} | {support} | `{route}` |".format(
                p=row["p"],
                h=row["h"],
                phases=row["recomputed_cap_phase_count"],
                mass=fmt_float(row["cap_mass_share"]),
                demand=row["total_hole_demand"],
                payments=row["total_payment_count"],
                share=fmt_float(row["max_payment_signature_share"]),
                support=fmt_float(row["effective_payment_signature_support"]),
                route=row["structural_route"],
            )
        )

    lines.extend(["", "## 6. Top actual payment 签名", ""])
    for row in result["cap_reports"]:
        lines.extend(
            [
                f"### P={row['p']} top={row['top_index']} h={row['h']} zeta={fmt_float(row['zeta_turn'])}",
                "",
                f"- `phase_count_by_holes={row['phase_count_by_holes']}`。",
                f"- `max_dp_state_count={row['max_dp_state_count']}`。",
                f"- top payment signatures: `{row['top_payment_signature']}`。",
                f"- top residues: `{row['top_residue_payment']}`。",
                f"- top column residues: `{row['top_column_residue_payment']}`。",
                "",
            ]
        )

    lines.extend(
        [
            "## 7. 当前硬点",
            "",
            "ActualPaymentSelection 的构造部分已经完成。剩余不是数据问题，而是终端结构引理：",
            "",
            "```text",
            "A. positive-limsup finite signature -> legal column/tail PDEC row；",
            "B. all finite signatures vanish -> CleanKLS/DLS admission + large-sieve close。",
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
    parser.add_argument("--p-values", type=str, default=None)
    parser.add_argument("--top-rows-per-p", type=int, default=1)
    parser.add_argument("--top-limit", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        continuous_path=args.continuous_json,
        mult_path=args.multiplicity_json,
        p_filter=parse_p_values(args.p_values),
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
                "all_payment_counts_match_demand": result[
                    "all_payment_counts_match_demand"
                ],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
