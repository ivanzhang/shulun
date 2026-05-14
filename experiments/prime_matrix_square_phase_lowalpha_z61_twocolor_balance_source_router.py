#!/usr/bin/env python3
"""下钻 z=61 局部块两色平衡的符号来源。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_coprime_boundary_bilinear_router as bilinear
import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
BILINEAR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json"
TWOCOLOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z = 61
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_OVERFLOW_MULTIPLIER = 16
NEXT_TARGET = "Z61MobiusSliceRemainderSignBalanceTheta0222OrLocalizedBlockPDEC"
BUCKETS = ["balanced<=2", "mid<=4", "unbalanced<=8", "far>8"]
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-localized-block-twocolor-balance-router.json",
    "prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def mobius_sign_squarefree(value: int, primes: list[int]) -> int:
    """返回 squarefree 数的 Möbius 符号；若非 squarefree 则返回 0。"""
    remaining = value
    omega = 0
    for prime in primes:
        if prime * prime > remaining:
            break
        if remaining % prime != 0:
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent > 1:
            return 0
        omega += 1
    if remaining > 1:
        omega += 1
    return -1 if omega % 2 else 1


def collect_values_and_primes(p_list: list[int]) -> tuple[list[int], list[int]]:
    """复用 Selberg 归因账本的 prime-a b 多重序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = attribution.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = attribution.envelope.primes_from_flags(flags, trial_limit)
    values = attribution.selberg.collect_values(p_list, flags, trial_primes)
    return values, trial_primes


def required_cap_for_z(z: int) -> float:
    """读取 z 的 signed-ratio cap。"""
    data = json.loads(TWOCOLOR_JSON.read_text(encoding="utf-8"))
    rows = [row for row in data["rows"] if int(row["z"]) == z]
    if not rows:
        raise ValueError(f"缺少 z={z} 的 two-color 合同")
    caps = {float(row["signed_ratio_cap"]) for row in rows}
    if len(caps) != 1:
        raise ValueError(f"z={z} 的 signed cap 不唯一: {caps}")
    return caps.pop()


def source_bucket_by_name(z: int) -> dict[str, dict[str, Any]]:
    """读取上一层 bucket 账本，用于恒等式校验。"""
    data = json.loads(BILINEAR_JSON.read_text(encoding="utf-8"))
    for row in data["rows"]:
        if int(row["z"]) == z:
            return {bucket["bucket"]: bucket for bucket in row["balance_buckets"]}
    raise ValueError(f"缺少 z={z} 的 bilinear bucket")


def build_modulus_weights(
    weights: dict[int, float], z: int, d_level: int, overflow_multiplier: int, primes: list[int]
) -> tuple[dict[str, dict[int, float]], dict[str, dict[str, Any]], dict[str, Any]]:
    """把边级权重聚合到同一模数 m=de。"""
    bucket_weights: dict[str, dict[int, float]] = {bucket: defaultdict(float) for bucket in BUCKETS}
    edge_stats = {
        bucket: {
            "edge_count": 0,
            "positive_lambda_edge_count": 0,
            "coefficient_sign_mismatch_count": 0,
            "non_squarefree_modulus_count": 0,
        }
        for bucket in BUCKETS
    }
    global_stats = {
        "edge_count": 0,
        "coefficient_sign_mismatch_count": 0,
        "non_squarefree_modulus_count": 0,
    }
    for d, lambda_d in weights.items():
        for e, lambda_e in weights.items():
            if math.gcd(d, e) != 1:
                continue
            modulus = d * e
            if modulus <= d_level or modulus > overflow_multiplier * d_level:
                continue
            bucket = bilinear.balance_bucket(d, e)
            lambda_product = lambda_d * lambda_e
            lambda_abs = abs(lambda_product)
            mu = mobius_sign_squarefree(modulus, primes)
            lambda_sign = 1 if lambda_product >= 0 else -1
            edge_stats[bucket]["edge_count"] += 1
            edge_stats[bucket]["positive_lambda_edge_count"] += 1 if lambda_product >= 0 else 0
            global_stats["edge_count"] += 1
            if mu == 0:
                edge_stats[bucket]["non_squarefree_modulus_count"] += 1
                global_stats["non_squarefree_modulus_count"] += 1
            elif lambda_abs > 0 and lambda_sign != mu:
                edge_stats[bucket]["coefficient_sign_mismatch_count"] += 1
                global_stats["coefficient_sign_mismatch_count"] += 1
            bucket_weights[bucket][modulus] += lambda_abs
    return bucket_weights, edge_stats, global_stats


