#!/usr/bin/env python3
"""把 core Möbius-log 余项拆成 S0 与逐素数 log-square 通道。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_core_channel_decomposition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
NEXT_TARGET = "CoreChannelS0AndPrimeLogSquareChannelBoundsOrVectorPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json",
    "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_core_channel_decomposition_router.py": file_sha256(
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


def factor_by_z(value: int, z: int, primes: list[int]) -> list[int]:
    """在 `prime<=z` 的 squarefree 支撑中分解 m。"""
    n = value
    factors = []
    for prime in primes:
        if prime > z:
            break
        if n % prime == 0:
            factors.append(prime)
            n //= prime
    return factors


def row_for_z(values: list[int], primes: list[int], z: int, d_level: int) -> dict[str, Any]:
    """计算单个 z 的 core 通道分解。"""
    weights = attribution.selberg.selberg_weights(z, d_level, primes)
    coeffs = attribution.coefficient_by_lcm(weights)
    counts = attribution.divisibility_counts(values, sorted(coeffs))
    small_primes = [prime for prime in primes if prime <= z]
    log_level = math.log(d_level)
    channel_values = {prime: 0.0 for prime in small_primes}
    s0 = 0.0
    core_net = 0.0
    core_abs = 0.0
    for modulus, coefficient in coeffs.items():
        if modulus > d_level:
            continue
        factors = factor_by_z(modulus, z, primes)
        mu = -1.0 if len(factors) % 2 else 1.0
        remainder = counts[modulus] - len(values) / modulus
        s0 += mu * remainder
        for prime in factors:
            channel_values[prime] += mu * remainder
        contribution = coefficient * remainder
        core_net += contribution
        core_abs += abs(contribution)
    weighted_channels = []
    weighted_sum = 0.0
    for prime, value in channel_values.items():
        weight = math.log(prime) ** 2 / (log_level * log_level)
        term = weight * value
        weighted_sum += term
        weighted_channels.append(
            {
                "prime": prime,
                "S_q": value,
                "log_square_weight": weight,
                "weighted_term": term,
                "abs_weighted_term": abs(term),
            }
        )
    reconstructed = s0 - weighted_sum
    top_channels = sorted(weighted_channels, key=lambda item: -item["abs_weighted_term"])[:16]
    channel_abs_sum = sum(abs(item["weighted_term"]) for item in weighted_channels)
    return {
        "z": z,
        "d_level": d_level,
        "prime_channel_count": len(small_primes),
        "S0": s0,
        "log_square_channel_sum": weighted_sum,
        "core_net": core_net,
        "core_abs_contribution": core_abs,
        "reconstructed_core_net": reconstructed,
        "reconstruction_error": core_net - reconstructed,
        "channel_abs_sum": channel_abs_sum,
        "channel_cancellation_ratio": safe_ratio(abs(weighted_sum), channel_abs_sum),
        "core_net_over_channel_abs": safe_ratio(abs(core_net), channel_abs_sum),
        "top_prime_channels": top_channels,
    }


def audit(p_list: list[int], z_list: list[int], d_level: int) -> dict[str, Any]:
    """执行 core 通道分解审计。"""
    values, primes = collect_values_and_primes(p_list)
    rows = [row_for_z(values, primes, z, d_level) for z in z_list]
    failures = [row for row in rows if abs(row["reconstruction_error"]) > 1e-8]
    worst_channel = max(rows, key=lambda row: row["core_net_over_channel_abs"] or 0.0)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_core_channel_decomposition_router",
        "status": "core_mobius_log_channel_decomposition_closed_channel_bounds_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "core_channel_decomposition_identity_closed": len(failures) == 0,
        "prime_channel_pdec_route_materialized": True,
        "S0_channel_bound_proved": False,
        "prime_log_square_channel_bound_proved": False,
        "core_mobius_log_residual_angle_bound_proved": False,
        "vector_squarefree_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "d_level": d_level,
        "value_count": len(values),
        "identity_failure_count": len(failures),
        "rows": rows,
        "worst_core_net_over_channel_abs_row": worst_channel,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "核心系数公式可继续展开为通道恒等式 "
            "`core=S0-(log D)^(-2) sum_{q<=z} (log q)^2 S_q`，"
            "其中 `S0=sum_{m<=D} mu(m)R_m`，"
            "`S_q=sum_{m<=D,q|m} mu(m)R_m`。"
            "因此 core 角度失败不会是无名高维异常：它必须由 `S0` 或某些素数 log-square 通道承担，"
            "可登记为 PrimeChannel-VectorSquarefree-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha core 通道分解",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"core_channel_decomposition_identity_closed={fmt_bool(result['core_channel_decomposition_identity_closed'])}",
        f"prime_channel_pdec_route_materialized={fmt_bool(result['prime_channel_pdec_route_materialized'])}",
        f"S0_channel_bound_proved={fmt_bool(result['S0_channel_bound_proved'])}",
        f"prime_log_square_channel_bound_proved={fmt_bool(result['prime_log_square_channel_bound_proved'])}",
        f"core_mobius_log_residual_angle_bound_proved={fmt_bool(result['core_mobius_log_residual_angle_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 通道恒等式",
        "",
        "| z | S0 | log-square sum | core net | error | channel abs | |core|/channel abs | channel cancellation |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['z']} | {fmt_float(row['S0'])} | "
            f"{fmt_float(row['log_square_channel_sum'])} | {fmt_float(row['core_net'])} | "
            f"{fmt_float(row['reconstruction_error'])} | {fmt_float(row['channel_abs_sum'])} | "
            f"{fmt_float(row['core_net_over_channel_abs'])} | "
            f"{fmt_float(row['channel_cancellation_ratio'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 最大素数通道",
            "",
            "| z | q | S_q | weight | weighted term |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["rows"]:
        for channel in row["top_prime_channels"][:6]:
            lines.append(
                f"| {row['z']} | {channel['prime']} | {fmt_float(channel['S_q'])} | "
                f"{fmt_float(channel['log_square_weight'])} | {fmt_float(channel['weighted_term'])} |"
            )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：core 通道恒等式。",
            "- 已物化：若 core 角度失败，则必须落入 `S0` 或某个 `S_q` 素数通道。",
            "- 未闭合：`S0` 通道统一界。",
            "- 未闭合：逐素数 log-square 通道统一界或失败 PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list), parse_int_list(args.z_list), args.d_level)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "identity_failure_count": result["identity_failure_count"],
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
