#!/usr/bin/env python3
"""生成 Triad-A1 ForcedCap 多桶 PDEC 的向量 LP 骨架。

用法示例：
  python3 experiments/prime_matrix_triad_a1_multibucket_pdec_skeleton.py

输出：
  docs/monograph/prime-matrix-triad-a1-multibucket-pdec-skeleton.json
  docs/monograph/prime-matrix-triad-a1-multibucket-pdec-skeleton.md
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
from prime_matrix_triad_a1_forcedcap_columntail_payment_audit import (
    file_sha256,
    forced_caps_from_dualcap,
    load_json,
    parse_p_values,
    residue_for_hole,
)
from prime_matrix_triad_a1_pdec_dualcap_extractor import cap_phases


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_EXPOSURE = DOCS / "prime-matrix-triad-a1-forcedcap-columntail-payment.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-multibucket-pdec-skeleton.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-multibucket-pdec-skeleton.md"
BUCKET_KINDS = ("residue", "column_residue")


def cap_key(row: dict[str, Any]) -> tuple[int, float, float, int, str]:
    """生成 cap 的稳定键。"""
    return (
        int(row["p"]),
        float(row["alpha"]),
        float(row["direction"]),
        int(row["h"]),
        str(row["source"]),
    )


def stable_counter_hash(counter: Counter[Any]) -> str:
    """对稀疏矩阵/向量计数生成稳定哈希。"""
    digest = hashlib.sha256()
    for key, value in sorted(counter.items(), key=lambda item: str(item[0])):
        digest.update(f"{key}\t{value}\n".encode("utf-8"))
    return digest.hexdigest()


def bucket_key(kind: str, p: int, q: int, phase: int, col: int, prime: int) -> str:
    """计算一个低洞原子在指定桶模型下的 bucket 标签。"""
    if kind == "residue":
        residue = residue_for_hole(p, q, phase, col, prime)
        return f"{prime}:{residue}"
    if kind == "column_residue":
        return f"{prime}:{col % prime}"
    raise ValueError(f"unsupported bucket kind: {kind}")


def ceil_ratio(numerator: int, denominator: int) -> int | None:
    """计算 ceil(numerator/denominator)。"""
    if denominator <= 0:
        return None
    return math.ceil(numerator / denominator)


def exposure_reference_for_kind(
    exposure_row: dict[str, Any] | None,
    kind: str,
) -> dict[str, int] | None:
    """取旧暴露账本中同口径字段，用于交叉校验。"""
    if exposure_row is None:
        return None
    if kind == "residue":
        max_key = "max_residue_exposure"
    elif kind == "column_residue":
        max_key = "max_column_residue_exposure"
    else:
        return None
    return {
        "total_hole_demand": int(exposure_row["total_hole_demand"]),
        "total_exposure_incidence": int(exposure_row["total_exposure_incidence"]),
        "max_bucket_exposure": int(exposure_row[max_key]),
    }


def analyze_bucket_matrix(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    exposure_row: dict[str, Any] | None,
    bucket_kind: str,
    top_limit: int,
) -> dict[str, Any]:
    """重算一个 cap 的 g_b(t) 向量 LP 骨架。"""
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

    phase_demand: Counter[int] = Counter()
    phase_exposure: Counter[int] = Counter()
    bucket_totals: Counter[str] = Counter()
    bucket_phase: Counter[tuple[str, int]] = Counter()
    total_demand = 0
    total_exposure = 0

    # 变量 g_b(t) 的稀疏上界 E_b(t)；不枚举实际支付选择。
    for phase in phases:
        mass = int(m_vector[phase])
        holes = low_holes_for_phase(p, q, low_primes, phase)
        demand = mass * len(holes)
        phase_demand[phase] += demand
        total_demand += demand
        for col in holes:
            for prime in high_primes:
                key = bucket_key(bucket_kind, p, q, phase, col, prime)
                bucket_totals[key] += mass
                bucket_phase[(key, phase)] += mass
                phase_exposure[phase] += mass
                total_exposure += mass

    max_bucket = max(bucket_totals.values(), default=0)
    min_actual_buckets = ceil_ratio(total_demand, max_bucket)
    exposure_reference = exposure_reference_for_kind(exposure_row, bucket_kind)
    reference_matches = (
        exposure_reference is None
        or (
            exposure_reference["total_hole_demand"] == total_demand
            and exposure_reference["total_exposure_incidence"] == total_exposure
            and exposure_reference["max_bucket_exposure"] == max_bucket
        )
    )
    phase_exposure_identity = all(
        phase_exposure[phase] == demand * len(high_primes)
        for phase, demand in phase_demand.items()
    )
    exposure_weights = [
        value / total_demand for value in bucket_totals.values()
        if total_demand > 0
    ]
    exposure_herfindahl = sum(value * value for value in exposure_weights)
    effective_support = (
        1.0 / exposure_herfindahl if exposure_herfindahl > 0 else None
    )
    route = (
        "MultiBucketVectorLPReady"
        if min_actual_buckets is not None and min_actual_buckets >= 2
        else "SingleBucketReturn"
    )
    return {
        "p": p,
        "q": q,
        "alpha": cap["alpha"],
        "direction": cap["direction"],
        "h": int(cap["h"]),
        "source": cap["source"],
        "bucket_kind": bucket_kind,
        "active_phase_count": len(phase_demand),
        "bucket_count": len(bucket_totals),
        "variable_count": len(bucket_phase),
        "total_demand": total_demand,
        "total_exposure_incidence": total_exposure,
        "high_prime_count": len(high_primes),
        "max_bucket_exposure": max_bucket,
        "max_bucket_exposure_share": (
            max_bucket / total_demand if total_demand else None
        ),
        "min_actual_buckets_by_exposure": min_actual_buckets,
        "single_bucket_payment_excluded": (
            min_actual_buckets is not None and min_actual_buckets >= 2
        ),
        "phase_exposure_identity": phase_exposure_identity,
        "existing_exposure_reference_matches": reference_matches,
        "exposure_herfindahl_by_demand": exposure_herfindahl,
        "effective_bucket_support_by_exposure": effective_support,
        "matrix_hash": stable_counter_hash(bucket_phase),
        "phase_demand_hash": stable_counter_hash(phase_demand),
        "bucket_total_hash": stable_counter_hash(bucket_totals),
        "lp_row_counts": {
            "nonnegativity_rows": len(bucket_phase),
            "bucket_exposure_upper_rows": len(bucket_phase),
            "phase_mass_upper_rows": len(phase_demand),
            "total_payment_rows": 1 if total_demand > 0 else 0,
        },
        "top_bucket_totals": [
            {"bucket": key, "count": count}
            for key, count in bucket_totals.most_common(top_limit)
        ],
        "failure_routes": [
            "SingleBucketReturn",
            "CorrelatedBucketBlock",
            "ColumnTailMissingRow",
            "DiffuseExtremizer",
        ],
        "route": route,
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    exposure_path: Path,
    p_filter: set[int] | None,
    top_limit: int,
) -> dict[str, Any]:
    """运行多桶 PDEC 骨架生成。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    exposure = load_json(exposure_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    exposure_by_cap = {cap_key(row): row for row in exposure["cap_reports"]}
    caps = forced_caps_from_dualcap(dualcap, p_filter)

    rows = []
    for cap in caps:
        exposure_row = exposure_by_cap.get(cap_key(cap))
        for bucket_kind in BUCKET_KINDS:
            rows.append(
                analyze_bucket_matrix(
                    cap=cap,
                    mult_item=mult_by_p[int(cap["p"])],
                    exposure_row=exposure_row,
                    bucket_kind=bucket_kind,
                    top_limit=top_limit,
                )
            )

    kind_summary = []
    for kind in BUCKET_KINDS:
        subset = [row for row in rows if row["bucket_kind"] == kind]
        kind_summary.append(
            {
                "bucket_kind": kind,
                "row_count": len(subset),
                "global_min_actual_buckets_by_exposure": min(
                    row["min_actual_buckets_by_exposure"]
                    for row in subset
                    if row["min_actual_buckets_by_exposure"] is not None
                ),
                "global_max_bucket_exposure_share": max(
                    row["max_bucket_exposure_share"] or 0.0 for row in subset
                ),
                "global_min_effective_bucket_support": min(
                    row["effective_bucket_support_by_exposure"]
                    for row in subset
                    if row["effective_bucket_support_by_exposure"] is not None
                ),
                "global_max_variable_count": max(
                    row["variable_count"] for row in subset
                ),
            }
        )

    return {
        "certificate_type": "triad_a1_multibucket_pdec_skeleton",
        "status": "forcedcap_multibucket_vector_lp_skeleton_materialized",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_json": file_sha256(mult_path),
            "forcedcap_exposure_json": file_sha256(exposure_path),
        },
        "forced_cap_count": len(caps),
        "bucket_kinds": list(BUCKET_KINDS),
        "matrix_row_count": len(rows),
        "all_existing_exposure_references_match": all(
            row["existing_exposure_reference_matches"] for row in rows
        ),
        "all_phase_exposure_identities_hold": all(
            row["phase_exposure_identity"] for row in rows
        ),
        "all_single_bucket_payments_excluded": all(
            row["single_bucket_payment_excluded"] for row in rows
        ),
        "kind_summary": kind_summary,
        "rows": rows,
        "structural_law": (
            "Multi-bucket PDEC must use variables g_b(t) with bounds "
            "0<=g_b(t)<=E_b(t), sum_b g_b(t)<=M(t), and one total payment row. "
            "A failure of U_CRT^multi<L_PDEC^multi must route to SingleBucketReturn, "
            "CorrelatedBucketBlock, ColumnTailMissingRow, or DiffuseExtremizer."
        ),
        "review_conclusion": (
            "ForcedCap 的 residue 与 column-residue 多桶向量 LP 骨架已物化；"
            "当前每个骨架都复核了旧暴露账本、相位暴露恒等式与单桶排除。"
            "下一步可以直接生成 U_CRT^multi/L_PDEC^multi 对偶证书或输出可路由失败。"
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
        "# Triad-A1 多桶 PDEC 骨架审计",
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
        "g_b(t) >= 0；",
        "g_b(t) <= E_b(t)；",
        "sum_b g_b(t) <= M(t)；",
        "sum_t sum_b g_b(t) = |Gamma_S|。",
        "```",
        "",
        "这里不使用固定常数；每个 cap 的桶数下界由自己的 `D/max_b E_b` 给出。",
        "",
        "## 2. 汇总",
        "",
        f"- `forced_cap_count={result['forced_cap_count']}`。",
        f"- `matrix_row_count={result['matrix_row_count']}`。",
        f"- `bucket_kinds={result['bucket_kinds']}`。",
        f"- `all_existing_exposure_references_match={result['all_existing_exposure_references_match']}`。",
        f"- `all_phase_exposure_identities_hold={result['all_phase_exposure_identities_hold']}`。",
        f"- `all_single_bucket_payments_excluded={result['all_single_bucket_payments_excluded']}`。",
        "",
        "## 3. Bucket 类型汇总",
        "",
        "| bucket kind | rows | min buckets | max exposure share | min effective support | max variables |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["kind_summary"]:
        lines.append(
            "| {kind} | {rows} | {lb} | {share} | {eff} | {vars} |".format(
                kind=row["bucket_kind"],
                rows=row["row_count"],
                lb=row["global_min_actual_buckets_by_exposure"],
                share=fmt_float(row["global_max_bucket_exposure_share"]),
                eff=fmt_float(row["global_min_effective_bucket_support"]),
                vars=row["global_max_variable_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap/桶骨架明细",
            "",
            "| P | kind | alpha | h | dir | phases | buckets | vars | D | min buckets | max share | eff support | route |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {p} | {kind} | {alpha} | {h} | {direction} | {phases} | {buckets} | {vars} | {demand} | {lb} | {share} | {eff} | `{route}` |".format(
                p=row["p"],
                kind=row["bucket_kind"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                phases=row["active_phase_count"],
                buckets=row["bucket_count"],
                vars=row["variable_count"],
                demand=row["total_demand"],
                lb=row["min_actual_buckets_by_exposure"],
                share=fmt_float(row["max_bucket_exposure_share"]),
                eff=fmt_float(row["effective_bucket_support_by_exposure"]),
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 失败路由",
            "",
            "后续若 `U_CRT^multi<L_PDEC^multi` 失败，失败对象必须输出：",
            "",
            "```text",
            "SingleBucketReturn      => 与已排除的单桶支付冲突，或回到单桶 PDEC；",
            "CorrelatedBucketBlock   => 细化为更小 multi-bucket formal unit；",
            "ColumnTailMissingRow    => 补 TailAnchor / ColumnCRT / cofactor 条件行；",
            "DiffuseExtremizer       => CleanKLS/DLS。",
            "```",
            "",
            "因此多桶 PDEC 不再是模糊出口，而是一个可继续递归剥离的向量 LP/对偶入口。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--exposure-json", type=Path, default=DEFAULT_EXPOSURE)
    parser.add_argument("--p-values", type=str, default="43,47")
    parser.add_argument("--top-limit", type=int, default=8)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        dualcap_path=args.dualcap_json,
        mult_path=args.multiplicity_json,
        exposure_path=args.exposure_json,
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
                "matrix_row_count": result["matrix_row_count"],
                "all_existing_exposure_references_match": result[
                    "all_existing_exposure_references_match"
                ],
                "all_single_bucket_payments_excluded": result[
                    "all_single_bucket_payments_excluded"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