def summarize_bucket(
    bucket: str,
    modulus_weights: dict[int, float],
    remainders: dict[int, float],
    primes: list[int],
    cap: float,
    source_bucket: dict[str, Any],
    edge_stat: dict[str, Any],
) -> dict[str, Any]:
    """汇总单个 bucket 的 Möbius 切片两色账本。"""
    quadrants = {
        "mu_plus_R_plus": 0.0,
        "mu_plus_R_minus": 0.0,
        "mu_minus_R_plus": 0.0,
        "mu_minus_R_minus": 0.0,
    }
    signed = 0.0
    abs_sum = 0.0
    positive_mass = 0.0
    negative_mass = 0.0
    top_moduli = []
    for modulus, weight_abs in sorted(modulus_weights.items()):
        mu = mobius_sign_squarefree(modulus, primes)
        remainder = remainders[modulus]
        contribution = mu * weight_abs * remainder
        mass = abs(weight_abs * remainder)
        signed += contribution
        abs_sum += mass
        if contribution >= 0:
            positive_mass += mass
        else:
            negative_mass += mass
        if mu > 0 and remainder >= 0:
            quadrants["mu_plus_R_plus"] += mass
        elif mu > 0:
            quadrants["mu_plus_R_minus"] += mass
        elif remainder >= 0:
            quadrants["mu_minus_R_plus"] += mass
        else:
            quadrants["mu_minus_R_minus"] += mass
        top_moduli.append(
            {
                "m": modulus,
                "mu": mu,
                "weight_abs": weight_abs,
                "remainder": remainder,
                "contribution": contribution,
                "abs_mass": mass,
            }
        )
    plus_slice_imbalance = abs(quadrants["mu_plus_R_plus"] - quadrants["mu_plus_R_minus"])
    minus_slice_imbalance = abs(quadrants["mu_minus_R_minus"] - quadrants["mu_minus_R_plus"])
    slice_imbalance_sum = plus_slice_imbalance + minus_slice_imbalance
    signed_ratio = safe_ratio(abs(signed), abs_sum)
    slice_imbalance_ratio = safe_ratio(slice_imbalance_sum, abs_sum)
    two_color_ratio = safe_ratio(max(positive_mass, negative_mass), min(positive_mass, negative_mass))
    required_two_color_ratio = (1.0 + cap) / (1.0 - cap)
    sorted_top = sorted(top_moduli, key=lambda row: row["abs_mass"], reverse=True)[:10]
    for row in sorted_top:
        row["abs_share"] = safe_ratio(row["abs_mass"], abs_sum)
    return {
        "bucket": bucket,
        "edge_count": edge_stat["edge_count"],
        "positive_lambda_edge_count": edge_stat["positive_lambda_edge_count"],
        "modulus_count": len(modulus_weights),
        "signed_contribution": signed,
        "abs_contribution": abs_sum,
        "positive_mass": positive_mass,
        "negative_mass": negative_mass,
        "signed_ratio": signed_ratio,
        "signed_ratio_cap": cap,
        "signed_ratio_slack": None if signed_ratio is None else cap - signed_ratio,
        "two_color_ratio": two_color_ratio,
        "required_two_color_ratio": required_two_color_ratio,
        "two_color_ratio_slack": None if two_color_ratio is None else required_two_color_ratio - two_color_ratio,
        "quadrants": quadrants,
        "mu_plus_slice_abs": quadrants["mu_plus_R_plus"] + quadrants["mu_plus_R_minus"],
        "mu_minus_slice_abs": quadrants["mu_minus_R_plus"] + quadrants["mu_minus_R_minus"],
        "mu_plus_slice_imbalance": plus_slice_imbalance,
        "mu_minus_slice_imbalance": minus_slice_imbalance,
        "slice_imbalance_sum": slice_imbalance_sum,
        "slice_imbalance_ratio": slice_imbalance_ratio,
        "slice_contract_slack": None if slice_imbalance_ratio is None else cap - slice_imbalance_ratio,
        "slice_contract_sample_passes": slice_imbalance_ratio is not None and slice_imbalance_ratio <= cap,
        "edge_signed_identity_error": signed - float(source_bucket["signed_contribution"]),
        "edge_abs_identity_error": abs_sum - float(source_bucket["abs_contribution"]),
        "coefficient_sign_mismatch_count": edge_stat["coefficient_sign_mismatch_count"],
        "non_squarefree_modulus_count": edge_stat["non_squarefree_modulus_count"],
        "top_moduli_by_abs_mass": sorted_top,
    }


