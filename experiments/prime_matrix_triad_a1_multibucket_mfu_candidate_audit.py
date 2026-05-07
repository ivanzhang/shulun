#!/usr/bin/env python3
"""提取 Triad-A1 ForcedCap 多桶 formal unit 候选行。

用法示例：
  python3 experiments/prime_matrix_triad_a1_multibucket_mfu_candidate_audit.py

输出：
  docs/monograph/prime-matrix-triad-a1-multibucket-mfu-candidate-audit.json
  docs/monograph/prime-matrix-triad-a1-multibucket-mfu-candidate-audit.md
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
)
from prime_matrix_triad_a1_multibucket_pdec_skeleton import (
    BUCKET_KINDS,
    bucket_key,
)
from prime_matrix_triad_a1_pdec_dualcap_extractor import cap_phases


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-multibucket-mfu-candidate-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-multibucket-mfu-candidate-audit.md"


def stable_counter_hash(counter: Counter[Any]) -> str:
    """对计数器生成稳定哈希。"""
    digest = hashlib.sha256()
    for key, value in sorted(counter.items(), key=lambda item: str(item[0])):
        digest.update(f"{key}\t{value}\n".encode("utf-8"))
    return digest.hexdigest()


def build_exposure_matrix(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    bucket_kind: str,
) -> tuple[Counter[int], Counter[str], Counter[tuple[int, str]], int]:
    """重建 phase-bucket 暴露矩阵。"""
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

    phase_totals: Counter[int] = Counter()
    bucket_totals: Counter[str] = Counter()
    pair_totals: Counter[tuple[int, str]] = Counter()
    total = 0

    # 暴露矩阵 E_b(t)：每个低洞对每个高素数给出唯一可支付 bucket。
    for phase in phases:
        mass = int(m_vector[phase])
        for col in low_holes_for_phase(p, q, low_primes, phase):
            for prime in high_primes:
                key = bucket_key(bucket_kind, p, q, phase, col, prime)
                phase_totals[phase] += mass
                bucket_totals[key] += mass
                pair_totals[(phase, key)] += mass
                total += mass

    return phase_totals, bucket_totals, pair_totals, total


def mutual_information(
    phase_totals: Counter[int],
    bucket_totals: Counter[str],
    pair_totals: Counter[tuple[int, str]],
    total: int,
) -> float:
    """计算暴露矩阵的 I(phase;bucket)。"""
    if total <= 0:
        return 0.0
    info = 0.0
    for (phase, bucket), count in pair_totals.items():
        numerator = count * total
        denominator = phase_totals[phase] * bucket_totals[bucket]
        if numerator > 0 and denominator > 0:
            info += (count / total) * math.log(numerator / denominator)
    return info


def top_lift_rows(
    phase_totals: Counter[int],
    bucket_totals: Counter[str],
    pair_totals: Counter[tuple[int, str]],
    total: int,
    top_limit: int,
) -> list[dict[str, Any]]:
    """输出最高 phase-bucket lift 候选。"""
    rows = []
    if total <= 0:
        return rows
    for (phase, bucket), count in pair_totals.items():
        denominator = phase_totals[phase] * bucket_totals[bucket]
        if denominator <= 0:
            continue
        lift = count * total / denominator
        rows.append(
            {
                "phase": phase,
                "bucket": bucket,
                "count": count,
                "mass_share": count / total,
                "lift": lift,
            }
        )
    rows.sort(key=lambda row: (row["lift"], row["mass_share"]), reverse=True)
    return rows[:top_limit]


def analyze_cap_kind(
    cap: dict[str, Any],
    mult_item: dict[str, Any],
    bucket_kind: str,
    top_limit: int,
) -> dict[str, Any]:
    """分析一个 cap 的 MFU 候选行。"""
    phase_totals, bucket_totals, pair_totals, total = build_exposure_matrix(
        cap,
        mult_item,
        bucket_kind,
    )
    info = mutual_information(phase_totals, bucket_totals, pair_totals, total)
    normalized_info = (
        info / math.log(len(bucket_totals)) if len(bucket_totals) > 1 else 0.0
    )
    has_correlation = info > 1e-15
    route = (
        "FiniteLayerMFUCandidateNeedsActualPaymentStitching"
        if has_correlation
        else "DistributedCleanKLSCandidate"
    )
    top_rows = top_lift_rows(
        phase_totals,
        bucket_totals,
        pair_totals,
        total,
        top_limit,
    )
    return {
        "p": int(cap["p"]),
        "q": int(cap["q"]),
        "alpha": cap["alpha"],
        "direction": cap["direction"],
        "h": int(cap["h"]),
        "source": cap["source"],
        "bucket_kind": bucket_kind,
        "phase_count": len(phase_totals),
        "bucket_count": len(bucket_totals),
        "pair_count": len(pair_totals),
        "total_exposure_incidence": total,
        "phase_bucket_mutual_info": info,
        "phase_bucket_mutual_info_normalized_by_log_bucket": normalized_info,
        "has_finite_layer_correlation": has_correlation,
        "matrix_hash": stable_counter_hash(pair_totals),
        "top_lift_rows": top_rows,
        "route": route,
    }


def run(
    dualcap_path: Path,
    mult_path: Path,
    p_filter: set[int] | None,
    top_limit: int,
) -> dict[str, Any]:
    """运行 MFU 候选审计。"""
    dualcap = load_json(dualcap_path)
    mult = load_json(mult_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    caps = forced_caps_from_dualcap(dualcap, p_filter)
    rows = []
    for cap in caps:
        for bucket_kind in BUCKET_KINDS:
            rows.append(
                analyze_cap_kind(
                    cap,
                    mult_by_p[int(cap["p"])],
                    bucket_kind,
                    top_limit,
                )
            )

    route_counts = Counter(row["route"] for row in rows)
    kind_summary = []
    for kind in BUCKET_KINDS:
        subset = [row for row in rows if row["bucket_kind"] == kind]
        kind_summary.append(
            {
                "bucket_kind": kind,
                "row_count": len(subset),
                "min_mutual_info": min(row["phase_bucket_mutual_info"] for row in subset),
                "max_mutual_info": max(row["phase_bucket_mutual_info"] for row in subset),
                "min_normalized_mutual_info": min(
                    row["phase_bucket_mutual_info_normalized_by_log_bucket"]
                    for row in subset
                ),
                "max_normalized_mutual_info": max(
                    row["phase_bucket_mutual_info_normalized_by_log_bucket"]
                    for row in subset
                ),
                "max_pair_count": max(row["pair_count"] for row in subset),
            }
        )

    return {
        "certificate_type": "triad_a1_multibucket_mfu_candidate_audit",
        "status": "finite_layer_mfu_candidate_rows_materialized",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "dualcap_json": file_sha256(dualcap_path),
            "multiplicity_json": file_sha256(mult_path),
        },
        "forced_cap_count": len(caps),
        "matrix_row_count": len(rows),
        "route_counts": dict(sorted(route_counts.items())),
        "all_rows_have_finite_layer_correlation": all(
            row["has_finite_layer_correlation"] for row in rows
        ),
        "kind_summary": kind_summary,
        "rows": rows,
        "structural_law": (
            "Finite-layer phase-bucket correlation is a candidate compatibility row, "
            "not a proof of actual payment. If actual payment follows a correlated row persistently, "
            "it becomes a multi-bucket formal unit and must enter PDEC. If actual payment avoids every "
            "persistent finite signature, it is DistributedPayment and enters CleanKLS/DLS."
        ),
        "review_conclusion": (
            "当前 forced 多桶暴露矩阵均存在有限层 phase-bucket 相关候选行；"
            "这给出了 MFU-1 的候选输入，但还未证明实际支付图 Gamma 持久落在这些行上。"
            "下一步是 ActualPaymentStitching：持久则 PDEC，不持久则 CleanKLS/DLS。"
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
        "# Triad-A1 多桶 MFU 候选审计",
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
        "I(phase;bucket)>0",
        "  => finite-layer correlated bucket row；",
        "actual payment 持久跟随该 row",
        "  => multi-bucket formal unit / PDEC；",
        "actual payment 不持久跟随任何 finite row",
        "  => DistributedPayment / CleanKLS-DLS。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `forced_cap_count={result['forced_cap_count']}`。",
        f"- `matrix_row_count={result['matrix_row_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_rows_have_finite_layer_correlation={result['all_rows_have_finite_layer_correlation']}`。",
        "",
        "## 3. Bucket 类型汇总",
        "",
        "| bucket kind | rows | min MI | max MI | min normalized MI | max normalized MI | max pairs |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["kind_summary"]:
        lines.append(
            "| {kind} | {rows} | {min_mi} | {max_mi} | {min_nmi} | {max_nmi} | {pairs} |".format(
                kind=row["bucket_kind"],
                rows=row["row_count"],
                min_mi=fmt_float(row["min_mutual_info"]),
                max_mi=fmt_float(row["max_mutual_info"]),
                min_nmi=fmt_float(row["min_normalized_mutual_info"]),
                max_nmi=fmt_float(row["max_normalized_mutual_info"]),
                pairs=row["max_pair_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. Cap 明细",
            "",
            "| P | kind | alpha | h | dir | phases | buckets | pairs | MI | normalized MI | route |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {p} | {kind} | {alpha} | {h} | {direction} | {phases} | {buckets} | {pairs} | {mi} | {nmi} | `{route}` |".format(
                p=row["p"],
                kind=row["bucket_kind"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                phases=row["phase_count"],
                buckets=row["bucket_count"],
                pairs=row["pair_count"],
                mi=fmt_float(row["phase_bucket_mutual_info"]),
                nmi=fmt_float(row["phase_bucket_mutual_info_normalized_by_log_bucket"]),
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "这些候选行仍是 exposure 层对象。它们说明可支付图存在有限层相关结构，但不说明实际支付一定使用它。",
            "正式闭合必须补 `ActualPaymentStitching`：",
            "",
            "```text",
            "若 Gamma 持久落入某个候选相关行 => MFU/PDEC；",
            "若 Gamma 对所有候选行都不持久 => CleanKLS/DLS。",
            "```",
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
                "matrix_row_count": result["matrix_row_count"],
                "all_rows_have_finite_layer_correlation": result[
                    "all_rows_have_finite_layer_correlation"
                ],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
