#!/usr/bin/env python3
"""审计 fixed-b q-scan 的短区间除数乘积封套。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_fixed_b_divisor_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-divisor-envelope-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-divisor-envelope-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-divisor-envelope-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_fixed_b_qscan_router as qscan


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-fixed-b-divisor-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-fixed-b-divisor-envelope-router.md"

DEFAULT_P_LIST = qscan.DEFAULT_P_LIST
NEXT_TARGET = "SemiprimeIncidenceOnFixedBShortIntervalsSelbergOrPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.json",
    "prime-matrix-square-phase-lowalpha-occupied-b-collision-geometry-router.json",
]

normal = qscan.normal
envelope = qscan.envelope


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
        "experiments/prime_matrix_square_phase_lowalpha_fixed_b_divisor_envelope_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def interval_bounds_for_b(p: int, b: int) -> tuple[int, int]:
    """返回固定 b 的整数区间 J_b。"""
    p2 = p * p
    return p2 // b + 1, (p2 + p - 1) // b


def log_interval_product(left: int, right: int) -> float:
    """计算短区间整数乘积的对数。"""
    if right < left:
        return 0.0
    return sum(math.log(n) for n in range(left, right + 1))


def divisor_envelope_for_b(p: int, b: int) -> dict[str, Any]:
    """给出固定 b 的确定性除数乘积封套。"""
    left, right = interval_bounds_for_b(p, b)
    interval_capacity = max(0, right - left + 1)
    q_lower = p * p // (b * b) + 1
    log_product = log_interval_product(left, right)
    if q_lower <= 1 or log_product <= 0:
        envelope_bound = 0
    else:
        envelope_bound = math.floor(log_product / math.log(q_lower))
    return {
        "b": b,
        "n_interval": [left, right],
        "n_interval_capacity": interval_capacity,
        "n_interval_width": p / b,
        "q_lower_from_a_le_b": q_lower,
        "log_interval_product": log_product,
        "divisor_product_envelope": envelope_bound,
    }


def collect_qscan_by_b(
    p: int,
    flags: bytearray,
    trial_primes: list[int],
) -> tuple[dict[int, list[dict[str, Any]]], dict[int, list[dict[str, Any]]], dict[int, list[dict[str, Any]]]]:
    """收集 fixed-b q-scan 的 phase、prime-a、prime-b 三层候选。"""
    records = [qscan.collision.decorate_record(p, record) for record in qscan.collision.collect_records_for_p(p, flags, trial_primes)]
    b_values = sorted({int(record["b"]) for record in records})
    active_q = qscan.active_q_axes_for_p(p, flags)
    by_b_phase: dict[int, list[dict[str, Any]]] = defaultdict(list)
    by_b_prime_a: dict[int, list[dict[str, Any]]] = defaultdict(list)
    by_b_prime_b: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for b in b_values:
        for q in active_q:
            candidate = qscan.qscan_candidate(p, b, q, flags, trial_primes)
            if candidate is None:
                continue
            by_b_phase[b].append(candidate)
            if candidate["prime_a"]:
                by_b_prime_a[b].append(candidate)
                if candidate["prime_b"]:
                    by_b_prime_b[b].append(candidate)
    return by_b_phase, by_b_prime_a, by_b_prime_b


def b_summary(
    p: int,
    b: int,
    phase: list[dict[str, Any]],
    prime_a: list[dict[str, Any]],
    prime_b: list[dict[str, Any]],
) -> dict[str, Any]:
    """汇总单个 b 的封套与实际重数。"""
    env = divisor_envelope_for_b(p, b)
    q_values = sorted(candidate["q"] for candidate in phase)
    n_values = sorted(candidate["n"] for candidate in phase)
    return {
        **env,
        "phase_multiplicity": len(phase),
        "prime_a_multiplicity": len(prime_a),
        "prime_b_multiplicity": len(prime_b),
        "phase_over_envelope": safe_ratio(len(phase), env["divisor_product_envelope"]),
        "prime_a_over_phase": safe_ratio(len(prime_a), len(phase)),
        "prime_b_over_prime_a": safe_ratio(len(prime_b), len(prime_a)),
        "envelope_slack": env["divisor_product_envelope"] - len(phase),
        "q_values": q_values[:16],
        "n_values": n_values[:16],
        "sample_phase": phase[:8],
        "sample_prime_a": prime_a[:8],
        "sample_prime_b": prime_b[:8],
    }


def audit_p(p: int, flags: bytearray, trial_primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的 fixed-b 除数封套。"""
    by_b_phase, by_b_prime_a, by_b_prime_b = collect_qscan_by_b(p, flags, trial_primes)
    summaries = [
        b_summary(p, b, phase, by_b_prime_a.get(b, []), by_b_prime_b.get(b, []))
        for b, phase in by_b_phase.items()
    ]
    failures = [item for item in summaries if item["phase_multiplicity"] > item["divisor_product_envelope"]]
    top_phase = max(summaries, key=lambda item: item["phase_multiplicity"], default=None)
    top_prime_a = max(summaries, key=lambda item: item["prime_a_multiplicity"], default=None)
    top_prime_b = max(summaries, key=lambda item: item["prime_b_multiplicity"], default=None)
    tightest = max(
        summaries,
        key=lambda item: item["phase_over_envelope"] or 0.0,
        default=None,
    )
    return {
        "p": p,
        "b_with_phase_count": len(summaries),
        "phase_fibers": sum(item["phase_multiplicity"] for item in summaries),
        "prime_a_fibers": sum(item["prime_a_multiplicity"] for item in summaries),
        "prime_b_fibers": sum(item["prime_b_multiplicity"] for item in summaries),
        "divisor_envelope_sum": sum(item["divisor_product_envelope"] for item in summaries),
        "max_phase_multiplicity": max((item["phase_multiplicity"] for item in summaries), default=0),
        "max_prime_a_multiplicity": max((item["prime_a_multiplicity"] for item in summaries), default=0),
        "max_prime_b_multiplicity": max((item["prime_b_multiplicity"] for item in summaries), default=0),
        "max_divisor_envelope": max((item["divisor_product_envelope"] for item in summaries), default=0),
        "phase_over_envelope_sum": safe_ratio(
            sum(item["phase_multiplicity"] for item in summaries),
            sum(item["divisor_product_envelope"] for item in summaries),
        ),
        "envelope_failure_count": len(failures),
        "top_phase_b": top_phase,
        "top_prime_a_b": top_prime_a,
        "top_prime_b_b": top_prime_b,
        "tightest_envelope_b": tightest,
        "sample_failures": failures[:8],
    }


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行 fixed-b 除数封套审计。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = envelope.primes_from_flags(flags, trial_limit)
    profiles = [audit_p(p, flags, trial_primes) for p in p_list]

    phase_fibers = sum(profile["phase_fibers"] for profile in profiles)
    prime_a_fibers = sum(profile["prime_a_fibers"] for profile in profiles)
    prime_b_fibers = sum(profile["prime_b_fibers"] for profile in profiles)
    envelope_sum = sum(profile["divisor_envelope_sum"] for profile in profiles)
    failure_count = sum(profile["envelope_failure_count"] for profile in profiles)

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_fixed_b_divisor_envelope_router",
        "status": "fixed_b_phase_sparse_reduced_to_divisor_product_envelope_prime_incidence_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "fixed_b_divisor_product_envelope_proved": failure_count == 0,
        "phase_sparse_envelope_failure_count": failure_count,
        "semiprime_incidence_selberg_bound_proved": False,
        "prime_b_spike_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "b_with_phase_count": sum(profile["b_with_phase_count"] for profile in profiles),
        "phase_fibers": phase_fibers,
        "prime_a_fibers": prime_a_fibers,
        "prime_b_fibers": prime_b_fibers,
        "divisor_envelope_sum": envelope_sum,
        "phase_over_envelope_sum": safe_ratio(phase_fibers, envelope_sum),
        "prime_a_over_phase": safe_ratio(prime_a_fibers, phase_fibers),
        "prime_b_over_prime_a": safe_ratio(prime_b_fibers, prime_a_fibers),
        "max_phase_multiplicity": max((profile["max_phase_multiplicity"] for profile in profiles), default=0),
        "max_prime_a_multiplicity": max((profile["max_prime_a_multiplicity"] for profile in profiles), default=0),
        "max_prime_b_multiplicity": max((profile["max_prime_b_multiplicity"] for profile in profiles), default=0),
        "max_divisor_envelope": max((profile["max_divisor_envelope"] for profile in profiles), default=0),
        "top_phase_b": max((profile["top_phase_b"] for profile in profiles), key=lambda item: item["phase_multiplicity"], default=None),
        "top_prime_a_b": max(
            (profile["top_prime_a_b"] for profile in profiles),
            key=lambda item: item["prime_a_multiplicity"],
            default=None,
        ),
        "top_prime_b_b": max(
            (profile["top_prime_b_b"] for profile in profiles),
            key=lambda item: item["prime_b_multiplicity"],
            default=None,
        ),
        "tightest_envelope_b": max(
            (profile["tightest_envelope_b"] for profile in profiles),
            key=lambda item: item["phase_over_envelope"] or 0.0,
            default=None,
        ),
        "profiles": profiles,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "固定 b 后，phase 候选 q 是短区间 J_b=(P^2/b,(P^2+P-1)/b] 内整数的互异素因子。"
            "同时由 a<=b 得 q>P^2/b^2。故所有 phase 候选 q 的乘积整除 J_b 内整数乘积，"
            "并强制 `#q <= log(prod J_b)/log(P^2/b^2)`。样本中该确定性封套零失败。"
            "因此 fixed-b phase 稀疏性已从经验重数压成除数乘积不等式；剩余是对这些短区间中"
            "`n=q*a` 且 a、b 为素数的半素数/双素性 incidence 做 Selberg/Brun 上界，"
            "或把持续尖峰登记为 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha fixed-b 除数封套路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fixed_b_divisor_product_envelope_proved={fmt_bool(result['fixed_b_divisor_product_envelope_proved'])}",
        f"phase_sparse_envelope_failure_count={result['phase_sparse_envelope_failure_count']}",
        f"semiprime_incidence_selberg_bound_proved={fmt_bool(result['semiprime_incidence_selberg_bound_proved'])}",
        f"prime_b_spike_pdec_excluded={fmt_bool(result['prime_b_spike_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全局账本",
        "",
        "| b with phase | phase fibers | envelope sum | phase/envelope | prime-a | prime-a/phase | prime-b | prime-b/prime-a |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['b_with_phase_count']} | {result['phase_fibers']} | "
            f"{result['divisor_envelope_sum']} | {fmt_float(result['phase_over_envelope_sum'])} | "
            f"{result['prime_a_fibers']} | {fmt_float(result['prime_a_over_phase'])} | "
            f"{result['prime_b_fibers']} | {fmt_float(result['prime_b_over_prime_a'])} |"
        ),
        "",
        "## 2. 重数与封套",
        "",
        "| max phase | max prime-a | max prime-b | max divisor envelope | envelope failures |",
        "| ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {result['max_phase_multiplicity']} | {result['max_prime_a_multiplicity']} | "
            f"{result['max_prime_b_multiplicity']} | {result['max_divisor_envelope']} | "
            f"{result['phase_sparse_envelope_failure_count']} |"
        ),
        "",
        "## 3. 关键样本",
        "",
        "| kind | data |",
        "| --- | --- |",
        f"| top phase | `{result['top_phase_b']}` |",
        f"| top prime-a | `{result['top_prime_a_b']}` |",
        f"| top prime-b | `{result['top_prime_b_b']}` |",
        f"| tightest envelope | `{result['tightest_envelope_b']}` |",
        "",
        "## 4. 每个 P 的总结",
        "",
        "| P | phase | envelope | phase/envelope | prime-a | prime-b | max phase | max envelope | failures |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        lines.append(
            f"| {profile['p']} | {profile['phase_fibers']} | {profile['divisor_envelope_sum']} | "
            f"{fmt_float(profile['phase_over_envelope_sum'])} | {profile['prime_a_fibers']} | "
            f"{profile['prime_b_fibers']} | {profile['max_phase_multiplicity']} | "
            f"{profile['max_divisor_envelope']} | {profile['envelope_failure_count']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：固定 `b` 的 phase 候选都是 `J_b` 中整数的互异活跃素因子。",
            "- 已闭合：由 `a<=b` 得每个候选 `q>P^2/b^2`。",
            "- 已闭合：乘积整除给出 `#Q_b <= log(prod_{n in J_b} n)/log(P^2/b^2)`；样本零失败。",
            "- 未闭合：`prime-a` 候选即 `J_b` 中带活跃小素因子与素补因子的半素数 incidence，需要 Selberg/Brun 上界。",
            "- 未闭合：`prime-b` 尖峰的 PDEC/SAE 排除。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "fixed_b_divisor_product_envelope_proved": result[
                    "fixed_b_divisor_product_envelope_proved"
                ],
                "phase_sparse_envelope_failure_count": result["phase_sparse_envelope_failure_count"],
                "phase_fibers": result["phase_fibers"],
                "divisor_envelope_sum": result["divisor_envelope_sum"],
                "max_divisor_envelope": result["max_divisor_envelope"],
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
