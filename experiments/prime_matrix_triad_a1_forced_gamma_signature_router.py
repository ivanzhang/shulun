#!/usr/bin/env python3
"""把 ForcedCap 的 Gamma 小自由度接到有限签名/分散二分。

用法示例：
  python3 experiments/prime_matrix_triad_a1_forced_gamma_signature_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-forced-gamma-signature-router.json
  docs/monograph/prime-matrix-triad-a1-forced-gamma-signature-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_MFU = DOCS / "prime-matrix-triad-a1-multibucket-mfu-candidate-audit.json"
DEFAULT_FIBER = DOCS / "prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.json"
DEFAULT_FIBER_DOMINANCE = DOCS / "prime-matrix-triad-a1-forcedcap-fiber-dominance-router.json"
DEFAULT_GAMMA_FREEDOM = DOCS / "prime-matrix-triad-a1-forcedcap-gamma-freedom-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-forced-gamma-signature-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-forced-gamma-signature-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm_float(value: Any) -> str:
    """稳定化浮点键。"""
    return f"{float(value):.17g}"


def cap_key(row: dict[str, Any]) -> tuple[int, int, str, str, int, str]:
    """生成跨账本 cap 键。"""
    return (
        int(row["p"]),
        int(row["q"]),
        norm_float(row["alpha"]),
        norm_float(row["direction"]),
        int(row["h"]),
        str(row["source"]),
    )


def ceil_ratio(numerator: float, denominator: float) -> int | None:
    """计算浮点比例上取整。"""
    if denominator <= 0:
        return None
    return math.ceil(numerator / denominator)


def bucket_metrics(
    bucket_kind: str,
    fiber_row: dict[str, Any],
    dominance_row: dict[str, Any],
) -> dict[str, Any]:
    """提取当前 bucket 类型的 fiber 支配指标。"""
    if bucket_kind == "residue":
        return {
            "max_bucket_fiber_cover_share": float(
                fiber_row["max_residue_cover_over_demand"]
            ),
            "min_actual_buckets_by_fiber": int(
                dominance_row["min_actual_residue_buckets_by_fiber"]
            ),
            "top_fiber_buckets": fiber_row["top_residue_cover"],
        }
    if bucket_kind == "column_residue":
        return {
            "max_bucket_fiber_cover_share": float(
                fiber_row["max_column_residue_cover_over_demand"]
            ),
            "min_actual_buckets_by_fiber": int(
                dominance_row["min_actual_column_residue_buckets_by_fiber"]
            ),
            "top_fiber_buckets": fiber_row["top_column_residue_cover"],
        }
    raise ValueError(f"未知 bucket_kind: {bucket_kind}")


def analyze_row(
    mfu_row: dict[str, Any],
    fiber_row: dict[str, Any],
    dominance_row: dict[str, Any],
    gamma_row: dict[str, Any],
) -> dict[str, Any]:
    """拼接一个 MFU 候选行与 Gamma 小自由度账本。"""
    bucket_kind = str(mfu_row["bucket_kind"])
    metrics = bucket_metrics(bucket_kind, fiber_row, dominance_row)
    ambiguous = float(gamma_row["ambiguous_gamma_share_upper_bound"])
    forced = float(gamma_row["forced_gamma_share_lower_bound"])
    signal = float(mfu_row["phase_bucket_mutual_info_normalized_by_log_bucket"])
    signal_margin = signal - ambiguous
    signal_to_ambiguity = signal / ambiguous if ambiguous > 0 else math.inf
    max_bucket_share = float(metrics["max_bucket_fiber_cover_share"])
    ambiguous_bucket_lb = ceil_ratio(ambiguous, max_bucket_share)
    forced_majority_gap = forced - max_bucket_share
    route = (
        "ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission"
        if (
            forced >= 0.9
            and ambiguous <= 0.06
            and signal_margin > 0
            and int(metrics["min_actual_buckets_by_fiber"]) >= 2
        )
        else "NeedsActualGammaSignatureRefinement"
    )
    return {
        "p": int(mfu_row["p"]),
        "q": int(mfu_row["q"]),
        "alpha": mfu_row["alpha"],
        "direction": mfu_row["direction"],
        "h": int(mfu_row["h"]),
        "source": mfu_row["source"],
        "bucket_kind": bucket_kind,
        "phase_count": int(mfu_row["phase_count"]),
        "bucket_count": int(mfu_row["bucket_count"]),
        "pair_count": int(mfu_row["pair_count"]),
        "phase_bucket_mutual_info": float(mfu_row["phase_bucket_mutual_info"]),
        "normalized_signature_signal": signal,
        "ambiguous_gamma_share_upper_bound": ambiguous,
        "forced_gamma_share_lower_bound": forced,
        "signature_signal_minus_ambiguous_budget": signal_margin,
        "signature_signal_to_ambiguity_ratio": signal_to_ambiguity,
        "max_bucket_fiber_cover_share": max_bucket_share,
        "forced_majority_minus_max_bucket_share": forced_majority_gap,
        "min_actual_buckets_by_fiber": int(metrics["min_actual_buckets_by_fiber"]),
        "ambiguous_escape_bucket_lower_bound": ambiguous_bucket_lb,
        "top_lift_rows": mfu_row["top_lift_rows"],
        "top_fiber_buckets": metrics["top_fiber_buckets"],
        "route": route,
    }


def run(
    mfu_path: Path,
    fiber_path: Path,
    fiber_dominance_path: Path,
    gamma_freedom_path: Path,
) -> dict[str, Any]:
    """运行 forced Gamma 签名路由。"""
    mfu = load_json(mfu_path)
    fiber = load_json(fiber_path)
    dominance = load_json(fiber_dominance_path)
    gamma = load_json(gamma_freedom_path)

    fiber_by_key = {cap_key(row): row for row in fiber["cap_reports"]}
    dominance_by_key = {cap_key(row): row for row in dominance["cap_rows"]}
    gamma_by_key = {cap_key(row): row for row in gamma["rows"]}

    rows: list[dict[str, Any]] = []
    missing_keys: list[str] = []
    for mfu_row in mfu["rows"]:
        key = cap_key(mfu_row)
        if key not in fiber_by_key or key not in dominance_by_key or key not in gamma_by_key:
            missing_keys.append(repr(key))
            continue
        rows.append(
            analyze_row(
                mfu_row=mfu_row,
                fiber_row=fiber_by_key[key],
                dominance_row=dominance_by_key[key],
                gamma_row=gamma_by_key[key],
            )
        )

    route_counts = Counter(row["route"] for row in rows)
    all_rows_routed = bool(rows) and not missing_keys and all(
        row["route"] == "ForcedMajorityFiniteSignatureOrSmallAmbiguousCleanKLSAdmission"
        for row in rows
    )
    return {
        "certificate_type": "triad_a1_forced_gamma_signature_router",
        "status": "forced_gamma_signature_pressure_materialized",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "mfu_candidate_json": file_sha256(mfu_path),
            "fiber_consistent_payment_json": file_sha256(fiber_path),
            "fiber_dominance_json": file_sha256(fiber_dominance_path),
            "gamma_freedom_json": file_sha256(gamma_freedom_path),
        },
        "forced_cap_count": int(gamma["forced_cap_count"]),
        "signature_matrix_row_count": len(rows),
        "missing_key_count": len(missing_keys),
        "missing_keys": missing_keys[:20],
        "route_counts": dict(sorted(route_counts.items())),
        "all_rows_routed_to_forced_signature_or_small_ambiguous_clean": all_rows_routed,
        "global_max_ambiguous_gamma_share_upper_bound": max(
            row["ambiguous_gamma_share_upper_bound"] for row in rows
        ),
        "global_min_forced_gamma_share_lower_bound": min(
            row["forced_gamma_share_lower_bound"] for row in rows
        ),
        "global_min_signature_signal_minus_ambiguous_budget": min(
            row["signature_signal_minus_ambiguous_budget"] for row in rows
        ),
        "global_min_signature_signal_to_ambiguity_ratio": min(
            row["signature_signal_to_ambiguity_ratio"] for row in rows
        ),
        "global_min_ambiguous_escape_bucket_lower_bound": min(
            row["ambiguous_escape_bucket_lower_bound"]
            for row in rows
            if row["ambiguous_escape_bucket_lower_bound"] is not None
        ),
        "kind_summary": [
            summarize_kind(kind, [row for row in rows if row["bucket_kind"] == kind])
            for kind in sorted({row["bucket_kind"] for row in rows})
        ],
        "rows": rows,
        "structural_law": (
            "写 Gamma=Gamma_forced union Gamma_amb，且 Gamma_amb 的质量至多为 aD。"
            "任何超过 a 预算的持久有限签名都不能纯由选择自由解释，其持久部分必须来自 forced fiber 主体，"
            "于是路由到 MFU/PDEC。若没有有限签名在 a 预算以上持久，则剩余责任是小自由度、多桶、分散的，"
            "准入 CleanKLS/DLS。"
        ),
        "review_conclusion": (
            "ForcedCap 的 Gamma 自由度已压到小预算后，48 个有限层 phase-bucket 签名行全部满足 "
            "`signature_signal > ambiguous_budget`。因此下一步不再是寻找新的 exposure 统计，"
            "而是证明实际 Gamma 若持久命中这些签名则进入 PDEC；若不持久，则小 ambiguous 分散残余进入 CleanKLS/DLS。"
        ),
    }


def summarize_kind(kind: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    """按 bucket 类型汇总。"""
    return {
        "bucket_kind": kind,
        "row_count": len(rows),
        "min_normalized_signature_signal": min(
            row["normalized_signature_signal"] for row in rows
        ),
        "max_ambiguous_gamma_share_upper_bound": max(
            row["ambiguous_gamma_share_upper_bound"] for row in rows
        ),
        "min_signature_signal_minus_ambiguous_budget": min(
            row["signature_signal_minus_ambiguous_budget"] for row in rows
        ),
        "min_signature_signal_to_ambiguity_ratio": min(
            row["signature_signal_to_ambiguity_ratio"] for row in rows
        ),
        "min_actual_buckets_by_fiber": min(
            row["min_actual_buckets_by_fiber"] for row in rows
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    if math.isinf(value):
        return "inf"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Forced Gamma 签名路由器",
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
        "Gamma = Gamma_forced union Gamma_amb；",
        "|Gamma_amb| <= aD；",
        "persistent finite signature mass > aD",
        "  => 不能只由 ambiguous choice 解释，必须含 forced fiber 主体，进入 MFU/PDEC；",
        "no persistent finite signature above aD",
        "  => 小 ambiguous 多桶分散，进入 CleanKLS/DLS。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `forced_cap_count={result['forced_cap_count']}`。",
        f"- `signature_matrix_row_count={result['signature_matrix_row_count']}`。",
        f"- `missing_key_count={result['missing_key_count']}`。",
        f"- `route_counts={result['route_counts']}`。",
        f"- `all_rows_routed_to_forced_signature_or_small_ambiguous_clean={result['all_rows_routed_to_forced_signature_or_small_ambiguous_clean']}`。",
        f"- `global_max_ambiguous_gamma_share_upper_bound={fmt_float(result['global_max_ambiguous_gamma_share_upper_bound'])}`。",
        f"- `global_min_forced_gamma_share_lower_bound={fmt_float(result['global_min_forced_gamma_share_lower_bound'])}`。",
        f"- `global_min_signature_signal_minus_ambiguous_budget={fmt_float(result['global_min_signature_signal_minus_ambiguous_budget'])}`。",
        f"- `global_min_signature_signal_to_ambiguity_ratio={fmt_float(result['global_min_signature_signal_to_ambiguity_ratio'])}`。",
        f"- `global_min_ambiguous_escape_bucket_lower_bound={result['global_min_ambiguous_escape_bucket_lower_bound']}`。",
        "",
        "## 3. Bucket 类型汇总",
        "",
        "| bucket kind | rows | min signal | max ambiguous | min margin | min ratio | min fiber buckets |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["kind_summary"]:
        lines.append(
            "| {kind} | {rows} | {signal} | {amb} | {margin} | {ratio} | {buckets} |".format(
                kind=row["bucket_kind"],
                rows=row["row_count"],
                signal=fmt_float(row["min_normalized_signature_signal"]),
                amb=fmt_float(row["max_ambiguous_gamma_share_upper_bound"]),
                margin=fmt_float(row["min_signature_signal_minus_ambiguous_budget"]),
                ratio=fmt_float(row["min_signature_signal_to_ambiguity_ratio"]),
                buckets=row["min_actual_buckets_by_fiber"],
            )
        )
    lines.extend(
        [
            "",
            "## 4. 行明细",
            "",
            "| P | alpha | h | dir | kind | signal | ambiguous | margin | ratio | fiber buckets | route |",
            "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {p} | {alpha} | {h} | {direction} | {kind} | {signal} | {amb} | {margin} | {ratio} | {buckets} | `{route}` |".format(
                p=row["p"],
                alpha=fmt_float(row["alpha"]),
                h=row["h"],
                direction=fmt_float(row["direction"]),
                kind=row["bucket_kind"],
                signal=fmt_float(row["normalized_signature_signal"]),
                amb=fmt_float(row["ambiguous_gamma_share_upper_bound"]),
                margin=fmt_float(row["signature_signal_minus_ambiguous_budget"]),
                ratio=fmt_float(row["signature_signal_to_ambiguity_ratio"]),
                buckets=row["min_actual_buckets_by_fiber"],
                route=row["route"],
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mfu-json", type=Path, default=DEFAULT_MFU)
    parser.add_argument("--fiber-json", type=Path, default=DEFAULT_FIBER)
    parser.add_argument("--fiber-dominance-json", type=Path, default=DEFAULT_FIBER_DOMINANCE)
    parser.add_argument("--gamma-freedom-json", type=Path, default=DEFAULT_GAMMA_FREEDOM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        mfu_path=args.mfu_json,
        fiber_path=args.fiber_json,
        fiber_dominance_path=args.fiber_dominance_json,
        gamma_freedom_path=args.gamma_freedom_json,
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
                "signature_matrix_row_count": result["signature_matrix_row_count"],
                "all_rows_routed": result[
                    "all_rows_routed_to_forced_signature_or_small_ambiguous_clean"
                ],
                "global_min_signature_signal_minus_ambiguous_budget": result[
                    "global_min_signature_signal_minus_ambiguous_budget"
                ],
                "global_min_signature_signal_to_ambiguity_ratio": result[
                    "global_min_signature_signal_to_ambiguity_ratio"
                ],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