def audit(p_list: list[int], z: int, d_level: int, overflow_multiplier: int) -> dict[str, Any]:
    """执行 z=61 两色平衡符号来源审计。"""
    values, primes = collect_values_and_primes(p_list)
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    bucket_weights, edge_stats, global_edge_stats = build_modulus_weights(weights, z, d_level, overflow_multiplier, primes)
    moduli = sorted({modulus for weights_by_modulus in bucket_weights.values() for modulus in weights_by_modulus})
    counts = attribution.divisibility_counts(values, moduli)
    remainders = {modulus: counts[modulus] - len(values) / modulus for modulus in moduli}
    cap = required_cap_for_z(z)
    source_buckets = source_bucket_by_name(z)
    rows = [
        summarize_bucket(bucket, bucket_weights[bucket], remainders, primes, cap, source_buckets[bucket], edge_stats[bucket])
        for bucket in BUCKETS
    ]
    identity_failures = [
        row
        for row in rows
        if abs(row["edge_signed_identity_error"]) > 1e-8 or abs(row["edge_abs_identity_error"]) > 1e-8
    ]
    slice_failures = [row for row in rows if not row["slice_contract_sample_passes"]]
    tightest_slice = min(rows, key=lambda row: row["slice_contract_slack"] if row["slice_contract_slack"] is not None else 10**9)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_twocolor_balance_source_router",
        "status": "z61_twocolor_balance_reduced_to_mobius_slice_remainder_balance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "z": z,
        "d_level": d_level,
        "overflow_multiplier": overflow_multiplier,
        "value_count": len(values),
        "exact_modulus_aggregation_identity_closed": len(identity_failures) == 0,
        "coefficient_sign_equals_mobius_closed": global_edge_stats["coefficient_sign_mismatch_count"] == 0,
        "all_boundary_moduli_squarefree_closed": global_edge_stats["non_squarefree_modulus_count"] == 0,
        "cancellation_free_mobius_slice_contract_materialized": True,
        "sample_satisfies_mobius_slice_contract": len(slice_failures) == 0,
        "mobius_slice_remainder_sign_balance_proved": False,
        "localized_block_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "edge_stats": global_edge_stats,
        "rows": rows,
        "identity_failure_count": len(identity_failures),
        "slice_contract_sample_failure_count": len(slice_failures),
        "tightest_slice_contract_row": tightest_slice,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "z=61 的每个局部块贡献可精确聚合为 "
            "`sum_m mu(m) W_bucket(m) R_m`，其中 `W_bucket(m)>=0`。"
            "因此两色平衡的真正符号来源不是边级随机性，而是 Möbius 奇偶切片中 "
            "`R_m=A_m-N/m` 的正负质量平衡。"
            "若能证明每个 bucket 的切片不平衡和不超过 signed cap，"
            "则不用依赖正负切片之间的偶然抵消即可闭合 z=61 cap；"
            "若失败，则失败模数簇就是 LocalizedBlock-PDEC 证书。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 两色平衡符号来源",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_modulus_aggregation_identity_closed={fmt_bool(result['exact_modulus_aggregation_identity_closed'])}",
        f"coefficient_sign_equals_mobius_closed={fmt_bool(result['coefficient_sign_equals_mobius_closed'])}",
        f"all_boundary_moduli_squarefree_closed={fmt_bool(result['all_boundary_moduli_squarefree_closed'])}",
        f"cancellation_free_mobius_slice_contract_materialized={fmt_bool(result['cancellation_free_mobius_slice_contract_materialized'])}",
        f"sample_satisfies_mobius_slice_contract={fmt_bool(result['sample_satisfies_mobius_slice_contract'])}",
        f"mobius_slice_remainder_sign_balance_proved={fmt_bool(result['mobius_slice_remainder_sign_balance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 聚合恒等式",
        "",
        "在 coprime boundary 中有 `(d,e)=1` 且 `m=de`，所以",
        "",
        "```text",
        "lambda_d lambda_e = mu(d)mu(e)|lambda_d lambda_e| = mu(m)|lambda_d lambda_e|",
        "Block_b = sum_m mu(m) W_b(m) R_m,  W_b(m)=sum_{de=m, bucket=b}|lambda_d lambda_e|.",
        "```",
        "",
        "这把边级两色问题压缩成同模数 `m` 上的 Möbius 切片余项符号平衡。",
        "",
        "## 2. z=61 bucket 账本",
        "",
        "| bucket | moduli | signed/abs | cap | slice ratio | slice slack | two-color | required | id err |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| `{row['bucket']}` | {row['modulus_count']} | {fmt_float(row['signed_ratio'])} | "
            f"{fmt_float(row['signed_ratio_cap'])} | {fmt_float(row['slice_imbalance_ratio'])} | "
            f"{fmt_float(row['slice_contract_slack'])} | {fmt_float(row['two_color_ratio'])} | "
            f"{fmt_float(row['required_two_color_ratio'])} | {fmt_float(row['edge_signed_identity_error'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. Möbius 切片四象限",
            "",
            "| bucket | mu+ R+ | mu+ R- | mu- R+ | mu- R- | plus imbalance | minus imbalance |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["rows"]:
        q = row["quadrants"]
        lines.append(
            f"| `{row['bucket']}` | {fmt_float(q['mu_plus_R_plus'])} | "
            f"{fmt_float(q['mu_plus_R_minus'])} | {fmt_float(q['mu_minus_R_plus'])} | "
            f"{fmt_float(q['mu_minus_R_minus'])} | {fmt_float(row['mu_plus_slice_imbalance'])} | "
            f"{fmt_float(row['mu_minus_slice_imbalance'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：边级贡献到同模数 `m=de` 的精确聚合恒等式。",
            "- 已闭合：coprime 边上 `lambda_d lambda_e` 的符号等于 `mu(m)`。",
            "- 已物化：不依赖跨切片抵消的充分合同 `slice_imbalance_ratio<=cap`。",
            "- 未闭合：全局证明每个 bucket 的 Möbius 切片余项符号平衡。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 最大质量模数",
            "",
        ]
    )
    for row in result["rows"]:
        lines.extend(
            [
                f"### `{row['bucket']}`",
                "",
                "| m | mu | W | R_m | contribution | abs share |",
                "| ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for top in row["top_moduli_by_abs_mass"]:
            lines.append(
                f"| {top['m']} | {top['mu']} | {fmt_float(top['weight_abs'])} | "
                f"{fmt_float(top['remainder'])} | {fmt_float(top['contribution'])} | "
                f"{fmt_float(top['abs_share'])} |"
            )
        lines.append("")
    lines.extend(
        [
            "## 6. 依赖哈希",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z", type=int, default=DEFAULT_Z)
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--overflow-multiplier", type=int, default=DEFAULT_OVERFLOW_MULTIPLIER)
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), args.z, args.d_level, args.overflow_multiplier)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "exact_modulus_aggregation_identity_closed": result["exact_modulus_aggregation_identity_closed"],
                "sample_satisfies_mobius_slice_contract": result["sample_satisfies_mobius_slice_contract"],
                "tightest_bucket": result["tightest_slice_contract_row"]["bucket"],
                "tightest_slice_slack": result["tightest_slice_contract_row"]["slice_contract_slack"],
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
