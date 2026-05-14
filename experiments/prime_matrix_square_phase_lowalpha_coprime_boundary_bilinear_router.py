#!/usr/bin/env python3
"""把 coprime boundary lcm edge 化为双线性平衡块。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "CoprimeBoundaryBilinearDispersionBlocksOrEndpointPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json",
    "prime-matrix-square-phase-lowalpha-vector-pdec-unified-obligation-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def collect_values_and_primes(p_list: list[int]) -> tuple[list[int], list[int]]:
    """复用 Selberg 归因账本的 prime-a b 序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = attribution.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = attribution.envelope.primes_from_flags(flags, trial_limit)
    values = attribution.selberg.collect_values(p_list, flags, trial_primes)
    return values, trial_primes


def balance_bucket(d: int, e: int) -> str:
    """按 `max(d,e)/min(d,e)` 给 coprime 边分桶。"""
    ratio = max(d, e) / min(d, e)
    if ratio <= 2:
        return "balanced<=2"
    if ratio <= 4:
        return "mid<=4"
    if ratio <= 8:
        return "unbalanced<=8"
    return "far>8"


def empty_bucket(label: str) -> dict[str, Any]:
    """初始化桶。"""
    return {
        "bucket": label,
        "edge_count": 0,
        "positive_edge_count": 0,
        "signed_contribution": 0.0,
        "abs_contribution": 0.0,
        "weight_abs": 0.0,
    }


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """计算单个 z 的 coprime boundary 双线性平衡块。"""
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    coeffs = attribution.coefficient_by_lcm(weights)
    counts = attribution.divisibility_counts(values, sorted(coeffs))
    remainders = {m: counts[m] - len(values) / m for m in coeffs}
    buckets = {name: empty_bucket(name) for name in ["balanced<=2", "mid<=4", "unbalanced<=8", "far>8"]}
    total = empty_bucket("total")
    for d, lambda_d in weights.items():
        for e, lambda_e in weights.items():
            if math.gcd(d, e) != 1:
                continue
            modulus = d * e
            if modulus <= d_level or modulus > overflow_multiplier * d_level:
                continue
            contribution = lambda_d * lambda_e * remainders[modulus]
            bucket = buckets[balance_bucket(d, e)]
            for row in (bucket, total):
                row["edge_count"] += 1
                row["positive_edge_count"] += 1 if contribution >= 0 else 0
                row["signed_contribution"] += contribution
                row["abs_contribution"] += abs(contribution)
                row["weight_abs"] += abs(lambda_d * lambda_e)
    for row in [total, *buckets.values()]:
        row["signed_over_abs"] = safe_ratio(abs(row["signed_contribution"]), row["abs_contribution"])
        row["abs_share_of_total"] = safe_ratio(row["abs_contribution"], total["abs_contribution"])
    return {
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "identity": "sum_{(d,e)=1,D<de<=MD} lambda_d lambda_e R_de",
        "total": total,
        "balance_buckets": list(buckets.values()),
        "dominant_bucket": max(buckets.values(), key=lambda row: row["abs_contribution"], default=None),
    }


def audit(p_list: list[int], z_list: list[int], d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行 coprime boundary 双线性分解。"""
    values, primes = collect_values_and_primes(p_list)
    rows = [row_for_z(values, primes, z, d_level, overflow_multiplier) for z in z_list]
    active_rows = [row for row in rows if row["total"]["edge_count"] > 0]
    worst_signed_bucket = None
    all_buckets = []
    for row in active_rows:
        for bucket in row["balance_buckets"]:
            if bucket["edge_count"] > 0:
                all_buckets.append({"z": row["z"], **bucket})
    if all_buckets:
        worst_signed_bucket = max(all_buckets, key=lambda row: row["signed_over_abs"] or 0.0)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router",
        "status": "coprime_boundary_bilinear_balance_blocks_materialized_bounds_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "coprime_boundary_bilinear_identity_closed": True,
        "balance_block_ledger_materialized": True,
        "balanced_bilinear_dispersion_bound_proved": False,
        "unbalanced_endpoint_pdec_excluded": False,
        "coprime_boundary_edge_angle_bound_proved": False,
        "row_column_unconditional_closed": False,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "value_count": len(values),
        "rows": rows,
        "worst_signed_bucket": worst_signed_bucket,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "coprime boundary lcm edge 已化为双线性形式 "
            "`sum_{(d,e)=1,D<de<=16D} lambda_d lambda_e R_de`。"
            "按 `max(d,e)/min(d,e)` 拆成 balanced/mid/unbalanced/far 四块后，"
            "失败只能来自 balanced 双线性离散偏差或 unbalanced endpoint PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha coprime boundary 双线性路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"coprime_boundary_bilinear_identity_closed={fmt_bool(result['coprime_boundary_bilinear_identity_closed'])}",
        f"balance_block_ledger_materialized={fmt_bool(result['balance_block_ledger_materialized'])}",
        f"balanced_bilinear_dispersion_bound_proved={fmt_bool(result['balanced_bilinear_dispersion_bound_proved'])}",
        f"unbalanced_endpoint_pdec_excluded={fmt_bool(result['unbalanced_endpoint_pdec_excluded'])}",
        f"coprime_boundary_edge_angle_bound_proved={fmt_bool(result['coprime_boundary_edge_angle_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 双线性平衡块",
        "",
        "| z | bucket | edges | positive | abs | signed | signed/abs | abs share |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        for bucket in row["balance_buckets"]:
            lines.append(
                f"| {row['z']} | `{bucket['bucket']}` | {bucket['edge_count']} | "
                f"{bucket['positive_edge_count']} | {fmt_float(bucket['abs_contribution'])} | "
                f"{fmt_float(bucket['signed_contribution'])} | {fmt_float(bucket['signed_over_abs'])} | "
                f"{fmt_float(bucket['abs_share_of_total'])} |"
            )
    worst = result["worst_signed_bucket"]
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：coprime boundary edge 的双线性恒等式。",
            "- 已物化：balanced/mid/unbalanced/far 四类平衡块。",
            "- 未闭合：balanced/mid 块的双线性离散偏差界。",
            "- 未闭合：unbalanced/far 块的 endpoint PDEC 排斥或吸收。",
        ]
    )
    if worst is not None:
        lines.append(
            f"- 当前样本最大 signed/abs 桶为 `z={worst['z']}, {worst['bucket']}`，值 "
            f"`{fmt_float(worst['signed_over_abs'])}`。"
        )
    lines.extend(
        [
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z-list", default=",".join(str(item) for item in DEFAULT_Z_LIST))
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--overflow-multiplier", type=int, default=DEFAULT_OVERFLOW_MULTIPLIER)
    args = parser.parse_args()
    result = audit(
        parse_int_list(args.p_list),
        parse_int_list(args.z_list),
        args.d_level,
        args.overflow_multiplier,
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
